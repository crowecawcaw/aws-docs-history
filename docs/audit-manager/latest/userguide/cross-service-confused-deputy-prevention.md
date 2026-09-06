

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Cross-service confused deputy prevention
<a name="cross-service-confused-deputy-prevention"></a>

The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action. In AWS, cross-service impersonation can result in the confused deputy problem. Cross-service impersonation can occur when one service (the *calling service*) calls another service (the *called service*). The calling service can be manipulated to use its permissions to act on another customer's resources when it doesn't have permission to do so. To prevent this, Amazon Web Services provides tools that help you protect your data for all services with service principals that have been given access to resources in your account. 

We recommend using the [`aws:SourceArn`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn) and [`aws:SourceAccount`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceaccount) global condition context keys in resource policies to limit the permissions that AWS Audit Manager gives to another service for access to your resources. 
+ Use `aws:SourceArn` if you want only one resource to be associated with the cross-service access. You can also use `aws:SourceArn` with a wildcard (`*`) if you want to specify multiple resources.

  For example, you might use an Amazon SNS topic to receive activity notifications from Audit Manager. In this case, in your SNS topic access policy, the ARN value of `aws:SourceArn` is the Audit Manager resource that the notification comes from. Because it's likely that you have multiple Audit Manager resources, we recommend that you use `aws:SourceArn` with a wildcard. This enables you to specify all of your Audit Manager resources in your SNS topic access policy. 
+ Use `aws:SourceAccount` if you want to allow any resource in that account to be associated with the cross-service use. 
+ If the `aws:SourceArn` value doesn't contain the account ID, such as an Amazon S3 bucket ARN, you must use both global condition context keys to limit permissions. 
+ If you use both conditions, and if the `aws:SourceArn` value contains the account ID, the `aws:SourceAccount` value and the account in the `aws:SourceArn` value must show the same account ID when used in the same policy statement.
+ The most effective way to protect against the confused deputy problem is to use the `aws:SourceArn` global condition context key with the full ARN of the resource. If you don't know the full Amazon Resource Name (ARN) of the resource or if you are specifying multiple resources, use the `aws:SourceArn` global context condition key with wildcard characters (`*`) for the unknown portions of the ARN. For example, `arn:aws:{{servicename}}:*:{{123456789012}}:*`. 

## Audit Manager confused deputy support
<a name="audit-manager-confused-deputy-support"></a>

Audit Manager provides confused deputy support in the following scenarios. These policy examples show how you can use the `aws:SourceArn` and `aws:SourceAccount` condition keys to prevent the confused deputy problem.
+ [Example policy: The SNS topic that you use to receive Audit Manager notifications](https://docs.aws.amazon.com/audit-manager/latest/userguide/security_iam_id-based-policy-examples.html#sns-topic-permissions)
+ [Example policy: The KMS key that you use to encrypt your SNS topic](https://docs.aws.amazon.com/audit-manager/latest/userguide/security_iam_id-based-policy-examples.html#sns-key-permissions)

Audit Manager doesn't provide confused deputy support for the customer managed key that you provide in your Audit Manager [Configuring your data encryption settings](settings-KMS.md) settings. If you provided your own customer managed key, you can’t use `aws:SourceAccount` or `aws:SourceArn` conditions in that KMS key policy.