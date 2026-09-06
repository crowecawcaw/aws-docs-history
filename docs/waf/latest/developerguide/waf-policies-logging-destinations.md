

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Logging destinations
<a name="waf-policies-logging-destinations"></a>

This section describes the logging destinations that you can choose to send your AWS WAF policy logs. Each section provides guidance for configuring logging for the destination type and information about any behavior that's specific to the destination type. After you've configured your logging destination, you can provide its specifications to your Firewall Manager AWS WAF policy to start logging to it.

Firewall Manager doesn't have visibility into log failures after creating the logging configuration. It's your responsibility to verify that log delivery is working as you intended.

Firewall Manager doesn't modify any existing logging configurations in your organization's member accounts. 

**Topics**
+ [Amazon Data Firehose data streams](#waf-policies-logging-destinations-kinesis-data-firehose)
+ [Amazon Simple Storage Service buckets](#waf-policies-logging-destinations-s3)

## Amazon Data Firehose data streams
<a name="waf-policies-logging-destinations-kinesis-data-firehose"></a>

This topic provides information for sending your web ACL traffic logs to an Amazon Data Firehose data stream.

When you enable Amazon Data Firehose logging, Firewall Manager sends logs from your policy's web ACLs to an Amazon Data Firehose where you've configured a storage destination. After you enable logging, AWS WAF delivers logs for each configured web ACL, through the HTTPS endpoint of Kinesis Data Firehose to the configured storage destination. Before you use it, test your delivery stream to be sure that it has enough throughput to accommodate your organization's logs. For more information about how to create an Amazon Kinesis Data Firehose and review the stored logs, see [What Is Amazon Data Firehose?](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html)

You must have the following permissions to successfully enable logging with a Kinesis:
+ `iam:CreateServiceLinkedRole`
+ `firehose:ListDeliveryStreams`
+ `wafv2:PutLoggingConfiguration`

When you configure a Amazon Data Firehose logging destination on an AWS WAF policy, Firewall Manager creates a web ACL for the policy in the Firewall Manager administrator account as follows: 
+ Firewall Manager creates the web ACL in the Firewall Manager administrator account regardless of whether the account is in scope of the policy.
+ The web ACL has logging enabled, with a log name `FMManagedWebACLV2-Logging{{policy name}}-{{timestamp}}`, where the timestamp is the UTC time that the log was enabled for the web ACL, in milliseconds. For example, `FMManagedWebACLV2-LoggingMyWAFPolicyName-1621880565180`. The web ACL has no rule groups and no associated resources. 
+ You are charged for the web ACL according to the AWS WAF pricing guidelines. For more information, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/). 
+ Firewall Manager deletes the web ACL when you delete the policy. 

For information about service-linked roles and the `iam:CreateServiceLinkedRole` permission, see [Using service-linked roles for AWS WAF](using-service-linked-roles.md).

For more information about creating your delivery stream, see [Creating an Amazon Data Firehose Delivery Stream](https://docs.aws.amazon.com/firehose/latest/dev/basic-create.html).

## Amazon Simple Storage Service buckets
<a name="waf-policies-logging-destinations-s3"></a>

This topic provides information for sending your web ACL traffic logs to an Amazon S3 bucket.

The bucket that you choose as your logging destination must be owned by a Firewall Manager administrator account. For information about the requirements for creating your Amazon S3 bucket for logging and bucket naming requirements, see [Amazon Simple Storage Service ](https://docs.aws.amazon.com/waf/latest/developerguide/logging-s3.html) in the *AWS WAF Developer Guide*.

**Eventual consistency**  
When you make change to AWS WAF policies configured with an Amazon S3 logging destination, Firewall Manager updates the bucket policy to add the permissions necessary for logging. When doing so, Firewall Manager follows the last-writer-wins semantics and data consistency models that Amazon Simple Storage Service follows. If you concurrently make multiple policy updates to a Amazon S3 destination in the Firewall Manager console or through the [PutPolicy](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_PutPolicy.html) API, some permissions may not be saved. For more information about the Amazon S3 data consistency model, see [Amazon S3 data consistency model](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html#ConsistencyModel) in the *Amazon Simple Storage Service User Guide*.

### Permissions to publish logs to an Amazon S3 bucket
<a name="waf-policies-logging-s3-permissions"></a>

Configuring web ACL traffic logging for an Amazon S3 bucket in an AWS WAF policy requires the following permissions settings. Firewall Manager automatically attaches these permissions to your Amazon S3 bucket when you configure Amazon S3 as your logging destination to give the service permission to publish logs to the bucket. If you want to manage finer-grained access to your logging and Firewall Manager resources, you can set these permissions yourself. For information about managing permissions, see [Access management for AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the *IAM User Guide*. For information about the AWS WAF managed policies, see [AWS managed policies for AWS WAF](security-iam-awsmanpol.md). 

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Id": "AWSLogDeliveryForFirewallManager",
    "Statement": [
        {
            "Sid": "AWSLogDeliveryAclCheckFMS",
            "Effect": "Allow",
            "Principal": {
                "Service": "delivery.logs.amazonaws.com"
            },
            "Action": "s3:GetBucketAcl",
            "Resource": "arn:aws:s3:::aws-waf-logs-{{amzn-s3-demo-destination-bucket}}-suffix"
        },
        {
            "Sid": "AWSLogDeliveryWriteFMS",
            "Effect": "Allow",
            "Principal": {
                "Service": "delivery.logs.amazonaws.com"
            },
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::aws-waf-logs-{{amzn-s3-demo-destination-bucket}}-suffix/{{policy-id}}/AWSLogs/*",
            "Condition": {
                "StringEquals": {
                    "s3:x-amz-acl": "bucket-owner-full-control"
                }
            }
        }
    ]
}
```

------

To prevent the cross-service confused deputy problem, you can add the [`aws:SourceArn`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn) and [`aws:SourceAccount`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceaccount) global condition context keys to your bucket's policy. To add these keys, you can either modify the policy that Firewall Manager creates for you when you configure the logging destination, or if you want fine grained control, you can create your own policy. If you add these conditions to your logging destination policy, Firewall Manager won't validate or monitor the confused deputy protections. For general information about the confused deputy problem, see [The confused deputy problem ](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html) in the *IAM User Guide*. 

When you add the `sourceAccount` add `sourceArn` properties it'll increase the bucket policy size. If you're adding a long list of `sourceAccount` add `sourceArn` properties, take care not to exceed the Amazon S3 [bucket policy size](https://docs.aws.amazon.com/general/latest/gr/s3.html#limits_s3) quota.

The following example shows how to prevent the confused deputy problem by using the `aws:SourceArn` and `aws:SourceAccount` global condition context keys in your bucket's policy. Replace {{member-account-id}} with the account IDs of the members in your organization.

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Id":"AWSLogDeliveryForFirewallManager",
   "Statement":[
      {
         "Sid":"AWSLogDeliveryAclCheckFMS",
         "Effect":"Allow",
         "Principal":{
            "Service":"delivery.logs.amazonaws.com"
         },
         "Action":"s3:GetBucketAcl",
         "Resource":"arn:aws:s3:::aws-waf-logs-{{amzn-s3-demo-destination-bucket}}-suffix",
         "Condition":{
            "StringEquals":{
               "aws:SourceAccount":[
               "{{111122223333}}",
               "{{444455556666}}"
               ]
            },
            "ArnLike":{
               "aws:SourceArn":[
               "arn:aws:logs:*:{{111122223333}}:*",
               "arn:aws:logs:*:{{444455556666}}:*"
               ]
            }
         }
      },
      {
         "Sid":"AWSLogDeliveryWriteFMS",
         "Effect":"Allow",
         "Principal":{
            "Service":"delivery.logs.amazonaws.com"
         },
         "Action":"s3:PutObject",
         "Resource":"arn:aws:s3:::aws-waf-logs-{{amzn-s3-demo-destination-bucket}}-suffix/{{policy-id}}/AWSLogs/*",
         "Condition":{
            "StringEquals":{
               "s3:x-amz-acl":"bucket-owner-full-control",
               "aws:SourceAccount":[
               "{{111122223333}}",
               "{{444455556666}}"
               ]
            },
            "ArnLike":{
               "aws:SourceArn":[
               "arn:aws:logs:*:{{111122223333}}:*",
               "arn:aws:logs:*:{{444455556666}}:*"
               ]
            }
         }
      }
   ]
}
```

------

#### Server-side encryption for Amazon S3 buckets
<a name="waf-policies-logging-s3-kms-permissions"></a>

You can enable Amazon S3 server-side encryption or use a AWS Key Management Service customer managed key on your S3 bucket. If you choose to use the default Amazon S3 encryption on your Amazon S3 bucket for AWS WAF logs, you don't need to take any special action. However, if you choose to use a customer-provided encryption key to encrypt your Amazon S3 data at rest, you must add the following permission statement to your AWS Key Management Service key policy:

```
{
            "Sid": "Allow Logs Delivery to use the key",
            "Effect": "Allow",
            "Principal": {
                "Service": "delivery.logs.amazonaws.com"
            },
            "Action": [
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:ReEncrypt*",
                "kms:GenerateDataKey*",
                "kms:DescribeKey"
            ],
            "Resource": "*"
}
```

For information about using customer-provided encryption keys with Amazon S3, see [Using server-side encryption with customer-provided keys (SSE-C)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html) in the *Amazon Simple Storage Service User Guide*.