Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Managing the default branch for a

repository

You can specify which branch to use as the _default branch_ in a
source repository in Amazon CodeCatalyst. All source repositories in CodeCatalyst have contents and a
default branch regardless of how you create them. If you use a blueprint to create a
project, the default branch in the source repository created for that project is named
_main_. The contents of the default branch are displayed
automatically on the overview page for that repository.

###### Important

CodeCatalyst doesn't support detecting changes in the default branch for linked
repositories. To change the default branch for a linked repository, you must first unlink it
from CodeCatalyst, change the default branch, and then link it again. For more information,
see [Linking GitHub repositories, Bitbucket repositories, GitLab project repositories,
and Jira projects in CodeCatalyst](extensions-link.md "extensions-link.md").

As a best practice, always make sure you have the latest version of the extension
before you link a repository.

The default branch is treated a little differently than all other branches in a source
repository. It has a special label next to its name, **Default**. The
default branch is the one used as the base or default branch in local repositories
(repos) when users clone the repository to local computers with a Git client. It is also
the default used when creating workflows for storing workflow YAML files, and for
storing information for issues. When using search in CodeCatalyst, only the default branch of
a repository is searched. Because the default branch is fundamental to so many aspects
of projects, you cannot delete a branch if it is specified as the default branch.
However, you can choose to use a different branch as the default branch. If you do, any
[branch rules](source-branches-branch-rules.md "source-branches-branch-rules.md") that were applied
to the former default branch will be applied automatically to the branch you specify as
the default branch.

###### Note

You must have the Project administrator role to change the default branch for
source repositories in CodeCatalyst projects. This does not apply to linked
repositories.

###### To view and change the default branch for a

repository

1. Navigate to the project where your repository resides.
2. Choose the name of the repository from the list of source repositories for the
   project. Alternatively, in the navigation pane, choose
   **Code**, and then choose **Source
   repositories**.

Choose the repository where you want to view the settings, including the
default branch. 3. On the overview page of the repository, choose **More**, and
then choose **Manage settings**. 4. In **Default branch**, the name of the branch specified as
the default branch is displayed along with a label called
**Default** next to the name. This same label appears next
to the branch name in the list of branches in
**Branches**. 5. To change the default branch, choose **Edit**.

###### Note

You must have the Project administrator role in the project to change the default branch. 6. Choose the name of the branch you want to make the default branch from the
drop-down list and then choose **Save**.
