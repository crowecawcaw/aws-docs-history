# Concepts and best practice for AWS Billing Conductor

This section highlights some best practices for when you're working with AWS Billing Conductor.

## Controlling access to AWS Billing Conductor

The AWS Billing Conductor is only accessible to users who have access to the payer or management account. To grant IAM users permission to create billing groups and see the AWS Billing Conductor Key Performance Indicators (KPIs) in the Billing and Cost Management console, you must also grant IAM users the following:

- List accounts within Organizations

To learn more about giving users the ability to create billing groups and pricing plans in the AWS Billing Conductor console, see [Identity and access management for AWS Billing Conductor](security-iam.md "security-iam.md").

You can also create AWS Billing Conductor resources programmatically using the AWS Billing Conductor API. When you configure access to the AWS Billing Conductor API, we recommend creating a unique IAM user for allowing programmatic access. This helps you define more precise access controls between who in your organization has access to the AWS Billing Conductor console, and the API. To give multiple IAM users query access to the AWS Billing Conductor API, we recommend creating a programmatic access IAM role for each.

## Understanding how the primary account join and leave date affect pro forma billing

This section applies only when using Billing Conductor as a standalone service without billing transfer enabled.

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

**Example: Using Billing Conductor as a standalone service**

In this example, we have two billing groups, `A` and `B`. Billing group `A` starts the billing period with accounts 1 through 3 in the group. At mid-month, the payer account moves `Account 3` to `Billing Group B`. At that point, the re-computation of the costs for Billing Groups `A` and `B` are required to accurately model the latest change. When `Account 3` is moved, `Billing Group A`’s usage is modeled as if `Account 3` was not a part of the billing group during the current billing period. Additionally, `Billing Group B`’s usage is modeled as if `Account 3` was a part of `Billing Group B` since the beginning of the billing period. This approach eliminates the need to calculate complex rates and chargeback models when accounts move across groups within the billing period.

From the member account's stance, the new billing group's settings are applied to the account's usage for the entire month when `Account 3` moves from one new billing group to another in the middle of the month. This is reflected in Cost Explorer and Bills as if the account has been apart of the new billing group from the start of the month.

| Billing Group A | Days: 1<br>• 15 | Days: 16<br>• 30 | End of Month |
| --------------- | --------------- | ---------------- | ------------ |
| Account 1       | $ 100           | $ 100            | $ 200        |
| Account 2       | $ 100           | $ 100            | $ 200        |
| Account 3       | $ 100           | N/A              | N/A          |
| **Total**       | **$ 300**       | **$ 200**        | **$ 400**    |

| Billing Group B | Days: 1<br>• 15 | Days: 16<br>• 30 | End of Month |
| --------------- | --------------- | ---------------- | ------------ |
| Account 4       | $ 100           | $ 100            | $ 200        |
| Account 5       | $ 100           | $ 100            | $ 200        |
| Account 6       | $ 100           | $ 100            | $ 200        |
| Account 3       | $ 100           | $ 100            | $ 200        |
| **Total**       | **$ 400**       | **$ 400**        | **$ 800**    |

**Example: Using Billing Conductor with billing transfer**

Unlike standalone Billing Conductor users, billing transfer users don't manually configure billing groups. However, pro forma and chargeable data changes occur when linked accounts are added to or removed from AWS Organizations, or when the bill transfer account modifies the pricing configuration.

## Billing Conductor with two-level billing transfers

Billing transfer supports two-level transfers for selected accounts. A bill transfer account can transfer its own bill and all its bill source account bills to an external management account (bill transfer receiver). This receiving account is responsible for paying both the bills from the two-levels-down bill source accounts and the bills from the intermediary bill transfer account, which becomes a bill source account by transferring its bill.

For more information about two-level transfers, see [Billing transfer quotas](../../../awsaccountbilling/latest/aboutv2/orgs_transfer_billing-quotas.md "../../../awsaccountbilling/latest/aboutv2/orgs_transfer_billing-quotas.md").

| Account roles in billing transfer configurations | Account role                                                                                                                                                        | One-level transfer                                                                                                                                                                                                                                                                                                                                                | Two-level transfer |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| Bill source account                              | Generates a consolidated bill and transfers it to an external management account                                                                                    | Generates a consolidated bill and transfers it to an external management account                                                                                                                                                                                                                                                                                  |
| Bill transfer account                            | Not applicable                                                                                                                                                      | Transfers its own bill and bill source account bills to a bill transfer receiver account. Acts as a bill transfer account for bill source accounts and as a bill source account for the bill transfer receiver. Uses Billing Conductor to manage pricing visible to bill source accounts.                                                                         |
| Bill transfer receiver                           | Receives and pays consolidated bills from the bill source account and its own account. Uses Billing Conductor to manage pricing visible to the bill source account. | Receives and pays consolidated bills from all bill source accounts (includinging the bill transfer account) and its own account. Uses Billing Conductor to manage pricing for all bill source accounts. Only the bill transfer account sees costs priced by the bill transfer receiver, while bill source accounts see costs priced by the bill transfer account. |

**Example 1: Conglomerate business**

Each subsidiary has multiple business units. The media conglomerate implements a central FinOps strategy to incentivize the use of specific AWS services across the business, modernize their infrastructure, and lower overall cloud costs.

**Usage flow**

- The AWS usage of `Business Unit_1.1` (Bill Source `accountID 123`) is $15, based on standard AWS standard computation.
- The AWS usage of the `Subsidiary_1` (`accountID 456`) is $30, based on standard AWS standard computation.
- The AWS usage of the `Conglomerate_A` (Bill Transfer-Bill Receiver `accountID 789`) is $10, based on standard AWS standard computation.

**Payment flow**

`Conglomerate_A` (`accountID 789`) receives three separate consolidated bills and invoices for each account's usage. They pay AWS a total of $55.

**Showback and chargeback flows**

`Conglomerate_A` (bill transfer receiver, `accountID 789`) charges `Subsidiary_1` (bill transfer `accountID 456`) $14 for the usage of Business Unit_1.1 (Bill source `accountID 123`) and $29 for the usage of the Subsidiary 1 (Bill Transfer `accountID 456`) to reward them in using the recommended AWS services.

In the AWS Billing and Cost Management console, `Subsidiary_1` views only `Business Unit_1.1`'s costs (`accountID 123`) at $14 and their own costs (`accountID 456`) at $29, as set by `Conglomerate_A`. `Subsidiary_1` pays `Conglomerate_A` $43 for the combined usage.

To provide incentives for improved budgeting operations, `Subsidiary_1` charges `Business Unit_1.1` $13.50.

In the AWS Billing and Cost Management console, `Business Unit_1.1` views only their own costs at $13.50, as set by `Subsidiary_1`.

**Example 2: Distribution reselling business**

Company B is a distributor reselling AWS services. The distributor receives AWS Partner Network (APN) discounts to support AWS expansion. The distributor resells to their partners (downstream sellers), who then resell to end customers. Both distributors and downstream sellers share the APN discount and charge end customers based on public, pre-discounted pricing.

**Usage flow**

- The AWS usage of end-customer (Bill Source account ID 123) is $20 (based on standard AWS standard computation)
- The AWS of the Downstream seller (Bill transfer account ID 456) is $2 (based on standard AWS standard computation)
- The AWS usage of the Distributor (Bill Transfer-Bill Receiver account ID 789) is $1 (based on standard AWS standard computation)

**Payment flow**

The Distributor (Bill Transfer Account-Bill Receiver account ID 789) will receive three different consolidated bills and invoices for the usage of each account, and will pay a total of $23 to AWS.

**Showback and chargeback flows**

The Distributor (Bill Transfer-Bill Receiver account ID 789) charges back the Downstream seller (Bill Transfer account ID 456) $21 for the usage of end-customer account (Bill Source account ID 123) and $3 for the usage of the Bill Transfer account (ID 456). Downstream seller exclusively views the costs of end-customer (bill source ID 123) priced at $21 in its Billing and Cost Management console. Downstream seller exclusively views its own costs for its Bill Transfer account (ID 456) priced at $3.

The Downstream seller will charge back $22 to the End-Customer (for example, public pricing).

###### Note

For two-level billing transfers:

The bill transfer receiver account doesn't need to send invitations to bill source accounts. Only the bill transfer account sends invitations. When a bill source account accepts the invitation, the bill transfer receiver receives a CloudWatch notification andand automatically takes over billing for the bill source accounts.

The bill transfer receiver account must configure a billing group manually in the bill source accounts' AWS Organizations through Billing Conductor. This configuration enables the bill transfer account to view their bill source account costs as allocated by the bill transfer receiver. For APN Distribution program users, this enables downstream sellers to see how much they owe their distributor for their end customers' usage.

For help with automating this process, contact Support.
