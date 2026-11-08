

# Diagnosing console errors with the AWS assistant
<a name="diagnose-errors"></a>

With the AWS assistant, you can diagnose common console errors. Examples include missing permissions, incorrect settings, and exceeded service quotas. It supports errors in the following services:
+ Amazon Elastic Compute Cloud (Amazon EC2)
+ Amazon Elastic Container Service (Amazon ECS)
+ Amazon Simple Storage Service (Amazon S3)
+ AWS Lambda
+ AWS Step Functions

It also diagnoses IAM permission errors on all console pages and some service-specific errors in other services.

This capability is available only in the AWS Management Console. The AWS assistant doesn't keep a history of earlier diagnosis sessions.

## Required permissions
<a name="diagnose-permissions"></a>

Your IAM identity needs permission to diagnose console errors. For an example policy, see [Allow users to diagnose console errors](security-iam-examples.md#iam-example-diagnose).

## Diagnosing a console error
<a name="diagnose-procedure"></a>

**To diagnose a console error**

1. When a supported error occurs, choose **Diagnose with AWS assistant** in the error message.

1. Review the explanation and the steps to fix the error. The steps can take several seconds to appear.

1. To give feedback, choose the thumbs-up or thumbs-down icon. To add details, choose **Tell me more**.

If the diagnosis doesn't fix the problem, you can ask the AWS assistant to create an AWS Support case. To report a problem with the diagnosis itself, choose the thumbs-down icon. For information about support cases, see [Contacting AWS Support with the AWS assistant](support.md).