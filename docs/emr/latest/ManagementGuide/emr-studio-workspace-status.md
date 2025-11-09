# Understand Workspace status

After you create an EMR Studio Workspace, it appears as a row in the
**Workspaces** list in your Studio with its name,
status, creation time, and last modified timestamp. The following table describes
Workspace statuses.

| Status        | Description                                                                                                                                                                                                                                                                          |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Starting**  | The Workspace is being prepared, but is not yet ready to use. You<br>can't open a Workspace when its status is Starting.                                                                                                                                                             |
| **Ready**     | You can open the Workspace to use the notebook editor, but you must<br>attach the Workspace to an EMR cluster before you can run notebook<br>code.                                                                                                                                   |
| **Attaching** | The Workspace is being attached to a cluster.                                                                                                                                                                                                                                        |
| **Attached**  | The Workspace is attached to an EMR cluster and ready for you to<br>write and run notebook code. If a Workspace's status is not<br>**Attached**, you must attach it to a cluster before you can run<br>notebook code.                                                                |
| **Idle**      | The Workspace has stopped. To reactivate an idle Workspace,<br>select it from the Workspaces list. The status changes from<br>**Idle\*<br>• to **Starting*<br>• to<br>\*\*Ready*<br>• when you select the Workspace.                                                                 |
| **Stopping**  | The Workspace is shutting down and will be set to<br>**Idle**. When you stop a Workspace, it terminates any<br>corresponding notebook kernels. EMR Studio stops notebooks that have been<br>inactive for a long time.                                                                |
| **Deleting**  | When you delete a Workspace, EMR Studio marks it for deletion and<br>starts the deletion process. After the deletion process completes, the<br>Workspace disappears from the list. When you delete a Workspace, its<br>notebook files will remain in the Amazon S3 storage location. |
