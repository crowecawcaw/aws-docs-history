

# Temporary elevated access for AWS accounts
<a name="temporary-elevated-access"></a>

All access to your AWS account involves some level of privilege. Sensitive operations, such as changing the configuration for a production environment, require special treatment due to scope and potential impact. Temporary elevated access (also known as just-in-time access) is a way to request, approve, and track the use of a permission to perform a specific task during a specified time. Temporary elevated access supplements other forms of access control, such as permission sets and multi-factor authentication.

**Note**  
To ensure business continuity, we recommend that you [set up emergency access to the AWS Management Console](https://docs.aws.amazon.com/singlesignon/latest/userguide/emergency-access.html).

To address a range of customers' needs, AWS IAM Identity Center integrates with the solutions from AWS Security Competency partners. AWS validates that these solutions address a common set of temporary elevated access requirements. We recommend that you review each partner solution carefully so that you can choose one that best fits your unique needs and preferences, including your business, the architecture of your cloud environment, and your budget.

Validated solutions include [Apono Access Management Platform](https://www.apono.io/), [CyberArk Secure Cloud Access](https://www.cyberark.com/products/secure-cloud-access/), [Okta Access Requests](https://help.okta.com/en-us/Content/Topics/identity-governance/access-requests/ar-overview.htm), and [Tenable](https://ermetic.com/solution/just-in-time/) (previously Ermetic).

Partners can nominate solutions using the AWS Security Competency application in Partner Center. For more information, see [AWS Security Competency Partners](https://aws.amazon.com/security/partner-solutions/).

**Note**  
If you are using resource-based, Amazon Elastic Kubernetes Service or AWS Key Management Service, see [Referencing permission sets in resource policies, Amazon EKS Cluster config maps, and AWS KMS key policies](https://docs.aws.amazon.com/singlesignon/latest/userguide/referencingpermissionsets.html) before you choose your just-in-time solution.