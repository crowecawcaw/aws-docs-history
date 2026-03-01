# Troubleshooting notification issues

You can use the information on this page to resolve common notification issues in
Audit Manager.

###### Topics

- [I specified an Amazon SNS topic in Audit Manager, but I'm not receiving any notifications](#missing-notifications "#missing-notifications")
- [I specified a FIFO topic, but I'm not receiving notifications in the expected order](#wrong-order-notifications "#wrong-order-notifications")

## I specified an Amazon SNS topic in Audit Manager, but I'm not receiving any notifications

If your Amazon SNS topic uses AWS KMS for server-side encryption (SSE), you might be
missing the required permissions for your AWS KMS key policy. You might also fail to
receive notifications if you didn't subscribe an endpoint to your topic.

If you aren't receiving notifications, make sure that you did the
following:

- You attached the required permissions policy to your KMS key. For an
  example policy that you can use, see [Example 2 (Permissions for the KMS key that's attached to the SNS topic)](security_iam_id-based-policy-examples.md#sns-key-permissions "security_iam_id-based-policy-examples.md#sns-key-permissions").
- You subscribed an endpoint to the topic that the notifications are sent
  through. When you subscribe an email endpoint to a topic, you receive an
  email asking you to confirm your subscription. You must confirm your
  subscription to start receiving email notifications. For more information,
  see [Getting Started](../../../sns/latest/dg/sns-getting-started.md "../../../sns/latest/dg/sns-getting-started.md") in the Amazon SNS Developer Guide.

## I specified a FIFO topic, but I'm not receiving notifications in the expected order

Audit Manager supports sending notifications to FIFO SNS topics. However, the order in
which Audit Manager sends notifications to your FIFO topics isn't guaranteed.
