

# Getting started with High Performance Networking
<a name="hpn-getting-started"></a>

## Supported offerings
<a name="hpn-supported-offerings"></a>

Oracle Database@AWS High Performance Networking is supported with the following Oracle Database@AWS offerings:
+ Oracle Exadata Database Service on Dedicated Infrastructure
+ Autonomous Database on Dedicated Exadata Infrastructure<a name="hpn-setup-procedure"></a>

**To set up High Performance Networking**

1. <a name="create-odb-network"></a>**Step 1: Create an Oracle Database@AWS Network**
**Note**  
High Performance Networking is not currently available in [these Availability Zones](#unsupported-availability-zones). When you create an ODB network in an AZ where this capability is not available, the API will create the ODB network without a placement group. The get response will include a status reason saying the placement groups are not supported in this AZ.

   Create an Oracle Database@AWS network using the AWS Management Console or the AWS CLI. A placement group is automatically created and associated with your ODB network.

   **AWS CLI example:**

   ```
   aws odb create-odb-network \
     --display-name {{value}} \
     --availability-zone {{value}}
   ```

1. <a name="retrieve-placement-group"></a>**Step 2: Retrieve the placement group ID**

   After creating your ODB network, retrieve the placement group ID using the `GetODBNetwork` API or from the Oracle Database@AWS console.

   **AWS CLI example:**

   ```
   aws odb get-odb-network --odb-network-id {{odb-network-id}}
   ```

   **Sample response:**

   ```
   {
     "odbNetwork": {
       "availabilityZone": "us-east-2a",
       "availabilityZoneId": "use2-az1",
       "ec2PlacementGroupId": "pg-017f45f602aba9085",
       "backupSubnetCidr": "[IP_ADDRESS]"
     }
   }
   ```

1. <a name="launch-ec2-instances"></a>**Step 3: Launch Amazon EC2 Instances Using the placement group**

   When launching Amazon EC2 instances for your application, specify the placement group ID retrieved in Step 2. This ensures your instances are placed in close proximity to your Oracle Database@AWS database for optimal latency.

   **AWS CLI example:**

   ```
   aws ec2 run-instances \
     --placement GroupId=pg-017f45f602aba9085 \
     {{[other parameters]}}
   ```

   You can also specify the placement group when launching instances through the AWS Management Console under **Advanced Details > placement group**.

1. <a name="use-odcr"></a>**Step 4 (Recommended): Use On-Demand Capacity Reservations**

   Amazon EC2 On-Demand capacity is subject to availability. To ensure high availability of capacity for your latency-sensitive workloads, we recommend using **Amazon EC2 On-Demand Capacity Reservations (ODCR)** with the Oracle Database@AWS placement group.

## Additional permissions required for creating and deleting ODB networks
<a name="placement-group-permissions"></a>

Oracle Database@AWS requires the following additional permissions for creating and deleting ODB networks with placement groups:

### Create ODB network permissions
<a name="placement-group-permissions-create"></a>
+ `ec2:CreatePlacementGroup`
+ `ec2:AttachResourcesToPlacementGroup`
+ `ec2:CreateTags`

### Delete ODB network permissions
<a name="placement-group-permissions-delete"></a>
+ `ec2:DeletePlacementGroup`
+ `ec2:DetachResourcesFromPlacementGroup`

## Identifying Oracle Database@AWS placement groups
<a name="identifying-placement-groups"></a>

Placement groups associated with ODB networks can be identified by:
+ **Name prefix** – All Oracle Database@AWS placement groups have an `ODB-` prefix in their name, making them easy to identify in the Amazon EC2 console.
+ **System tag** – Each Oracle Database@AWS placement group includes an immutable system tag indicating its association with an Oracle Database@AWS network.

## Deleting an Oracle Database@AWS Network
<a name="deleting-odb-network"></a>

When an Oracle Database@AWS network is deleted:
+ The associated placement group is **automatically deleted**.
+ Amazon EC2 instances that were previously associated with the placement group **remain running** but become unassociated from any placement group.

**Important**  
If you are creating a new Oracle Database@AWS network and need these instances to be in the new Oracle Database@AWS network's placement group, then make sure you use [modify-instance-placement](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/change-instance-placement-group.html).

```
aws ec2 modify-instance-placement \
  --instance-id {{instance-id}} \
  --group-id {{new-placement-group-id}}
```

## Unsupported Availability Zones
<a name="unsupported-availability-zones"></a>

Oracle Database@AWS High Performance Networking is not available in the following Availability Zones:


| Region name | Region code | Availability Zones | 
| --- | --- | --- | 
| US East (N. Virginia) | us-east-1 | use1-az4, use1-az6 | 
| US West (Oregon) | us-west-2 | usw2-az3, usw2-az4 | 
| Europe (Frankfurt) | eu-central-1 | euc1-az2 | 
| Asia Pacific (Seoul) | ap-northeast-2 | apne2-az1 | 
| Asia Pacific (Melbourne) | ap-southeast-4 | apse4-az1 | 