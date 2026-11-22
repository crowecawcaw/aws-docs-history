

# Granting agents access to partner reporting data

You can give AI agents and tools — such as the AWS Partner Central agent, Amazon Q, or your own Model Context Protocol (MCP) client — programmatic access to your AWS Partner Central reporting data. An agent acts with the permissions of the IAM identity that it signs in with. To grant access, attach an AWS Identity and Access Management (IAM) policy that allows the `partnercentral:GetPartnerReportingData` action to that identity: the user's role for console or OAuth sign-in, or the agent's own role for a custom agent. You can scope access to specific datasets (recommended) or to all datasets.

**Note**  
For AWS Marketplace seller datasets, see [Granting agents access to seller reporting data](https://docs.aws.amazon.com/marketplace/latest/userguide/agent-reporting-data-access.html).

## Agent access policies
<a name="agent-access-policies"></a>

If the IAM identity already has the `AWSPartnerCentralFullAccess` managed policy, that policy includes the partnercentral:GetPartnerReportingData action and you don't need an additional policy. To grant only this access, use one of the following policies.

You can grant an agent access to your reporting data in one of two ways:
+ **Specific datasets (recommended)** – Grants access only to the dataset ARNs that you specify. This approach follows the principle of least privilege.
+ **All current and future datasets** – Grants access using a wildcard resource. Use this approach only if the agent needs access to all datasets.

**Note**  
An explicit `Deny` in any other IAM policy, a service control policy (SCP), or a permissions boundary overrides these `Allow` statements.

**To grant an agent access to partner reporting data**

1. Decide whether to grant access to specific datasets (recommended) or to all current and future datasets.

1. Create an IAM policy using the appropriate example that follows. In the example, replace {{111122223333}} with your own AWS account ID.

1. Attach the policy to the agent's IAM identity (user, group, or role).

For information about finding your account ID, see [Your AWS account ID and its alias](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html) in the *AWS Identity and Access Management User Guide*. You can grant access only to reporting data in your own account. Cross-account access isn't supported.

After you attach the policy, the agent can call the partnercentral:GetPartnerReportingData action to retrieve the reporting data that you granted access to.

**Note**  
To remove access to a dataset later, delete that dataset's entry from the Resource array in the policy.

For more information about creating IAM policies, see [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *AWS Identity and Access Management (IAM) User Guide*.

### Example – Access to specific datasets
<a name="agent-access-specific-datasets"></a>

Use this policy because it grants access only to the datasets that you specify. This approach follows the principle of least privilege.

In each dataset ARN, the final Dataset/ segment matches the dashboard name. Include the ARN for each dashboard whose data the agent needs.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "partnercentral:GetPartnerReportingData"
            ],
            "Resource": [
                "arn:aws:partnercentral::{{111122223333}}:catalog/AWS/ReportingData/AttributedRevenue_V1/Dataset/AttributedRevenue_V1",
                "arn:aws:partnercentral::{{111122223333}}:catalog/AWS/ReportingData/Opportunity_V1/Dataset/OpportunityPipelineAnalysis_V1",
                "arn:aws:partnercentral::{{111122223333}}:catalog/AWS/ReportingData/TrainingAndCertification_V1/Dataset/TrainingAndCertifications_V1",
                "arn:aws:partnercentral::{{111122223333}}:catalog/AWS/ReportingData/Channel_V1/Dataset/ResellRevenueAndDiscounts_V1",
                "arn:aws:partnercentral::{{111122223333}}:catalog/AWS/ReportingData/Benefits_V1/Dataset/FundingAndInvestments_V1",
                "arn:aws:partnercentral::{{111122223333}}:catalog/AWS/ReportingData/Engagement_V1/Dataset/LeadPipelineAnalysis_V1",
                "arn:aws:partnercentral::{{111122223333}}:catalog/AWS/ReportingData/Engagement_V1/Dataset/MarketingCampaignAnalysis_V1",
                "arn:aws:partnercentral::{{111122223333}}:catalog/AWS/ReportingData/Aggregated/Dataset/AtAGlance_V1"
            ]
        }
    ]
}
```

This example grants access to the following datasets:
+ Attributed Revenue
+ Opportunity Pipeline Analysis
+ Training and Certifications
+ Resell Revenue and Discounts
+ Funding and Investments
+ Lead Pipeline Analysis
+ Marketing Campaign Analysis
+ At a Glance

**Note**  
The Attributed Revenue dataset currently returns no rows.

### Example – Access to all datasets
<a name="agent-access-all-datasets"></a>

This policy grants access to all current and future datasets by using a wildcard resource.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "partnercentral:GetPartnerReportingData"
            ],
            "Resource": [
                "arn:aws:partnercentral::{{111122223333}}:catalog/AWS/ReportingData/*/Dataset/*"
            ]
        }
    ]
}
```

**Important**  
Use the specific-datasets policy instead. The wildcard resource grants broader access than might be necessary.

## Troubleshooting access
<a name="troubleshooting-agent-reporting-access"></a>

If an agent's request is denied, the call appears in AWS CloudTrail with eventSource `partnercentral-analytics.amazonaws.com`, eventName `GetPartnerReportingData`, and errorCode `AccessDenied`. The agent's response names the missing permission and the ARN that it needs. To resolve the error, add that ARN to the `Resource` list in the policy, and then reattach the policy to the agent's IAM identity.