

# Actions, resources, and condition keys for AWS Partner Central
<a name="list_partner-central"></a>

AWS Partner Central (service prefix: `partnercentral`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/partner-central/latest/getting-started/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/partner-central/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/partner-central/latest/APIReference/access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/partnercentral/partnercentral.json) for this service.

**Topics**
+ [API operations defined by AWS Partner Central](#list_partner-central-operations)
+ [Actions defined by AWS Partner Central](#list_partner-central-actions-as-permissions)
+ [Permission-only actions for AWS Partner Central](#list_partner-central-permission-only-actions)
+ [Resource types defined by AWS Partner Central](#list_partner-central-resources-for-iam-policies)
+ [Condition keys for AWS Partner Central](#list_partner-central-policy-keys)

## API operations defined by AWS Partner Central
<a name="list_partner-central-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_partner-central-actions-as-permissions).




- **   AcceptConnectionInvitation  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:AcceptConnectionInvitation](#list_partner-central-action-AcceptConnectionInvitation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateAwsTrainingCertificationEmailDomain  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:AssociateAwsTrainingCertificationEmailDomain](#list_partner-central-action-AssociateAwsTrainingCertificationEmailDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelConnection  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:CancelConnection](#list_partner-central-action-CancelConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelConnectionInvitation  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:CancelConnectionInvitation](#list_partner-central-action-CancelConnectionInvitation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelProfileUpdateTask  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:CancelProfileUpdateTask](#list_partner-central-action-CancelProfileUpdateTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateConnectionInvitation  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:CreateConnectionInvitation](#list_partner-central-action-CreateConnectionInvitation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreatePartner  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:CreatePartner](#list_partner-central-action-CreatePartner)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [partnercentral:TagResource](#list_partner-central-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DisassociateAwsTrainingCertificationEmailDomain  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:DisassociateAwsTrainingCertificationEmailDomain](#list_partner-central-action-DisassociateAwsTrainingCertificationEmailDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAllianceLeadContact  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:GetAllianceLeadContact](#list_partner-central-action-GetAllianceLeadContact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConnection  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:GetConnection](#list_partner-central-action-GetConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConnectionInvitation  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:GetConnectionInvitation](#list_partner-central-action-GetConnectionInvitation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConnectionPreferences  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:GetConnectionPreferences](#list_partner-central-action-GetConnectionPreferences) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPartner  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:GetPartner](#list_partner-central-action-GetPartner) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProfileUpdateTask  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:GetProfileUpdateTask](#list_partner-central-action-GetProfileUpdateTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProfileVisibility  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:GetProfileVisibility](#list_partner-central-action-GetProfileVisibility) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQualificationsAssociationDetails  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:GetQualificationsAssociationDetails](#list_partner-central-action-GetQualificationsAssociationDetails) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQualificationsAssociationTask  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:GetQualificationsAssociationTask](#list_partner-central-action-GetQualificationsAssociationTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQualificationsDisassociationTask  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:GetQualificationsDisassociationTask](#list_partner-central-action-GetQualificationsDisassociationTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetVerification  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:GetVerification](#list_partner-central-action-GetVerification) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListConnectionInvitations  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:ListConnectionInvitations](#list_partner-central-action-ListConnectionInvitations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConnections  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:ListConnections](#list_partner-central-action-ListConnections) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPartners  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:ListPartners](#list_partner-central-action-ListPartners) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:ListTagsForResource](#list_partner-central-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutAllianceLeadContact  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:PutAllianceLeadContact](#list_partner-central-action-PutAllianceLeadContact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutProfileVisibility  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:PutProfileVisibility](#list_partner-central-action-PutProfileVisibility) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RejectConnectionInvitation  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:RejectConnectionInvitation](#list_partner-central-action-RejectConnectionInvitation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendEmailVerificationCode  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:SendEmailVerificationCode](#list_partner-central-action-SendEmailVerificationCode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartProfileUpdateTask  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:StartProfileUpdateTask](#list_partner-central-action-StartProfileUpdateTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartQualificationsAssociationTask  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:StartQualificationsAssociationTask](#list_partner-central-action-StartQualificationsAssociationTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartQualificationsDisassociationTask  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:StartQualificationsDisassociationTask](#list_partner-central-action-StartQualificationsDisassociationTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartVerification  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:StartVerification](#list_partner-central-action-StartVerification) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:TagResource](#list_partner-central-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:UntagResource](#list_partner-central-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateConnectionPreferences  **
  - **SDK client:** partnercentral-account
  - **IAM action:**  [partnercentral:UpdateConnectionPreferences](#list_partner-central-action-UpdateConnectionPreferences) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AmendBenefitApplication  **
  - **SDK client:** partnercentral-benefits
  - **IAM action:**  [partnercentral:AmendBenefitApplication](#list_partner-central-action-AmendBenefitApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateBenefitApplicationResource  **
  - **SDK client:** partnercentral-benefits
  - **IAM action:**  [partnercentral:AssociateBenefitApplicationResource](#list_partner-central-action-AssociateBenefitApplicationResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelBenefitApplication  **
  - **SDK client:** partnercentral-benefits
  - **IAM action:**  [partnercentral:CancelBenefitApplication](#list_partner-central-action-CancelBenefitApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateBenefitApplication  **
  - **SDK client:** partnercentral-benefits
  - **IAM action:**  [partnercentral:CreateBenefitApplication](#list_partner-central-action-CreateBenefitApplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [partnercentral:TagResource](#list_partner-central-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DisassociateBenefitApplicationResource  **
  - **SDK client:** partnercentral-benefits
  - **IAM action:**  [partnercentral:DisassociateBenefitApplicationResource](#list_partner-central-action-DisassociateBenefitApplicationResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetBenefit  **
  - **SDK client:** partnercentral-benefits
  - **IAM action:**  [partnercentral:GetBenefit](#list_partner-central-action-GetBenefit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBenefitAllocation  **
  - **SDK client:** partnercentral-benefits
  - **IAM action:**  [partnercentral:GetBenefitAllocation](#list_partner-central-action-GetBenefitAllocation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBenefitApplication  **
  - **SDK client:** partnercentral-benefits
  - **IAM action:**  [partnercentral:GetBenefitApplication](#list_partner-central-action-GetBenefitApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListBenefitAllocations  **
  - **SDK client:** partnercentral-benefits
  - **IAM action:**  [partnercentral:ListBenefitAllocations](#list_partner-central-action-ListBenefitAllocations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBenefitApplications  **
  - **SDK client:** partnercentral-benefits
  - **IAM action:**  [partnercentral:ListBenefitApplications](#list_partner-central-action-ListBenefitApplications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBenefits  **
  - **SDK client:** partnercentral-benefits
  - **IAM action:**  [partnercentral:ListBenefits](#list_partner-central-action-ListBenefits) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** partnercentral-benefits
  - **IAM action:**  [partnercentral:ListTagsForResource](#list_partner-central-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   RecallBenefitApplication  **
  - **SDK client:** partnercentral-benefits
  - **IAM action:**  [partnercentral:RecallBenefitApplication](#list_partner-central-action-RecallBenefitApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SubmitBenefitApplication  **
  - **SDK client:** partnercentral-benefits
  - **IAM action:**  [partnercentral:SubmitBenefitApplication](#list_partner-central-action-SubmitBenefitApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** partnercentral-benefits
  - **IAM action:**  [partnercentral:TagResource](#list_partner-central-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** partnercentral-benefits
  - **IAM action:**  [partnercentral:UntagResource](#list_partner-central-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateBenefitApplication  **
  - **SDK client:** partnercentral-benefits
  - **IAM action:**  [partnercentral:UpdateBenefitApplication](#list_partner-central-action-UpdateBenefitApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AcceptChannelHandshake  **
  - **SDK client:** partnercentral-channel
  - **IAM action:**  [partnercentral:AcceptChannelHandshake](#list_partner-central-action-AcceptChannelHandshake) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelChannelHandshake  **
  - **SDK client:** partnercentral-channel
  - **IAM action:**  [partnercentral:CancelChannelHandshake](#list_partner-central-action-CancelChannelHandshake) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateChannelHandshake  **
  - **SDK client:** partnercentral-channel
  - **IAM action:**  [partnercentral:CreateChannelHandshake](#list_partner-central-action-CreateChannelHandshake)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [partnercentral:GetProgramManagementAccount](#list_partner-central-action-GetProgramManagementAccount)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [partnercentral:GetRelationship](#list_partner-central-action-GetRelationship)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [partnercentral:TagResource](#list_partner-central-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateProgramManagementAccount  **
  - **SDK client:** partnercentral-channel
  - **IAM action:**  [partnercentral:CreateProgramManagementAccount](#list_partner-central-action-CreateProgramManagementAccount)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [partnercentral:TagResource](#list_partner-central-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRelationship  **
  - **SDK client:** partnercentral-channel
  - **IAM action:**  [partnercentral:CreateRelationship](#list_partner-central-action-CreateRelationship)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [partnercentral:GetProgramManagementAccount](#list_partner-central-action-GetProgramManagementAccount)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [partnercentral:TagResource](#list_partner-central-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteProgramManagementAccount  **
  - **SDK client:** partnercentral-channel
  - **IAM action:**  [partnercentral:DeleteProgramManagementAccount](#list_partner-central-action-DeleteProgramManagementAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRelationship  **
  - **SDK client:** partnercentral-channel
  - **IAM action:**  [partnercentral:DeleteRelationship](#list_partner-central-action-DeleteRelationship) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetRelationship  **
  - **SDK client:** partnercentral-channel
  - **IAM action:**  [partnercentral:GetRelationship](#list_partner-central-action-GetRelationship) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListChannelHandshakes  **
  - **SDK client:** partnercentral-channel
  - **IAM action:**  [partnercentral:ListChannelHandshakes](#list_partner-central-action-ListChannelHandshakes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProgramManagementAccounts  **
  - **SDK client:** partnercentral-channel
  - **IAM action:**  [partnercentral:ListProgramManagementAccounts](#list_partner-central-action-ListProgramManagementAccounts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRelationships  **
  - **SDK client:** partnercentral-channel
  - **IAM action:**  [partnercentral:ListRelationships](#list_partner-central-action-ListRelationships) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** partnercentral-channel
  - **IAM action:**  [partnercentral:ListTagsForResource](#list_partner-central-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   RejectChannelHandshake  **
  - **SDK client:** partnercentral-channel
  - **IAM action:**  [partnercentral:RejectChannelHandshake](#list_partner-central-action-RejectChannelHandshake) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** partnercentral-channel
  - **IAM action:**  [partnercentral:TagResource](#list_partner-central-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** partnercentral-channel
  - **IAM action:**  [partnercentral:UntagResource](#list_partner-central-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateProgramManagementAccount  **
  - **SDK client:** partnercentral-channel
  - **IAM action:**  [partnercentral:UpdateProgramManagementAccount](#list_partner-central-action-UpdateProgramManagementAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRelationship  **
  - **SDK client:** partnercentral-channel
  - **IAM action:**  [partnercentral:UpdateRelationship](#list_partner-central-action-UpdateRelationship) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateMarketplaceRevenueShare  **
  - **SDK client:** partnercentral-revenue-measurement
  - **IAM action:**  [partnercentral:CreateMarketplaceRevenueShare](#list_partner-central-action-CreateMarketplaceRevenueShare)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [partnercentral:TagResource](#list_partner-central-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateMarketplaceRevenueShareAllocation  **
  - **SDK client:** partnercentral-revenue-measurement
  - **IAM action:**  [partnercentral:CreateMarketplaceRevenueShareAllocation](#list_partner-central-action-CreateMarketplaceRevenueShareAllocation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateRevenueAttribution  **
  - **SDK client:** partnercentral-revenue-measurement
  - **IAM action:**  [partnercentral:CreateRevenueAttribution](#list_partner-central-action-CreateRevenueAttribution)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [partnercentral:TagResource](#list_partner-central-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   GetMarketplaceRevenueShare  **
  - **SDK client:** partnercentral-revenue-measurement
  - **IAM action:**  [partnercentral:GetMarketplaceRevenueShare](#list_partner-central-action-GetMarketplaceRevenueShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMarketplaceRevenueShareAllocation  **
  - **SDK client:** partnercentral-revenue-measurement
  - **IAM action:**  [partnercentral:GetMarketplaceRevenueShareAllocation](#list_partner-central-action-GetMarketplaceRevenueShareAllocation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRevenueAttribution  **
  - **SDK client:** partnercentral-revenue-measurement
  - **IAM action:**  [partnercentral:GetRevenueAttribution](#list_partner-central-action-GetRevenueAttribution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRevenueAttributionAllocation  **
  - **SDK client:** partnercentral-revenue-measurement
  - **IAM action:**  [partnercentral:GetRevenueAttributionAllocation](#list_partner-central-action-GetRevenueAttributionAllocation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRevenueAttributionAllocationsTask  **
  - **SDK client:** partnercentral-revenue-measurement
  - **IAM action:**  [partnercentral:GetRevenueAttributionAllocationsTask](#list_partner-central-action-GetRevenueAttributionAllocationsTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListMarketplaceRevenueShareAllocations  **
  - **SDK client:** partnercentral-revenue-measurement
  - **IAM action:**  [partnercentral:ListMarketplaceRevenueShareAllocations](#list_partner-central-action-ListMarketplaceRevenueShareAllocations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMarketplaceRevenueShares  **
  - **SDK client:** partnercentral-revenue-measurement
  - **IAM action:**  [partnercentral:ListMarketplaceRevenueShares](#list_partner-central-action-ListMarketplaceRevenueShares) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRevenueAttributionAllocations  **
  - **SDK client:** partnercentral-revenue-measurement
  - **IAM action:**  [partnercentral:ListRevenueAttributionAllocations](#list_partner-central-action-ListRevenueAttributionAllocations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRevenueAttributions  **
  - **SDK client:** partnercentral-revenue-measurement
  - **IAM action:**  [partnercentral:ListRevenueAttributions](#list_partner-central-action-ListRevenueAttributions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** partnercentral-revenue-measurement
  - **IAM action:**  [partnercentral:ListTagsForResource](#list_partner-central-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartRevenueAttributionAllocationsTask  **
  - **SDK client:** partnercentral-revenue-measurement
  - **IAM action:**  [partnercentral:StartRevenueAttributionAllocationsTask](#list_partner-central-action-StartRevenueAttributionAllocationsTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** partnercentral-revenue-measurement
  - **IAM action:**  [partnercentral:TagResource](#list_partner-central-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** partnercentral-revenue-measurement
  - **IAM action:**  [partnercentral:UntagResource](#list_partner-central-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateMarketplaceRevenueShareAllocation  **
  - **SDK client:** partnercentral-revenue-measurement
  - **IAM action:**  [partnercentral:UpdateMarketplaceRevenueShareAllocation](#list_partner-central-action-UpdateMarketplaceRevenueShareAllocation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRevenueAttribution  **
  - **SDK client:** partnercentral-revenue-measurement
  - **IAM action:**  [partnercentral:UpdateRevenueAttribution](#list_partner-central-action-UpdateRevenueAttribution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AcceptEngagementInvitation  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:AcceptEngagementInvitation](#list_partner-central-action-AcceptEngagementInvitation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssignOpportunity  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:AssignOpportunity](#list_partner-central-action-AssignOpportunity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateOpportunity  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:AssociateOpportunity](#list_partner-central-action-AssociateOpportunity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateEngagement  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:CreateEngagement](#list_partner-central-action-CreateEngagement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateEngagementContext  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:CreateEngagementContext](#list_partner-central-action-CreateEngagementContext)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [partnercentral:GetEngagement](#list_partner-central-action-GetEngagement)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   CreateEngagementInvitation  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:CreateEngagementInvitation](#list_partner-central-action-CreateEngagementInvitation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [partnercentral:GetEngagement](#list_partner-central-action-GetEngagement)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   CreateOpportunity  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:CreateOpportunity](#list_partner-central-action-CreateOpportunity)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [partnercentral:TagResource](#list_partner-central-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateResourceSnapshot  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:CreateResourceSnapshot](#list_partner-central-action-CreateResourceSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [partnercentral:GetAwsOpportunitySummary](#list_partner-central-action-GetAwsOpportunitySummary)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [partnercentral:GetOpportunity](#list_partner-central-action-GetOpportunity)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   CreateResourceSnapshotJob  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:CreateResourceSnapshot](#list_partner-central-action-CreateResourceSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [partnercentral:CreateResourceSnapshotJob](#list_partner-central-action-CreateResourceSnapshotJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [partnercentral:GetOpportunity](#list_partner-central-action-GetOpportunity)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [partnercentral:TagResource](#list_partner-central-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteResourceSnapshotJob  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:DeleteResourceSnapshotJob](#list_partner-central-action-DeleteResourceSnapshotJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateOpportunity  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:DisassociateOpportunity](#list_partner-central-action-DisassociateOpportunity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAwsOpportunitySummary  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:GetAwsOpportunitySummary](#list_partner-central-action-GetAwsOpportunitySummary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEngagement  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:GetEngagement](#list_partner-central-action-GetEngagement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEngagementInvitation  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:GetEngagementInvitation](#list_partner-central-action-GetEngagementInvitation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOpportunity  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:GetOpportunity](#list_partner-central-action-GetOpportunity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProspectingFromEngagementTask  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:GetProspectingFromEngagementTask](#list_partner-central-action-GetProspectingFromEngagementTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourceSnapshot  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:GetResourceSnapshot](#list_partner-central-action-GetResourceSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourceSnapshotJob  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:GetResourceSnapshotJob](#list_partner-central-action-GetResourceSnapshotJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSellingSystemSettings  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:GetSellingSystemSettings](#list_partner-central-action-GetSellingSystemSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListEngagementByAcceptingInvitationTasks  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:ListEngagementByAcceptingInvitationTasks](#list_partner-central-action-ListEngagementByAcceptingInvitationTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEngagementFromOpportunityTasks  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:ListEngagementFromOpportunityTasks](#list_partner-central-action-ListEngagementFromOpportunityTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEngagementInvitations  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:ListEngagementInvitations](#list_partner-central-action-ListEngagementInvitations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEngagementMembers  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:ListEngagementMembers](#list_partner-central-action-ListEngagementMembers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListEngagementResourceAssociations  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:ListEngagementResourceAssociations](#list_partner-central-action-ListEngagementResourceAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListEngagements  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:ListEngagements](#list_partner-central-action-ListEngagements) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOpportunities  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:ListOpportunities](#list_partner-central-action-ListOpportunities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOpportunityFromEngagementTasks  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:ListEngagementFromOpportunityTasks](#list_partner-central-action-ListEngagementFromOpportunityTasks)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [partnercentral:ListOpportunityFromEngagementTasks](#list_partner-central-action-ListOpportunityFromEngagementTasks)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListProspectingFromEngagementTasks  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:ListProspectingFromEngagementTasks](#list_partner-central-action-ListProspectingFromEngagementTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourceSnapshotJobs  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:ListResourceSnapshotJobs](#list_partner-central-action-ListResourceSnapshotJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourceSnapshots  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:ListResourceSnapshots](#list_partner-central-action-ListResourceSnapshots) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSolutions  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:ListSolutions](#list_partner-central-action-ListSolutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:ListTagsForResource](#list_partner-central-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutSellingSystemSettings  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:PutSellingSystemSettings](#list_partner-central-action-PutSellingSystemSettings)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** resource-snapshot-job.partnercentral-selling.amazonaws.com / **Access level:** Write

- **   RejectEngagementInvitation  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:RejectEngagementInvitation](#list_partner-central-action-RejectEngagementInvitation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartEngagementByAcceptingInvitationTask  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:AcceptEngagementInvitation](#list_partner-central-action-AcceptEngagementInvitation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [partnercentral:CreateOpportunity](#list_partner-central-action-CreateOpportunity)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [partnercentral:CreateResourceSnapshot](#list_partner-central-action-CreateResourceSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [partnercentral:CreateResourceSnapshotJob](#list_partner-central-action-CreateResourceSnapshotJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [partnercentral:GetEngagementInvitation](#list_partner-central-action-GetEngagementInvitation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [partnercentral:GetOpportunity](#list_partner-central-action-GetOpportunity)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [partnercentral:StartEngagementByAcceptingInvitationTask](#list_partner-central-action-StartEngagementByAcceptingInvitationTask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [partnercentral:StartResourceSnapshotJob](#list_partner-central-action-StartResourceSnapshotJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [partnercentral:SubmitOpportunity](#list_partner-central-action-SubmitOpportunity)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [partnercentral:TagResource](#list_partner-central-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   StartEngagementFromOpportunityTask  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:CreateEngagement](#list_partner-central-action-CreateEngagement)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [partnercentral:CreateResourceSnapshot](#list_partner-central-action-CreateResourceSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [partnercentral:CreateResourceSnapshotJob](#list_partner-central-action-CreateResourceSnapshotJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [partnercentral:GetOpportunity](#list_partner-central-action-GetOpportunity)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [partnercentral:StartEngagementFromOpportunityTask](#list_partner-central-action-StartEngagementFromOpportunityTask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [partnercentral:StartResourceSnapshotJob](#list_partner-central-action-StartResourceSnapshotJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [partnercentral:SubmitOpportunity](#list_partner-central-action-SubmitOpportunity)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [partnercentral:TagResource](#list_partner-central-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   StartOpportunityFromEngagementTask  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:CreateOpportunity](#list_partner-central-action-CreateOpportunity)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [partnercentral:CreateResourceSnapshot](#list_partner-central-action-CreateResourceSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [partnercentral:CreateResourceSnapshotJob](#list_partner-central-action-CreateResourceSnapshotJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [partnercentral:GetEngagement](#list_partner-central-action-GetEngagement)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [partnercentral:GetOpportunity](#list_partner-central-action-GetOpportunity)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [partnercentral:StartOpportunityFromEngagementTask](#list_partner-central-action-StartOpportunityFromEngagementTask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [partnercentral:StartResourceSnapshotJob](#list_partner-central-action-StartResourceSnapshotJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [partnercentral:TagResource](#list_partner-central-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   StartProspectingFromEngagementTask  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:StartProspectingFromEngagementTask](#list_partner-central-action-StartProspectingFromEngagementTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartResourceSnapshotJob  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:StartResourceSnapshotJob](#list_partner-central-action-StartResourceSnapshotJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopResourceSnapshotJob  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:StopResourceSnapshotJob](#list_partner-central-action-StopResourceSnapshotJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SubmitOpportunity  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:SubmitOpportunity](#list_partner-central-action-SubmitOpportunity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:TagResource](#list_partner-central-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:UntagResource](#list_partner-central-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateEngagementContext  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:GetEngagement](#list_partner-central-action-GetEngagement)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [partnercentral:UpdateEngagementContext](#list_partner-central-action-UpdateEngagementContext)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateOpportunity  **
  - **SDK client:** partnercentral-selling
  - **IAM action:**  [partnercentral:UpdateOpportunity](#list_partner-central-action-UpdateOpportunity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Partner Central
<a name="list_partner-central-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptChannelHandshake](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_AcceptChannelHandshake.html)  **
  - **Description:** Grants permission to accept channel handshakes in AWS Partner Central
  - **Resource types (\*required):** [ChannelHandshake\*](#list_partner-central-resource-ChannelHandshake)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:ChannelHandshakeType](#list_partner-central-partnercentral_ChannelHandshakeType)
  - **Access level:** Write

- **   [AcceptConnectionInvitation](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_AcceptConnectionInvitation.html)  **
  - **Description:** Grants permission to accept connection invitations in AWS Partner Central
  - **Resource types (\*required):** [ConnectionInvitation\*](#list_partner-central-resource-ConnectionInvitation)
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [AcceptEngagementInvitation](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_AcceptEngagementInvitation.html)  **
  - **Description:** Grants permission to accept Engagement Invitations on AWS Partner Central
  - **Resource types (\*required):** [engagement-invitation\*](#list_partner-central-resource-engagement-invitation)
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [AmendBenefitApplication](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_AmendBenefitApplication.html)  **
  - **Description:** Grants permission to amend benefit applications in AWS Partner Central
  - **Resource types (\*required):** [BenefitApplication\*](#list_partner-central-resource-BenefitApplication)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Access level:** Write

- **   [AssignOpportunity](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_AssignOpportunity.html)  **
  - **Description:** Grants permission to assign Opportunities on AWS Partner Central
  - **Resource types (\*required):** [Opportunity\*](#list_partner-central-resource-Opportunity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [AssociateAwsTrainingCertificationEmailDomain](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_AssociateAwsTrainingCertificationEmailDomain.html)  **
  - **Description:** Grants permission to associate AWS Training and Certification email domains in AWS Partner Central
  - **Resource types (\*required):** [Partner\*](#list_partner-central-resource-Partner)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [AssociateBenefitApplicationResource](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_AssociateBenefitApplicationResource.html)  **
  - **Description:** Grants permission to associate benefit application resources in AWS Partner Central
  - **Resource types (\*required):** [BenefitAllocation\*](#list_partner-central-resource-BenefitAllocation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Resource types (\*required):** [BenefitApplication\*](#list_partner-central-resource-BenefitApplication) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Resource types (\*required):** [Opportunity\*](#list_partner-central-resource-Opportunity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Access level:** Write

- **   [AssociateOpportunity](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_AssociateOpportunity.html)  **
  - **Description:** Grants permission to associate Opportunities on AWS Partner Central with other entities
  - **Resource types (\*required):** [Opportunity\*](#list_partner-central-resource-Opportunity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:RelatedEntityType](#list_partner-central-partnercentral_RelatedEntityType)
  - **Access level:** Write

- **   [CancelBenefitApplication](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_CancelBenefitApplication.html)  **
  - **Description:** Grants permission to cancel benefit applications in AWS Partner Central
  - **Resource types (\*required):** [BenefitApplication\*](#list_partner-central-resource-BenefitApplication)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Access level:** Write

- **   [CancelChannelHandshake](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_CancelChannelHandshake.html)  **
  - **Description:** Grants permission to cancel channel handshakes in AWS Partner Central
  - **Resource types (\*required):** [ChannelHandshake\*](#list_partner-central-resource-ChannelHandshake)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:ChannelHandshakeType](#list_partner-central-partnercentral_ChannelHandshakeType)
  - **Access level:** Write

- **   [CancelConnection](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_CancelConnection.html)  **
  - **Description:** Grants permission to cancel connections in AWS Partner Central
  - **Resource types (\*required):** [Connection\*](#list_partner-central-resource-Connection)
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [CancelConnectionInvitation](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_CancelConnectionInvitation.html)  **
  - **Description:** Grants permission to cancel connection invitations in AWS Partner Central
  - **Resource types (\*required):** [ConnectionInvitation\*](#list_partner-central-resource-ConnectionInvitation)
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [CancelProfileUpdateTask](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_CancelProfileUpdateTask.html)  **
  - **Description:** Grants permission to cancel profile update tasks in AWS Partner Central
  - **Resource types (\*required):** [Partner\*](#list_partner-central-resource-Partner)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [CreateBenefitApplication](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_CreateBenefitApplication.html)  **
  - **Description:** Grants permission to create benefit applications in AWS Partner Central
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_partner-central-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_partner-central-aws_TagKeys)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Access level:** Write

- **   [CreateChannelHandshake](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_CreateChannelHandshake.html)  **
  - **Description:** Grants permission to create channel handshakes in AWS Partner Central
  - **Resource types (\*required):** [ProgramManagementAccount](#list_partner-central-resource-ProgramManagementAccount) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_partner-central-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_partner-central-aws_TagKeys)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:ChannelHandshakeType](#list_partner-central-partnercentral_ChannelHandshakeType)
  - **Resource types (\*required):** [Relationship](#list_partner-central-resource-Relationship) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_partner-central-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_partner-central-aws_TagKeys)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:ChannelHandshakeType](#list_partner-central-partnercentral_ChannelHandshakeType)
  - **Access level:** Write

- **   [CreateConnectionInvitation](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_CreateConnectionInvitation.html)  **
  - **Description:** Grants permission to create connection invitations in AWS Partner Central
  - **Resource types (\*required):** 
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [CreateEngagement](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_CreateEngagement.html)  **
  - **Description:** Grants permission to creating engagements in AWS Partner Central
  - **Resource types (\*required):** [Engagement\*](#list_partner-central-resource-Engagement)
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [CreateEngagementContext](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_CreateEngagementContext.html)  **
  - **Description:** Grants permission to create engagement contexts in AWS Partner Central
  - **Resource types (\*required):** [Engagement\*](#list_partner-central-resource-Engagement)
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [CreateEngagementInvitation](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_CreateEngagementInvitation.html)  **
  - **Description:** Grants permission to creating engagement invitations in AWS Partner Central
  - **Resource types (\*required):** [engagement-invitation\*](#list_partner-central-resource-engagement-invitation)
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [CreateMarketplaceRevenueShare](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_CreateMarketplaceRevenueShare.html)  **
  - **Description:** Grants permission to create marketplace revenue shares in AWS Partner Central
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_partner-central-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_partner-central-aws_TagKeys)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [CreateMarketplaceRevenueShareAllocation](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_CreateMarketplaceRevenueShareAllocation.html)  **
  - **Description:** Grants permission to create marketplace revenue share allocations in AWS Partner Central
  - **Resource types (\*required):** [MarketplaceRevenueShare\*](#list_partner-central-resource-MarketplaceRevenueShare)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [CreateOpportunity](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_CreateOpportunity.html)  **
  - **Description:** Grants permission to create new Opportunities on AWS Partner Central
  - **Resource types (\*required):** [Opportunity\*](#list_partner-central-resource-Opportunity)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_partner-central-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_partner-central-aws_TagKeys)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [CreatePartner](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_CreatePartner.html)  **
  - **Description:** Grants permission to create partners in AWS Partner Central
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_partner-central-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_partner-central-aws_TagKeys)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [CreateProgramManagementAccount](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_CreateProgramManagementAccount.html)  **
  - **Description:** Grants permission to create program management accounts in AWS Partner Central
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_partner-central-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_partner-central-aws_TagKeys)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [CreateRelationship](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_CreateRelationship.html)  **
  - **Description:** Grants permission to create relationships in AWS Partner Central
  - **Resource types (\*required):** [ProgramManagementAccount\*](#list_partner-central-resource-ProgramManagementAccount)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_partner-central-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_partner-central-aws_TagKeys)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [CreateResourceSnapshot](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_CreateResourceSnapshot.html)  **
  - **Description:** Grants permission to creating resource snapshots in AWS Partner Central
  - **Resource types (\*required):** [ResourceSnapshot\*](#list_partner-central-resource-ResourceSnapshot)
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [CreateResourceSnapshotJob](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_CreateResourceSnapshotJob.html)  **
  - **Description:** Grants permission to creating resource snapshot jobs in AWS Partner Central
  - **Resource types (\*required):** [resource-snapshot-job\*](#list_partner-central-resource-resource-snapshot-job)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_partner-central-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_partner-central-aws_TagKeys)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [CreateRevenueAttribution](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_CreateRevenueAttribution.html)  **
  - **Description:** Grants permission to create revenue attributions in AWS Partner Central
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_partner-central-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_partner-central-aws_TagKeys)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [DeleteProgramManagementAccount](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_DeleteProgramManagementAccount.html)  **
  - **Description:** Grants permission to delete program management accounts in AWS Partner Central
  - **Resource types (\*required):** [ProgramManagementAccount\*](#list_partner-central-resource-ProgramManagementAccount)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [DeleteRelationship](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_DeleteRelationship.html)  **
  - **Description:** Grants permission to delete relationships in AWS Partner Central
  - **Resource types (\*required):** [Relationship\*](#list_partner-central-resource-Relationship)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [DeleteResourceSnapshotJob](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_DeleteResourceSnapshotJob.html)  **
  - **Description:** Grants permission to deleting resource snapshot jobs on AWS Partner Central
  - **Resource types (\*required):** [resource-snapshot-job\*](#list_partner-central-resource-resource-snapshot-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [DisassociateAwsTrainingCertificationEmailDomain](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_DisassociateAwsTrainingCertificationEmailDomain.html)  **
  - **Description:** Grants permission to disassociate AWS Training and Certification email domains in AWS Partner Central
  - **Resource types (\*required):** [Partner\*](#list_partner-central-resource-Partner)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [DisassociateBenefitApplicationResource](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_DisassociateBenefitApplicationResource.html)  **
  - **Description:** Grants permission to disassociate benefit application resources in AWS Partner Central
  - **Resource types (\*required):** [BenefitAllocation\*](#list_partner-central-resource-BenefitAllocation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Resource types (\*required):** [BenefitApplication\*](#list_partner-central-resource-BenefitApplication) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Resource types (\*required):** [Opportunity\*](#list_partner-central-resource-Opportunity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Access level:** Write

- **   [DisassociateOpportunity](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_DisassociateOpportunity.html)  **
  - **Description:** Grants permission to disassociate Opportunities on AWS Partner Central from other entities
  - **Resource types (\*required):** [Opportunity\*](#list_partner-central-resource-Opportunity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:RelatedEntityType](#list_partner-central-partnercentral_RelatedEntityType)
  - **Access level:** Write

- **   [GetAllianceLeadContact](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_GetAllianceLeadContact.html)  **
  - **Description:** Grants permission to retrieve alliance lead contact information in AWS Partner Central
  - **Resource types (\*required):** [Partner\*](#list_partner-central-resource-Partner)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Read

- **   [GetAwsOpportunitySummary](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_GetAwsOpportunitySummary.html)  **
  - **Description:** Grants permission to retrieve AWS Opportunity Summaries for Opportunities on AWS Partner Central
  - **Resource types (\*required):** [Opportunity\*](#list_partner-central-resource-Opportunity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Read

- **   [GetBenefit](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_GetBenefit.html)  **
  - **Description:** Grants permission to retrieve benefit details in AWS Partner Central
  - **Resource types (\*required):** [Benefit\*](#list_partner-central-resource-Benefit)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Access level:** Read

- **   [GetBenefitAllocation](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_GetBenefitAllocation.html)  **
  - **Description:** Grants permission to retrieve benefit allocation details in AWS Partner Central
  - **Resource types (\*required):** [BenefitAllocation\*](#list_partner-central-resource-BenefitAllocation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)
  - **Access level:** Read

- **   [GetBenefitApplication](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_GetBenefitApplication.html)  **
  - **Description:** Grants permission to retrieve benefit application details in AWS Partner Central
  - **Resource types (\*required):** [BenefitApplication\*](#list_partner-central-resource-BenefitApplication)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Access level:** Read

- **   [GetConnection](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_GetConnection.html)  **
  - **Description:** Grants permission to retrieve connection details in AWS Partner Central
  - **Resource types (\*required):** [Connection\*](#list_partner-central-resource-Connection)
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Read

- **   [GetConnectionInvitation](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_GetConnectionInvitation.html)  **
  - **Description:** Grants permission to retrieve connection invitation details in AWS Partner Central
  - **Resource types (\*required):** [ConnectionInvitation\*](#list_partner-central-resource-ConnectionInvitation)
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Read

- **   [GetConnectionPreferences](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_GetConnectionPreferences.html)  **
  - **Description:** Grants permission to retrieve connection preferences in AWS Partner Central
  - **Resource types (\*required):** 
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Read

- **   [GetEngagement](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_GetEngagement.html)  **
  - **Description:** Grants permission to retrieval of engagement details in AWS Partner Central
  - **Resource types (\*required):** [Engagement\*](#list_partner-central-resource-Engagement)
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Read

- **   [GetEngagementInvitation](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_GetEngagementInvitation.html)  **
  - **Description:** Grants permission to retrieve details of Engagement Invitations on AWS Partner Central
  - **Resource types (\*required):** [engagement-invitation\*](#list_partner-central-resource-engagement-invitation)
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Read

- **   [GetMarketplaceRevenueShare](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_GetMarketplaceRevenueShare.html)  **
  - **Description:** Grants permission to retrieve marketplace revenue share details in AWS Partner Central
  - **Resource types (\*required):** [MarketplaceRevenueShare\*](#list_partner-central-resource-MarketplaceRevenueShare)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Read

- **   [GetMarketplaceRevenueShareAllocation](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_GetMarketplaceRevenueShareAllocation.html)  **
  - **Description:** Grants permission to retrieve marketplace revenue share allocation details in AWS Partner Central
  - **Resource types (\*required):** [MarketplaceRevenueShare\*](#list_partner-central-resource-MarketplaceRevenueShare)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Read

- **   [GetOpportunity](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_GetOpportunity.html)  **
  - **Description:** Grants permission to retrieve details of Opportunities on AWS Partner Central
  - **Resource types (\*required):** [Opportunity\*](#list_partner-central-resource-Opportunity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Read

- **   [GetPartner](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_GetPartner.html)  **
  - **Description:** Grants permission to retrieve partner details in AWS Partner Central
  - **Resource types (\*required):** [Partner\*](#list_partner-central-resource-Partner)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Read

- **   [GetPartnerDashboard](${UserGuideDocPage}controlling-access-in-aws-partner-central.html)  **
  - **Description:** Grants permission to retrieve partner dashboard information in AWS Partner Central
  - **Resource types (\*required):** [Dashboard\*](#list_partner-central-resource-Dashboard)
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Read

- **   [GetProfileUpdateTask](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_GetProfileUpdateTask.html)  **
  - **Description:** Grants permission to retrieve profile update task details in AWS Partner Central
  - **Resource types (\*required):** [Partner\*](#list_partner-central-resource-Partner)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Read

- **   [GetProfileVisibility](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_GetProfileVisibility.html)  **
  - **Description:** Grants permission to retrieve profile visibility settings in AWS Partner Central
  - **Resource types (\*required):** [Partner\*](#list_partner-central-resource-Partner)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Read

- **   [GetProspectingFromEngagementTask](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_GetProspectingFromEngagementTask.html)  **
  - **Description:** Grants permission to retrieve prospecting from engagement task details in AWS Partner Central
  - **Resource types (\*required):** [ProspectingFromEngagementTask\*](#list_partner-central-resource-ProspectingFromEngagementTask)
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Read

- **   [GetQualificationsAssociationDetails](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_GetQualificationsAssociationDetails.html)  **
  - **Description:** Grants permission to retrieve qualifications association details in AWS Partner Central
  - **Resource types (\*required):** [Partner\*](#list_partner-central-resource-Partner)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Read

- **   [GetQualificationsAssociationTask](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_GetQualificationsAssociationTask.html)  **
  - **Description:** Grants permission to retrieve qualifications association task details in AWS Partner Central
  - **Resource types (\*required):** [Partner\*](#list_partner-central-resource-Partner)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Read

- **   [GetQualificationsDisassociationTask](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_GetQualificationsDisassociationTask.html)  **
  - **Description:** Grants permission to retrieve qualifications disassociation task details in AWS Partner Central
  - **Resource types (\*required):** [Partner\*](#list_partner-central-resource-Partner)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Read

- **   [GetRelationship](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_GetRelationship.html)  **
  - **Description:** Grants permission to retrieve relationship details in AWS Partner Central
  - **Resource types (\*required):** [Relationship\*](#list_partner-central-resource-Relationship)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Read

- **   [GetResourceSnapshot](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_GetResourceSnapshot.html)  **
  - **Description:** Grants permission to retrieving resource snapshot details in AWS Partner Central
  - **Resource types (\*required):** [ResourceSnapshot\*](#list_partner-central-resource-ResourceSnapshot)
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Read

- **   [GetResourceSnapshotJob](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_GetResourceSnapshotJob.html)  **
  - **Description:** Grants permission to retrieving resource snapshot job details in AWS Partner Central
  - **Resource types (\*required):** [resource-snapshot-job\*](#list_partner-central-resource-resource-snapshot-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Read

- **   [GetRevenueAttribution](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_GetRevenueAttribution.html)  **
  - **Description:** Grants permission to retrieve revenue attribution details in AWS Partner Central
  - **Resource types (\*required):** [RevenueAttribution\*](#list_partner-central-resource-RevenueAttribution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Read

- **   [GetRevenueAttributionAllocation](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_GetRevenueAttributionAllocation.html)  **
  - **Description:** Grants permission to retrieve revenue attribution allocation details in AWS Partner Central
  - **Resource types (\*required):** [RevenueAttribution\*](#list_partner-central-resource-RevenueAttribution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Read

- **   [GetRevenueAttributionAllocationsTask](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_GetRevenueAttributionAllocationsTask.html)  **
  - **Description:** Grants permission to retrieve revenue attribution allocations task details in AWS Partner Central
  - **Resource types (\*required):** [RevenueAttribution\*](#list_partner-central-resource-RevenueAttribution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Read

- **   [GetSellingSystemSettings](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_GetSellingSystemSettings.html)  **
  - **Description:** Grants permission to retrieving selling system settings in AWS Partner Central
  - **Resource types (\*required):** 
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Read

- **   [GetVerification](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_GetVerification.html)  **
  - **Description:** Grants permission to retrieve verification details in AWS Partner Central
  - **Resource types (\*required):** 
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:VerificationType](#list_partner-central-partnercentral_VerificationType)
  - **Access level:** Read

- **   [ListBenefitAllocations](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_ListBenefitAllocations.html)  **
  - **Description:** Grants permission to list benefit allocations in AWS Partner Central
  - **Resource types (\*required):** [BenefitAllocation\*](#list_partner-central-resource-BenefitAllocation)
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)
  - **Access level:** List

- **   [ListBenefitApplications](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_ListBenefitApplications.html)  **
  - **Description:** Grants permission to list benefit applications in AWS Partner Central
  - **Resource types (\*required):** [BenefitApplication\*](#list_partner-central-resource-BenefitApplication)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Access level:** List

- **   [ListBenefits](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_ListBenefits.html)  **
  - **Description:** Grants permission to list benefits in AWS Partner Central
  - **Resource types (\*required):** [Benefit\*](#list_partner-central-resource-Benefit)
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Access level:** List

- **   [ListChannelHandshakes](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_ListChannelHandshakes.html)  **
  - **Description:** Grants permission to list channel handshakes in AWS Partner Central
  - **Resource types (\*required):** [ChannelHandshake\*](#list_partner-central-resource-ChannelHandshake)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:ChannelHandshakeType](#list_partner-central-partnercentral_ChannelHandshakeType)
  - **Access level:** List

- **   [ListConnectionInvitations](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_ListConnectionInvitations.html)  **
  - **Description:** Grants permission to list connection invitations in AWS Partner Central
  - **Resource types (\*required):** 
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** List

- **   [ListConnections](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_ListConnections.html)  **
  - **Description:** Grants permission to list connections in AWS Partner Central
  - **Resource types (\*required):** 
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** List

- **   [ListEngagementByAcceptingInvitationTasks](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListEngagementByAcceptingInvitationTasks.html)  **
  - **Description:** Grants permission to listing engagements by accepting invitation tasks in AWS Partner Central
  - **Resource types (\*required):** 
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** List

- **   [ListEngagementFromOpportunityTasks](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListEngagementFromOpportunityTasks.html)  **
  - **Description:** Grants permission to listing engagements from opportunity tasks in AWS Partner Central
  - **Resource types (\*required):** 
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** List

- **   [ListEngagementInvitations](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListEngagementInvitations.html)  **
  - **Description:** Grants permission to list Engagement Invitations on AWS Partner Central
  - **Resource types (\*required):** 
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** List

- **   [ListEngagementMembers](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListEngagementMembers.html)  **
  - **Description:** Grants permission to listing engagement members in AWS Partner Central
  - **Resource types (\*required):** [Engagement\*](#list_partner-central-resource-Engagement)
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Read

- **   [ListEngagementResourceAssociations](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListEngagementResourceAssociations.html)  **
  - **Description:** Grants permission to listing engagement resource associations in AWS Partner Central
  - **Resource types (\*required):** [ResourceSnapshot\*](#list_partner-central-resource-ResourceSnapshot)
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Read

- **   [ListEngagements](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListEngagements.html)  **
  - **Description:** Grants permission to listing engagements in AWS Partner Central
  - **Resource types (\*required):** 
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** List

- **   [ListMarketplaceRevenueShareAllocations](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_ListMarketplaceRevenueShareAllocations.html)  **
  - **Description:** Grants permission to list marketplace revenue share allocations in AWS Partner Central
  - **Resource types (\*required):** [MarketplaceRevenueShare\*](#list_partner-central-resource-MarketplaceRevenueShare)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** List

- **   [ListMarketplaceRevenueShares](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_ListMarketplaceRevenueShares.html)  **
  - **Description:** Grants permission to list marketplace revenue shares in AWS Partner Central
  - **Resource types (\*required):** 
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** List

- **   [ListOpportunities](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListOpportunities.html)  **
  - **Description:** Grants permission to list Opportunities on AWS Partner Central
  - **Resource types (\*required):** 
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** List

- **   [ListOpportunityFromEngagementTasks](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListOpportunityFromEngagementTasks.html)  **
  - **Description:** Grants permission to list opportunity from engagement tasks in AWS Partner Central
  - **Resource types (\*required):** 
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** List

- **   [ListPartners](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_ListPartners.html)  **
  - **Description:** Grants permission to list partners in AWS Partner Central
  - **Resource types (\*required):** 
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** List

- **   [ListProgramManagementAccounts](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_ListProgramManagementAccounts.html)  **
  - **Description:** Grants permission to list program management accounts in AWS Partner Central
  - **Resource types (\*required):** [ProgramManagementAccount\*](#list_partner-central-resource-ProgramManagementAccount)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** List

- **   [ListProspectingFromEngagementTasks](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListProspectingFromEngagementTasks.html)  **
  - **Description:** Grants permission to list prospecting from engagement tasks in AWS Partner Central
  - **Resource types (\*required):** 
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** List

- **   [ListRelationships](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_ListRelationships.html)  **
  - **Description:** Grants permission to list relationships in AWS Partner Central
  - **Resource types (\*required):** [Relationship\*](#list_partner-central-resource-Relationship)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** List

- **   [ListResourceSnapshotJobs](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListResourceSnapshotJobs.html)  **
  - **Description:** Grants permission to listing resource snapshot jobs in AWS Partner Central
  - **Resource types (\*required):** 
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** List

- **   [ListResourceSnapshots](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListResourceSnapshots.html)  **
  - **Description:** Grants permission to listing resource snapshots in AWS Partner Central
  - **Resource types (\*required):** [ResourceSnapshot\*](#list_partner-central-resource-ResourceSnapshot)
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** List

- **   [ListRevenueAttributionAllocations](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_ListRevenueAttributionAllocations.html)  **
  - **Description:** Grants permission to list revenue attribution allocations in AWS Partner Central
  - **Resource types (\*required):** [RevenueAttribution\*](#list_partner-central-resource-RevenueAttribution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** List

- **   [ListRevenueAttributions](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_ListRevenueAttributions.html)  **
  - **Description:** Grants permission to list revenue attributions in AWS Partner Central
  - **Resource types (\*required):** 
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** List

- **   [ListSolutions](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListSolutions.html)  **
  - **Description:** Grants permission to list Solutions on AWS Partner Central
  - **Resource types (\*required):** 
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource in AWS Partner Central
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_partner-central-aws_TagKeys)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Access level:** Read

- **   [PutAllianceLeadContact](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_PutAllianceLeadContact.html)  **
  - **Description:** Grants permission to set alliance lead contact information in AWS Partner Central
  - **Resource types (\*required):** [Partner\*](#list_partner-central-resource-Partner)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [PutProfileVisibility](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_PutProfileVisibility.html)  **
  - **Description:** Grants permission to set profile visibility in AWS Partner Central
  - **Resource types (\*required):** [Partner\*](#list_partner-central-resource-Partner)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [PutSellingSystemSettings](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_PutSellingSystemSettings.html)  **
  - **Description:** Grants permission to put selling system settings in AWS Partner Central
  - **Resource types (\*required):** 
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [RecallBenefitApplication](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_RecallBenefitApplication.html)  **
  - **Description:** Grants permission to recall benefit applications in AWS Partner Central
  - **Resource types (\*required):** [BenefitApplication\*](#list_partner-central-resource-BenefitApplication)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Access level:** Write

- **   [RejectChannelHandshake](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_RejectChannelHandshake.html)  **
  - **Description:** Grants permission to reject channel handshakes in AWS Partner Central
  - **Resource types (\*required):** [ChannelHandshake\*](#list_partner-central-resource-ChannelHandshake)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:ChannelHandshakeType](#list_partner-central-partnercentral_ChannelHandshakeType)
  - **Access level:** Write

- **   [RejectConnectionInvitation](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_RejectConnectionInvitation.html)  **
  - **Description:** Grants permission to reject connection invitations in AWS Partner Central
  - **Resource types (\*required):** [ConnectionInvitation\*](#list_partner-central-resource-ConnectionInvitation)
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [RejectEngagementInvitation](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_RejectEngagementInvitation.html)  **
  - **Description:** Grants permission to reject Engagement Invitations on AWS Partner Central
  - **Resource types (\*required):** [engagement-invitation\*](#list_partner-central-resource-engagement-invitation)
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [SendEmailVerificationCode](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_SendEmailVerificationCode.html)  **
  - **Description:** Grants permission to send email verification codes in AWS Partner Central
  - **Resource types (\*required):** 
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [StartEngagementByAcceptingInvitationTask](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_StartEngagementByAcceptingInvitationTask.html)  **
  - **Description:** Grants permission to initiate tasks that start Engagements on AWS Partner Central by accepting an Engagement Invitation
  - **Resource types (\*required):** [engagement-by-accepting-invitation-task\*](#list_partner-central-resource-engagement-by-accepting-invitation-task)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_partner-central-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_partner-central-aws_TagKeys)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [StartEngagementFromOpportunityTask](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_StartEngagementFromOpportunityTask.html)  **
  - **Description:** Grants permission to initiate tasks that start Engagements from Opportunities on AWS Partner Central
  - **Resource types (\*required):** [engagement-from-opportunity-task\*](#list_partner-central-resource-engagement-from-opportunity-task)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_partner-central-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_partner-central-aws_TagKeys)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [StartOpportunityFromEngagementTask](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_StartOpportunityFromEngagementTask.html)  **
  - **Description:** Grants permission to initiate tasks that start Opportunities from Engagements on AWS Partner Central
  - **Resource types (\*required):** [OpportunityFromEngagementTask\*](#list_partner-central-resource-OpportunityFromEngagementTask)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_partner-central-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_partner-central-aws_TagKeys)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [StartProfileUpdateTask](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_StartProfileUpdateTask.html)  **
  - **Description:** Grants permission to start profile update tasks in AWS Partner Central
  - **Resource types (\*required):** [Partner\*](#list_partner-central-resource-Partner)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [StartProspectingFromEngagementTask](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_StartProspectingFromEngagementTask.html)  **
  - **Description:** Grants permission to initiate tasks that start prospecting from an engagement in AWS Partner Central
  - **Resource types (\*required):** [Engagement\*](#list_partner-central-resource-Engagement)
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [StartQualificationsAssociationTask](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_StartQualificationsAssociationTask.html)  **
  - **Description:** Grants permission to initiate tasks that start qualifications association in AWS Partner Central
  - **Resource types (\*required):** [Partner\*](#list_partner-central-resource-Partner)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [StartQualificationsDisassociationTask](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_StartQualificationsDisassociationTask.html)  **
  - **Description:** Grants permission to initiate tasks that start qualifications disassociation in AWS Partner Central
  - **Resource types (\*required):** [Partner\*](#list_partner-central-resource-Partner)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [StartResourceSnapshotJob](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_StartResourceSnapshotJob.html)  **
  - **Description:** Grants permission to starting resource snapshot jobs in AWS Partner Central
  - **Resource types (\*required):** [resource-snapshot-job\*](#list_partner-central-resource-resource-snapshot-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [StartRevenueAttributionAllocationsTask](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_StartRevenueAttributionAllocationsTask.html)  **
  - **Description:** Grants permission to initiate tasks that manage revenue attribution allocations in AWS Partner Central
  - **Resource types (\*required):** [RevenueAttribution\*](#list_partner-central-resource-RevenueAttribution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [StartVerification](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_StartVerification.html)  **
  - **Description:** Grants permission to start verification processes in AWS Partner Central
  - **Resource types (\*required):** 
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:VerificationType](#list_partner-central-partnercentral_VerificationType)
  - **Access level:** Write

- **   [StopResourceSnapshotJob](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_StopResourceSnapshotJob.html)  **
  - **Description:** Grants permission to stopping resource snapshot jobs in AWS Partner Central
  - **Resource types (\*required):** [resource-snapshot-job\*](#list_partner-central-resource-resource-snapshot-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [SubmitBenefitApplication](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_SubmitBenefitApplication.html)  **
  - **Description:** Grants permission to submit benefit applications in AWS Partner Central
  - **Resource types (\*required):** [BenefitApplication\*](#list_partner-central-resource-BenefitApplication)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Access level:** Write

- **   [SubmitOpportunity](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_SubmitOpportunity.html)  **
  - **Description:** Grants permission to submit Opportunities on AWS Partner Central
  - **Resource types (\*required):** [Opportunity\*](#list_partner-central-resource-Opportunity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add new tags to a resource. Supported resource: ResourceSnapshotJob
  - **Resource types (\*required):** [BenefitApplication](#list_partner-central-resource-BenefitApplication) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_partner-central-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_partner-central-aws_TagKeys)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Resource types (\*required):** [ChannelHandshake](#list_partner-central-resource-ChannelHandshake) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_partner-central-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_partner-central-aws_TagKeys)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Resource types (\*required):** [MarketplaceRevenueShare](#list_partner-central-resource-MarketplaceRevenueShare) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_partner-central-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_partner-central-aws_TagKeys)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Resource types (\*required):** [Opportunity](#list_partner-central-resource-Opportunity) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_partner-central-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_partner-central-aws_TagKeys)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Resource types (\*required):** [Partner](#list_partner-central-resource-Partner) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_partner-central-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_partner-central-aws_TagKeys)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Resource types (\*required):** [ProgramManagementAccount](#list_partner-central-resource-ProgramManagementAccount) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_partner-central-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_partner-central-aws_TagKeys)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Resource types (\*required):** [Relationship](#list_partner-central-resource-Relationship) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_partner-central-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_partner-central-aws_TagKeys)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Resource types (\*required):** [RevenueAttribution](#list_partner-central-resource-RevenueAttribution) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_partner-central-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_partner-central-aws_TagKeys)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Resource types (\*required):** [resource-snapshot-job](#list_partner-central-resource-resource-snapshot-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_partner-central-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_partner-central-aws_TagKeys)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a resource. Supported resource: ResourceSnapshotJob
  - **Resource types (\*required):** [BenefitApplication](#list_partner-central-resource-BenefitApplication) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_partner-central-aws_TagKeys)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Resource types (\*required):** [ChannelHandshake](#list_partner-central-resource-ChannelHandshake) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_partner-central-aws_TagKeys)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Resource types (\*required):** [MarketplaceRevenueShare](#list_partner-central-resource-MarketplaceRevenueShare) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_partner-central-aws_TagKeys)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Resource types (\*required):** [Opportunity](#list_partner-central-resource-Opportunity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_partner-central-aws_TagKeys)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Resource types (\*required):** [Partner](#list_partner-central-resource-Partner) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_partner-central-aws_TagKeys)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Resource types (\*required):** [ProgramManagementAccount](#list_partner-central-resource-ProgramManagementAccount) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_partner-central-aws_TagKeys)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Resource types (\*required):** [Relationship](#list_partner-central-resource-Relationship) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_partner-central-aws_TagKeys)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Resource types (\*required):** [RevenueAttribution](#list_partner-central-resource-RevenueAttribution) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_partner-central-aws_TagKeys)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Resource types (\*required):** [resource-snapshot-job](#list_partner-central-resource-resource-snapshot-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_partner-central-aws_TagKeys)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Access level:** Tagging, Write

- **   [UpdateBenefitApplication](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_UpdateBenefitApplication.html)  **
  - **Description:** Grants permission to update benefit applications in AWS Partner Central
  - **Resource types (\*required):** [BenefitApplication\*](#list_partner-central-resource-BenefitApplication)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)<br />[partnercentral:FulfillmentTypes](#list_partner-central-partnercentral_FulfillmentTypes)<br />[partnercentral:Programs](#list_partner-central-partnercentral_Programs)
  - **Access level:** Write

- **   [UpdateConnectionPreferences](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_UpdateConnectionPreferences.html)  **
  - **Description:** Grants permission to update connection preferences in AWS Partner Central
  - **Resource types (\*required):** 
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [UpdateEngagementContext](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_UpdateEngagementContext.html)  **
  - **Description:** Grants permission to update engagement contexts in AWS Partner Central
  - **Resource types (\*required):** [Engagement\*](#list_partner-central-resource-Engagement)
  - **Condition keys:** [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [UpdateMarketplaceRevenueShareAllocation](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_UpdateMarketplaceRevenueShareAllocation.html)  **
  - **Description:** Grants permission to update marketplace revenue share allocations in AWS Partner Central
  - **Resource types (\*required):** [MarketplaceRevenueShare\*](#list_partner-central-resource-MarketplaceRevenueShare)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [UpdateOpportunity](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_UpdateOpportunity.html)  **
  - **Description:** Grants permission to update Opportunities on AWS Partner Central
  - **Resource types (\*required):** [Opportunity\*](#list_partner-central-resource-Opportunity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [UpdateProgramManagementAccount](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_UpdateProgramManagementAccount.html)  **
  - **Description:** Grants permission to update program management accounts in AWS Partner Central
  - **Resource types (\*required):** [ProgramManagementAccount\*](#list_partner-central-resource-ProgramManagementAccount)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [UpdateRelationship](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_UpdateRelationship.html)  **
  - **Description:** Grants permission to update relationships in AWS Partner Central
  - **Resource types (\*required):** [Relationship\*](#list_partner-central-resource-Relationship)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write

- **   [UpdateRevenueAttribution](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_UpdateRevenueAttribution.html)  **
  - **Description:** Grants permission to update revenue attributions in AWS Partner Central
  - **Resource types (\*required):** [RevenueAttribution\*](#list_partner-central-resource-RevenueAttribution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_)<br />[partnercentral:Catalog](#list_partner-central-partnercentral_Catalog)
  - **Access level:** Write



## Permission-only actions for AWS Partner Central
<a name="list_partner-central-permission-only-actions"></a>

The following actions are defined by AWS Partner Central but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [CreateBusinessPlan](${UserGuideDocPage}controlling-access-in-aws-partner-central.html)  | Grants permission to create business plans in AWS Partner Central |  |   | Write | 
|   [CreateCollaborationChannelMembers](${UserGuideDocPage}controlling-access-in-aws-partner-central.html)  | Grants permission to create collaboration channel members in AWS Partner Central |  |   | Write | 
|   [CreateCollaborationChannelRequest](${UserGuideDocPage}controlling-access-in-aws-partner-central.html)  | Grants permission to create collaboration channel requests in AWS Partner Central |  |   | Write | 
|   [EnrollInPartnerPath](${UserGuideDocPage}controlling-access-in-aws-partner-central.html)  | Grants permission to enroll in partner paths in AWS Partner Central |  |   | Write | 
|   [GetBusinessPlan](${UserGuideDocPage}controlling-access-in-aws-partner-central.html)  | Grants permission to retrieve business plan details in AWS Partner Central |  |   | Read | 
|   [GetCollaborationChannel](${UserGuideDocPage}controlling-access-in-aws-partner-central.html)  | Grants permission to retrieve collaboration channel details in AWS Partner Central |  |   | Read | 
|   [GetPartnerProfile](${UserGuideDocPage}controlling-access-in-aws-partner-central.html)  | Grants permission to retrieve public partner profile details in AWS Partner Central |  |   | Read | 
|   [GetProgramManagementAccount](${UserGuideDocPage}controlling-access-in-aws-partner-central.html)  | Grants permission to retrieve program management account details in AWS Partner Central |  | [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog) | Read | 
|   [ListBusinessPlans](${UserGuideDocPage}controlling-access-in-aws-partner-central.html)  | Grants permission to list business plans in AWS Partner Central |  |   | List | 
|   [ListCollaborationChannels](${UserGuideDocPage}controlling-access-in-aws-partner-central.html)  | Grants permission to list collaboration channels in AWS Partner Central |  |   | List | 
|   [ListPartnerPaths](${UserGuideDocPage}controlling-access-in-aws-partner-central.html)  | Grants permission to list partner paths in AWS Partner Central |  |   | List | 
|   [PutBusinessPlan](${UserGuideDocPage}controlling-access-in-aws-partner-central.html)  | Grants permission to update business plans in AWS Partner Central |  |   | Write | 
|   [SearchPartnerProfiles](${UserGuideDocPage}controlling-access-in-aws-partner-central.html)  | Grants permission to search public partner profiles in AWS Partner Central |  |   | List | 
|   [UseSession](${UserGuideDocPage}controlling-access-in-aws-partner-central.html)  | Grants permission to use Partner Central Agents sessions in AWS Partner Central |  | [partnercentral:Catalog](#list_partner-central-partnercentral_Catalog) | Write | 

## Resource types defined by AWS Partner Central
<a name="list_partner-central-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Benefit](https://docs.aws.amazon.com/partner-central/latest/APIReference/using-the-benefits-api.html)  | arn:${Partition}:partnercentral:${Region}::catalog/${Catalog}/benefit/${Identifier} |   | 
|  [BenefitAllocation](https://docs.aws.amazon.com/partner-central/latest/APIReference/working-with-benefit-allocations.html)  | arn:${Partition}:partnercentral:${Region}:${Account}:catalog/${Catalog}/benefit-allocation/${Identifier} |   | 
|  [BenefitApplication](https://docs.aws.amazon.com/partner-central/latest/APIReference/working-with-benefit-applications.html)  | arn:${Partition}:partnercentral:${Region}:${Account}:catalog/${Catalog}/benefit-application/${Identifier} | [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_) | 
|  [ChannelHandshake](https://docs.aws.amazon.com/partner-central/latest/APIReference/working-with-channel-management.html)  | arn:${Partition}:partnercentral:${Region}:${Account}:catalog/${Catalog}/channel-handshake/${Identifier} | [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_) | 
|  [Connection](https://docs.aws.amazon.com/partner-central/latest/APIReference/working-with-account-connections.html)  | arn:${Partition}:partnercentral:${Region}::catalog/${Catalog}/connection/${Identifier} |   | 
|  [ConnectionInvitation](https://docs.aws.amazon.com/partner-central/latest/APIReference/working-with-account-connections.html)  | arn:${Partition}:partnercentral:${Region}::catalog/${Catalog}/connection-invitation/${Identifier} |   | 
|  [ConnectionPreferences](https://docs.aws.amazon.com/partner-central/latest/APIReference/working-with-account-connections.html)  | arn:${Partition}:partnercentral:${Region}:${Account}:catalog/${Catalog}/connection-preferences |   | 
|  [Dashboard](https://docs.aws.amazon.com/partner-central/latest/getting-started/partner-analytics.html)  | arn:${Partition}:partnercentral::${Account}:catalog/${Catalog}/ReportingData/${TableId}/Dashboard/${DashboardId} |   | 
|  [Engagement](https://docs.aws.amazon.com/partner-central/latest/APIReference/working-with-multi-partner-opportunities.html)  | arn:${Partition}:partnercentral:${Region}::catalog/${Catalog}/engagement/${Identifier} |   | 
|  [MarketplaceRevenueShare](https://docs.aws.amazon.com/partner-central/latest/APIReference/working-with-marketplace-revenue-share.html)  | arn:${Partition}:partnercentral:${Region}:${Account}:catalog/${Catalog}/marketplace-revenue-share/${MarketplaceProductId} | [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_) | 
|  [Opportunity](https://docs.aws.amazon.com/partner-central/latest/APIReference/working-with-your-opportunities.html)  | arn:${Partition}:partnercentral:${Region}:${Account}:catalog/${Catalog}/opportunity/${Identifier} | [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_) | 
|  [OpportunityFromEngagementTask](https://docs.aws.amazon.com/partner-central/latest/APIReference/working-with-multi-partner-opportunities.html)  | arn:${Partition}:partnercentral:${Region}::catalog/${Catalog}/opportunity-from-engagement-task/${TaskId} |   | 
|  [Partner](https://docs.aws.amazon.com/partner-central/latest/APIReference/working-with-partner-registration.html)  | arn:${Partition}:partnercentral:${Region}:${Account}:catalog/${Catalog}/partner/${Identifier} | [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_) | 
|  [ProgramManagementAccount](https://docs.aws.amazon.com/partner-central/latest/APIReference/working-with-channel-management.html)  | arn:${Partition}:partnercentral:${Region}:${Account}:catalog/${Catalog}/program-management-account/${Identifier} | [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_) | 
|  [ProspectingFromEngagementTask](https://docs.aws.amazon.com/partner-central/latest/APIReference/working-with-your-leads.html)  | arn:${Partition}:partnercentral:${Region}::catalog/${Catalog}/prospecting-from-engagement-task/${TaskIdentifier} |   | 
|  [Relationship](https://docs.aws.amazon.com/partner-central/latest/APIReference/working-with-channel-management.html)  | arn:${Partition}:partnercentral:${Region}:${Account}:catalog/${Catalog}/program-management-account/${ProgramManagementAccountId}/relationship/${RelationshipId} | [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_) | 
|  [ResourceSnapshot](https://docs.aws.amazon.com/partner-central/latest/APIReference/working-with-multi-partner-opportunities.html)  | arn:${Partition}:partnercentral:${Region}:${Account}:catalog/${Catalog}/engagement/${EngagementIdentifier}/resource/${ResourceType}/${ResourceIdentifier}/template/${TemplateIdentifier}/resource-snapshot/${SnapshotRevision} |   | 
|  [RevenueAttribution](https://docs.aws.amazon.com/partner-central/latest/APIReference/working-with-revenue-attribution.html)  | arn:${Partition}:partnercentral:${Region}:${Account}:catalog/${Catalog}/revenue-attribution/${RevenueAttributionId} | [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_) | 
|  [Solution](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListSolutions.html)  | arn:${Partition}:partnercentral:${Region}:${Account}:catalog/${Catalog}/solution/${Identifier} |   | 
|  [engagement-by-accepting-invitation-task](https://docs.aws.amazon.com/partner-central/latest/APIReference/working-with-multi-partner-opportunities.html)  | arn:${Partition}:partnercentral:${Region}::catalog/${Catalog}/engagement-by-accepting-invitation-task/${TaskId} |   | 
|  [engagement-from-opportunity-task](https://docs.aws.amazon.com/partner-central/latest/APIReference/working-with-multi-partner-opportunities.html)  | arn:${Partition}:partnercentral:${Region}::catalog/${Catalog}/engagement-from-opportunity-task/${TaskId} |   | 
|  [engagement-invitation](https://docs.aws.amazon.com/partner-central/latest/APIReference/working-with-multi-partner-opportunities.html)  | arn:${Partition}:partnercentral:${Region}::catalog/${Catalog}/engagement-invitation/${Identifier} |   | 
|  [resource-snapshot-job](https://docs.aws.amazon.com/partner-central/latest/APIReference/working-with-multi-partner-opportunities.html)  | arn:${Partition}:partnercentral:${Region}:${Account}:catalog/${Catalog}/resource-snapshot-job/${Identifier} | [aws:ResourceTag/${TagKey}](#list_partner-central-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Partner Central
<a name="list_partner-central-policy-keys"></a>

AWS Partner Central defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [partnercentral:Catalog](https://docs.aws.amazon.com/partner-central/latest/getting-started/controlling-access-in-aws-partner-central.html#condition-keys-for-aws-partner-central)  | Filters access by a specific Catalog | String | 
|   [partnercentral:ChannelHandshakeType](https://docs.aws.amazon.com/partner-central/latest/getting-started/controlling-access-in-aws-partner-central.html#condition-keys-for-aws-partner-central)  | Filters access by channel handshake types | String | 
|   [partnercentral:FulfillmentTypes](https://docs.aws.amazon.com/partner-central/latest/getting-started/controlling-access-in-aws-partner-central.html#condition-keys-for-aws-partner-central)  | Filters access by benefit fulfillment types | ArrayOfString | 
|   [partnercentral:Programs](https://docs.aws.amazon.com/partner-central/latest/getting-started/controlling-access-in-aws-partner-central.html#condition-keys-for-aws-partner-central)  | Filters access by program | ArrayOfString | 
|   [partnercentral:RelatedEntityType](https://docs.aws.amazon.com/partner-central/latest/getting-started/controlling-access-in-aws-partner-central.html#condition-keys-for-aws-partner-central)  | Filters access by entity types for Opportunity association | String | 
|   [partnercentral:VerificationType](https://docs.aws.amazon.com/partner-central/latest/getting-started/controlling-access-in-aws-partner-central.html#condition-keys-for-aws-partner-central)  | Filters access by the type of verification being performed | String | 