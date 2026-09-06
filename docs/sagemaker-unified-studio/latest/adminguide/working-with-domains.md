

# Domains in Amazon SageMaker Unified Studio
<a name="working-with-domains"></a>

In Amazon SageMaker Unified Studio, a domain is the organizing entity for connecting together your assets, users, and their projects. With Amazon SageMaker unified domains, you have the flexibility to reflect the data and analytics needs of your organizational structure, whether it's creating a single Amazon SageMaker unified domain for your enterprise or multiple domains for different business units.

Amazon SageMaker Unified Studio supports two distinct domain types to accommodate different organizational needs and authentication approaches:
+ **Identity Center-based domains** - Uses AWS IAM Identity Center for user authentication and management. These domains support single sign-on (SSO) through identity providers and provide centralized user management capabilities. You can create these domains using either quick setup or manual setup options through the Amazon SageMaker management console.
**Note**  
The Amazon SageMaker domain can reside in a different AWS Region than where the IAM Identity Center organization instance is located using IAM Identity Center multi-Region support. To use this feature, your IAM Identity Center instance must be connected to an external identity provider (IdP). For information about setting up IAM Identity Center multi-Region, see [Using IAM Identity Center across multiple AWS Regions](https://docs.aws.amazon.com/singlesignon/latest/userguide/multi-region-iam-identity-center.html).
+ **IAM-based domains** - Uses AWS Identity and Access Management (IAM) roles and AWS IAM Identity Center for authentication and access control. These domains provide an additional path to set up and manage your data and AI development environment using federated IAM roles for the execution IAM role. Only one IAM-based domain is available per AWS Account.

Both domain types provide access to the same core Amazon SageMaker Unified Studio capabilities for data analytics, machine learning, and AI development, but use different authentication mechanisms and setup processes. Choose the domain type that best fits your organization's identity management strategy and security requirements.

**Topics**
+ [Identity Center-based domains](identity-center-based-domains.md)
+ [IAM-based domains and projects](iam-based-domains.md)