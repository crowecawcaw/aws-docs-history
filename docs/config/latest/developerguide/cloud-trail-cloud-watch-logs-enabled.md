# cloud-trail-cloud-watch-logs-enabled

Checks if AWS CloudTrail trails are configured to send logs to CloudWatch logs. The trail is NON_COMPLIANT if the CloudWatchLogsLogGroupArn property of the trail is empty.

**Identifier:** CLOUD_TRAIL_CLOUD_WATCH_LOGS_ENABLED

**Resource Types:** AWS::CloudTrail::Trail

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

expectedDeliveryWindowAge (Optional)
Type: int

Maximum age in hours of the most recent delivery to CloudWatch logs that satisfies compliance.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
