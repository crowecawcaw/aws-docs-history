# Security best practices for Amazon Kinesis Video Streams with

WebRTC

Amazon Kinesis Video Streams (including its WebRTC capability) provides a number of security features to
consider as you develop and implement your own security policies. The following best practices are
general guidelines and don’t represent a complete security solution. Because these best practices
might not be appropriate or sufficient for your environment, treat them as helpful considerations
rather than prescriptions.

For security best practices for your remote devices, see [Security Best
Practices for Device Agents](../../../iot/latest/developerguide/device-defender-DetectMetricsMessagesBestPract.md "../../../iot/latest/developerguide/device-defender-DetectMetricsMessagesBestPract.md").

## Implement least privilege access

When granting permissions, you decide who is getting what permissions to which Kinesis Video Streams
resources. You enable specific actions that you want to allow on those resources. Therefore you
should grant only the permissions that are required to perform a task. Implementing least
privilege access is fundamental in reducing security risk and the impact that could result from
errors or malicious intent.

For example, a producer that sends data to Kinesis Video Streams requires only `PutMedia`,
`GetStreamingEndpoint`, and `DescribeStream`. Do not grant producer
applications permissions for all actions (`*`), or for other actions such as
`GetMedia`.

For more information, see [Apply least-privilege permissions](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege").

## Use IAM roles

Producer and client applications must have valid credentials to access Kinesis video streams.
You should not store AWS credentials directly in a client application or in an Amazon S3 bucket. These
are long-term credentials that are not automatically rotated and could have a significant
business impact if they are compromised.

Instead, you should use an IAM role to manage temporary credentials for your producer and
client applications to access Kinesis video streams. When you use a role, you don't have to use
long-term credentials to access other
resources.

For more information, see the following topics in the _IAM user
guide_:

- [IAM
  Roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md")
- [Common scenarios for roles: users, applications, and services](../../../IAM/latest/UserGuide/id_roles_common-scenarios.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios.md")

## Use CloudTrail to monitor API calls

Kinesis Video Streams with WebRTC is integrated with AWS CloudTrail, a service that provides a record of actions taken
by a user, role, or an AWS service in Kinesis Video Streams with WebRTC.

Using the information collected by CloudTrail, you can determine the request that was made to
Kinesis Video Streams with WebRTC, the IP address from which the request was made, who made the request, when it was
made, and additional details.

For more information, see [Log API calls with AWS CloudTrail](kvswebrtc-monitoring-ct.md "kvswebrtc-monitoring-ct.md").
