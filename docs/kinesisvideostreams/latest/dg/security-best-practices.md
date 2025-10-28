# Security best practices for Kinesis Video Streams

Amazon Kinesis Video Streams provides a number of security features to consider as you develop and implement your own security policies.
The following best practices are general guidelines and don’t represent a complete security solution. Because these best
practices might not be appropriate or sufficient for your environment, treat them as helpful considerations rather than
prescriptions.

For security best practices for your remote devices, see
[Security Best Practices for Device Agents](../../../iot/latest/developerguide/device-defender-DetectMetricsMessagesBestPract.md "../../../iot/latest/developerguide/device-defender-DetectMetricsMessagesBestPract.md").

## Implement least privilege access

When granting permissions, you decide who is getting what permissions to which Kinesis Video Streams resources. You enable
specific actions that you want to allow on those resources. Therefore you should grant only the permissions that are
required to perform a task. Implementing least privilege access is fundamental in reducing security risk and the impact
that could result from errors or malicious intent.

For example, a producer that sends data to Kinesis Video Streams requires only `PutMedia`, `GetStreamingEndpoint`, and `DescribeStream`.
Do not grant producer applications permissions for all actions (`*`), or for other actions such as `GetMedia`.

For more information, see [What Is Least Privilege & Why Do You Need It?](https://www.beyondtrust.com/blog/entry/what-is-least-privilege "https://www.beyondtrust.com/blog/entry/what-is-least-privilege")

## Use IAM roles

Producer and client applications must have valid credentials to access Kinesis Video Streams. You should not store AWS
credentials directly in a client application or in an Amazon S3 bucket. These are long-term credentials that aren't
automatically rotated and could have a significant business impact if they are compromised.

Instead, you should use an IAM role to manage temporary credentials for your producer and client
applications to access Kinesis Video Streams. When you use a role, you don't have to use long-term credentials (such as a
username and password or access keys) to access other resources.

For more information, see the following topics in the _IAM User Guide_:

- [IAM Roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md")
- [Common Scenarios for Roles: Users, Applications, and Services](../../../IAM/latest/UserGuide/id_roles_common-scenarios.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios.md")

## Use CloudTrail to monitor API calls

Kinesis Video Streams works with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an
AWS service in Kinesis Video Streams.

You can use the information collected by CloudTrail to determine the request that was made to Kinesis Video Streams, the IP
address from which the request was made, who made the request, when it was made, and additional details.

For more information, see [Log Amazon Kinesis Video Streams API calls with AWS CloudTrail](monitoring-cloudtrail.md "monitoring-cloudtrail.md").
