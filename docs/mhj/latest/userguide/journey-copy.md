AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Copying a journey

The following procedure describes how to create a copy of a migration journey. The
copy that you create will have the same phases, modules, tasks, subtasks, task
dependencies, acceptance criteria, and tools as the original journey. In the copy, all
the phases and modules will be in scope and the status of all the tasks will be
`Planned`. Attachments, assignees, and comments won't be included in the
copy.

1. Open the Migration Hub Journeys console. For information about how to access the console, see [Accessing AWS Migration Hub Journeys](setup.md "setup.md").
2. In the left navigation pane, choose **Migration
   journeys**.
3. In the list of migration journeys, choose the name of the journey that you
   want to copy.
4. Choose **Actions**, then choose **Copy
   journey**.
5. Specify a different name for the copy if you don't want it to have the name
   that Migration Hub Journeys suggests.
6. You can optionally specify a description and a completion date for the
   copy.
7. Specify the migration space in which you want to place the copy. You can
   choose an existing migration space or create a new one.
8. Choose **Copy**.
