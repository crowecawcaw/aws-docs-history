

# Encrypting Neptune resources at rest
<a name="encrypt"></a>

Data-at-rest encryption is the AWS recommendation. For more information, see [Data-at-Rest and Data-in-Transit encryption](https://docs.aws.amazon.com/whitepapers/latest/logical-separation/encrypting-data-at-rest-and--in-transit.html). Encryption is enforced in the AWS Console when you create a new Neptune DB Cluster or a new Neptune Global DB. This provides an additional layer of data protection. It secures your data from unauthorized access to the underlying storage and helps fulfill compliance requirements for data-at-rest encryption.

To manage the keys used for encrypting and decrypting your Neptune resources, you use [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/). AWS KMS combines secure, highly available hardware and software to provide a key management system scaled for the cloud. Using AWS KMS, you can create encryption keys and define the policies that control how these keys can be used. AWS KMS supports AWS CloudTrail, so you can audit key usage to verify that keys are being used appropriately.

At rest, all related logs, backups, and snapshots are encrypted for any encrypted Neptune DB clusters. The Neptune encryption does not apply to logs exported to Amazon CloudWatch.

## Encryption of Neptune resources
<a name="encrypt-enable"></a>

When you create a Neptune DB Cluster or a Neptune Global DB, you can supply the AWS KMS key identifier for your encryption key. If you don't specify a AWS KMS key identifier, Neptune uses your default Amazon RDS encryption key (`aws/rds`) in the Region. AWS KMS creates a default encryption key for each Region in your AWS account. For a Neptune Global cluster, there will be as many AWS KMS keys as Regions in it.

After you create a Neptune resource, you can't change the encryption key for that resource. So, be sure to determine your encryption key requirements before you create your Neptune resource. If a different AWS KMS key is required, you can use a snapshot of the existing Neptune DB Cluster to create a new one with a different AWS KMS key (see [Restoring from a DB Cluster Snapshot](backup-restore-restore-snapshot.md)).

You can use the Amazon Resource Name (ARN) of a key from another account to encrypt a Neptune resource. If you create a Neptune resource with the same AWS account that owns the AWS KMS encryption key, the AWS KMS key ID that you pass can be the AWS KMS key alias instead of the key's ARN.

**Important**  
If Neptune loses access to the encryption key for a Neptune DB Cluster - for example, when Neptune access to a key is revoked - the encrypted cluster is placed into a terminal state and can only be restored from a backup. We strongly recommend that you always enable backups for encrypted Neptune DB Clusters to guard against the loss of encrypted data in your databases.

## Key permissions needed when enabling encryption
<a name="encrypt-key-permissions"></a>

The IAM user or role creating a Neptune DB Cluster must have at least the following permissions for the KMS key:
+ `"kms:Encrypt"`
+ `"kms:Decrypt"`
+ `"kms:GenerateDataKey"`
+ `"kms:ReEncryptTo"`
+ `"kms:GenerateDataKeyWithoutPlaintext"`
+ `"kms:CreateGrant"`
+ `"kms:ReEncryptFrom"`
+ `"kms:DescribeKey"`

Here is an example (for `us-east-1` region) of a key policy that includes the necessary permissions:

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Id": "key-consolepolicy-3",
  "Statement": [
    {
      "Sid": "Enable Permissions for root principal",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::{{123456789012}}:root"
      },
      "Action": "kms:*",
      "Resource": "*"
    },
    {
      "Sid": "Allow use of the key for Neptune",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::{{123456789012}}:role/NeptuneFullAccess"
      },
      "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:GenerateDataKey",
        "kms:ReEncryptTo",
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:CreateGrant",
        "kms:ReEncryptFrom",
        "kms:DescribeKey"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": "rds.us-east-1.amazonaws.com"
        }
      }
    },
    {
      "Sid": "Deny use of the key for non Neptune",
      "Effect": "Deny",
      "Principal": {
        "AWS": "arn:aws:iam::{{123456789012}}:role/NeptuneFullAccess"
      },
      "Action": [
        "kms:*"
      ],
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "kms:ViaService": "rds.us-east-1.amazonaws.com"
        }
      }
    }
  ]
}
```

------
+ The first statement in this policy is optional. It gives access to the user's root principal.
+ The second statement provides access to all the required AWS KMS APIs for this role, scoped down to the RDS Service Principal.
+ The third statement tightens the security more by enforcing that this key is not usable by this role for any other AWS service.

You could also scope `createGrant` permissions down further by adding:

```
"Condition": {
  "Bool": {
    "kms:GrantIsForAWSResource": true
  }
}
```

## Limitations of Neptune Encryption
<a name="encrypt-limitations"></a>

The following limitations exist for Neptune Encryption:
+ You cannot convert an unencrypted Neptune DB Cluster to an encrypted one. You can only enable encryption for a Neptune DB Cluster when it is created. However, you can restore an unencrypted Neptune DB Cluster snapshot to an encrypted Neptune DB Cluster. To do this, specify a KMS encryption key when you restore from the unencrypted Neptune DB Cluster snapshot.
+ For compatibility reasons, it is still possible to create an unencrypted Neptune DB Cluster via the CLI and AWS SDKs. The console only allows creation of encrypted Neptune DB Clusters.
+ You cannot mix encrypted and unencrypted Neptune DB Clusters in the same Neptune Global DB. Either all the clusters are encrypted or all the clusters are unencrypted. This is enforced in the Neptune Global DB configuration.