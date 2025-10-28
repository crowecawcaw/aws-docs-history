Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Storing source code in repositories for a project in

CodeCatalyst

A source repository is where you securely store code and files for your project. It also
stores your source history, from the first commit through the latest changes. If you choose
a blueprint that includes a source repository, that repository also contains the
configuration files and other information for workflows and notifications for the project.
This configuration information is stored in a folder named
**.codecatalyst**.

You can create a source repository in CodeCatalyst either by creating a project with a
blueprint that creates a source repository as part of creating a project, or by creating a
source repository in an existing project. Project users will automatically see and be able
to use the repositories you create for a project. You can also choose to link a Git
repository hosted on GitHub, Bibucket, or GitLab to your project. When you do so, your project users
can view and access that linked repository in the list of repositories for the project.

###### Note

Before you can link the repository, you must install the extension for the service
that hosts it. You cannot link an archived repository. While you can link an empty
repository, you can't use it in CodeCatalyst until you have initialized it with an initial
commit that creates a default branch. For more information, see [Installing an extension in a space](install-extension.md "install-extension.md").

By default, a source repository is shared with other members of your Amazon CodeCatalyst project.
You can create additional source repositories for a project or link repositories to the
project. All members of a project can view, add, edit, and delete files and folders in the
project's source repositories.

To quickly work on code in a source repository, you can create a Dev Environment that clones a
specified repository and branch into it where you can work on the code in the integrated
development environment (IDE) you choose for the Dev Environment. You can clone a source
repository on your local computer and pull and push changes between your local repo and the
remote repository in CodeCatalyst. You can also work with source repositories by configuring
access to them in your preferred IDE as long as that IDE supports credential
management.

Repository names must be unique within a CodeCatalyst project.

###### Topics

- [Creating a source repository](source-repositories-create.md "source-repositories-create.md")
- [Cloning an existing Git repository
  into a source repository](source-repositories-add-existing.md "source-repositories-add-existing.md")
- [Linking a source repository](source-repositories-link.md "source-repositories-link.md")
- [Viewing a source repository](source-repositories-view.md "source-repositories-view.md")
- [Editing the settings for a source
  repository](source-repositories-edit.md "source-repositories-edit.md")
- [Cloning a source repository](source-repositories-clone.md "source-repositories-clone.md")
- [Deleting a source repository](source-repositories-delete.md "source-repositories-delete.md")
