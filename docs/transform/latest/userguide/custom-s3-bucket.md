# Using your own Amazon S3 bucket

By default, AWS Transform uses a service-managed Amazon S3 bucket to store transformation artifacts.
You can choose to use your own Amazon S3 bucket instead for greater control over data
storage, encryption, and access policies.

###### Note

If you have an Amazon S3 bucket for mainframe transformations, you can continue to use that
S3 connector and you don't need to use this functionality.

###### Note

Your Amazon S3 bucket stores only the uploads and transformation artifacts that you
interact with. Internal system-generated artifacts are not stored in your bucket.
Additionally, AWS Transform indexes the artifacts in your bucket. It stores the indexed data in
a service-managed knowledge base that is used to provide you an enriched chat experience.

## Prerequisites

Before you configure your own Amazon S3 bucket, make sure that the following requirements are
met:

- The bucket must be in the same AWS Region where AWS Transform is enabled.
- The required bucket policy must be applied to your bucket. For more information, see
  [Required bucket policy](#custom-s3-bucket-policy "#custom-s3-bucket-policy").
- If you use the AWS Transform web application, CORS must be configured on your bucket. For more
  information, see [Required CORS configuration](#custom-s3-bucket-cors "#custom-s3-bucket-cors").
- If you use a custom AWS KMS key, the required key policy must be applied. For more
  information, see [KMS key policy (optional)](#custom-s3-bucket-kms-policy "#custom-s3-bucket-kms-policy").

### Supported encryption configurations

Your bucket must use one of the following encryption configurations:

- SSE-S3 (AES256) — Leave the KMS key field empty. AWS Transform writes objects without specifying an encryption header, and Amazon S3 applies the bucket's default encryption with S3-managed keys. For more information, see [Using server-side encryption with Amazon S3 managed keys (SSE-S3)](../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md "../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md") in the _Amazon S3 User Guide_.
- SSE-KMS with a customer-managed KMS key — Provide the KMS key ARN. AWS Transform writes objects with `x-amz-server-side-encryption: aws:kms` using the provided key. Follow
  [KMS key policy (optional)](#custom-s3-bucket-kms-policy "#custom-s3-bucket-kms-policy").

The following are not supported:

- SSE-KMS with an AWS-managed KMS key (for example, `aws/s3`)
- SSE-C
- DSSE-KMS
- Asymmetric KMS keys or KMS keys with a key spec other than SYMMETRIC\_DEFAULT

###### Warning

AWS-managed KMS keys are not supported. If your bucket is encrypted with `aws/s3`, migrate to a customer-managed key or SSE-S3 before using the bucket with AWS Transform.

## Configuring your Amazon S3 bucket

You can configure AWS Transform to use your own Amazon S3 bucket from the AWS Transform console.

###### To use your own Amazon S3 bucket

1. In the AWS Transform console, choose **Settings**.
2. Under **Artifact storage**, choose **Use my own S3
   bucket**. You can use a bucket in your current AWS account or in another account.
3. For **Bucket**, enter the Amazon S3 URI.
4. (Optional) For **KMS key**, enter an AWS KMS key ARN to encrypt objects
   in the bucket. If you leave this field empty, AWS Transform writes objects without an encryption
   header, and Amazon S3 applies the bucket's default encryption settings. For more information,
   see [Setting default server-side encryption behavior for Amazon S3 buckets](../../../AmazonS3/latest/userguide/bucket-encryption.md "../../../AmazonS3/latest/userguide/bucket-encryption.md") in the
   _Amazon S3 User Guide_.

If your bucket's default encryption is SSE-KMS, enter the customer-managed KMS key ARN
in this field and update your key policy. For more information, see
[KMS key policy (optional)](#custom-s3-bucket-kms-policy "#custom-s3-bucket-kms-policy"). 5. Choose **Save**. AWS Transform validates the bucket configuration and
permissions before applying the configuration.

After you save the configuration, AWS Transform uses your bucket to store transformation
artifacts.

###### Note

AWS Transform validates your configuration only when you save. If you later change the bucket
policy, CORS configuration, or KMS key policy, re-save your profile settings to
re-validate.

## Required bucket policy

You must configure the bucket policy to grant AWS Transform access. Add the following bucket policy
to your Amazon S3 bucket to allow the AWS Transform service principal to read, write, delete, and list
transformation artifacts.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "transform.amazonaws.com"
                ]
            },
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject",
                "s3:AbortMultipartUpload",
                "s3:ListMultipartUploadParts",
                "s3:PutObjectTagging"
            ],
            "Resource": "arn:aws:s3:::`bucket-name`/AWSTransform/*",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "`profile-account-id`",
                    "aws:SourceArn": "`profile-arn`"
                }
            }
        },
        {
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "transform.amazonaws.com"
                ]
            },
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::`bucket-name`",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "`profile-account-id`",
                    "aws:SourceArn": "`profile-arn`"
                }
            }
        }
    ]
}
```

Replace the following values:

- `bucket-name` – The name of your Amazon S3 bucket.
- `profile-account-id` – The AWS account ID associated with your AWS Transform profile.
- `profile-arn` – The ARN of your AWS Transform profile.

## Required CORS configuration

If you use the AWS Transform web application, you must configure Cross-Origin Resource Sharing
(CORS) on your Amazon S3 bucket. You can find the web application domain after enabling AWS Transform. For
more information, see [Getting started with AWS Transform](getting-started.md "getting-started.md").

```
[
    {
        "AllowedHeaders": [
            "host",
            "content-type",
            "if-none-match",
            "x-amz-checksum-sha256",
            "x-amz-expected-bucket-owner",
            "x-amz-server-side-encryption",
            "x-amz-server-side-encryption-aws-kms-key-id",
            "x-amz-server-side-encryption-context",
            "x-amz-source-account",
            "x-amz-source-arn"
        ],
        "AllowedMethods": [
            "GET",
            "PUT",
            "HEAD"
        ],
        "AllowedOrigins": [
            "`webapp-domain`"
        ],
        "ExposeHeaders": [
            "ETag",
            "x-amz-checksum-sha256",
            "x-amz-request-id",
            "x-amz-id-2"
        ],
        "MaxAgeSeconds": 3600
    }
]
```

Replace the following values:

- `webapp-domain` – Your web application origin URL (for example,
  `https://1a2b3c4d5e6f7a8b9.transform.us-east-1.on.aws`), which can be found on
  the AWS Transform settings page. **Do not include the trailing slash.**

## KMS key policy (optional)

This section applies only when your bucket is encrypted with a customer-managed KMS key.
If your bucket uses SSE-S3, skip this section.

If you specify your own AWS KMS key for bucket encryption, add the following statement to
your key policy. AWS Transform relies on Forward Access Sessions (FAS) to create grants for its service
principal. These grants are used to validate your key and access artifacts in your Amazon S3
bucket.

```
{
    "Sid": "AllowAWSTransformServiceAccess",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::`key-owner-account-id`:root"
    },
    "Action": [
        "kms:CreateGrant",
        "kms:DescribeKey"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "kms:ViaService": "transform.`region`.amazonaws.com"
        }
    }
}
```

Replace the following values:

- `key-owner-account-id` – The AWS account ID that owns the KMS key.
- `region` – The AWS Region where AWS Transform is enabled (for example, `us-east-1`).

## Switching back to the default bucket

You can switch back to the service-managed bucket at any time.

###### To switch to AWS Transform managed storage

1. In the AWS Transform console, choose **Settings**.
2. Under **Artifact storage**, choose **Edit**.
3. Choose **AWS Transform managed storage**.
4. Choose **Save**.

###### Warning

If you switch storage configurations while transformation jobs are in progress, those
jobs fail. Any artifacts that were already generated by those in-progress jobs would also
not be accessible.

###### Important

When you switch back to the service-managed bucket:

- Artifacts in your bucket are not automatically migrated. To retain any artifacts,
  download them from your Amazon S3 bucket and re-upload them through the AWS Transform web application
  to the artifact store for the corresponding workspace and job.
- AWS Transform retires its grant on your KMS key. Objects written to your bucket remain in
  your bucket; delete them manually if they are no longer needed.

## Uploading files directly to your bucket

You can upload files directly to your Amazon S3 bucket without using the AWS Transform web application.
To make uploaded files available to transformation agents, upload them to the `User Uploads`
folder for the job. The directory path for this folder uses the following
format:

```
AWSTransform/Workspaces/`workspace-id`/Jobs/`job-id`/User Uploads/
```

Replace the following values:

- `workspace-id` – The ID of your AWS Transform workspace.
- `job-id` – The ID of the transformation job.

Each job in AWS Transform has its own `User Uploads` folder. Files that you upload to this
path appear in the web application and are available to transformation agents while they
complete the job.

File paths must not contain `..`, `//`, or leading or trailing
spaces — files that violate these constraints are not visible to agents.

###### Deleting bucket contents can cause job failures

Deleting `job_objective` will cause job failures for active jobs or if the
session is restored. For all other files, deleting them may result in unexpected agent
behavior or job failures.

###### Important

If your bucket uses SSE-KMS, include the following headers on every direct upload:

```
x-amz-server-side-encryption: aws:kms
x-amz-server-side-encryption-aws-kms-key-id: `your-kms-key-arn`
```

Objects must be encrypted with the KMS key registered in your AWS Transform profile. Objects
encrypted with any other key are not accessible to AWS Transform.

## Compatibility Matrix

The following table summarizes the compatibility of AWS Transform with common Amazon S3 bucket
features.

| Feature                                 | Compatibility                   | Notes                                                       |
| --------------------------------------- | ------------------------------- | ----------------------------------------------------------- |
| Bucket versioning                       | Supported                       | Manage noncurrent versions with a lifecycle rule.           |
| Object Ownership                        | Required: Bucket owner enforced | Bucket owner preferred and Object writer are not supported. |
| ACL                                     | Not supported                   | ACLs must be disabled on the bucket.                        |
| Object Lock (governance mode)           | Partially supported             | Deletes might be blocked by retention settings.             |
| Object Lock (compliance mode)           | Not supported                   | —                                                           |
| Block Public Access                     | Supported                       | —                                                           |
| Requester Pays                          | Not supported                   | —                                                           |
| S3 Access Points                        | Not supported                   | Use the bucket name.                                        |
| S3 Object Lambda Access Points          | Not supported                   | Use the bucket name.                                        |
| S3 on Outposts                          | Not supported                   | —                                                           |
| S3 Express One Zone (directory buckets) | Not supported                   | —                                                           |
| Cross-Region buckets                    | Not supported                   | —                                                           |
| Cross-account buckets                   | Supported                       | —                                                           |
| Cross-account KMS keys                  | Not supported                   | —                                                           |
| Lifecycle rules                         | Supported                       | —                                                           |
| CloudTrail data events                  | Supported                       | —                                                           |
