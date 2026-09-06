

# Troubleshooting AWS Elemental MediaTailor identity and access
<a name="security_iam_troubleshoot"></a>

Use the following information to help you diagnose and fix common issues that you might encounter when working with MediaTailor and IAM.

**Topics**
+ [I am not authorized to perform an action in MediaTailor](#security_iam_troubleshoot-no-permissions)
+ [I am not authorized to perform iam:PassRole](#security_iam_troubleshoot-passrole)
+ [I want to allow people outside of my AWS account to access my MediaTailor resources](#security_iam_troubleshoot-cross-account-access)
+ [MediaTailor cannot access my Amazon S3 bucket](#security_iam_troubleshoot-s3-access)

## I am not authorized to perform an action in MediaTailor
<a name="security_iam_troubleshoot-no-permissions"></a>

If you receive an error that you're not authorized to perform an action, your policies must be updated to allow you to perform the action.

The following example error occurs when the `mateojackson` IAM user tries to use the console to view details about a fictional `{{my-example-widget}}` resource but doesn't have the fictional `mediatailor:{{GetWidget}}` permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: mediatailor:{{GetWidget}} on resource: {{my-example-widget}}
```

In this case, the policy for the `mateojackson` user must be updated to allow access to the `{{my-example-widget}}` resource by using the `mediatailor:{{GetWidget}}` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

## I am not authorized to perform iam:PassRole
<a name="security_iam_troubleshoot-passrole"></a>

If you receive an error that you're not authorized to perform the `iam:PassRole` action, your policies must be updated to allow you to pass a role to MediaTailor.

Some AWS services allow you to pass an existing role to that service instead of creating a new service role or service-linked role. To do this, you must have permissions to pass the role to the service.

The following example error occurs when an IAM user named `marymajor` tries to use the console to perform an action in MediaTailor. However, the action requires the service to have permissions that are granted by a service role. Mary does not have permissions to pass the role to the service.

```
User: arn:aws:iam::123456789012:user/marymajor is not authorized to perform: iam:PassRole
```

In this case, Mary's policies must be updated to allow her to perform the `iam:PassRole` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

## I want to allow people outside of my AWS account to access my MediaTailor resources
<a name="security_iam_troubleshoot-cross-account-access"></a>

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant people access to your resources.

To learn more, consult the following:
+ To learn whether MediaTailor supports these features, see [How AWS Elemental MediaTailor works with IAM](security_iam_service-with-iam.md).
+ To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you own](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html) in the *IAM User Guide*.
+ To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html) in the *IAM User Guide*.
+ To learn how to provide access through identity federation, see [Providing access to externally authenticated users (identity federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html) in the *IAM User Guide*.
+ To learn the difference between using roles and resource-based policies for cross-account access, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*.

## MediaTailor cannot access my Amazon S3 bucket
<a name="security_iam_troubleshoot-s3-access"></a>

If MediaTailor returns errors when trying to access content from your Amazon S3 bucket, check the following common causes:

### Amazon S3 permissions issues
<a name="security_iam_troubleshoot-s3-permissions"></a>

**Error symptoms:**
+ `502 BadGatewayException` with Amazon S3 related messages
+ `403 Forbidden` errors in MediaTailor logs
+ Content fails to load from Amazon S3 origin

**Resolution:**

1. Verify your MediaTailor service role has the required Amazon S3 permissions:

1. Check your Amazon S3 bucket policy allows MediaTailor access:

### HTTPS access issues
<a name="security_iam_troubleshoot-s3-https"></a>

**Error symptoms:**
+ SSL/TLS handshake failures
+ `502 Bad Gateway` when accessing HTTPS Amazon S3 URLs

**Resolution:**

1. Ensure your Amazon S3 bucket policy requires HTTPS:

1. Verify MediaTailor configuration uses HTTPS URLs for Amazon S3 content.

### Cross-account Amazon S3 access
<a name="security_iam_troubleshoot-s3-cross-account"></a>

**Error symptoms:**
+ `Access Denied` errors when Amazon S3 bucket is in different account
+ MediaTailor cannot assume cross-account roles

**Resolution:**

1. Update the Amazon S3 bucket policy in the content account to trust MediaTailor's service role

1. Add cross-account permissions to MediaTailor's service role

1. Ensure both accounts have proper trust relationships configured