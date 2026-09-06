

# Guidance on subscribing to SNS Topics
<a name="sns-guidance"></a>

Subscribe to SNS topics to get information about your AWS Control Tower environment.

**Note**  
AWS Control Tower will stop sending drift notifications to SNS topic for all customers on LZ4.0\+.
+ The `aws-controltower-AllConfigNotifications` SNS topic receives all events published by AWS Config, including compliance notifications and Amazon CloudWatch event notifications. For example, this topic informs you if a control violation has occurred. It also gives information about other types of events. (Learn more from [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/notifications-for-AWS-Config.html) about what they publish when this topic is configured.) 
+ [Data Events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html?icmpid=docs_cloudtrail_console#logging-data-events) from the `aws-controltower-BaselineCloudTrail` trail are set to publish to the `aws-controltower-AllConfigNotifications` SNS topic as well.
+ To receive detailed compliance notifications, we recommend that you subscribe to the `aws-controltower-AllConfigNotifications` SNS topic. This topic aggregates compliance notifications from all child accounts.
+ To receive drift notifications and other notifications as well as compliance notifications, but fewer notifications overall, we recommend that you subscribe to the `aws-controltower-AggregateSecurityNotifications` SNS topic.
+ To receive notifications about AWS Control Tower Account Factory for Terraform (AFT) errors, you can subscribe to an SNS topic called [aft\_failure\_notifications](https://github.com/aws-ia/terraform-aws-control_tower_account_factory/blob/0f2caea57e37a1a58dc305e2f342e9c28aeb9c41/modules/aft-account-request-framework/sns.tf), shown in the AFT repository. For example:

  ```
  resource "aws_sns_topic" "aft_failure_notifications" {
      name = "aft-failure-notifications"
      kms_master_key_id = "alias/aws/sns"
  }
  ```
+ All SNS topics are encrypted at rest with disk encryption. for more information, see [Data encryption](https://docs.aws.amazon.com/sns/latest/dg/sns-data-encryption.html).

For more information about SNS topics and compliance, see [Prevention and notification](https://docs.aws.amazon.com/controltower/latest/userguide/prevention-and-notification.html).