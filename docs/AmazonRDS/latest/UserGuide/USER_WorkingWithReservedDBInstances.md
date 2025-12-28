# Reserved DB instances for Amazon RDS

Using reserved DB instances, you can reserve a DB instance for a one- or three-year term. Reserved DB instances provide you with a
significant discount compared to on-demand DB instance pricing. Reserved DB instances are not physical instances, but rather a
billing discount applied to the use of certain on-demand DB instances in your account. Discounts for reserved DB instances are tied
to instance type and AWS Region.

The general process for working with reserved DB instances is: First get information about available reserved DB instance
offerings, then purchase a reserved DB instance offering, and finally get information about your existing reserved DB
instances.

For information about purchasing reserved DB instances and viewing the billing for reserved DB instances, see the following sections.

- [Purchasing reserved DB instances for Amazon RDS](USER_WorkingWithReservedDBInstances.md "USER_WorkingWithReservedDBInstances.md")
- [Viewing the billing for reserved DB instances for Amazon RDS](reserved-instances-billing.md "reserved-instances-billing.md")

## Overview of reserved DB

instances

When you purchase a reserved DB instance in Amazon RDS, you purchase a commitment to getting a discounted rate, on a specific DB
instance type, for the duration of the reserved DB instance. To use an Amazon RDS reserved DB instance, you create a new DB instance
just like you do for an on-demand instance.

The new DB instance that you create must have the same specifications as the reserved DB instance for the following:

- AWS Region
- DB engine (The DB engine's version number doesn't need to match.)
- DB instance type
- DB instance size (RDS for Db2, RDS for SQL Server, and RDS for Oracle License Included)
- Edition (RDS for Db2, RDS for SQL Server, and RDS for Oracle)
- License type (license-included or bring-your-own-license)

If the specifications of the new DB instance match an existing reserved DB instance for your account, you are billed at the
discounted rate offered for the reserved DB instance. Otherwise, the DB instance is billed at an on-demand rate.

You can modify a DB instance that you're using as a reserved DB instance. If the modification is within the specifications of
the reserved DB instance, part or all of the discount still applies to the modified DB instance. If the modification is outside
the specifications, such as changing the instance class, the discount no longer applies. For more information, see [Size-flexible reserved DB instances](#USER_WorkingWithReservedDBInstances.SizeFlexible "#USER_WorkingWithReservedDBInstances.SizeFlexible").

###### Topics

- [Offering types](#USER_WorkingWithReservedDBInstances.OfferingTypes "#USER_WorkingWithReservedDBInstances.OfferingTypes")
- [Size-flexible reserved DB instances](#USER_WorkingWithReservedDBInstances.SizeFlexible "#USER_WorkingWithReservedDBInstances.SizeFlexible")
- [Reserved DB instance
  billing example](#USER_WorkingWithReservedDBInstances.BillingExample "#USER_WorkingWithReservedDBInstances.BillingExample")
- [Reserved DB instances for a Multi-AZ DB cluster](#USER_WorkingWithReservedDBInstances.MultiAZDBClusters "#USER_WorkingWithReservedDBInstances.MultiAZDBClusters")
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

### Size-flexible reserved DB instances

When you purchase a reserved DB instance, one thing that you specify is the instance class, for example db.r5.large. For
more information about DB instance classes, see [DB instance classes](Concepts.md "Concepts.md").

If you have a DB instance, and you need to scale it to larger capacity, your reserved DB instance is automatically applied
to your scaled DB instance. That is, your reserved DB instances are automatically applied across all DB instance class
sizes. Size-flexible reserved DB instances are available for DB instances with the same AWS Region and database engine.
Size-flexible reserved DB instances can only scale in their instance class type. For example, a reserved DB instance for a
db.r6i.large can apply to a db.r6i.xlarge, but not to a db.r6id.large or db.r7g.large, because db.r6id.large and db.r7g.large are different instance class
types.

Reserved DB instance benefits apply to both Multi-AZ and Single-AZ configurations. This means that you can
move freely between configurations within the same DB instance class type. For example, you can move from a Single-AZ
deployment running on one large DB instance (four normalized units per hour) to a Multi-AZ deployment running on two medium
DB instances (2+2 = 4 normalized units per hour).

Size-flexible reserved DB instances are available for the following Amazon RDS database engines:

- RDS for Db2
- RDS for MariaDB
- RDS for MySQL
- RDS for Oracle, Bring Your Own License
- RDS for PostgreSQL

Size flexibility does not apply to RDS for SQL Server and RDS for Oracle License Included.

For details about using size-flexible reserved instances with
Aurora, see
[Reserved DB instances for Aurora](../AuroraUserGuide/USER_WorkingWithReservedDBInstances.md "../AuroraUserGuide/USER_WorkingWithReservedDBInstances.md").

You can compare usage for different reserved DB instance sizes by using normalized units per hour. For example, one unit
of usage on two db.r3.large DB instances is equivalent to eight normalized units per hour of usage on one db.r3.small. The
following table shows the number of normalized units per hour for each DB instance size.

| Instance size | Single-AZ normalized units per hour (deployment with one DB instance) | Multi-AZ DB instance normalized units per hour (deployment with one DB instance and one standby) | Multi-AZ DB cluster normalized units per hour (deployment with one DB instance and two standbys) |
| ------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| micro         | 0.5                                                                   | 1                                                                                                | 1.5                                                                                              |
| small         | 1                                                                     | 2                                                                                                | 3                                                                                                |
| medium        | 2                                                                     | 4                                                                                                | 6                                                                                                |
| large         | 4                                                                     | 8                                                                                                | 12                                                                                               |
| xlarge        | 8                                                                     | 16                                                                                               | 24                                                                                               |
| 2xlarge       | 16                                                                    | 32                                                                                               | 48                                                                                               |
| 4xlarge       | 32                                                                    | 64                                                                                               | 96                                                                                               |
| 6xlarge       | 48                                                                    | 96                                                                                               | 144                                                                                              |
| 8xlarge       | 64                                                                    | 128                                                                                              | 192                                                                                              |
| 10xlarge      | 80                                                                    | 160                                                                                              | 240                                                                                              |
| 12xlarge      | 96                                                                    | 192                                                                                              | 288                                                                                              |
| 16xlarge      | 128                                                                   | 256                                                                                              | 384                                                                                              |
| 24xlarge      | 192                                                                   | 384                                                                                              | 576                                                                                              |
| 32xlarge      | 256                                                                   | 512                                                                                              | 768                                                                                              |

For example, suppose that you purchase a `db.t2.medium` reserved DB instance, and you have two running
`db.t2.small` DB instances in your account in the same AWS Region. In this case, the billing benefit is
applied in full to both instances.

![Applying a reserved DB instance in full to smaller DB instances](images/ri-db-instance-flex-full.png)

Alternatively, if you have one `db.t2.large` instance running in your account in the same AWS Region, the
billing benefit is applied to 50 percent of the usage of the DB instance.

![Applying a reserved DB instance in part to a larger DB instance](images/ri-db-instance-flex-partial.png)

### Reserved DB instance

billing example

The price for a reserved DB instance doesn't provide a discount for the costs associated with
storage, backups, and I/O. It provides a discount only on the hourly, on-demand instance usage. The following example
illustrates the total cost per month for a reserved DB instance:

- An RDS for MySQL reserved Single-AZ db.r5.large DB instance class in US East (N. Virginia) with the No Upfront option
  at a cost of $0.12 for the instance, or $90 per month
- 400 GiB of General Purpose SSD (gp2) storage at a cost of 0.115 per GiB per month, or $45.60 per month
- 600 GiB of backup storage at $0.095, or $19 per month (400 GiB free)

Add all of these charges ($90 + $45.60 + $19) with the reserved DB instance, and the total cost per
month is $154.60.

If you choose to use an on-demand DB instance instead of a reserved DB instance, an RDS for MySQL
Single-AZ db.r5.large DB instance class in US East (N. Virginia) costs $0.1386 per hour, or $101.18 per month. So, for an
on-demand DB instance, add all of these options ($101.18 + $45.60 + $19), and the total cost per month is $165.78. You save
a little over $11 per month by using the reserved DB instance.

###### Note

The prices in this example are sample prices and might not match actual prices. For Amazon RDS pricing information, see
[Amazon RDS pricing](https://aws.amazon.com/rds/pricing "https://aws.amazon.com/rds/pricing").

### Reserved DB instances for a Multi-AZ DB cluster

To purchase the equivalent reserved DB instances for a Multi-AZ DB cluster, you can do one of
the following:

- Reserve three Single-AZ DB instances that are the same size as the
  instances in the cluster.
- Reserve one Multi-AZ DB instance and one Single-AZ DB instance that are
  the same size as the DB instances in the cluster.

For example, suppose that you have one cluster consisting of three db.m6gd.large
DB instances. In this case, you can either purchase three db.m6gd.large Single-AZ
reserved DB instances, or one db.m6gd.large Multi-AZ reserved DB instance and one
db.m6gd.large Single-AZ reserved DB instance. Either of these options reserves the
maximum reserved instance discount for the Multi-AZ DB cluster.

Alternately, you can use size-flexible DB instances and purchase a larger DB
instance to cover smaller DB instances in one or more clusters. For example, if you
have two clusters with six total db.m6gd.large DB instances, you can purchase three
db.m6gd.xl Single-AZ reserved DB instances. Doing so reserves all six DB instances
in the two clusters. For more information, see [Size-flexible reserved DB instances](#USER_WorkingWithReservedDBInstances.SizeFlexible "#USER_WorkingWithReservedDBInstances.SizeFlexible").

You might reserve DB instances that are the same size as the DB instances in the
cluster, but reserve fewer DB instances than the total number of DB instances in the
cluster. However, if you do so, the cluster is only partially reserved. For example,
suppose that you have one cluster with three db.m6gd.large DB instances, and you
purchase one db.m6gd.large Multi-AZ reserved DB instance. In this case, the cluster
is only partially reserved, because only two of the three instances in the cluster
are covered by reserved DB instances. The remaining DB instance is charged at the
on-demand db.m6gd.large hourly rate.

For more information about Multi-AZ DB clusters, see [Multi-AZ DB cluster deployments for Amazon RDS](multi-az-db-clusters-concepts.md "multi-az-db-clusters-concepts.md").

### Deleting a reserved DB instance

The terms for a reserved DB instance involve a one-year or three-year commitment. You can't cancel a reserved DB instance.
However, you can delete a DB instance that is covered by a reserved DB instance discount. The process for deleting a DB
instance that is covered by a reserved DB instance discount is the same as for any other DB instance.

You're billed for the upfront costs regardless of whether you use the resources.

If you delete a DB instance that is covered by a reserved DB instance discount, you can launch another DB instance with
compatible specifications. In this case, you continue to get the discounted rate during the reservation term (one or three
years).
