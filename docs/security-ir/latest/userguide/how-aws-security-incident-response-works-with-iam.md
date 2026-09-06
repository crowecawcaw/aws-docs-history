

# How AWS Security Incident Response Works with IAM
<a name="how-aws-security-incident-response-works-with-iam"></a>

 AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources. IAM administrators control who can be *authenticated* (signed in) and *authorized* (have permissions) to use AWS Security Incident Response resources. IAM is an AWS service that you can use with no additional charge. 


|  IAM features that you can use with AWS Security Incident Response  |   | 
| --- | --- | 
| *IAM feature* | *Service alignment* | 
| Identity-based policies | Yes | 
| Resource-based policies | No | 
| Policy actions | Yes | 
| Policy resources | Yes | 
| Policy conditions keys | Yes (global) | 
| ACLs | No | 
| ABAC (tags in policies) | Yes | 
| Temporary credentials | Yes | 
| Forward access sessions (FAS) | Yes | 
| Service roles | No | 
| Service-linked roles | Yes | 

**Topics**
+ [Identity-based policies for AWS Security Incident Response](identity-based-policies.md)
+ [Policy condition keys for AWS Security Incident Response](policy-condition-keys-for-aws-security-incident-response.md)
+ [Access control lists (ACLs) in AWS Security Incident Response](access-control-lists-acls-in-aws-security-incident-response.md)