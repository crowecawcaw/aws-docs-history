

# Purchasing reserved DB instances for Amazon RDS
<a name="USER_WorkingWithReservedDBInstances.WorkingWith"></a>

You can use the AWS Management Console, the AWS CLI, and the RDS API to work with reserved DB instances.

## Console
<a name="USER_WorkingWithReservedDBInstances.CON"></a>

You can use the AWS Management Console to work with reserved DB instances as shown in the following procedures. 

**To get pricing and information about available reserved DB instance offerings**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Reserved instances**. 

1. Choose **Purchase Reserved DB Instance**.

1. For **Product description**, choose the DB engine and licensing type.

1. For **DB instance class**, choose the DB instance class.

1. For **Deployment Option**, choose whether you want a Single-AZ or Multi-AZ DB instance deployment.
**Note**  
To purchase the equivalent reserved DB instances for a Multi-AZ DB cluster deployment, either purchase three Single-AZ reserved DB instances, or one Multi-AZ and one Single-AZ reserved DB instance. For more information, see [Reserved DB instances for a Multi-AZ DB cluster](USER_WorkingWithReservedDBInstances.md#USER_WorkingWithReservedDBInstances.MultiAZDBClusters).

1. For **Term**, choose the length of time to reserve the the DB instance.

1. For **Offering type**, choose the offering type. 

   After you select the offering type, you can see the pricing information. 
**Important**  
Choose **Cancel** to avoid purchasing the reserved DB instance and incurring any charges. 

After you have information about the available reserved DB instance offerings, you can use the information to purchase an offering as shown in the following procedure. 

**To purchase a reserved DB instance**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Reserved instances**. 

1. 
**Important**  
Before proceeding, verify that you are in the correct AWS Region. Reserved DB instances are Region-specific and cannot be transferred between Regions. Check the Region selector in the console to ensure you are purchasing the reserved instance in the intended Region.

1. Choose **Purchase reserved DB instance**.

1. For **Product description**, choose the DB engine and licensing type.

1. For **DB instance class**, choose the DB instance class.

1. For **Multi-AZ deployment**, choose whether you want a Single-AZ or Multi-AZ DB instance deployment.
**Note**  
To purchase the equivalent reserved DB instances for a Multi-AZ DB cluster deployment, either purchase three Single-AZ reserved DB instances, or one Multi-AZ and one Single-AZ reserved DB instance. For more information, see [Reserved DB instances for a Multi-AZ DB cluster](USER_WorkingWithReservedDBInstances.md#USER_WorkingWithReservedDBInstances.MultiAZDBClusters).

1. For **Term**, choose the length of time you want the DB instance reserved.

1. For **Offering type**, choose the offering type.

   After you choose the offering type, you can see the pricing information.  
![Purchase reserved DB instance console.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/reservedinstance.png)

1. (Optional) You can assign your own identifier to the reserved DB instances that you purchase to help you track them. For **Reserved Id**, type an identifier for your reserved DB instance.

1. Choose **Submit**.

   Your reserved DB instance is purchased, then displayed in the **Reserved instances** list.

After you have purchased reserved DB instances, you can get information about your reserved DB instances as shown in the following procedure.

**To get information about reserved DB instances for your AWS account**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the **Navigation** pane, choose **Reserved instances**.

   The reserved DB instances for your account appear. To see detailed information about a particular reserved DB instance, choose that instance in the list. You can then see detailed information about that instance in the detail pane.

## AWS CLI
<a name="USER_WorkingWithReservedDBInstances.CLI"></a>

You can use the AWS CLI to work with reserved DB instances as shown in the following examples.

**Example of getting available reserved DB instance offerings**  
To get information about available reserved DB instance offerings, call the AWS CLI command [`describe-reserved-db-instances-offerings`](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-reserved-db-instances-offerings.html).  

```
aws rds describe-reserved-db-instances-offerings
```
This call returns output similar to the following:   

```
 1. OFFERING  OfferingId                            Class         Multi-AZ  Duration  Fixed Price  Usage Price  Description  Offering Type
 2. OFFERING  438012d3-4052-4cc7-b2e3-8d3372e0e706  db.r3.large   y         1y        1820.00 USD  0.368 USD    mysql        Partial  Upfront
 3. OFFERING  649fd0c8-cf6d-47a0-bfa6-060f8e75e95f  db.r3.small   n         1y         227.50 USD  0.046 USD    mysql        Partial  Upfront
 4. OFFERING  123456cd-ab1c-47a0-bfa6-12345667232f  db.r3.small   n         1y         162.00 USD   0.00 USD    mysql        All      Upfront
 5.     Recurring Charges:   Amount  Currency  Frequency        
 6.     Recurring Charges:   0.123   USD       Hourly
 7. OFFERING  123456cd-ab1c-37a0-bfa6-12345667232d  db.r3.large   y         1y         700.00 USD   0.00 USD    mysql        All      Upfront
 8.     Recurring Charges:   Amount  Currency  Frequency
 9.     Recurring Charges:   1.25    USD       Hourly
10. OFFERING  123456cd-ab1c-17d0-bfa6-12345667234e  db.r3.xlarge  n         1y        4242.00 USD   2.42 USD    mysql        No       Upfront
```

After you have information about the available reserved DB instance offerings, you can use the information to purchase an offering.

To purchase a reserved DB instance, use the AWS CLI command [`purchase-reserved-db-instances-offering`](https://docs.aws.amazon.com/cli/latest/reference/rds/purchase-reserved-db-instances-offering.html) with the following parameters:
+ `--reserved-db-instances-offering-id` – The ID of the offering that you want to purchase. See the preceding example to get the offering ID.
+ `--reserved-db-instance-id` – You can assign your own identifier to the reserved DB instances that you purchase to help track them.

**Example of purchasing a reserved DB instance**  
The following example purchases the reserved DB instance offering with ID {{649fd0c8-cf6d-47a0-bfa6-060f8e75e95f}}, and assigns the identifier of {{MyReservation}}.  
For Linux, macOS, or Unix:  

```
aws rds purchase-reserved-db-instances-offering \
    --reserved-db-instances-offering-id {{649fd0c8-cf6d-47a0-bfa6-060f8e75e95f}} \
    --reserved-db-instance-id {{MyReservation}}
```
For Windows:  

```
aws rds purchase-reserved-db-instances-offering ^
    --reserved-db-instances-offering-id {{649fd0c8-cf6d-47a0-bfa6-060f8e75e95f}} ^
    --reserved-db-instance-id {{MyReservation}}
```
The command returns output similar to the following:   

```
1. RESERVATION  ReservationId      Class        Multi-AZ  Start Time                Duration  Fixed Price  Usage Price  Count  State            Description  Offering Type
2. RESERVATION  MyReservation      db.r3.small  y         2011-12-19T00:30:23.247Z  1y        455.00 USD   0.092 USD    1      payment-pending  mysql        Partial  Upfront
```

After you have purchased reserved DB instances, you can get information about your reserved DB instances.

To get information about reserved DB instances for your AWS account, call the AWS CLI command [`describe-reserved-db-instances`](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-reserved-db-instances.html), as shown in the following example.

**Example of getting your reserved DB instances**  

```
aws rds describe-reserved-db-instances
```
The command returns output similar to the following:   

```
1. RESERVATION  ReservationId     Class        Multi-AZ  Start Time                Duration  Fixed Price  Usage Price  Count  State    Description  Offering Type
2. RESERVATION  MyReservation     db.r3.small  y         2011-12-09T23:37:44.720Z  1y        455.00 USD   0.092 USD    1      retired  mysql        Partial  Upfront
```

## RDS API
<a name="USER_WorkingWithReservedDBInstances.API"></a>

You can use the RDS API to work with reserved DB instances:
+ To get information about available reserved DB instance offerings, call the Amazon RDS API operation [`DescribeReservedDBInstancesOfferings`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeReservedDBInstancesOfferings.html).
+ After you have information about the available reserved DB instance offerings, you can use the information to purchase an offering. Call the [`PurchaseReservedDBInstancesOffering`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_PurchaseReservedDBInstancesOffering.html) RDS API operation with the following parameters:
  + `--reserved-db-instances-offering-id` – The ID of the offering that you want to purchase.
  + `--reserved-db-instance-id` – You can assign your own identifier to the reserved DB instances that you purchase to help track them.
+ After you have purchased reserved DB instances, you can get information about your reserved DB instances. Call the [`DescribeReservedDBInstances`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeReservedDBInstances.html) RDS API operation.