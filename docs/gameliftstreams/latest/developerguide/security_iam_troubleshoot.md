# Troubleshooting Amazon GameLift Streams identity and access

Use the following information to help you diagnose and fix common issues that you might
encounter when working with Amazon GameLift Streams and IAM.

###### Topics

- [I am not authorized to perform an action in Amazon GameLift Streams](#security_iam_troubleshoot-no-permissions "#security_iam_troubleshoot-no-permissions")
- [I am not authorized to perform iam:PassRole](#security_iam_troubleshoot-passrole "#security_iam_troubleshoot-passrole")
- [I want to allow people outside of my AWS account to access my Amazon GameLift Streams resources](#security_iam_troubleshoot-cross-account-access "#security_iam_troubleshoot-cross-account-access")

## I am not authorized to perform an action in Amazon GameLift Streams

If you receive an error that you're not authorized to perform an action, your
policies must be updated to allow you to perform the action.

The following example error occurs when the `mateojackson` IAM user
tries to use the console to view details about a fictional
`my-example-widget` resource but doesn't
have the fictional `gameliftstreams:`GetWidget`` permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: gameliftstreams:GetWidget on resource: my-example-widget
```

In this case, the policy for the `mateojackson` user must be updated to allow access to the
`my-example-widget` resource by using the
`gameliftstreams:`GetWidget`` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

## I am not authorized to perform iam:PassRole

If you receive an error that you're not authorized to perform the `iam:PassRole`
action, you must update your IAM policy to allow you to pass a role to Amazon GameLift Streams.

You need the `iam:PassRole` permission to call
`StartStreamSession` with the `RoleArn` parameter.

For resolution steps and an example IAM policy, see the "Access denied on iam:PassRole"
section in [Troubleshooting session credentials](session-credentials-troubleshooting.md "session-credentials-troubleshooting.md"). For more information about
`iam:PassRole`, see [Granting a user permissions to pass
a role to an AWS service](../../../IAM/latest/UserGuide/id_roles_use_passrole.md "../../../IAM/latest/UserGuide/id_roles_use_passrole.md") in the _IAM User Guide_.

## I want to allow people outside of my AWS account to access my Amazon GameLift Streams resources

This is not possible with Amazon GameLift Streams. All API access is restricted to the account which owns the resources. Instead, customers who
wish to share content externally are responsible for using their account to initiate new stream sessions on behalf of other users using
Amazon GameLift Streams APIs, and forwarding the appropriate connection information to those external users' web browsers.
