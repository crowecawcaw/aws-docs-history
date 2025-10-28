# Preventative security best

practices for Amazon Keyspaces

The following security best practices are considered preventative because they can
help you anticipate and prevent security incidents in Amazon Keyspaces.

**Use encryption at rest**

Amazon Keyspaces encrypts at rest all user data that's stored in tables by using
encryption keys stored in [AWS Key Management Service
(AWS KMS)](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/"). This provides an additional layer of data protection by
securing your data from unauthorized access to the underlying
storage.

By default, Amazon Keyspaces uses an AWS owned key for encrypting all of your
tables. If this key doesn’t exist, it's created for you. Service default
keys can't be disabled.

Alternatively, you can use a [customer managed key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") for encryption at rest.
For more information, see [Amazon Keyspaces Encryption at Rest](EncryptionAtRest.md "EncryptionAtRest.md").

**Use IAM roles to authenticate access to Amazon Keyspaces**

For users, applications, and other AWS services to access Amazon Keyspaces, they must
include valid AWS credentials in their AWS API requests. You should not
store AWS credentials directly in the application or EC2 instance. These are
long-term credentials that are not automatically rotated, and therefore
could have significant business impact if they are compromised. An IAM role
enables you to obtain temporary access keys that can be used to access AWS
services and resources.

For more information, see
[IAM Roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md").

**Use IAM policies for Amazon Keyspaces base authorization**

When granting permissions, you decide who is getting them, which Amazon Keyspaces
APIs they are getting permissions for, and the specific actions you want to
allow on those resources. Implementing least privilege is key in reducing
security risks and the impact that can result from errors or malicious
intent.

Attach permissions policies to IAM identities (that is, users, groups, and
roles) and thereby grant permissions to perform operations on Amazon Keyspaces
resources.

You can do this by using the following:

- [AWS managed (predefined) policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies")
- [Customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies")

**Use IAM policy conditions for fine-grained access control**

When you grant permissions in Amazon Keyspaces, you can specify conditions that
determine how a permissions policy takes effect. Implementing least
privilege is key in reducing security risks and the impact that can result
from errors or malicious intent.

You can specify conditions when granting permissions using an IAM policy.
For example, you can do the following:

- Grant permissions to allow users read-only access to specific keyspaces or tables.
- Grant permissions to allow a user write access to a certain
  table, based upon the identity of that user.

For more information, see [Identity-Based Policy Examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

**Consider client-side encryption**

If you store sensitive or confidential data in Amazon Keyspaces, you might want to
encrypt that data as close as possible to its origin so that your data is
protected throughout its lifecycle. Encrypting your sensitive data in
transit and at rest helps ensure that your plaintext data isn’t available to
any third party.
