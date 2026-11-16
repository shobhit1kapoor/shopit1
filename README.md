# CS 4348 Project 2: Bank Simulation

**Student:** Shobhit Kapoor
**Course:** CS 4348
**Section:** 501

## What the program does

The program simulates a bank with three tellers and fifty customers. Customers make a deposit or withdrawal. A teller must get the manager's approval for a withdrawal. Only one teller can use the manager at a time. Up to two tellers can use the safe at once. Up to two customers can use the door at once.

The program uses Python threads and semaphores to coordinate customers, tellers, and shared resources. It uses only Python's standard library.

## Files

- `project2.py` runs the bank simulation.
- `README.md` explains the program and how to run it.
- `devlog.md` records the work on this package. It notes where Codex helped.
- `.gitignore` excludes Python cache files.
- `.git/` contains the real Git history.

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

Each message follows this format:

```text
THREAD_TYPE ID [THREAD_TYPE ID]: MESSAGE
```

Empty brackets (`[]`) mean the thread is not speaking to a specific customer or teller. Timing and transaction choices are random, so each run looks different.

## Checks

Codex ran the program three times on the local computer at my request. All three runs finished successfully. Each output showed fifty completed transactions, fifty customers leaving, and all three tellers leaving. The checks also confirmed that customers entered after the bank opened, only one teller used the manager at a time, and no more than two tellers used the safe together.

I did not check the program on the course's `cs1` or `cs2` machines.

## Notes for the grader

The bank assignment brief describes a thread simulation. The supplied rubric also mentions processes and pipes, which are not part of that brief. Please confirm whether those rubric items apply.

The Git history records the real work dates. The commits are dated November 16, 2026; they have not been backdated to the assignment's listed due date.

The devlog is an honest record of AI-assisted work on this package. It does not invent earlier work sessions or personal experiences.
