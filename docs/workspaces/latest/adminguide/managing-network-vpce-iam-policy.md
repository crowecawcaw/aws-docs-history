

# Using Amazon S3 VPC Endpoints for WorkSpaces Pools Features
<a name="managing-network-vpce-iam-policy"></a>

When you enable Application Settings Persistence for a WorkSpaces Pool or Home folders for a WorkSpaces Pool directory, WorkSpaces uses the VPC you specify for your directory to provide access to Amazon Simple Storage Service (Amazon S3) buckets. To enable WorkSpaces Pools access to your private S3 endpoint, attach the following custom policy to your VPC endpoint for Amazon S3. For more information about private Amazon S3 endpoints, see [VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html) and [Endpoints for Amazon S3](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-s3.html) in the *Amazon VPC User Guide*.

Use the following policy for resources in your Region type. Replace {{111122223333}} with your AWS account ID:

------
#### [ Commercial AWS Regions ]

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowWorkSpacesPoolsToAccessS3Buckets",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:sts::{{111122223333}}:assumed-role/workspaces_DefaultRole/WorkSpacesPoolSession"
            },
            "Action": [
                "s3:ListBucket",
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject",
                "s3:GetObjectVersion",
                "s3:DeleteObjectVersion"
            ],
            "Resource": [
                "arn:aws:s3:::wspool-app-settings-*",
                "arn:aws:s3:::wspool-home-folder-*",
                "arn:aws:s3:::wspool-logs-*"
            ]
        }
    ]
}
```

------
#### [ AWS GovCloud (US) Regions ]

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowWorkSpacesPoolsToAccessS3Buckets",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws-us-gov:sts::{{111122223333}}:assumed-role/workspaces_DefaultRole/WorkSpacesPoolSession"
            },
            "Action": [
                "s3:ListBucket",
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject",
                "s3:GetObjectVersion",
                "s3:DeleteObjectVersion"
            ],
            "Resource": [
                "arn:aws-us-gov:s3:::wspool-app-settings-*",
                "arn:aws-us-gov:s3:::wspool-home-folder-*",
                "arn:aws-us-gov:s3:::wspool-logs-*"
            ]
        }
    ]
}
```

------