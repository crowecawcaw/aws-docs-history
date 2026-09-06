

# Security Best Practices for Amazon DataZone
<a name="security-best-practices"></a>

Amazon DataZone provides a number of security features to consider as you develop and implement your own security policies. The following best practices are general guidelines and don’t represent a complete security solution. Because these best practices might not be appropriate or sufficient for your environment, treat them as helpful considerations rather than prescriptions. 

## Implement least privilege access
<a name="security-best-practices-privileges"></a>

When granting permissions, you decide who is getting what permissions to which Amazon DataZone resources. You enable specific actions that you want to allow on those resources. Therefore you should grant only the permissions that are required to perform a task. Implementing least privilege access is fundamental in reducing security risk and the impact that could result from errors or malicious intent. 

For more information, see [AWS managed policies for Amazon DataZone](security-iam-awsmanpol.md) and [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html). 

## Use IAM roles
<a name="security-best-practices-roles"></a>

Producer and client applications must have valid credentials to access Amazon DataZone resources. You should not store AWS credentials directly in a client application or in an Amazon S3 bucket. These are long-term credentials that are not automatically rotated and could have a significant business impact if they are compromised. 

Instead, you should use an IAM role to manage temporary credentials for your producer and client applications to access Amazon DataZone resources. When you use a role, you don't have to use long-term credentials (such as a user name and password or access keys) to access other resources.

For more information, see the following topics in the *IAM User Guide*:
+ [IAM Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
+ [Common Scenarios for Roles: Users, Applications, and Services](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios.html)

## Implement Server-Side Encryption in Dependent Resources
<a name="security-best-practices-sse"></a>

Data at rest and data in transit can be encrypted in Amazon DataZone. 

## Use CloudTrail to Monitor API Calls
<a name="security-best-practices-cloudtrail"></a>

Amazon DataZone is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Amazon DataZone.

Using the information collected by CloudTrail, you can determine the request that was made to Amazon DataZone, the IP address from which the request was made, who made the request, when it was made, and additional details.

## Using RAM in Amazon DataZone
<a name="security-best-practices-ram"></a>

Associating your AWS accounts with Amazon DataZone domains enables domain users to publish and consume data from these AWS accounts. Amazon DataZone uses AWS Resource Access Manager (RAM) to manage cross-account access. For more information, see [Associated accounts in Amazon DataZone](working-with-associated-accounts.md) and [Security in AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/security.html).