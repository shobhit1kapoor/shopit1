# CS4348 Project 2: Bank Simulation

This program simulates the bank described in the Project 2 assignment using Python threads and `threading.Semaphore`.

## Run

Requires Python 3.9 or newer. No third-party packages are needed.

```powershell
python project2.py
```

The program starts three teller threads, then fifty customer threads. It prints one synchronized action line at a time in the format:

```text
THREAD_TYPE ID [THREAD_TYPE ID]: MESSAGE
```

An empty counterpart is shown as `[]` when a thread is not interacting with a particular other thread.

## Synchronization model

- A bank-open semaphore keeps customers from entering until all three tellers are ready.
- A capacity-two door semaphore controls customer entry and exit.
- A capacity-one manager semaphore serializes withdrawal approvals.
- A capacity-two safe semaphore limits the number of tellers performing transactions in the safe.
- A dispatch semaphore protects the ready-teller queue and customer line; per-customer/teller semaphores coordinate assignment, introductions, transaction requests, completion, and departure.
- An output semaphore keeps each log line intact.

Each customer selects a random deposit or withdrawal and waits 0–100 ms before visiting. Manager and safe work take the durations specified in the assignment. Random choices are unseeded, so the order and timing vary from run to run.

## Submission notes

The supplied sanitized rubric refers to a devlog, commit history, processes, and pipes, while the Project 2 brief describes a thread-based bank simulation. This repository includes the implementation and a truthful work log for this session; it does not claim earlier sessions or backdated commits. Review the rubric with the instructor if those extra grading requirements apply.
