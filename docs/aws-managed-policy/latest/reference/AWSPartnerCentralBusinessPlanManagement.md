

# AWSPartnerCentralBusinessPlanManagement
<a name="AWSPartnerCentralBusinessPlanManagement"></a>

**Description**: Provides access to manage business plans and their attachments in AWS Partner Central, including read access to the Partner Central and AWS Marketplace reporting data behind business plan metrics

`AWSPartnerCentralBusinessPlanManagement` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSPartnerCentralBusinessPlanManagement-how-to-use"></a>

You can attach `AWSPartnerCentralBusinessPlanManagement` to your users, groups, and roles.

## Policy details
<a name="AWSPartnerCentralBusinessPlanManagement-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 10, 2026, 23:37 UTC 
+ **Edited time:** November 10, 2026, 23:37 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSPartnerCentralBusinessPlanManagement`

## Policy version
<a name="AWSPartnerCentralBusinessPlanManagement-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSPartnerCentralBusinessPlanManagement-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "BusinessPlanResourceAccess",
      "Effect" : "Allow",
      "Action" : [
        "partnercentral:GetBusinessPlan",
        "partnercentral:UpdateBusinessPlan",
        "partnercentral:CancelBusinessPlan",
        "partnercentral:ListBusinessPlanHistory",
        "partnercentral:CreateBusinessPlanItem",
        "partnercentral:GetBusinessPlanItem",
        "partnercentral:UpdateBusinessPlanItem",
        "partnercentral:DeleteBusinessPlanItem",
        "partnercentral:AssociateBusinessPlan",
        "partnercentral:DisassociateBusinessPlan",
        "partnercentral:StartBusinessPlanSubmissionTask",
        "partnercentral:CancelBusinessPlanSubmissionTask",
        "partnercentral:GetBusinessPlanSubmissionTask",
        "partnercentral:ListBusinessPlanSubmissionTasks",
        "partnercentral:StartBusinessPlanAttachmentImportTask",
        "partnercentral:GetBusinessPlanAttachmentImportTask",
        "partnercentral:ListBusinessPlanAttachmentImportTasks",
        "partnercentral:GetBusinessPlanAttachment",
        "partnercentral:ListBusinessPlanAttachments",
        "partnercentral:DeleteBusinessPlanAttachment",
        "partnercentral:TagResource",
        "partnercentral:UntagResource"
      ],
      "Resource" : "arn:aws:partnercentral:*:*:catalog/*/business-plan/*",
      "Condition" : {
        "StringEquals" : {
          "partnercentral:Catalog" : [
            "AWS",
            "Sandbox"
          ]
        }
      }
    },
    {
      "Sid" : "BusinessPlanAccountAccess",
      "Effect" : "Allow",
      "Action" : [
        "partnercentral:CreateBusinessPlan",
        "partnercentral:ListBusinessPlans",
        "partnercentral:ListBusinessPlanItems",
        "partnercentral:ListBusinessPlanAssociations",
        "partnercentral:GetBusinessPlanItemSchema",
        "partnercentral:GetBusinessPlanSettings",
        "partnercentral:PutBusinessPlanSettings"
      ],
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "partnercentral:Catalog" : [
            "AWS",
            "Sandbox"
          ]
        }
      }
    },
    {
      "Sid" : "PartnerReportingDataAccess",
      "Effect" : "Allow",
      "Action" : [
        "partnercentral:GetPartnerReportingData"
      ],
      "Resource" : [
        "arn:aws:partnercentral::*:catalog/AWS/ReportingData/Opportunity_V1/Dataset/OpportunityPipelineAnalysis_V1",
        "arn:aws:partnercentral::*:catalog/AWS/ReportingData/Channel_V1/Dataset/ResellRevenueAndDiscounts_V1",
        "arn:aws:partnercentral::*:catalog/AWS/ReportingData/Benefits_V1/Dataset/MapPartnerPerformanceIndex_V1",
        "arn:aws:partnercentral::*:catalog/AWS/ReportingData/AttributedRevenue_V1/Dataset/AttributedRevenue_V1",
        "arn:aws:partnercentral::*:catalog/AWS/ReportingData/PartnerCompetency_V1/Dataset/Competency_V1",
        "arn:aws:partnercentral::*:catalog/AWS/ReportingData/TrainingAndCertification_V1/Dataset/TrainingAndCertifications_V1"
      ]
    },
    {
      "Sid" : "SellerReportingDataAccess",
      "Effect" : "Allow",
      "Action" : [
        "aws-marketplace:GetSellerReportingData"
      ],
      "Resource" : [
        "arn:aws:aws-marketplace::*:AWSMarketplace/ReportingData/BillingEvent_V1/Dataset/BilledRevenue_V1",
        "arn:aws:aws-marketplace::*:AWSMarketplace/ReportingData/Solution_V1/Dataset/Solution_V1",
        "arn:aws:aws-marketplace::*:AWSMarketplace/ReportingData/Marketing_V1/Dataset/CaseStudy_V1"
      ]
    },
    {
      "Sid" : "PartnerCentralEphemeralWriteS3Access",
      "Effect" : "Allow",
      "Action" : [
        "s3:PutObject"
      ],
      "Resource" : "arn:aws:s3:::aws-partner-central-marketplace-ephemeral-writeonly-files/${aws:PrincipalAccount}/*"
    }
  ]
}
```

## Learn more
<a name="AWSPartnerCentralBusinessPlanManagement-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)