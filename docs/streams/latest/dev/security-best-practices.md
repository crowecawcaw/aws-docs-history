# Security best practices for Kinesis Data Streams

Amazon Kinesis Data Streams provides a number of security features to consider as you develop and implement your own security policies.
The following best practices are general guidelines and don’t represent a complete security solution. Because these best
practices might not be appropriate or sufficient for your environment, treat them as helpful considerations rather than
prescriptions.

## Implement least privilege access

When granting permissions, you decide who is getting what permissions to which Kinesis Data Streams resources. You enable
specific actions that you want to allow on those resources. Therefore you should grant only the permissions that are
required to perform a task. Implementing least privilege access is fundamental in reducing security risk and the impact
that could result from errors or malicious intent.

## Use IAM roles

Producer and client applications must have valid credentials to access
Kinesis data streams. You should not store AWS credentials directly in a client application or in an Amazon S3 bucket.
These are long-term credentials that are not automatically rotated and could have a significant business impact if they are compromised.

Instead, you should use an IAM role to manage temporary credentials for your producer and client applications to access Kinesis data streams. When you
use a role, you don't have to use long-term credentials (such as a user name and password or access keys) to access other resources.

For more information, see the following topics in the _IAM User Guide_:

- [IAM Roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md")
- [Common Scenarios for Roles: Users, Applications, and Services](../../../IAM/latest/UserGuide/id_roles_common-scenarios.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios.md")

## Implement server-side encryption in dependent

resources

Data at rest and data in transit can be encrypted in Kinesis Data Streams. For more information, see [Data protection in Amazon Kinesis Data Streams](server-side-encryption.md "server-side-encryption.md").

## Use CloudTrail to monitor API calls

Kinesis Data Streams is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Kinesis Data Streams.

Using the information collected by CloudTrail, you can determine the request that was made to Kinesis Data Streams, the IP address from which the request was made, who made the request, when it was made, and additional details.

For more information, see [Log Amazon Kinesis Data Streams API calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").
