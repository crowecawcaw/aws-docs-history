

# Troubleshooting Amazon Textract identity and access

Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon Textract Core and IAM.

**Topics**
+ [I am not authorized to perform an action in Amazon Textract](#security_iam_troubleshoot-no-permissions)
+ [I am not authorized to perform iam:PassRole](#security_iam_troubleshoot-passrole)
+ [I get AccessDeniedException from an Amazon Textract Insights operation](#security_iam_troubleshoot-insights-accessdenied)
+ [My Amazon Textract Insights job can't read the input or write the output](#security_iam_troubleshoot-insights-s3)
+ [AWS KMS denies access when I use a customer managed key](#security_iam_troubleshoot-insights-kms)
+ [I get an access error when I create a resource with tags](#security_iam_troubleshoot-insights-tags)
+ [I want to allow people outside of my AWS account to access my Amazon Textract resources](#security_iam_troubleshoot-cross-account-access)

## I am not authorized to perform an action in Amazon Textract
<a name="security_iam_troubleshoot-no-permissions"></a>

If the AWS Management Console tells you that you're not authorized to perform an action, then you must contact your administrator for assistance. Your administrator is the person that provided you with your username and password.

The following example error occurs when the `mateojackson` IAM user tries to run `DetectDocumentText` on a test image but does not have `textract:DetectDocumentText` permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: textract:DetectDocumentText on resource: textimage.png
```

In this case, Mateo asks their administrator to update their policies to allow access to the `textimage.png` resource using the `textract:DetectDocumentText` action.

## I am not authorized to perform iam:PassRole
<a name="security_iam_troubleshoot-passrole"></a>

If you receive an error that you're not authorized to perform the `iam:PassRole` action, your policies must be updated to allow you to pass a role to Amazon Textract.

Some AWS services allow you to pass an existing role to that service instead of creating a new service role or service-linked role. To do this, you must have permissions to pass the role to the service.

The following example error occurs when an IAM user named `marymajor` tries to use the console to perform an action in Amazon Textract. However, the action requires the service to have permissions that are granted by a service role. Mary does not have permissions to pass the role to the service.

```
User: arn:aws:iam::123456789012:user/marymajor is not authorized to perform: iam:PassRole
```

In this case, Mary's policies must be updated to allow her to perform the `iam:PassRole` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

## I get AccessDeniedException from an Amazon Textract Insights operation
<a name="security_iam_troubleshoot-insights-accessdenied"></a>

Amazon Textract Insights returns `AccessDeniedException` when your policy doesn't allow the action, or when the project, blueprint, or job belongs to another AWS account. Public blueprints owned by AWS are the exception: any account can use them in a project or a job.

If the resource is in your account, confirm that your policy allows the action and that you're calling the AWS Region where the resource was created. For the other errors that Amazon Textract Insights returns, see [Troubleshooting](insights-troubleshooting.md).

## My Amazon Textract Insights job can't read the input or write the output
<a name="security_iam_troubleshoot-insights-s3"></a>

Confirm that the calling identity has `s3:GetObject` on the input and `s3:PutObject` on the output, that both buckets are in the AWS Region you call, and that no bucket policy or service control policy denies access. For the required permissions, see [Prerequisites and setup](insights-prerequisites.md).

Amazon Textract Insights checks access to your input and output when you call `StartDocumentInsights`. It reads the input document and writes an empty `.s3_access_check` object under your output prefix. If either check is denied, `StartDocumentInsights` fails with `AccessDeniedException` and the message "Access Denied. Check S3 URIs and read/write permissions." No job is created. The output bucket must be owned by your account, and a bucket owned by another account fails the same way.

If access changes after the job starts, the job ends with `Status` `FAILED`. Read `ErrorType` and `ErrorMessage` from `GetDocumentInsights`. If the input can't be read, `ErrorType` is `InvalidS3ObjectException` or `AccessDeniedException`. If the output can't be written, `ErrorType` is `InternalServerError`.

## AWS KMS denies access when I use a customer managed key
<a name="security_iam_troubleshoot-insights-kms"></a>

Confirm that the calling identity can use the key in both its IAM policy and the key policy, that the key is in the AWS Region you call, and that your key policy conditions don't pin values that Amazon Textract Insights generates, such as job IDs. For the required AWS KMS permissions, an example key policy, and the encryption context to match, see [Data protection and encryption](insights-data-protection.md).

If the calling identity can't use the key, `StartDocumentInsights` fails with `AccessDeniedException` and the message "Access Denied. Check KMS key permissions." If the key doesn't exist, is disabled, or isn't a symmetric encryption key, it fails with `ValidationException`. No job is created in either case.

## I get an access error when I create a resource with tags
<a name="security_iam_troubleshoot-insights-tags"></a>

When you pass `Tags` to `CreateProject`, `CreateBlueprint`, or `StartDocumentInsights`, you also need `textract:TagResource`. Add that permission, or create the resource without tags. See [Tagging Amazon Textract Insights resources](insights-tagging.md).

## I want to allow people outside of my AWS account to access my Amazon Textract resources
<a name="security_iam_troubleshoot-cross-account-access"></a>

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant people access to your resources.

To learn more, consult the following:
+ To learn whether Amazon Textract supports these features, see [How Amazon Textract works with IAM](security_iam_service-with-iam.md).
+ To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you own](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html) in the *IAM User Guide*.
+ To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html) in the *IAM User Guide*.
+ To learn how to provide access through identity federation, see [Providing access to externally authenticated users (identity federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html) in the *IAM User Guide*.
+ To learn the difference between using roles and resource-based policies for cross-account access, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*.