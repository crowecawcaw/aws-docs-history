# Understanding Consolidated Bills

If you manage an organization in AWS Organizations, you can use consolidated billing to view aggregated usage costs for accounts in the organization. Consolidated billing can also help you reduce those costs. For example, to ensure that you pay the lowest available prices for AWS products and services, AWS offers pricing tiers that reward higher usage with lower prices and discounted rates for purchasing instances in advance (known as _reservations_ or _Reserved Instances_). Using consolidated billing, you can combine usage from multiple accounts into a single invoice, allowing you to reach the tiers with lower prices faster. You can also apply unused reservations from one account to another account's instance usage.

###### Note

You can use billing transfer to get centralized access to cost management data and individual consolidated bills from multiple AWS Organizations.

When you transfer billing to an external management account, the computation boundary of each AWS Organizations remains unchanged. Charges and discounts (including Reserved Instances and Savings Plans) are calculated at the individual AWS Organizations level. For more information, see [Transfer billing management to external accounts](orgs_transfer_billing.md "orgs_transfer_billing.md").

###### Topics

- [Calculating Consolidated Bills](#Calculating "#Calculating")
- [Pricing Tiers](#Blended_Rate_Overview "#Blended_Rate_Overview")
- [Reserved Instances](#Instance_Reservations "#Instance_Reservations")
- [Savings Plans](#cb_savingsplans "#cb_savingsplans")
- [Blended Rates and Costs](#Blended_CB "#Blended_CB")

## Calculating Consolidated Bills

In an organization, the management account is responsible for paying all charges that the member accounts incur. If you're an administrator of a management account and you have the appropriate permissions, you can view aggregated usage costs for Reserved Instance discounts and volume tiering for all member accounts. You can also view the charges that individual member accounts incur, because AWS creates a separate bill for each member account based on that account’s usage. AWS also includes invoice summaries for each account in the management account invoice. During each billing period, AWS calculates your estimated charges several times each day so that you can track your costs as your organization incurs them. Your bill is not finalized until the beginning of the next month.

###### Note

Like member accounts, a management account can incur usage charges. However, as a best
practice you shouldn't use the management account to run AWS services. An exception is
for services and resources that are required to manage the organization itself. For
example, as part of managing your consolidated billing you might create an S3 bucket
in the management account to store AWS Cost and Usage Reports.

## Pricing Tiers

Some AWS services are priced in _tiers_, which specify unit costs
for defined amounts of AWS usage. As your usage increases, your usage crosses
thresholds into new pricing tiers that specify lower unit costs for additional usage in
a month. Your AWS usage is measured every month. To measure usage, AWS treats all
accounts in an organization as a single account. Member accounts don't reach tier
thresholds individually. Instead, all usage in the organization is aggregated for each
service, which ensures faster access to lower-priced tiers. As each month begins, your
service usage is reset to zero.

Each AWS service publishes its pricing information independently. You can access all
individual pricing pages from the [AWS
Pricing](http://aws.amazon.com/pricing/ "http://aws.amazon.com/pricing/") page.

### Calculating Costs for Amazon S3 Standard Storage

The following table shows an example of pricing tiers (your costs might vary). For
more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

**Amazon S3 Pricing Tiers**

| Tier description  | Price per GB | Price per TB |
| ----------------- | ------------ | ------------ |
| First 1 TB/month  | $0.10        | $100.00      |
| Next 49 TB/month  | $0.08        | $80.00       |
| Next 450 TB/month | $0.06        | $60          |

The following table shows Amazon S3 usage for an organization that includes a management account and three member accounts.

**Example S3 Usage Blended Cost**

| Account           | Tier           | Storage amount (GB) | Storage amount (TB) | Unblended rate (/GB) | Unblended rate (/TB) | Unblended cost |
| ----------------- | -------------- | ------------------- | ------------------- | -------------------- | -------------------- | -------------- |
| Management        | First TB/month | 1,000               | 1                   | $0.10                | 100                  | $100.00        |
| Next 49 TB/month  | 49,000         | 49                  | $0.08               | 80                   | $3,920.00            |
| Next 450 TB/month | 45,000         | 45                  | $0.06               | 60                   | $2,700.00            |
| **Total**         |                | **95,000**          | **95**              |                      |                      | **$6,720.00**  |

| Account           | Tier           | Storage amount (GB) | Storage amount (TB) | Unblended rate (/GB) | Unblended rate (/TB) | Unblended cost | Blended rate (/GB)<br>(=$6,720/95,000) | Blended rate (/TB)<br>(=$6,720/95) | Blended cost<br>(= Blended rate \<br>• storage) |
| ----------------- | -------------- | ------------------- | ------------------- | -------------------- | -------------------- | -------------- | -------------------------------------- | ---------------------------------- | ----------------------------------------------- |
| Member 1          | First TB/month | 1,000               | 1                   | $0.10                | 100                  | $100.00        | 0.070737                               | 70.737                             | $70.37                                          |
| Next 49 TB/month  | 14,000         | 14                  | $0.08               | 80                   | $1,120.00            | 0.070737       | 70.737                                 | $990.318                           |
| Next 450 TB/month | 15,000         | 15                  | $0.06               | 60                   | $900.00              | 0.070737       | 70.737                                 | $1,061.055                         |

| Account           | Tier             | Storage amount (GB) | Storage amount (TB) | Unblended rate (/GB) | Unblended rate (/TB) | Unblended cost | Blended rate (/GB)<br>(=$6,720/95,000) | Blended rate (/TB)<br>(=$6,720/95) | Blended cost<br>(= Blended rate \<br>• storage) |
| ----------------- | ---------------- | ------------------- | ------------------- | -------------------- | -------------------- | -------------- | -------------------------------------- | ---------------------------------- | ----------------------------------------------- |
| Member 2          | Next 49 TB/month | 20,000              | 20                  | $0.08                | 80                   | $1,600.00      | 0.070737                               | 70.737                             | $1,414.74                                       |
| Next 450 TB/month | 15,000           | 15                  | $0.06               | 60                   | $900.00              | 0.070737       | 70.737                                 | $1,061.55                          |

| Account           | Tier             | Storage amount (GB) | Storage amount (TB) | Unblended rate (/GB) | Unblended rate (/TB) | Unblended cost | Blended rate (/GB)<br>(=$6,720/95,000) | Blended rate (/TB)<br>(=$6,720/95) | Blended cost<br>(= Blended rate \<br>• storage) |
| ----------------- | ---------------- | ------------------- | ------------------- | -------------------- | -------------------- | -------------- | -------------------------------------- | ---------------------------------- | ----------------------------------------------- |
| Member 3          | Next 49 TB/month | 15,000              | 15                  | $0.08                | 80                   | $1,200.00      | 0.070737                               | 70.737                             | $1,061.55                                       |
| Next 450 TB/month | 15,000           | 15                  | $0.06               | 60                   | $900.00              | 0.070737       | 70.737                                 | $1,061.55                          |

The costs in the preceding table are calculated as follows:

1. All usage for the organization adds up to 95 TB or 95,000 GB. This is rolled
   up into the management account for recording purposes. The management account has no
   usage of its own. Only the member accounts incur usage. Member 1 uses 1 TB of
   storage. This satisfies the first pricing tier for the organization. The second
   pricing tier is satisfied by all three member accounts (14 TB for member 1 + 20
   TB for member 2 + 15 TB for member 3 = 49 TB). The third pricing tier is applied
   to any usage over 49 TB. In this example, the third pricing tier is applied to
   total member account usage of 45 TB.
2. The total cost is calculated by adding the cost of the first TB (1,000 GB \*
   $0.10 = 1 TB \* $100.00 = $100.00) to the cost of the next 49 TB (49,000 GB \*
   $0.08 = 49 TB \* $80.00 = $3920.00) and the cost of the remaining 45 TB (45,000
   GB \* $0.06 = 45 TB \* $60.00 = $2700.00), for a total of $6,720 ($100.00 +
   $3920.00 + $2700.00 = $6720.00).

The preceding example shows how using consolidated billing in AWS Organizations helps lower the
overall monthly cost of storage. If you calculate the cost for each member account
separately, the total cost is $7,660 rather than $6,720. By aggregating the usage of the
three accounts, you reach the lower-priced tiers sooner. The most expensive storage, the
first TB, is charged at the highest price just once, rather than three times. For
example, three TB of storage at the most expensive rate of $100/TB would result in a
charge of $300. Charging this storage as 1 TB ($100) and two additional TB at $80 ($160)
results in a total charge of $260.

## Reserved Instances

AWS also offers discounted hourly rates in exchange for an upfront fee and term
contract.

### Zonal Reserved Instances

A Reserved Instance is a reservation that provides a discounted hourly rate in
exchange for an upfront fee and term contract. Services such as Amazon Elastic Compute Cloud ([Amazon EC2](http://aws.amazon.com/ec2/reserved-instances/ "http://aws.amazon.com/ec2/reserved-instances/")) and Amazon Relational Database Service
([Amazon RDS](http://aws.amazon.com/rds/reserved-instances/ "http://aws.amazon.com/rds/reserved-instances/")) use this
approach to sell reserved capacity for hourly use of _Reserved
Instances_. It is not a virtual machine. It is a commitment to pay in
advance for specific Amazon EC2 or Amazon RDS instances. In return, you get a discounted rate
as compared to On-Demand Instance usage. From a technical perspective, there is no
difference between a Reserved Instance and an On-Demand Instance. When you launch an
instance, AWS checks for qualifying usage across all accounts in an organization
that can be applied to an active reservation. For more information, see [Reserved
Instances](../../../AWSEC2/latest/UserGuide/concepts-on-demand-reserved-instances.md "../../../AWSEC2/latest/UserGuide/concepts-on-demand-reserved-instances.md") in the _Amazon EC2 User Guide_ and [Working with
Reserved DB Instances](../../../AmazonRDS/latest/DeveloperGuide/USER_WorkingWithReservedDBInstances.md "../../../AmazonRDS/latest/DeveloperGuide/USER_WorkingWithReservedDBInstances.md") in the
_Amazon Relational Database Service Developer Guide_.

When you reserve capacity with Reserved Instances, your hourly usage is calculated
at a discounted rate for instances of the same usage type in the same Availability
Zone.

### Regional Reserved Instances

Regional Reserved Instances don't reserve capacity. Instead, they provide
Availability Zone flexibility and in certain cases instance size flexibility.
Availability Zone flexibility allows you to run one or more instances in any
Availability Zone in your reserved AWS Region. The Reserved Instance discount is
applied to any usage in any Availability Zone. Instance size flexibility provides
the Reserved Instance discount to instance usage regardless of size, within that
instance family. Instance size flexibility applies to only regional Reserved
Instances on the Linux/Unix platform with default tenancy. For more information
about regional Reserved Instances, see [Reservation Details](../../../cur/latest/userguide/reservation-columns.md "../../../cur/latest/userguide/reservation-columns.md") in the _Cost and Usage Reports Guide_ in this documentation and [Applying Reserved Instances](../../../AWSEC2/latest/UserGuide/concepts-reserved-instances-application.md#apply_ri "../../../AWSEC2/latest/UserGuide/concepts-reserved-instances-application.md#apply_ri") in the [Amazon Elastic Compute Cloud
User Guide for Linux Instances](../../../AWSEC2/latest/UserGuide.md "../../../AWSEC2/latest/UserGuide.md").

### Calculating Costs for Amazon EC2 with Reserved

Instances

AWS calculates the charges for Amazon EC2 instances by aggregating all the EC2 usage
for a specific instance type in a specific AWS Region for an organization.

#### Calculation Process

AWS calculates blended rates for Amazon EC2 instances using the following
logic:

1. AWS aggregates usage for all accounts in an organization for the
   month or partial month, and calculates costs based on unblended rates
   such as rates for On-Demand and Reserved Instances. Line items for these
   costs are created for the management account. This bill computation model
   attempts to apply the lowest unblended rates that each line item is
   eligible for. The allocation logic first applies Reserved Instance
   hours, then free tier hours, and then On-Demand rates to any remaining
   usage. In the AWS Cost and Usage Reports, you can see line items for these aggregated
   costs.
2. AWS identifies each Amazon EC2 usage type in each AWS Region and
   allocates cost from the aggregated management account to the corresponding
   member account line items for identical usage types in the same region.
   In the AWS Cost and Usage Reports, the **Unblended Rate**
   column shows that rate applied to each line item.

###### Note

When AWS assigns Reserved Instance hours to member accounts, it always starts with the account that purchased the reservation. If there are hours from the capacity reservation left over, AWS applies them to other accounts that operate identical usage types in the same Availability Zone.

AWS allocates a regional RI by instance size: The RI is applied
first to the smallest instance in the instance family, then to the
next smallest, and so on. AWS applies an RI or a fraction of an RI
based on the [normalization factor](../../../AWSEC2/latest/UserGuide/apply_ri.md#apply-regional-ri "../../../AWSEC2/latest/UserGuide/apply_ri.md#apply-regional-ri") of the instance. The order in
which AWS applies RIs doesn't result in a price difference.

When you transfer billing to an external management account, the computation boundary of each AWS Organizations remains unchanged. Charges and discounts (including Reserved Instances and Savings Plans) are calculated at the individual AWS Organizations level. For more information, see [Transfer billing management to external accounts](orgs_transfer_billing.md "orgs_transfer_billing.md").

## Savings Plans

Savings Plans is a flexible pricing model that can help you reduce your AWS usage bill.
Compute Savings Plans enables you to commit to an amount each hour, and receive discounted Amazon EC2, Fargate, and AWS Lambda usage up to that amount.

###### Note

When you use billing transfer, Savings Plans apply only to the AWS Organizations where they're purchased, regardless of which account pays the bill. You can't purchase or share Savings Plans across multiple AWS Organizations.

### Calculating Costs with Savings Plans

AWS calculates the charges for Amazon EC2, Fargate, and AWS Lambda by aggregating all usage that's not covered by Reserved Instances, and applying the Savings Plans rates starting with the highest discount.

The Savings Plans are applied to the account that owns the Savings Plans. Then, it is shared with other accounts in the AWS organization. For more information, see [Understanding How Savings Plans are Applied to Your Usage](../../../savingsplans/latest/userguide/sp-applying.md "../../../savingsplans/latest/userguide/sp-applying.md") in the _Savings Plans User Guide_.

###### Note

When you transfer billing to an external management account, the computation boundary of each AWS Organizations remains unchanged. Charges and discounts (including Reserved Instances and Savings Plans) are calculated at the individual AWS Organizations level. For more information, see [Transfer billing management to external accounts](orgs_transfer_billing.md "orgs_transfer_billing.md").

## Blended Rates and Costs

Blended rates are the averaged rates of the Reserved Instances and On-Demand Instances
that are used by member accounts in an organization in AWS Organizations. AWS calculates
blended costs by multiplying the blended rate for each service with an account’s usage
of that service.

###### Note

- AWS shows each member account their charges as unblended costs. AWS continues to apply
  all of the consolidated billing benefits such as reservations and tiered prices across all member
  accounts in AWS Organizations.
- Blended rates for Amazon EC2 are calculated at the hourly level.

This section includes examples that show how AWS calculates blended
rates for the following services.

- [Calculating Blended Rates for Amazon S3
  Standard Storage](#Blended_S3_Stand_Storage "#Blended_S3_Stand_Storage")
- [Calculating Blended Rates for Amazon EC2](#blended-rate-example "#blended-rate-example")

### Calculating Blended Rates for Amazon S3

Standard Storage

AWS calculates blended rates for Amazon S3 standard storage by taking the total
cost of storage and dividing by the amount of data stored per month.

Using the
example from [Calculating Consolidated Bills](#Calculating "#Calculating") where we calculated a cost of $6,720 for a management account and three member accounts, we calculate the blended rates for the
accounts using the following logic:

1. The blended rate in GB is calculated by dividing the total cost
   ($6,720) by the amount of storage (95,000 GB) to produce a blended rate
   of $0.070737/GB. The blended rate in TB is calculated by dividing the
   total cost ($6,720) by the amount of storage (95 TB) to produce a
   blended rate of $70.737/TB.
2. The blended cost for each member account is allocated by multiplying
   the blended rate (for GB or TB) by the usage, resulting in the amounts
   listed in the Blended Cost column. For example, Member 1 uses 14,000 GB
   of storage priced at the blended rate of $0.070737 (or 14 TB priced at
   $70.737) for a blended cost of $990.318.

### Calculating Blended Rates for Amazon EC2

The consolidated billing logic aggregates
Amazon EC2 costs to the management account and then allocates it to the member accounts
based on proportional usage.

For this example, all usage is of the same usage
type, occurs in the same Availability Zone, and is for the same Reserved
Instance term. This example covers Full Upfront and Partial Upfront Reserved
Instances.

The following table shows line items that represent the calculation of line
items for Amazon EC2 usage for a 720-hour (30-day) month. Each instance is of the
same usage type (`t2.small`) running in the same Availability Zone.
The organization has purchased three Reserved Instances for a one-year term.
Member Account 1 has three Reserved Instances. Member Account 2 has no Reserved
Instances, but uses an On-Demand Instance.

| Line item account   | Billing type    | Usage type | Upfront cost | Monthly cost | Usage available | Usage quantity | Unblended rate | Unblended cost | Blended rate | Blended cost |
| ------------------- | --------------- | ---------- | ------------ | ------------ | --------------- | -------------- | -------------- | -------------- | ------------ | ------------ |
| Management account  | RI, All upfront | t2.small   | $274.00      | $0.00        | -               | 1440           | -              | -              | -            | -            |
| RI, Partial upfront | t2.small        | $70.00     | $5.84        | -            | 720             | -              | -              | -              | -            |
| Member account 1    | RI applied      | t2.small   | -            | -            | 1440            | 1440           | $0.00          | $0.00          | $0.00575     | $8.28        |
| RI applied          | t2.small        | -          | -            | 720          | 720             | $0.00          | $0.00          | $0.00575       | $4.14        |
| Member account 2    | On-Demand       | t2.small   | -            | -            | -               | 720            | $0.023         | $16.56         | $0.00575     | $4.14        |
| **Total**           |                 |            |              |              | **2160**        | **2880**       |                | **$16.56**     |              | **$16.56**   |

The data in the preceding table shows the following information:

- The organization purchased 1,440 hours of Reserved Instance capacity
  at a Full Upfront rate (two EC2 instances).
- The organization purchased 720 hours of Reserved Instance capacity at
  a Partial Upfront rate (one EC2 instance).
- Member account 1 completely uses the two Full Upfront Reserved Instances and the one Partial Upfront Reserved Instance for a total usage of 2,160 hours. Member account 2 uses 720 hours of an On-Demand Instance. Total usage for the organization is 2,880 hours (2160 + 720 = 2,880).
- The unblended rate for the three Reserved Instances is $0.00. The
  unblended cost of an RI is always $0.00 because RI charges are not
  included in blended rate calculations.
- The unblended rate for the On-Demand Instance is $0.023. Unblended
  rates are associated with the current price of the product. They can't
  be verified from information in the preceding table.
- The blended rate is calculated by dividing the total cost ($16.56) by the total amount of Amazon EC2 usage (2,880 hours). This produces a rate of $0.005750000 dollars per hour.
