

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Troubleshoot identity and access issues
<a name="troubleshoot-iam"></a>

This section helps administrators troubleshoot identity and access issues with AWS Wickr. If the steps in this section don't resolve your issue, open a case in the [AWS Support Center](https://console.aws.amazon.com/support/home).

**Topics**
+ [Before you begin](#troubleshoot-iam-before)
+ [Common identity and access issues](#troubleshoot-iam-common)

## Before you begin
<a name="troubleshoot-iam-before"></a>

Verify the following before troubleshooting:
+ You have administrator access to the AWS account that contains your Wickr network.
+ You have access to the IAM console or permission to view IAM policies.
+ You know which IAM user or role is experiencing the access issue.

## Common identity and access issues
<a name="troubleshoot-iam-common"></a>

### I am not authorized to perform an action in the AWS Management Console for Wickr
<a name="troubleshoot-iam-no-permissions"></a>

If the AWS Management Console for Wickr tells you that you're not authorized to perform an action, then you must contact your administrator for assistance. Your administrator is the person that provided you with your sign-in credentials.

The following example error occurs when the `mateojackson` IAM user tries to use the AWS Management Console for Wickr to create, manage, or view Wickr networks but does not have the `wickr:CreateAdminSession` and `wickr:ListNetworks` permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: wickr:ListNetworks
```

In this case, Mateo asks his administrator to update his policies to allow him to access the AWS Management Console for Wickr using the `wickr:CreateAdminSession` and `wickr:ListNetworks` actions. For more information, see [Identity-based policy examples for AWS Wickr](security_iam_id-based-policy-examples.md) and [AWS managed policy: AWSWickrFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSWickrFullAccess).