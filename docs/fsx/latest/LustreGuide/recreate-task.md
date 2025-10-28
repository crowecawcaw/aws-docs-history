# Duplicating a task

You can duplicate an existing data repository task in the Amazon FSx console. When you
duplicate a task, an exact copy of the existing task is displayed in the
**Create import data repository task** or **Create export data repository task**
page. You can make changes to the paths to export or import, as needed,
before creating and running the new task.

###### Note

A request to run a duplicate task will fail if an exact copy of that task is already running.
An exact copy of a task that is already running contains the same file system path or paths in
the case of an export task or the same data repository paths in the case of an import task.

You can duplicate a task from the task details view, the **Data Repository Tasks** pane in the
**Data Repository** tab for the file system, or from the **Data repository
tasks** page.

###### To duplicate an existing task

1. Choose a task on the **Data Repository Tasks**
   pane in the **Data Repository** tab for the file system.
2. Choose **Duplicate task**. Depending on which type of task you chose,
   the **Create import data repository task** or **Create export data repository task** page
   appears. All settings for the new task are identical to those for the task that you're
   duplicating.
3. Change or add the paths that you want to import from or export to.
4. Choose **Create**.
