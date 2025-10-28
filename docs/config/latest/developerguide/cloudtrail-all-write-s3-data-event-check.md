# cloudtrail-all-write-s3-data-event-check

Checks if an AWS CloudTrail multi-Region trail is enabled and logs all write S3 data events for your buckets. The rule is NON_COMPLIANT if no multi-Region trail logs all write S3 data event types for all current and future S3 buckets.

**Identifier:** CLOUDTRAIL_ALL_WRITE_S3_DATA_EVENT_CHECK

**Resource Types:** AWS::::Account

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
