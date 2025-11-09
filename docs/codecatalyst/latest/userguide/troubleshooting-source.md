Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Troubleshooting problems with source repositories

The following information can help you troubleshoot common issues with source repositories in CodeCatalyst.

###### Topics

- [I have reached the maximum storage for my space and see warnings or errors](#source-troubleshoot-storage "#source-troubleshoot-storage")
- [I receive an error when trying to clone or push to an Amazon CodeCatalyst source repository](#source-troubleshoot-clone "#source-troubleshoot-clone")
- [I receive an error when trying to commit or push to an Amazon CodeCatalyst source repository](#source-troubleshoot-commit-code "#source-troubleshoot-commit-code")
- [I need a source repository for my project](#source-troubleshoot-need-repository "#source-troubleshoot-need-repository")
- [My source repository is brand-new but contains a commit](#source-troubleshoot-initial-commit "#source-troubleshoot-initial-commit")
- [I want a different branch as my default branch](#source-troubleshoot-default-branch "#source-troubleshoot-default-branch")
- [I am receiving emails about activity in pull requests](#source-troubleshoot-repository-emails "#source-troubleshoot-repository-emails")
- [I forgot my personal access token (PAT)](#source-troubleshoot-forgot-pat "#source-troubleshoot-forgot-pat")
- [A pull request doesn’t display the changes I expect](#source-troubleshoot-pull-request-diff "#source-troubleshoot-pull-request-diff")
- [A pull request shows a status of Not mergeable](#source-troubleshoot-pull-request-not-mergeable "#source-troubleshoot-pull-request-not-mergeable")

## I have reached the maximum storage for my space and see warnings or errors

**Problem:** I want to commit code to one or more source repositories in CodeCatalyst, but I see an error.
In the console, I see a message on the source repository page that I have reached the storage limit for the space.

**Possible fixes:** Depending on your role in the project or space,
you can either reduce the size of one or more of your source repositories,
delete unused source repositories, or change your billing tier to one that has more storage.

- To reduce the size of a source repository in a project, you can delete unused branches.
  For more information, see [Deleting a branch](source-branches-delete.md "source-branches-delete.md") and
  [Contributor role](ipa-role-types.md#ipa-role-contributor "ipa-role-types.md#ipa-role-contributor").
- To reduce the overall storage for a space, you can delete unused source repositories. For more
  information, see [Deleting a source repository](source-repositories-delete.md "source-repositories-delete.md") and [Project administrator role](ipa-role-types.md#ipa-role-project-admin "ipa-role-types.md#ipa-role-project-admin").
- To increase the amount of storage available for your space, you can change your billing tier to one with more storage. For more information, see [Changing your CodeCatalyst billing tier](../adminguide/managing-billing-change-plan.md "../adminguide/managing-billing-change-plan.md") in the Amazon CodeCatalyst Administrator Guide.

## I receive an error when trying to clone or push to an Amazon CodeCatalyst source repository

**Problem:** When I try to clone a source repository to a local computer or
into an integrated development environment (IDE), I receive a permissions error.

**Possible fixes:** You might not have a
personal access token (PAT) for your AWS Builder ID, you might not have configured your
credential management system with your PAT, or your PAT might have expired. Try one or
more of the following solutions:

- Create a personal access token (PAT). For more information, see [Grant users repository access with personal access tokens](ipa-tokens-keys.md "ipa-tokens-keys.md").
- Make sure you have accepted an invitation to the project that contains the source repository and that you are still a member of
  that project. You cannot clone a source repository if you aren’t an active member of that project. Sign in to the console and attempt to navigate to
  the space and the project where you're trying to clone a source repository. If you cannot see the project in the list of projects for the space,
  you either aren't a member of that project, or you haven't accepted an invitation to that project. For more information, see
  [Accepting an invitation and creating an AWS Builder ID](sign-up-sign-in.md "sign-up-sign-in.md").
- Make sure your clone command is formatted correctly and includes your AWS Builder ID. For example:

```
https://`LiJuan`@git.us-west-2.codecatalyst.aws/v1/`ExampleCorp`/`MyExampleProject`/`MyExampleRepo`
```

- Use the AWS CLI to make sure that you have a PAT associated with your AWS Builder ID, and that it is not expired.
  If you don’t have one or the PAT is expired, create one. For more information, see [Grant users repository access with personal access tokens](ipa-tokens-keys.md "ipa-tokens-keys.md").
- Try creating a Dev Environment to work with the code in the source repository instead of cloning it to a local repo or IDE.
  For more information, see [Creating a Dev Environment](devenvironment-create.md "devenvironment-create.md").

## I receive an error when trying to commit or push to an Amazon CodeCatalyst source repository

**Problem:** When I try to push to a source repository, I receive a permissions error.

**Possible fixes:** You might not have a role in the
project that allows you to commit and push code changes to the project. View your role in the project where you are trying to push
changes to a source repository. For more information, see [Getting a list of members and their project roles](projects-members.md#projects-members-view "projects-members.md#projects-members-view")
and [Granting access with user roles](ipa-roles.md "ipa-roles.md").

If you have a role that allows committing and pushing changes, the branch where you are trying to commit changes might have a branch rule
configured for it that prevents you from pushing code changes to that branch. Try creating a branch and pushing your code to that branch instead.
For more information, see [Manage allowed actions for a branch with
branch rules](source-branches-branch-rules.md "source-branches-branch-rules.md").

## I need a source repository for my project

**Problem:** My project either doesn’t have a source repository, or I need another source repository for my project.

**Possible fixes:** Some projects are created without any resources. If you are a member of the project,
you can create source repositories for that project in CodeCatalyst. If someone with the **Space administrator** role installs the
**GitHub Repositories** and connects it to a GitHub account, you can link to available GitHub repositories to add them to
your project if you have the **Project administrator** role. For more information, see
[Creating a source repository](source-repositories-create.md "source-repositories-create.md") and [Linking a source repository](source-repositories-link.md "source-repositories-link.md").

## My source repository is brand-new but contains a commit

**Problem:** I just created a source repository. It should be empty, but it has a commit,
a branch, and a `README.md` file in it.

**Possible fixes:** This is expected behavior. All source repositories in CodeCatalyst include an initial commit
that sets the default branch to `main` and includes either sample code (if the repository was created for a project using a
blueprint that included sample code) or a template markdown file for a repository README file. You can create additional branches in
the console and in Git clients. You can create and edit files in the console, and delete files in Dev Environments and Git clients.

## I want a different branch as my default branch

**Problem:** My source repository came with a default branch named `main`, but I want a
different branch as my default branch.

**Possible fixes:** You cannot change or delete the default branch in source repositories in CodeCatalyst.
You can create additional branches and use those branches in source actions in workflows. You can also choose to link GitHub
repositories and use them as repositories for your project.

## I am receiving emails about activity in pull requests

**Problem:** I didn't sign up or configure email notifications about pull request activity, but I'm receiving them anyway.

**Possible fixes:** Email notifications are sent automatically about pull request activity. For more information, see
[Reviewing code with pull requests in
Amazon CodeCatalyst](source-pull-requests.md "source-pull-requests.md").

## I forgot my personal access token (PAT)

**Problem:** I’ve been using a PAT for cloning, pushing, and pulling code for source repositories,
but I’ve lost the value for my token, and I can’t find it in the CodeCatalyst console.

**Possible fixes:** The quickest way to solve this problem is to create another PAT and configure
your credential manager or IDE to use this new PAT. We only display the value of a PAT when you create it. If you lose this value,
it cannot be retrieved. For more information, see [Grant users repository access with personal access tokens](ipa-tokens-keys.md "ipa-tokens-keys.md").

## A pull request doesn’t display the changes I expect

**Problem:** I created a pull request, but I don’t see the changes I expect to see between the source and destination branches.

**Possible fixes:** This might be caused by a number of issues.
Try one or more of the following solutions:

- You might be reviewing the changes between older revisions, or you might not be viewing the latest changes.
  Refresh your browser and make sure that you’ve chosen the comparison between revisions you want to view.
- Not all changes in a pull request can be displayed in the console. For example, you cannot view Git submodules
  in the console, so you cannot view differences in a submodule in a pull request. Some differences might be too large to display.
  For more information, see [Quotas for source repositories in CodeCatalyst](source-quotas.md "source-quotas.md") and
  [Viewing a file](source-files-view.md "source-files-view.md").
- Pull requests display the differences between the merge base and whatever revision you choose.
  When you create a pull request, the difference displayed for you is the
  difference between the tip of the source branch and the tip of the destination
  branch. Once the pull request has been created, the displayed difference is
  between the revision and its merge base. The merge base is the commit that was
  the tip of the destination branch when the revision was created. The merge base
  can change between revisions. For more information about differences and merge
  bases in Git, see [git-merge-base](https://git-scm.com/docs/git-merge-base "https://git-scm.com/docs/git-merge-base") in the Git documentation.

## A pull request shows a status of Not mergeable

**Problem:** I want to merge a pull request, but its status shows as **Not mergeable**.

**Possible fixes:** This can be caused by one or more problems:

- All required reviewers for your pull request must approve a pull request before it can be merged. Review
  the list of required reviewers for any reviewers with a clock icon next to the name. A clock icon indicates that the reviewer hasn't approved the pull request.

###### Note

If a required reviewer has been removed from your project before approving the pull request, you cannot merge the pull request. Close the pull request
and create a new pull request.

- There might be a merge conflict between the source branch and the destination branch. CodeCatalyst does not support all possible Git merge strategies and options.
  You can evaluate the branches for merge conflicts in a Dev Environment or clone the repository and use an IDE or Git tools to find and resolve merge conflicts. For more information,
  see [Merging a pull request](pull-requests-merge.md "pull-requests-merge.md").
