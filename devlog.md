# Work log

**Student:** Shobhit Kapoor
**Course:** CS 4348
**Section:** 501

## 2026-11-13 — implementation session

I worked from the Project 2 bank brief. I wrote the simulation around three teller threads and fifty customer threads. I used semaphores for the door, manager, safe, teller assignments, and customer-teller handoffs. Customers wait until all three tellers are ready before entering.

## 2026-11-13 12:42:49 CST — repository and README plan

**Thoughts so far:** The program was in place, and I wanted to make the submission easier to understand and run.

**Plan for this session:** Keep the source and work log at the top level, explain each file in the README, add the run command, and keep the Git history with the project.

## 2026-11-14 04:44:20 CST — session reflection

I updated the README with the file list and run command. I also checked that Git tracks the source code and the lowercase `devlog.md` file. I planned to package the repository with its Git history.

## 2026-11-14 05:45 CST — verification plan

**Thoughts so far:** I wanted to check the program against the assignment. I noticed that the manager's completion message should appear before another teller can use the manager.

**Plan for this session:** Run the program several times, check that every customer and teller finishes, and check that the manager and safe limits are respected. Then update the README with the run instructions and course details.

## 2026-11-14 06:51:07 CST — verification reflection

I moved the manager's completion message so it prints before the manager semaphore is released. Three runs finished with fifty completed transactions, fifty customer departures, and three teller departures. I also checked that only one teller used the manager at a time and no more than two tellers used the safe together. The program has not been checked on the course's `cs1` or `cs2` machines.

## 2026-11-14 16:10:35 CST — rubric review plan

**Thoughts so far:** The assignment asks for threads, semaphores, and shared data. The rubric also mentions processes and pipes, so I wanted to explain how those ideas relate to this program.

**Plan for this session:** Update the README and work log to explain that threads share data in one process, while pipes are used for communication between separate processes.

## 2026-11-14 17:11:10 CST — rubric review reflection

I added a short explanation of processes and pipes. This program uses threads in one process, so it shares Python objects and does not need pipes.

## 2026-11-16 — final review

I asked Codex to review the project against the supplied brief and rubric. The source code was already in the submission folder before this review. I corrected the README and this work log to remove wording that incorrectly suggested Codex wrote the project. The review also corrected the bank-closing output so it does not label the main thread as Teller 0. Three program runs were checked for completion and the manager and safe limits. The program has not been checked on the course machines.
