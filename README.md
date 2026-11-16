# CS 4348 Project 2: Bank Simulation

**Student:** Shobhit Kapoor
**Course:** CS 4348
**Section:** 501

## What the program does

This program simulates a bank with three tellers and fifty customers. Each customer randomly chooses a deposit or withdrawal. A teller gets the manager's approval for a withdrawal, then uses the safe to complete the transaction. The bank opens after all three tellers are ready and closes after all customers leave.

The program uses Python threads and semaphores. The manager semaphore allows one teller at a time. The safe semaphore allows up to two tellers at a time. The door semaphore allows up to two customers to enter or leave at once. Other semaphores coordinate the opening of the bank, teller assignments, and customer-teller conversations. A semaphore also keeps each output line together. The program uses only Python's standard library.

## Files

- `project2.py` contains and runs the simulation.
- `README.md` explains the program and how to run it.
- `devlog.md` records the project work and review.
- `.gitignore` excludes Python cache files.
- `.git/` contains the Git history.

## How to run

Use Python 3.7 or newer. No extra packages are needed.

On Windows:

```text
py project2.py
```

On Linux or macOS:

```text
python3 project2.py
```

Most output lines use this format:

```text
THREAD_TYPE ID [THREAD_TYPE ID]: MESSAGE
```

Empty brackets (`[]`) mean the thread is not speaking to a specific customer or teller. The final bank-closing message comes from the main thread and appears by itself. Transaction choices and timing are random, so each run looks different.

## Final checks

The program was run three times during the final review on November 16, 2026. Each run completed all fifty transactions, showed all fifty customers leaving, and showed all three tellers leaving. The output was also checked for the bank opening before customer entry, exclusive manager use, and a maximum of two tellers in the safe. The final closing message is printed after the teller threads finish.

The program has not been checked on the course's `cs1` or `cs2` machines.

## Processes and pipes

The assignment asks for threads in one application. Threads in this program share Python objects, and semaphores coordinate access to those objects. A pipe can pass data between separate processes, but this program does not create separate processes or use pipes because the assignment calls for threads.
