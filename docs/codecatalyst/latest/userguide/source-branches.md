Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Organizing your source code work with branches in

Amazon CodeCatalyst

In Git, branches are pointers or references to a commit. In development, they're a
convenient way to organize your work. You can use branches to separate work on a new or
different version of files without affecting work in other branches. You can use branches to
develop new features, store a specific version of your project, and more. You can configure
rules for branches in source repositories to limit certain actions on a branch to specific roles
in that project.

Source repositories in Amazon CodeCatalyst have contents and a default branch regardless of how you
create them. Linked repositories might not have a default branch or content, but are not
usable by CodeCatalyst until you initialize them and create a default branch. When you create a
project using a blueprint, CodeCatalyst creates a source repository for that project that
includes a README.md file, sample code, workflow definitions, and other resources. When you
create a source repository without using a blueprint, a README.md file is added for you as
a first commit, and a _default branch_ is created for you. This default
branch is named _main_. This default branch is the one used as the base
or default branch in local repositories (repos) when users clone the repository.

###### Note

You can't delete the default branch. The first branch created for a source
repository is the default branch for that repository. Additionally, search only displays
results from the default branch. You can't search for code in other branches.

Creating a repository in CodeCatalyst also creates a first commit, which creates a
_default branch_ with a README.md file included in it. The name of
that default branch is _main_. This is the default branch name used in
the examples in this guide.

###### Topics

- [Creating a branch](source-create-delete-branch.md "source-create-delete-branch.md")
- [Managing the default branch for a
  repository](source-branches-default-branch.md "source-branches-default-branch.md")
- [Manage allowed actions for a branch with
  branch rules](source-branches-branch-rules.md "source-branches-branch-rules.md")
- [Git commands for branches](source-branches-git.md "source-branches-git.md")
- [Viewing branches and details](source-branches-view.md "source-branches-view.md")
- [Deleting a branch](source-branches-delete.md "source-branches-delete.md")
