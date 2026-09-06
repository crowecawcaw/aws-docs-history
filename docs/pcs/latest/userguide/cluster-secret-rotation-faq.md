# Frequently asked questions about cluster secret rotation in AWS PCS

Find answers to common questions about cluster secret rotation in AWS PCS.

**What is a cluster secret?**

A cluster secret is a secure credential that enables secure communications between the Slurm controller and AWS PCS compute nodes. It also serves as the JSON Web Token (JWT) key for Slurm REST API authentication.

**What's the difference between cluster secret and JWT key?**

In AWS PCS, the cluster secret and JWT key are the same resource serving different purposes. The cluster secret authenticates Slurm internal communications, while the JWT key signs tokens for REST API authentication. When rotated, both aspects are affected simultaneously.

**How long does rotation take?**

The rotation process typically takes a few minutes. Your cluster remains in ACTIVE state and billing continues normally during rotation.

**Can I schedule automatic rotations?**

You can enable scheduled rotation in Secrets Manager. However, the initial release requires manual preparation (scaling node groups to 0) before each rotation.

**Will my existing JWT tokens still work after rotation?**

No, existing JWT tokens become invalid after rotation. Issue new tokens for REST API clients.

**Where can I find my cluster secret?**

You can find your cluster secret in the Secrets Manager console or through the AWS PCS console. For detailed instructions, see [Use AWS Secrets Manager to find the cluster secret](working-with_clusters_secrets_find_secrets-manager.md "working-with_clusters_secrets_find_secrets-manager.md") and [Use AWS PCS to find the cluster secret](working-with_clusters_secrets_find_pcs.md "working-with_clusters_secrets_find_pcs.md").

**Why does rotation require scaling node groups to 0?**

Rotation requires no running instances to ensure cluster stability during the secret update process. This prevents authentication conflicts between old and new secrets.

**What compliance requirements does this feature support?**

This feature enables AWS PCS to meet industry compliance standards including HIPAA and FedRAMP, which mandate regular credential rotation as part of their security controls.

**Can I use my own customer managed key for the AWS PCS managed secret?**

Yes. You can encrypt the cluster secret with a symmetric `ENCRYPT_DECRYPT`
customer managed key in the same AWS account and AWS Region. You attach or change the key through the
AWS Secrets Manager `UpdateSecret` operation. There is no AWS PCS API parameter for the secret's
encryption key.

The key policy must grant the AWS PCS service-linked role
(`AWSServiceRoleForPCS`) `kms:Decrypt`, `kms:GenerateDataKey`, and
`kms:DescribeKey`. For more information, see [Use a customer managed key to encrypt the cluster secret](working-with_clusters_secrets_cmk.md "working-with_clusters_secrets_cmk.md").

**Can I change the cluster secret value myself?**

No. AWS PCS manages the secret value. If you try to change the `SecretString` or
`SecretBinary` through AWS Secrets Manager, the request fails. You can change the encryption
key (the AWS KMS key) and the description.

**What happens if the service-linked role loses access to the key?**

Rotation and node operations that read the secret fail. The underlying cause is a AWS KMS
access-denied error that is visible in AWS CloudTrail, and the rotation surfaces as a failed
rotation. The cluster itself remains `ACTIVE`.
