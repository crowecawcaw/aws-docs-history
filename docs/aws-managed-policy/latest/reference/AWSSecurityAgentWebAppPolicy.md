

# AWSSecurityAgentWebAppPolicy
<a name="AWSSecurityAgentWebAppPolicy"></a>

**Description**: Provides permissions for authenticated users to access the Security Agent Web Application for configuring and executing automated security penetration tests. This policy enables users to manage pentests, view findings, monitor test execution, and interact with AWS resources required for security testing operations.

`AWSSecurityAgentWebAppPolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSSecurityAgentWebAppPolicy-how-to-use"></a>

You can attach `AWSSecurityAgentWebAppPolicy` to your users, groups, and roles.

## Policy details
<a name="AWSSecurityAgentWebAppPolicy-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: February 05, 2026, 23:19 UTC 
+ **Edited time:** June 11, 2026, 18:27 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AWSSecurityAgentWebAppPolicy`

## Policy version
<a name="AWSSecurityAgentWebAppPolicy-version"></a>

**Policy version:** v6 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSSecurityAgentWebAppPolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "ApplicationAccess",
      "Effect" : "Allow",
      "Action" : [
        "securityagent:ListAgentSpaces",
        "securityagent:ListSecurityRequirements",
        "securityagent:ListTargetDomains",
        "securityagent:BatchGetTargetDomains"
      ],
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "AgentSpaceAccess",
      "Effect" : "Allow",
      "Action" : [
        "securityagent:AddArtifact",
        "securityagent:CreateThreat",
        "securityagent:BatchDeleteCodeReviews",
        "securityagent:BatchDeletePentests",
        "securityagent:BatchDeleteThreatModels",
        "securityagent:BatchGetAgentSpaces",
        "securityagent:BatchGetArtifactMetadata",
        "securityagent:BatchGetCodeReviewJobs",
        "securityagent:BatchGetCodeReviewJobTasks",
        "securityagent:BatchGetCodeReviews",
        "securityagent:BatchGetFindings",
        "securityagent:BatchGetPentestJobContentMetadata",
        "securityagent:BatchGetPentestJobs",
        "securityagent:BatchGetPentestJobTasks",
        "securityagent:BatchGetPentests",
        "securityagent:BatchGetThreatModelJobs",
        "securityagent:BatchGetThreatModelJobTasks",
        "securityagent:BatchGetThreatModels",
        "securityagent:BatchGetThreats",
        "securityagent:CreateCodeReview",
        "securityagent:CreateDesignReview",
        "securityagent:CreatePentest",
        "securityagent:CreateThreatModel",
        "securityagent:DeleteArtifact",
        "securityagent:DeleteDesignReview",
        "securityagent:GetArtifact",
        "securityagent:GetDesignReview",
        "securityagent:GetDesignReviewArtifact",
        "securityagent:GetDesignReviewFeedback",
        "securityagent:ListArtifacts",
        "securityagent:ListCodeReviewJobsForCodeReview",
        "securityagent:ListCodeReviewJobTasks",
        "securityagent:ListCodeReviews",
        "securityagent:ListDesignReviewComments",
        "securityagent:ListDesignReviews",
        "securityagent:ListDiscoveredEndpoints",
        "securityagent:ListFindings",
        "securityagent:ListIntegratedResources",
        "securityagent:ListPentestJobsForPentest",
        "securityagent:ListPentestJobTasks",
        "securityagent:ListPentests",
        "securityagent:ListThreatModelJobs",
        "securityagent:ListThreatModelJobTasks",
        "securityagent:ListThreatModels",
        "securityagent:ListThreats",
        "securityagent:PutDesignReviewFeedback",
        "securityagent:StartCodeRemediation",
        "securityagent:StartCodeReviewJob",
        "securityagent:StartPentestJob",
        "securityagent:StartThreatModelJob",
        "securityagent:StopCodeReviewJob",
        "securityagent:StopPentestJob",
        "securityagent:StopThreatModelJob",
        "securityagent:UpdateCodeReview",
        "securityagent:UpdateFinding",
        "securityagent:UpdatePentest",
        "securityagent:UpdateThreat",
        "securityagent:UpdateThreatModel"
      ],
      "Resource" : "arn:aws:securityagent:*:*:agent-space*",
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
<a name="AWSSecurityAgentWebAppPolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)