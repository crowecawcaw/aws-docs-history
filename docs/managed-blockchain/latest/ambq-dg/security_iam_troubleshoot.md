# Troubleshooting Amazon Managed Blockchain (AMB) Query identity and

access

Use the following information to help you diagnose and fix common issues that you might
encounter when working with AMB Query and IAM.

###### Topics

- [I am not authorized to
  perform an action in AMB Query](#security_iam_troubleshoot-no-permissions "#security_iam_troubleshoot-no-permissions")

## I am not authorized to

perform an action in AMB Query

If you receive an error that you're not authorized to perform an action, your
policies must be updated to allow you to perform the action.

The following example error occurs when the `mateojackson` IAM user
tries to use the console to view details about a fictional
`my-example-widget` resource but doesn't
have the fictional `managedblockchain-query::`GetWidget`` permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: managedblockchain-query::GetWidget on resource: my-example-widget
```

In this case, the policy for the `mateojackson` user must be updated to allow access to the
`my-example-widget` resource by using the
`managedblockchain-query::`GetWidget`` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.
