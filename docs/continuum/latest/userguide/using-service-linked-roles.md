

# Using service-linked roles for AWS Continuum
<a name="using-service-linked-roles"></a>

AWS Continuum uses AWS Identity and Access Management (IAM) [service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to AWS Continuum. Service-linked roles are predefined by AWS Continuum and include all the permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes setting up AWS Continuum easier because you don't have to manually add the necessary permissions. AWS Continuum defines the permissions of its service-linked roles, and unless defined otherwise, only AWS Continuum can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy can't be attached to any other IAM entity.

You can delete a service-linked role only after first deleting its related resources. This protects your AWS Continuum resources because you can't inadvertently remove permission to access the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and look for the services that have **Yes** in the **Service-linked role** column. Choose a **Yes** link to view the service-linked role documentation for that service.

**Topics**
+ [Service-linked role permissions for AWS Continuum](#slr-permissions)
+ [Creating a service-linked role for AWS Continuum](#create-slr)
+ [Editing a service-linked role for AWS Continuum](#edit-slr)
+ [Deleting a service-linked role for AWS Continuum](#delete-slr)

## Service-linked role permissions for AWS Continuum
<a name="slr-permissions"></a>

AWS Continuum uses the service-linked role named `AWSServiceRoleForContinuumCollector`. This role allows AWS Continuum to collect resource information and security findings and validate network reachability. The role trusts the `collector.continuum.amazonaws.com` service to assume the role.

**Important**  
Network Insights creation requests must include the `AWSContinuum=true` tag and may specify only the `AWSContinuum` tag key. Tagging is permitted only during path or analysis creation. The role can start analyses only on paths with this tag and delete only paths and analyses with this tag. These create, start, tag, and delete permissions require the resource account to match the calling principal's account.

The permissions policy for the role, named `AWSContinuumCollectorServiceRolePolicy`, allows AWS Continuum to perform the following tasks. Network Insights paths and analyses and Tiros reachability queries help AWS Continuum validate network reachability.
+ **Lambda** – Retrieve function information, policies, aliases, versions, and function URL configurations. Retrieve layer versions, their policies, and event source mappings.
+ **IAM** – Retrieve AWS managed policy documents and their versions.
+ **IAM Access Analyzer** – List analyzers and findings.
+ **GuardDuty** – List and retrieve findings in your account.
+ **Amazon Inspector** – List findings.
+ **Amazon ECR** – Retrieve metadata about private container images.
+ **WAFv2** – List resources associated with regional web ACLs and global web ACLs in `us-east-1`.
+ **API Gateway** – Retrieve API resource, export, authorizer, custom domain, route, and mapping metadata for the resource paths in the policy.
+ **Elastic Load Balancing** – Retrieve load balancer, listener, and target group attributes and target health.
+ **Amazon EKS** – List and describe Pod Identity associations and access entries and list associated access policies. These actions are limited to clusters, Pod Identity associations, and access entries in your account.
+ **Amazon EC2** – Retrieve information about Network Insights paths and analyses.
+ **Amazon EC2** – Create Network Insights paths and analyses and tag them with `AWSContinuum=true` during creation.
+ **Amazon EC2** – Start analyses on paths tagged `AWSContinuum=true`. Delete paths and analyses with this tag.
+ **Tiros** – Create reachability queries and retrieve their answers.
+ **Amazon S3** – Retrieve account-level public access block settings and bucket ACLs, locations, policy status, and public access block settings.

**Note**  
If you monitor API calls, you might see calls to Tiros APIs. Tiros is a service that is only accessible by AWS services and that surfaces network reachability findings to Reachability Analyzer. Calls to the Tiros endpoint are required for Reachability Analyzer to function. To access Reachability Analyzer, users must also have the same API permissions.

### Permissions policy
<a name="continuum-collector-permissions-policy"></a>

The role is configured with the following permissions policy.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "LambdaFunctionSupplementalMetadataRead",
      "Effect": "Allow",
      "Action": [
        "lambda:GetPolicy",
        "lambda:ListAliases",
        "lambda:ListVersionsByFunction",
        "lambda:ListFunctionUrlConfigs",
        "lambda:GetFunction"
      ],
      "Resource": "arn:aws:lambda:*:*:function:*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid": "LambdaLayerVersionSupplementalMetadataRead",
      "Effect": "Allow",
      "Action": [
        "lambda:GetLayerVersion",
        "lambda:GetLayerVersionPolicy"
      ],
      "Resource": "arn:aws:lambda:*:*:layer:*:*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid": "LambdaEventSourceMappingRead",
      "Effect": "Allow",
      "Action": "lambda:ListEventSourceMappings",
      "Resource": "*"
    },
    {
      "Sid": "IamAwsManagedPolicyDocumentRead",
      "Effect": "Allow",
      "Action": [
        "iam:GetPolicy",
        "iam:GetPolicyVersion"
      ],
      "Resource": "arn:aws:iam::aws:policy/*"
    },
    {
      "Sid": "AccessAnalyzerFindingsRead",
      "Effect": "Allow",
      "Action": "access-analyzer:ListFindings",
      "Resource": "arn:aws:access-analyzer:*:*:analyzer/*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid": "GuardDutyFindingsRead",
      "Effect": "Allow",
      "Action": [
        "guardduty:ListFindings",
        "guardduty:GetFindings"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid": "EcrPrivateImageMetadataRead",
      "Effect": "Allow",
      "Action": "ecr:DescribeImages",
      "Resource": "arn:aws:ecr:*:*:repository/*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid": "Wafv2ResourceAssociationRead",
      "Effect": "Allow",
      "Action": "wafv2:ListResourcesForWebACL",
      "Resource": [
        "arn:aws:wafv2:*:*:regional/webacl/*/*",
        "arn:aws:wafv2:us-east-1:*:global/webacl/*/*"
      ],
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid": "ApiGatewaySupplementalMetadataRead",
      "Effect": "Allow",
      "Action": "apigateway:GET",
      "Resource": [
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
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid": "Elbv2SupplementalMetadataRead",
      "Effect": "Allow",
      "Action": [
        "elasticloadbalancing:DescribeLoadBalancerAttributes",
        "elasticloadbalancing:DescribeListenerAttributes",
        "elasticloadbalancing:DescribeTargetGroupAttributes",
        "elasticloadbalancing:DescribeTargetHealth"
      ],
      "Resource": "*"
    },
    {
      "Sid": "EksSupplementalMetadataRead",
      "Effect": "Allow",
      "Action": [
        "eks:ListPodIdentityAssociations",
        "eks:DescribePodIdentityAssociation",
        "eks:ListAccessEntries",
        "eks:DescribeAccessEntry",
        "eks:ListAssociatedAccessPolicies"
      ],
      "Resource": [
        "arn:aws:eks:*:*:cluster/*",
        "arn:aws:eks:*:*:podidentityassociation/*",
        "arn:aws:eks:*:*:access-entry/*"
      ],
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid": "NetworkInsightsRead",
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeNetworkInsightsPaths",
        "ec2:DescribeNetworkInsightsAnalyses"
      ],
      "Resource": "*"
    },
    {
      "Sid": "CreateTaggedNetworkInsightsPath",
      "Effect": "Allow",
      "Action": "ec2:CreateNetworkInsightsPath",
      "Resource": "arn:aws:ec2:*:*:network-insights-path/*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "${aws:PrincipalAccount}",
          "aws:RequestTag/AWSContinuum": "true"
        },
        "ForAllValues:StringEquals": {
          "aws:TagKeys": "AWSContinuum"
        }
      }
    },
    {
      "Sid": "CreateTaggedNetworkInsightsAnalysis",
      "Effect": "Allow",
      "Action": "ec2:StartNetworkInsightsAnalysis",
      "Resource": "arn:aws:ec2:*:*:network-insights-analysis/*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "${aws:PrincipalAccount}",
          "aws:RequestTag/AWSContinuum": "true"
        },
        "ForAllValues:StringEquals": {
          "aws:TagKeys": "AWSContinuum"
        }
      }
    },
    {
      "Sid": "UseTaggedNetworkInsightsPath",
      "Effect": "Allow",
      "Action": "ec2:StartNetworkInsightsAnalysis",
      "Resource": "arn:aws:ec2:*:*:network-insights-path/*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "${aws:PrincipalAccount}",
          "aws:ResourceTag/AWSContinuum": "true"
        }
      }
    },
    {
      "Sid": "TagNetworkInsightsResourcesOnCreate",
      "Effect": "Allow",
      "Action": "ec2:CreateTags",
      "Resource": [
        "arn:aws:ec2:*:*:network-insights-path/*",
        "arn:aws:ec2:*:*:network-insights-analysis/*"
      ],
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "${aws:PrincipalAccount}",
          "aws:RequestTag/AWSContinuum": "true",
          "ec2:CreateAction": [
            "CreateNetworkInsightsPath",
            "StartNetworkInsightsAnalysis"
          ]
        },
        "ForAllValues:StringEquals": {
          "aws:TagKeys": "AWSContinuum"
        }
      }
    },
    {
      "Sid": "DeleteTaggedNetworkInsightsResources",
      "Effect": "Allow",
      "Action": [
        "ec2:DeleteNetworkInsightsAnalysis",
        "ec2:DeleteNetworkInsightsPath"
      ],
      "Resource": [
        "arn:aws:ec2:*:*:network-insights-path/*",
        "arn:aws:ec2:*:*:network-insights-analysis/*"
      ],
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "${aws:PrincipalAccount}",
          "aws:ResourceTag/AWSContinuum": "true"
        }
      }
    },
    {
      "Sid": "TirosQueryRead",
      "Effect": "Allow",
      "Action": [
        "tiros:CreateQuery",
        "tiros:GetQueryAnswer"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid": "SecurityServiceDiscoveryAndFindings",
      "Effect": "Allow",
      "Action": [
        "access-analyzer:ListAnalyzers",
        "inspector2:ListFindings"
      ],
      "Resource": "*"
    },
    {
      "Sid": "S3AccountPublicAccessRead",
      "Effect": "Allow",
      "Action": "s3:GetAccountPublicAccessBlock",
      "Resource": "*"
    },
    {
      "Sid": "S3BucketExposureRead",
      "Effect": "Allow",
      "Action": [
        "s3:GetBucketAcl",
        "s3:GetBucketLocation",
        "s3:GetBucketPolicyStatus",
        "s3:GetBucketPublicAccessBlock"
      ],
      "Resource": "arn:aws:s3:::*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "${aws:PrincipalAccount}"
        }
      }
    }
  ]
}
```

You must configure permissions to allow your users, groups, or roles to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

## Creating a service-linked role for AWS Continuum
<a name="create-slr"></a>

You can use the IAM console, the AWS CLI, or the AWS API to create `AWSServiceRoleForContinuumCollector`. In the AWS CLI or the AWS API, specify `collector.continuum.amazonaws.com` as the service name.

For instructions, see [Creating a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role) in the *IAM User Guide*.

## Editing a service-linked role for AWS Continuum
<a name="edit-slr"></a>

AWS Continuum does not allow you to edit the `AWSServiceRoleForContinuumCollector` service-linked role. After you create a service-linked role, you can't change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

## Deleting a service-linked role for AWS Continuum
<a name="delete-slr"></a>

You can use the IAM console, the AWS CLI, or the AWS API to delete `AWSServiceRoleForContinuumCollector`. For instructions on preparing the role for deletion, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

**Note**  
If AWS Continuum is using the role, deletion might fail. Wait a few minutes and try again.