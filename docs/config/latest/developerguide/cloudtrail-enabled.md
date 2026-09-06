

# cloudtrail-enabled
<a name="cloudtrail-enabled"></a>

**Important**  
For this rule, the rule identifier (CLOUD\_TRAIL\_ENABLED) and rule name (cloudtrail-enabled) are different.

Checks if an AWS CloudTrail trail is enabled in your AWS account. The rule is NON\_COMPLIANT if a trail is not enabled. Optionally, the rule checks a specific S3 bucket, Amazon Simple Notification Service (Amazon SNS) topic, and CloudWatch log group.



**Identifier:** CLOUD\_TRAIL\_ENABLED

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

s3BucketName (Optional)Type: String  
Name of S3 bucket for CloudTrail to deliver log files to.

snsTopicArn (Optional)Type: String  
SNS topic ARN for CloudTrail to use for notifications.

cloudWatchLogsLogGroupArn (Optional)Type: String  
CloudWatch log group ARN for CloudTrail to send data to.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d363c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).