End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Cross-service confused deputy

prevention for AWS IoT Events

###### Note

- The AWS IoT Events service only allows you to use roles to start actions in the same account in
  which a resource was created. This helps prevent a confused deputy attack in AWS IoT Events.
- This page serves as a reference for you to see how the confused deputy issue works and
  can be prevented in the event that cross account resources were allowed in the AWS IoT Events
  service.
  The confused deputy problem is a security issue where an entity that doesn't have permission
  to perform an action can coerce a more-privileged entity to perform the action. In AWS,
  cross-service impersonation can result in the confused deputy problem.

Cross-service impersonation can occur when one service (the _calling
service_) calls another service (the _called service_). The
calling service can be manipulated to use its permissions to act on another customer's resources
in a way it should not otherwise have permission to access. To prevent this, AWS provides
tools that help you protect your data for all services with service principals that have been
given access to resources in your account.

We recommend using the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context keys in resource policies
to limit the permissions that AWS IoT Events gives another service to the resource. If the
`aws:SourceArn` value does not contain the account ID, such as an Amazon S3 bucket ARN,
you must use both global condition context keys to limit permissions. If you use both global
condition context keys and the `aws:SourceArn` value contains the account ID, the
`aws:SourceAccount` value and the account in the `aws:SourceArn` value
must use the same account ID when used in the same policy statement.

Use `aws:SourceArn` if you want only one resource to be associated with the
cross-service access. Use `aws:SourceAccount` if you want to allow any resource in
that account to be associated with the cross-service use.

The value of `aws:SourceArn` must be the Detector Model or Alarm model associated with the
`sts:AssumeRole` request.

The most effective way to protect against the confused deputy problem is to use the
`aws:SourceArn` global condition context key with the full ARN of the resource. If
you don't know the full ARN of the resource or if you are specifying multiple resources, use the
`aws:SourceArn` global context condition key with wildcards (`*`) for
the unknown portions of the ARN. For example,
`arn:aws:`iotevents`:*:`123456789012`:*`.

The following examples show how you can use the `aws:SourceArn` and
`aws:SourceAccount` global condition context keys in AWS IoT Events to prevent the
confused deputy problem.

###### Topics

- [Example: Secure access to an AWS IoT Events detector
  model](accessing-a-detector-model.md "accessing-a-detector-model.md")
- [Example: Secure access to an AWS IoT Events alarm model](accessing-an-alarm-model.md "accessing-an-alarm-model.md")
- [Example: Access an AWS IoT Events resource in a
  specified region](accessing-resource-in-specified-region.md "accessing-resource-in-specified-region.md")
- [Example: Configure logging options for AWS IoT Events](logging-options.md "logging-options.md")
