

# AmazonBedrockAgentCoreMemoryBedrockModelInferenceExecutionRolePolicy
<a name="AmazonBedrockAgentCoreMemoryBedrockModelInferenceExecutionRolePolicy"></a>

**Description**: Provides Bedrock Model inference permission to Bedrock agent core memory

`AmazonBedrockAgentCoreMemoryBedrockModelInferenceExecutionRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonBedrockAgentCoreMemoryBedrockModelInferenceExecutionRolePolicy-how-to-use"></a>

You can attach `AmazonBedrockAgentCoreMemoryBedrockModelInferenceExecutionRolePolicy` to your users, groups, and roles.

## Policy details
<a name="AmazonBedrockAgentCoreMemoryBedrockModelInferenceExecutionRolePolicy-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: July 16, 2025, 13:37 UTC 
+ **Edited time:** July 17, 2026, 17:12 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonBedrockAgentCoreMemoryBedrockModelInferenceExecutionRolePolicy`

## Policy version
<a name="AmazonBedrockAgentCoreMemoryBedrockModelInferenceExecutionRolePolicy-version"></a>

**Policy version:** v4 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonBedrockAgentCoreMemoryBedrockModelInferenceExecutionRolePolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "BedrockInvokeModel",
      "Effect" : "Allow",
      "Action" : [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream"
      ],
      "Resource" : [
        "arn:aws:bedrock:*::foundation-model/*",
        "arn:aws:bedrock:*:*:inference-profile/*"
      ],
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "BedrockMantleInference",
      "Effect" : "Allow",
      "Action" : "bedrock-mantle:CreateInference",
      "Resource" : "arn:aws:bedrock-mantle:*:*:project/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "BedrockMantleCallWithBearerToken",
      "Effect" : "Allow",
      "Action" : "bedrock-mantle:CallWithBearerToken",
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonBedrockAgentCoreMemoryBedrockModelInferenceExecutionRolePolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)