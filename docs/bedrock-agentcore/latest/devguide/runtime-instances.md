# Runtime Instances and capacity providers

The **Instances** compute type runs your agents on AWS managed Amazon EC2 infrastructure in your own AWS account, provisioned through a [capacity provider](runtime-instances-how-it-works.md#runtime-instances-capacity-provider "runtime-instances-how-it-works.md#runtime-instances-capacity-provider"). Because these instances run in your account, the security and encryption model differs from the serverless microVM compute type. The following topics describe that model: the shared responsibility between you and AgentCore, the IAM roles involved, multi-tenant session isolation, and how the EC2 resources are encrypted at rest.

For a broader overview of the Instances compute type and how to use it, see [Instances](runtime-instances-how-it-works.md "runtime-instances-how-it-works.md") and [Get started with Instances](runtime-instances-getting-started.md "runtime-instances-getting-started.md").

###### Topics

- [Security model and permissions for Runtime Instances](runtime-instances-security.md "runtime-instances-security.md")
- [Encryption at rest for Runtime Instances](runtime-instances-encryption.md "runtime-instances-encryption.md")
