

# Mapping legacy Partner Central roles to AWS IAM
<a name="legacy-role-mappings"></a>

If you are migrating to the new experience, use the following table to map your existing users to AWS IAM managed policies. These mappings are included by default in the user export available within the Migration tool in the legacy AWS Partner Central experience. For more information about each managed policy, see [AWS managed policies for AWS Partner Central users](https://docs.aws.amazon.com/partner-central/latest/getting-started/security-iam-awsmanpol.html).


| Legacy User Role | Recommended Mapping | Notes | 
| --- | --- | --- | 
| Alliance lead |  +  `AWSPartnerCentralFullAccess` <br />+  `AWSMarketplaceSellerFullAccess`   | You need both policies to match previous Alliance lead permissions. If you don't need full access to AWS Marketplace, use `AWSMarketplaceSellerProductsFullAccess` instead. | 
| Alliance team member |  +  `AWSPartnerCentralFullAccess` <br />+  `AWSMarketplaceSellerFullAccess`   | Extension of Alliance lead with same permissions. | 
| ACE Manager | `AWSPartnerCentralOpportunityManagement` | Grants access to the full opportunity pipeline. | 
| ACE User | `AWSPartnerCentralOpportunityManagement` | IAM doesn't support restricting visibility to a single opportunity owner. This policy grants you edit access to all opportunities in the pipeline. To restrict access to only your own opportunities, contact APN Support. | 
| Technical Staff |  +  `AWSPartnerCentralFullAccess` <br />+  `AWSMarketplaceSellerProductsFullAccess`   | You need `AWSPartnerCentralFullAccess` to manage APN program applications. You need both policies to manage Foundational Technical Review submissions. | 
| Marketing Staff | `AWSPartnerCentralMarketingManagement` | Add `AWSPartnerCentralIncentiveBenefitManagement` only if this user also manages MDF or funding allocation. | 
| Cloud admin | `AdministratorAccess` or `IAMFullAccess` | No AWS Partner Central specific managed policy required. As a Cloud admin, you manage AWS IAM and should have administrator rights to the AWS account. | 
| Standard user | None | As a Standard user, you no longer need access to AWS Partner Central to attribute your Skill Builder certifications to your AWS Partner Central scorecard. For more information, see [AWS Skill Builder Access](https://partnercentral.awspartner.com/partnercentral2/s/article?category=Introductory_resources&article=Partner-Central-Migration-Guide#Major-Changes) on the Partner Central website. | 
| Channel user |  +  `AWSPartnerCentralChannelManagement` <br />+  `AWSPartnerCentralChannelHandshakeApprovalManagement`   | These policies do not include access to deal registration functionality. To enable deal registration access, attach `AWSPartnerCentralFullAccess`. | 

**Legacy ACE User permission changes**  
In the legacy experience, as an ACE User, you could only see and edit opportunities where you were assigned as the Opportunity Owner. The new experience doesn't have a direct equivalent — the closest policy (`AWSPartnerCentralOpportunityManagement`) grants access to all opportunities in your pipeline, not only ones that you own. If you need to restrict access to only your own opportunities, contact APN Support for assistance.