

# Using agents for funding recommendations and fund requests
<a name="partner-funding-agent"></a>

AWS Partner Central agents analyze your opportunities against available funding programs and can create fund requests directly from the opportunity details page.

## Prerequisites
<a name="partner-funding-agent-prerequisites"></a>
+ Your account has migrated to AWS Partner Central in the AWS Management Console.
+ Your IAM user or role has the required permissions:
  + `partnercentral:ListBenefitAllocations`
  + `partnercentral:ListBenefitApplications`
  + `partnercentral:CreateBenefitApplication`
  + `partnercentral:GetBenefitApplication`
  + `partnercentral:UpdateBenefitApplication`
  + `partnercentral:AssociateBenefitApplicationResource`
  + `partnercentral:DisassociateBenefitApplicationResource`
  + `partnercentral:GetOpportunity`
  + `partnercentral:GetAwsOpporunitySummary`
  + `partnercentral:UseSession`
  + `aws-marketplace:DescribeEntity`
  + `aws-marketplace:SearchAgreements`
+ You have at least one active opportunity.

## How funding recommendations work
<a name="partner-funding-agent-how-it-works"></a>

When you open an opportunity details page, the **Funding Recommendation** widget automatically evaluates the opportunity against available AWS funding programs based on opportunity stage, expected revenue, customer use case, and partner path eligibility.

If a match is found, the widget displays the following information:


| Element | Description | 
| --- | --- | 
| Program name | The recommended funding program. | 
| Program description | A summary from AWS funding documentation. | 
| Reason for recommendation | Why this opportunity may qualify, based on stage, ARR, and use case. | 

**Note**  
Funding recommendations are provided for informational purposes to help identify potentially relevant programs. Recommendations do not guarantee funding approval or eligibility.

The widget provides three actions:


| Action | Description | 
| --- | --- | 
| Get estimated funding | Calculates potential funding based on opportunity value and program rules. | 
| Create fund request | Starts a draft fund request auto-populated with opportunity data. | 
| Learn about funding programs | Opens a conversational interface for funding questions. | 

If no match is found, the widget indicates this and offers a **Learn about funding programs** button.

When a recommended program is associated with a Standard Strategic Collaboration Agreement (SCA), the feature also displays SCA budget allocation information — what has been allocated and what remains available.

**Note**  
The agent does not access the SCA agreement document itself. SCA agreements are managed in Contract Central.

## Getting a funding recommendation
<a name="partner-funding-agent-get-recommendation"></a>

1. Navigate to **Opportunities** in the left navigation.

1. Select an opportunity.

1. Locate the **Funding Recommendation** widget on the opportunity details page.

1. Review the recommendation and choose an action.

You can also choose **Ask about this opportunity** and ask questions such as "What funding programs are available?" or "Why was this program recommended?"

## Creating a fund request
<a name="partner-funding-agent-create-request"></a>

1. In the **Funding Recommendation** widget, choose **Create fund request**.

1. The agent collects data from the opportunity record.

1. If information is missing, the agent asks clarifying questions in the chat interface.

1. The agent generates a draft and provides a link.

1. Open the link to review the draft in the AWS Funding portal, then submit.

After submission, the request follows the standard approval workflow. Track progress on the **Funding Dashboard**. For more information, see [Creating a fund request](create-fund-request.md).

You can also start this process through the chat interface by choosing **Ask about this opportunity** and typing "Create a fund request for this opportunity."

## Important considerations
<a name="partner-funding-agent-considerations"></a>


| Consideration | Details | 
| --- | --- | 
| Eligibility | Recommendations are based on available data. Final eligibility is determined during the application review. | 
| Data scope | The agent uses only your opportunity and partner account data. | 
| Permissions | Users without fund request permissions receive an access denied message. | 
| Sessions | Conversations are session-based, not persisted. Each interaction has a unique Session ID. | 

## Related resources
<a name="partner-funding-agent-related-resources"></a>
+ [Managing fund requests in AWS Partner Central](partner-funding.md)
+ [Creating a fund request](create-fund-request.md)
+ [AWS Partner Funding Benefits](https://docs.aws.amazon.com/partner-central/latest/getting-started/funding-benefits.html)