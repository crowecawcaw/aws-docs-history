# s3-bucket-logging-enabled

Checks if logging is enabled for your S3 buckets. The rule is NON_COMPLIANT if logging is not enabled.

**Identifier:** S3_BUCKET_LOGGING_ENABLED

**Resource Types:** AWS::S3::Bucket

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

targetPrefix (Optional)
Type: String

Prefix of the S3 bucket for storing server access logs.

targetBucket (Optional)
Type: String

Target S3 bucket for storing server access logs.

## Proactive Evaluation

For steps on how to run this rule in proactive mode,
see [Evaluating Your Resources with AWS Config Rules](evaluating-your-resources.md#evaluating-your-resources-proactive "evaluating-your-resources.md#evaluating-your-resources-proactive").
For this rule to return COMPLIANT in proactive mode, the resource configuration schema for the [StartResourceEvaluation](../APIReference/API_StartResourceEvaluation.md "../APIReference/API_StartResourceEvaluation.md") API needs to include the following inputs, encoded as a string:

```
"ResourceConfiguration":
...
{
   "BucketName": "`amzn-s3-demo-bucket`",
   "LoggingConfiguration": {
         "DestinationBucketName": "`amzn-s3-demo-destination-bucket`",
         "LogFilePrefix":"`my-log`"
   }
}
...

```

For more information on proactive evaluation, see [Evaluation Mode](evaluate-config-rules.md "evaluate-config-rules.md").

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
