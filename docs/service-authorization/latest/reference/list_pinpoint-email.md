

# Actions, resources, and condition keys for Amazon Pinpoint Email Service
<a name="list_pinpoint-email"></a>

Amazon Pinpoint Email Service (service prefix: `ses`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/pinpoint/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization-policies.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/ses/ses.json) for this service.

**Topics**
+ [API operations defined by Amazon Pinpoint Email Service](#list_pinpoint-email-operations)
+ [Actions defined by Amazon Pinpoint Email Service](#list_pinpoint-email-actions-as-permissions)
+ [Resource types defined by Amazon Pinpoint Email Service](#list_pinpoint-email-resources-for-iam-policies)
+ [Condition keys for Amazon Pinpoint Email Service](#list_pinpoint-email-policy-keys)

## API operations defined by Amazon Pinpoint Email Service
<a name="list_pinpoint-email-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_pinpoint-email-actions-as-permissions).




- **   CreateConfigurationSet  **
  - **IAM action:**  [ses:CreateConfigurationSet](#list_pinpoint-email-action-CreateConfigurationSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ses:TagResource](#list_pinpoint-email-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateConfigurationSetEventDestination  **
  - **IAM action:**  [ses:CreateConfigurationSetEventDestination](#list_pinpoint-email-action-CreateConfigurationSetEventDestination)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ses.amazonaws.com / **Access level:** Write

- **   CreateDedicatedIpPool  **
  - **IAM action:**  [ses:CreateDedicatedIpPool](#list_pinpoint-email-action-CreateDedicatedIpPool)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ses:TagResource](#list_pinpoint-email-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDeliverabilityTestReport  **
  - **IAM action:**  [ses:CreateDeliverabilityTestReport](#list_pinpoint-email-action-CreateDeliverabilityTestReport)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ses:TagResource](#list_pinpoint-email-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateEmailIdentity  **
  - **IAM action:**  [ses:CreateEmailIdentity](#list_pinpoint-email-action-CreateEmailIdentity)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ses:TagResource](#list_pinpoint-email-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteConfigurationSet  **
  - **IAM action:**  [ses:DeleteConfigurationSet](#list_pinpoint-email-action-DeleteConfigurationSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConfigurationSetEventDestination  **
  - **IAM action:**  [ses:DeleteConfigurationSetEventDestination](#list_pinpoint-email-action-DeleteConfigurationSetEventDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDedicatedIpPool  **
  - **IAM action:**  [ses:DeleteDedicatedIpPool](#list_pinpoint-email-action-DeleteDedicatedIpPool) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEmailIdentity  **
  - **IAM action:**  [ses:DeleteEmailIdentity](#list_pinpoint-email-action-DeleteEmailIdentity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAccount  **
  - **IAM action:**  [ses:GetAccount](#list_pinpoint-email-action-GetAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBlacklistReports  **
  - **IAM action:**  [ses:GetBlacklistReports](#list_pinpoint-email-action-GetBlacklistReports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConfigurationSet  **
  - **IAM action:**  [ses:GetConfigurationSet](#list_pinpoint-email-action-GetConfigurationSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConfigurationSetEventDestinations  **
  - **IAM action:**  [ses:GetConfigurationSetEventDestinations](#list_pinpoint-email-action-GetConfigurationSetEventDestinations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDedicatedIp  **
  - **IAM action:**  [ses:GetDedicatedIp](#list_pinpoint-email-action-GetDedicatedIp) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDedicatedIps  **
  - **IAM action:**  [ses:GetDedicatedIps](#list_pinpoint-email-action-GetDedicatedIps) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDeliverabilityDashboardOptions  **
  - **IAM action:**  [ses:GetDeliverabilityDashboardOptions](#list_pinpoint-email-action-GetDeliverabilityDashboardOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDeliverabilityTestReport  **
  - **IAM action:**  [ses:GetDeliverabilityTestReport](#list_pinpoint-email-action-GetDeliverabilityTestReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDomainDeliverabilityCampaign  **
  - **IAM action:**  [ses:GetDomainDeliverabilityCampaign](#list_pinpoint-email-action-GetDomainDeliverabilityCampaign) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDomainStatisticsReport  **
  - **IAM action:**  [ses:GetDomainStatisticsReport](#list_pinpoint-email-action-GetDomainStatisticsReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEmailIdentity  **
  - **IAM action:**  [ses:GetEmailIdentity](#list_pinpoint-email-action-GetEmailIdentity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListConfigurationSets  **
  - **IAM action:**  [ses:ListConfigurationSets](#list_pinpoint-email-action-ListConfigurationSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDedicatedIpPools  **
  - **IAM action:**  [ses:ListDedicatedIpPools](#list_pinpoint-email-action-ListDedicatedIpPools) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDeliverabilityTestReports  **
  - **IAM action:**  [ses:ListDeliverabilityTestReports](#list_pinpoint-email-action-ListDeliverabilityTestReports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDomainDeliverabilityCampaigns  **
  - **IAM action:**  [ses:ListDomainDeliverabilityCampaigns](#list_pinpoint-email-action-ListDomainDeliverabilityCampaigns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListEmailIdentities  **
  - **IAM action:**  [ses:ListEmailIdentities](#list_pinpoint-email-action-ListEmailIdentities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [ses:ListTagsForResource](#list_pinpoint-email-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutAccountDedicatedIpWarmupAttributes  **
  - **IAM action:**  [ses:PutAccountDedicatedIpWarmupAttributes](#list_pinpoint-email-action-PutAccountDedicatedIpWarmupAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutAccountSendingAttributes  **
  - **IAM action:**  [ses:PutAccountSendingAttributes](#list_pinpoint-email-action-PutAccountSendingAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutConfigurationSetDeliveryOptions  **
  - **IAM action:**  [ses:PutConfigurationSetDeliveryOptions](#list_pinpoint-email-action-PutConfigurationSetDeliveryOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutConfigurationSetReputationOptions  **
  - **IAM action:**  [ses:PutConfigurationSetReputationOptions](#list_pinpoint-email-action-PutConfigurationSetReputationOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutConfigurationSetSendingOptions  **
  - **IAM action:**  [ses:PutConfigurationSetSendingOptions](#list_pinpoint-email-action-PutConfigurationSetSendingOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutConfigurationSetTrackingOptions  **
  - **IAM action:**  [ses:PutConfigurationSetTrackingOptions](#list_pinpoint-email-action-PutConfigurationSetTrackingOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutDedicatedIpInPool  **
  - **IAM action:**  [ses:PutDedicatedIpInPool](#list_pinpoint-email-action-PutDedicatedIpInPool) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutDedicatedIpWarmupAttributes  **
  - **IAM action:**  [ses:PutDedicatedIpWarmupAttributes](#list_pinpoint-email-action-PutDedicatedIpWarmupAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutDeliverabilityDashboardOption  **
  - **IAM action:**  [ses:PutDeliverabilityDashboardOption](#list_pinpoint-email-action-PutDeliverabilityDashboardOption) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutEmailIdentityDkimAttributes  **
  - **IAM action:**  [ses:PutEmailIdentityDkimAttributes](#list_pinpoint-email-action-PutEmailIdentityDkimAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutEmailIdentityFeedbackAttributes  **
  - **IAM action:**  [ses:PutEmailIdentityFeedbackAttributes](#list_pinpoint-email-action-PutEmailIdentityFeedbackAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutEmailIdentityMailFromAttributes  **
  - **IAM action:**  [ses:PutEmailIdentityMailFromAttributes](#list_pinpoint-email-action-PutEmailIdentityMailFromAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [ses:TagResource](#list_pinpoint-email-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [ses:UntagResource](#list_pinpoint-email-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateConfigurationSetEventDestination  **
  - **IAM action:**  [ses:UpdateConfigurationSetEventDestination](#list_pinpoint-email-action-UpdateConfigurationSetEventDestination)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ses.amazonaws.com / **Access level:** Write



## Actions defined by Amazon Pinpoint Email Service
<a name="list_pinpoint-email-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateConfigurationSet](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_CreateConfigurationSet.html)  **
  - **Description:** Grants permission to create a configuration set
  - **Resource types (\*required):** [configuration-set](#list_pinpoint-email-resource-configuration-set) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-email-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-email-aws_TagKeys)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Resource types (\*required):** [dedicated-ip-pool](#list_pinpoint-email-resource-dedicated-ip-pool) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-email-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-email-aws_TagKeys)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Write

- **   [CreateConfigurationSetEventDestination](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_CreateConfigurationSetEventDestination.html)  **
  - **Description:** Grants permission to create a configuration set event destination
  - **Resource types (\*required):** [configuration-set\*](#list_pinpoint-email-resource-configuration-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Write

- **   [CreateDedicatedIpPool](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_CreateDedicatedIpPool.html)  **
  - **Description:** Grants permission to create a new pool of dedicated IP addresses
  - **Resource types (\*required):** [dedicated-ip-pool](#list_pinpoint-email-resource-dedicated-ip-pool)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-email-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-email-aws_TagKeys)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Write

- **   [CreateDeliverabilityTestReport](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_CreateDeliverabilityTestReport.html)  **
  - **Description:** Grants permission to create a new predictive inbox placement test
  - **Resource types (\*required):** [identity\*](#list_pinpoint-email-resource-identity)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-email-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-email-aws_TagKeys)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Write

- **   [CreateEmailIdentity](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_CreateEmailIdentity.html)  **
  - **Description:** Grants permission to start the process of verifying an email identity
  - **Resource types (\*required):** [identity](#list_pinpoint-email-resource-identity)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-email-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-email-aws_TagKeys)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Write

- **   [DeleteConfigurationSet](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DeleteConfigurationSet.html)  **
  - **Description:** Grants permission to delete an existing configuration set
  - **Resource types (\*required):** [configuration-set\*](#list_pinpoint-email-resource-configuration-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Write

- **   [DeleteConfigurationSetEventDestination](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DeleteConfigurationSetEventDestination.html)  **
  - **Description:** Grants permission to delete an event destination
  - **Resource types (\*required):** [configuration-set\*](#list_pinpoint-email-resource-configuration-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Write

- **   [DeleteDedicatedIpPool](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DeleteDedicatedIpPool.html)  **
  - **Description:** Grants permission to delete a dedicated IP pool
  - **Resource types (\*required):** [dedicated-ip-pool\*](#list_pinpoint-email-resource-dedicated-ip-pool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Write

- **   [DeleteEmailIdentity](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DeleteEmailIdentity.html)  **
  - **Description:** Grants permission to delete an email identity that you previously verified
  - **Resource types (\*required):** [identity\*](#list_pinpoint-email-resource-identity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Write

- **   [GetAccount](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_GetAccount.html)  **
  - **Description:** Grants permission to get information about the email-sending status and capabilities
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Read

- **   [GetBlacklistReports](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_GetBlacklistReports.html)  **
  - **Description:** Grants permission to retrieve a list of the deny lists on which your dedicated IP addresses appear
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Read

- **   [GetConfigurationSet](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_GetConfigurationSet.html)  **
  - **Description:** Grants permission to get information about an existing configuration set
  - **Resource types (\*required):** [configuration-set\*](#list_pinpoint-email-resource-configuration-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Read

- **   [GetConfigurationSetEventDestinations](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_GetConfigurationSetEventDestinations.html)  **
  - **Description:** Grants permission to retrieve a list of event destinations that are associated with a configuration set
  - **Resource types (\*required):** [configuration-set\*](#list_pinpoint-email-resource-configuration-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Read

- **   [GetDedicatedIp](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_GetDedicatedIp.html)  **
  - **Description:** Grants permission to get information about a dedicated IP address
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Read

- **   [GetDedicatedIps](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_GetDedicatedIps.html)  **
  - **Description:** Grants permission to list the dedicated IP addresses that are associated with your account
  - **Resource types (\*required):** [dedicated-ip-pool\*](#list_pinpoint-email-resource-dedicated-ip-pool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Read

- **   [GetDeliverabilityDashboardOptions](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_GetDeliverabilityDashboardOptions.html)  **
  - **Description:** Grants permission to get the status of the Deliverability dashboard
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Read

- **   [GetDeliverabilityTestReport](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_GetDeliverabilityTestReport.html)  **
  - **Description:** Grants permission to retrieve the results of a predictive inbox placement test
  - **Resource types (\*required):** [deliverability-test-report\*](#list_pinpoint-email-resource-deliverability-test-report)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Read

- **   [GetDomainDeliverabilityCampaign](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_GetDomainDeliverabilityCampaign.html)  **
  - **Description:** Grants permission to retrieve all the deliverability data for a specific campaign
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Read

- **   [GetDomainStatisticsReport](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_GetDomainStatisticsReport.html)  **
  - **Description:** Grants permission to retrieve inbox placement and engagement rates for the domains that you use to send email
  - **Resource types (\*required):** [identity\*](#list_pinpoint-email-resource-identity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Read

- **   [GetEmailIdentity](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_GetEmailIdentity.html)  **
  - **Description:** Grants permission to get information about a specific identity associated with your account
  - **Resource types (\*required):** [identity\*](#list_pinpoint-email-resource-identity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Read

- **   [ListConfigurationSets](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_ListConfigurationSets.html)  **
  - **Description:** Grants permission to list all of the configuration sets associated with your account
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** List

- **   [ListDedicatedIpPools](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_ListDedicatedIpPools.html)  **
  - **Description:** Grants permission to list all of the dedicated IP pools that exist in your account
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** List

- **   [ListDeliverabilityTestReports](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_ListDeliverabilityTestReports.html)  **
  - **Description:** Grants permission to retrieve a list of the predictive inbox placement tests that you've performed, regardless of their statuses
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** List

- **   [ListDomainDeliverabilityCampaigns](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_ListDomainDeliverabilityCampaigns.html)  **
  - **Description:** Grants permission to retrieve deliverability data for all the campaigns that used a specific domain to send email during a specified time range
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Read

- **   [ListEmailIdentities](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_ListEmailIdentities.html)  **
  - **Description:** Grants permission to list all of the email identities that are associated with your account
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to retrieve a list of the tags (keys and values) that are associated with a specific resource
  - **Resource types (\*required):** [configuration-set](#list_pinpoint-email-resource-configuration-set) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Resource types (\*required):** [dedicated-ip-pool](#list_pinpoint-email-resource-dedicated-ip-pool) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Resource types (\*required):** [deliverability-test-report](#list_pinpoint-email-resource-deliverability-test-report) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Resource types (\*required):** [identity](#list_pinpoint-email-resource-identity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Read

- **   [PutAccountDedicatedIpWarmupAttributes](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutAccountDedicatedIpWarmupAttributes.html)  **
  - **Description:** Grants permission to enable or disable the automatic warm-up feature for dedicated IP addresses
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Write

- **   [PutAccountSendingAttributes](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutAccountSendingAttributes.html)  **
  - **Description:** Grants permission to enable or disable the ability of your account to send email
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Write

- **   [PutConfigurationSetDeliveryOptions](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutConfigurationSetDeliveryOptions.html)  **
  - **Description:** Grants permission to associate a configuration set with a dedicated IP pool
  - **Resource types (\*required):** [configuration-set\*](#list_pinpoint-email-resource-configuration-set) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Resource types (\*required):** [dedicated-ip-pool](#list_pinpoint-email-resource-dedicated-ip-pool) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Write

- **   [PutConfigurationSetReputationOptions](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutConfigurationSetReputationOptions.html)  **
  - **Description:** Grants permission to enable or disable collection of reputation metrics for emails that you send using a particular configuration set
  - **Resource types (\*required):** [configuration-set\*](#list_pinpoint-email-resource-configuration-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Write

- **   [PutConfigurationSetSendingOptions](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutConfigurationSetSendingOptions.html)  **
  - **Description:** Grants permission to enable or disable email sending for messages that use a particular configuration set
  - **Resource types (\*required):** [configuration-set\*](#list_pinpoint-email-resource-configuration-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Write

- **   [PutConfigurationSetTrackingOptions](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutConfigurationSetTrackingOptions.html)  **
  - **Description:** Grants permission to specify a custom domain to use for open and click tracking elements in email that you send using a particular configuration set
  - **Resource types (\*required):** [configuration-set\*](#list_pinpoint-email-resource-configuration-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Write

- **   [PutDedicatedIpInPool](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutDedicatedIpInPool.html)  **
  - **Description:** Grants permission to move a dedicated IP address to an existing dedicated IP pool
  - **Resource types (\*required):** [dedicated-ip-pool\*](#list_pinpoint-email-resource-dedicated-ip-pool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Write

- **   [PutDedicatedIpWarmupAttributes](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutDedicatedIpWarmupAttributes.html)  **
  - **Description:** Grants permission to enable dedicated IP warm up attributes
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Write

- **   [PutDeliverabilityDashboardOption](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutDeliverabilityDashboardOption.html)  **
  - **Description:** Grants permission to enable or disable the Deliverability dashboard
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Write

- **   [PutEmailIdentityDkimAttributes](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutEmailIdentityDkimAttributes.html)  **
  - **Description:** Grants permission to enable or disable DKIM authentication for an email identity
  - **Resource types (\*required):** [identity\*](#list_pinpoint-email-resource-identity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Write

- **   [PutEmailIdentityFeedbackAttributes](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutEmailIdentityFeedbackAttributes.html)  **
  - **Description:** Grants permission to enable or disable feedback forwarding for an identity
  - **Resource types (\*required):** [identity\*](#list_pinpoint-email-resource-identity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Write

- **   [PutEmailIdentityMailFromAttributes](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutEmailIdentityMailFromAttributes.html)  **
  - **Description:** Grants permission to enable or disable the custom MAIL FROM domain configuration for an email identity
  - **Resource types (\*required):** [identity\*](#list_pinpoint-email-resource-identity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Write

- **   [SendEmail](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_SendEmail.html)  **
  - **Description:** Grants permission to send an email message
  - **Resource types (\*required):** [configuration-set](#list_pinpoint-email-resource-configuration-set) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)<br />[ses:FeedbackAddress](#list_pinpoint-email-ses_FeedbackAddress)<br />[ses:FromAddress](#list_pinpoint-email-ses_FromAddress)<br />[ses:FromDisplayName](#list_pinpoint-email-ses_FromDisplayName)<br />[ses:Recipients](#list_pinpoint-email-ses_Recipients)
  - **Resource types (\*required):** [identity\*](#list_pinpoint-email-resource-identity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)<br />[ses:FeedbackAddress](#list_pinpoint-email-ses_FeedbackAddress)<br />[ses:FromAddress](#list_pinpoint-email-ses_FromAddress)<br />[ses:FromDisplayName](#list_pinpoint-email-ses_FromDisplayName)<br />[ses:Recipients](#list_pinpoint-email-ses_Recipients)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add one or more tags (keys and values) to a specified resource
  - **Resource types (\*required):** [configuration-set](#list_pinpoint-email-resource-configuration-set) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-email-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-email-aws_TagKeys)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Resource types (\*required):** [dedicated-ip-pool](#list_pinpoint-email-resource-dedicated-ip-pool) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-email-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-email-aws_TagKeys)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Resource types (\*required):** [deliverability-test-report](#list_pinpoint-email-resource-deliverability-test-report) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-email-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-email-aws_TagKeys)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Resource types (\*required):** [identity](#list_pinpoint-email-resource-identity) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pinpoint-email-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-email-aws_TagKeys)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove one or more tags (keys and values) from a specified resource
  - **Resource types (\*required):** [configuration-set](#list_pinpoint-email-resource-configuration-set) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-email-aws_TagKeys)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Resource types (\*required):** [dedicated-ip-pool](#list_pinpoint-email-resource-dedicated-ip-pool) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-email-aws_TagKeys)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Resource types (\*required):** [deliverability-test-report](#list_pinpoint-email-resource-deliverability-test-report) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-email-aws_TagKeys)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Resource types (\*required):** [identity](#list_pinpoint-email-resource-identity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pinpoint-email-aws_TagKeys)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Tagging, Write

- **   [UpdateConfigurationSetEventDestination](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_UpdateConfigurationSetEventDestination.html)  **
  - **Description:** Grants permission to update the configuration of an event destination for a configuration set
  - **Resource types (\*required):** [configuration-set\*](#list_pinpoint-email-resource-configuration-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_)<br />[ses:ApiVersion](#list_pinpoint-email-ses_ApiVersion)
  - **Access level:** Write



## Resource types defined by Amazon Pinpoint Email Service
<a name="list_pinpoint-email-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [configuration-set](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_CreateConfigurationSet.html)  | arn:${Partition}:ses:${Region}:${Account}:configuration-set/${ConfigurationSetName} | [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_) | 
|  [dedicated-ip-pool](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DedicatedIp.html)  | arn:${Partition}:ses:${Region}:${Account}:dedicated-ip-pool/${DedicatedIPPool} | [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_) | 
|  [deliverability-test-report](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DeliverabilityTestReport.html)  | arn:${Partition}:ses:${Region}:${Account}:deliverability-test-report/${ReportId} | [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_) | 
|  [identity](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_IdentityInfo.html)  | arn:${Partition}:ses:${Region}:${Account}:identity/${IdentityName} | [aws:ResourceTag/${TagKey}](#list_pinpoint-email-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Pinpoint Email Service
<a name="list_pinpoint-email-policy-keys"></a>

Amazon Pinpoint Email Service defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters actions based on the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters actions based on tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters actions based on the presence of tag keys in the request | ArrayOfString | 
|   [ses:ApiVersion](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonses.html#amazonses-policy-keys)  | Filters actions based on the SES API version | String | 
|   [ses:FeedbackAddress](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonses.html#amazonses-policy-keys)  | Filters actions based on the "Return-Path" address, which specifies where bounces and complaints are sent by email feedback forwarding | String | 
|   [ses:FromAddress](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonses.html#amazonses-policy-keys)  | Filters actions based on the "From" address of a message | String | 
|   [ses:FromDisplayName](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonses.html#amazonses-policy-keys)  | Filters actions based on the "From" address that is used as the display name of a message | String | 
|   [ses:Recipients](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonses.html#amazonses-policy-keys)  | Filters actions based on the recipient addresses of a message, which include the "To", "CC", and "BCC" addresses | ArrayOfString | 