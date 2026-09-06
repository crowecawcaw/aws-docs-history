

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Network Migration API permissions
<a name="network-migration-api-permissions"></a>

The Network Migration APIs allow you to automate the migration of network infrastructure from VMware to AWS. To use these APIs, attach both the [AWSApplicationMigrationNetworkMigrationMultiAccount](security-iam-awsmanpol-AWSApplicationMigrationNetworkMigrationMultiAccount.md#security-iam-awsmanpol-AWSApplicationMigrationNetworkMigrationMultiAccount.title) managed policy and the following custom policy to your IAM identity.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "Tags",
            "Effect": "Allow",
            "Action": [
                "mgn:TagResource"
            ],
            "Resource": [
                "arn:aws:mgn:*:*:network-migration-definition/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/CreatedBy": "AWSTransform",
                    "mgn:CreateAction": [
                        "CreateNetworkMigrationDefinition"
                    ]
                }
            }
        },
        {
            "Sid": "CreateMethod",
            "Effect": "Allow",
            "Action": [
                "mgn:CreateNetworkMigrationDefinition"
            ],
            "Resource": [
                "*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/CreatedBy": "AWSTransform"
                }
            }
        },
        {
            "Sid": "ResourceMethods",
            "Effect": "Allow",
            "Action": [
                "mgn:UpdateNetworkMigrationDefinition",
                "mgn:StartNetworkMigrationMapping",
                "mgn:StartNetworkMigrationCodeGeneration",
                "mgn:StartNetworkMigrationDeployment",
                "mgn:StartNetworkMigrationAnalysis"
            ],
            "Resource": [
                "*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/CreatedBy": "AWSTransform"
                }
            }
        },
        {
            "Sid": "ReadonlyMethods",
            "Effect": "Allow",
            "Action": [
                "mgn:GetNetworkMigrationDefinition"
            ],
            "Resource": [
                "arn:aws:mgn:*:*:network-migration-definition/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/CreatedBy": "AWSTransform"
                }
            }
        },
        {
            "Sid": "DeleteExistingNetworkMigrationDefinition",
            "Effect": "Allow",
            "Action": [
                "mgn:DeleteNetworkMigrationDefinition"
            ],
            "Resource": [
                "arn:aws:mgn:*:*:network-migration-definition/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/CreatedBy": "AWSTransform"
                }
            }
        },
        {
            "Sid": "ReadOnly",
            "Effect": "Allow",
            "Action": [
                "mgn:ListNetworkMigrationDefinitions",
                "mgn:ListNetworkMigrationExecutions",
                "mgn:ListNetworkMigrationMapperSegments",
                "mgn:ListNetworkMigrationMappings",
                "mgn:ListNetworkMigrationMapperSegmentConstructs",
                "mgn:ListNetworkMigrationCodeGenerationSegments",
                "mgn:ListNetworkMigrationCodeGenerations",
                "mgn:ListNetworkMigrationDeployedStacks",
                "mgn:ListNetworkMigrationDeployments",
                "mgn:ListNetworkMigrationAnalysisResults",
                "mgn:ListNetworkMigrationAnalyses",
                "mgn:GetNetworkMigrationMapperSegmentConstruct"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "MGNNetworkMigrationUpdate",
            "Effect": "Allow",
            "Action": [
                "mgn:UpdateNetworkMigrationMapperSegment",
                "mgn:StartNetworkMigrationMappingUpdate",
                "mgn:ListNetworkMigrationMappingUpdates"
            ],
            "Resource": [
                "arn:aws:mgn:*:*:network-migration-definition/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/CreatedBy": "AWSTransform"
                }
            }
        },
        {
            "Sid": "MGNImportFileEnrichment",
            "Effect": "Allow",
            "Action": [
                "mgn:StartImportFileEnrichment",
                "mgn:ListImportFileEnrichments"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "S3Bucket",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetBucketTagging",
                "s3:GetBucketPublicAccessBlock",
                "s3:GetBucketLocation",
                "s3:CreateBucket",
                "s3:PutBucketTagging",
                "s3:PutEncryptionConfiguration"
            ],
            "Resource": "arn:aws:s3:::*",
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "aws:CalledVia": [
                        "mgn.amazonaws.com"
                    ]
                }
            }
        },
        {
            "Sid": "S3BucketObject",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:GetObjectVersion",
                "s3:ListMultipartUploadParts",
                "s3:ListBucketMultipartUploads",
                "s3:GetObjectAttributes",
                "s3:PutObject",
                "s3:AbortMultipartUpload",
                "s3:DeleteObject"
            ],
            "Resource": "arn:aws:s3:::*/*",
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "aws:CalledVia": [
                        "mgn.amazonaws.com"
                    ]
                }
            }
        },
        {
            "Sid": "MGNNetworkAnalysis",
            "Effect": "Allow",
            "Action": [
                "ec2:CreateNetworkInsightsPath",
                "ec2:StartNetworkInsightsAnalysis",
                "ec2:DeleteNetworkInsightsPath",
                "ec2:DeleteNetworkInsightsAnalysis",
                "ec2:CreateTags"
            ],
            "Resource": [
                "arn:aws:ec2:*:*:network-insights-path/*",
                "arn:aws:ec2:*:*:network-insights-analysis/*",
                "arn:aws:ec2:*:*:network-interface/*"
            ],
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "aws:CalledVia": [
                        "mgn.amazonaws.com"
                    ]
                }
            }
        },
        {
            "Sid": "EC2DescribeNoCondition",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeVpcAttribute"
            ],
            "Resource": "*"
        },
        {
            "Sid": "MGNServiceQuota",
            "Effect": "Allow",
            "Action": "servicequotas:GetServiceQuota",
            "Resource": "arn:aws:servicequotas:*:*:vpc/L-2AFB9258",
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "aws:CalledVia": "mgn.amazonaws.com"
                }
            }
        },
        {
            "Sid": "EC2GetSubnetCidrReservations",
            "Effect": "Allow",
            "Action": "ec2:GetSubnetCidrReservations",
            "Resource": "*"
        },
        {
            "Sid": "TirosForNetworkInsights",
            "Effect": "Allow",
            "Action": [
                "tiros:CreateQuery",
                "tiros:GetQueryAnswer",
                "tiros:GetQueryExplanation"
            ],
            "Resource": "*"
        }
    ]
}
```

------