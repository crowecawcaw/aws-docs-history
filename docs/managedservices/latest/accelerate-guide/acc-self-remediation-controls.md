

# Self-remediation Security Hub controls in Accelerate
<a name="acc-self-remediation-controls"></a>

The following self-remediation controls are available in Accelerate.

**Topics**
+ [S3.7 - S3 general purpose buckets should use cross-Region replication](#acc-s37-control)
+ [S3.11 - S3 general purpose buckets should have event notifications enabled](#acc-s311-control)
+ [S3.13 - S3 general purpose buckets should have Lifecycle configurations](#acc-s313-control)
+ [S3.15 - S3 general purpose buckets should have Object Lock enabled](#acc-s315-control)
+ [Config.1 - AWS Config should be enabled and use the service-linked role for resource recording](#acc-config1-control)

## S3.7 - S3 general purpose buckets should use cross-Region replication
<a name="acc-s37-control"></a>

*Resources:*
+ arn:aws:s3:::ams-a<account\_id>-alarmmanager-<region>
+ arn:aws:s3:::ams-a<account\_id>-patch-data-reporting-<region>
+ arn:aws:s3:::ams-a<account\_id>-patch-data-reporting-<region>-audit
+ arn:aws:s3:::ams-config-recorder-bucket-<account\_id>
+ arn:aws:s3:::ams-config-recorder-bucket-<account\_id>-audit

The S3 buckets used by AMS infrastructure components do not have cross-Region replication enabled to optimize costs for you. Enabling cross-Region replication incurs data transfer charges for replicating data between regions, plus additional storage costs in the destination region. For buckets that support internal AMS operations and do not require geographic redundancy by default, cross-Region replication would add significant ongoing costs without providing necessary benefits.

Since these buckets store operational data such as alarm management, patch reporting, and configuration recording within a single region, cross-Region replication is not required for normal AMS operations. However, AMS offers the capability to enable cross-Region replication on these buckets based on your specific disaster recovery or compliance requirements. Contact AMS if you require assistance configuring cross-Region replication for your use case.

## S3.11 - S3 general purpose buckets should have event notifications enabled
<a name="acc-s311-control"></a>

*Resources:*
+ arn:aws:s3:::ams-a<account\_id>-alarmmanager-<region>
+ arn:aws:s3:::ams-a<account\_id>-patch-data-reporting-<region>
+ arn:aws:s3:::ams-a<account\_id>-patch-data-reporting-<region>-audit
+ arn:aws:s3:::ams-config-recorder-bucket-<account\_id>
+ arn:aws:s3:::ams-config-recorder-bucket-<account\_id>-audit

The S3 buckets used by AMS infrastructure components do not have event notifications enabled to optimize costs for you. Enabling S3 event notifications incurs charges for the notification delivery mechanism (such as Amazon Simple Notification Service, SQS, or AWS Lambda invocations), which can add up depending on the volume of S3 operations. See [Amazon SNS Pricing](https://aws.amazon.com/sns/pricing/) for more information.

Since these buckets support internal AMS operations and do not require event-driven workflows by default, we did not enable event notifications to avoid unnecessary costs. However, AMS offers the capability to enable event notifications on these buckets based on your specific monitoring or automation requirements. Contact AMS if you require assistance configuring event notifications for your use case.

## S3.13 - S3 general purpose buckets should have Lifecycle configurations
<a name="acc-s313-control"></a>

*Resources:*
+ arn:aws:s3:::ams-config-recorder-bucket-<account\_id>
+ arn:aws:s3:::ams-config-recorder-bucket-<account\_id>-audit

Historically, the component these S3 resources belong to has not included these configurations for cost-efficiency reasons for you. However, AMS offers the capability to remediate this control using your configuration. Contact AMS if you require assistance in doing so.

## S3.15 - S3 general purpose buckets should have Object Lock enabled
<a name="acc-s315-control"></a>

*Resources:*
+ arn:aws:s3:::ams-a<account\_id>-alarmmanager-<region>

The S3 buckets used by the AMS Alarm Manager system don't have Object Lock enabled due to cost-efficiency considerations for you. Enabling Object Lock can increase costs (require additional API calls resulting to an increase CloudTrail data) and operational complexity, particularly for buckets that require frequent object updates or deletions as part of normal operations. However, you can manually enable Object Lock on these buckets if your compliance or data retention requirements necessitate this feature. Contact AMS if you require assistance with this configuration.

*Resources:*
+ arn:aws:s3:::ams-a<account\_id>-patch-data-reporting-<region>
+ arn:aws:s3:::ams-a<account\_id>-patch-data-reporting-<region>-audit

Object Lock can't be enabled on the `ams-a<AccountID>-patch-data-reporting-<Region>` and `ams-a<AccountID>-patch-data-reporting-<Region>-audit` buckets due to AWS service limitations. The patch-data-reporting bucket receives data from Systems Manager inventory through SSM Resource Data Sync, which is incompatible with S3 Object Lock. The audit bucket serves as an S3 server access logs destination, which cannot have Object Lock enabled. For more information, see [Creating a resource data sync for Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/inventory-create-resource-data-sync.html) in the *AWS Systems Manager User Guide*. These AWS service constraints make Object Lock technically impossible while maintaining required functionality.

## Config.1 - AWS Config should be enabled and use the service-linked role for resource recording
<a name="acc-config1-control"></a>

*Resources:*
+ Config Recorder

During onboarding, AMS deploys AWS Config with the service-linked role `AWSServiceRoleForConfig` by default. However, this control might fail if you have supplied custom AWS Identity and Access Management roles for AWS Config instead of using the service-linked role to reduce costs. While custom roles can work, they require manual policy management and might not automatically receive updates when AWS Config adds support for new resource types or features.

You can self-remediate this finding by updating your AWS Config recorder to use the service-linked role `AWSServiceRoleForConfig`. This is the recommended configuration and aligns with AWS best practices. For detailed instructions on AWS Config infrastructure deployed by AMS, see [Infrastructure security monitoring](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-sec-infra-sec.html).