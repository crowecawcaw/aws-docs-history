

# s3-bucket-logging-enabled
<a name="s3-bucket-logging-enabled"></a>

Checks if logging is enabled for your S3 buckets. The rule is NON\_COMPLIANT if logging is not enabled. 



**Identifier:** S3\_BUCKET\_LOGGING\_ENABLED

**Resource Types:** AWS::S3::Bucket

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

targetPrefix (Optional)Type: String  
Prefix of the S3 bucket for storing server access logs.

targetBucket (Optional)Type: String  
Target S3 bucket for storing server access logs.

## Proactive Evaluation
<a name="w2aac20c16c17b7e1395c19"></a>

 For steps on how to run this rule in proactive mode, see [Evaluating Your Resources with AWS Config Rules](./evaluating-your-resources.html#evaluating-your-resources-proactive). For this rule to return COMPLIANT in proactive mode, the resource configuration schema for the [StartResourceEvaluation](https://docs.aws.amazon.com/config/latest/APIReference/API_StartResourceEvaluation.html) API needs to include the following inputs, encoded as a string: 

```
"ResourceConfiguration":
...
{
   "BucketName": "{{amzn-s3-demo-bucket}}",
   "LoggingConfiguration": {
         "DestinationBucketName": "{{amzn-s3-demo-destination-bucket}}",
         "LogFilePrefix":"{{my-log}}"
   }
}
...
```

 For more information on proactive evaluation, see [Evaluation Mode](./evaluate-config-rules.html). 

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1395c21"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).