# Bulk operation prerequisites

This section explains bulk operation prerequisites, including AWS Identity and Access Management (IAM) permissions for exchanging
resources between AWS services and your local machine. Before you start a bulk operation, complete the following
prerequisite:

- Create an Amazon S3 bucket to store resources. For more information about using Amazon S3, see [What is Amazon S3?](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md")

## IAM permissions

To perform bulk operations, you must create an AWS Identity and Access Management (IAM) policy with permissions that allow the
exchange of AWS resources between Amazon S3, AWS IoT SiteWise, and your local machine. For more information about creating
IAM policies, see [Creating
IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md").

To perform bulk operations, you need the following policies.

This policy allows access to the required AWS IoT SiteWise API actions for bulk operations:

```
{
    "Sid": "SiteWiseApiAccess",
    "Effect": "Allow",
    "Action": [
        "iotsitewise:CreateAsset",
        "iotsitewise:CreateAssetModel",
        "iotsitewise:UpdateAsset",
        "iotsitewise:UpdateAssetModel",
        "iotsitewise:UpdateAssetProperty",
        "iotsitewise:ListAssets",
        "iotsitewise:ListAssetModels",
        "iotsitewise:ListAssetProperties",
        "iotsitewise:ListAssetModelProperties",
        "iotsitewise:ListAssociatedAssets",
        "iotsitewise:DescribeAsset",
        "iotsitewise:DescribeAssetModel",
        "iotsitewise:DescribeAssetProperty",
        "iotsitewise:AssociateAssets",
        "iotsitewise:DisassociateAssets",
        "iotsitewise:AssociateTimeSeriesToAssetProperty",
        "iotsitewise:DisassociateTimeSeriesFromAssetProperty",
        "iotsitewise:BatchPutAssetPropertyValue",
        "iotsitewise:BatchGetAssetPropertyValue",
        "iotsitewise:TagResource",
        "iotsitewise:UntagResource",
        "iotsitewise:ListTagsForResource",
        "iotsitewise:CreateAssetModelCompositeModel",
        "iotsitewise:UpdateAssetModelCompositeModel",
        "iotsitewise:DescribeAssetModelCompositeModel",
        "iotsitewise:DeleteAssetModelCompositeModel",
        "iotsitewise:ListAssetModelCompositeModels",
        "iotsitewise:ListCompositionRelationships",
        "iotsitewise:DescribeAssetCompositeModel"
    ],
    "Resource": "*"
}
```

This policy allows access to the AWS IoT TwinMaker API operations that you use to work with bulk
operations:

```
{
    "Sid": "MetadataTransferJobApiAccess",
    "Effect": "Allow",
    "Action": [
        "iottwinmaker:CreateMetadataTransferJob",
        "iottwinmaker:CancelMetadataTransferJob",
        "iottwinmaker:GetMetadataTransferJob",
        "iottwinmaker:ListMetadataTransferJobs"
    ],
    "Resource": "*"
}
```

This policy provides access to Amazon S3 buckets for transferring metadata for bulk operations.

For a specific Amazon S3 bucket
If you use one specific bucket for working with your bulk operations metadata, this policy
provides access to that bucket:

```
{
    "Effect": "Allow",
    "Action": [
        "s3:PutObject",
        "s3:GetObject",
        "s3:GetBucketLocation",
        "s3:ListBucket",
        "s3:AbortMultipartUpload",
        "s3:ListBucketMultipartUploads",
        "s3:ListMultipartUploadParts"
    ],
    "Resource": [
        "arn:aws:s3:::`bucket name`",
        "arn:aws:s3:::`bucket name`/*"
    ]
}
```

To allow any Amazon S3 bucket
If you will use many different buckets to work with your bulk operations metadata, this policy
provides access to any bucket:

```
{
    "Effect": "Allow",
    "Action": [
        "s3:PutObject",
        "s3:GetObject",
        "s3:GetBucketLocation",
        "s3:ListBucket",
        "s3:AbortMultipartUpload",
        "s3:ListBucketMultipartUploads",
        "s3:ListMultipartUploadParts"
    ],
    "Resource": "*"
}
```

For information about troubleshooting import and export operations, see [Troubleshoot bulk import and
export](troubleshooting-bulk.md "troubleshooting-bulk.md").
