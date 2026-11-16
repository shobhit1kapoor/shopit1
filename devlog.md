# Work log

**Student:** Shobhit Kapoor
**Course:** CS 4348
**Section:** 501
**AI help:** Codex helped write and check the code and documents. The entries below describe the work done with that help.

## 2026-11-16 — implementation session

This project was assembled in one recorded session from the supplied Project 2 brief. The implementation models three tellers, fifty customers, the two-person entrance/exit, serialized manager access for withdrawals, two safe slots, customer/teller handshakes, and the required action logging.

This entry records the actual work performed for this package. It does not reconstruct earlier sessions or claim personal reflections from the student. Add your own dated entries describing your decisions, progress, and any issues you encountered if the course requires a student-authored multi-session devlog.

## 2026-11-16 04:42:49 CST — repository-instructions review (Codex-assisted)

**Thoughts so far:** The newly supplied Git/Project Instructions confirm a root `devlog.md`, a README with file roles and command-line run instructions, a clean working tree, and a ZIP of the repository. The sanitized rubric's process and pipe categories still appear inconsistent with the Project 2 bank brief, which specifies threads.

**Plan for this session:** Use the required lowercase `devlog.md` filename, update the README to describe the files and run command, preserve actual Git timestamps, and rebuild the archive with the repository metadata included. Keep the work record explicit about its AI-assisted authorship and do not invent student reflections.

## 2026-11-16 04:44:20 CST — session reflection (Codex-assisted)

The README now lists the project files and command-line run instructions, and Git tracks the required lowercase `devlog.md`. The code and documentation updates have real commits dated today; the repository has not been backdated. The application has not been run, and this log remains an AI activity record rather than the student's own multi-session reflections. The final ZIP will be rebuilt from the committed repository after this entry is committed.


## 2026-11-16 04:45 CST — verification plan (AI-assisted; time rounded to the minute)

**Thoughts so far:** I wanted to check the program against the assignment and make the README easier to follow. The manager's completion message should appear before the next teller uses the manager.

**Plan for this review:** Run the program several times, check that all customers and tellers finish, check the manager and safe limits, then add my course details and clear run instructions.

## 2026-11-16 04:51:07 CST — verification reflection (AI-assisted)

The first checks found that the manager's completion message could appear after the next teller's permission message. Codex moved that message so it prints before the manager semaphore is released. Three new runs then finished successfully. Each run showed fifty completed transactions, fifty customer departures, three teller departures, and the right manager and safe limits. The README now has the run commands and my course details. The program has not been checked on `cs1` or `cs2`.

This review happened in one recorded work period. The original work log above remains unchanged. This entry does not claim that I kept a multi-session diary while the code was written.

## 2026-11-16 05:10:35 CST — rubric review plan (AI-assisted)

**Thoughts so far:** Shobhit confirmed that the rubric is for this bank project. The points for threads, semaphores, and shared data match the assignment. The devlog section also asks about processes and pipes, even though the bank program uses threads.

**Plan for this session:** Update the README and work log to explain this clearly. Keep the code aligned with the bank assignment, and do not claim that it uses processes or pipes.

## 2026-11-16 05:11:10 CST — rubric review reflection (AI-assisted)

Shobhit confirmed that the rubric is for this project. I updated the README to say that clearly. With Codex's help, I connected the processes-and-pipes rubric items to this program: threads share data inside one process, and semaphores control when they use that data. Separate processes can use pipes to pass data between them. The bank brief asks for threads, so this program does not use pipes. I did not add a different process design that would conflict with the assignment.

## 2026-11-16 05:21:57 CST — date correction

Shobhit clarified that the due date printed in the supplied project brief is wrong. I removed the deadline comparison from the README and will not use that date to judge the Git history. The actual due date was not given here. Git keeps the real dates of the work.
