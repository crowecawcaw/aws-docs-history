# Concepts and best practice for AWS Billing Conductor

This section highlights some best practices for when you're working with AWS Billing Conductor.

## Controlling access to AWS Billing Conductor

The AWS Billing Conductor is only accessible to users who have access to the payer or management account. To grant IAM users permission to create billing groups and see the AWS Billing Conductor Key Performance Indicators (KPIs) in the Billing and Cost Management console, you must also grant IAM users the following:

- List accounts within Organizations

To learn more about giving users the ability to create billing groups and pricing plans in the AWS Billing Conductor console, see [Identity and access management for AWS Billing Conductor](security-iam.md "security-iam.md").

You can also create AWS Billing Conductor resources programmatically using the AWS Billing Conductor API. When you configure access to the AWS Billing Conductor API, we recommend creating a unique IAM user for allowing programmatic access. This helps you define more precise access controls between who in your organization has access to the AWS Billing Conductor console, and the API. To give multiple IAM users query access to the AWS Billing Conductor API, we recommend creating a programmatic access IAM role for each.

## Understanding how the primary account join and leave date affect pro forma billing

The date when the primary account joined your Organization defines the historical boundary
for pro forma costs for that billing group. If you choose an account that joined your
Organization in the middle of the month as the primary account of a billing group, all accounts
in that billing group are not able to see their pro forma billing data for the first half of the
month. This is because the primary account wasn't a part of the Organization at that time.
Similarly, if the primary account left your Organization in the middle of the month, the accounts
in the billing group are not able to see pro forma billing from the date the primary account left
the Organization.

###### Note

The billing group is marked for deletion in the following month when the primary account leaves your Organization. To maintain pro forma billing for accounts in this billing group for the following months, we recommend you delete the billing group and create a new one. The new billing group can be created with a new primary account, or using the original account if it rejoined your Organization.

For example, your primary account joined your organization on October 15 and left on October 28. The pro forma billing data for all accounts in the billing group will only include the cost and usage between October 15 through the 28th. This is true even if other accounts are a part of the billing group for thee entire month of October.

To avoid discrepancy between the cost and usage datasets across the billable pro forma domains, ensure the account chosen as the primary account is a part of your Organization for the entire month.

## Understanding the AWS Billing Conductor update frequency

AWS billing data is updated at least once a day. AWS Billing Conductor uses this data to compute your pro forma billing data. Custom line items that are generated to apply to the current month are reflected within 24 hours. Custom line items that are generated to apply to the prior billing period might take up to 48 hours to reflect in a billing group AWS Cost and Usage Reports, or on the bills page for a given billing group.

## Understanding the AWS Billing Conductor computational logic

The AWS Billing Conductor computation is flexible to the changes that you make in a given month, while retaining the historical integrity of your prior period billing data. This is best described with an example.

In this example, we have two billing groups, `A` and `B`. Billing group `A` starts the billing period with accounts 1 through 3 in the group. At mid-month, the payer account moves `Account 3` to `Billing Group B`. At that point, the re-computation of the costs for Billing Groups `A` and `B` are required to accurately model the latest change. When `Account 3` is moved, `Billing Group A`’s usage is modeled as if `Account 3` was not a part of the billing group during the current billing period. Additionally, `Billing Group B`’s usage is modeled as if `Account 3` was a part of `Billing Group B` since the beginning of the billing period. This approach eliminates the need to calculate complex rates and chargeback models when accounts move across groups within the billing period.

From the member account's stance, the new billing group's settings are applied to the account's usage for the entire month when `Account 3` moves from one new billing group to another in the middle of the month. This is reflected in Cost Explorer and Bills as if the account has been apart of the new billing group from the start of the month.

| Billing Group A | Days: 1 - 15 | Days: 16 - 30 | End of Month |
| --------------- | ------------ | ------------- | ------------ |
| Account 1       | $ 100        | $ 100         | $ 200        |
| Account 2       | $ 100        | $ 100         | $ 200        |
| Account 3       | $ 100        | N/A           | N/A          |
| **Total**       | **$ 300**    | **$ 200**     | **$ 400**    |
| Billing Group B | Days: 1 - 15 | Days: 16 - 30 | End of Month |
| ---             | ---          | ---           | ---          |
| Account 4       | $ 100        | $ 100         | $ 200        |
| Account 5       | $ 100        | $ 100         | $ 200        |
| Account 6       | $ 100        | $ 100         | $ 200        |
| Account 3       | $ 100        | $ 100         | $ 200        |
| **Total**       | **$ 400**    | **$ 400**     | **$ 800**    |
