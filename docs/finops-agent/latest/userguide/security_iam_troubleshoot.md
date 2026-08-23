AWS FinOps Agent is in preview release and is subject to change.

# Troubleshooting AWS FinOps Agent identity and access

Use the following information to help you diagnose and fix common issues that you might
encounter when working with AWS FinOps Agent and IAM.

###### Topics

- [I am not authorized to perform an action in AWS FinOps Agent](#security_iam_troubleshoot-no-permissions "#security_iam_troubleshoot-no-permissions")
- [I am not authorized to perform iam:PassRole](#security_iam_troubleshoot-passrole "#security_iam_troubleshoot-passrole")
- [I want to allow people outside of my AWS account to access my AWS FinOps Agent resources](#security_iam_troubleshoot-cross-account-access "#security_iam_troubleshoot-cross-account-access")

## I am not authorized to perform an action in AWS FinOps Agent

If you receive an error that you're not authorized to perform an action, your
policies must be updated to allow you to perform the action.

The following example error occurs when the `mateojackson` IAM user
tries to use the console to view details about a fictional
`my-example-widget` resource but doesn't
have the fictional `finops-agent:`GetWidget`` permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: finops-agent:GetWidget on resource: my-example-widget
```

In this case, the policy for the `mateojackson` user must be updated to allow access to the
`my-example-widget` resource by using the
`finops-agent:`GetWidget`` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

## I am not authorized to perform iam:PassRole

If you receive an error that you're not authorized to perform the `iam:PassRole` action, your policies must be updated to allow you to pass a role to AWS FinOps Agent.

Some AWS services allow you to pass an existing role to that service instead of creating a new service role or service-linked role. To do
this, you must have permissions to pass the role to the service.

The following example error occurs when an IAM user named `marymajor` tries to use the console to perform an action in
AWS FinOps Agent. However, the action requires the service to have permissions that are granted by a service role. Mary does not have permissions to pass the
role to the service.

```
User: arn:aws:iam::123456789012:user/`marymajor` is not authorized to perform: iam:PassRole
```

In this case, Mary's policies must be updated to allow her to perform the `iam:PassRole` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

## I want to allow people outside of my AWS account to access my AWS FinOps Agent resources

During preview, AWS FinOps Agent does not support cross-account access through resource-based policies. Adding a resource-based policy or another policy to the agent role does not grant a different AWS account access to an agent or its data. To analyze organization-wide cost data, deploy AWS FinOps Agent in your organization's management account (the payer account), where Cost Explorer provides organization-wide visibility subject to the IAM permissions you configure.
