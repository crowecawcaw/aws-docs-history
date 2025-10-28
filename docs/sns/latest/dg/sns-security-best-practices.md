# Amazon SNS security best practices

AWS provides many security features for Amazon SNS. Review these security features in the
context of your own security policy.

###### Note

The guidance for these security features applies to common use cases and implementations.
We recommend that you review these best practices in the context of your specific use case,
architecture, and threat model.

## Preventative best practices

The following are preventative security best practices for Amazon SNS.

###### Topics

- [Ensure topics aren't publicly
  accessible](#ensure-topics-not-publicly-accessible "#ensure-topics-not-publicly-accessible")
- [Implement least-privilege access](#implement-least-privilege-access "#implement-least-privilege-access")
- [Use IAM
  roles for applications and AWS services which require Amazon SNS access](#use-iam-roles-for-applications-aws-services-which-require-access "#use-iam-roles-for-applications-aws-services-which-require-access")
- [Implement server-side encryption](#implement-server-side-encryption "#implement-server-side-encryption")
- [Enforce encryption of data in
  transit](#enforce-encryption-data-in-transit "#enforce-encryption-data-in-transit")
- [Consider using VPC endpoints to
  access Amazon SNS](#consider-using-vpc-endpoints-access-sns "#consider-using-vpc-endpoints-access-sns")
- [Ensure subscriptions are not configured to
  deliver to raw http endpoints](#http-subscription-configuration "#http-subscription-configuration")
- [Enforce authentication on unsubscribe](#enforce-authentication-on-unsubscribe "#enforce-authentication-on-unsubscribe")

### Ensure topics aren't publicly

accessible

Unless you explicitly require anyone on the internet to be able to read or write to your
Amazon SNS topic, you should ensure that your topic isn't publicly accessible (accessible by
everyone in the world or by any authenticated AWS user).

- Avoid creating policies with `Principal` set to `""`.
- Avoid using a wildcard (`*`). Instead, name a specific user or
  users.

### Implement least-privilege access

When you grant permissions, you decide who receives them, which topics the permissions
are for, and specific API actions that you want to allow for these topics. Implementing the
principle of least privilege is important to reducing security risks. It also helps to
reduce the negative effect of errors or malicious intent.

Follow the standard security advice of granting least privilege. That is, grant only the
permissions required to perform a specific task. You can implement least privilege by using
a combination of security policies pertaining to user access.

Amazon SNS uses the publisher-subscriber model, requiring three types of user account
access:

- **Administrators** – Access to creating,
  modifying, and deleting topics. Administrators also control topic policies.
- **Publishers** – Access to sending messages to
  topics.
- **Subscribers** – Access to subscribing to
  topics.

For more information, see the following sections:

- [Identity and access management in Amazon SNS](security-iam.md "security-iam.md")
- [Amazon SNS API permissions:
  Actions and resources reference](sns-access-policy-language-api-permissions-reference.md "sns-access-policy-language-api-permissions-reference.md")

### Use IAM

roles for applications and AWS services which require Amazon SNS access

For applications or AWS services, such as Amazon EC2, to access Amazon SNS topics, they must use
valid AWS credentials in their AWS API requests. Because these credentials aren't
rotated automatically, you shouldn't store AWS credentials directly in the application or
EC2 instance.

You should use an IAM role to manage temporary credentials for applications or
services that need to access Amazon SNS. When you use a role, you don't need to distribute
long-term credentials (such as a username, password, and access keys) to an EC2 instance or
AWS service, such as AWS Lambda. Instead, the role supplies temporary permissions that
applications can use when they make calls to other AWS resources.

For more information, see [IAM Roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md")
and [Common Scenarios for Roles:
Users, Applications, and Services](../../../IAM/latest/UserGuide/id_roles_common-scenarios.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios.md") in the
_IAM User Guide_.

### Implement server-side encryption

To mitigate data leakage issues, use encryption at rest to encrypt your messages using a
key stored in a different location from the location that stores your messages. Server-side
encryption (SSE) provides data encryption at rest. Amazon SNS encrypts your data at the message
level when it stores it, and decrypts the messages for you when you access them. SSE uses
keys managed in AWS Key Management Service. When you authenticate your request and have access permissions,
there is no difference between accessing encrypted and unencrypted topics.

For more information, see [Securing Amazon SNS data with server-side
encryption](sns-server-side-encryption.md "sns-server-side-encryption.md") and [Managing Amazon SNS encryption keys and costs](sns-key-management.md "sns-key-management.md").

### Enforce encryption of data in

transit

It's possible, but not recommended, to publish messages that are not encrypted during
transit by using HTTP. However, when a topic is encrypted at rest using AWS KMS, it is
required to use HTTPS for publishing messages to ensure encryption both at rest and in
transit. While the topic does not automatically reject HTTP messages, using HTTPS is
necessary to maintain the security standards.

AWS recommends that you use HTTPS instead of HTTP. When you use HTTPS, messages are
automatically encrypted during transit, even if the SNS topic itself isn't encrypted.
Without HTTPS, a network-based attacker can eavesdrop on network traffic or manipulate it
using an attack such as man-in-the-middle.

To enforce only encrypted connections over HTTPS, add the [`aws:SecureTransport`](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_Boolean "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_Boolean") condition in the IAM policy that's attached
to unencrypted SNS topics. This forces message publishers to use HTTPS instead of HTTP. You
can use the following example policy as a guide:

JSON

```
`{
 "Id": "ExamplePolicy",
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowPublishThroughSSLOnly",
 "Action": "SNS:Publish",
 "Effect": "Deny",
 "Resource": [
 "arn:aws:sns:us-east-1:`111122223333`:test-topic"
 ],
 "Condition": {
 "Bool": {
 "aws:SecureTransport": "false"
 }
 },
 "Principal": "*"
 }
 ]
}`

```

### Consider using VPC endpoints to

access Amazon SNS

If you have topics that you must be able to interact with, but these topics must
absolutely not be exposed to the internet, use VPC endpoints to limit topic access to only
the hosts within a particular VPC. You can use topic policies to control access to topics
from specific Amazon VPC endpoints or from specific VPCs.

Amazon SNS VPC endpoints provide two ways to control access to your messages:

- You can control the requests, users, or groups that are allowed through a specific
  VPC endpoint.
- You can control which VPCs or VPC endpoints have access to your topic using a topic
  policy.

For more information, see [Creating the endpoint](sns-vpc-create-endpoint.md#sns-vpc-endpoint-create "sns-vpc-create-endpoint.md#sns-vpc-endpoint-create") and [Creating an Amazon VPC endpoint policy for Amazon SNS](sns-vpc-endpoint-policy.md "sns-vpc-endpoint-policy.md").

### Ensure subscriptions are not configured to

deliver to raw http endpoints

Avoid configuring subscriptions to deliver to a raw http endpoints. Always have
subscriptions delivering to an endpoint domain name. For example, a subscription configured
to deliver to an endpoint, `http://1.2.3.4/my-path`, should be changed to
`http://my.domain.name/my-path`.

### Enforce authentication on unsubscribe

Unless you are required to allow unauthenticated unsubscribe,
like in cases of easy unsubscribe for email or SMS,
you must enforce authentication for unsubscribing from a topic.
This is in alignment with the
[least-privilege access control recommendation](#implement-least-privilege-access "#implement-least-privilege-access") .

You can set `AuthenticateOnUnsubscribe` to `True` while confirming a subscription.
Failing to set the `AuthenticateOnUnsubscribe` flag to `True`
when confirming a Amazon SNS subscription, can cause unsubscribe requests to succeed,
even if they are unauthenticated. For more information, see Amazon SNS API reference for
[ConfirmSubscription](../api/API_ConfirmSubscription.md "../api/API_ConfirmSubscription.md"), or the
[Python example in the Amazon Q Detector Library](../../../codeguru/detector-library/python/sns-unauthenticated-unsubscribe.md "../../../codeguru/detector-library/python/sns-unauthenticated-unsubscribe.md").

For example, to confirm an email subscription using AWS CLI,
copy the link from “Confirm Subscription” text in the email notification.
That URL will give you required information to call the below AWS CLI command.

```
aws sns confirm-subscription --region us-west-2 \
    --topic-arn sns-topic-arn \
    --token token-from-subscribe-notification \
    --authenticate-on-unsubscribe true

```

Where:

- aws-region is the AWS Region that the topic is located in.
  This is also available in the topic ARN.
- sns-topic-arn is the ARN of the topic. This is the text after “TopicArn=”
  and before “&Token” in the confirm subscription URL.
- token-from-subscribe-notification is the UUID string after “Token=”
  and before “&Endpoint” in the confirm subscription URL.

The following is an example URL:

```

        https://sns.us-west-2.amazonaws.com/confirmation.html?TopicArn=arn:aws:sns:us-west-2:123456789012:sns-topic&Token=a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1&Endpoint=email@address.com

```
