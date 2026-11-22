

# `AWSSupportRemediator-EnableRedshiftClusterAuditLogging`

**Description**

Enables audit logging to Amazon CloudWatch Logs on an Amazon Redshift cluster.

The runbook calls the Amazon Redshift `EnableLogging` API with `LogDestinationType` set to `cloudwatch` and the requested log types.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [Amazon Redshift clusters should have audit logging enabled](https://docs.aws.amazon.com/securityhub/latest/userguide/redshift-controls.html#redshift-4).

If the Amazon Redshift cluster does not exist or audit logging is already enabled, the automation completes successfully without making changes.

Amazon Redshift supports Amazon Simple Storage Service (Amazon S3) and CloudWatch Logs as audit logging destinations. If the cluster already publishes audit logs to Amazon S3, this automation does not switch the destination to CloudWatch Logs because doing so would disrupt downstream consumers of the existing logs.

Enabling audit logging causes Amazon Redshift to publish the requested log types to CloudWatch Logs. By default, this automation publishes connection logs and user logs. Amazon Redshift delivers logs in the same AWS Region as the cluster. CloudWatch Logs storage and ingestion charges apply. For more information about pricing, see [Amazon CloudWatch Logs pricing](https://aws.amazon.com/cloudwatch/pricing/). Amazon Redshift creates new log groups under `/aws/redshift/cluster/<cluster-identifier>/<log-type>` on first log delivery. To disable audit logging after enabling it, call the Amazon Redshift `DisableLogging` API on the cluster.

The user activity log stream contains full SQL statement text, which can include literals, personally identifiable information (PII), or other sensitive content. By default, this automation does not export the user activity log. To include user activity logging, pass `LogExports` as `[connectionlog, userlog, useractivitylog]`. Amazon Redshift publishes user activity content only when the cluster's parameter group has `enable_user_activity_logging` set to `true`. By default, this parameter is `false`, and the cluster does not capture SQL text.

Amazon Redshift creates the CloudWatch log groups with the account's default CloudWatch Logs settings. This automation does not associate an AWS Key Management Service (AWS KMS) key or set a retention period on the log groups. To customize encryption, see [Encrypt log data in CloudWatch Logs using AWS Key Management Service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/encrypt-log-data-kms.html). To set a finite retention period, see [Change log data retention in CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html).

Amazon Redshift uses its service principal to deliver audit logs to CloudWatch Logs asynchronously after this automation enables logging. If your CloudWatch Logs resource policy or AWS KMS key policy denies the Amazon Redshift service principal, log delivery does not succeed. Before running this automation, verify that any such policies allow the Amazon Redshift service principal for the cluster's AWS Region. To confirm delivery after running this automation, call the Amazon Redshift `DescribeLoggingStatus` API. Inspect `LastSuccessfulDeliveryTime` and `LastFailureMessage` to verify the result.

**Important considerations**  
You are responsible for reviewing automation actions before they run.
This automation might cause stack drift if the resource is part of an AWS CloudFormation stack. The next stack update or rollback reverts the audit logging configuration to the value defined in the stack template.
Access to `AWSSupportRemediator-*` runbooks requires an active Business Support\+, Enterprise Support, or Unified Operations Support plan. For more information, see [Compare AWS Support Plans](https://aws.amazon.com/premiumsupport/plans/) on the AWS website.

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ ClusterIdentifier

  Type: String

  Description: (Required) The unique identifier of the Amazon Redshift cluster on which to enable audit logging.
+ LogExports

  Type: StringList

  Description: (Optional) The collection of exported log types. Possible values are `connectionlog`, `userlog`, and `useractivitylog`. Default: [connectionlog, userlog]. The default excludes `useractivitylog` because that log stream can contain full SQL statement text. Pass `useractivitylog` only when you need to capture SQL text in CloudWatch Logs and have appropriate retention and access controls configured.

  Default: ['connectionlog', 'userlog']

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `redshift:DescribeLoggingStatus`
+ `redshift:EnableLogging`

**Document Steps**

1. **validateInputs** - Checks whether the specified Amazon Redshift cluster exists and whether audit logging is already enabled. Returns no change required when the cluster does not exist or already has logging enabled.

1. **branchOnChangeRequired** - Branches on whether a change is required. Continues to `enableLogging` when `validateInputs.ChangeRequired` is `true`. Otherwise, ends the runbook successfully.

1. **enableLogging** - Calls the Amazon Redshift `EnableLogging` API for the specified cluster with `LogDestinationType` set to `cloudwatch` and the requested log export types.

**Outputs**
+ validateInputs.ChangeRequired: Whether a change is required. `false` when the cluster does not exist or already has audit logging enabled.
+ validateInputs.ValidationMessage: A message describing why no change is required, or `N/A` when a change is required.
+ validateInputs.ExistingLoggingConfiguration: The initial audit logging configuration from `DescribeLoggingStatus`. Useful for post-execution review when the cluster already has logging enabled.
+ enableLogging.Response: The response from the Amazon Redshift `EnableLogging` API after the automation applies a change.