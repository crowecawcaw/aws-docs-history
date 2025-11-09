Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Manage allowed actions for a branch with

branch rules

When you create a branch, certain actions are allowed for that branch based on the
permissions for that role. You can change what actions are allowed for a specific branch
by configuring branch rules. Branch rules are based on the role a user has in your
project. You can choose to limit some predefined actions, such as pushing commits to a
branch, to users with a particular role in a project. This can help you protect specific
branches in a project by limiting which roles are allowed to perform certain actions.
For example, if you configure a branch rule to only allow users with the
**Project administrator** role to merge or push to that branch,
users with other roles in the project will not be able to make changes to the code in
the that branch.

You should carefully consider all the implications of creating a rule for a branch.
For example, if you choose to limit pushes to a branch to users with the
**Project administrator** role, users with the
**Contributor** role will not be able to create or edit
workflows in that branch, because the workflow YAML is stored in that branch, and those
users cannot commit and push changes to the YAML. As a best practice, test any branch
rules after you create them in order to make sure that they do not have any impacts that
you did not intend. You can also use branch rules in conjunction with approval rules for pull
requests. For more information, see [Managing requirements for merging
a pull request with approval rules](source-pull-requests-approval-rules.md "source-pull-requests-approval-rules.md").

###### Note

You must have the Project administrator role to manage branch rules for source
repositories in CodeCatalyst projects. You cannot create branch rules for linked
repositories.

You can only create branch rules that are more restrictive than the default
permissions for the role. You cannot create branch rules that are more permissive
than what a user's role in the project allows. For example, you cannot create a
branch rule that allows users with the Reviewer role to push to the
branch.

Branch rules that are applied to the default branch of your source repository will
behave a little differently than branch rules applied to other branches. Any rule
applied to the default branch will be automatically applied to any branch you specify as
the default branch. The branch that was formerly set as the default branch will still
keep the rules applied to it, except that it will no longer have protection against
deletion. That protection is only applied to the current default branch.

Branch rules have two states, **Standard** and
**Custom**. **Standard** indicates that the
actions allowed on a branch are those that match the permissions for the role the user
has in CodeCatalyst for branch actions. To learn more about what roles have which permissions,
see [Granting access with user roles](ipa-roles.md "ipa-roles.md"). **Custom**
indicates that one or more branch actions have actions that have a specific list of
roles allowed to perform that action that differ from the default permissions granted by
a user's roe in the project.

###### Note

If you create a branch rule to restrict one or more actions for a branch, the
**Delete the branch** action is automatically set to only allow
users with the Project administrator role to delete that branch.

The following table lists the actions and the default settings for roles allowed to
perform these actions on a branch.

| Branch actions and roles                                                    | **Branch action**                  | Roles allowed to perform this action when no branch rules are<br>applied |
| --------------------------------------------------------------------------- | ---------------------------------- | ------------------------------------------------------------------------ |
| Merge to the branch (this includes merging a pull request to the<br>branch) | Project administrator, Contributor |
| Push to the branch                                                          | Project administrator, Contributor |
| Delete the branch                                                           | Project administrator, Contributor |
| Delete the branch (default branch)                                          | Not allowed                        |

You cannot delete branch rules, but you can update them to allow actions from all the
roles that would be allowed to perform this action on a branch, which effectively
removes the rule.

###### Note

You must have the Project administrator role to configure branch rules for source
repositories in CodeCatalyst projects. This does not apply to linked repositories. Linked
repositories do not support the branch rules in CodeCatalyst.

###### To view and edit branch rules for a

repository

1. Navigate to the project where your repository resides.
2. Choose the name of the repository from the list of source repositories for the
   project. Alternatively, in the navigation pane, choose
   **Code**, and then choose **Source
   repositories**.

Choose the repository where you want to view branch rules. 3. On the overview page of the repository, choose
**Branches**. 4. In the **Branch rules** column, view the status of rules for
each branch of the repository. **Standard** indicates that the
rules for branch action are the default ones for any branch created in a source
repository and match the permissions granted to those roles in a project.
**Custom** indicates that one or more branch actions have
rules that restrict one or more actions allowed for that branch to a different
set of roles.

To view the specifics of the branch rules for a branch, choose the word
**Standard** or **Custom** next to the
branch you want to review. 5. To create or change a branch rule, choose **Manage
settings**. On the settings page for the source repository, in
**Branch rules**, choose **Edit**. 6. In **Branch**, choose the name of the branch for which you
want to configure a rule from the drop-down list. For each of the allowed action
types, choose the roles you want to allow to perform that action from the
drop-down list, and then choose **Save**.
