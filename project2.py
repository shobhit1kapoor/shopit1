#!/usr/bin/env python3
"""Threaded bank simulation for CS4348 Project 2."""

from collections import deque
import random
import threading
import time

CUSTOMER_COUNT = 50
TELLER_COUNT = 3


class Bank:
    def __init__(self):
        # Binary semaphores protect shared state and keep each output line intact.
        self.dispatch_lock = threading.Semaphore(1)
        self.output_lock = threading.Semaphore(1)

        # Counting semaphores model the bank's limited-capacity resources.
        self.door = threading.Semaphore(2)
        self.manager = threading.Semaphore(1)
        self.safe = threading.Semaphore(2)

        # One permit per customer makes this a one-way "bank is open" gate.
        self.bank_open = threading.Semaphore(0)
        self.waiting_customers = deque()
        self.ready_tellers = deque()
        self.ready_count = 0
        self.opened = False
        self.closing = False

    def log(self, kind, identifier, message, other=None):
        counterpart = f"[{other[0]} {other[1]}]" if other else "[]"
        self.output_lock.acquire()
        try:
            print(f"{kind} {identifier} {counterpart}: {message}", flush=True)
        finally:
            self.output_lock.release()

    def assign(self, teller, customer):
        teller.customer = customer
        customer.teller = teller
        customer.assigned.release()

    def customer_joins_line(self, customer):
        self.dispatch_lock.acquire()
        try:
            if self.ready_tellers:
                teller = self.ready_tellers.popleft()
                self.assign(teller, customer)
            else:
                self.waiting_customers.append(customer)
        finally:
            self.dispatch_lock.release()

    def teller_becomes_ready(self, teller, starting=False):
        """Queue a teller, dispatch a waiting customer, or stop during shutdown."""
        self.dispatch_lock.acquire()
        try:
            if starting:
                self.ready_count += 1

            if self.closing:
                teller.stop = True
                return False

            if self.waiting_customers:
                customer = self.waiting_customers.popleft()
                self.assign(teller, customer)
            else:
                self.ready_tellers.append(teller)

            if starting and self.ready_count == TELLER_COUNT and not self.opened:
                self.opened = True
                self.log("Teller", teller.identifier, "all tellers are ready; the bank opens")
                for _ in range(CUSTOMER_COUNT):
                    self.bank_open.release()
            return True
        finally:
            self.dispatch_lock.release()

    def close(self):
        """Wake tellers already waiting after every customer has left."""
        self.dispatch_lock.acquire()
        try:
            self.closing = True
            idle = list(self.ready_tellers)
            self.ready_tellers.clear()
            for teller in idle:
                teller.stop = True
                teller.customer_arrived.release()
        finally:
            self.dispatch_lock.release()


class Customer(threading.Thread):
    def __init__(self, bank, identifier):
        super().__init__(name=f"Customer-{identifier}")
        self.bank = bank
        self.identifier = identifier
        self.transaction = random.choice(("deposit", "withdrawal"))
        self.random = random.Random()
        self.assigned = threading.Semaphore(0)
        self.transaction_requested = threading.Semaphore(0)
        self.transaction_done = threading.Semaphore(0)
        self.teller = None

    def run(self):
        bank = self.bank
        cid = self.identifier
        bank.log("Customer", cid, f"wants to perform a {self.transaction} transaction")

        delay = self.random.randint(0, 100)
        bank.log("Customer", cid, f"waits {delay} ms before going to the bank")
        time.sleep(delay / 1000.0)
        bank.log("Customer", cid, "is done waiting and goes to the bank")

        # The customer cannot approach the entrance until all three tellers are ready.
        bank.bank_open.acquire()
        bank.door.acquire()
        bank.log("Customer", cid, "enters the bank")
        bank.door.release()

        bank.log("Customer", cid, "gets in line")
        bank.customer_joins_line(self)
        self.assigned.acquire()

        teller = self.teller
        bank.log("Customer", cid, "selects teller", ("Teller", teller.identifier))
        bank.log("Customer", cid, "introduces itself", ("Teller", teller.identifier))
        teller.customer_arrived.release()

        self.transaction_requested.acquire()
        bank.log(
            "Customer",
            cid,
            f"asks for {self.transaction} transaction",
            ("Teller", teller.identifier),
        )
        teller.transaction = self.transaction
        teller.transaction_ready.release()

        self.transaction_done.acquire()
        bank.log("Customer", cid, "leaves teller", ("Teller", teller.identifier))
        teller.customer_left.release()

        bank.log("Customer", cid, "goes to the door")
        bank.door.acquire()
        bank.log("Customer", cid, "leaves the bank")
        bank.door.release()


class Teller(threading.Thread):
    def __init__(self, bank, identifier):
        super().__init__(name=f"Teller-{identifier}")
        self.bank = bank
        self.identifier = identifier
        self.random = random.Random()
        self.customer_arrived = threading.Semaphore(0)
        self.transaction_requested = threading.Semaphore(0)
        self.transaction_ready = threading.Semaphore(0)
        self.transaction_done = threading.Semaphore(0)
        self.customer_left = threading.Semaphore(0)
        self.customer = None
        self.transaction = None
        self.stop = False

    def serve_customer(self):
        bank = self.bank
        tid = self.identifier

        # Waiting on customer_arrived pairs with the customer's introduction.
        self.customer_arrived.acquire()
        if self.stop:
            return False
        customer = self.customer
        cid = customer.identifier
        bank.log("Teller", tid, "serves a customer", ("Customer", cid))
        bank.log("Teller", tid, "asks for transaction", ("Customer", cid))
        customer.transaction_requested.release()

        self.transaction_ready.acquire()
        transaction = self.transaction
        bank.log(
            "Teller",
            tid,
            f"handles {transaction} transaction",
            ("Customer", cid),
        )

        if transaction == "withdrawal":
            delay = self.random.randint(5, 30)
            bank.log("Teller", tid, "goes to the manager", ("Customer", cid))
            bank.manager.acquire()
            try:
                bank.log("Teller", tid, "gets manager's permission", ("Customer", cid))
                time.sleep(delay / 1000.0)
                bank.log("Teller", tid, "got manager's permission", ("Customer", cid))
            finally:
                bank.manager.release()

        delay = self.random.randint(10, 50)
        bank.log("Teller", tid, "goes to the safe", ("Customer", cid))
        bank.safe.acquire()
        try:
            bank.log("Teller", tid, "enters the safe", ("Customer", cid))
            time.sleep(delay / 1000.0)
        finally:
            bank.log("Teller", tid, "leaves the safe", ("Customer", cid))
            bank.safe.release()

        bank.log("Teller", tid, f"finishes {transaction} transaction", ("Customer", cid))
        bank.log("Teller", tid, "waits for customer to leave", ("Customer", cid))
        customer.transaction_done.release()
        self.customer_left.acquire()
        return True

    def run(self):
        bank = self.bank
        tid = self.identifier
        bank.log("Teller", tid, "is ready to serve")
        if not bank.teller_becomes_ready(self, starting=True):
            bank.log("Teller", tid, "leaves for the day")
            return

        while True:
            bank.log("Teller", tid, "waits for a customer")
            if self.stop:
                break
            if not self.serve_customer():
                break
            bank.log("Teller", tid, "is ready to serve")
            if not bank.teller_becomes_ready(self):
                break

        bank.log("Teller", tid, "leaves for the day")


def main():
    bank = Bank()
    tellers = [Teller(bank, i) for i in range(TELLER_COUNT)]
    customers = [Customer(bank, i) for i in range(CUSTOMER_COUNT)]

    # Start tellers first, then customers as required by the assignment.
    for teller in tellers:
        teller.start()
    for customer in customers:
        customer.start()

    for customer in customers:
        customer.join()

    bank.close()
    for teller in tellers:
        teller.join()

    bank.log("Teller", 0, "the bank closes for the day")


if __name__ == "__main__":
    main()



