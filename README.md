# CS4348 Project 2: Bank Simulation

This repository contains a single-file Python simulation of the bank described in the supplied Project 2 brief. It uses only the Python standard library.

## Files

- `project2.py` implements three teller threads, fifty customer threads, the bank-opening gate, customer line and teller dispatch, customer/teller handshakes, door capacity, manager access, safe capacity, and synchronized output.
- `README.md` describes the program and how to run it.
- `devlog.md` records the actual AI-assisted work on this package. It is transparent about the source of the entries and does not claim to be Shobhit's personal multi-session reflection.
- `.gitignore` excludes Python bytecode caches.
- `.git/` contains the repository history.

## Run from the command line

Requires Python 3.7 or newer and no external packages.

```text
python project2.py
```

On systems where the Python 3 command is named `python3`, use `python3 project2.py`.

Each log line follows `THREAD_TYPE ID [THREAD_TYPE ID]: MESSAGE`; `[]` means there is no current counterpart. Durations and deposit/withdrawal choices are random, so output order varies between runs.

## Synchronization model

- A bank-open semaphore releases customers only after all three tellers are ready.
- A capacity-two semaphore controls customer entry and exit through the door.
- A capacity-one semaphore serializes withdrawal approvals from the manager.
- A capacity-two semaphore limits tellers inside the safe.
- A dispatch semaphore protects the customer queue and ready-teller queue. Per-thread semaphores coordinate assignment, transaction requests, completion, and customer departure.
- An output semaphore keeps log lines intact.

The program uses Python threads and semaphores, with shared objects for communication. It does not use third-party libraries.

## Submission notes

The supplied Git/Project Instructions describe a clean working tree, a root `devlog.md`, a README, and a ZIP of the repository. This package follows those file and packaging instructions. Its Git history records the actual work dates and is not backdated. The supplied sanitized rubric also mentions processes and pipes, which do not appear in the bank simulation brief; confirm whether those rubric categories apply to this project.

The devlog is an honest AI-assisted work record, not a substitute for the student's own reflection entries if the course requires them. Review and supplement it with your own account before submitting.
