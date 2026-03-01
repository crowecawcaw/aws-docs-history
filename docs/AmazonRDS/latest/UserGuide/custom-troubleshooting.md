# Troubleshooting DB issues for Amazon RDS Custom for Oracle

The shared responsibility model of RDS Custom provides OS shell–level access and database administrator access. RDS Custom runs resources in
your account, unlike Amazon RDS, which runs resources in a system account. With greater access comes greater responsibility. In the following
sections, you can learn how to troubleshoot issues with Amazon RDS Custom DB instances.

###### Note

This section explains how to troubleshoot RDS Custom for Oracle. For troubleshooting RDS Custom for SQL Server, see
[Troubleshooting DB issues for Amazon RDS Custom for SQL Server](custom-troubleshooting-sqlserver.md "custom-troubleshooting-sqlserver.md").

###### Topics

- [Viewing RDS Custom events](#custom-troubleshooting.support-perimeter.viewing-events "#custom-troubleshooting.support-perimeter.viewing-events")
- [Subscribing to RDS Custom events](#custom-troubleshooting.support-perimeter.subscribing "#custom-troubleshooting.support-perimeter.subscribing")
- [Troubleshooting DB instance creation issues](#custom-troubleshooting.creation-issues "#custom-troubleshooting.creation-issues")
- [Troubleshooting custom engine version creation for RDS Custom for Oracle](#custom-troubleshooting.cev "#custom-troubleshooting.cev")
- [Fixing unsupported configurations in RDS Custom for Oracle](#custom-troubleshooting.fix-unsupported "#custom-troubleshooting.fix-unsupported")
- [Troubleshooting upgrades for RDS Custom for Oracle](#custom-troubleshooting-upgrade "#custom-troubleshooting-upgrade")
- [Troubleshooting replica promotion for RDS Custom for Oracle](#custom-troubleshooting-promote "#custom-troubleshooting-promote")

## Viewing RDS Custom events

The procedure for viewing events is the same for RDS Custom and Amazon RDS DB instances. For more information, see [Viewing Amazon RDS events](USER_ListEvents.md "USER_ListEvents.md").

To view RDS Custom event notification using the AWS CLI, use the `describe-events` command. RDS Custom introduces several new
events. The event categories are the same as for Amazon RDS. For the list of events, see [Amazon RDS event categories and event messages](USER_Events.md "USER_Events.md").

The following example retrieves details for the events that have occurred for the specified RDS Custom DB instance.

```
aws rds describe-events \
    --source-identifier my-custom-instance \
    --source-type db-instance
```

## Subscribing to RDS Custom events

The procedure for subscribing to events is the same for RDS Custom and Amazon RDS DB instances. For more information, see [Subscribing to Amazon RDS event notification](USER_Events.md "USER_Events.md").

To subscribe to RDS Custom event notification using the CLI, use the `create-event-subscription` command. Include the
following required parameters:

- `--subscription-name`
- `--sns-topic-arn`

The following example creates a subscription for backup and recovery events for an RDS Custom DB instance in the current AWS
account. Notifications are sent to an Amazon Simple Notification Service (Amazon SNS) topic, specified by `--sns-topic-arn`.

```
aws rds create-event-subscription \
    --subscription-name my-instance-events \
    --source-type db-instance \
    --event-categories '["backup","recovery"]' \
    --sns-topic-arn arn:aws:sns:us-east-1:123456789012:interesting-events
```

## Troubleshooting DB instance creation issues

If your environment isn't properly configured or required permissions are missing, you
can't create or restore RDS Custom for Oracle DB instances. When you attempt to create or restore a DB instance,
Amazon RDS validates your environment and returns specific error messages if it detects any
issues.

After you resolve all issues, try again to create or restore your RDS Custom for Oracle DB instance.

### Common permissions issues

When you create or restore a RDS Custom for Oracle instance, Amazon RDS validates that your environment
has the required permissions. If permissions are missing or denied, the operation fails
with a specific error message.

| Issue type              | Error message                                                                                                                                                                                                                                                                                                                                                                                  | Action                                                                                                                                                                                   |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IAM role access policy  | **`You can't create the DB instance because of<br>incompatible resources. The host environment validation failed<br>for the following permissions: <permission> on resource:<br><resource> due to permissions issue with message: User:<br><user> is not authorized to perform: <permission> on<br>resource: <resource> because no identity-based policy<br>allows the <permission> action.`** | Ensure that the listed required permissions are present and set to `Allow` in the access policy with the appropriate resources included.                                                 |
| Permission boundary     | **`You can't create the DB instance because of<br>incompatible resources. The host environment validation failed<br>for the following permissions: <permission> on resource:<br><resource> due to permissions issue with message: User:<br><user> is not authorized to perform: <permission> on<br>resource: <resource> with an explicit deny in a<br>permissions boundary.`**                 | Verify that the permissions boundary attached to the instance role isn't restricting the listed required permissions and resources.                                                      |
| Service control policy  | **`You can't create the DB instance because of<br>incompatible resources. The host environment validation failed<br>for the following permissions: <permission> on resource:<br><resource> due to permissions issue with message: User:<br><user> is not authorized to perform: <permission> on<br>resource: <resource> with an explicit deny in a service<br>control policy.`**               | Contact your AWS Organizations administrator and verify that the service<br>control policy attached to your account isn't restricting the listed<br>required permissions and resources.  |
| Resource control policy | **`You can't create the DB instance because of<br>incompatible resources. The host environment validation failed<br>for the following permissions: <permission> on resource:<br><resource> due to permissions issue with message: User:<br><user> is not authorized to perform: <permission> on<br>resource: <resource> with an explicit deny in a resource<br>control policy.`**              | Contact your AWS Organizations administrator and verify that the resource<br>control policy attached to your account isn't restricting the listed<br>required permissions and resources. |
| VPC endpoint policy     | **`You can't create the DB instance because of<br>incompatible resources. The host environment validation failed<br>for the following permissions: <permission> on resource:<br><resource> due to permissions issue with message: User:<br><user> is not authorized to perform: <permission> on<br>resource: <resource> with an explicit deny in a VPC<br>endpoint policy.`**                  | Ensure that the required VPC endpoints exist and the policies attached to them aren't restricting the listed required permissions and resources.                                         |

### Networking issues

In addition to reviewing [Step 6: Configure your VPC for RDS Custom for Oracle](custom-setup-orcl.md#custom-setup-orc.vpc-config "custom-setup-orcl.md#custom-setup-orc.vpc-config"), verify that the following are
configured correctly and not restricting access to the required AWS services:

**Security group attached to the Amazon EC2 instance**

Ensure that the security group allows all necessary inbound and outbound
traffic for RDS Custom operations.

**Security group attached to your VPC**

Verify that VPC security groups permit traffic to and from the required AWS services.

**VPC endpoints**

Confirm that all required VPC endpoints are properly configured and accessible.

**Networking access control lists**

Check that network ACLs aren't blocking traffic needed for RDS Custom
functionality.

## Troubleshooting custom engine version creation for RDS Custom for Oracle

When CEV creation fails, RDS Custom issues `RDS-EVENT-0198` with the message `Creation failed for custom engine
 version `major-engine-version.cev_name``, and includes details about the failure. For
example, the event prints missing files.

CEV creation might fail because of the following issues:

- The Amazon S3 bucket containing your installation files isn't in the same AWS Region as your CEV.
- When you request CEV creation in an AWS Region for the first time, RDS Custom creates an S3 bucket for storing RDS Custom
  resources (such as CEV artifacts, AWS CloudTrail logs, and transaction logs).

CEV creation fails if RDS Custom can't create the S3 bucket. Either the caller doesn't have S3 permissions as described in
[Step 5: Grant required permissions to your IAM user or role](custom-setup-orcl.md#custom-setup-orcl.iam-user "custom-setup-orcl.md#custom-setup-orcl.iam-user"), or the number of S3 buckets
has reached the limit.

- The caller doesn't have permissions to get files from your S3 bucket that contains the installation media files. These
  permissions are described in [Step 7: Add necessary IAM permissions](custom-cev.md#custom-cev.preparing.iam "custom-cev.md#custom-cev.preparing.iam").
- Your IAM policy has an `aws:SourceIp` condition. Make sure to follow the recommendations in [AWS Denies access to
  AWS based on the source IP](../../../IAM/latest/UserGuide/reference_policies_examples_aws_deny-ip.md "../../../IAM/latest/UserGuide/reference_policies_examples_aws_deny-ip.md") in the _AWS Identity and Access Management User Guide_. Also make sure that the
  caller has the S3 permissions described in [Step 5: Grant required permissions to your IAM user or role](custom-setup-orcl.md#custom-setup-orcl.iam-user "custom-setup-orcl.md#custom-setup-orcl.iam-user").
- Installation media files listed in the CEV manifest aren't in your S3 bucket.
- The SHA-256 checksums of the installation files are unknown to RDS Custom.

Confirm that the SHA-256 checksums of the provided files match the SHA-256 checksum on the Oracle website. If the
checksums match, contact [AWS Support](https://aws.amazon.com/premiumsupport "https://aws.amazon.com/premiumsupport") and provide the failed CEV
name, file name, and checksum.

- The OPatch version is incompatible with your patch files. You might get the following message: `OPatch is lower than
minimum required version. Check that the version meets the requirements for all patches, and try again`. To apply an
  Oracle patch, you must use a compatible version of the OPatch utility. You can find the required version of the Opatch utility in
  the readme file for the patch. Download the most recent OPatch utility from My Oracle Support, and try creating your CEV
  again.
- The patches specified in the CEV manifest are in the wrong order.

You can view RDS events either on the RDS console (in the navigation pane, choose **Events**) or by using the
`describe-events` AWS CLI command. The default duration is 60 minutes. If no events are returned, specify a longer
duration, as shown in the following example.

```
aws rds describe-events --duration 360
```

Currently, the MediaImport service that imports files from Amazon S3 to create CEVs isn't integrated with AWS CloudTrail. Therefore,
if you turn on data logging for Amazon RDS in CloudTrail, calls to the MediaImport service such as the
`CreateCustomDbEngineVersion` event aren't logged.

However, you might see calls from the API gateway that accesses your Amazon S3 bucket. These calls come from the MediaImport
service for the `CreateCustomDbEngineVersion` event.

## Fixing unsupported configurations in RDS Custom for Oracle

In the shared responsibility model, it's your responsibility to fix configuration
issues that put your RDS Custom for Oracle DB instance into the `unsupported-configuration` state.
If the issue is with the AWS infrastructure, use the console or the AWS CLI to fix it. If
the issue is with the operating system or the database configuration, log in to the host to
fix it.

###### Note

This section explains how to fix unsupported configurations in RDS Custom for Oracle. For
information about RDS Custom for SQL Server, see [Fixing unsupported configurations in RDS Custom for SQL Server](custom-troubleshooting-sqlserver.md#custom-troubleshooting-sqlserver.fix-unsupported "custom-troubleshooting-sqlserver.md#custom-troubleshooting-sqlserver.fix-unsupported").

The following tables includes descriptions of the notifications and events that the
support perimeter sends and how to fix them. These notifications and the support perimeter
are subject to change. For background on the support perimeter, see [RDS Custom support perimeter](custom-concept.md#custom-troubleshooting.support-perimeter "custom-concept.md#custom-troubleshooting.support-perimeter"). For event descriptions, see
[Amazon RDS event categories and event messages](USER_Events.md "USER_Events.md").

| Event ID   | Configuration                    | RDS event message                                                                                         | Action                                         |
| ---------- | -------------------------------- | --------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| `SP-O0000` | Manual unsupported configuration | **`The RDS Custom DB instance status is set to [Unsupported<br>configuration] because of:<br>`reason`.`** | To resolve this issue, create an Support case. |

**AWS resources (infrastructure)**

| Event ID       | Configuration                                   | RDS event message                                                                                                                                                                                                                                       | Action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **`SP-O1001`** | Amazon Elastic Block Store (Amazon EBS) volumes | **`The following EBS volumes were added to EC2 instance<br>`ec2_id`: `volume_id`.<br>To resolve the issue, detach the specified volumes from the<br>instance.`**                                                                                        | RDS Custom creates two types of EBS volume, besides the root volume created from the Amazon<br>Machine Image (AMI), and associates them with the EC2 instance:<br>• The binary volume where the database software binaries are located<br>• The data volumes where database files are located<br>When you create your DB instance, the storage configurations that you specify configure the data<br>volumes.<br>The support perimeter monitors the following:<br>• The initial EBS volumes created with the DB instance are still associated with the<br>instance.<br>• The initial EBS volumes still have the same configurations as initially set:<br>storage type, size, Provisioned IOPS, and storage throughput.<br>• No additional EBS volumes are attached to the DB instance.<br>Use the following CLI command to compare the volume type of the EBS volume details and the<br>RDS Custom for Oracle DB instance details:<br>```<br>aws rds describe-db-instances \<br>--db-instance-identifier db-instance-name | grep StorageType<br>```                                                                               |
| **`SP-O1002`** | Amazon Elastic Block Store (Amazon EBS) volumes | **`EBS volume `volume_id` has been<br>detached from EC2 instance [`ec2_id`]. You<br>can't detach the original volume from this instance. To resolve the<br>issue, re-attach `volume_id` to<br>`ec2_id``**.                                              | RDS Custom creates two types of EBS volume, besides the root volume created from the Amazon<br>Machine Image (AMI), and associates them with the EC2 instance:<br>• The binary volume where the database software binaries are located<br>• The data volumes where database files are located<br>When you create your DB instance, the storage configurations that you specify configure the data<br>volumes.<br>The support perimeter monitors the following:<br>• The initial EBS volumes created with the DB instance are still associated with the<br>instance.<br>• The initial EBS volumes still have the same configurations as initially set:<br>storage type, size, Provisioned IOPS, and storage throughput.<br>• No additional EBS volumes are attached to the DB instance.<br>Use the following CLI command to compare the volume type of the EBS volume details and the<br>RDS Custom for Oracle DB instance details:<br>```<br>aws rds describe-db-instances \<br>--db-instance-identifier db-instance-name | grep StorageType<br>```                                                                               |
| **`SP-O1003`** | Amazon Elastic Block Store (Amazon EBS) volumes | **`The original EBS volume<br>`volume_id` attached to EC2 instance<br>`ec2_id` has been modified as follows: size<br>[`X`] to [`Y`], type<br>[`N`] to [`M`], or<br>IOPS [`J`] to [`K`].<br>To resolve the issue, revert the modification.`**            | RDS Custom creates two types of EBS volume, besides the root volume created from the Amazon<br>Machine Image (AMI), and associates them with the EC2 instance:<br>• The binary volume where the database software binaries are located<br>• The data volumes where database files are located<br>When you create your DB instance, the storage configurations that you specify configure the data<br>volumes.<br>The support perimeter monitors the following:<br>• The initial EBS volumes created with the DB instance are still associated with the<br>instance.<br>• The initial EBS volumes still have the same configurations as initially set:<br>storage type, size, Provisioned IOPS, and storage throughput.<br>• No additional EBS volumes are attached to the DB instance.<br>Use the following CLI command to compare the volume type of the EBS volume details and the<br>RDS Custom for Oracle DB instance details:<br>```<br>aws rds describe-db-instances \<br>--db-instance-identifier db-instance-name | grep StorageType<br>```                                                                               |
| **`SP-O1004`** | Amazon EC2 instance state                       | **`Automated recovery left EC2 instance<br>[`ec2_id`] in an impaired state. To resolve the<br>issue, see Troubleshooting instance recovery failures.`**                                                                                                 | To check the status of a DB instance, use the console or run the following<br>AWS CLI command:<br>```<br>aws rds describe-db-instances \<br>--db-instance-identifier `db-instance-name`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | grep DBInstanceStatus<br>```                                                                          |
| **`SP-O1005`** | Amazon EC2 instance attributes                  | **`EC2 instance [`ec2_id`] was<br>modified as follows: attribute [`att1`] changed<br>from [`val-old`] to<br>[`val-new`], attribute<br>[`att2`] changed from<br>[`val-old`] to<br>[`val-new`]. To resolve the issue, revert to<br>the original value.`** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **`SP-O1006`** | Amazon EC2 instance state                       | **`EC2 instance [`ec2_id`] was<br>terminated or can't be found. To resolve the issue, delete the RDS Custom<br>DB instance.`**                                                                                                                          | The support perimeter monitors EC2 instance state-change<br>notifications. The EC2 instance must always be running.<br>To delete your DB instance<br>1. To check the status of a DB instance, use the console or run the<br>following AWS CLI command:<br>```<br>aws rds describe-db-instances \<br>--db-instance-identifier `db-instance-name`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | grep DBInstanceStatus<br>```<br>2. Delete your RDS Custom for Oracle DB instance.                     |
| **`SP-O1007`** | Amazon EC2 instance state                       | **`EC2 instance [`ec2_id`] was<br>stopped. To resolve the issue, start the instance.`**                                                                                                                                                                 | The support perimeter monitors EC2 instance state-change<br>notifications. The EC2 instance must always be running.<br>To restart your DB instance<br>1. To check the status of a DB instance, use the console or run the<br>following AWS CLI command:<br>```<br>aws rds describe-db-instances \<br>--db-instance-identifier `db-instance-name`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | grep DBInstanceStatus<br>```<br>2. Start your DB instance.<br>3. Remount the binary and data volumes. |
| **`SP-1008`**  | Amazon SQS permission                           | **`Permissions are missing for Amazon SQS. Check the permissions<br>for the IAM instance profile, VPC endpoint policy, and dependent service<br>connections, and then try again.`**                                                                     | You can resolve this by making sure the IAM profile associated with<br>the host has the following permissions:<br>`<br>"SQS:SendMessage"<br>"SQS:ReceiveMessage"<br>"SQS:DeleteMessage"<br>"SQS:GetQueueUrl"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **`SP-1009`**  | Amazon Simple Queue Service (Amazon SQS)        | **`The SQS queue [%s] was deleted and couldn't be recovered.<br>To resolve this issue, recreate the queue.`**                                                                                                                                           | Recreate the Amazon SQS queue.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

**Operating system**

| Event ID       | Configuration                                | RDS event message                                                                                                                                                                                                            | Action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------- | -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **`SP-O2001`** | RDS Custom agent status                      | **`The RDS Custom agent isn't running on EC2 instance<br>[`ec2_id`]. Make sure the agent is running on<br>[`ec2_id`].`**                                                                                                     | On RDS Custom for Oracle, the DB instance goes outside the support perimeter if the<br>RDS Custom agent stops. The agent publishes the `IamAlive` metric<br>to Amazon CloudWatch every 30 seconds. An alarm is triggered if the metric<br>hasn't been published for 30 seconds. The support perimeter also<br>monitors the RDS Custom agent process state on the host every 30<br>minutes.<br>To restart the RDS Custom agent<br>1. Log in to your host and make sure that the RDS Custom agent is<br>running.<br>2. Run the following command to find the status of the<br>agent.<br>`<br>service rdscustomagent status<br>`<br>3. Use the following command to start the agent.<br>`<br>service rdscustomagent start<br>`<br>When the RDS Custom agent is running again, the `IamAlive`<br>metric is published to Amazon CloudWatch, and the alarm switches to the<br>`OK` state. This switch notifies the support perimeter that<br>the agent is running.                                                                                                                                                                   |
| `SP-O2002`     | AWS Systems Manager agent (SSM agent) status | **`The Systems Manager agent on EC2 instance<br>[`ec2_id`] is unreachable. Make sure that you<br>that have correctly configured the network, agent, and IAM permissions.`**                                                  | SSM Agent must always be running. The RDS Custom agent is responsible<br>for making sure that the Systems Manager agent is running. If SSM Agent was<br>terminated and then restarted, the RDS Custom agent publishes the metric<br>`SSM_Agent_Restarted_Or_NotFound` to CloudWatch. The RDS Custom<br>agent has an alarm on the metric<br>`do-not-delete-rds-custom-ssm-agent-restarted-or-notfound-`ec2-id``<br>configured to trigger when there has been a restart in each of the<br>previous three minutes. The support perimeter also monitors the process<br>state of SSM Agent on the host every 30 minutes.<br>For more information, see [Troubleshooting SSM Agent](../../../systems-manager/latest/userguide/troubleshooting-ssm-agent.md "../../../systems-manager/latest/userguide/troubleshooting-ssm-agent.md").                                                                                                                                                                                                                                                                                                 |
| `SP-O2003`     | AWS Systems Manager agent (SSM agent) status | **`The Systems Manager agent on EC2 instance<br>[`ec2_id`] crashed multiple times. For more<br>information, see the SSM Agent troubleshooting<br>documentation.`**                                                           | For more information, see [Troubleshooting SSM Agent](../../../systems-manager/latest/userguide/troubleshooting-ssm-agent.md "../../../systems-manager/latest/userguide/troubleshooting-ssm-agent.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **`SP-O2004`** | OS time zone                                 | **`The time zone on EC2 instance<br>[`ec2_id`] was changed. To resolve this issue,<br>revert the timezone to the previous setting of<br>[`previous-time-zone`]. Then use an RDS options<br>group to change the time zone.`** | RDS automation detected that the time zone on the host was changed<br>without the use of an option group. This host-level change can cause RDS<br>automation failures, so the EC2 instance is placed in the<br>`unsupported-configuration` state.<br>To fix the time zone setting<br>1. Log in to your EC2 host and check the OS time zone as<br>follows:<br>`<br>timedatectl<br>`<br>2. Pause RDS Custom automation. For more information, see [Pausing and resuming your RDS Custom DB instance](custom-managing.md#custom-managing.pausing "custom-managing.md#custom-managing.pausing").<br>3. Stop the DB instance.<br>4. Revert the time zone change on the operating system.<br>5. Start the DB instance.<br>6. Resume RDS Custom automation.<br>Your DB instance becomes available within 30 minutes. To prevent moving out<br>of perimeter in the future, modify your timezone through an options<br>group. For more information, see [Oracle time zone](custom-managing.md "custom-managing.md").                                                                                                                    |
| **`SP-O2005`** | `sudo` configurations                        | **`The sudo configurations on EC2 instance<br>[`ec2_id`] lack necessary permissions. To<br>resolve this issue, revert the recent changes to the sudo<br>configurations.`**                                                   | The support perimeter verifies that certain OS users are allowed to<br>run certain commands on the host. It monitors `sudo`<br>configurations and compares them to the supported state.<br>If the `sudo` configurations aren't supported, RDS Custom<br>tries to overwrite them and return to the previous supported state. If<br>the attempt is successful, RDS Custom sends the following<br>notification:<br>**`RDS Custom successfully overwrote your<br>configuration.`**<br>If the overwrite isn't successful, your DB instance remains in the<br>unsupported configuration state. To resolve this problem, either revert<br>the changes within the `sudoers.d/` file or fix the<br>permissions.<br>To investigate changes to the `sudo` configurations<br>1. Log in to your host.<br>2. Run the following command.<br>``<br>visudo -c -f /etc/sudoers.d/`individual_sudo_files`<br>``<br>3. Modify the `sudo` configurations as<br>necessary.<br>After the support perimeter determines that the `sudo`<br>configurations are supported, your RDS Custom for Oracle DB instance becomes available<br>within 30 minutes. |
| **`SP-O2006`** | S3 bucket accessibility                      | **`RDS Custom automation can't download files from the S3 bucket<br>on EC2 instance [`ec2_id`]. Check your<br>networking configuration and make sure the instance allows connections<br>to and from S3.`**                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **`SP-2007`**  | High Availability Software Solution Version  | **`The HA solution of your instance differs from the expected<br>version. To resolve this issue, create an AWS Support<br>case.`**                                                                                           | Create an AWS Support case.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

**Database**

| Event ID       | Configuration               | RDS event message                                                                                                                                                                                                                                   | Action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| -------------- | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`SP-O3001`** | Database archive lag target | **`The ARCHIVE_LAG_TARGET parameter on EC2 instance<br>[`ec2_id`] is out of the recommended<br>range `value_range`. To resolve the issue,<br>set the parameter to a value within value_range.`**                                                    | The support perimeter monitors the `ARCHIVE_LAG_TARGET`<br>database parameter to verify that the latest restorable time of the<br>DB instance is within reasonable bounds.<br>To change the lag target for archived redo logs<br>1. Log in to your EC2 host<br>2. Connect to your RDS Custom for Oracle DB instance<br>3. Change the `ARCHIVE_LAG_TARGET` parameter to a<br>value from 60–7200. For example, use the following SQL<br>statement.<br>`<br>ALTER SYSTEM SET ARCHIVE_LAG_TARGET=300 SCOPE=BOTH;<br>`<br>Your DB instance becomes available within 30 minutes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **`SP-O3002`** | Oracle Data Guard role      | **`The database role [`role_name`]<br>isn't supported for Oracle Data Guard on EC2 instance<br>[`ec2_id`]. To resolve the issue, set<br>the DATABASE_ROLE parameter to either PRIMARY or PHYSICAL<br>STANDBY.`**                                    | The support perimeter monitors the current database role every 15<br>seconds and sends a CloudWatch notification if the database role has changed.<br>The Oracle Data Guard `DATABASE_ROLE` parameter must be<br>either `PRIMARY` or `PHYSICAL STANDBY`.<br>To restore your Oracle Data Guard database role to a supported value<br>1. Check the Oracle Data Guard role by running the following<br>statement:<br>`<br>SELECT DATABASE_ROLE FROM V$DATABASE;<br>`<br>2. If your DB instance is standalone, use either of the following<br>statements to change it back to the `PRIMARY`<br>role:<br>`<br>ALTER DATABASE COMMIT TO SWITCHOVER PRIMARY;<br>ALTER DATABASE ACTIVATE STANDBY DATABASE;<br>`<br>If your DB instance is a replica, use the following statement to<br>change it back to the `PHYSICAL STANDBY` role:<br>`<br>ALTER DATABASE CONVERT TO PHYSICAL STANDBY;<br>`<br>After the support perimeter determines that the database role is<br>supported, your RDS Custom for Oracle DB instance becomes available within 15<br>seconds. |
| **`SP-O3003`** | Database health             | **`The SMON process of the Oracle database is in a zombie<br>state. To resolve the issue, manually recover the database on EC2<br>instance [`ec2_id`], open the database, and<br>then immediately back it up. For more help, contact<br>Support.`** | The support perimeter monitors the DB instance state. It also monitors how<br>many restarts occurred during the previous hour and day. You're<br>notified when the instance is in a state where it still exists, but you<br>can't interact with it.<br>To make the support perimeter evaluate your instance state<br>1. Log in to your host and determine the database state.<br>```<br>ps -eo pid,state,command                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | grep smon<br>```<br>2. If necessary, restart your DB instance. If the restart fails,<br>proceed to the next step.<br>3. If necessary, restart your EC2 host.<br>After your DB instance restarts, the RDS Custom agent detects that your DB instance is<br>no longer in an unresponsive state. It then notifies the support<br>perimeter to reevaluate your DB instance state. |
| **`SP-O3004`** | Database log mode           | **`The database log mode on EC2 instance<br>[`ec2_id`] was changed to<br>[`value_b`]. To resolve the issue, set<br>the log mode to [`value_a`].`**                                                                                                  | To change your DB instance log mode to `ARCHIVELOG`<br>1. Log in to your EC2 host.<br>2. Connect to your database and run the following<br>statement:<br>`<br>SELECT LOG_MODE FROM V$DATABASE;<br>`<br>Or you can run the follow command in SQL\*Plus:<br>`<br>ARCHIVE LOG LIST<br>`<br>3. Run the following SQL\*Plus command to initiate a consistent<br>shutdown.<br>`<br>SHUTDOWN IMMEDIATE<br>`<br>The RDS Custom agent automatically restarts your DB instance and sets the log<br>mode to `ARCHIVELOG`. Your DB instance becomes available within 30<br>minutes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **`SP-O3005`** | Oracle home path            | **`The Oracle home on EC2 instance<br>[`ec2_id`] was changed to<br>`new_path`. To resolve the issue,<br>revert the setting to<br>`old_path`.`**                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **`SP-O3006`** | Database unique name        | **`The database unique name on EC2 instance<br>[`ec2_id`] was changed to<br>`new_value`. To resolve the issue,<br>revert the name to `old_value`.`**                                                                                                | To change the database unique name for your DB instance<br>1. Log in to your EC2 host.<br>2. Connect to the database and run the following<br>statement:<br>`<br>SELECT DB_UNIQUE_NAME FROM V$DATABASE;<br>`<br>3. Specify the original database unique name using the command<br>`ALTER SYSTEM SET DB_UNIQUE_NAME`.<br>4. Run the following SQL statement to initiate a consistent<br>shutdown.<br>`<br>SHUTDOWN IMMEDIATE;<br>`<br>The RDS Custom agent automatically restarts your DB instance and sets the log<br>mode to `ARCHIVELOG`. Your DB instance becomes available within 30<br>minutes.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## Troubleshooting upgrades for RDS Custom for Oracle

Your upgrade of an RDS Custom for Oracle instance might fail. Following, you can find techniques that you can use during upgrades of RDS Custom DB for
Oracle DB instances:

- Examine the upgrade output log files in the `/tmp` directory on
  your DB instance. The names of the logs depend on your DB engine version. For example, you
  might see logs that contain the strings `catupgrd` or
  `catup`.
- Examine the `alert.log` file located in the
  `/rdsdbdata/log/trace` directory.
- Run the following `grep` command in the `root` directory to track the upgrade OS process. This command
  shows where the log files are being written and determine the state of the upgrade process.

```
ps -aux | grep upg
```

The following shows sample output.

```
root     18884  0.0  0.0 235428  8172 ?        S<   17:03   0:00 /usr/bin/sudo -u rdsdb /rdsdbbin/scripts/oracle-control ORCL op_apply_upgrade_sh RDS-UPGRADE/2.upgrade.sh
rdsdb    18886  0.0  0.0 153968 12164 ?        S<   17:03   0:00 /usr/bin/perl -T -w /rdsdbbin/scripts/oracle-control ORCL op_apply_upgrade_sh RDS-UPGRADE/2.upgrade.sh
rdsdb    18887  0.0  0.0 113196  3032 ?        S<   17:03   0:00 /bin/sh /rdsdbbin/oracle/rdbms/admin/RDS-UPGRADE/2.upgrade.sh
rdsdb    18900  0.0  0.0 113196  1812 ?        S<   17:03   0:00 /bin/sh /rdsdbbin/oracle/rdbms/admin/RDS-UPGRADE/2.upgrade.sh
rdsdb    18901  0.1  0.0 167652 20620 ?        S<   17:03   0:07 /rdsdbbin/oracle/perl/bin/perl catctl.pl -n 4 -d /rdsdbbin/oracle/rdbms/admin -l /tmp catupgrd.sql
root     29944  0.0  0.0 112724  2316 pts/0    S+   18:43   0:00 grep --color=auto upg
```

- Run the following SQL query to verify the current state of the components to find the database version and the options installed on
  the DB instance.

```
SET LINESIZE 180
COLUMN COMP_ID FORMAT A15
COLUMN COMP_NAME FORMAT A40 TRUNC
COLUMN STATUS FORMAT A15 TRUNC
SELECT COMP_ID, COMP_NAME, VERSION, STATUS FROM DBA_REGISTRY ORDER BY 1;
```

The output resembles the following.

```
COMP_NAME                                STATUS               PROCEDURE
---------------------------------------- -------------------- --------------------------------------------------
Oracle Database Catalog Views            VALID                DBMS_REGISTRY_SYS.VALIDATE_CATALOG
Oracle Database Packages and Types       VALID                DBMS_REGISTRY_SYS.VALIDATE_CATPROC
Oracle Text                              VALID                VALIDATE_CONTEXT
Oracle XML Database                      VALID                DBMS_REGXDB.VALIDATEXDB

4 rows selected.
```

- Run the following SQL query to check for invalid objects that might interfere with the upgrade process.

```
SET PAGES 1000 LINES 2000
COL OBJECT FOR A40
SELECT SUBSTR(OWNER,1,12) OWNER,
       SUBSTR(OBJECT_NAME,1,30) OBJECT,
       SUBSTR(OBJECT_TYPE,1,30) TYPE, STATUS,
       CREATED
FROM   DBA_OBJECTS
WHERE  STATUS <>'VALID'
AND    OWNER IN ('SYS','SYSTEM','RDSADMIN','XDB');
```

## Troubleshooting replica promotion for RDS Custom for Oracle

You can promote managed Oracle replicas in RDS Custom for Oracle using the console,
`promote-read-replica` AWS CLI command, or `PromoteReadReplica` API.
If you delete your primary DB instance, and all replicas are healthy, RDS Custom for Oracle promotes
your managed replicas to standalone instances automatically. If a replica has paused
automation or is outside the support perimeter, you must fix the replica before RDS Custom can
promote it automatically. For more information, see [Promoting an RDS Custom for Oracle replica to a standalone DB instance](custom-rr.md "custom-rr.md").

The replica promotion workflow might become stuck in the following situation:

- The primary DB instance is in the state `STORAGE_FULL`.
- The primary database can't archive all of its online redo logs.
- A gap exists between the archived redo log files on your Oracle replica and the primary database.

###### To respond to the stuck workflow

1. Synchronize the redo log gap on your Oracle replica DB instance.
2. Force the promotion of your read replica to the latest applied redo log. Run the following commands in SQL\*Plus:

```
ALTER DATABASE ACTIVATE STANDBY DATABASE;
SHUTDOWN IMMEDIATE
STARTUP
```

3. Contact Support and ask them to move your DB instance to `available`
   status.
