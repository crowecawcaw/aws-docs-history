# Viewing your pro forma data in AWS Budgets

AWS accounts in AWS Billing Conductor billing groups can monitor pro forma spendings using
AWS Budgets. Budgets created by AWS accounts in Billing Conductor billing groups capture the pro forma
billing data, enabling alerts when your pro forma spending limit is exceeding. The budget forecast
will also be based on the pro forma data, and you will be alerted when you are about to exceed
your spending limit as well.

Billing group primary accounts can monitor the holistic billing group pro forma spend, and
spending on specific billing group member accounts. Billing group managed accounts, or billing
group members, can create and view pro forma budgets of their own AWS accounts. These accounts
can see the budget history for the billing periods they were members of the billing group. Billing
data isn't shared from the budget history for dates prior to joining the billing group.

When accounts join a billing group, their existing budget information will begin capturing
pro forma data. The budget history and forecast are based on the pro forma data. When accounts
leave a billing group, the budget begins capturing billable data. The budget history and forecast
will be based on billable data going forward.

###### Note

We recommend linked accounts in billing groups, that previously had budget alerts configured on billable data, to update the threshold to the budget alerts to match the pro forma data view.

As a billing transfer user, only bill source accounts can use budgets and budget alerts. If a bill transfer account needs to set up a budget, they must obtain an IAM role in the bill source account.

For more information about AWS Budgets, see [Managing your costs with AWS Budgets](../../../cost-management/latest/userguide/budgets-managing-costs.md "../../../cost-management/latest/userguide/budgets-managing-costs.md") in the _AWS Cost Management User Guide_.
