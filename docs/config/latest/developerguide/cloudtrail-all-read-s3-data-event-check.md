# cloudtrail-all-read-s3-data-event-check

Checks if an AWS CloudTrail multi-Region trail is enabled and logs all read S3 data events for your buckets. The rule is NON\_COMPLIANT if no multi-Region trail logs all read S3 data event types for all current and future S3 buckets.

**Identifier:** CLOUDTRAIL\_ALL\_READ\_S3\_DATA\_EVENT\_CHECK

**Resource Types:** AWS::::Account

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (Taipei) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
