# Security Best Practices for Amazon DataZone

Amazon DataZone provides a number of security features to consider as you develop and implement
your own security policies. The following best practices are general guidelines and don’t
represent a complete security solution. Because these best practices might not be
appropriate or sufficient for your environment, treat them as helpful considerations rather
than prescriptions.

## Implement least privilege

access

When granting permissions, you decide who is getting what permissions to which
Amazon DataZone resources. You enable specific actions that you want to allow on those
resources. Therefore you should grant only the permissions that are required to perform
a task. Implementing least privilege access is fundamental in reducing security risk and
the impact that could result from errors or malicious intent.

For more information, see [AWS managed policies for Amazon DataZone](security-iam-awsmanpol.md "security-iam-awsmanpol.md") and [Service control policies (SCPs)](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md").

## Use IAM roles

Producer and client applications must have valid credentials to access Amazon DataZone
resources. You should not store AWS credentials directly in a client application or in
an Amazon S3 bucket. These are long-term credentials that are not automatically rotated and
could have a significant business impact if they are compromised.

Instead, you should use an IAM role to manage temporary credentials for your
producer and client applications to access Amazon DataZone resources. When you use a role,
you don't have to use long-term credentials (such as a user name and password or access
keys) to access other resources.

For more information, see the following topics in the _IAM User
Guide_:

- [IAM
  Roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md")
- [Common Scenarios
  for Roles: Users, Applications, and Services](../../../IAM/latest/UserGuide/id_roles_common-scenarios.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios.md")

## Implement Server-Side Encryption in

Dependent Resources

Data at rest and data in transit can be encrypted in Amazon DataZone.

## Use CloudTrail to Monitor API

Calls

Amazon DataZone is integrated with AWS CloudTrail, a service that provides a record of actions
taken by a user, role, or an AWS service in Amazon DataZone.

Using the information collected by CloudTrail, you can determine the request that was made
to Amazon DataZone, the IP address from which the request was made, who made the request,
when it was made, and additional details.

## Using RAM in Amazon DataZone

Associating your AWS accounts with Amazon DataZone domains enables domain users to
publish and consume data from these AWS accounts. Amazon DataZone uses AWS Resource
Access Manager (RAM) to manage cross-account access. For more information, see [Associated accounts in Amazon DataZone](working-with-associated-accounts.md "working-with-associated-accounts.md")
and [Security in
AWS RAM](../../../ram/latest/userguide/security.md "../../../ram/latest/userguide/security.md").
