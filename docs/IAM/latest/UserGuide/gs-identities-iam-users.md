# Use cases for IAM users

IAM users that you create in your AWS account have long-term credentials that you
manage directly.

When it comes to managing access in AWS, IAM users are generally not the best choice.
There are a few key reasons why you should avoid relying on IAM users for most of your use
cases.

First, IAM users are designed for individual accounts, so they don't scale well as your
organization grows. Managing permissions and security for a large number of IAM users can
quickly become a challenge.

IAM users also lack the centralized visibility and auditing capabilities that you get
with other AWS identity management solutions. This can make it more challenging to
maintain security and regulatory compliance.

Finally, implementing security best practices like multi-factor authentication, password
policies, and role separation is much easier with more scalable identity management
approaches.

Instead of relying on IAM users, we recommend using more robust solutions like IAM Identity Center with AWS Organizations, or federated identities from external providers. These options will give you
better control, security, and operational efficiency as your AWS environment grows.

As a result, we recommend that you only use IAM users for [use cases not supported by
federated users](id.md#id_which-to-choose "id.md#id_which-to-choose").

The following list identifies the specific use cases that require long-term credentials
with IAM users in AWS. You can use IAM to create these IAM users under the
umbrella of your AWS account, and use IAM to manage their permissions.

- Emergency access to your AWS account
- Workloads that can't use IAM roles
  - AWS CodeCommit access
  - Amazon Keyspaces (for Apache Cassandra) access

- Third-party AWS clients
- AWS IAM Identity Center isn't available for your account and you have no other identity
  provider
