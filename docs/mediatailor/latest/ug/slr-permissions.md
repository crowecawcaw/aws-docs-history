# Service-linked role permissions for MediaTailor

MediaTailor uses the service-linked role named **AWSServiceRoleForMediaTailor** –
MediaTailor uses this service-linked role to invoke CloudWatch to create and manage log groups, log streams, and log events. This service-linked role is attached to the following managed policy:
`AWSMediaTailorServiceRolePolicy`.

The AWSServiceRoleForMediaTailor service-linked role trusts the following services to assume the
role:

- `mediatailor.amazonaws.com`
  The role permissions policy allows MediaTailor to complete the following actions on the
  specified resources:

- Action: `logs:PutLogEvents` on
  `arn:aws:logs:*:*:log-group:/aws/MediaTailor/*:log-stream:*`
- Action: `logs:CreateLogStream, logs:CreateLogGroup, logs:DescribeLogGroups, logs:DescribeLogStreams` on
  `arn:aws:logs:*:*:log-group:/aws/MediaTailor/*`
  You must configure permissions to allow an IAM entity (such as a user, group, or role)
  to create, edit, or delete a service-linked role. For more information, see [Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
  _IAM User Guide_.
