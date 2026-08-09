# Amazon S3

Amazon S3 is an object storage service that stores data as objects within buckets. You can
connect an Amazon S3 bucket as a data source for your managed knowledge base to ingest the
objects you store there.

## Supported features

- Document metadata fields through separate metadata files
- Inclusion and exclusion content filters using file patterns and S3 key prefixes
- Incremental content syncs for added, updated, and deleted content
- Cross-account Amazon S3 bucket access
- Document-level access control (ACLs), with customer-provided ACL files

## Prerequisites

**In Amazon S3, make sure you**:

- Note the Amazon S3 bucket name and the AWS account ID of the bucket owner.
  The bucket must be a General Purpose bucket in the same AWS Region as
  your knowledge base, and you must have permission to access it.
- If the bucket is in a different AWS account from the knowledge base,
  or if it is encrypted with a customer managed KMS key, configure the
  bucket policy and (if applicable) the KMS key policy to allow access
  from your knowledge base service role. See [Bucket policies for cross-account and KMS-encrypted access](#kb-managed-s3-bucket-policies "#kb-managed-s3-bucket-policies").

**In your AWS account, make sure you**:

- Include the necessary permissions to connect to your data source in your
  AWS Identity and Access Management (IAM) role/permissions policy for your knowledge base. For
  information on the required permissions, see [Permissions to access your data sources](kb-permissions.md#kb-permissions-access-ds "kb-permissions.md#kb-permissions-access-ds").

## Bucket policies for cross-account and KMS-encrypted access

If your Amazon S3 bucket is in a different AWS account from your knowledge base, or
if it is encrypted with a customer managed KMS key, add a resource-based policy
to grant your knowledge base service role access. The following examples show the
minimum statements required.

### Cross-account bucket policy

In the account that owns the Amazon S3 bucket, add the following statement to the
bucket policy. Replace
`kb-account-id` with the account ID where your
knowledge base is created, `kb-service-role` with the
name of your knowledge base service role, and
`bucket-name` with your bucket name.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowBedrockKnowledgeBaseAccess",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::`kb-account-id`:role/`kb-service-role`"
            },
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::`bucket-name`",
                "arn:aws:s3:::`bucket-name`/*"
            ]
        }
    ]
}
```

For more general guidance, see [Configure access to Amazon S3 buckets](bedrock/latest/userguide/s3-bucket-access.md "bedrock/latest/userguide/s3-bucket-access.md").

### KMS key policy for encrypted buckets

If your Amazon S3 bucket is encrypted with a customer managed KMS key, add the
following statement to the key policy. Use the same placeholders as in the
cross-account bucket policy. Allow a few minutes for key policy changes to
propagate.

```
{
    "Sid": "AllowBedrockKnowledgeBaseKmsAccess",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::`kb-account-id`:role/`kb-service-role`"
    },
    "Action": [
        "kms:Decrypt",
        "kms:DescribeKey"
    ],
    "Resource": "*"
}
```

The `"Resource": "*"` here scopes to the key the policy is
attached to.

## How to set up an Amazon S3 data source

Setting up an Amazon S3 data source involves the following steps:

1. **Prepare your bucket.** Confirm the bucket
   name, the account ID, and (for cross-account access) the bucket policy. If
   you plan to use document metadata, decide on the Amazon S3 prefix where your
   `.metadata.json` files live.
2. **Connect the data source.** Create the
   Amazon S3 data source in the knowledge base using the AWS Management Console or the API. See
   [Create the data source](#kb-managed-ds-s3-create "#kb-managed-ds-s3-create").
3. **(Optional) Enable document-level access
   control.** Filter query results by user permissions defined in
   customer-provided ACL files. See [Document-level access controls](kb-managed-ds-s3-acl.md "kb-managed-ds-s3-acl.md").

## Create the data source

Console

###### To connect an Amazon S3 bucket to your managed knowledge base

1. Under **Data source**, provide a name for your data source.
2. Select **Amazon S3** from the data source dropdown.
3. Under **Data source location**, choose whether the Amazon S3 bucket is in **This AWS account** or **Other AWS account**.
4. Enter the Amazon S3 URI of your bucket. You can choose **Browse S3** to select a bucket.
5. (Optional) Enter a **Metadata files prefix** — the Amazon S3 prefix where document metadata files (`.metadata.json`) are stored for this data source.
6. (Optional) Expand **S3 prefix filter patterns** to include or exclude specific paths.
7. (Optional) Expand **File filter patterns** to add regex patterns to include or exclude specific files.
8. (Optional) To enable document-level access control, select **Control document access with ACLs** and provide the Amazon S3 URI of your global ACL file. This option cannot be changed after creation. For details, see [Document-level access controls](kb-managed-ds-s3-acl.md "kb-managed-ds-s3-acl.md").

API
To create an Amazon S3 data source, send a [CreateDataSource](../APIReference/API_agent_CreateDataSource.md "../APIReference/API_agent_CreateDataSource.md") request with an Agents for Amazon Bedrock build-time
endpoint. The following AWS Command Line Interface example creates a data source for a
bucket in the same account, with prefix and pattern filters. For a
description of each field, see the connector parameters reference that
follows.

```
aws bedrock-agent create-data-source \
 --name "`S3-connector`" \
 --knowledge-base-id "`your-knowledge-base-id`" \
 --data-source-configuration file://s3-managed-connector.json
```

The `s3-managed-connector.json` file contains the following:

```
{
    "type": "MANAGED_KNOWLEDGE_BASE_CONNECTOR",
    "managedKnowledgeBaseConnectorConfiguration": {
        "connectorParameters": {
            "type": "S3",
            "version": "1",
            "connectionConfiguration": {
                "bucketName": "`my-knowledge-base-bucket`",
                "bucketOwnerAccountId": "`123456789012`"
            },
            "filterConfiguration": {
                "inclusionPrefixes": ["`documents/`"],
                "inclusionPatterns": ["`.*\\.pdf`", "`.*\\.txt`"],
                "exclusionPatterns": ["`.*\\.tmp`"]
            },
            "metadataFilesPrefix": "`metadata/`"
        }
    }
}
```

To enable document-level access control, set `aclEnabled` to
`true` and add an `aclConfiguration` with
`globalAccessControlListS3Uri`. See [Document-level access controls](kb-managed-ds-s3-acl.md "kb-managed-ds-s3-acl.md").

For managed knowledge bases, `CreateDataSource` is
asynchronous: the data source status transitions from
`CREATING` to `AVAILABLE` when the operation
completes.

## Connector parameters

The data source configuration uses the following connector parameters. To connect
to Amazon S3, specify `S3` as the connector type in
`connectorParameters`. For the fields that wrap
`connectorParameters` (such as
`deletionProtectionConfiguration` and
`mediaExtractionConfiguration`), see [Connect a data source](kb-managed-connect-ds.md "kb-managed-connect-ds.md").

connectionConfiguration| Field | Required | Description |
| --- | --- | --- |
| `bucketName` | Yes | The name of the Amazon S3 bucket. |
| `bucketOwnerAccountId` | Conditional | The AWS account ID of the bucket owner. Required for<br>cross-account access. |

filterConfiguration (optional)| Field | Required | Description |
| --- | --- | --- |
| `inclusionPrefixes` | No | List of Amazon S3 key prefixes to include (for example,<br>`documents/`). |
| `exclusionPrefixes` | No | List of Amazon S3 key prefixes to exclude (for example,<br>`archive/`). |
| `inclusionPatterns` | No | List of regular expressions. Only objects whose keys match at<br>least one pattern are ingested. |
| `exclusionPatterns` | No | List of regular expressions. Objects whose keys match any pattern<br>are not ingested. |
| `maxFileSizeInMegaBytes` | No | Maximum size, in megabytes, of any single file the connector<br>ingests. Provide as a numeric string (for example,<br>`"500"`). Defaults to `"500"`. |

Top-level connector parameters (optional)| Field | Required | Description |
| --- | --- | --- |
| `metadataFilesPrefix` | No | The Amazon S3 prefix where document metadata files<br>(`.metadata.json`) are stored. |
| `aclEnabled` | No | Set to `true` to enable document-level access<br>control. You cannot change this setting after you create the data<br>source. For details, see [Document-level access controls](kb-managed-ds-s3-acl.md "kb-managed-ds-s3-acl.md"). |
| `aclConfiguration` | Conditional | Contains `globalAccessControlListS3Uri` — the<br>Amazon S3 URI of a JSON file that maps key prefixes to access control<br>entries. Required when `aclEnabled` is<br>`true`; ignored when `aclEnabled` is<br>`false`. See [Document-level access controls](kb-managed-ds-s3-acl.md "kb-managed-ds-s3-acl.md"). |

### Document metadata files

You can attach metadata to each document by uploading a sidecar file alongside
it. For each document, create a file named
``filename.extension`.metadata.json` in the
same Amazon S3 path. The metadata file must not exceed 10 KB. For example, alongside
`report.pdf`, upload `report.pdf.metadata.json` with the
following content:

```
{
    "metadataAttributes": {
        "company": {
            "value": {
                "type": "STRING",
                "stringValue": "BioPharm Innovations"
            }
        },
        "created_date": {
            "value": {
                "type": "NUMBER",
                "numberValue": 20221205
            }
        },
        "author": {
            "value": {
                "type": "STRING",
                "stringValue": "Lisa Thompson"
            }
        }
    }
}
```

For information on the supported attribute data types and the filtering
operators you can apply at query time, see [Metadata and
filtering](kb-test-config.md "kb-test-config.md").
