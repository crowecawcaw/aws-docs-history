# Giving Amazon Managed Service for Prometheus

permission to send alert messages to your Amazon SNS topic

You must give Amazon Managed Service for Prometheus permission to send messages to your Amazon SNS topic. The
following policy statement will give that permission. It includes a
`Condition` statement to help prevent a security problem known as
the _confused deputy_ problem. The `Condition`
statement restricts access to the Amazon SNS topic to allow only operations coming
from this specific account and Amazon Managed Service for Prometheus workspace. For more information about
the confused deputy problem, see [Cross-service
confused deputy prevention](#cross-service-confused-deputy-prevention "#cross-service-confused-deputy-prevention").

###### To give Amazon Managed Service for Prometheus permission to send messages to your Amazon SNS topic

1. Open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. In the navigation pane, choose **Topics**.
3. Choose the name of the topic that you are using with Amazon Managed Service for Prometheus.
4. Choose **Edit**.
5. Choose **Access policy** and add the following policy
   statement to the existing policy.

```
{
    "Sid": "Allow_Publish_Alarms",
    "Effect": "Allow",
    "Principal": {
        "Service": "aps.amazonaws.com"
    },
    "Action": [
        "sns:Publish",
        "sns:GetTopicAttributes"
    ],
    "Condition": {
        "ArnEquals": {
            "aws:SourceArn": "`workspace_ARN`"
        },
        "StringEquals": {
            "AWS:SourceAccount": "`account_id`"
        }
    },
    "Resource": "arn:aws:sns:`region`:`account_id`:`topic_name`"
}
```

[Optional] If your Amazon SNS topic is service side encryption (SSE)
enabled, you need to allow Amazon Managed Service for Prometheus to send messages to this encrypted
topic by adding the `kms:GenerateDataKey*` and
`kms:Decrypt` permissions to the AWS KMS key policy of the
key used to encrypt the topic.

For example, you could add the following to the policy:

```
{
  "Statement": [{
    "Effect": "Allow",
    "Principal": {
      "Service": "aps.amazonaws.com"
    },
    "Action": [
      "kms:GenerateDataKey*",
      "kms:Decrypt"
    ],
    "Resource": "*"
  }]
}
```

For more information, see [AWS KMS Permissions for SNS Topic](../../../sns/latest/dg/sns-key-management.md#sns-what-permissions-for-sse "../../../sns/latest/dg/sns-key-management.md#sns-what-permissions-for-sse"). 6. Choose **Save changes**.

###### Note

By default, Amazon SNS creates the access policy with condition on
`AWS:SourceOwner`. For more information, see [SNS Access Policy](../../../sns/latest/dg/sns-access-policy-use-cases.md#source-account-versus-source-owner "../../../sns/latest/dg/sns-access-policy-use-cases.md#source-account-versus-source-owner").

###### Note

IAM follows the [Most-restrictive policy first](../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md "../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md") rule. In your SNS topic, if
there is a policy block that is more restrictive than the documented Amazon SNS
policy block, the permission for the topic policy is not granted. To
evaluate your policy and find out what's been granted, see [Policy evaluation logic](../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md "../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md").

## SNS topic

configuration for opt-in regions

You can use `aps.amazonaws.com` to configure an Amazon SNS topic in
the same AWS Region as your Amazon Managed Service for Prometheus workspace. To use an SNS topic from
a non-opt-in Region (such as us-east-1) with an opt-in Region (such as
af-south-1), you need to use the Regional service principal format. In the
Regional service principle, replace `us-east-1`
with the non-opt-in Region you want to use:
`aps.`us-east-1`.amazonaws.com`.

The following table lists the opt-in Regions and their corresponding
Regional service principals:

| Opt-in Regions and their Regional service principals | Region name    | Region                           | Regional service principal                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------------------------------------- | -------------- | -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Africa (Cape Town)                                   | af-south-1     | af-south-1.aps.amazonaws.com     |
| Asia Pacific (Hong Kong)                             | ap-east-1      | ap-east-1.aps.amazonaws.com      |
| Asia Pacific (Thailand)                              | ap-southeast-7 | ap-southeast-7.aps.amazonaws.com |
| Europe (Milan)                                       | eu-south-1     | eu-south-1.aps.amazonaws.com     |
| Europe (Zurich)                                      | eu-central-2   | eu-central-2.aps.amazonaws.com   |
| Middle East (UAE)                                    | me-central-1   | me-central-1.aps.amazonaws.com   |
| Asia Pacific (Malaysia)                              | ap-southeast-5 | ap-southeast-5.aps.amazonaws.com | For information on enabling an opt-in Region, see [Managing AWS Regions](../../../accounts/latest/reference/manage-acct-regions.md "../../../accounts/latest/reference/manage-acct-regions.md") in the _IAM User Guide_ in the Amazon Web Services General Reference. When configuring your Amazon SNS topic for these opt-in Regions, ensure you use the correct Regional service principal to enable cross-region delivery of alerts. ## Cross-service confused deputy prevention The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action. In AWS, cross-service impersonation can result in the confused deputy problem. Cross-service impersonation can occur when one service (the _calling service_) calls another service (the _called service_). The calling service can be manipulated to use its permissions to act on another customer's resources in a way it should not otherwise have permission to access. To prevent this, AWS provides tools that help you protect your data for all services with service principals that have been given access to resources in your account. We recommend using the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context keys in resource policies to limit the permissions that Amazon Managed Service for Prometheus gives to Amazon SNS to the resource. If you use both global condition context keys, the `aws:SourceAccount` value and the account in the `aws:SourceArn` value must use the same account ID when used in the same policy statement. The value of `aws:SourceArn` must be the ARN of the Amazon Managed Service for Prometheus workspace. The most effective way to protect against the confused deputy problem is to use the `aws:SourceArn` global condition context key with the full ARN of the resource. If you don't know the full ARN of the resource or if you are specifying multiple resources, use the `aws:SourceArn` global context condition key with wildcards (`*`) for the unknown portions of the ARN. For example, `arn:aws:`servicename`::`123456789012`:*`. The policy shown in [Giving Amazon Managed Service for Prometheus permission to send alert messages to your Amazon SNS topic](AMP-alertmanager-receiver-AMPpermission.md "AMP-alertmanager-receiver-AMPpermission.md") shows how you can use the `aws:SourceArn` and `aws:SourceAccount` global condition context keys in Amazon Managed Service for Prometheus to prevent the confused deputy problem. |
