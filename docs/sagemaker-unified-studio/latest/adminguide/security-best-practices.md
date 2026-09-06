

# Security Best Practices for Amazon SageMaker Unified Studio
<a name="security-best-practices"></a>

Amazon SageMaker Unified Studio provides a number of security features to consider as you develop and implement your own security policies. The following best practices are general guidelines and don’t represent a complete security solution. Because these best practices might not be appropriate or sufficient for your environment, treat them as helpful considerations rather than prescriptions. 

## Implement least privilege access
<a name="security-best-practices-privileges"></a>

When granting permissions, you decide who is getting what permissions to which Amazon SageMaker Unified Studio resources. You enable specific actions that you want to allow on those resources. Therefore you should grant only the permissions that are required to perform a task. Implementing least privilege access is fundamental in reducing security risk and the impact that could result from errors or malicious intent. 

## Use IAM roles
<a name="security-best-practices-roles"></a>

Producer and client applications must have valid credentials to access Amazon SageMaker Unified Studio resources. You should not store AWS credentials directly in a client application or in an Amazon S3 bucket. These are long-term credentials that are not automatically rotated and could have a significant business impact if they are compromised. 

Instead, you should use an IAM role to manage temporary credentials for your producer and client applications to access Amazon SageMaker Unified Studio resources. When you use a role, you don't have to use long-term credentials (such as a user name and password or access keys) to access other resources.

For more information, see the following topics in the *IAM User Guide*:
+ [IAM Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
+ [Common Scenarios for Roles: Users, Applications, and Services](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios.html)

## Implement Server-Side Encryption in Dependent Resources
<a name="security-best-practices-sse"></a>

Data at rest and data in transit can be encrypted in Amazon SageMaker Unified Studio. 

## Use CloudTrail to Monitor API Calls
<a name="security-best-practices-cloudtrail"></a>

Amazon SageMaker Unified Studio is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Amazon SageMaker Unified Studio.

Using the information collected by CloudTrail, you can determine the request that was made to Amazon SageMaker Unified Studio, the IP address from which the request was made, who made the request, when it was made, and additional details.