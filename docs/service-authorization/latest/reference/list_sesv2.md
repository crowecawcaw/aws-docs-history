

# Actions, resources, and condition keys for Amazon Simple Email Service v2
<a name="list_sesv2"></a>

Amazon Simple Email Service v2 (service prefix: `ses`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/ses/latest/APIReference-V2/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/control-user-access.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/ses/ses.json) for this service.

**Topics**
+ [API operations defined by Amazon Simple Email Service v2](#list_sesv2-operations)
+ [Actions defined by Amazon Simple Email Service v2](#list_sesv2-actions-as-permissions)
+ [Permission-only actions for Amazon Simple Email Service v2](#list_sesv2-permission-only-actions)
+ [Resource types defined by Amazon Simple Email Service v2](#list_sesv2-resources-for-iam-policies)
+ [Condition keys for Amazon Simple Email Service v2](#list_sesv2-policy-keys)

## API operations defined by Amazon Simple Email Service v2
<a name="list_sesv2-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_sesv2-actions-as-permissions).




- **   BatchGetMetricData  **
  - **IAM action:**  [ses:BatchGetMetricData](#list_sesv2-action-BatchGetMetricData) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CancelExportJob  **
  - **IAM action:**  [ses:CancelExportJob](#list_sesv2-action-CancelExportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateConfigurationSet  **
  - **IAM action:**  [ses:CreateConfigurationSet](#list_sesv2-action-CreateConfigurationSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ses:TagResource](#list_sesv2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateConfigurationSetEventDestination  **
  - **IAM action:**  [ses:CreateConfigurationSetEventDestination](#list_sesv2-action-CreateConfigurationSetEventDestination)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ses.amazonaws.com / **Access level:** Write

- **   CreateContact  **
  - **IAM action:**  [ses:CreateContact](#list_sesv2-action-CreateContact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateContactList  **
  - **IAM action:**  [ses:CreateContactList](#list_sesv2-action-CreateContactList)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ses:TagResource](#list_sesv2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCustomVerificationEmailTemplate  **
  - **IAM action:**  [ses:CreateCustomVerificationEmailTemplate](#list_sesv2-action-CreateCustomVerificationEmailTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ses:TagResource](#list_sesv2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDedicatedIpPool  **
  - **IAM action:**  [ses:CreateDedicatedIpPool](#list_sesv2-action-CreateDedicatedIpPool)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ses:TagResource](#list_sesv2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDeliverabilityTestReport  **
  - **IAM action:**  [ses:CreateDeliverabilityTestReport](#list_sesv2-action-CreateDeliverabilityTestReport)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ses:TagResource](#list_sesv2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateEmailIdentity  **
  - **IAM action:**  [ses:CreateEmailIdentity](#list_sesv2-action-CreateEmailIdentity)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ses:TagResource](#list_sesv2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateEmailIdentityPolicy  **
  - **IAM action:**  [ses:CreateEmailIdentityPolicy](#list_sesv2-action-CreateEmailIdentityPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   CreateEmailTemplate  **
  - **IAM action:**  [ses:CreateEmailTemplate](#list_sesv2-action-CreateEmailTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ses:TagResource](#list_sesv2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateExportJob  **
  - **IAM action:**  [ses:CreateExportJob](#list_sesv2-action-CreateExportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateImportJob  **
  - **IAM action:**  [ses:CreateImportJob](#list_sesv2-action-CreateImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateMultiRegionEndpoint  **
  - **IAM action:**  [ses:CreateMultiRegionEndpoint](#list_sesv2-action-CreateMultiRegionEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ses:TagResource](#list_sesv2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateTenant  **
  - **IAM action:**  [ses:CreateTenant](#list_sesv2-action-CreateTenant)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ses:TagResource](#list_sesv2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateTenantResourceAssociation  **
  - **IAM action:**  [ses:CreateTenantResourceAssociation](#list_sesv2-action-CreateTenantResourceAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConfigurationSet  **
  - **IAM action:**  [ses:DeleteConfigurationSet](#list_sesv2-action-DeleteConfigurationSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConfigurationSetEventDestination  **
  - **IAM action:**  [ses:DeleteConfigurationSetEventDestination](#list_sesv2-action-DeleteConfigurationSetEventDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteContact  **
  - **IAM action:**  [ses:DeleteContact](#list_sesv2-action-DeleteContact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteContactList  **
  - **IAM action:**  [ses:DeleteContactList](#list_sesv2-action-DeleteContactList) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCustomVerificationEmailTemplate  **
  - **IAM action:**  [ses:DeleteCustomVerificationEmailTemplate](#list_sesv2-action-DeleteCustomVerificationEmailTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDedicatedIpPool  **
  - **IAM action:**  [ses:DeleteDedicatedIpPool](#list_sesv2-action-DeleteDedicatedIpPool) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEmailIdentity  **
  - **IAM action:**  [ses:DeleteEmailIdentity](#list_sesv2-action-DeleteEmailIdentity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEmailIdentityPolicy  **
  - **IAM action:**  [ses:DeleteEmailIdentityPolicy](#list_sesv2-action-DeleteEmailIdentityPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteEmailTemplate  **
  - **IAM action:**  [ses:DeleteEmailTemplate](#list_sesv2-action-DeleteEmailTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMultiRegionEndpoint  **
  - **IAM action:**  [ses:DeleteMultiRegionEndpoint](#list_sesv2-action-DeleteMultiRegionEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSuppressedDestination  **
  - **IAM action:**  [ses:DeleteSuppressedDestination](#list_sesv2-action-DeleteSuppressedDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTenant  **
  - **IAM action:**  [ses:DeleteTenant](#list_sesv2-action-DeleteTenant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTenantResourceAssociation  **
  - **IAM action:**  [ses:DeleteTenantResourceAssociation](#list_sesv2-action-DeleteTenantResourceAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAccount  **
  - **IAM action:**  [ses:GetAccount](#list_sesv2-action-GetAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBlacklistReports  **
  - **IAM action:**  [ses:GetBlacklistReports](#list_sesv2-action-GetBlacklistReports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConfigurationSet  **
  - **IAM action:**  [ses:GetConfigurationSet](#list_sesv2-action-GetConfigurationSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConfigurationSetEventDestinations  **
  - **IAM action:**  [ses:GetConfigurationSetEventDestinations](#list_sesv2-action-GetConfigurationSetEventDestinations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetContact  **
  - **IAM action:**  [ses:GetContact](#list_sesv2-action-GetContact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetContactList  **
  - **IAM action:**  [ses:GetContactList](#list_sesv2-action-GetContactList) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCustomVerificationEmailTemplate  **
  - **IAM action:**  [ses:GetCustomVerificationEmailTemplate](#list_sesv2-action-GetCustomVerificationEmailTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDedicatedIp  **
  - **IAM action:**  [ses:GetDedicatedIp](#list_sesv2-action-GetDedicatedIp) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDedicatedIpPool  **
  - **IAM action:**  [ses:GetDedicatedIpPool](#list_sesv2-action-GetDedicatedIpPool) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDedicatedIps  **
  - **IAM action:**  [ses:GetDedicatedIps](#list_sesv2-action-GetDedicatedIps) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDeliverabilityDashboardOptions  **
  - **IAM action:**  [ses:GetDeliverabilityDashboardOptions](#list_sesv2-action-GetDeliverabilityDashboardOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDeliverabilityTestReport  **
  - **IAM action:**  [ses:GetDeliverabilityTestReport](#list_sesv2-action-GetDeliverabilityTestReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDomainDeliverabilityCampaign  **
  - **IAM action:**  [ses:GetDomainDeliverabilityCampaign](#list_sesv2-action-GetDomainDeliverabilityCampaign) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDomainStatisticsReport  **
  - **IAM action:**  [ses:GetDomainStatisticsReport](#list_sesv2-action-GetDomainStatisticsReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEmailAddressInsights  **
  - **IAM action:**  [ses:GetEmailAddressInsights](#list_sesv2-action-GetEmailAddressInsights) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEmailIdentity  **
  - **IAM action:**  [ses:GetEmailIdentity](#list_sesv2-action-GetEmailIdentity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEmailIdentityPolicies  **
  - **IAM action:**  [ses:GetEmailIdentityPolicies](#list_sesv2-action-GetEmailIdentityPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEmailTemplate  **
  - **IAM action:**  [ses:GetEmailTemplate](#list_sesv2-action-GetEmailTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetExportJob  **
  - **IAM action:**  [ses:GetExportJob](#list_sesv2-action-GetExportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetImportJob  **
  - **IAM action:**  [ses:GetImportJob](#list_sesv2-action-GetImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMessageInsights  **
  - **IAM action:**  [ses:GetMessageInsights](#list_sesv2-action-GetMessageInsights) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMultiRegionEndpoint  **
  - **IAM action:**  [ses:GetMultiRegionEndpoint](#list_sesv2-action-GetMultiRegionEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetReputationEntity  **
  - **IAM action:**  [ses:GetReputationEntity](#list_sesv2-action-GetReputationEntity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSuppressedDestination  **
  - **IAM action:**  [ses:GetSuppressedDestination](#list_sesv2-action-GetSuppressedDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTenant  **
  - **IAM action:**  [ses:GetTenant](#list_sesv2-action-GetTenant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListConfigurationSets  **
  - **IAM action:**  [ses:ListConfigurationSets](#list_sesv2-action-ListConfigurationSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListContactLists  **
  - **IAM action:**  [ses:ListContactLists](#list_sesv2-action-ListContactLists) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListContacts  **
  - **IAM action:**  [ses:ListContacts](#list_sesv2-action-ListContacts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCustomVerificationEmailTemplates  **
  - **IAM action:**  [ses:ListCustomVerificationEmailTemplates](#list_sesv2-action-ListCustomVerificationEmailTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDedicatedIpPools  **
  - **IAM action:**  [ses:ListDedicatedIpPools](#list_sesv2-action-ListDedicatedIpPools) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDeliverabilityTestReports  **
  - **IAM action:**  [ses:ListDeliverabilityTestReports](#list_sesv2-action-ListDeliverabilityTestReports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDomainDeliverabilityCampaigns  **
  - **IAM action:**  [ses:ListDomainDeliverabilityCampaigns](#list_sesv2-action-ListDomainDeliverabilityCampaigns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListEmailIdentities  **
  - **IAM action:**  [ses:ListEmailIdentities](#list_sesv2-action-ListEmailIdentities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEmailTemplates  **
  - **IAM action:**  [ses:ListEmailTemplates](#list_sesv2-action-ListEmailTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListExportJobs  **
  - **IAM action:**  [ses:ListExportJobs](#list_sesv2-action-ListExportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListImportJobs  **
  - **IAM action:**  [ses:ListImportJobs](#list_sesv2-action-ListImportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMultiRegionEndpoints  **
  - **IAM action:**  [ses:ListMultiRegionEndpoints](#list_sesv2-action-ListMultiRegionEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRecommendations  **
  - **IAM action:**  [ses:ListRecommendations](#list_sesv2-action-ListRecommendations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListReputationEntities  **
  - **IAM action:**  [ses:ListReputationEntities](#list_sesv2-action-ListReputationEntities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourceTenants  **
  - **IAM action:**  [ses:ListResourceTenants](#list_sesv2-action-ListResourceTenants) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSuppressedDestinations  **
  - **IAM action:**  [ses:ListSuppressedDestinations](#list_sesv2-action-ListSuppressedDestinations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [ses:ListTagsForResource](#list_sesv2-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTenantResources  **
  - **IAM action:**  [ses:ListTenantResources](#list_sesv2-action-ListTenantResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTenants  **
  - **IAM action:**  [ses:ListTenants](#list_sesv2-action-ListTenants) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutAccountDedicatedIpWarmupAttributes  **
  - **IAM action:**  [ses:PutAccountDedicatedIpWarmupAttributes](#list_sesv2-action-PutAccountDedicatedIpWarmupAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutAccountDetails  **
  - **IAM action:**  [ses:PutAccountDetails](#list_sesv2-action-PutAccountDetails) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutAccountPricingAttributes  **
  - **IAM action:**  [ses:PutAccountPricingAttributes](#list_sesv2-action-PutAccountPricingAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutAccountSendingAttributes  **
  - **IAM action:**  [ses:PutAccountSendingAttributes](#list_sesv2-action-PutAccountSendingAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutAccountSuppressionAttributes  **
  - **IAM action:**  [ses:PutAccountSuppressionAttributes](#list_sesv2-action-PutAccountSuppressionAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutAccountVdmAttributes  **
  - **IAM action:**  [ses:PutAccountVdmAttributes](#list_sesv2-action-PutAccountVdmAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutConfigurationSetArchivingOptions  **
  - **IAM action:**  [ses:PutConfigurationSetArchivingOptions](#list_sesv2-action-PutConfigurationSetArchivingOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutConfigurationSetDeliveryOptions  **
  - **IAM action:**  [ses:PutConfigurationSetDeliveryOptions](#list_sesv2-action-PutConfigurationSetDeliveryOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutConfigurationSetReputationOptions  **
  - **IAM action:**  [ses:PutConfigurationSetReputationOptions](#list_sesv2-action-PutConfigurationSetReputationOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutConfigurationSetSendingOptions  **
  - **IAM action:**  [ses:PutConfigurationSetSendingOptions](#list_sesv2-action-PutConfigurationSetSendingOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutConfigurationSetSuppressionOptions  **
  - **IAM action:**  [ses:PutConfigurationSetSuppressionOptions](#list_sesv2-action-PutConfigurationSetSuppressionOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutConfigurationSetTrackingOptions  **
  - **IAM action:**  [ses:PutConfigurationSetTrackingOptions](#list_sesv2-action-PutConfigurationSetTrackingOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutConfigurationSetVdmOptions  **
  - **IAM action:**  [ses:PutConfigurationSetVdmOptions](#list_sesv2-action-PutConfigurationSetVdmOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutDedicatedIpInPool  **
  - **IAM action:**  [ses:PutDedicatedIpInPool](#list_sesv2-action-PutDedicatedIpInPool) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutDedicatedIpPoolScalingAttributes  **
  - **IAM action:**  [ses:PutDedicatedIpPoolScalingAttributes](#list_sesv2-action-PutDedicatedIpPoolScalingAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutDedicatedIpWarmupAttributes  **
  - **IAM action:**  [ses:PutDedicatedIpWarmupAttributes](#list_sesv2-action-PutDedicatedIpWarmupAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutDeliverabilityDashboardOption  **
  - **IAM action:**  [ses:PutDeliverabilityDashboardOption](#list_sesv2-action-PutDeliverabilityDashboardOption) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutEmailIdentityConfigurationSetAttributes  **
  - **IAM action:**  [ses:PutEmailIdentityConfigurationSetAttributes](#list_sesv2-action-PutEmailIdentityConfigurationSetAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutEmailIdentityDkimAttributes  **
  - **IAM action:**  [ses:PutEmailIdentityDkimAttributes](#list_sesv2-action-PutEmailIdentityDkimAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutEmailIdentityDkimSigningAttributes  **
  - **IAM action:**  [ses:PutEmailIdentityDkimSigningAttributes](#list_sesv2-action-PutEmailIdentityDkimSigningAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutEmailIdentityFeedbackAttributes  **
  - **IAM action:**  [ses:PutEmailIdentityFeedbackAttributes](#list_sesv2-action-PutEmailIdentityFeedbackAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutEmailIdentityMailFromAttributes  **
  - **IAM action:**  [ses:PutEmailIdentityMailFromAttributes](#list_sesv2-action-PutEmailIdentityMailFromAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutSuppressedDestination  **
  - **IAM action:**  [ses:PutSuppressedDestination](#list_sesv2-action-PutSuppressedDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutTenantSuppressionAttributes  **
  - **IAM action:**  [ses:PutTenantSuppressionAttributes](#list_sesv2-action-PutTenantSuppressionAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendBulkEmail  **
  - **IAM action:**  [ses:SendBulkEmail](#list_sesv2-action-SendBulkEmail) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendCustomVerificationEmail  **
  - **IAM action:**  [ses:SendCustomVerificationEmail](#list_sesv2-action-SendCustomVerificationEmail) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [ses:TagResource](#list_sesv2-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TestRenderEmailTemplate  **
  - **IAM action:**  [ses:TestRenderEmailTemplate](#list_sesv2-action-TestRenderEmailTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UntagResource  **
  - **IAM action:**  [ses:UntagResource](#list_sesv2-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateConfigurationSetEventDestination  **
  - **IAM action:**  [ses:UpdateConfigurationSetEventDestination](#list_sesv2-action-UpdateConfigurationSetEventDestination)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ses.amazonaws.com / **Access level:** Write

- **   UpdateContact  **
  - **IAM action:**  [ses:UpdateContact](#list_sesv2-action-UpdateContact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateContactList  **
  - **IAM action:**  [ses:UpdateContactList](#list_sesv2-action-UpdateContactList) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCustomVerificationEmailTemplate  **
  - **IAM action:**  [ses:UpdateCustomVerificationEmailTemplate](#list_sesv2-action-UpdateCustomVerificationEmailTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEmailIdentityPolicy  **
  - **IAM action:**  [ses:UpdateEmailIdentityPolicy](#list_sesv2-action-UpdateEmailIdentityPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   UpdateEmailTemplate  **
  - **IAM action:**  [ses:UpdateEmailTemplate](#list_sesv2-action-UpdateEmailTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateReputationEntityCustomerManagedStatus  **
  - **IAM action:**  [ses:UpdateReputationEntityCustomerManagedStatus](#list_sesv2-action-UpdateReputationEntityCustomerManagedStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateReputationEntityPolicy  **
  - **IAM action:**  [ses:UpdateReputationEntityPolicy](#list_sesv2-action-UpdateReputationEntityPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Simple Email Service v2
<a name="list_sesv2-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchGetMetricData](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_BatchGetMetricData.html)  **
  - **Description:** Grants permission to get metric data on your activity
  - **Resource types (\*required):** [configuration-set](#list_sesv2-resource-configuration-set) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [identity](#list_sesv2-resource-identity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Read

- **   [CancelExportJob](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_CancelExportJob.html)  **
  - **Description:** Grants permission to cancel an export job
  - **Resource types (\*required):** [export-job\*](#list_sesv2-resource-export-job)
  - **Condition keys:** [ses:ApiVersion](#list_sesv2-ses_ApiVersion)<br />[ses:ExportSourceType](#list_sesv2-ses_ExportSourceType)
  - **Access level:** Write

- **   [CreateConfigurationSet](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_CreateConfigurationSet.html)  **
  - **Description:** Grants permission to create a new configuration set
  - **Resource types (\*required):** [configuration-set\*](#list_sesv2-resource-configuration-set) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sesv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [dedicated-ip-pool](#list_sesv2-resource-dedicated-ip-pool) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sesv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [mailmanager-archive](#list_sesv2-resource-mailmanager-archive) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sesv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [CreateConfigurationSetEventDestination](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_CreateConfigurationSetEventDestination.html)  **
  - **Description:** Grants permission to create a configuration set event destination
  - **Resource types (\*required):** [configuration-set\*](#list_sesv2-resource-configuration-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [CreateContact](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_CreateContact.html)  **
  - **Description:** Grants permission to create a contact
  - **Resource types (\*required):** [contact-list\*](#list_sesv2-resource-contact-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [CreateContactList](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_CreateContactList.html)  **
  - **Description:** Grants permission to create a contact list
  - **Resource types (\*required):** [contact-list\*](#list_sesv2-resource-contact-list)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sesv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [CreateCustomVerificationEmailTemplate](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_CreateCustomVerificationEmailTemplate.html)  **
  - **Description:** Grants permission to create a new custom verification email template
  - **Resource types (\*required):** [custom-verification-email-template\*](#list_sesv2-resource-custom-verification-email-template)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sesv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [CreateDedicatedIpPool](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_CreateDedicatedIpPool.html)  **
  - **Description:** Grants permission to create a new pool of dedicated IP addresses
  - **Resource types (\*required):** [dedicated-ip-pool\*](#list_sesv2-resource-dedicated-ip-pool)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sesv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [CreateDeliverabilityTestReport](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_CreateDeliverabilityTestReport.html)  **
  - **Description:** Grants permission to create a new predictive inbox placement test
  - **Resource types (\*required):** [identity\*](#list_sesv2-resource-identity)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sesv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [CreateEmailIdentity](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_CreateEmailIdentity.html)  **
  - **Description:** Grants permission to start the process of verifying an email identity
  - **Resource types (\*required):** [identity\*](#list_sesv2-resource-identity)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sesv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [CreateEmailIdentityPolicy](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_CreateEmailIdentityPolicy.html)  **
  - **Description:** Grants permission to create the specified sending authorization policy for the given identity
  - **Resource types (\*required):** [identity\*](#list_sesv2-resource-identity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Permissions management, Write

- **   [CreateEmailTemplate](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_CreateEmailTemplate.html)  **
  - **Description:** Grants permission to create an email template
  - **Resource types (\*required):** [template\*](#list_sesv2-resource-template)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sesv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [CreateExportJob](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_CreateExportJob.html)  **
  - **Description:** Grants permission to create an export job
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_sesv2-ses_ApiVersion)<br />[ses:ExportSourceType](#list_sesv2-ses_ExportSourceType)
  - **Access level:** Write

- **   [CreateImportJob](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_CreateImportJob.html)  **
  - **Description:** Grants permission to creates an import job for a data destination
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [CreateMultiRegionEndpoint](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_CreateMultiRegionEndpoint.html)  **
  - **Description:** Grants permission to create a new multi-region endpoint
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sesv2-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [CreateTenant](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_CreateTenant.html)  **
  - **Description:** Grants permission to create a new tenant
  - **Resource types (\*required):** [tenant\*](#list_sesv2-resource-tenant)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sesv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [CreateTenantResourceAssociation](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_CreateTenantResourceAssociation.html)  **
  - **Description:** Grants permission to associate a SES resource to a tenant
  - **Resource types (\*required):** [configuration-set\*](#list_sesv2-resource-configuration-set) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sesv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [identity\*](#list_sesv2-resource-identity) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sesv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [template\*](#list_sesv2-resource-template) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sesv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [tenant\*](#list_sesv2-resource-tenant) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sesv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [DeleteConfigurationSet](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_DeleteConfigurationSet.html)  **
  - **Description:** Grants permission to delete an existing configuration set
  - **Resource types (\*required):** [configuration-set\*](#list_sesv2-resource-configuration-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [DeleteConfigurationSetEventDestination](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_DeleteConfigurationSetEventDestination.html)  **
  - **Description:** Grants permission to delete an event destination
  - **Resource types (\*required):** [configuration-set\*](#list_sesv2-resource-configuration-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [DeleteContact](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_DeleteContact.html)  **
  - **Description:** Grants permission to delete a contact from a contact list
  - **Resource types (\*required):** [contact-list\*](#list_sesv2-resource-contact-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [DeleteContactList](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_DeleteContactList.html)  **
  - **Description:** Grants permission to delete a contact list with all of its contacts
  - **Resource types (\*required):** [contact-list\*](#list_sesv2-resource-contact-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [DeleteCustomVerificationEmailTemplate](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_DeleteCustomVerificationEmailTemplate.html)  **
  - **Description:** Grants permission to delete an existing custom verification email template
  - **Resource types (\*required):** [custom-verification-email-template\*](#list_sesv2-resource-custom-verification-email-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [DeleteDedicatedIpPool](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_DeleteDedicatedIpPool.html)  **
  - **Description:** Grants permission to delete a dedicated IP pool
  - **Resource types (\*required):** [dedicated-ip-pool\*](#list_sesv2-resource-dedicated-ip-pool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [DeleteEmailIdentity](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_DeleteEmailIdentity.html)  **
  - **Description:** Grants permission to delete an email identity
  - **Resource types (\*required):** [identity\*](#list_sesv2-resource-identity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [DeleteEmailIdentityPolicy](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_DeleteEmailIdentityPolicy.html)  **
  - **Description:** Grants permission to delete the specified sending authorization policy for the given identity (an email address or a domain)
  - **Resource types (\*required):** [identity\*](#list_sesv2-resource-identity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Permissions management, Write

- **   [DeleteEmailTemplate](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_DeleteEmailTemplate.html)  **
  - **Description:** Grants permission to delete an email template
  - **Resource types (\*required):** [template\*](#list_sesv2-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [DeleteMultiRegionEndpoint](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_DeleteMultiRegionEndpoint.html)  **
  - **Description:** Grants permission to delete a multi-region endpoint
  - **Resource types (\*required):** [multi-region-endpoint\*](#list_sesv2-resource-multi-region-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [DeleteSuppressedDestination](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_DeleteSuppressedDestination.html)  **
  - **Description:** Grants permission to remove an email address from the suppression list for your account or tenant
  - **Resource types (\*required):** [tenant](#list_sesv2-resource-tenant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [DeleteTenant](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_DeleteTenant.html)  **
  - **Description:** Grants permission to delete a tenant
  - **Resource types (\*required):** [tenant\*](#list_sesv2-resource-tenant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [DeleteTenantResourceAssociation](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_DeleteTenantResourceAssociation.html)  **
  - **Description:** Grants permission to remove an associated SES resource from a tenant
  - **Resource types (\*required):** [configuration-set\*](#list_sesv2-resource-configuration-set) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [identity\*](#list_sesv2-resource-identity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [template\*](#list_sesv2-resource-template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [tenant\*](#list_sesv2-resource-tenant) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [GetAccount](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetAccount.html)  **
  - **Description:** Grants permission to get information about the email-sending status and capabilities for your account
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Read

- **   [GetBlacklistReports](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetBlacklistReports.html)  **
  - **Description:** Grants permission to retrieve a list of the deny lists on which your dedicated IP addresses or tracked domains appear
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Read

- **   [GetConfigurationSet](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetConfigurationSet.html)  **
  - **Description:** Grants permission to get information about an existing configuration set
  - **Resource types (\*required):** [configuration-set\*](#list_sesv2-resource-configuration-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Read

- **   [GetConfigurationSetEventDestinations](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetConfigurationSetEventDestinations.html)  **
  - **Description:** Grants permission to retrieve a list of event destinations that are associated with a configuration set
  - **Resource types (\*required):** [configuration-set\*](#list_sesv2-resource-configuration-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Read

- **   [GetContact](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetContact.html)  **
  - **Description:** Grants permission to return a contact from a contact list
  - **Resource types (\*required):** [contact-list\*](#list_sesv2-resource-contact-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Read

- **   [GetContactList](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetContactList.html)  **
  - **Description:** Grants permission to return contact list metadata
  - **Resource types (\*required):** [contact-list\*](#list_sesv2-resource-contact-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Read

- **   [GetCustomVerificationEmailTemplate](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetCustomVerificationEmailTemplate.html)  **
  - **Description:** Grants permission to return the custom email verification template for the template name you specify
  - **Resource types (\*required):** [custom-verification-email-template\*](#list_sesv2-resource-custom-verification-email-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Read

- **   [GetDedicatedIp](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetDedicatedIp.html)  **
  - **Description:** Grants permission to get information about a dedicated IP address
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Read

- **   [GetDedicatedIpPool](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetDedicatedIpPool.html)  **
  - **Description:** Grants permission to get information about a dedicated IP pool
  - **Resource types (\*required):** [dedicated-ip-pool\*](#list_sesv2-resource-dedicated-ip-pool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Read

- **   [GetDedicatedIps](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetDedicatedIps.html)  **
  - **Description:** Grants permission to list the dedicated IP addresses a dedicated IP pool
  - **Resource types (\*required):** [dedicated-ip-pool\*](#list_sesv2-resource-dedicated-ip-pool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Read

- **   [GetDeliverabilityDashboardOptions](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetDeliverabilityDashboardOptions.html)  **
  - **Description:** Grants permission to get the status of the Deliverability dashboard
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Read

- **   [GetDeliverabilityTestReport](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetDeliverabilityTestReport.html)  **
  - **Description:** Grants permission to retrieve the results of a predictive inbox placement test
  - **Resource types (\*required):** [deliverability-test-report\*](#list_sesv2-resource-deliverability-test-report)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Read

- **   [GetDomainDeliverabilityCampaign](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetDomainDeliverabilityCampaign.html)  **
  - **Description:** Grants permission to retrieve all the deliverability data for a specific campaign
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Read

- **   [GetDomainStatisticsReport](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetDomainStatisticsReport.html)  **
  - **Description:** Grants permission to retrieve inbox placement and engagement rates for the domains that you use to send email
  - **Resource types (\*required):** [identity\*](#list_sesv2-resource-identity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Read

- **   [GetEmailAddressInsights](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetEmailAddressInsights.html)  **
  - **Description:** Grants permission to get insights about email address
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Read

- **   [GetEmailIdentity](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetEmailIdentity.html)  **
  - **Description:** Grants permission to get information about a specific identity
  - **Resource types (\*required):** [identity\*](#list_sesv2-resource-identity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Read

- **   [GetEmailIdentityPolicies](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetEmailIdentityPolicies.html)  **
  - **Description:** Grants permission to return the requested sending authorization policies for the given identity (an email address or a domain)
  - **Resource types (\*required):** [identity\*](#list_sesv2-resource-identity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Read

- **   [GetEmailTemplate](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetEmailTemplate.html)  **
  - **Description:** Grants permission to return the template object, which includes the subject line, HTML part, and text part for the template you specify
  - **Resource types (\*required):** [template\*](#list_sesv2-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Read

- **   [GetExportJob](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetExportJob.html)  **
  - **Description:** Grants permission to get information about an export job
  - **Resource types (\*required):** [export-job\*](#list_sesv2-resource-export-job)
  - **Condition keys:** [ses:ApiVersion](#list_sesv2-ses_ApiVersion)<br />[ses:ExportSourceType](#list_sesv2-ses_ExportSourceType)
  - **Access level:** Read

- **   [GetImportJob](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetImportJob.html)  **
  - **Description:** Grants permission to provide information about an import job
  - **Resource types (\*required):** [import-job\*](#list_sesv2-resource-import-job)
  - **Condition keys:** [ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Read

- **   [GetMessageInsights](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetMessageInsights.html)  **
  - **Description:** Grants permission to provide insights about a message
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Read

- **   [GetMultiRegionEndpoint](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetMultiRegionEndpoint.html)  **
  - **Description:** Grants permission to get information about a multi-region endpoint
  - **Resource types (\*required):** [multi-region-endpoint\*](#list_sesv2-resource-multi-region-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Read

- **   [GetReputationEntity](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetReputationEntity.html)  **
  - **Description:** Grants permission to retrieve information about a reputation entity's status
  - **Resource types (\*required):** [tenant\*](#list_sesv2-resource-tenant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Read

- **   [GetSuppressedDestination](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetSuppressedDestination.html)  **
  - **Description:** Grants permission to retrieve information about a specific email address that's on the suppression list for your account or tenant
  - **Resource types (\*required):** [tenant](#list_sesv2-resource-tenant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Read

- **   [GetTenant](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetTenant.html)  **
  - **Description:** Grants permission to get information about a tenant
  - **Resource types (\*required):** [tenant\*](#list_sesv2-resource-tenant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Read

- **   [ListConfigurationSets](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListConfigurationSets.html)  **
  - **Description:** Grants permission to list all of the configuration sets for your account
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** List

- **   [ListContactLists](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListContactLists.html)  **
  - **Description:** Grants permission to list all of the contact lists available for your account
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** List

- **   [ListContacts](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListContacts.html)  **
  - **Description:** Grants permission to list the contacts present in a specific contact list
  - **Resource types (\*required):** [contact-list\*](#list_sesv2-resource-contact-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** List

- **   [ListCustomVerificationEmailTemplates](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListCustomVerificationEmailTemplates.html)  **
  - **Description:** Grants permission to list all of the existing custom verification email templates for your account
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** List

- **   [ListDedicatedIpPools](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListDedicatedIpPools.html)  **
  - **Description:** Grants permission to list all of the dedicated IP pools for your account
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** List

- **   [ListDeliverabilityTestReports](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListDeliverabilityTestReports.html)  **
  - **Description:** Grants permission to retrieve the list of the predictive inbox placement tests that you've performed, regardless of their statuses, for your account
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** List

- **   [ListDomainDeliverabilityCampaigns](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListDomainDeliverabilityCampaigns.html)  **
  - **Description:** Grants permission to list deliverability data for campaigns that used a specific domain to send email during a specified time range
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Read

- **   [ListEmailIdentities](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListEmailIdentities.html)  **
  - **Description:** Grants permission to list the email identities for your account
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** List

- **   [ListEmailTemplates](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListEmailTemplates.html)  **
  - **Description:** Grants permission to list all of the email templates for your account
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** List

- **   [ListExportJobs](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListExportJobs.html)  **
  - **Description:** Grants permission to list all the exports jobs for your account
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_sesv2-ses_ApiVersion)<br />[ses:ExportSourceType](#list_sesv2-ses_ExportSourceType)
  - **Access level:** List

- **   [ListImportJobs](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListImportJobs.html)  **
  - **Description:** Grants permission to list all of the import jobs for your account
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** List

- **   [ListMultiRegionEndpoints](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListMultiRegionEndpoints.html)  **
  - **Description:** Grants permission to list all of the multi-region endpoints for your account
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** List

- **   [ListRecommendations](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListRecommendations.html)  **
  - **Description:** Grants permission to list recommendations for your account
  - **Resource types (\*required):** [identity](#list_sesv2-resource-identity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Read

- **   [ListReputationEntities](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListReputationEntities.html)  **
  - **Description:** Grants permission to retrieve a list of reputation entities
  - **Resource types (\*required):** [tenant\*](#list_sesv2-resource-tenant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** List

- **   [ListResourceTenants](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListResourceTenants)  **
  - **Description:** Grants permission to list all the tenants associated to a SES resource
  - **Resource types (\*required):** [configuration-set\*](#list_sesv2-resource-configuration-set) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [identity\*](#list_sesv2-resource-identity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [template\*](#list_sesv2-resource-template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** List

- **   [ListSuppressedDestinations](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListSuppressedDestinations.html)  **
  - **Description:** Grants permission to list email addresses that are on the suppression list for your account or tenant
  - **Resource types (\*required):** [tenant](#list_sesv2-resource-tenant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to retrieve a list of the tags (keys and values) that are associated with a specific resource for your account
  - **Resource types (\*required):** [configuration-set](#list_sesv2-resource-configuration-set) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [contact-list](#list_sesv2-resource-contact-list) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [custom-verification-email-template](#list_sesv2-resource-custom-verification-email-template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [dedicated-ip-pool](#list_sesv2-resource-dedicated-ip-pool) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [deliverability-test-report](#list_sesv2-resource-deliverability-test-report) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [identity](#list_sesv2-resource-identity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [mailmanager-archive](#list_sesv2-resource-mailmanager-archive) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [template](#list_sesv2-resource-template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [tenant](#list_sesv2-resource-tenant) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Read

- **   [ListTenantResources](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListTenantResources)  **
  - **Description:** Grants permission to list all the resources associated to a tenant
  - **Resource types (\*required):** [tenant\*](#list_sesv2-resource-tenant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** List

- **   [ListTenants](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListTenants)  **
  - **Description:** Grants permission to list all the tenants for your account
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** List

- **   [PutAccountDedicatedIpWarmupAttributes](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutAccountDedicatedIpWarmupAttributes.html)  **
  - **Description:** Grants permission to enable or disable the automatic warm-up feature for dedicated IP addresses
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [PutAccountDetails](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutAccountDetails.html)  **
  - **Description:** Grants permission to update your account details
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [PutAccountPricingAttributes](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutAccountPricingAttributes.html)  **
  - **Description:** Grants permission to set the pricing plan for your account
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [PutAccountSendingAttributes](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutAccountSendingAttributes.html)  **
  - **Description:** Grants permission to enable or disable the ability to send email for your account
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [PutAccountSuppressionAttributes](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutAccountSuppressionAttributes.html)  **
  - **Description:** Grants permission to change the settings for the account-level suppression list
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [PutAccountVdmAttributes](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutAccountVdmAttributes.html)  **
  - **Description:** Grants permission to change the settings for VDM for your account
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [PutConfigurationSetArchivingOptions](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutConfigurationSetArchivingOptions.html)  **
  - **Description:** Grants permission to associate a configuration set with a Mail Manager archive
  - **Resource types (\*required):** [configuration-set\*](#list_sesv2-resource-configuration-set) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [mailmanager-archive](#list_sesv2-resource-mailmanager-archive) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [PutConfigurationSetDeliveryOptions](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutConfigurationSetDeliveryOptions.html)  **
  - **Description:** Grants permission to associate a configuration set with a dedicated IP pool
  - **Resource types (\*required):** [configuration-set\*](#list_sesv2-resource-configuration-set) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [dedicated-ip-pool](#list_sesv2-resource-dedicated-ip-pool) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [PutConfigurationSetReputationOptions](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutConfigurationSetReputationOptions.html)  **
  - **Description:** Grants permission to enable or disable collection of reputation metrics for emails that you send using a particular configuration set
  - **Resource types (\*required):** [configuration-set\*](#list_sesv2-resource-configuration-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [PutConfigurationSetSendingOptions](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutConfigurationSetSendingOptions.html)  **
  - **Description:** Grants permission to enable or disable email sending for messages that use a particular configuration set
  - **Resource types (\*required):** [configuration-set\*](#list_sesv2-resource-configuration-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [PutConfigurationSetSuppressionOptions](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutConfigurationSetSuppressionOptions.html)  **
  - **Description:** Grants permission to specify the account suppression list preferences for a particular configuration set
  - **Resource types (\*required):** [configuration-set\*](#list_sesv2-resource-configuration-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [PutConfigurationSetTrackingOptions](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutConfigurationSetTrackingOptions.html)  **
  - **Description:** Grants permission to specify a custom domain to use for open and click tracking elements in email that you send for a particular configuration set
  - **Resource types (\*required):** [configuration-set\*](#list_sesv2-resource-configuration-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [PutConfigurationSetVdmOptions](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutConfigurationSetVdmOptions.html)  **
  - **Description:** Grants permission to override account-level VDM settings for a particular configuration set
  - **Resource types (\*required):** [configuration-set\*](#list_sesv2-resource-configuration-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [PutDedicatedIpInPool](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutDedicatedIpInPool.html)  **
  - **Description:** Grants permission to move a dedicated IP address to an existing dedicated IP pool
  - **Resource types (\*required):** [dedicated-ip-pool\*](#list_sesv2-resource-dedicated-ip-pool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [PutDedicatedIpPoolScalingAttributes](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutDedicatedIpPoolScalingAttributes.html)  **
  - **Description:** Grants permission to transition a dedicated IP pool from Standard to Managed
  - **Resource types (\*required):** [dedicated-ip-pool\*](#list_sesv2-resource-dedicated-ip-pool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [PutDedicatedIpWarmupAttributes](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutDedicatedIpWarmupAttributes.html)  **
  - **Description:** Grants permission to put Dedicated IP warm up attributes
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [PutDeliverabilityDashboardOption](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutDeliverabilityDashboardOption.html)  **
  - **Description:** Grants permission to enable or disable the Deliverability dashboard
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [PutEmailIdentityConfigurationSetAttributes](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutEmailIdentityConfigurationSetAttributes.html)  **
  - **Description:** Grants permission to associate a configuration set with an email identity
  - **Resource types (\*required):** [configuration-set](#list_sesv2-resource-configuration-set) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [identity\*](#list_sesv2-resource-identity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [PutEmailIdentityDkimAttributes](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutEmailIdentityDkimAttributes.html)  **
  - **Description:** Grants permission to enable or disable DKIM authentication for an email identity
  - **Resource types (\*required):** [identity\*](#list_sesv2-resource-identity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [PutEmailIdentityDkimSigningAttributes](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutEmailIdentityDkimSigningAttributes.html)  **
  - **Description:** Grants permission to configure or change the DKIM authentication settings for an email domain identity
  - **Resource types (\*required):** [identity\*](#list_sesv2-resource-identity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [PutEmailIdentityFeedbackAttributes](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutEmailIdentityFeedbackAttributes.html)  **
  - **Description:** Grants permission to enable or disable feedback forwarding for an email identity
  - **Resource types (\*required):** [identity\*](#list_sesv2-resource-identity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [PutEmailIdentityMailFromAttributes](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutEmailIdentityMailFromAttributes.html)  **
  - **Description:** Grants permission to enable or disable the custom MAIL FROM domain configuration for an email identity
  - **Resource types (\*required):** [identity\*](#list_sesv2-resource-identity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [PutSuppressedDestination](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutSuppressedDestination.html)  **
  - **Description:** Grants permission to add an email address to the suppression list for your account or tenant
  - **Resource types (\*required):** [tenant](#list_sesv2-resource-tenant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [PutTenantSuppressionAttributes](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutTenantSuppressionAttributes.html)  **
  - **Description:** Grants permission to change the settings for the tenant-level suppression list
  - **Resource types (\*required):** [tenant\*](#list_sesv2-resource-tenant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [SendBulkEmail](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_SendBulkEmail.html)  **
  - **Description:** Grants permission to compose an email message to multiple destinations
  - **Resource types (\*required):** [configuration-set](#list_sesv2-resource-configuration-set) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)<br />[ses:MultiRegionEndpointId](#list_sesv2-ses_MultiRegionEndpointId)<br />[ses:TenantName](#list_sesv2-ses_TenantName)
  - **Resource types (\*required):** [identity\*](#list_sesv2-resource-identity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)<br />[ses:MultiRegionEndpointId](#list_sesv2-ses_MultiRegionEndpointId)<br />[ses:TenantName](#list_sesv2-ses_TenantName)
  - **Resource types (\*required):** [template\*](#list_sesv2-resource-template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)<br />[ses:MultiRegionEndpointId](#list_sesv2-ses_MultiRegionEndpointId)<br />[ses:TenantName](#list_sesv2-ses_TenantName)
  - **Access level:** Write

- **   [SendCustomVerificationEmail](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_SendCustomVerificationEmail.html)  **
  - **Description:** Grants permission to add an email address to the list of identities and attempts to verify it
  - **Resource types (\*required):** [custom-verification-email-template\*](#list_sesv2-resource-custom-verification-email-template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)<br />[ses:FeedbackAddress](#list_sesv2-ses_FeedbackAddress)<br />[ses:FromAddress](#list_sesv2-ses_FromAddress)<br />[ses:FromDisplayName](#list_sesv2-ses_FromDisplayName)<br />[ses:Recipients](#list_sesv2-ses_Recipients)
  - **Resource types (\*required):** [identity](#list_sesv2-resource-identity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)<br />[ses:FeedbackAddress](#list_sesv2-ses_FeedbackAddress)<br />[ses:FromAddress](#list_sesv2-ses_FromAddress)<br />[ses:FromDisplayName](#list_sesv2-ses_FromDisplayName)<br />[ses:Recipients](#list_sesv2-ses_Recipients)
  - **Access level:** Write

- **   [SendEmail](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_SendEmail.html)  **
  - **Description:** Grants permission to send an email message
  - **Resource types (\*required):** [configuration-set](#list_sesv2-resource-configuration-set) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)<br />[ses:FeedbackAddress](#list_sesv2-ses_FeedbackAddress)<br />[ses:FromAddress](#list_sesv2-ses_FromAddress)<br />[ses:FromDisplayName](#list_sesv2-ses_FromDisplayName)<br />[ses:MultiRegionEndpointId](#list_sesv2-ses_MultiRegionEndpointId)<br />[ses:Recipients](#list_sesv2-ses_Recipients)<br />[ses:TenantName](#list_sesv2-ses_TenantName)
  - **Resource types (\*required):** [identity\*](#list_sesv2-resource-identity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)<br />[ses:FeedbackAddress](#list_sesv2-ses_FeedbackAddress)<br />[ses:FromAddress](#list_sesv2-ses_FromAddress)<br />[ses:FromDisplayName](#list_sesv2-ses_FromDisplayName)<br />[ses:MultiRegionEndpointId](#list_sesv2-ses_MultiRegionEndpointId)<br />[ses:Recipients](#list_sesv2-ses_Recipients)<br />[ses:TenantName](#list_sesv2-ses_TenantName)
  - **Resource types (\*required):** [template](#list_sesv2-resource-template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)<br />[ses:FeedbackAddress](#list_sesv2-ses_FeedbackAddress)<br />[ses:FromAddress](#list_sesv2-ses_FromAddress)<br />[ses:FromDisplayName](#list_sesv2-ses_FromDisplayName)<br />[ses:MultiRegionEndpointId](#list_sesv2-ses_MultiRegionEndpointId)<br />[ses:Recipients](#list_sesv2-ses_Recipients)<br />[ses:TenantName](#list_sesv2-ses_TenantName)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_TagResource.html)  **
  - **Description:** Grants permission to add one or more tags (keys and values) to a specified resource
  - **Resource types (\*required):** [configuration-set](#list_sesv2-resource-configuration-set) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sesv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [contact-list](#list_sesv2-resource-contact-list) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sesv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [custom-verification-email-template](#list_sesv2-resource-custom-verification-email-template) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sesv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [dedicated-ip-pool](#list_sesv2-resource-dedicated-ip-pool) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sesv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [deliverability-test-report](#list_sesv2-resource-deliverability-test-report) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sesv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [identity](#list_sesv2-resource-identity) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sesv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [mailmanager-archive](#list_sesv2-resource-mailmanager-archive) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sesv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [template](#list_sesv2-resource-template) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sesv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [tenant](#list_sesv2-resource-tenant) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sesv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Tagging, Write

- **   [TestRenderEmailTemplate](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_TestRenderEmailTemplate.html)  **
  - **Description:** Grants permission to create a preview of the MIME content of an email when provided with a template and a set of replacement data
  - **Resource types (\*required):** [template\*](#list_sesv2-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_UntagResource.html)  **
  - **Description:** Grants permission to remove one or more tags (keys and values) from a specified resource
  - **Resource types (\*required):** [configuration-set](#list_sesv2-resource-configuration-set) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [contact-list](#list_sesv2-resource-contact-list) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [custom-verification-email-template](#list_sesv2-resource-custom-verification-email-template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [dedicated-ip-pool](#list_sesv2-resource-dedicated-ip-pool) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [deliverability-test-report](#list_sesv2-resource-deliverability-test-report) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [identity](#list_sesv2-resource-identity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [mailmanager-archive](#list_sesv2-resource-mailmanager-archive) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [template](#list_sesv2-resource-template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [tenant](#list_sesv2-resource-tenant) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sesv2-aws_TagKeys)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Tagging, Write

- **   [UpdateConfigurationSetEventDestination](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_UpdateConfigurationSetEventDestination.html)  **
  - **Description:** Grants permission to update the configuration of an event destination for a configuration set
  - **Resource types (\*required):** [configuration-set\*](#list_sesv2-resource-configuration-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [UpdateContact](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_UpdateContact.html)  **
  - **Description:** Grants permission to update a contact's preferences for a list
  - **Resource types (\*required):** [contact-list\*](#list_sesv2-resource-contact-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [UpdateContactList](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_UpdateContactList.html)  **
  - **Description:** Grants permission to update contact list metadata
  - **Resource types (\*required):** [contact-list\*](#list_sesv2-resource-contact-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [UpdateCustomVerificationEmailTemplate](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_UpdateCustomVerificationEmailTemplate.html)  **
  - **Description:** Grants permission to update an existing custom verification email template
  - **Resource types (\*required):** [custom-verification-email-template\*](#list_sesv2-resource-custom-verification-email-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [UpdateEmailIdentityPolicy](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_UpdateEmailIdentityPolicy.html)  **
  - **Description:** Grants permission to update the specified sending authorization policy for the given identity (an email address or a domain)
  - **Resource types (\*required):** [identity\*](#list_sesv2-resource-identity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Permissions management, Write

- **   [UpdateEmailTemplate](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_UpdateEmailTemplate.html)  **
  - **Description:** Grants permission to update an email template
  - **Resource types (\*required):** [template\*](#list_sesv2-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [UpdateReputationEntityCustomerManagedStatus](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_UpdateReputationEntityCustomerManagedStatus.html)  **
  - **Description:** Grants permission to update the customer-managed sending status
  - **Resource types (\*required):** [tenant\*](#list_sesv2-resource-tenant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write

- **   [UpdateReputationEntityPolicy](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_UpdateReputationEntityPolicy.html)  **
  - **Description:** Grants permission to assign a reputation policy
  - **Resource types (\*required):** [reputation-policy\*](#list_sesv2-resource-reputation-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Resource types (\*required):** [tenant\*](#list_sesv2-resource-tenant) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_sesv2-ses_ApiVersion)
  - **Access level:** Write



## Permission-only actions for Amazon Simple Email Service v2
<a name="list_sesv2-permission-only-actions"></a>

The following actions are defined by Amazon Simple Email Service v2 but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   ReplicateEmailIdentityDkimSigningKey  **
  - **Description:** Grants permission to replicate email identity DKIM signing key
  - **Resource types (\*required):** [identity\*](#list_sesv2-resource-identity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_)<br />[ses:ReplicaRegion](#list_sesv2-ses_ReplicaRegion)
  - **Access level:** Permissions management, Write



## Resource types defined by Amazon Simple Email Service v2
<a name="list_sesv2-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [configuration-set](https://docs.aws.amazon.com/ses/latest/APIReference/API_ConfigurationSet.html)  | arn:${Partition}:ses:${Region}:${Account}:configuration-set/${ConfigurationSetName} | [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_) | 
|  [contact-list](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ContactList.html)  | arn:${Partition}:ses:${Region}:${Account}:contact-list/${ContactListName} | [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_) | 
|  [custom-verification-email-template](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_CustomVerificationEmailTemplateMetadata.html)  | arn:${Partition}:ses:${Region}:${Account}:custom-verification-email-template/${TemplateName} | [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_) | 
|  [dedicated-ip-pool](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_DedicatedIp.html)  | arn:${Partition}:ses:${Region}:${Account}:dedicated-ip-pool/${DedicatedIPPool} | [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_) | 
|  [deliverability-test-report](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_DeliverabilityTestReport.html)  | arn:${Partition}:ses:${Region}:${Account}:deliverability-test-report/${ReportId} | [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_) | 
|  [export-job](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ExportJobSummary.html)  | arn:${Partition}:ses:${Region}:${Account}:export-job/${ExportJobId} |   | 
|  [identity](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_IdentityInfo.html)  | arn:${Partition}:ses:${Region}:${Account}:identity/${IdentityName} | [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_) | 
|  [import-job](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ImportJobSummary.html)  | arn:${Partition}:ses:${Region}:${Account}:import-job/${ImportJobId} |   | 
|  [mailmanager-archive](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_Archive.html)  | arn:${Partition}:ses:${Region}:${Account}:mailmanager-archive/${ArchiveId} | [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_) | 
|  [multi-region-endpoint](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_MultiRegionEndpoint.html)  | arn:${Partition}:ses:${Region}:${Account}:multi-region-endpoint/${EndpointName} |   | 
|  [reputation-policy](https://docs.aws.amazon.com/ses/latest/APIReference/API_ReputationPolicy.html)  | arn:${Partition}:ses:${Region}:aws:reputation-policy/${ReputationPolicyName} |   | 
|  [template](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_Template.html)  | arn:${Partition}:ses:${Region}:${Account}:template/${TemplateName} | [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_) | 
|  [tenant](https://docs.aws.amazon.com/ses/latest/APIReference/API_Tenant.html)  | arn:${Partition}:ses:${Region}:${Account}:tenant/${TenantName}/${TenantId} | [aws:ResourceTag/${TagKey}](#list_sesv2-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Simple Email Service v2
<a name="list_sesv2-policy-keys"></a>

Amazon Simple Email Service v2 defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 
|   [ses:ApiVersion](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonses.html#amazonses-policy-keys)  | Filters access by the SES API version | String | 
|   [ses:ExportSourceType](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonses.html#amazonses-policy-keys)  | Filters access by the export source type | String | 
|   [ses:FeedbackAddress](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonses.html#amazonses-policy-keys)  | Filters access by the "Return-Path" address, which specifies where bounces and complaints are sent by email feedback forwarding | String | 
|   [ses:FromAddress](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonses.html#amazonses-policy-keys)  | Filters access by the "From" address of a message | String | 
|   [ses:FromDisplayName](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonses.html#amazonses-policy-keys)  | Filters access by the "From" address that is used as the display name of a message | String | 
|   [ses:MultiRegionEndpointId](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonses.html#amazonses-policy-keys)  | Filters access by the multi-region endpoint ID that is used to send email | String | 
|   [ses:Recipients](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonses.html#amazonses-policy-keys)  | Filters access by the recipient addresses of a message, which include the "To", "CC", and "BCC" addresses | ArrayOfString | 
|   [ses:ReplicaRegion](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonses.html#amazonses-policy-keys)  | Filters access by the replica regions for Replicating domain DKIM signing key | ArrayOfString | 
|   [ses:TenantName](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonses.html#amazonses-policy-keys)  | Filters access by the tenant name that is used to send email | String | 