# Domains in Amazon SageMaker Unified Studio

In Amazon SageMaker Unified Studio, a domain is the organizing entity for connecting together your assets, users,
and their projects. With Amazon SageMaker unified domains, you have the flexibility to reflect
the data and analytics needs of your organizational structure, whether it's creating a single
Amazon SageMaker unified domain for your enterprise or multiple domains for different business
units.

Amazon SageMaker Unified Studio supports two distinct domain types to accommodate different organizational
needs and authentication approaches:

- **Identity Center-based domains** - Use AWS IAM Identity
  Center for user authentication and management. These domains support single sign-on (SSO)
  through identity providers and provide centralized user management capabilities. You can
  create these domains using either quick setup or manual setup options through the Amazon
  SageMaker management console.
- **IAM-based domains** - Use AWS Identity and Access
  Management (IAM) roles for authentication and access control. These domains provide an
  additional path to setup and manage your data and AI development environment using federated
  IAM roles for login and execution. Only one IAM-based domain is available per AWS
  Account.
  Both domain types provide access to the same core Amazon SageMaker Unified Studio capabilities for data analytics,
  machine learning, and AI development, but use different authentication mechanisms and setup
  processes. Choose the domain type that best fits your organization's identity management
  strategy and security requirements.

###### Topics

- [Identity Center-based domains](identity-center-based-domains.md "identity-center-based-domains.md")
- [IAM-based domains and projects](iam-based-domains.md "iam-based-domains.md")
