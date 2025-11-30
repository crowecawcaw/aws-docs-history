# IAM-based domains and projects

IAM-based domains in Amazon SageMaker Unified Studio provide another configuration option to setup and manage
your data and AI development environment. IAM-based domains automate creation of a Amazon SageMaker Unified Studio
domain using AWS Identity and Access Management (IAM) roles, and also use IAM roles to
access data and resources for a project within an IAM-based domain.

###### Note

A project in Amazon SageMaker Unified Studio is a boundary within a domain where you can collaborate with
other users to work on a business use case. In projects, you can create and share data and
resources. For more details, see [Projects](../userguide/projects.md "../userguide/projects.md").

By default, Amazon SageMaker Unified Studio will create a domain configured with an AWS IAM role. You can use
an existing IAM role or choose to create a new IAM role for the domain setup. Projects within
this IAM-based domain also use an IAM role to access data and infrastructure within Amazon SageMaker Unified Studio.
In addition, each project is assigned an IAM role for login, this federated IAM role is used
to authenticate and access the assigned IAM project. Only one IAM-based domain is available
per AWS Account per region. Each IAM-based domain supports multiple projects, and each
project can be assigned to only one IAM-role for authentication and execution.

Amazon SageMaker Unified Studio also supports domains configured with AWS IAM Identity Center (IdC). Projects
within this Identity Center-based domain use the project role to access data and resources, or
Identity-based data authorization using AWS IAM Trusted Identity Propagation. End users
login using their identity provided directly by Identity Center or through SSO to an identity
provider. Additional details to setup an Identity Center based domain are available in [Identity Center-based domains](identity-center-based-domains.md "identity-center-based-domains.md").

###### Topics

- [Overview of IAM-based domains](iam-based-domains-overview.md "iam-based-domains-overview.md")
- [Set up IAM-based domains in Amazon SageMaker Unified Studio](setup-iam-based-domains.md "setup-iam-based-domains.md")
- [Manage data encryption in
  IAM-based domains](manage-data-encryption-iam-based-domains.md "manage-data-encryption-iam-based-domains.md")
- [Access the Domain Administration
  Page](access-domain-administration-page.md "access-domain-administration-page.md")
- [Configure VPC Networking for
  Amazon SageMaker Unified Studio Domain](vpc-networking-iam-based-domains.md "vpc-networking-iam-based-domains.md")
- [Manage Projects from Domain
  Administration](manage-projects-domain-administration.md "manage-projects-domain-administration.md")
- [Configure Domain Settings](configure-domain-settings-iam-based.md "configure-domain-settings-iam-based.md")
- [Projects in IAM-based domains](projects-iam-based-domains.md "projects-iam-based-domains.md")
