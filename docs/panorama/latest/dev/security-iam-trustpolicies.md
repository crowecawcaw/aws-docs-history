End of support notice: On May 31, 2026, AWS will end support for
AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama
resources. For more information, see [AWS Panorama end of support](panorama-end-of-support.md "panorama-end-of-support.md").

# Cross-service confused deputy prevention

The confused deputy problem is a security issue where an entity that doesn't have permission to perform an
action can coerce a more-privileged entity to perform the action. In AWS, cross-service impersonation can result
in the confused deputy problem. Cross-service impersonation can occur when one service (the _calling
service_) calls another service (the _called service_). The calling service can be
manipulated to use its permissions to act on another customer's resources in a way it should not otherwise have
permission to access. To prevent this, AWS provides tools that help you protect your data for all services with
service principals that have been given access to resources in your account.

We recommend using the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context keys in resource policies to limit the
permissions that AWS Panorama gives another service to the resource. If you use both global condition context keys, the
`aws:SourceAccount` value and the account in the `aws:SourceArn` value must use the same
account ID when used in the same policy statement.

The value of `aws:SourceArn` must be the ARN of an AWS Panorama device.

The most effective way to protect against the confused deputy problem is to use the `aws:SourceArn`
global condition context key with the full ARN of the resource. If you don't know the full ARN of the resource or if
you are specifying multiple resources, use the `aws:SourceArn` global context condition key with
wildcards (`*`) for the unknown portions of the ARN. For example,
`arn:aws:`servicename`::`123456789012`:*`.

For instructions on securing the service role that AWS Panorama uses to give permission to the AWS Panorama Appliance, see [Securing the appliance role](permissions-services.md#permissions-services-appliance "permissions-services.md#permissions-services-appliance").
