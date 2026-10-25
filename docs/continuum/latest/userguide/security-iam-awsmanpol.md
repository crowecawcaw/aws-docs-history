

# AWS managed policies for AWS Continuum
<a name="security-iam-awsmanpol"></a>

To add permissions to users, groups, and roles, it is easier to use AWS managed policies than to write policies yourself. It takes time and expertise to [create IAM customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) that provide your team with only the permissions they need. To get started quickly, you can use our AWS managed policies. These policies cover common use cases and are available in your AWS account. For more information about AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

AWS services maintain and update AWS managed policies. You can't change the permissions in AWS managed policies. Services occasionally add additional permissions to an AWS managed policy to support new features. This type of update affects all identities (users, groups, and roles) where the policy is attached. Services are most likely to update an AWS managed policy when a new feature is launched or when new operations become available. Services do not remove permissions from an AWS managed policy, so policy updates won't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple services. For example, the **ReadOnlyAccess** AWS managed policy provides read-only access to all AWS services and resources. When a service launches a new feature, AWS adds read-only permissions for new operations and resources. For a list and descriptions of job function policies, see [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.

## AWS managed policy: AWSContinuumCollectorServiceRolePolicy
<a name="security-iam-awsmanpol-AWSContinuumCollectorServiceRolePolicy"></a>

You can't attach `AWSContinuumCollectorServiceRolePolicy` to your IAM entities. This policy is attached to the `AWSServiceRoleForContinuumCollector` service-linked role that allows AWS Continuum to collect resource information and security findings and validate network reachability on your behalf. For more information, see [Using service-linked roles for AWS Continuum](using-service-linked-roles.md).

Several statements use `aws:ResourceAccount` conditions to require the resource account to match the calling principal's account. These conditions apply to the following permissions:
+ Lambda function and layer version reads
+ Access Analyzer findings
+ GuardDuty findings
+ ECR image metadata
+ WAFv2 resource associations
+ API Gateway metadata
+ Amazon EKS metadata reads
+ Network Insights create, start, tag, and delete actions
+ Tiros reachability queries
+ S3 bucket reads

GuardDuty uses `Resource: "*"` with the account condition.

IAM policy reads are limited to AWS managed policies under `arn:aws:iam::aws:policy/*`. The following statements use `Resource: "*"` without an `aws:ResourceAccount` condition:
+ Lambda event source mapping reads
+ Elastic Load Balancing metadata reads
+ Network Insights describe actions
+ Security service discovery and Amazon Inspector findings
+ S3 account public access reads

**Permissions details**

This policy includes the following permissions. AWS Continuum uses them to map your resources and their relationships and determine whether exposures are network-reachable in your environment.
+ Lambda allows AWS Continuum to read function information, function policies, aliases, versions, and function URL configurations (`lambda:GetFunction`, `lambda:GetPolicy`, `lambda:ListAliases`, `lambda:ListVersionsByFunction`, and `lambda:ListFunctionUrlConfigs`), read layer versions and their policies (`lambda:GetLayerVersion` and `lambda:GetLayerVersionPolicy`), and list event source mappings (`lambda:ListEventSourceMappings`).
+ IAM allows AWS Continuum to read AWS managed policy documents (`iam:GetPolicy` and `iam:GetPolicyVersion`).
+ IAM Access Analyzer allows AWS Continuum to list analyzers and findings (`access-analyzer:ListAnalyzers` and `access-analyzer:ListFindings`).
+ GuardDuty allows AWS Continuum to list and retrieve findings (`guardduty:ListFindings` and `guardduty:GetFindings`).
+ Amazon ECR allows AWS Continuum to read private image metadata (`ecr:DescribeImages`).
+ WAFv2 allows AWS Continuum to list resource associations for regional web ACLs and global web ACLs in `us-east-1` (`wafv2:ListResourcesForWebACL`).
+ API Gateway allows AWS Continuum to read REST API resources, stage exports, authorizers, custom domain names, base path mappings, API exports, routes, and API mappings on the specified resource paths (`apigateway:GET`).
+ Elastic Load Balancing allows AWS Continuum to read load balancer, listener, and target group attributes and target health (`elasticloadbalancing:DescribeLoadBalancerAttributes`, `elasticloadbalancing:DescribeListenerAttributes`, `elasticloadbalancing:DescribeTargetGroupAttributes`, and `elasticloadbalancing:DescribeTargetHealth`).
+ Amazon EKS allows AWS Continuum to list and describe Pod Identity associations and access entries and list associated access policies (`eks:ListPodIdentityAssociations`, `eks:DescribePodIdentityAssociation`, `eks:ListAccessEntries`, `eks:DescribeAccessEntry`, and `eks:ListAssociatedAccessPolicies`).

  These actions are limited to clusters, Pod Identity associations, and access entries in your account.
+ Amazon EC2 allows AWS Continuum to read Network Insights paths and analyses (`ec2:DescribeNetworkInsightsPaths` and `ec2:DescribeNetworkInsightsAnalyses`).
+ Amazon EC2 allows AWS Continuum to create Network Insights paths and start analyses (`ec2:CreateNetworkInsightsPath` and `ec2:StartNetworkInsightsAnalysis`).

  Creation requests must include `AWSContinuum=true` and may specify only the `AWSContinuum` tag key. To start an analysis, the path must have the `AWSContinuum=true` resource tag.
+ Amazon EC2 allows AWS Continuum to tag Network Insights paths and analyses during creation (`ec2:CreateTags`).

  Tagging is permitted only during `CreateNetworkInsightsPath` or `StartNetworkInsightsAnalysis`. Tagging requests must include `AWSContinuum=true` and may specify only the `AWSContinuum` tag key.
+ Amazon EC2 allows AWS Continuum to delete Network Insights paths and analyses (`ec2:DeleteNetworkInsightsPath` and `ec2:DeleteNetworkInsightsAnalysis`).

  The paths and analyses must have the `AWSContinuum=true` resource tag.
+ Tiros allows AWS Continuum to create reachability queries and retrieve their answers (`tiros:CreateQuery` and `tiros:GetQueryAnswer`).
+ Amazon Inspector allows AWS Continuum to list findings (`inspector2:ListFindings`).
+ Amazon S3 allows AWS Continuum to read account-level public access block settings (`s3:GetAccountPublicAccessBlock`) and bucket ACLs, locations, policy status, and public access block settings (`s3:GetBucketAcl`, `s3:GetBucketLocation`, `s3:GetBucketPolicyStatus`, and `s3:GetBucketPublicAccessBlock`).

For the complete policy JSON, see [Permissions policy](using-service-linked-roles.md#continuum-collector-permissions-policy).

To view the policy in the AWS Managed Policy Reference, see [AWSContinuumCollectorServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSContinuumCollectorServiceRolePolicy.html).

## AWS Continuum managed policy documentation updates
<a name="security-iam-awsmanpol-updates"></a>

The following table lists documentation updates for AWS Continuum managed policies. For alerts about guide updates, subscribe to the RSS feed on the [Document history for the AWS Continuum User Guide](doc-history.md) page.


| Change | Description | Date | 
| --- | --- | --- | 
| [AWSContinuumCollectorServiceRolePolicy documentation](#security-iam-awsmanpol-AWSContinuumCollectorServiceRolePolicy) | Updated the permissions documentation for `AWSServiceRoleForContinuumCollector`. The guide now includes the collector policy statements, resource scopes, and tag requirements. | October 13, 2026 | 