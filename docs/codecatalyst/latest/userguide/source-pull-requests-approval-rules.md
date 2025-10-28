Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Managing requirements for merging

a pull request with approval rules

When you create a pull request, you can choose to add required or optional reviewers
to that individual pull request. However, you can also create requirements that all pull
requests must meet when merging to a specific destination branch. These requirements are
called approval rules. Approval rules are configured for branches in a repository. When
you create a pull request whose destination branch has an approval rule configured for
it, the requirements for that rule must be met in addition to approvals from any
required reviewers before you can merge the pull request to that branch. Creating
approval rules can help you maintain quality standards for merges to branches such as
your default branch.

Approval rules that are applied to the default branch of your source repository will
behave a little differently than approval rules applied to other branches. Any rule
applied to the default branch will be automatically applied to any branch you specify as
the default branch. The branch that was formerly set as the default branch will still
keep the rules applied to it.

When you create approval rules, you should consider how that rule will be met by your
project users both in the present and in the future. For example, if you have six users
in your project, and you create an approval rule that requires five approvals before it
can be merged to the destination branch, you have effectively created a rule that
requires everyone except the person who created the pull requets to approve that pull
request before it can be merged.

###### Note

You must have the Project administrator role to create and manage approval rules in
CodeCatalyst projects. You cannot create approval rules for linked repositories.

You cannot delete approval rules, but you can update them to require zero approvals,
which effectively removes the rule.

###### To view and edit approval rules for destination branches

for pull requests

1. Navigate to the project where your repository resides.
2. Choose the name of the repository from the list of source repositories for the
   project. Alternatively, in the navigation pane, choose
   **Code**, and then choose **Source
   repositories**.

Choose the repository where you want to view approval rules. 3. On the overview page of the repository, choose
**Branches**. 4. In the **Approval rules** column, choose
**View** to see the status of any rules for each branch of
the repository.

In **Minimum number of approvals**, the number corresponds to
the number of approvals required before a pull request can be merged to that
branch. 5. To create or change an approval rule, choose **Manage
settings**. On the settings page for the source repository, in
**Approval rules**, choose
**Edit**.

###### Note

You must have the **Project administrator** role to edit
approval rules. 6. In **Branch**, choose the name of the branch for which you
want to configure an approval rule from the drop-down list. In **Minimum
number of approvals**, enter a number, and then choose
**Save**.
