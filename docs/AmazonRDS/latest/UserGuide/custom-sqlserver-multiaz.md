# Modifying an RDS Custom for SQL Server Single-AZ deployment to a Multi-AZ deployment

You can modify an existing RDS Custom for SQL Server DB instance from a Single-AZ deployment to a
Multi-AZ deployment. When you modify the DB instance,Amazon RDS performs several
actions:

- Takes a snapshot of the primary DB instance.
- Creates new volumes for the standby replica from the snapshot. These
  volumes initialize in the background, and maximum volume performance is achieved after
  the data is fully initialized.
- Turns on synchronous block-level replication between the primary and secondary DB instances.

###### Important

We recommend that you avoid modifying your RDS Custom for SQL Server DB instance from a Single-AZ to a Multi-AZ
deployment on a production DB instance during periods of peak activity.

AWS uses a snapshot to create the standby instance to avoid downtime when you
convert from Single-AZ to Multi-AZ, but performance might be impacted during and after
converting to Multi-AZ. This impact can be significant for workloads that are sensitive
to write latency. While this capability allows large volumes to quickly be restored from
snapshots, it can cause increase in the latency of I/O operations because of the
synchronous replication. This latency can impact your database performance.

###### Note

If you created your RDS Custom for SQL Server DB instance before 29 August, 2024, patch to the latest minor version
before modifying.

- For SQL Server 2019 instances, upgrade the DB engine version to `15.00.4410.1.v1` or higher.
- For SQL Server 2022 instances, upgrade the DB engine version to `16.00.4150.1.v1` or higher.

###### Topics

- [Configuring prerequisites
  to modify a Single-AZ to a Multi-AZ deployment using CloudFormation](#custom-sqlserver-multiaz.modify-saztomaz-prereqs.cf "#custom-sqlserver-multiaz.modify-saztomaz-prereqs.cf")
- [Configuring prerequisites to modify a Single-AZ to a Multi-AZ deployment manually](#custom-sqlserver-multiaz.modify-saztomaz-prereqs.manual "#custom-sqlserver-multiaz.modify-saztomaz-prereqs.manual")
- [Modify using the RDS console, AWS CLI, or RDS API.](#custom-sqlserver-multiaz.modify-saztomaz-afterprereqs "#custom-sqlserver-multiaz.modify-saztomaz-afterprereqs")

## Configuring prerequisites

to modify a Single-AZ to a Multi-AZ deployment using CloudFormation

To use a Multi-AZ deployment, you must ensure you've applied the latest CloudFormation template
with prerequisites, or manually configure the latest prerequisites. If you've already applied the latest
CloudFormation prerequisite template, you can skip these steps.

To configure the RDS Custom for SQL Server Multi-AZ deployment prerequisites using CloudFormation

1. Open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. To start the Create Stack wizard, select the existing stack you used to create
   a Single-AZ deployment and choose **Update**.

The **Update stack** page appears. 3. For **Prerequisite - Prepare template**, choose **Replace current template**. 4. For **Specify template**, do the following:

    1. Download the latest CloudFormation template file. Open the context (right-click) menu for the link
     [custom-sqlserver-onboard.zip](samples/custom-sqlserver-onboard.md "samples/custom-sqlserver-onboard.md")
     and choose **Save Link As**.
    2. Save and extract the `custom-sqlserver-onboard.json` file to your computer.
    3. For **Template source**, choose **Upload a template file**.
    4. For **Choose file**, navigate to and then choose
     `custom-sqlserver-onboard.json`.

5. Choose **Next**.

The **Specify stack details** page appears. 6. To keep the default options, choose **Next**.

The **Advanced Options** page appears. 7. To keep the default options, choose **Next**. 8. To keep the default options, choose **Next**. 9. On the **Review Changes** page, do the following:

    1. For **Capabilities**, select the ****I acknowledge that
     CloudFormation might create IAM resources with custom names**** check box.
    2. Choose **Submit**.

10. Verify the update is successful. The status of a successful operation
    shows `UPDATE_COMPLETE`.

If the update fails, any new configuration specified in the update process
will be rolled back. The existing resource will still be usable. For example, if you
add network ACL rules numbered 18 and 19, but there were existing rules with same
numbers, the update would return the following error: `Resource handler
 returned message: "The network acl entry identified by 18 already exists.`
In this scenario you can modify the existing ACL rules to use a number lower than
18, then retry the update.

## Configuring prerequisites to modify a Single-AZ to a Multi-AZ deployment manually

###### Important

To simplify setup, we recommend that you use the latest CloudFormation template file provided in the network setup instructions.
For more information, see
[Configuring prerequisites
to modify a Single-AZ to a Multi-AZ deployment using CloudFormation](#custom-sqlserver-multiaz.modify-saztomaz-prereqs.cf "#custom-sqlserver-multiaz.modify-saztomaz-prereqs.cf").

If you choose to configure the prerequisites manually, perform the following tasks.

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. Choose **Endpoint**. The **Create Endpoint** page appears.
3. For **Service Category**, choose **AWS services**.
4. In **Services**, search for `SQS`
5. In **VPC**, choose the VPC where your RDS Custom for SQL Server DB instance is deployed.
6. In **Subnets**, choose the subnets where your RDS Custom for SQL Server DB instance is deployed.
7. In **Security Groups**, choose the `-vpc-endpoint-sg` group.
8. For **Policy**, choose **Custom**
9. In your custom policy, replace the `AWS
partition`, `Region`,
   `accountId`,and
   `IAM-Instance-role` with your own
   values.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Condition": {
 "StringLike": {
 "aws:ResourceTag/AWSRDSCustom": "custom-sqlserver"
 }
 },
 "Action": [
 "SQS:SendMessage",
 "SQS:ReceiveMessage",
 "SQS:DeleteMessage",
 "SQS:GetQueueUrl"
 ],
 "Resource": "arn:aws:sqs:`us-east-1`:`111122223333`:do-not-delete-rds-custom-*",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/{IAM-Instance-role}"
 }
 }
 ]
}`

```

10. Update the **Instance profile** with permission to
    access Amazon SQS. Replace the `AWS partition`,
    `Region`, and
    `accountId` with your own values.

```

                        {
    "Sid": "SendMessageToSQSQueue",
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
        "aws:ResourceTag/AWSRDSCustom": "custom-sqlserver"
      }
    }
  }
                        >

```

11. Update the Amazon RDS security group inbound and outbound rules to allow port 1120.
    1.  In **Security Groups**, choose the `-rds-custom-instance-sg` group.
    2.  For **Inbound Rules**, create a **Custom TCP** rule to allow port `1120` from the source `-rds-custom-instance-sg` group.
    3.  For **Outbound Rules**, create a **Custom TCP** rule to allow port `1120` to the destination `-rds-custom-instance-sg` group.

12. Add a rule in your private network Access Control List (ACL) that allows TCP ports `0-65535` for the source subnet of the DB instance.

###### Note

When creating an **Inbound Rule** and **Outbound Rule**,
take note of the highest existing **Rule number**. The new rules you create must have
a **Rule number** lower than 100 and not match any existing **Rule number**.

    1. In **Network ACLs**, choose the `-private-network-acl` group.
    2. For **Inbound Rules**, create an **All TCP** rule to allow TCP ports `0-65535` with a source from
     `privatesubnet1` and `privatesubnet2`.
    3. For **Outbound Rules**, create an **All TCP** rule to allow TCP ports `0-65535`
     to destination `privatesubnet1` and `privatesubnet2`.

## Modify using the RDS console, AWS CLI, or RDS API.

After you've completed the prerequisites, you can modify an RDS Custom for SQL Server DB instance from a Single-AZ to Multi-AZ deployment using the
RDS console, AWS CLI, or RDS API.

###### To modify an existing RDS Custom for SQL Server Single-AZ to Multi-AZ deployment

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the Amazon RDS console, choose **Databases**.

The **Databases** pane appears. 3. Choose the RDS Custom for SQL Server DB instance that you want to modify. 4. For **Actions**, choose **Convert to Multi-AZ deployment**. 5. On the **Confirmation** page, choose **Apply
immediately** to apply the changes immediately.
Choosing this option doesn't cause downtime, but there is a possible
performance impact. Alternatively, you can choose to apply the
update during the next maintenance window. For more information, see
[Using the schedule modifications
setting](USER_ModifyInstance.md "USER_ModifyInstance.md"). 6. On the **Confirmation** page, choose **Convert to Multi-AZ**.
To convert to a Multi-AZ DB instance deployment by using the AWS CLI, call the [modify-db-instance](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md")
command and set the `--multi-az` option. Specify the DB instance identifier and the values for other options that you
want to modify. For information about each option, see [Settings for DB instances](USER_ModifyInstance.md "USER_ModifyInstance.md").

###### Example

The following code modifies `mycustomdbinstance`
by including the `--multi-az` option. The changes are applied during the next maintenance window
by using `--no-apply-immediately`. Use `--apply-immediately`
to apply the changes immediately. For more information, see
[Using the schedule modifications
setting](USER_ModifyInstance.md "USER_ModifyInstance.md").

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `mycustomdbinstance` \
    --multi-az \
    `--no-apply-immediately`
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `mycustomdbinstance` ^
    --multi-az  \ ^
    `--no-apply-immediately`
```

To convert to a Multi-AZ DB instance deployment with the RDS API,
call the [ModifyDBInstance](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md") operation
and set the `MultiAZ` parameter to true.
