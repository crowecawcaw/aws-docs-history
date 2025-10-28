# Enabling Amazon CloudWatch Logs log forwarding for

AWS Managed Microsoft AD

You can use either the AWS Directory Service console or APIs to forward domain controller security event
logs to Amazon CloudWatch Logs for your AWS Managed Microsoft AD. This helps you to meet your security monitoring, audit,
and log retention policy requirements by providing transparency of the security events in your
directory.

CloudWatch Logs can also forward these events to other AWS accounts, AWS services, or third party
applications. This makes it easier for you to centrally monitor and configure alerts to detect
and respond proactively to unusual activities in near real time.

Once enabled, you can then use the CloudWatch Logs console to retrieve the data from the log group you
specified when you enabled the service. This log group contains the security logs from your
domain controllers.

For more information about log groups and how to read their data, see [Working with log groups and log streams](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md") in the _Amazon CloudWatch Logs User
Guide_.

###### Note

Log forwarding is a Regional feature of AWS Managed Microsoft AD.
If you are using [Multi-Region replication](ms_ad_configure_multi_region_replication.md "ms_ad_configure_multi_region_replication.md"), the
following procedures must be applied separately in each Region. For more information, see
[Global vs Regional features](multi-region-global-region-features.md "multi-region-global-region-features.md").

Once enabled, the log forwarding capability will begin transmitting logs from your domain controllers to the
specified CloudWatch log group. Any logs created before log forwarding is enabled will not be transferred to the CloudWatch log group.

###### Topics

- [Using the AWS Management Console to enable Amazon CloudWatch Logs
  log forwarding](#enable_log_forwarding_with_console "#enable_log_forwarding_with_console")
- [Using the CLI or PowerShell to enable
  Amazon CloudWatch Logs log forwarding](#enable_log_forwarding_with_cli "#enable_log_forwarding_with_cli")

## Using the AWS Management Console to enable Amazon CloudWatch Logs

log forwarding

You can enable Amazon CloudWatch Logs log forwarding for your AWS Managed Microsoft AD in the AWS Management Console.

1. In the [AWS Directory Service
   console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, choose **Directories**.
2. Choose the directory ID of the AWS Managed Microsoft AD directory that you want to share.
3. On the **Directory details** page, do one of the
   following:
   - If you have multiple Regions showing under **Multi-Region
     replication**, select the Region where you want to enable log forwarding,
     and then choose the **Networking & security** tab.
     For more information, see [Primary vs additional Regions](multi-region-global-primary-additional.md "multi-region-global-primary-additional.md").
   - If you do not have any Regions showing under **Multi-Region
     replication**, choose the **Networking &
     security** tab.

4. In the **Log forwarding** section, choose **Enable**.
5. On the **Enable log forwarding to CloudWatch** dialog, choose either of the
   following options:
   1. Select **Create a new CloudWatch log group**, under
      **CloudWatch Log group name**, specify a name that you can
      refer to in CloudWatch Logs.
   2. Select **Choose an existing CloudWatch log group**, and
      under **Existing CloudWatch log groups**, select a log group
      from the menu.

6. Review the pricing information and link, and then choose **Enable**.

## Using the CLI or PowerShell to enable

Amazon CloudWatch Logs log forwarding

Before you can use the [`ds create-log-subscription`](../../../cli/latest/reference/ds/create-log-subscription.md "../../../cli/latest/reference/ds/create-log-subscription.md") command, you must first create an
Amazon CloudWatch log group and then create an IAM resource policy that will grant the necessary
permission to that group. To enable log forwarding using the CLI or PowerShell, complete the
following steps.

### Step 1: Create a log group in CloudWatch Logs

Create a log group that will be used to receive the security logs from your domain
controllers. We recommend pre-pending the name with `/aws/directoryservice/`, but
that is not required. For example:

CLI Command

```
aws logs create-log-group --log-group-name '/aws/directoryservice/`d-1111111111`'
```

PowerShell Command

```
New-CWLLogGroup -LogGroupName '/aws/directoryservice/`d-1111111111`'
```

For instructions on how to create a CloudWatch Logs group, see [Create a log group in CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#Create-Log-Group "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#Create-Log-Group") in the _Amazon CloudWatch Logs User
Guide_.

### Step 2: Create a CloudWatch Logs resource policy in

IAM

Create a CloudWatch Logs resource policy granting AWS Directory Service rights to add logs into the new log group
you created in Step 1. You can either specify the exact ARN to the log group to limit
AWS Directory Service's access to other log groups or use a wild card to include all log groups. The
following sample policy uses the wild card method to identify that all log groups that start
with `/aws/directoryservice/` for the AWS account where your directory resides
will be included.

You will need to save this policy to a text file (for example DSPolicy.json) on your
local workstation as you will need to run it from the CLI. For example:

CLI Command

```
aws logs put-resource-policy --policy-name DSLogSubscription --policy-document
          file://DSPolicy.json
```

PowerShell Command

```
$PolicyDocument = Get-Content .\DSPolicy.json –Raw
```

```
Write-CWLResourcePolicy -PolicyName DSLogSubscription -PolicyDocument $PolicyDocument
```

### Step 3: Create an AWS Directory Service log

subscription

In this final step, you can now proceed to enable log forwarding by creating the log
subscription. For example:

CLI Command

```
aws ds create-log-subscription --directory-id '`d-1111111111`' --log-group-name '/aws/directoryservice/`d-1111111111`'
```

PowerShell Command

```
New-DSLogSubscription -DirectoryId '`d-1111111111`' -LogGroupName '/aws/directoryservice/`d-1111111111`'
```
