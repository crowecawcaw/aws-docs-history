This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Troubleshooting AWS Wickr identity and

access

Use the following information to help you diagnose and fix common issues that you might
encounter when working with Wickr and IAM.

###### Topics

- [I am not authorized to
  perform an administrative action in the AWS Management Console for Wickr](#security_iam_troubleshoot-no-permissions "#security_iam_troubleshoot-no-permissions")

## I am not authorized to

perform an administrative action in the AWS Management Console for Wickr

If the AWS Management Console for Wickr tells you that you're not authorized to perform an action,
then you must contact your administrator for assistance. Your administrator is the
person that provided you with your sign-in credentials.

The following example error occurs when the `mateojackson` IAM user
tries to use the AWS Management Console for Wickr to create, manage, or view Wickr networks in the
AWS Management Console for Wickr but does not have the `wickr:CreateAdminSession`
and `wickr:ListNetworks` permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: wickr:ListNetworks
```

In this case, Mateo asks his administrator to update his policies to allow him to
access the AWS Management Console for Wickr using the `wickr:CreateAdminSession`
and `wickr:ListNetworks` actions. For more information, see [Identity-based policy examples for
AWS Wickr](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md") and [AWS managed policy:
AWSWickrFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSWickrFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSWickrFullAccess").
