# Enabling AWS Resilience Hub to publish to your

Amazon Simple Notification Service topics

This section explains about how to enable AWS Resilience Hub to publish notifications about
the application to your Amazon Simple Notification Service (Amazon SNS) topics. To push notifications to an Amazon SNS
topic, ensure that you have the following:

- An active AWS Resilience Hub application.
- An existing Amazon SNS topic to which AWS Resilience Hub must send notifications. For
  more information about creating an Amazon SNS topic, see [Creating an Amazon SNS topic](../../../sns/latest/dg/sns-create-topic.md "../../../sns/latest/dg/sns-create-topic.md").
  To enable AWS Resilience Hub to publish notifications to your Amazon SNS topic, you must update
  the access policy of the Amazon SNS topic with the following:

###### Note

When you use AWS Resilience Hub to publish messages from opt-in Regions to topics
located in Regions that are enabled by default, you must modify the resource
policy created for the Amazon SNS topic. Change the value of principal from
`resiliencehub.amazonaws.com` to
`resiliencehub.<opt-in-region>.amazonaws.com`.

If you are using a Server Side Encrypted (SSE) Amazon SNS topic, you must ensure that
AWS Resilience Hub has the `Decrypt` and `GenerateDataKey`\* access to
the Amazon SNS encryption key.

To provide `Decrypt` and `GenerateDataKey*` access to
AWS Resilience Hub, you must include the following permissions to AWS Key Management Service access
policy.
