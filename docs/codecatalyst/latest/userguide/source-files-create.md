

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Creating or adding a file
<a name="source-files-create"></a>

To create and add files to a source repository, you can use the Amazon CodeCatalyst console, a Dev Environment, a connected integrated development environment (IDE), or a Git client. The CodeCatalyst console includes a code editor for creating files. This editor is a convenient way to create or edit a simple file, such as a README.md file, in a branch in a repository. When working on more than one file, consider [creating a Dev Environment](devenvironment-create.md).

**To create a Dev Environment from a source repository**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. In the navigation pane, choose **Code**, and then choose **Source repositories**.

1. Choose the source repository where you want to work on code.

1. Choose **Create Dev Environment**.

1. Choose a supported IDE from the drop-down menu. See [Supported integrated development environments for Dev Environments](devenvironment-create.md#devenvironment-supported-ide) for more information.

1. Do one of the following:
   + Choose **Work in existing branch**, and then choose a branch from the **Existing branch** drop-down menu.
   + Choose **Work in new branch**, enter a branch name into the **Branch name** field, and choose a branch off of which to create the new branch from the **Create branch from** drop-down menu.

1. Optionally add a name for the Dev Environment or edit its configuration.

1. Choose **Create**.

**To create a file in the CodeCatalyst console**

1. Navigate to the project where you want to create a file. For more information about how to navigate to a repository, see [Viewing a source repository](source-repositories-view.md). 

1. Choose the name of the repository from the list of source repositories for the project. Alternatively, in the navigation pane, choose **Code**, and then choose **Source repositories**.

   Choose the repository where you want to create the file. 

1. (Optional) Choose the branch where you want to create the file, if you want to create the file in a different branch than the default branch.

1. Choose **Create file**. 

1. Enter the name of the file in **File name**. Add the contents of the file in the editor. 
**Tip**  
If you want to create the file in a sub-folder or subdirectory of the root of the branch, include that structure as part of the file name.

   When you are satisfied with your changes, choose **Commit**.

1. In **File name**, review the name of the file and make any changes you might want to it. Optionally choose the branch where you want to create the file from the list of available branches in **Branch**. In **Commit message**, optionally enter a brief but informative description of why you made this change. This will be displayed as the basic commit information for the commit that adds the file to the source repository.

1. Choose **Commit** to commit and push the file to the source repository.

You can also add files to a source repository by cloning it to your local computer and using a Git client or connected integrated development environment (IDE) to push your files and changes. 

**Note**  
If you want to add a Git submodule, you must use a Git client or a Dev Environment and run the **git submodule add** command. You cannot add or view Git submodules in the CodeCatalyst console or view the differences in Git submodules in pull requests. For more information about Git submodules, see the [Git documentation](https://git-scm.com/book/en/v2/Git-Tools-Submodules).<a name="source-files-add-git"></a>

**To add a file using a Git client or connected integrated development environment (IDE)**

1. Clone your source repository to your local computer. For more information, see [Cloning a source repository](source-repositories-clone.md).

1. Create files in your local repo or copy files into your local repo.

1. Create and push a commit by doing one of the following:
   + If you are using a Git client, at the terminal or command line, run the **git add** command, specifying the names of the files you want to add. Alternatively, to add all added or changed files, run the **git add** command followed by either a single or double period to indicate whether you want to include all the changes at the current directory level (single period) or all changes in the current directory and all subdirectories (double period). To commit the changes, run the **git commit -m** command and provide a commit message. To push your changes to the source repository in CodeCatalyst, run **git push**. For more information about Git commands, see your Git documentation and [Git commands for branches](source-branches-git.md).
   + If you are using a Dev Environment or an IDE, create files and add files in the IDE, and then commit and push your changes. For more information, see see [Write and modify code with Dev Environments in CodeCatalyst](devenvironment.md) or consult your IDE documentation.