# Troubleshooting Tag Editor identity and

access

Use the following information to help you diagnose and fix common issues that you might
encounter when working with Tag Editor and IAM.

###### Topics

- [I am not authorized to
  perform an action in Tag Editor](#security_iam_troubleshoot-permissions-taged "#security_iam_troubleshoot-permissions-taged")
- [I am not authorized to perform
  iam:PassRole](#security_troubleshoot-passrole "#security_troubleshoot-passrole")

## I am not authorized to

perform an action in Tag Editor

If the AWS Management Console tells you that you're not authorized to perform an action, then you
must contact your administrator for assistance. Your administrator is the person that
provided you with your sign-in credentials.

The following example error occurs when the user `mateojackson` tries to
use the console to view tags on a resource but does not have `tag:GetTagKeys`
permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: tag:GetTagKeys on resource: arn:aws:resource-groups::us-west-2:123456789012:`resource-type`/my-test-resource
```

In this case, Mateo asks his administrator to update his policies to allow him to
access the `my-test-resource` resource using the `tag:GetTagKeys`
action.

## I am not authorized to perform

iam:PassRole

If you receive an error that you're not authorized to perform the `iam:PassRole` action, your policies must be updated to allow you to pass a role to Tag Editor.

Some AWS services allow you to pass an existing role to that service instead of creating a new service role or service-linked role. To do
this, you must have permissions to pass the role to the service.

The following example error occurs when an IAM user named `marymajor` tries to use the console to perform an action in
Tag Editor. However, the action requires the service to have permissions that are granted by a service role. Mary does not have permissions to pass the
role to the service.

```
User: arn:aws:iam::123456789012:user/`marymajor` is not authorized to perform: iam:PassRole
```

In this case, Mary's policies must be updated to allow her to perform the `iam:PassRole` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.
