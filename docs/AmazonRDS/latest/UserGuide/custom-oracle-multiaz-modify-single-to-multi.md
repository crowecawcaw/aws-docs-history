

# Converting a Single-AZ deployment to a Multi-AZ deployment in RDS Custom for Oracle
<a name="custom-oracle-multiaz-modify-single-to-multi"></a>

**Note**  
End of support notice: On March 31, 2027, AWS will end support for Amazon RDS Custom for Oracle. After March 31, 2027, you will no longer be able to access the RDS Custom for Oracle console or RDS Custom for Oracle resources. For more information, see [RDS Custom for Oracle end of support](RDS-Custom-for-Oracle-end-of-support.md).

You can convert an existing multi-AZ compatible RDS Custom for Oracle instance from a Single-AZ deployment to a Multi-AZ deployment. When you modify the DB instance, Amazon RDS performs several actions:
+ Takes a snapshot of the primary DB instance.
+ Creates new volumes for the standby replica from the snapshot. These volumes initialize in the background, and maximum volume performance is achieved after the data is fully initialized.
+ Turns on synchronous block-level replication between the primary and standby DB instances.

**Important**  
We recommend that you avoid modifying your RDS Custom for Oracle DB instance from a Single-AZ to a Multi-AZ deployment on a production DB instance during periods of peak activity.

AWS uses a snapshot to create the standby instance to avoid downtime when you convert from Single-AZ to Multi-AZ, but performance might be impacted during and after converting to Multi-AZ. This impact can be significant for workloads that are sensitive to write latency. While this capability allows large volumes to quickly be restored from snapshots, it can cause increase in the latency of I/O operations because of the synchronous replication. This latency can impact your database performance.

## Configuring prerequisites to modify a Single-AZ to a Multi-AZ deployment using CloudFormation
<a name="custom-oracle-multiaz-modify-cf-prereqs"></a>

Follow [Step 3: Extract the CloudFormation templates for RDS Custom for Oracle](custom-setup-orcl.md#custom-setup-orcl.cf.downloading) to setup your VPC and IAM profile again to add SQS VPC endpoint and SQS permission in IAM profile.

## Configuring prerequisites to modify a Single-AZ to a Multi-AZ deployment manually
<a name="custom-oracle-multiaz-modify-manual-prereqs"></a>

If you choose to configure the prerequisites manually, perform the following tasks.

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/)

1. Choose **Endpoint**. The **Create Endpoint** page appears.

1. For **Service Category**, choose **AWS services**.

1. In **Services**, search for `SQS`.

1. In **VPC**, choose the VPC where your RDS Custom for Oracle DB instance is deployed.

1. In **Subnets**, choose the subnets where your RDS Custom for Oracle DB instance is deployed.

1. In **Security Groups**, choose the security group where your RDS Custom for Oracle DB instance is deployed.

1. For **Policy**, choose **Custom**.

1. In your custom policy, replace the `AWS partition`, `Region`, `accountId`, and `IAM-Instance-role` with your own values.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Condition": {
                "StringLike": {
                    "aws:ResourceTag/AWSRDSCustom": "custom-oracle"
                }
            },
            "Action": [
                "SQS:SendMessage",
                "SQS:ReceiveMessage",
                "SQS:DeleteMessage",
                "SQS:GetQueueUrl"
            ],
            "Resource": "arn:aws:sqs:us-east-1:111122223333:do-not-delete-rds-custom-*",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::111122223333:role/{IAM-Instance-role}"
            }
        }
    ]
}
```

------

Update the **Instance profile** with permission to access Amazon SQS. Replace the `AWS partition`, `Region`, and `accountId` with your own values.

```
{
    "Sid": "13",
    "Effect": "Allow",
    "Action": [
        "SQS:SendMessage",
        "SQS:ReceiveMessage",
        "SQS:DeleteMessage",
        "SQS:GetQueueUrl"
    ],
    "Resource": [
        {
            "Fn::Sub": "arn:${AWS::Partition}:sqs:${AWS::Region}:${AWS::AccountId}:do-not-delete-rds-custom-*"
        }
    ],
    "Condition": {
        "StringLike": {
            "aws:ResourceTag/AWSRDSCustom": "custom-oracle"
        }
    }
}
```

Update the Amazon RDS security group inbound and outbound rules to allow port 1120.
+ In **Security Groups**, choose the group where your RDS Custom for Oracle DB instance is deployed.
+ For **Inbound Rules**, create a **Custom TCP** rule to allow port `1120` from the source group.
+ For **Outbound Rules**, create a **Custom TCP** rule to allow port `1120` to the destination group.

## Modify using the RDS console, AWS CLI, or RDS API
<a name="custom-oracle-multiaz-modify-console-cli-api"></a>

After you've completed the prerequisites, you can modify an RDS Custom for Oracle DB instance from a Single-AZ to Multi-AZ deployment using the Amazon RDS console, AWS CLI, or Amazon RDS API.

### Console
<a name="custom-oracle-multiaz-modify-console"></a>

**To modify an existing RDS Custom for Oracle Single-AZ to Multi-AZ deployment**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the Amazon RDS console, choose **Databases**. The **Databases** pane appears.

1. Choose the RDS Custom for Oracle DB instance that you want to modify.

1. For **Actions**, choose **Convert to Multi-AZ deployment**.

1. On the **Confirmation** page, choose **Apply immediately** to apply the changes immediately. Choosing this option doesn't cause downtime, but there is a possible performance impact. Alternatively, you can choose to apply the update during the next maintenance window. For more information, see [Using the schedule modifications setting](USER_ModifyInstance.ApplyImmediately.md).

1. On the **Confirmation** page, choose **Convert to Multi-AZ**.

### AWS CLI
<a name="custom-oracle-multiaz-modify-cli"></a>

To convert to a Multi-AZ DB instance deployment by using the AWS CLI, call the [modify-db-instance](https://docs.aws.amazon.com//cli/latest/reference/rds/modify-db-instance.html) command and set the `--multi-az` option. Specify the DB instance identifier and the values for other options that you want to modify. For information about each option, see [Settings for DB instances](USER_ModifyInstance.Settings.md).

**Example**  
The following code modifies `mycustomdbinstance` by including the `--multi-az` option. The changes are applied during the next maintenance window by using `--no-apply-immediately`. Use `--apply-immediately` to apply the changes immediately. For more information, see [Using the schedule modifications setting](USER_ModifyInstance.ApplyImmediately.md).  
For Linux, macOS, or Unix:  

```
aws rds modify-db-instance \
    --db-instance-identifier {{mycustomdbinstance}} \
    --multi-az \
    [--no-apply-immediately | --apply-immediately]
```
For Windows:  

```
aws rds modify-db-instance ^
    --db-instance-identifier {{mycustomdbinstance}} ^
    --multi-az ^
    [--no-apply-immediately | --apply-immediately]
```

### RDS API
<a name="custom-oracle-multiaz-modify-api"></a>

To convert to a Multi-AZ DB instance deployment with the Amazon RDS API, call the [ModifyDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) operation and set the `MultiAZ` parameter to true.