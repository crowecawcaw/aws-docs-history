# Purchasing reserved DB instances for Amazon Aurora

You can use the AWS Management Console, the AWS CLI, and the RDS API to work with reserved DB instances.

You can use the AWS Management Console to work with reserved DB instances
as shown in the following procedures.

###### To get pricing and information about available reserved DB instance offerings

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane,
   choose **Reserved instances**.
3. Choose **Purchase Reserved DB Instance**.
4. For **Product description**, choose the DB engine and licensing type.
5. For **DB instance class**, choose the DB instance class.
6. For **Deployment Option**, choose whether you want a
   Single-AZ or Multi-AZ DB instance deployment.

###### Note

Reserved Amazon Aurora _instances_ always have the
deployment option set to **Single-AZ DB instance**.
However, when you create an Aurora DB _cluster_,
the default deployment option is **Create an Aurora Replica
or Reader in a different AZ** (Multi-AZ).

You must purchase a reserved DB instance for each instance that
you plan to use, including Aurora Replicas. Therefore, for Multi-AZ
deployments on Aurora, you must purchase extra reserved DB
instances. 7. For **Term**, choose the length of time to reserve the the DB
instance. 8. For **Offering type**, choose the offering type.

After you select the offering type,
you can see the pricing information.

###### Important

Choose **Cancel** to avoid purchasing the reserved DB instance and incurring any charges.
After you have information about the available reserved DB instance offerings,
you can use the information to purchase an offering as shown in the following procedure.

###### To purchase a reserved DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane,
   choose **Reserved instances**.
3. ###### Important

Before proceeding, verify that you are in the correct AWS Region. Reserved DB instances are Region-specific and cannot be transferred between Regions. Check the Region selector in the upper-right corner of the console to ensure you are purchasing the reserved instance in the intended Region. 4. Choose **Purchase reserved DB instance**. 5. For **Product description**, choose the DB engine and licensing type. 6. For **DB instance class**, choose the DB instance class. 7. For **Multi-AZ deployment**, choose whether you want a
Single-AZ or Multi-AZ DB instance deployment.

###### Note

Reserved Amazon Aurora _instances_ always have the
deployment option set to **Single-AZ DB instance**.
When you create an Amazon Aurora DB _cluster_ from
your reserved DB instance, the DB cluster is automatically created
as Multi-AZ. Make sure to purchase a reserved DB instance for each
DB instance that you plan to use, including Aurora Replicas. 8. For **Term**, choose the length of time you want the DB instance reserved. 9. For **Offering type**, choose the offering type.

After you choose the offering type, you can see the pricing information.

![Purchase reserved DB instance console](images/reservedinstance-aur.png) 10. (Optional) You can assign your own identifier to the reserved DB instances that you purchase to help you track them.
For **Reserved Id**, type an identifier for your reserved DB instance. 11. Choose **Submit**.

Your reserved DB instance is purchased, then displayed in the **Reserved instances**
list.
After you have purchased reserved DB instances, you can get information about your reserved DB instances as shown in the
following procedure.

###### To get information about reserved DB instances for your AWS account

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the **Navigation** pane, choose **Reserved instances**.

The reserved DB instances for your account appear. To see detailed information about a particular reserved DB
instance, choose that instance in the list. You can then see detailed information about that instance in the
detail pane at the bottom of the console.
You can use the AWS CLI to work with reserved DB instances as shown in the following examples.

###### Example of getting available reserved DB instance offerings

To get information about available reserved DB instance offerings, call the AWS CLI command [`describe-reserved-db-instances-offerings`](../../../cli/latest/reference/rds/describe-reserved-db-instances-offerings.md "../../../cli/latest/reference/rds/describe-reserved-db-instances-offerings.md").

```
aws rds describe-reserved-db-instances-offerings
```

This call returns output similar to the following:

```

OFFERING  OfferingId                            Class         Multi-AZ  Duration  Fixed Price  Usage Price  Description  Offering Type
OFFERING  438012d3-4052-4cc7-b2e3-8d3372e0e706  db.r3.large   y         1y        1820.00 USD  0.368 USD    mysql        Partial  Upfront
OFFERING  649fd0c8-cf6d-47a0-bfa6-060f8e75e95f  db.r3.small   n         1y         227.50 USD  0.046 USD    mysql        Partial  Upfront
OFFERING  123456cd-ab1c-47a0-bfa6-12345667232f  db.r3.small   n         1y         162.00 USD   0.00 USD    mysql        All      Upfront
    Recurring Charges:   Amount  Currency  Frequency
    Recurring Charges:   0.123   USD       Hourly
OFFERING  123456cd-ab1c-37a0-bfa6-12345667232d  db.r3.large   y         1y         700.00 USD   0.00 USD    mysql        All      Upfront
    Recurring Charges:   Amount  Currency  Frequency
    Recurring Charges:   1.25    USD       Hourly
OFFERING  123456cd-ab1c-17d0-bfa6-12345667234e  db.r3.xlarge  n         1y        4242.00 USD   2.42 USD    mysql        No       Upfront
```

After you have information about the available reserved DB instance offerings, you can use the information to purchase an
offering.

To purchase a reserved DB instance, use the AWS CLI command [`purchase-reserved-db-instances-offering`](../../../cli/latest/reference/rds/purchase-reserved-db-instances-offering.md "../../../cli/latest/reference/rds/purchase-reserved-db-instances-offering.md") with the following parameters:

- `--reserved-db-instances-offering-id` – The ID of the offering that you want to purchase.
  See the preceding example to get the offering ID.
- `--reserved-db-instance-id` – You can assign your own identifier to the reserved DB
  instances that you purchase to help track them.

###### Example of purchasing a reserved DB instance

The following example purchases the reserved DB instance offering with ID
`649fd0c8-cf6d-47a0-bfa6-060f8e75e95f`, and assigns the identifier of
`MyReservation`.

For Linux, macOS, or Unix:

```
aws rds purchase-reserved-db-instances-offering \
    --reserved-db-instances-offering-id `649fd0c8-cf6d-47a0-bfa6-060f8e75e95f` \
    --reserved-db-instance-id `MyReservation`
```

For Windows:

```
aws rds purchase-reserved-db-instances-offering ^
    --reserved-db-instances-offering-id `649fd0c8-cf6d-47a0-bfa6-060f8e75e95f` ^
    --reserved-db-instance-id `MyReservation`
```

The command returns output similar to the following:

```
RESERVATION  ReservationId      Class        Multi-AZ  Start Time                Duration  Fixed Price  Usage Price  Count  State            Description  Offering Type
RESERVATION  MyReservation      db.r3.small  y         2011-12-19T00:30:23.247Z  1y        455.00 USD   0.092 USD    1      payment-pending  mysql        Partial  Upfront
```

After you have purchased reserved DB instances, you can get information about your reserved DB instances.

To get information about reserved DB instances for your AWS account, call the AWS CLI command [`describe-reserved-db-instances`](../../../cli/latest/reference/rds/describe-reserved-db-instances.md "../../../cli/latest/reference/rds/describe-reserved-db-instances.md"), as
shown in the following example.

###### Example of getting your reserved DB instances

```
aws rds describe-reserved-db-instances
```

The command returns output similar to the following:

```
RESERVATION  ReservationId     Class        Multi-AZ  Start Time                Duration  Fixed Price  Usage Price  Count  State    Description  Offering Type
RESERVATION  MyReservation     db.r3.small  y         2011-12-09T23:37:44.720Z  1y        455.00 USD   0.092 USD    1      retired  mysql        Partial  Upfront
```

You can use the RDS API to work with reserved DB instances:

- To get information about available reserved DB instance offerings, call the Amazon RDS API operation [`DescribeReservedDBInstancesOfferings`](../APIReference/API_DescribeReservedDBInstancesOfferings.md "../APIReference/API_DescribeReservedDBInstancesOfferings.md").
- After you have information about the available reserved DB instance offerings, you can use the information to
  purchase an offering. Call the [`PurchaseReservedDBInstancesOffering`](../APIReference/API_PurchaseReservedDBInstancesOffering.md "../APIReference/API_PurchaseReservedDBInstancesOffering.md") RDS API operation with the following
  parameters:
  - `--reserved-db-instances-offering-id` – The ID of the offering that you want to
    purchase.
  - `--reserved-db-instance-id` – You can assign your own identifier to the reserved DB
    instances that you purchase to help track them.

- After you have purchased reserved DB instances, you can get information about your reserved DB instances. Call
  the [`DescribeReservedDBInstances`](../APIReference/API_DescribeReservedDBInstances.md "../APIReference/API_DescribeReservedDBInstances.md") RDS API operation.
