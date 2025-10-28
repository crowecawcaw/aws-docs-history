# Encrypting data at rest

Encryption at rest encrypts data stored on your EFS file system. This helps
you meet compliance requirements and protect sensitive data from unauthorized access. Your
organization might require encryption of all data that meets a specific classification or is
associated with a particular application, workload, or environment.

###### Note

The AWS key management infrastructure uses Federal Information Processing Standards
(FIPS) 140-3 approved cryptographic algorithms. The infrastructure is consistent with
National Institute of Standards and Technology (NIST) 800-57 recommendations.

When you create a file system using the Amazon EFS console, encryption at rest is enabled by
default. When using the AWS CLI, API, or SDKs to create a file system, you must explicity
enable encryption.

After you create an EFS file system, you cannot change its encryption
setting. This means that you cannot modify an unencrypted file system to make it encrypted.
Instead, [replicate the file system](efs-replication.md "efs-replication.md") to copy data from
the unencrypted file system to a new encrypted file system. For more information, see [How do I turn on
encryption at rest for an existing EFS file system?](https://repost.aws/knowledge-center/efs-turn-on-encryption-at-rest "https://repost.aws/knowledge-center/efs-turn-on-encryption-at-rest")

## How encryption at rest works

In an encrypted file system, data and metadata are encrypted by default before being
written to storage and are automatically decrypted when read. These processes are handled
transparently by Amazon EFS, so you don't need to modify your applications.

Amazon EFS uses AWS KMS for key management as follows:

- **File data encryption** – The contents of your files
  are encrypted using the KMS key that you specify. This can be either:
  - The AWS owned key for Amazon EFS (`aws/elasticfilesystem`) – Default
    option, no additional charges.
  - A customer managed key that you create and manage – Provides additional control and
    audit capabilities.

- **Metadata encryption** - File names, directory
  names, and directory contents are encrypted using a key that Amazon EFS manages
  internally.

### Encryption process

When a file system is created or rerplicated to a file system in the same account,
Amazon EFS uses a [Forward Access Session
(FAS)](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md") to make KMS calls using the caller's credentials. In CloudTrail logs, the
`kms:CreateGrant` call appears to be made by the same user identity that
created the file system or replication. You can identify Amazon EFS service calls in CloudTrail by
looking for the `invokedBy` field with the value
`elasticfilesystem.amazonaws.com`. The resource policy on the KMS key must
allow the `CreateGrant` action for FAS to make the call.

###### Important

You manage control of the grant, and can revoke it at any time. Revoking the grant
prevents Amazon EFS from accessing the KMS key for future operations. For more information,
see [Retiring and revoking grants](../../../kms/latest/developerguide/grant-delete.md "../../../kms/latest/developerguide/grant-delete.md") in the _AWS Key Management Service Developer Guide._.

When using customer managed KMS keys, the resource policy must also allow the Amazon EFS
service principal and include the `kms:ViaService` condition to restrict access
to the specific service endpoint. For example:

```
"kms:ViaService":
    "elasticfilesystem.us-east-2.amazonaws.com"

```

Amazon EFS uses industry-standard AES-256 encryption algorithm to encrypt data and metadata
at rest.

For more information about KMS key policies for Amazon EFS, see [Using AWS KMS keys for Amazon EFS](EFSKMS.md "EFSKMS.md").

## Enforcing encryption at rest for new file

systems

You can use the `elasticfilesystem:Encrypted` IAM condition key in
AWS Identity and Access Management (IAM) identity-based policies to enforce creation at rest when users create
EFS file systems. For more information about using the condition key, see [Example: Enforce the creation
of encrypted file systems](security_iam_id-based-policy-examples.md#using-iam-to-enforce-encryption-at-rest "security_iam_id-based-policy-examples.md#using-iam-to-enforce-encryption-at-rest").

You can also define service control policies (SCPs) inside AWS Organizations to enforce Amazon EFS
encryption for all AWS accounts in your organization. For more information about service
control policies in AWS Organizations, see [Service control policies](../../../organizations/latest/userguide/orgs_manage_policies_scps.md#orgs_manage_policies_scp "../../../organizations/latest/userguide/orgs_manage_policies_scps.md#orgs_manage_policies_scp") in the _AWS Organizations User Guide_.
