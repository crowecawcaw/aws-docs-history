# Reserved DB instances for Amazon Aurora

Using reserved DB instances, you can reserve a DB instance for a one- or three-year term. Reserved DB instances provide you with a
significant discount compared to on-demand DB instance pricing. Reserved DB instances are not physical instances, but rather a
billing discount applied to the use of certain on-demand DB instances in your account. Discounts for reserved DB instances are tied
to instance type and AWS Region.

The general process for working with reserved DB instances is: First get information about available reserved DB instance
offerings, then purchase a reserved DB instance offering, and finally get information about your existing reserved DB
instances.

For information about purchasing reserved DB instances and viewing the billing for reserved DB instances, see the following sections.

- [Purchasing reserved DB instances for Amazon Aurora](USER_WorkingWithReservedDBInstances.md "USER_WorkingWithReservedDBInstances.md")
- [Viewing the billing for reserved DB instances for Amazon Aurora](reserved-instances-billing.md "reserved-instances-billing.md")

## Overview of reserved DB

instances

When you purchase a reserved DB instance in Amazon RDS, you purchase a commitment to getting a discounted rate, on a specific DB
instance type, for the duration of the reserved DB instance. To use an Amazon RDS reserved DB instance, you create a new DB instance
just like you do for an on-demand instance.

The new DB instance that you create must have the same specifications as the reserved DB instance for the following:

- AWS Region
- DB engine (The DB engine's version number doesn't need to match.)
- DB instance type

If the specifications of the new DB instance match an existing reserved DB instance for your account, you are billed at the
discounted rate offered for the reserved DB instance. Otherwise, the DB instance is billed at an on-demand rate.

You can modify a DB instance that you're using as a reserved DB instance. If the modification is within the specifications of
the reserved DB instance, part or all of the discount still applies to the modified DB instance. If the modification is outside
the specifications, such as changing the instance class, the discount no longer applies. For more information, see [Size-flexible reserved DB instances](#USER_WorkingWithReservedDBInstances.SizeFlexible "#USER_WorkingWithReservedDBInstances.SizeFlexible").

###### Topics

- [Offering types](#USER_WorkingWithReservedDBInstances.OfferingTypes "#USER_WorkingWithReservedDBInstances.OfferingTypes")
- [Aurora DB cluster configuration flexibility](#ReservedDBInstances.ClusterConfig "#ReservedDBInstances.ClusterConfig")
- [Size-flexible reserved DB instances](#USER_WorkingWithReservedDBInstances.SizeFlexible "#USER_WorkingWithReservedDBInstances.SizeFlexible")
- [Aurora reserved DB instance billing examples](#USER_WorkingWithReservedDBInstances.BillingExample "#USER_WorkingWithReservedDBInstances.BillingExample")
- [Deleting a reserved DB instance](#USER_WorkingWithReservedDBInstances.Cancelling "#USER_WorkingWithReservedDBInstances.Cancelling")

For more information about reserved DB instances, including pricing, see [Amazon RDS reserved instances](http://aws.amazon.com/rds/reserved-instances/#2 "http://aws.amazon.com/rds/reserved-instances/#2").

### Offering types

Reserved DB instances are available in three varieties—No Upfront, Partial Upfront, and All Upfront—that let
you optimize your Amazon RDS costs based on your expected usage.

###### Note

Not all RDS instance classes support all Reserved Instance offering types. For
example, some instance classes might not offer the No Upfront option. To confirm
availability, review the Reserved Instance offerings in the AWS Management Console or use the
`describe-reserved-db-instances-offerings` AWS CLI command.

**No Upfront**

This option provides access to a reserved DB instance without requiring an upfront payment. Your No Upfront
reserved DB instance bills a discounted hourly rate for every hour within the term, regardless of usage, and no
upfront payment is required. This option is only available as a one-year reservation.

**Partial Upfront**

This option requires a part of the reserved DB instance to be paid upfront. The remaining hours in the term
are billed at a discounted hourly rate, regardless of usage. This option is the replacement for the previous
Heavy Utilization option.

**All Upfront**

Full payment is made at the start of the term, with no other costs incurred for the remainder of the term
regardless of the number of hours used.

If you are using consolidated billing, all the accounts in the organization are treated as one account. This means that all accounts
in the organization can receive the hourly cost benefit of reserved DB instances that are purchased by any other account. For more
information about consolidated billing, see [Amazon RDS reserved DB instances](../../../awsaccountbilling/latest/aboutv2/consolidatedbilling-other.md#consolidatedbilling-rds "../../../awsaccountbilling/latest/aboutv2/consolidatedbilling-other.md#consolidatedbilling-rds")
in the _AWS Billing and Cost Management User Guide_.

### Aurora DB cluster configuration flexibility

You can use Aurora reserved DB instances with both DB cluster configurations:

- Aurora I/O-Optimized – You pay only for the usage and storage of your DB clusters, with no additional charges for read
  and write I/O operations.
- Aurora Standard – In addition to the usage and storage of your DB clusters, you also pay a standard rate per 1
  million requests for I/O operations.

Aurora automatically accounts for the price difference between these configurations. Aurora I/O-Optimized consumes
30% more normalized units per hour than Aurora Standard.

For more information about Aurora cluster storage configurations, see [Storage configurations for Amazon Aurora DB
clusters](Aurora.Overview.md#aurora-storage-type "Aurora.Overview.md#aurora-storage-type"). For more information about pricing for Aurora
cluster storage configurations, see [Amazon Aurora pricing](https://aws.amazon.com/rds/aurora/pricing/ "https://aws.amazon.com/rds/aurora/pricing/").

### Size-flexible reserved DB instances

When you purchase a reserved DB instance, one thing that you specify is the instance class, for example db.r5.large. For
more information about DB instance classes, see [Amazon Aurora DB instance classes](Concepts.md "Concepts.md").

If you have a DB instance, and you need to scale it to larger capacity, your reserved DB instance is automatically applied
to your scaled DB instance. That is, your reserved DB instances are automatically applied across all DB instance class
sizes. Size-flexible reserved DB instances are available for DB instances with the same AWS Region and database engine.
Size-flexible reserved DB instances can only scale in their instance class type. For example, a reserved DB instance for a
db.r6i.large can apply to a db.r6i.xlarge, but not to a db.r6id.large or db.r7g.large, because db.r6id.large and db.r7g.large are different instance class
types.

Size-flexible reserved DB instances are available for the following Aurora database engines:

- Aurora MySQL
- Aurora PostgreSQL

You can compare usage for different reserved DB instance sizes by using normalized units per hour. For example, one unit
of usage on two db.r3.large DB instances is equivalent to eight normalized units per hour of usage on one db.r3.small. The
following table shows the number of normalized units per hour for each DB instance size.

| Instance size | Normalized units per hour for one DB instance, Aurora Standard | Normalized units per hour for one DB instance, Aurora I/O-Optimized | Normalized units per hour for three DB instances (writer and two readers), Aurora Standard | Normalized units per hour for three DB instances (writer and two readers), Aurora I/O-Optimized |
| ------------- | -------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| small         | 1                                                              | 1.3                                                                 | 3                                                                                          | 3.9                                                                                             |
| medium        | 2                                                              | 2.6                                                                 | 6                                                                                          | 7.8                                                                                             |
| large         | 4                                                              | 5.2                                                                 | 12                                                                                         | 15.6                                                                                            |
| xlarge        | 8                                                              | 10.4                                                                | 24                                                                                         | 31.2                                                                                            |
| 2xlarge       | 16                                                             | 20.8                                                                | 48                                                                                         | 62.4                                                                                            |
| 4xlarge       | 32                                                             | 41.6                                                                | 96                                                                                         | 124.8                                                                                           |
| 8xlarge       | 64                                                             | 83.2                                                                | 192                                                                                        | 249.6                                                                                           |
| 12xlarge      | 96                                                             | 124.8                                                               | 288                                                                                        | 374.4                                                                                           |
| 16xlarge      | 128                                                            | 166.4                                                               | 384                                                                                        | 499.2                                                                                           |
| 24xlarge      | 192                                                            | 249.6                                                               | 576                                                                                        | 748.8                                                                                           |
| 32xlarge      | 256                                                            | 332.8                                                               | 768                                                                                        | 998.4                                                                                           |

For example, suppose that you purchase a `db.t2.medium` reserved DB instance, and you have two running
`db.t2.small` DB instances in your account in the same AWS Region. In this case, the billing benefit is
applied in full to both instances.

![Applying a reserved DB instance in full to smaller DB instances](images/ri-db-instance-flex-full.png)

Alternatively, if you have one `db.t2.large` instance running in your account in the same AWS Region, the
billing benefit is applied to 50 percent of the usage of the DB instance.

![Applying a reserved DB instance in part to a larger DB instance](images/ri-db-instance-flex-partial.png)

###### Note

We recommend using the T DB instance classes only for development and test servers, or other non-production servers.
For more details on the T instance classes, see [DB instance class types](Concepts.DBInstanceClass.md "Concepts.DBInstanceClass.md").

### Aurora reserved DB instance billing examples

The following examples illustrate the pricing for reserved DB instances for Aurora DB clusters using both
the Aurora Standard and Aurora I/O-Optimized DB cluster configurations.

#### Example using Aurora Standard

The price for a reserved DB instance doesn't provide a discount for the costs associated with
storage, backups, and I/O. The following example illustrates the total cost per month for a reserved DB instance:

- An Aurora MySQL reserved Single-AZ db.r5.large DB instance class in US East (N. Virginia) at a cost of $0.19 per
  hour, or $138.70 per month
- Aurora storage at a cost of $0.10 per GiB per month (assume $45.60 per month for this example)
- Aurora I/O at a cost of $0.20 per 1 million requests (assume $20 per month for this example)
- Aurora backup storage at $0.021 per GiB per month (assume $30 per month for this example)

Add all of these options ($138.70 + $45.60 + $20 + $30) with the reserved DB instance, and the total cost per month is $234.30.

If you choose to use an on-demand DB instance instead of a reserved DB instance, an Aurora MySQL
Single-AZ db.r5.large DB instance class in US East (N. Virginia) costs $0.29 per hour, or $217.50 per month. So, for an
on-demand DB instance, add all of these options ($217.50 + $45.60 + $20 + $30), and the total cost per month is $313.10. You
save nearly $79 per month by using the reserved DB instance.

#### Example using an Aurora Standard DB cluster with two reader instances

To use reserved instances for Aurora DB clusters, simply purchase one reserved instance for each DB
instance in the cluster.

Extending the first example, you have an Aurora MySQL DB cluster with one writer DB instance and two
Aurora Replicas, for a total of three DB instances in the cluster. The two Aurora Replicas incur no extra storage or
backups charges. If you purchase three db.r5.large Aurora MySQL reserved DB instances, your cost will be $234.30 (for
the writer DB instance) + 2 \* ($138.70 + $20 I/O per Aurora Replica), for a total of $551.70 per month.

The corresponding on-demand cost for an Aurora MySQL DB cluster with one writer DB instance and two
Aurora Replicas is $313.10 + 2 \* ($217.50 + $20 I/O per instance) for a total of $788.10 per month. You save $236.40 per
month by using the reserved DB instances.

#### Example using Aurora I/O-Optimized

You can reuse your existing Aurora Standard reserved DB instances with Aurora I/O-Optimized. To fully use the benefits of your reserved
instance discounts with Aurora I/O-Optimized, you can buy 30% additional reserved instances similar to your current reserved
instances.

The following table shows examples of how to estimate the additional reserved instances when using Aurora I/O-Optimized. If the
required reserved instances are a fraction, you can take advantage of the size flexibility available with reserved
instances to get to a whole number. In these examples, "current" refers to the Aurora Standard reserved instances that you have
now. Additional reserved instances are the number of Aurora Standard reserved instances that you must buy to maintain your
current reserved instance discounts when using Aurora I/O-Optimized.

| DB instance class | Current Aurora Standard reserved instances | Reserved instances required for Aurora I/O-Optimized | Additional reserved instances needed | Additional reserved instances needed, using size flexibility                                                                                   |
| ----------------- | ------------------------------------------ | ---------------------------------------------------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| db.r6g.large      | 10                                         | 10 \<br>• 1.3 = 13                                   | 3 \<br>• db.r6g.large                | 3 \<br>• db.r6g.large                                                                                                                          |
| db.r6g.4xlarge    | 20                                         | 20 \<br>• 1.3 = 26                                   | 6 \<br>• db.r6g.4xlarge              | 6 \<br>• db.r6g.4xlarge                                                                                                                        |
| db.r6g.12xlarge   | 5                                          | 5 \<br>• 1.3 = 6.5                                   | 1.5 \<br>• db.r6g.12xlarge           | One each of db.r6g.12xlarge, r6g.4xlarge, and r6g.2xlarge<br>(0.5 \<br>• db.r6g.12xlarge = 1 \<br>• db.r6g.4xlarge + 1 \<br>• db.r6g.2xlarge ) |
| db.r6i.24xlarge   | 15                                         | 15 \<br>• 1.3 = 19.5                                 | 4.5 \<br>• db.r6i.24xlarge           | 4 \<br>• db.r6i.24xlarge + 1 \<br>• db.r6i.12xlarge<br>(0.5 \<br>• db.r6i.24xlarge = 1 \<br>• db.r6i.12xlarge)                                 |

#### Example using an Aurora I/O-Optimized DB cluster with two reader instances

You have an Aurora MySQL DB cluster with one writer DB instance and two Aurora Replicas, for a total
of three DB instances in the cluster. They use the Aurora I/O-Optimized DB cluster configuration. To use reserved DB instances for
this cluster, you would need to buy four reserved DB instances of the same DB instance class. Three DB instances using
Aurora I/O-Optimized consume 3.9 normalized units per hour, compared to 3 normalized units per hour for three DB instances using
Aurora Standard. However, you save the monthly I/O costs for each DB instance.

###### Note

The prices in these examples are sample prices and might not match actual prices. For Aurora pricing information, see
[Amazon Aurora pricing](https://aws.amazon.com/rds/aurora/pricing "https://aws.amazon.com/rds/aurora/pricing").

### Deleting a reserved DB instance

The terms for a reserved DB instance involve a one-year or three-year commitment. You can't cancel a reserved DB instance.
However, you can delete a DB instance that is covered by a reserved DB instance discount. The process for deleting a DB
instance that is covered by a reserved DB instance discount is the same as for any other DB instance.

You're billed for the upfront costs regardless of whether you use the resources.

If you delete a DB instance that is covered by a reserved DB instance discount, you can launch another DB instance with
compatible specifications. In this case, you continue to get the discounted rate during the reservation term (one or three
years).
