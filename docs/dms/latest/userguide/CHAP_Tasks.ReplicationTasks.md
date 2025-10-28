# Creating multiple

tasks

In some migration scenarios, you might have to create several migration tasks.
Tasks work independently and can run concurrently. Each task has its own initial
load, CDC, and log reading process. Tables that are related through data
manipulation language (DML) must be part of the same task.

Some reasons to create multiple tasks for a migration include the
following:

- The target tables for the tasks reside on different databases, such as
  when you are fanning out or breaking a system into multiple systems.
- You want to break the migration of a large table into multiple tasks by
  using filtering.

###### Note

Because each task has its own change capture and log reading process, changes
are _not_ coordinated across tasks. Therefore, when using multiple
tasks to perform a migration, make sure that each individual source transaction is
wholly contained within a single task. You can use multiple tasks to perform a migration
if no individual transaction is split across different tasks.
