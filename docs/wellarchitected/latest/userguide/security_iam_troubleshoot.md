# Troubleshooting AWS Well-Architected Tool identity

and access

Use the following information to help you diagnose and fix common issues that you might
encounter when working with AWS WA Tool and IAM.

###### Topics

- [I'm not authorized to perform
  an action in AWS WA Tool](#security_iam_troubleshoot-no-permissions "#security_iam_troubleshoot-no-permissions")

## I'm not authorized to perform

an action in AWS WA Tool

If the AWS Management Console tells you that you're not authorized to perform an action, then you
must contact your administrator for assistance. Your administrator is the person that
provided you with your sign-in credentials.

The following example error occurs when the
`mateojackson` user tries to use the console to perform the
`DeleteWorkload` action, but does not have permissions.

```
User: arn:aws:iam::`123456789012`:user/`mateojackson` is not authorized to perform: `wellarchitected:DeleteWorkload` on resource: `11112222333344445555666677778888`
```

For this example, ask your administrator to update your policies to allow you to
access the `11112222333344445555666677778888` resource using the
`wellarchitected:DeleteWorkload` action.
