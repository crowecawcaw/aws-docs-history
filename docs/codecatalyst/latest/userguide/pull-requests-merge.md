Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Merging a pull request

After your code has been reviewed and all required reviewers have approved it, you can
merge a pull request in the CodeCatalyst console using a supported merge strategy, such as
fast-forward. Not all merge strategies supported in the CodeCatalyst console are available as
choices for all pull requests. CodeCatalyst evaluates the merge and only allows you to choose
between merge strategies that are available in the console and capable of merging the
source branch into the destination branch. You can also merge a pull request with your
choice of Git merge strategies by running the **git merge** command on
your local computer or a Dev Environment to merge the source branch into the destination
branch. You can then push those changes in the destination branch to the source
repository in CodeCatalyst.

###### Note

Merging the branch and pushing the changes in Git does not automatically close the
pull request.

If you have the Project administrator role, you can also choose to merge a pull request
that has not yet met all the requirements for approvals and approval rules.

## Merging a pull request

(console)

You can merge a pull request in the CodeCatalyst console if there are no merge conflicts
between the source and destination branches and if all required reviewers have
approved the pull request. If there are conflicts, or if the merge can't be
completed, the merge button is inactive, and a **Not mergeable**
label is displayed. In that case, you must obtain approval from any required
approvers, resolve conflicts locally if necessary, and push those changes before you
can merge. Merging a pull request will automatically send an email to the creator of
the pull request as well as any required or optional reviewers. It will not
automatically close or change the status of any issues linked to the pull
request.

###### Tip

You can configure what pull request events you that will receive emails about
as part of your profile. For more information, see [Sending Slack and email notifications from CodeCatalyst](notifications-manage.md "notifications-manage.md").

###### To merge a pull request

1. Navigate to the project where you want to merge a pull request.
2. On the project page, under **Open pull requests**, choose
   the pull request you want to merge. If you do not see the pull request,
   choose **View all pull requests** and then choose it from
   the list. Alternatively, in the navigation pane, choose
   **Code**, choose **Pull requests**,
   and then choose the pull request you want to merge. Choose
   **Merge**.
3. Choose from the available merge strategies for the pull request.
   Optionally, select or deselect the option to delete the source branch after
   merging the pull request, and then choose **Merge**.

###### Note

If the **Merge** button is inactive, or you see the
**Not mergeable** label, either required reviewers
have not yet approved the pull request, or the pull request can't be
merged in the CodeCatalyst console. A reviewer who has not approved a pull
request is indicated by a clock icon in the **Pull request
details** area in **Overview**. If all
required reviewers have approved the pull request but the
**Merge** button is still inactive, you might have
a merge conflict. Choose the underlined **Not
mergeable** label to see more details about why the pull
request can't be merged. You can resolve merge conflicts for the
destination branch in a Dev Environment or the CodeCatalyst console and then merge
the pull request, or you can resolve conflicts and merge locally, and
then push the commit that contains the merge to the source branch in
CodeCatalyst. For more information, see [Merging a pull request (Git)](#pull-requests-merge-git "#pull-requests-merge-git") and your Git
documentation.

## Override merge requirements

If you have the **Project administrator** role, you can choose to
merge a pull request that has not yet met all the requirements for required
approvals and approval rules. This is referred to as overriding the requirements for
a pull request. You might choose to do this if a required reviewer is unavailable,
or if an urgent need arises to merge a specific pull request into a branch that has
approval rules that cannot be met quickly.

###### To merge a pull request

1. In the pull request where you want to override requirements and merge,
   choose the drop-down arrow next to the **Merge** button.
   Choose **Override approval requirements**.
2. In **Override reason**, provide details of why you are
   merging this pull request without it meeting the approval rules and required
   reviewer requirements. While this is optional, this is highly recommended.
3. Optionally choose a merge strategy, or accept the default. You can also
   choose to update the automatically-generated commit message with more
   details.
4. Select or deselect the option to delete the source branch on merge. We
   recommend that you retain the source branch when overriding the requirements
   for merging a pull request until you've had a chance to review the decision
   with other team members.
5. Choose **Merge**.

## Merging a pull request (Git)

Git supports many options for merging and managing branches. The following
commands are some of the options that you can use. For more information, see the
available documentation on the [Git
website](https://git-scm.com/doc "https://git-scm.com/doc"). Once you have merged and pushed your changes, manually close
the pull request. For more information, see [Closing a pull request](pull-requests-close.md "pull-requests-close.md").

Common Git commands for merging
branches| Merges changes from the source branch in the local repo to the<br>destination branch in the local repo. | `git checkout<br>`destination-branch-name``<br>`git merge<br>`source-branch-name`` |
| Merges the source branch into the destination branch,<br>specifying a fast-forward merge. This merges the branches and<br>moves the destination branch pointer to the tip of the source<br>branch. | `git checkout<br>`destination-branch-name``<br>`git merge --ff-only<br>`source-branch-name`` |
| Merges the source branch into the destination branch,<br>specifying a squash merge. This combines all commits from the<br>source branch into a single merge commit in the destination<br>branch. | `git checkout<br>`destination-branch-name``<br>`git merge --squash<br>`source-branch-name`` |
| Merges the source branch into the destination branch,<br>specifying a three-way merge. This creates a merge commit and<br>adds the individual commits from the source branch to the<br>destination branch. | `git checkout<br>`destination-branch-name``<br>`git merge --no-ff<br>`source-branch-name`` |
| Deletes the source branch in the local repo. This is useful to<br>do as a clean-up for your local repo after merging to the<br>destination branch and pushing the changes to the source<br>repository. | `git branch -d<br>`source-branch-name`` |
| Deletes the source branch in the remote repository (the source<br>repository in CodeCatalyst) using the local repo's specified nickname<br>for the remote repository. (Note the use of the colon<br>(`:`).) Alternatively, specify<br>`--delete` as part of the command. | `git push `remote-name`<br>:`source-branch-name``<br>`git push `remote-name` --delete<br>`source-branch-name`` |
