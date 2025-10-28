# Diagnosing common errors in the console with

Amazon Q Developer

In the AWS Management Console, Amazon Q Developer diagnoses common errors you encounter while working with AWS
services, such as insufficient permissions, incorrect configuration, and exceeding service
limits. Amazon Q troubleshoots errors you receive while using the following services in the
AWS console:

- Amazon Elastic Compute Cloud (Amazon EC2)
- Amazon Elastic Container Service (Amazon ECS)
- Amazon Simple Storage Service (Amazon S3)
- AWS Lambda
- AWS Step Functions
  In addition, Amazon Q troubleshoots IAM permission errors across all AWS console pages
  and a limited number of service-specific errors for some AWS services. Amazon Q doesn't
  maintain a history of previous error diagnosing sessions.

If you're unable to diagnose your error with Amazon Q, you can use Amazon Q to create a
support case with Support. For more information, see [Using Amazon Q Developer to chat with Support](support-chat.md "support-chat.md"). If you have an issue specific to the Amazon Q error diagnosing
feature, you can use the thumbs-down icon to report an issue.

## Add permissions

For an IAM policy that grants permissions needed for diagnosing console errors, see
[Allow users to diagnose
console errors with Amazon Q](id-based-policy-examples-users.md#id-based-policy-examples-allow-error-diagnosing "id-based-policy-examples-users.md#id-based-policy-examples-allow-error-diagnosing").

## Diagnose common errors in the

console

To use Amazon Q to diagnose an error in the AWS Management Console, use the following
procedure.

1. If you receive an error that Amazon Q can help you with, a
   **Diagnose with Amazon Q** button appears in the error
   message. If you want to use Amazon Q to diagnose the error,
   choose **Diagnose with Amazon Q** to proceed.
2. A window appears where Amazon Q first provides information about the error. It
   then provides a series of steps you can take to resolve the error. It can take
   several seconds for Amazon Q to generate instructions.
3. To provide feedback, you can use the thumbs-up and thumbs-down icons. To
   provide detailed feedback, choose the **Tell me more** button
   that appears after you select an icon.
