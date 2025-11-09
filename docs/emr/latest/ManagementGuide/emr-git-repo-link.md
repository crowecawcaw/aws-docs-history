# Link or unlink a Git-based repository in EMR Studio

Use the following steps to link or unlink a Git-based repository to an
EMR notebook in the old console, or to an EMR Studio Workspace
in the console.

###### Note

EMR Notebooks are available as EMR Studio Workspaces in the console. The **Create Workspace** button in the console lets you create new notebooks. To access or create Workspaces, EMR Notebooks users need additional IAM role permissions. For more information, see [Amazon EMR Notebooks are Amazon EMR Studio Workspaces in the console](emr-managed-notebooks-migration.md "emr-managed-notebooks-migration.md") and [Amazon EMR console](whats-new-in-console.md "whats-new-in-console.md").

Console
Because EMR Notebooks are EMR Studio Workspaces in the new
console, you can you can refer to [Link Git-based repositories to an EMR Studio
Workspace](emr-studio-git-repo.md "emr-studio-git-repo.md") for more information on
working with Git repositories in your Workspace. But at this
time, you can't delete Git repositories from Workspaces.

## Understanding

repository status

A Git repository may have any of the following status in the repository list.
For more information about linking EMR notebooks with Git repositories,
see [Link or unlink a Git-based repository in EMR Studio](emr-git-repo-link.md "emr-git-repo-link.md").

| Status        | Meaning                                                                                                                                                                                                                                                                           |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Linking       | The Git repository is being linked to the notebook. While<br>the repository is **Linking**, you cannot<br>stop the notebook.                                                                                                                                                      |
| Linked        | The Git repository is linked to the notebook. While the<br>repository has a \*_Linked_<br>• status, it is<br>connected to the remote repository.                                                                                                                                  |
| Link Failed   | The Git repository failed to link to the notebook. You can<br>try again to link it.                                                                                                                                                                                               |
| Unlinking     | The Git repository is being unlinked from the notebook.<br>While the repository is **Unlinking**, you<br>cannot stop the notebook. Unlinking a Git repository from a<br>notebook only disconnects it from the remote repository; it<br>doesn't delete any code from the notebook. |
| Unlink Failed | The Git repository failed to unlink from the notebook. You<br>can try again to unlink it.                                                                                                                                                                                         |
