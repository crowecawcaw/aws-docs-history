

# Permission requirements for S3 Tables SSE-KMS encryption
<a name="s3-tables-kms-permissions"></a>

When you use server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS) for tables in S3 table buckets you need to grant permissions for different identities in your account. At minimum your access identity and the S3 Tables maintenance principal need access to your key, the other permissions required depend on your use case.

**Required Permissions**   
To access a table encrypted with a KMS key, you need these permissions on that key:  
+ `kms:GenerateDataKey`
+ `kms:Decrypt`
To use SSE-KMS on tables the Amazon S3 Tables maintenance service principal (`maintenance.s3tables.amazonaws.com`) needs `kms:GenerateDataKey` and `kms:Decrypt` permissions on the key.

**Additional permissions**  
These additional permissions are required depending on your use case:  
+ **Permissions for AWS analytics services and direct access** – If you work with SSE-KMS encrypted tables through AWS analytics services or third-party engines accessing S3 tables directly, the IAM role you use needs permission to use your KMS key.
+ **Permissions with Lake Formation enabled** – If you have opted in to AWS Lake Formation for access control, the Lake Formation service role needs permission to use your KMS key.
+ **Permissions for S3 Metadata tables** – If you use SSE-KMS encryption for S3 Metadata tables, you need to provide the S3 Metadata service principal (`metadata.s3.amazonaws.com`) access to your KMS key. This allows S3 Metadata to update encrypted tables so they will reflect your latest data changes.

**Note**  
For cross-account KMS keys, your IAM role needs both key access permission and explicit authorization in the key policy. For more information about cross-account permissions for KMS keys, see [Allowing external AWS accounts to use a KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html#cross-account-console) in the *AWS Key Management Service Service Developer Guide*.

**Topics**
+ [Granting the S3 Tables maintenance service principal permissions to your KMS key](#tables-kms-maintenance-permissions)
+ [Granting IAM principals permissions to work with encrypted tables in integrated AWS analytics services](#tables-kms-integration-permissions)
+ [Granting IAM principals permissions to work with encrypted tables when Lake Formation is enabled](#tables-kms-lf-permissions)
+ [Granting the S3 Metadata service principal permissions to use your KMS key](#tables-kms-metadata-permissions)

## Granting the S3 Tables maintenance service principal permissions to your KMS key
<a name="tables-kms-maintenance-permissions"></a>

This permission is required to create SSE-KMS encrypted tables and to allow automatic table maintenance like compaction, snapshot management, and unreferenced file removal on the encrypted tables.

**Note**  
Whenever you make a request to create an SSE-KMS encrypted table, S3 Tables checks to make sure the `maintenance.s3tables.amazonaws.com` principal has access to your KMS key. To perform this check, a zero-byte object is temporarily created in your table bucket, this object will be automatically removed by the [unreferenced file removal](s3-table-buckets-maintenance.md#s3-table-bucket-maintenance-unreferenced) maintenance operations. If the KMS key you specified for encryption doesn’t have maintenance access the createTable operation will fail.

To grant maintenance access on SSE-KMS encrypted tables, you can use the following example key policy. In this policy, the `maintenance.s3tables.amazonaws.com` service principal is granted permission to use a specific KMS key for encrypting and decrypting tables in a specific table bucket. To use the policy, replace the {{user input placeholders}} with your own information:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "EnableKeyUsage",
            "Effect": "Allow",
            "Principal": {
                "Service": "maintenance.s3tables.amazonaws.com"            
            },
            "Action": [
                "kms:GenerateDataKey",
                "kms:Decrypt"
            ],
            "Resource": "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/{{key-id}}",
            "Condition": {
                "StringLike": {
                    "kms:EncryptionContext:aws:s3:arn":"{{<table-or-table-bucket-arn>}}/*"
                }
            }
        }
    ]
}
```

------

## Granting IAM principals permissions to work with encrypted tables in integrated AWS analytics services
<a name="tables-kms-integration-permissions"></a>

To work with S3 tables in AWS analytics services, you integrate your table buckets with AWS Glue Data Catalog. This integration allows AWS analytics services to automatically discover and access table data. For more information on the integration, see [Integrating Amazon S3 Tables with AWS analytics services](s3-tables-integrating-aws.md).

When you work with SSE-KMS encrypted tables through AWS analytics services or third-party and open-source engines accessing S3 tables directly, the IAM role you use needs permission to use your AWS KMS key for encryption operations.

You can grant KMS key access through an IAM policy attached to your role or through a KMS key policy.

------
#### [ IAM policy ]

Attach this inline policy to the IAM role you use for querying to allow KMS key access. Replace the KMS key ARN with your own.

```
{
    "Version":"2012-10-17",		 	 	 ,                    
    "Statement": [
        {
            "Sid": "AllowKMSKeyUsage",
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": "arn:aws:kms:us-west-2:{{111122223333}}:key/{{1234abcd-12ab-34cd-56ef-1234567890ab}}"
        }
    ]
}
```

------
#### [ KMS key policy ]

Alternatively, attach this statement to your KMS key policy to allow the specified IAM role to use the key. Replace the role ARN with the IAM role you use for querying.

```
{
    "Sid": "Allow use of the key",
    "Effect": "Allow",
    "Principal": {
        "AWS": [
            "arn:aws:iam::{{<catalog-account-id>}}:role/{{<role-name>}}"
        ]
    },
    "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey",
    ],
    "Resource": "*"
}
```

------

## Granting IAM principals permissions to work with encrypted tables when Lake Formation is enabled
<a name="tables-kms-lf-permissions"></a>

If you have opted in to AWS Lake Formation for access control on your S3 Tables integration, the Lake Formation service role needs permission to use your AWS KMS key for encryption operations. Lake Formation uses this role to vend credentials on behalf of principals accessing your tables.

The following KMS key policy example grants the Lake Formation service role permission to use a specific KMS key in your account for encryption operations. Replace the placeholder values with your own.

```
{
  "Sid": "AllowTableRoleAccess",
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::{{111122223333}}:role/service-role/S3TablesRoleForLakeFormation"
  },
  "Action": [
      "kms:GenerateDataKey", 
      "kms:Decrypt"
  ],
  "Resource": "{{<kms-key-arn>}}"
}
```

## Granting the S3 Metadata service principal permissions to use your KMS key
<a name="tables-kms-metadata-permissions"></a>

To allow Amazon S3 to update SSE-KMS encrypted metadata tables, and perform maintenance on those metadata tables, you can use the following example key policy. In this policy, you allow the `metadata.s3.amazonaws.com` and `maintenance.s3tables.amazonaws.com` service principals to encrypt and decrypt tables in a specific table bucket using a specific key. To use the policy, replace the {{user input placeholders}} with your own information:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "EnableKeyUsage",
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "maintenance.s3tables.amazonaws.com",
                    "metadata.s3.amazonaws.com"
                ]           
            },
            "Action": [
                "kms:GenerateDataKey",
                "kms:Decrypt"
            ],
            "Resource": "{{arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}}",
            "Condition": {
                "StringLike": {
                    "kms:EncryptionContext:aws:s3:arn":"{{<table-or-table-bucket-arn>}}/*"
                }
            }
        }
    ]
}
```

------