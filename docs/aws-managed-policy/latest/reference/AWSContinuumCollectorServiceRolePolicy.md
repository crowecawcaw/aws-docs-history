

# AWSContinuumCollectorServiceRolePolicy
<a name="AWSContinuumCollectorServiceRolePolicy"></a>

**Description**: Grants Amazon Continuum access to AWS services for discovering and reading configuration, assessing network reachability and security posture data in your account.

`AWSContinuumCollectorServiceRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSContinuumCollectorServiceRolePolicy-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="AWSContinuumCollectorServiceRolePolicy-details"></a>
+ **Type**: Service-linked role policy 
+ **Creation time**: October 16, 2026, 01:07 UTC 
+ **Edited time:** October 16, 2026, 01:07 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/AWSContinuumCollectorServiceRolePolicy`

## Policy version
<a name="AWSContinuumCollectorServiceRolePolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSContinuumCollectorServiceRolePolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "LambdaFunctionSupplementalMetadataRead",
      "Effect" : "Allow",
      "Action" : [
        "lambda:GetPolicy",
        "lambda:ListAliases",
        "lambda:ListVersionsByFunction",
        "lambda:ListFunctionUrlConfigs",
        "lambda:GetFunction"
      ],
      "Resource" : "arn:aws:lambda:*:*:function:*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "LambdaLayerVersionSupplementalMetadataRead",
      "Effect" : "Allow",
      "Action" : [
        "lambda:GetLayerVersion",
        "lambda:GetLayerVersionPolicy"
      ],
      "Resource" : "arn:aws:lambda:*:*:layer:*:*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "LambdaEventSourceMappingRead",
      "Effect" : "Allow",
      "Action" : "lambda:ListEventSourceMappings",
      "Resource" : "*"
    },
    {
      "Sid" : "IamAwsManagedPolicyDocumentRead",
      "Effect" : "Allow",
      "Action" : [
        "iam:GetPolicy",
        "iam:GetPolicyVersion"
      ],
      "Resource" : "arn:aws:iam::aws:policy/*"
    },
    {
      "Sid" : "AccessAnalyzerFindingsRead",
      "Effect" : "Allow",
      "Action" : "access-analyzer:ListFindings",
      "Resource" : "arn:aws:access-analyzer:*:*:analyzer/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "GuardDutyFindingsRead",
      "Effect" : "Allow",
      "Action" : [
        "guardduty:ListFindings",
        "guardduty:GetFindings"
      ],
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "EcrPrivateImageMetadataRead",
      "Effect" : "Allow",
      "Action" : "ecr:DescribeImages",
      "Resource" : "arn:aws:ecr:*:*:repository/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "Wafv2ResourceAssociationRead",
      "Effect" : "Allow",
      "Action" : "wafv2:ListResourcesForWebACL",
      "Resource" : [
        "arn:aws:wafv2:*:*:regional/webacl/*/*",
        "arn:aws:wafv2:us-east-1:*:global/webacl/*/*"
      ],
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "ApiGatewaySupplementalMetadataRead",
      "Effect" : "Allow",
      "Action" : "apigateway:GET",
      "Resource" : [
        "arn:aws:apigateway:*::/restapis/*/resources",
        "arn:aws:apigateway:*::/restapis/*/stages/*/exports/*",
        "arn:aws:apigateway:*::/restapis/*/authorizers",
        "arn:aws:apigateway:*::/domainnames",
        "arn:aws:apigateway:*::/domainnames/*/basepathmappings",
        "arn:aws:apigateway:*::/apis/*/exports/*",
        "arn:aws:apigateway:*::/apis/*/routes",
        "arn:aws:apigateway:*::/apis/*/authorizers",
        "arn:aws:apigateway:*::/domainnames/*/apimappings"
      ],
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "Elbv2SupplementalMetadataRead",
      "Effect" : "Allow",
      "Action" : [
        "elasticloadbalancing:DescribeLoadBalancerAttributes",
        "elasticloadbalancing:DescribeListenerAttributes",
        "elasticloadbalancing:DescribeTargetGroupAttributes",
        "elasticloadbalancing:DescribeTargetHealth"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "EksSupplementalMetadataRead",
      "Effect" : "Allow",
      "Action" : [
        "eks:ListPodIdentityAssociations",
        "eks:DescribePodIdentityAssociation",
        "eks:ListAccessEntries",
        "eks:DescribeAccessEntry",
        "eks:ListAssociatedAccessPolicies"
      ],
      "Resource" : [
        "arn:aws:eks:*:*:cluster/*",
        "arn:aws:eks:*:*:podidentityassociation/*",
        "arn:aws:eks:*:*:access-entry/*"
      ],
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "NetworkInsightsRead",
      "Effect" : "Allow",
      "Action" : [
        "ec2:DescribeNetworkInsightsPaths",
        "ec2:DescribeNetworkInsightsAnalyses"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "CreateTaggedNetworkInsightsPath",
      "Effect" : "Allow",
      "Action" : "ec2:CreateNetworkInsightsPath",
      "Resource" : "arn:aws:ec2:*:*:network-insights-path/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}",
          "aws:RequestTag/AWSContinuum" : "true"
        },
        "ForAllValues:StringEquals" : {
          "aws:TagKeys" : "AWSContinuum"
        }
      }
    },
    {
      "Sid" : "CreateTaggedNetworkInsightsAnalysis",
      "Effect" : "Allow",
      "Action" : "ec2:StartNetworkInsightsAnalysis",
      "Resource" : "arn:aws:ec2:*:*:network-insights-analysis/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}",
          "aws:RequestTag/AWSContinuum" : "true"
        },
        "ForAllValues:StringEquals" : {
          "aws:TagKeys" : "AWSContinuum"
        }
      }
    },
    {
      "Sid" : "UseTaggedNetworkInsightsPath",
      "Effect" : "Allow",
      "Action" : "ec2:StartNetworkInsightsAnalysis",
      "Resource" : "arn:aws:ec2:*:*:network-insights-path/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}",
          "aws:ResourceTag/AWSContinuum" : "true"
        }
      }
    },
    {
      "Sid" : "TagNetworkInsightsResourcesOnCreate",
      "Effect" : "Allow",
      "Action" : "ec2:CreateTags",
      "Resource" : [
        "arn:aws:ec2:*:*:network-insights-path/*",
        "arn:aws:ec2:*:*:network-insights-analysis/*"
      ],
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}",
          "aws:RequestTag/AWSContinuum" : "true",
          "ec2:CreateAction" : [
            "CreateNetworkInsightsPath",
            "StartNetworkInsightsAnalysis"
          ]
        },
        "ForAllValues:StringEquals" : {
          "aws:TagKeys" : "AWSContinuum"
        }
      }
    },
    {
      "Sid" : "DeleteTaggedNetworkInsightsResources",
      "Effect" : "Allow",
      "Action" : [
        "ec2:DeleteNetworkInsightsAnalysis",
        "ec2:DeleteNetworkInsightsPath"
      ],
      "Resource" : [
        "arn:aws:ec2:*:*:network-insights-path/*",
        "arn:aws:ec2:*:*:network-insights-analysis/*"
      ],
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}",
          "aws:ResourceTag/AWSContinuum" : "true"
        }
      }
    },
    {
      "Sid" : "TirosQueryRead",
      "Effect" : "Allow",
      "Action" : [
        "tiros:CreateQuery",
        "tiros:GetQueryAnswer"
      ],
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "SecurityServiceDiscoveryAndFindings",
      "Effect" : "Allow",
      "Action" : [
        "access-analyzer:ListAnalyzers",
        "inspector2:ListFindings"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "S3AccountPublicAccessRead",
      "Effect" : "Allow",
      "Action" : "s3:GetAccountPublicAccessBlock",
      "Resource" : "*"
    },
    {
      "Sid" : "S3BucketExposureRead",
      "Effect" : "Allow",
      "Action" : [
        "s3:GetBucketAcl",
        "s3:GetBucketLocation",
        "s3:GetBucketPolicyStatus",
        "s3:GetBucketPublicAccessBlock"
      ],
      "Resource" : "arn:aws:s3:::*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    }
  ]
}
```

## Learn more
<a name="AWSContinuumCollectorServiceRolePolicy-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)