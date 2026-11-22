

# AmazonSageMakerHyperPodInferenceGatewayGlobalRoutingAccess

**Description**: This policy provides the permissions that the SageMaker HyperPod inference gateway controller needs to join a SageMaker global inference gateway. It enables the controller to create and manage an Amazon EC2 VPC endpoint service in front of the gateway's Network Load Balancer, and an interface VPC endpoint to Amazon Kinesis Data Streams with its security group. It also enables the controller to read Amazon EC2 networking and Elastic Load Balancing resources, to store the gateway's TLS server certificate in Amazon S3 (with AWS KMS through Amazon S3 for encrypted buckets), and to describe the SageMaker HyperPod cluster.

`AmazonSageMakerHyperPodInferenceGatewayGlobalRoutingAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonSageMakerHyperPodInferenceGatewayGlobalRoutingAccess-how-to-use"></a>

You can attach `AmazonSageMakerHyperPodInferenceGatewayGlobalRoutingAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonSageMakerHyperPodInferenceGatewayGlobalRoutingAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 17, 2026, 23:17 UTC 
+ **Edited time:** November 17, 2026, 23:17 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonSageMakerHyperPodInferenceGatewayGlobalRoutingAccess`

## Policy version
<a name="AmazonSageMakerHyperPodInferenceGatewayGlobalRoutingAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonSageMakerHyperPodInferenceGatewayGlobalRoutingAccess-json"></a>

```json
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "CreateEndpointSvc",
      "Effect" : "Allow",
      "Action" : "ec2:CreateVpcEndpointServiceConfiguration",
      "Resource" : "arn:aws:ec2:*:*:vpc-endpoint-service/*",
      "Condition" : {
        "StringEquals" : {
          "aws:RequestTag/CreatedBy" : "HyperPodInference",
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        },
        "Null" : {
          "aws:RequestTag/HyperPodInferenceOwner" : "false"
        },
        "ForAllValues:StringEquals" : {
          "aws:TagKeys" : [
            "CreatedBy",
            "HyperPodInferenceOwner"
          ]
        }
      }
    },
    {
      "Sid" : "TagEndpointSvc",
      "Effect" : "Allow",
      "Action" : "ec2:CreateTags",
      "Resource" : "arn:aws:ec2:*:*:vpc-endpoint-service/*",
      "Condition" : {
        "StringEquals" : {
          "ec2:CreateAction" : "CreateVpcEndpointServiceConfiguration",
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        },
        "ForAllValues:StringEquals" : {
          "aws:TagKeys" : [
            "CreatedBy",
            "HyperPodInferenceOwner"
          ]
        },
        "Null" : {
          "aws:TagKeys" : "false"
        }
      }
    },
    {
      "Sid" : "DescribeNetwork",
      "Effect" : "Allow",
      "Action" : [
        "ec2:DescribeVpcEndpointServiceConfigurations",
        "ec2:DescribeVpcEndpointConnections",
        "ec2:DescribeVpcEndpointServices",
        "ec2:DescribeVpcEndpoints",
        "ec2:DescribeSecurityGroups",
        "ec2:DescribeSubnets",
        "ec2:DescribeVpcs",
        "ec2:DescribeRegions",
        "elasticloadbalancing:DescribeLoadBalancers",
        "elasticloadbalancing:DescribeTargetGroups",
        "elasticloadbalancing:DescribeTargetHealth"
      ],
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "DescribeSvcPerms",
      "Effect" : "Allow",
      "Action" : "ec2:DescribeVpcEndpointServicePermissions",
      "Resource" : "arn:aws:ec2:*:*:vpc-endpoint-service/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "ManageEndpointService",
      "Effect" : "Allow",
      "Action" : [
        "ec2:ModifyVpcEndpointServiceConfiguration",
        "ec2:ModifyVpcEndpointServicePermissions",
        "ec2:DeleteVpcEndpointServiceConfigurations"
      ],
      "Resource" : "arn:aws:ec2:*:*:vpc-endpoint-service/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceTag/CreatedBy" : "HyperPodInference",
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "AllowMultiRegion",
      "Effect" : "Allow",
      "Action" : "vpce:AllowMultiRegion",
      "Resource" : [
        "arn:aws:ec2:*:*:vpc-endpoint-service/*",
        "arn:aws:ec2:*:*:vpc-endpoint/*"
      ],
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "WriteGIGCert",
      "Effect" : "Allow",
      "Action" : "s3:PutObject",
      "Resource" : "arn:aws:s3:::hyperpod-tls*/*gig/*/*-certificate-*.pem",
      "Condition" : {
        "StringEquals" : {
          "s3:RequestObjectTag/CreatedBy" : "HyperPodInference",
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        },
        "ForAllValues:StringEquals" : {
          "s3:RequestObjectTagKeys" : [
            "CreatedBy"
          ]
        },
        "Null" : {
          "s3:RequestObjectTagKeys" : "false"
        }
      }
    },
    {
      "Sid" : "TagGIGCert",
      "Effect" : "Allow",
      "Action" : "s3:PutObjectTagging",
      "Resource" : "arn:aws:s3:::hyperpod-tls*/*gig/*/*-certificate-*.pem",
      "Condition" : {
        "StringEquals" : {
          "s3:RequestObjectTag/CreatedBy" : "HyperPodInference",
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        },
        "StringEqualsIfExists" : {
          "s3:ExistingObjectTag/CreatedBy" : "HyperPodInference"
        },
        "ForAllValues:StringEquals" : {
          "s3:RequestObjectTagKeys" : [
            "CreatedBy"
          ]
        },
        "Null" : {
          "s3:RequestObjectTagKeys" : "false"
        }
      }
    },
    {
      "Sid" : "EncryptGIGCert",
      "Effect" : "Allow",
      "Action" : "kms:GenerateDataKey",
      "Resource" : "arn:aws:kms:*:*:key/*",
      "Condition" : {
        "StringLike" : {
          "kms:ViaService" : "s3.*.amazonaws.com",
          "kms:EncryptionContext:aws:s3:arn" : "arn:aws:s3:::hyperpod-tls*"
        },
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "DeleteGIGCert",
      "Effect" : "Allow",
      "Action" : "s3:DeleteObject",
      "Resource" : "arn:aws:s3:::hyperpod-tls*/*gig/*/*-certificate-*.pem",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "DescribeCluster",
      "Effect" : "Allow",
      "Action" : "sagemaker:DescribeCluster",
      "Resource" : "arn:aws:sagemaker:*:*:cluster/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "CreateKinesisEndpoint",
      "Effect" : "Allow",
      "Action" : "ec2:CreateVpcEndpoint",
      "Resource" : "arn:aws:ec2:*:*:vpc-endpoint/*",
      "Condition" : {
        "StringEquals" : {
          "aws:RequestTag/CreatedBy" : "HyperPodInference",
          "aws:RequestTag/HyperPodInferenceComponent" : "metrics-publisher-kinesis-endpoint",
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        },
        "StringLike" : {
          "ec2:VpceServiceName" : "com.amazonaws.*.kinesis-streams"
        },
        "ForAllValues:StringEquals" : {
          "aws:TagKeys" : [
            "CreatedBy",
            "HyperPodInferenceOwner",
            "HyperPodInferenceComponent",
            "Name"
          ]
        },
        "Null" : {
          "aws:TagKeys" : "false"
        }
      }
    },
    {
      "Sid" : "CreateEndpointSG",
      "Effect" : "Allow",
      "Action" : "ec2:CreateSecurityGroup",
      "Resource" : "arn:aws:ec2:*:*:security-group/*",
      "Condition" : {
        "StringEquals" : {
          "aws:RequestTag/CreatedBy" : "HyperPodInference",
          "aws:RequestTag/HyperPodInferenceComponent" : "metrics-publisher-kinesis-endpoint",
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        },
        "ForAllValues:StringEquals" : {
          "aws:TagKeys" : [
            "CreatedBy",
            "HyperPodInferenceOwner",
            "HyperPodInferenceComponent",
            "Name"
          ]
        },
        "Null" : {
          "aws:TagKeys" : "false"
        }
      }
    },
    {
      "Sid" : "UseVpc",
      "Effect" : "Allow",
      "Action" : [
        "ec2:CreateVpcEndpoint",
        "ec2:ModifyVpcEndpoint"
      ],
      "Resource" : [
        "arn:aws:ec2:*:*:vpc/*",
        "arn:aws:ec2:*:*:subnet/*",
        "arn:aws:ec2:*:*:security-group/*"
      ],
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "UseVpcForSG",
      "Effect" : "Allow",
      "Action" : "ec2:CreateSecurityGroup",
      "Resource" : "arn:aws:ec2:*:*:vpc/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "TagKinesisEndpoint",
      "Effect" : "Allow",
      "Action" : "ec2:CreateTags",
      "Resource" : [
        "arn:aws:ec2:*:*:vpc-endpoint/*",
        "arn:aws:ec2:*:*:security-group/*"
      ],
      "Condition" : {
        "StringEquals" : {
          "ec2:CreateAction" : [
            "CreateVpcEndpoint",
            "CreateSecurityGroup"
          ],
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        },
        "ForAllValues:StringEquals" : {
          "aws:TagKeys" : [
            "CreatedBy",
            "HyperPodInferenceOwner",
            "HyperPodInferenceComponent",
            "Name"
          ]
        },
        "Null" : {
          "aws:TagKeys" : "false"
        }
      }
    },
    {
      "Sid" : "ManageKinesisEndpoint",
      "Effect" : "Allow",
      "Action" : [
        "ec2:DeleteVpcEndpoints",
        "ec2:ModifyVpcEndpoint",
        "ec2:AuthorizeSecurityGroupIngress",
        "ec2:DeleteSecurityGroup"
      ],
      "Resource" : [
        "arn:aws:ec2:*:*:vpc-endpoint/*",
        "arn:aws:ec2:*:*:security-group/*"
      ],
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceTag/CreatedBy" : "HyperPodInference",
          "aws:ResourceTag/HyperPodInferenceComponent" : "metrics-publisher-kinesis-endpoint",
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    }
  ]
}
```

## Learn more
<a name="AmazonSageMakerHyperPodInferenceGatewayGlobalRoutingAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)