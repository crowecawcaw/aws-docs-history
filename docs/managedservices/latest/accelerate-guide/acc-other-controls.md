

# Other Security Hub controls in Accelerate
<a name="acc-other-controls"></a>

The following compensating controls are available in Accelerate.

**Topics**
+ [Lambda.3 - Lambda functions should be in a VPC](#acc-lambda3-control)
+ [S3.17 - S3 general purpose buckets should be encrypted at rest with AWS KMS keys](#acc-s317-control)
+ [KMS.2 - IAM principals should not have IAM inline policies that allow decryption actions on all KMS keys](#acc-kms2-control)
+ [S3.9 - S3 general purpose buckets should have server access logging enabled](#acc-s39-control)
+ [EC2.6 - VPC flow logging should be enabled in all VPCs](#acc-ec26-control)

## Lambda.3 - Lambda functions should be in a VPC
<a name="acc-lambda3-control"></a>

*Resources:*
+ AMSAlarmManagerDeploymentHandler
+ AMSAlarmManagerOrphanedAlarmCleanup
+ AMSAlarmManagerRemediation
+ AMSAlarmManagerReporting
+ AMSAlarmManagerTriggerEvaluation
+ AMSAlarmManagerValidation
+ AMSConfigExtensionDeploymentHandler
+ AMSConfigFSXExtension
+ AMSConfigOutpostExtension
+ AMSConfigSyntheticCanaryExtension

The AWS Lambda functions deployed by AMS don't communicate with resources in your accounts. Therefore, they don't require dedicated Elastic Network Interfaces (ENIs) or VPC placement. Deploying these functions outside of a VPC reduces costs and improves deployment speed. This approach doesn't introduce any security concerns for intra-resource communication. Since these Lambda functions operate independently and don't access VPC-based resources, VPC deployment adds unnecessary complexity and expense without providing additional security benefits.

## S3.17 - S3 general purpose buckets should be encrypted at rest with AWS KMS keys
<a name="acc-s317-control"></a>

*Resources:*
+ arn:aws:s3:::ams-a<account\_id>-alarmmanager-<region>

The Amazon Simple Storage Service buckets used by the AMS Alarm Manager system use Amazon-managed encryption keys (SSE-S3) instead of customer-managed KMS keys (SSE-KMS). Implementing customer-managed keys requires you to grant AMS explicit permissions to use your KMS keys through key policies. This introduces additional operational complexity and risk. Using this control provides strong encryption at rest while avoiding additional costs and operational complexity for you.

If you modify key policies, rotate keys improperly, or accidentally delete or disable your keys, AMS monitoring immediately fails for you. This dependency on customer-managed key availability compromises AMS critical monitoring and alerting infrastructure. It could potentially disrupt real-time monitoring capabilities, alert delivery, incident response, and service health visibility. Amazon-managed encryption keys automatically encrypt data at rest without requiring you to manage key policies, rotation schedules, or access permissions. This implementation meets encryption requirements while maintaining cost efficiency and operational simplicity for AMS-managed infrastructure.

*Resources:*
+ arn:aws:s3:::ams-a<account\_id>-cloudtrail-log-<region>-audit

The AWS CloudTrail audit logging bucket cannot use AWS KMS encryption due to AWS service limitations. S3 buckets that serve as server access logging destinations must not have KMS key encryption enabled. For more information, see [Configuring default encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-bucket-encryption.html) and [Troubleshoot server access logging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/troubleshooting-server-access-logging.html) in the *Amazon Simple Storage Service User Guide*. Enabling AWS KMS encryption on logging destination buckets can cause logging failures and create operational issues. This bucket uses Amazon S3-managed encryption (SSE-S3) instead. This provides encryption at rest while maintaining compatibility with S3 server access logging functionality.

## KMS.2 - IAM principals should not have IAM inline policies that allow decryption actions on all KMS keys
<a name="acc-kms2-control"></a>

*Resources:*
+ KMS Key: alias/ams/patchreporting

The inline policy contains "Resource": ["\*"] in a KMS key policy, which is a resource-based policy attached to a specific KMS key (ams\_ssm\_inventory\_bucket\_kms\_key). Key policies are inherently scoped to the individual key, and using \* in the Resource element is standard AWS practice since the policy scope is already constrained by the key itself. For more information, see [Creating a key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-overview.html) and [Default key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-default.html) in the *AWS KMS keys Developer Guide*. This configuration poses no security risk as access is limited to a single KMS key, not all keys in the account.

## S3.9 - S3 general purpose buckets should have server access logging enabled
<a name="acc-s39-control"></a>

*Resources:*
+ ams-config-recorder-bucket-<account\_id>-audit

These S3 buckets are access logging destination buckets for AWS Config Recorder buckets. S3 recommends against setting up access logging on these buckets as it will generate an infinite loops of logging, driving up cost unnecessarily. AWS Security Hub instead recommends that resources in this scenario should have findings suppressed.

*Remediation:*

You should suppress this finding for these affected buckets as the findings aren't useful. If you don't want to suppress the findings, then you can optionally configure self-logging on the bucket. Self-logging comes with the risk that the logging might be removed if AMS updates the bucket.

## EC2.6 - VPC flow logging should be enabled in all VPCs
<a name="acc-ec26-control"></a>

*Resources:*
+ Default vpc at account create

By default, AMS doesn't enable VPC Flow logs for the default VPC.

*Remediation:*

You can self-remediate the control by adding the `ams:managed=true` tag key/value, clearing the state of the config rule and re-running the evaluation of the rule. The auto-remediation component of AMS enables VPC Flow Logs on the vpc.