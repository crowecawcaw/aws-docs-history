

# Required roles and permissions for canaries
<a name="CloudWatch_Synthetics_Canaries_CanaryPermissions"></a>

Each canary must be associated with an IAM role that has certain permissions attached. When you create a canary using the CloudWatch console, you can choose for CloudWatch Synthetics to create an IAM role for the canary. If you do, the role will have the permissions needed.

If you want to create the IAM role yourself, or create an IAM role that you can use when using the AWS CLI or APIs to create a canary, the role must contain the permissions listed in this section.

All IAM roles for canaries must include the following trust policy statement.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "lambda.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

------

Additionally, the canary's IAM role needs one of the following statements.

 **Basic canary that doesn't use AWS KMS or need Amazon VPC access** 

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::{{path/to/your/s3/bucket/canary/results/folder}}"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetBucketLocation"
            ],
            "Resource": [
                "arn:aws:s3:::{{name/of/the/s3/bucket/that/contains/canary/results}}"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "logs:PutLogEvents",
                "logs:CreateLogGroup"
            ],
            "Resource": [
            "arn:aws:logs:{{us-east-1}}:{{123456789012}}:log-group:/aws/lambda/cwsyn-{{canary_name}}-*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListAllMyBuckets",
                "xray:PutTraceSegments"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Resource": "*",
            "Action": "cloudwatch:PutMetricData",
            "Condition": {
                "StringEquals": {
                    "cloudwatch:namespace": "CloudWatchSynthetics"
                }
            }
        }
    ]
}
```

------

 **Canary that uses AWS KMS to encrypt canary artifacts but does not need Amazon VPC access** 

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::{{path/to/your/S3/bucket/canary/results/folder}}"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetBucketLocation"
            ],
            "Resource": [
                "arn:aws:s3:::{{name/of/the/S3/bucket/that/contains/canary/results}}"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "logs:PutLogEvents",
                "logs:CreateLogGroup"
            ],
            "Resource": [
            "arn:aws:logs:{{us-east-1}}:{{123456789012}}:log-group:/aws/lambda/cwsyn-{{canary_name}}-*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListAllMyBuckets",
                "xray:PutTraceSegments"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Resource": "*",
            "Action": "cloudwatch:PutMetricData",
            "Condition": {
                "StringEquals": {
                    "cloudwatch:namespace": "CloudWatchSynthetics"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/{{KMS_key_id}}",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": [
                        "s3.{{us-east-1}}.amazonaws.com"
                    ]
                }
            }
        }
    ]
}
```

------

 **Canary that does not use AWS KMS but does need Amazon VPC access** 

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::{{path/to/your/S3/bucket/canary/results/folder}}"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetBucketLocation"
            ],
            "Resource": [
                "arn:aws:s3:::{{name/of/the/S3/bucket/that/contains/canary/results}}"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "logs:PutLogEvents",
                "logs:CreateLogGroup"
            ],
            "Resource": [
            "arn:aws:logs:{{us-east-1}}:{{123456789012}}:log-group:/aws/lambda/cwsyn-{{canary_name}}-*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListAllMyBuckets",
                "xray:PutTraceSegments"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Resource": "*",
            "Action": "cloudwatch:PutMetricData",
            "Condition": {
                "StringEquals": {
                    "cloudwatch:namespace": "CloudWatchSynthetics"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:CreateNetworkInterface",
                "ec2:DescribeNetworkInterfaces",
                "ec2:DeleteNetworkInterface"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```

------

 **Canary that uses AWS KMS to encrypt canary artifacts and also needs Amazon VPC access** 

If you update a non-VPC canary to start using a VPC, you'll need to update the canary's role to include the network interface permissions listed in the following policy.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::{{path/to/your/S3/bucket/canary/results/folder}}"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetBucketLocation"
            ],
            "Resource": [
                "arn:aws:s3:::{{name/of/the/S3/bucket/that/contains/canary/results}}"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "logs:PutLogEvents",
                "logs:CreateLogGroup"
            ],
            "Resource": [
            "arn:aws:logs:{{us-east-1}}:{{123456789012}}:log-group:/aws/lambda/cwsyn-{{canary_name}}-*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListAllMyBuckets",
                "xray:PutTraceSegments"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Resource": "*",
            "Action": "cloudwatch:PutMetricData",
            "Condition": {
                "StringEquals": {
                    "cloudwatch:namespace": "CloudWatchSynthetics"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:CreateNetworkInterface",
                "ec2:DescribeNetworkInterfaces",
                "ec2:DeleteNetworkInterface"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/{{KMS_key_id}}",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": [
                        "s3.{{us-east-1}}.amazonaws.com"
                    ]
                }
            }
        }
    ]
}
```

------

## Canary that uses a customer managed AWS KMS key to encrypt Lambda function environment variables
<a name="CloudWatch_Synthetics_Canaries_FunctionKmsPermissions"></a>

If you configure a customer managed key for environment variable encryption at rest, you must have `kms:CreateGrant`, `kms:Encrypt`, `kms:Decrypt`, and `kms:DescribeKey` permissions on the key. The canary execution role must also have `kms:Decrypt` if you use encryption in transit. For more information, see [Encrypting environment variables at rest with a customer managed key](CloudWatch_Synthetics_Canaries_CommonFeatures.md#CloudWatch_Synthetics_function_encryption).

If you use encryption in transit, add the following statement to your canary's execution role policy:

```
{
  "Effect": "Allow",
  "Action": "kms:Decrypt",
  "Resource": "arn:aws:kms:us-east-1:111122223333:key/a1b2c3d4-e5f6-7890-abcd-EXAMPLE11111"
}
```

Add this statement to whichever base execution role policy you are already using (basic, VPC, or artifact KMS).