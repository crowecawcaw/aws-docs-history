

# Store SFTP server host keys in AWS Secrets Manager
<a name="server-host-key-storage"></a>

Instead of letting Transfer Family manage your host key material, you can store the host keys for your SFTP-enabled server in a secret in AWS Secrets Manager (Secrets Manager). With Secrets Manager storage, Transfer Family stores the host key in a secret that you can encrypt with your own AWS Key Management Service (AWS KMS) key.

Choose Secrets Manager storage when you want to retrieve your host key material and reuse the same host key across servers and AWS Regions. You can also choose Secrets Manager storage when you want to encrypt your host key material with an AWS KMS key that you manage, or when you want to scope and audit access to the host key in Secrets Manager. To use Secrets Manager storage, set the storage type to `SECRETS_MANAGER`, as described in the following section.

## Configure the host key storage type
<a name="server-host-key-storage-configure"></a>

You set the storage type when you create a server or when you import or update a host key. You can use the AWS Management Console, the AWS CLI, or the AWS API. In the AWS Transfer Family console, new servers default to AWS Secrets Manager storage. In the AWS CLI and the AWS API, new servers default to `SERVICE_MANAGED` storage if you don't set `HostKeyStorageType`. Transfer Family generates a host key for you if you don't provide one.
+ When you create a server with the [CreateServer](https://docs.aws.amazon.com/transfer/latest/APIReference/API_CreateServer) API operation, set the `HostKeyStorageType` parameter to `SERVICE_MANAGED` or `SECRETS_MANAGER`.
+ When you import or update a host key with the [ImportHostKey](https://docs.aws.amazon.com/transfer/latest/APIReference/API_ImportHostKey) or [UpdateHostKey](https://docs.aws.amazon.com/transfer/latest/APIReference/API_UpdateHostKey) API operation, set the `StorageType` parameter to `SERVICE_MANAGED` or `SECRETS_MANAGER`.

To encrypt the Secrets Manager secret with a customer managed key, set the optional `KmsKey` parameter to the Amazon Resource Name (ARN) of an AWS KMS key when you import or update the host key. If you don't specify a key, Transfer Family uses the AWS managed key for Secrets Manager. To change the key for a host key that already uses Secrets Manager storage, call UpdateHostKey with the new `KmsKey`, and Transfer Family re-encrypts the secret under the new key. To use a customer managed key, you must also update its key policy. For more information, see [Grant access to a customer managed key](#server-host-key-storage-kms).

**Note**  
When you call UpdateHostKey with `StorageType` set to `SECRETS_MANAGER`, your IAM identity must have the `transfer:ExportHostKey` permission, even if the host key already uses Secrets Manager storage. `transfer:ExportHostKey` is a permission-only action that doesn't map to an API operation.  
You can change the storage type of an existing host key from `SERVICE_MANAGED` to `SECRETS_MANAGER` only if you imported the host key on or after October 14, 2026. To move an older host key to Secrets Manager storage, contact AWS Support to request an exception. Include your AWS account ID in your request.

The first time that you use Secrets Manager storage, Transfer Family creates the AWSServiceRoleForTransfer service-linked role in your account. Your IAM identity must have the `iam:CreateServiceLinkedRole` permission for this call. For more information, see [Using service-linked roles for AWS Transfer Family](using-service-linked-roles.md).

The [DescribeHostKey](https://docs.aws.amazon.com/transfer/latest/APIReference/API_DescribeHostKey) and [ListHostKeys](https://docs.aws.amazon.com/transfer/latest/APIReference/API_ListHostKeys) API operations report the `StorageType` of each host key. For a host key that uses Secrets Manager storage, the response also includes the `SecretId` of the Secrets Manager secret that holds the key material.

## How Transfer Family manages the Secrets Manager secret
<a name="server-host-key-storage-slr"></a>

When you use Secrets Manager storage, Transfer Family creates a secret in your account with a name that begins with the `transfer!` prefix. Transfer Family uses the AWSServiceRoleForTransfer service-linked role to read the secret and serve the host key to incoming connections. For more information about this service-linked role, see [Using service-linked roles for AWS Transfer Family](using-service-linked-roles.md).

**Note**  
The secret is a managed secret. You can see it in the AWS Secrets Manager console, but Transfer Family controls its lifecycle, so we recommend that you don't modify or delete it manually. The AWSServiceRoleForTransfer service-linked role includes permissions that allow Transfer Family to eventually clean up orphaned secrets that are no longer associated with a host key. For more information, see [AWS Secrets Manager secrets managed by other AWS services](https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html).

## Work with the Secrets Manager secret
<a name="server-host-key-storage-manage"></a>

The following list describes what you can and can't do with the Secrets Manager secret that Transfer Family creates for your host key:
+ *Finding the secret* – Transfer Family names the secret with a `transfer!` prefix. To help you scope access or filter secrets in the Secrets Manager console, Transfer Family applies the tags `aws:transfer:owningServerArn` and `aws:transfer:owningHostKeyArn`, in addition to the owning-service tag `aws:secretsmanager:owningService=transfer`.
+ *Changing or rotating the host key* – You can't change the host key value through the Transfer Family API or in the Secrets Manager console, and Transfer Family doesn't use Secrets Manager automatic rotation for these secrets. To rotate a host key, import a new host key and delete the old one. For more information, see [Rotate the server host keys](server-host-key-rotate.md).
+ *Adding tags* – You can add your own tags to the secret.
+ *Changing the encryption key* – Call `UpdateHostKey` with the `KmsKey` parameter. Transfer Family re-encrypts the secret under the new key. For more information, see [Configure the host key storage type](#server-host-key-storage-configure).
+ *Deleting the secret* – To remove a host key, use the `DeleteHostKey` API operation. When you delete a host key or its server, Transfer Family schedules the secret for deletion. For more information, see [Delete a server host key](server-host-key-delete.md).

**Important**  
We strongly recommend that you don't delete this secret manually. Deleting the secret prevents Transfer Family from reading the host key and disrupts your SFTP-enabled server. Likewise, if you remove the service-linked role's access to the secret or to its AWS KMS key, new connections to your server fail. Operations on host keys are eventually consistent.

## Grant access to a customer managed key
<a name="server-host-key-storage-kms"></a>

If you encrypt the Secrets Manager secret with a customer managed key, the key policy must allow the Transfer Family service-linked role to call `kms:Decrypt`. The service-linked role's managed policy doesn't grant `kms:Decrypt`, so without this key policy statement Transfer Family can't read the host key material to serve it to incoming connections.

The following example key policy statement grants this access. The conditions limit the grant to calls that Secrets Manager makes on behalf of Transfer Family, for secrets whose names begin with `transfer!`. Replace {{111122223333}} with your AWS account ID and {{us-east-1}} with your AWS Region. If your Region is in a partition other than `aws`, also replace `arn:aws` with the ARN prefix for your partition.

```
{
  "Sid": "Enable Transfer SLR to access",
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::{{111122223333}}:role/aws-service-role/transfer.amazonaws.com/AWSServiceRoleForTransfer"
  },
  "Action": "kms:Decrypt",
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "kms:ViaService": "secretsmanager.{{us-east-1}}.amazonaws.com"
    },
    "StringLike": {
      "kms:EncryptionContext:SecretARN": "arn:aws:secretsmanager:{{us-east-1}}:{{111122223333}}:secret:transfer!*"
    }
  }
}
```