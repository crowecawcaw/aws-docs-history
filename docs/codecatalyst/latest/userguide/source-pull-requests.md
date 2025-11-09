Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Reviewing code with pull requests in

Amazon CodeCatalyst

A pull request is the primary way you and other project members can review, comment on,
and merge code changes from one branch to another. You can use pull requests to review code
changes collaboratively for minor changes or fixes, major feature additions, or new versions
of your released software. If you use issues to track work on your project, you can link
specific issues to pull requests to help you track what issues are being addressed by the
code changes in the pull request. When you create, update, comment on, merge, or close a
pull request, an email is automatically sent to the author of the pull request as well as
any required or optional reviewers for the pull request.

###### Tip

You can configure what pull request events you that will receive emails about as part
of your profile. For more information, see [Sending Slack and email notifications from CodeCatalyst](notifications-manage.md "notifications-manage.md").

Pull requests require two branches in a source repository: a source branch that contains
the code that you want reviewed, and a destination branch, where you want to merge the
reviewed code. The source branch contains the AFTER commit, which is the commit that
contains the changes you want to merge into the destination branch. The destination branch
contains the BEFORE commit, which represents the state of the code before the pull request
branch is merged into the destination branch.

###### Note

While you are creating a pull request, the difference displayed is the difference
between the tip of the source branch and the tip of the destination branch. Once you
create the pull request, the displayed difference will be between the revision of the
pull request you choose and the commit that was the tip of the destination branch when
you created the pull request. For more information about differences and merge bases in
Git, see [git-merge-base](https://git-scm.com/docs/git-merge-base "https://git-scm.com/docs/git-merge-base") in
the Git documentation.

While a pull request is created for a specific source repository and branches, you can
create, view, review, and close them as part of working with your project. You do not have
to view the source repository in order to view and work with pull requests. A pull request
state is set to **Open** when you create it. The pull request remains open
until you either merge it in the CodeCatalyst console, which changes the state to
**Merged**, or close it, which changes the state to
**Closed**.

When your code has been reviewed, you can change the pull request state in one of several
ways:

- Merge the pull request in the CodeCatalyst console. The code in the source branch of the
  pull request will be merged into the destination branch. The pull request status
  will change to **Merged**. It can't be changed back to
  **Open**.
- Merge the branches locally and push your changes, and then close the pull request
  in the CodeCatalyst console.
- Use the CodeCatalyst console to close the pull request without merging. This will change
  the status to **Closed**, and it will not merge the code from the
  source branch into the destination branch.
  Before you create a pull request:

- Commit and push the code changes you want reviewed to a branch (the source
  branch).
- Set up notifications for your project, so other users can be notified about any
  workflows that run when you create a pull request. (This step is optional but
  recommended.)

###### Topics

- [Creating a pull request](pull-requests-create.md "pull-requests-create.md")
- [Viewing pull requests](pull-requests-view.md "pull-requests-view.md")
- [Managing requirements for merging
  a pull request with approval rules](source-pull-requests-approval-rules.md "source-pull-requests-approval-rules.md")
- [Reviewing a pull request](pull-requests-review.md "pull-requests-review.md")
- [Updating a pull request](pull-requests-update.md "pull-requests-update.md")
- [Merging a pull request](pull-requests-merge.md "pull-requests-merge.md")
- [Closing a pull request](pull-requests-close.md "pull-requests-close.md")
