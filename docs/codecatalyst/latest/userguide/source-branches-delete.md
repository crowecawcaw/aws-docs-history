

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Deleting a branch
<a name="source-branches-delete"></a>

If you no longer need a branch, you can delete it. For example, if you've merged a branch with a feature change into the default branch and that feature has been released, you might want to delete the original feature branch, as the changes are already part of the default branch. Keeping the number of branches low can help users find the branch that contains the changes they want to work on. When you delete a branch, copies of that branch remain in the clones of the repository on local computers until users pull and synchronize those changes.<a name="source-branch-delete"></a>

**To delete a branch (console)**

1. Navigate to the project where your repository resides.

1. Choose the name of the repository from the list of source repositories for the project. Alternatively, in the navigation pane, choose **Code**, and then choose **Source repositories**.

   Choose the repository where you want to delete a branch.

1. On the overview page of the repository, choose the drop-down selector next to the branch name, and then choose **View all**.

1. Choose the branch that you want to delete and then choose **Delete branch**.
**Note**  
You cannot delete the default branch for a repository.

1. A confirmation dialog box appears. It shows the repository, number of open pull requests, and number of workflows associated with the branch. 

1. To confirm deletion of the branch, type **delete** into the text box, and then choose **Delete**.

You can also use Git to delete branches. For more information, see [Common Git commands for branches](source-branches-git.md#source-branches-git-table).