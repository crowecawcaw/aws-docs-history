# Configuring budget actions

You can use AWS Budgets to run an action on your behalf when a budget exceeds a certain
cost or usage threshold. To do this, after you set a threshold, configure a budget action to
run either automatically or after your manual approval.

Your available actions include applying an IAM policy or a service control policy (SCP).
They also include targeting specific Amazon EC2 or Amazon RDS instances in your account. You can use
SCPs so that you don't need to provision any new resources during the budget period.

###### Note

From the management account, you can apply an SCP to another account. However, you
can't target Amazon EC2 or Amazon RDS instances in another account.

You can also configure multiple actions to initiate at the same notification threshold. For
example, you can configure actions to initiate automatically when you reach 90 percent of
your forecasted costs for the month. To do so, perform the following actions:

- Apply a custom `Deny IAM` policy that restricts the ability for a user,
  group, or role to provision additional Amazon EC2 resources.
- Target specific Amazon EC2 instances in `US East (N. Virginia)
us-east-1`.

###### Topics

- [Setting up a role for AWS Budgets to run budget
  actions](budgets-action-role.md "budgets-action-role.md")
- [Configuring a budget action](budgets-action-configure.md "budgets-action-configure.md")
- [Reviewing and approving your budget
  action](budgets-action-review.md "budgets-action-review.md")
