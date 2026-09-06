

# Actions, resources, and condition keys for Amazon SES
<a name="list_ses"></a>

Amazon SES (service prefix: `ses`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/ses/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/control-user-access.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/ses/ses.json) for this service.

**Topics**
+ [API operations defined by Amazon SES](#list_ses-operations)
+ [Actions defined by Amazon SES](#list_ses-actions-as-permissions)
+ [Resource types defined by Amazon SES](#list_ses-resources-for-iam-policies)
+ [Condition keys for Amazon SES](#list_ses-policy-keys)

## API operations defined by Amazon SES
<a name="list_ses-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_ses-actions-as-permissions).




- **   CloneReceiptRuleSet  **
  - **IAM action:**  [ses:CloneReceiptRuleSet](#list_ses-action-CloneReceiptRuleSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateConfigurationSet  **
  - **IAM action:**  [ses:CreateConfigurationSet](#list_ses-action-CreateConfigurationSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ses:TagResource](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_TagResource.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateConfigurationSetEventDestination  **
  - **IAM action:**  [ses:CreateConfigurationSetEventDestination](#list_ses-action-CreateConfigurationSetEventDestination)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ses.amazonaws.com / **Access level:** Write

- **   CreateConfigurationSetTrackingOptions  **
  - **IAM action:**  [ses:CreateConfigurationSetTrackingOptions](#list_ses-action-CreateConfigurationSetTrackingOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateCustomVerificationEmailTemplate  **
  - **IAM action:**  [ses:CreateCustomVerificationEmailTemplate](#list_ses-action-CreateCustomVerificationEmailTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ses:TagResource](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_TagResource.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateReceiptFilter  **
  - **IAM action:**  [ses:CreateReceiptFilter](#list_ses-action-CreateReceiptFilter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateReceiptRule  **
  - **IAM action:**  [ses:CreateReceiptRule](#list_ses-action-CreateReceiptRule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ses.amazonaws.com / **Access level:** Write

- **   CreateReceiptRuleSet  **
  - **IAM action:**  [ses:CreateReceiptRuleSet](#list_ses-action-CreateReceiptRuleSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateTemplate  **
  - **IAM action:**  [ses:CreateTemplate](#list_ses-action-CreateTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConfigurationSet  **
  - **IAM action:**  [ses:DeleteConfigurationSet](#list_ses-action-DeleteConfigurationSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConfigurationSetEventDestination  **
  - **IAM action:**  [ses:DeleteConfigurationSetEventDestination](#list_ses-action-DeleteConfigurationSetEventDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConfigurationSetTrackingOptions  **
  - **IAM action:**  [ses:DeleteConfigurationSetTrackingOptions](#list_ses-action-DeleteConfigurationSetTrackingOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCustomVerificationEmailTemplate  **
  - **IAM action:**  [ses:DeleteCustomVerificationEmailTemplate](#list_ses-action-DeleteCustomVerificationEmailTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIdentity  **
  - **IAM action:**  [ses:DeleteIdentity](#list_ses-action-DeleteIdentity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIdentityPolicy  **
  - **IAM action:**  [ses:DeleteIdentityPolicy](#list_ses-action-DeleteIdentityPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteReceiptFilter  **
  - **IAM action:**  [ses:DeleteReceiptFilter](#list_ses-action-DeleteReceiptFilter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteReceiptRule  **
  - **IAM action:**  [ses:DeleteReceiptRule](#list_ses-action-DeleteReceiptRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteReceiptRuleSet  **
  - **IAM action:**  [ses:DeleteReceiptRuleSet](#list_ses-action-DeleteReceiptRuleSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTemplate  **
  - **IAM action:**  [ses:DeleteTemplate](#list_ses-action-DeleteTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVerifiedEmailAddress  **
  - **IAM action:**  [ses:DeleteVerifiedEmailAddress](#list_ses-action-DeleteVerifiedEmailAddress) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeActiveReceiptRuleSet  **
  - **IAM action:**  [ses:DescribeActiveReceiptRuleSet](#list_ses-action-DescribeActiveReceiptRuleSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeConfigurationSet  **
  - **IAM action:**  [ses:DescribeConfigurationSet](#list_ses-action-DescribeConfigurationSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeReceiptRule  **
  - **IAM action:**  [ses:DescribeReceiptRule](#list_ses-action-DescribeReceiptRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeReceiptRuleSet  **
  - **IAM action:**  [ses:DescribeReceiptRuleSet](#list_ses-action-DescribeReceiptRuleSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAccountSendingEnabled  **
  - **IAM action:**  [ses:GetAccountSendingEnabled](#list_ses-action-GetAccountSendingEnabled) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCustomVerificationEmailTemplate  **
  - **IAM action:**  [ses:GetCustomVerificationEmailTemplate](#list_ses-action-GetCustomVerificationEmailTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIdentityDkimAttributes  **
  - **IAM action:**  [ses:GetIdentityDkimAttributes](#list_ses-action-GetIdentityDkimAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIdentityMailFromDomainAttributes  **
  - **IAM action:**  [ses:GetIdentityMailFromDomainAttributes](#list_ses-action-GetIdentityMailFromDomainAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIdentityNotificationAttributes  **
  - **IAM action:**  [ses:GetIdentityNotificationAttributes](#list_ses-action-GetIdentityNotificationAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIdentityPolicies  **
  - **IAM action:**  [ses:GetIdentityPolicies](#list_ses-action-GetIdentityPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIdentityVerificationAttributes  **
  - **IAM action:**  [ses:GetIdentityVerificationAttributes](#list_ses-action-GetIdentityVerificationAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSendQuota  **
  - **IAM action:**  [ses:GetSendQuota](#list_ses-action-GetSendQuota) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSendStatistics  **
  - **IAM action:**  [ses:GetSendStatistics](#list_ses-action-GetSendStatistics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTemplate  **
  - **IAM action:**  [ses:GetTemplate](#list_ses-action-GetTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListConfigurationSets  **
  - **IAM action:**  [ses:ListConfigurationSets](#list_ses-action-ListConfigurationSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCustomVerificationEmailTemplates  **
  - **IAM action:**  [ses:ListCustomVerificationEmailTemplates](#list_ses-action-ListCustomVerificationEmailTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIdentities  **
  - **IAM action:**  [ses:ListIdentities](#list_ses-action-ListIdentities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIdentityPolicies  **
  - **IAM action:**  [ses:ListIdentityPolicies](#list_ses-action-ListIdentityPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReceiptFilters  **
  - **IAM action:**  [ses:ListReceiptFilters](#list_ses-action-ListReceiptFilters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListReceiptRuleSets  **
  - **IAM action:**  [ses:ListReceiptRuleSets](#list_ses-action-ListReceiptRuleSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTemplates  **
  - **IAM action:**  [ses:ListTemplates](#list_ses-action-ListTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListVerifiedEmailAddresses  **
  - **IAM action:**  [ses:ListVerifiedEmailAddresses](#list_ses-action-ListVerifiedEmailAddresses) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutConfigurationSetDeliveryOptions  **
  - **IAM action:**  [ses:PutConfigurationSetDeliveryOptions](#list_ses-action-PutConfigurationSetDeliveryOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutIdentityPolicy  **
  - **IAM action:**  [ses:PutIdentityPolicy](#list_ses-action-PutIdentityPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   ReorderReceiptRuleSet  **
  - **IAM action:**  [ses:ReorderReceiptRuleSet](#list_ses-action-ReorderReceiptRuleSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendCustomVerificationEmail  **
  - **IAM action:**  [ses:SendCustomVerificationEmail](#list_ses-action-SendCustomVerificationEmail) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetActiveReceiptRuleSet  **
  - **IAM action:**  [ses:SetActiveReceiptRuleSet](#list_ses-action-SetActiveReceiptRuleSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetIdentityDkimEnabled  **
  - **IAM action:**  [ses:SetIdentityDkimEnabled](#list_ses-action-SetIdentityDkimEnabled) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetIdentityFeedbackForwardingEnabled  **
  - **IAM action:**  [ses:SetIdentityFeedbackForwardingEnabled](#list_ses-action-SetIdentityFeedbackForwardingEnabled) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetIdentityHeadersInNotificationsEnabled  **
  - **IAM action:**  [ses:SetIdentityHeadersInNotificationsEnabled](#list_ses-action-SetIdentityHeadersInNotificationsEnabled) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetIdentityMailFromDomain  **
  - **IAM action:**  [ses:SetIdentityMailFromDomain](#list_ses-action-SetIdentityMailFromDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetIdentityNotificationTopic  **
  - **IAM action:**  [ses:SetIdentityNotificationTopic](#list_ses-action-SetIdentityNotificationTopic) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetReceiptRulePosition  **
  - **IAM action:**  [ses:SetReceiptRulePosition](#list_ses-action-SetReceiptRulePosition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TestRenderTemplate  **
  - **IAM action:**  [ses:TestRenderTemplate](#list_ses-action-TestRenderTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAccountSendingEnabled  **
  - **IAM action:**  [ses:UpdateAccountSendingEnabled](#list_ses-action-UpdateAccountSendingEnabled) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateConfigurationSetEventDestination  **
  - **IAM action:**  [ses:UpdateConfigurationSetEventDestination](#list_ses-action-UpdateConfigurationSetEventDestination)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ses.amazonaws.com / **Access level:** Write

- **   UpdateConfigurationSetReputationMetricsEnabled  **
  - **IAM action:**  [ses:UpdateConfigurationSetReputationMetricsEnabled](#list_ses-action-UpdateConfigurationSetReputationMetricsEnabled) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateConfigurationSetSendingEnabled  **
  - **IAM action:**  [ses:UpdateConfigurationSetSendingEnabled](#list_ses-action-UpdateConfigurationSetSendingEnabled) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateConfigurationSetTrackingOptions  **
  - **IAM action:**  [ses:UpdateConfigurationSetTrackingOptions](#list_ses-action-UpdateConfigurationSetTrackingOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCustomVerificationEmailTemplate  **
  - **IAM action:**  [ses:UpdateCustomVerificationEmailTemplate](#list_ses-action-UpdateCustomVerificationEmailTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateReceiptRule  **
  - **IAM action:**  [ses:UpdateReceiptRule](#list_ses-action-UpdateReceiptRule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ses.amazonaws.com / **Access level:** Write

- **   UpdateTemplate  **
  - **IAM action:**  [ses:UpdateTemplate](#list_ses-action-UpdateTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   VerifyDomainDkim  **
  - **IAM action:**  [ses:VerifyDomainDkim](#list_ses-action-VerifyDomainDkim) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   VerifyDomainIdentity  **
  - **IAM action:**  [ses:VerifyDomainIdentity](#list_ses-action-VerifyDomainIdentity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   VerifyEmailAddress  **
  - **IAM action:**  [ses:VerifyEmailAddress](#list_ses-action-VerifyEmailAddress) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   VerifyEmailIdentity  **
  - **IAM action:**  [ses:VerifyEmailIdentity](#list_ses-action-VerifyEmailIdentity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon SES
<a name="list_ses-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CloneReceiptRuleSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_CloneReceiptRuleSet.html)  **
  - **Description:** Grants permission to create a receipt rule set by cloning an existing one
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [CreateConfigurationSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateConfigurationSet.html)  **
  - **Description:** Grants permission to create a new configuration set
  - **Resource types (\*required):** [configuration-set](#list_ses-resource-configuration-set)
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [CreateConfigurationSetEventDestination](https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateConfigurationSetEventDestination.html)  **
  - **Description:** Grants permission to create a configuration set event destination
  - **Resource types (\*required):** [configuration-set](#list_ses-resource-configuration-set)
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [CreateConfigurationSetTrackingOptions](https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateConfigurationSetTrackingOptions.html)  **
  - **Description:** Grants permission to creates an association between a configuration set and a custom domain for open and click event tracking
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [CreateCustomVerificationEmailTemplate](https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateCustomVerificationEmailTemplate.html)  **
  - **Description:** Grants permission to create a new custom verification email template
  - **Resource types (\*required):** [custom-verification-email-template](#list_ses-resource-custom-verification-email-template)
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [CreateReceiptFilter](https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateReceiptFilter.html)  **
  - **Description:** Grants permission to create a new IP address filter
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [CreateReceiptRule](https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateReceiptRule.html)  **
  - **Description:** Grants permission to create a receipt rule
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [CreateReceiptRuleSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateReceiptRuleSet.html)  **
  - **Description:** Grants permission to create an empty receipt rule set
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [CreateTemplate](https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateTemplate.html)  **
  - **Description:** Grants permission to creates an email template
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [DeleteConfigurationSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteConfigurationSet.html)  **
  - **Description:** Grants permission to delete an existing configuration set
  - **Resource types (\*required):** [configuration-set](#list_ses-resource-configuration-set)
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [DeleteConfigurationSetEventDestination](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteConfigurationSetEventDestination.html)  **
  - **Description:** Grants permission to delete an event destination
  - **Resource types (\*required):** [configuration-set](#list_ses-resource-configuration-set)
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [DeleteConfigurationSetTrackingOptions](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteConfigurationSetTrackingOptions.html)  **
  - **Description:** Grants permission to delete an association between a configuration set and a custom domain for open and click event tracking
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [DeleteCustomVerificationEmailTemplate](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteCustomVerificationEmailTemplate.html)  **
  - **Description:** Grants permission to delete an existing custom verification email template
  - **Resource types (\*required):** [custom-verification-email-template](#list_ses-resource-custom-verification-email-template)
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [DeleteIdentity](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteIdentity.html)  **
  - **Description:** Grants permission to delete the specified identity
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [DeleteIdentityPolicy](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteIdentityPolicy.html)  **
  - **Description:** Grants permission to delete the specified sending authorization policy for the given identity (an email address or a domain)
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Permissions management, Write

- **   [DeleteReceiptFilter](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteReceiptFilter.html)  **
  - **Description:** Grants permission to delete the specified IP address filter
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [DeleteReceiptRule](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteReceiptRule.html)  **
  - **Description:** Grants permission to delete the specified receipt rule
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [DeleteReceiptRuleSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteReceiptRuleSet.html)  **
  - **Description:** Grants permission to delete the specified receipt rule set and all of the receipt rules it contains
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [DeleteTemplate](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteTemplate.html)  **
  - **Description:** Grants permission to delete an email template
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [DeleteVerifiedEmailAddress](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteVerifiedEmailAddress.html)  **
  - **Description:** Grants permission to delete the specified email address from the list of verified addresses
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [DescribeActiveReceiptRuleSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_DescribeActiveReceiptRuleSet.html)  **
  - **Description:** Grants permission to return the metadata and receipt rules for the receipt rule set that is currently active
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Read

- **   [DescribeConfigurationSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_DescribeConfigurationSet.html)  **
  - **Description:** Grants permission to return the details of the specified configuration set
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Read

- **   [DescribeReceiptRule](https://docs.aws.amazon.com/ses/latest/APIReference/API_DescribeReceiptRule.html)  **
  - **Description:** Grants permission to return the details of the specified receipt rule
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Read

- **   [DescribeReceiptRuleSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_DescribeReceiptRuleSet.html)  **
  - **Description:** Grants permission to return the details of the specified receipt rule set
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Read

- **   [GetAccountSendingEnabled](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetAccountSendingEnabled.html)  **
  - **Description:** Grants permission to return the email sending status of your account
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Read

- **   [GetCustomVerificationEmailTemplate](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetCustomVerificationEmailTemplate.html)  **
  - **Description:** Grants permission to return the custom email verification template for the template name you specify
  - **Resource types (\*required):** [custom-verification-email-template](#list_ses-resource-custom-verification-email-template)
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Read

- **   [GetIdentityDkimAttributes](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetIdentityDkimAttributes.html)  **
  - **Description:** Grants permission to return the current status of Easy DKIM signing for an entity
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Read

- **   [GetIdentityMailFromDomainAttributes](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetIdentityMailFromDomainAttributes.html)  **
  - **Description:** Grants permission to return the custom MAIL FROM attributes for a list of identities (email addresses and/or domains)
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Read

- **   [GetIdentityNotificationAttributes](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetIdentityNotificationAttributes.html)  **
  - **Description:** Grants permission to return a structure describing identity notification attributes for a list of verified identities (email addresses and/or domains),
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Read

- **   [GetIdentityPolicies](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetIdentityPolicies.html)  **
  - **Description:** Grants permission to return the requested sending authorization policies for the given identity (an email address or a domain)
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Read

- **   [GetIdentityVerificationAttributes](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetIdentityVerificationAttributes.html)  **
  - **Description:** Grants permission to return the verification status and (for domain identities) the verification token for a list of identities
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Read

- **   [GetSendQuota](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetSendQuota.html)  **
  - **Description:** Grants permission to return the user's current sending limits
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Read

- **   [GetSendStatistics](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetSendStatistics.html)  **
  - **Description:** Grants permission to returns the user's sending statistics
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Read

- **   [GetTemplate](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetTemplate.html)  **
  - **Description:** Grants permission to return the template object, which includes the subject line, HTML par, and text part for the template you specify
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Read

- **   [ListConfigurationSets](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListConfigurationSets.html)  **
  - **Description:** Grants permission to list all of the configuration sets for your account
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** List

- **   [ListCustomVerificationEmailTemplates](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListCustomVerificationEmailTemplates.html)  **
  - **Description:** Grants permission to list all of the existing custom verification email templates for your account
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** List

- **   [ListIdentities](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListIdentities.html)  **
  - **Description:** Grants permission to list the email identities for your account
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** List

- **   [ListIdentityPolicies](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListIdentityPolicies.html)  **
  - **Description:** Grants permission to list all of the email templates for your account
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** List

- **   [ListReceiptFilters](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListReceiptFilters.html)  **
  - **Description:** Grants permission to list the IP address filters associated with your account
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Read

- **   [ListReceiptRuleSets](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListReceiptRuleSets.html)  **
  - **Description:** Grants permission to list the receipt rule sets that exist under your account
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Read

- **   [ListTemplates](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListTemplates.html)  **
  - **Description:** Grants permission to list the email templates present in your account
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** List

- **   [ListVerifiedEmailAddresses](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListVerifiedEmailAddresses.html)  **
  - **Description:** Grants permission to list all of the email addresses that have been verified in your account
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Read

- **   [PutConfigurationSetDeliveryOptions](https://docs.aws.amazon.com/ses/latest/APIReference/API_PutConfigurationSetDeliveryOptions.html)  **
  - **Description:** Grants permission to add or update the delivery options for a configuration set
  - **Resource types (\*required):** [configuration-set](#list_ses-resource-configuration-set)
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [PutIdentityPolicy](https://docs.aws.amazon.com/ses/latest/APIReference/API_PutIdentityPolicy.html)  **
  - **Description:** Grants permission to add or update a sending authorization policy for the specified identity (an email address or a domain)
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Permissions management, Write

- **   [ReorderReceiptRuleSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_ReorderReceiptRuleSet.html)  **
  - **Description:** Grants permission to reorder the receipt rules within a receipt rule set
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [SendBounce](https://docs.aws.amazon.com/ses/latest/APIReference/API_SendBounce.html)  **
  - **Description:** Grants permission to generate and send a bounce message to the sender of an email you received through Amazon SES
  - **Resource types (\*required):** [identity\*](#list_ses-resource-identity)
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)<br />[ses:FromAddress](#list_ses-ses_FromAddress)
  - **Access level:** Write

- **   [SendBulkTemplatedEmail](https://docs.aws.amazon.com/ses/latest/APIReference/API_SendBulkTemplatedEmail.html)  **
  - **Description:** Grants permission to compose an email message to multiple destinations
  - **Resource types (\*required):** [configuration-set](#list_ses-resource-configuration-set) / **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)<br />[ses:FeedbackAddress](#list_ses-ses_FeedbackAddress)<br />[ses:FromAddress](#list_ses-ses_FromAddress)<br />[ses:FromDisplayName](#list_ses-ses_FromDisplayName)<br />[ses:Recipients](#list_ses-ses_Recipients)
  - **Resource types (\*required):** [identity\*](#list_ses-resource-identity) / **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)<br />[ses:FeedbackAddress](#list_ses-ses_FeedbackAddress)<br />[ses:FromAddress](#list_ses-ses_FromAddress)<br />[ses:FromDisplayName](#list_ses-ses_FromDisplayName)<br />[ses:Recipients](#list_ses-ses_Recipients)
  - **Resource types (\*required):** [template\*](#list_ses-resource-template) / **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)<br />[ses:FeedbackAddress](#list_ses-ses_FeedbackAddress)<br />[ses:FromAddress](#list_ses-ses_FromAddress)<br />[ses:FromDisplayName](#list_ses-ses_FromDisplayName)<br />[ses:Recipients](#list_ses-ses_Recipients)
  - **Access level:** Write

- **   [SendCustomVerificationEmail](https://docs.aws.amazon.com/ses/latest/APIReference/API_SendCustomVerificationEmail.html)  **
  - **Description:** Grants permission to add an email address to the list of identities and attempts to verify it for your account
  - **Resource types (\*required):** [custom-verification-email-template](#list_ses-resource-custom-verification-email-template) / **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)<br />[ses:FeedbackAddress](#list_ses-ses_FeedbackAddress)<br />[ses:FromAddress](#list_ses-ses_FromAddress)<br />[ses:FromDisplayName](#list_ses-ses_FromDisplayName)<br />[ses:Recipients](#list_ses-ses_Recipients)
  - **Resource types (\*required):** [identity\*](#list_ses-resource-identity) / **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)<br />[ses:FeedbackAddress](#list_ses-ses_FeedbackAddress)<br />[ses:FromAddress](#list_ses-ses_FromAddress)<br />[ses:FromDisplayName](#list_ses-ses_FromDisplayName)<br />[ses:Recipients](#list_ses-ses_Recipients)
  - **Access level:** Write

- **   [SendEmail](https://docs.aws.amazon.com/ses/latest/APIReference/API_SendEmail.html)  **
  - **Description:** Grants permission to send an email message
  - **Resource types (\*required):** [configuration-set](#list_ses-resource-configuration-set) / **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)<br />[ses:FeedbackAddress](#list_ses-ses_FeedbackAddress)<br />[ses:FromAddress](#list_ses-ses_FromAddress)<br />[ses:FromDisplayName](#list_ses-ses_FromDisplayName)<br />[ses:Recipients](#list_ses-ses_Recipients)
  - **Resource types (\*required):** [identity\*](#list_ses-resource-identity) / **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)<br />[ses:FeedbackAddress](#list_ses-ses_FeedbackAddress)<br />[ses:FromAddress](#list_ses-ses_FromAddress)<br />[ses:FromDisplayName](#list_ses-ses_FromDisplayName)<br />[ses:Recipients](#list_ses-ses_Recipients)
  - **Resource types (\*required):** [template](#list_ses-resource-template) / **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)<br />[ses:FeedbackAddress](#list_ses-ses_FeedbackAddress)<br />[ses:FromAddress](#list_ses-ses_FromAddress)<br />[ses:FromDisplayName](#list_ses-ses_FromDisplayName)<br />[ses:Recipients](#list_ses-ses_Recipients)
  - **Access level:** Write

- **   [SendRawEmail](https://docs.aws.amazon.com/ses/latest/APIReference/API_SendRawEmail.html)  **
  - **Description:** Grants permission to send an email message, with header and content specified by the client
  - **Resource types (\*required):** [configuration-set](#list_ses-resource-configuration-set) / **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)<br />[ses:FeedbackAddress](#list_ses-ses_FeedbackAddress)<br />[ses:FromAddress](#list_ses-ses_FromAddress)<br />[ses:FromDisplayName](#list_ses-ses_FromDisplayName)<br />[ses:Recipients](#list_ses-ses_Recipients)
  - **Resource types (\*required):** [identity\*](#list_ses-resource-identity) / **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)<br />[ses:FeedbackAddress](#list_ses-ses_FeedbackAddress)<br />[ses:FromAddress](#list_ses-ses_FromAddress)<br />[ses:FromDisplayName](#list_ses-ses_FromDisplayName)<br />[ses:Recipients](#list_ses-ses_Recipients)
  - **Access level:** Write

- **   [SendTemplatedEmail](https://docs.aws.amazon.com/ses/latest/APIReference/API_SendTemplatedEmail.html)  **
  - **Description:** Grants permission to compose an email message using an email template
  - **Resource types (\*required):** [configuration-set](#list_ses-resource-configuration-set) / **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)<br />[ses:FeedbackAddress](#list_ses-ses_FeedbackAddress)<br />[ses:FromAddress](#list_ses-ses_FromAddress)<br />[ses:FromDisplayName](#list_ses-ses_FromDisplayName)<br />[ses:Recipients](#list_ses-ses_Recipients)
  - **Resource types (\*required):** [identity\*](#list_ses-resource-identity) / **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)<br />[ses:FeedbackAddress](#list_ses-ses_FeedbackAddress)<br />[ses:FromAddress](#list_ses-ses_FromAddress)<br />[ses:FromDisplayName](#list_ses-ses_FromDisplayName)<br />[ses:Recipients](#list_ses-ses_Recipients)
  - **Resource types (\*required):** [template\*](#list_ses-resource-template) / **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)<br />[ses:FeedbackAddress](#list_ses-ses_FeedbackAddress)<br />[ses:FromAddress](#list_ses-ses_FromAddress)<br />[ses:FromDisplayName](#list_ses-ses_FromDisplayName)<br />[ses:Recipients](#list_ses-ses_Recipients)
  - **Access level:** Write

- **   [SetActiveReceiptRuleSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_SetActiveReceiptRuleSet.html)  **
  - **Description:** Grants permission to set the specified receipt rule set as the active receipt rule set
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [SetIdentityDkimEnabled](https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityDkimEnabled.html)  **
  - **Description:** Grants permission to enable or disable Easy DKIM signing of email sent from an identity
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [SetIdentityFeedbackForwardingEnabled](https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityFeedbackForwardingEnabled.html)  **
  - **Description:** Grants permission to enable or disable whether Amazon SES forwards bounce and complaint notifications for an identity (an email address or a domain)
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [SetIdentityHeadersInNotificationsEnabled](https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityHeadersInNotificationsEnabled.html)  **
  - **Description:** Grants permission to set whether Amazon SES includes the original email headers in the Amazon Simple Notification Service (Amazon SNS) notifications of a specified type for a given identity (an email address or a domain)
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [SetIdentityMailFromDomain](https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityMailFromDomain.html)  **
  - **Description:** Grants permission to enable or disable the custom MAIL FROM domain setup for a verified identity
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [SetIdentityNotificationTopic](https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityNotificationTopic.html)  **
  - **Description:** Grants permission to set an Amazon Simple Notification Service (Amazon SNS) topic to use when delivering notifications for a verified identity
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [SetReceiptRulePosition](https://docs.aws.amazon.com/ses/latest/APIReference/API_SetReceiptRulePosition.html)  **
  - **Description:** Grants permission to set the position of the specified receipt rule in the receipt rule set
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [TestRenderTemplate](https://docs.aws.amazon.com/ses/latest/APIReference/API_TestRenderTemplate.html)  **
  - **Description:** Grants permission to create a preview of the MIME content of an email when provided with a template and a set of replacement data
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [UpdateAccountSendingEnabled](https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateAccountSendingEnabled.html)  **
  - **Description:** Grants permission to enable or disable email sending for your account
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [UpdateConfigurationSetEventDestination](https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateConfigurationSetEventDestination.html)  **
  - **Description:** Grants permission to update the event destination of a configuration set
  - **Resource types (\*required):** [configuration-set](#list_ses-resource-configuration-set)
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [UpdateConfigurationSetReputationMetricsEnabled](https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateConfigurationSetReputationMetricsEnabled.html)  **
  - **Description:** Grants permission to enable or disable the publishing of reputation metrics for emails sent using a specific configuration set
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [UpdateConfigurationSetSendingEnabled](https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateConfigurationSetSendingEnabled.html)  **
  - **Description:** Grants permission to enable or disable email sending for messages sent using a specific configuration set
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [UpdateConfigurationSetTrackingOptions](https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateConfigurationSetTrackingOptions.html)  **
  - **Description:** Grants permission to modify an association between a configuration set and a custom domain for open and click event tracking
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [UpdateCustomVerificationEmailTemplate](https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateCustomVerificationEmailTemplate.html)  **
  - **Description:** Grants permission to update an existing custom verification email template
  - **Resource types (\*required):** [custom-verification-email-template](#list_ses-resource-custom-verification-email-template)
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [UpdateReceiptRule](https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateReceiptRule.html)  **
  - **Description:** Grants permission to update a receipt rule
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [UpdateTemplate](https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateTemplate.html)  **
  - **Description:** Grants permission to update an email template
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [VerifyDomainDkim](https://docs.aws.amazon.com/ses/latest/APIReference/API_VerifyDomainDkim.html)  **
  - **Description:** Grants permission to return a set of DKIM tokens for a domain
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [VerifyDomainIdentity](https://docs.aws.amazon.com/ses/latest/APIReference/API_VerifyDomainIdentity.html)  **
  - **Description:** Grants permission to verify a domain
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [VerifyEmailAddress](https://docs.aws.amazon.com/ses/latest/APIReference/API_VerifyEmailAddress.html)  **
  - **Description:** Grants permission to verify an email address
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write

- **   [VerifyEmailIdentity](https://docs.aws.amazon.com/ses/latest/APIReference/API_VerifyEmailIdentity.html)  **
  - **Description:** Grants permission to verify an email identity
  - **Resource types (\*required):** 
  - **Condition keys:** [ses:ApiVersion](#list_ses-ses_ApiVersion)
  - **Access level:** Write



## Resource types defined by Amazon SES
<a name="list_ses-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [configuration-set](https://docs.aws.amazon.com/ses/latest/APIReference/API_ConfigurationSet.html)  | arn:${Partition}:ses:${Region}:${Account}:configuration-set/${ConfigurationSetName} |   | 
|  [custom-verification-email-template](https://docs.aws.amazon.com/ses/latest/APIReference/API_CustomVerificationEmailTemplate.html)  | arn:${Partition}:ses:${Region}:${Account}:custom-verification-email-template/${TemplateName} |   | 
|  [identity](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_IdentityInfo.html)  | arn:${Partition}:ses:${Region}:${Account}:identity/${IdentityName} |   | 
|  [template](https://docs.aws.amazon.com/ses/latest/APIReference/API_Template.html)  | arn:${Partition}:ses:${Region}:${Account}:template/${TemplateName} |   | 

## Condition keys for Amazon SES
<a name="list_ses-policy-keys"></a>

Amazon SES defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [ses:ApiVersion](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonses.html#amazonses-policy-keys)  | Filters actions based on the SES API version | String | 
|   [ses:FeedbackAddress](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonses.html#amazonses-policy-keys)  | Filters actions based on the "Return-Path" address, which specifies where bounces and complaints are sent by email feedback forwarding | String | 
|   [ses:FromAddress](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonses.html#amazonses-policy-keys)  | Filters actions based on the "From" address of a message | String | 
|   [ses:FromDisplayName](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonses.html#amazonses-policy-keys)  | Filters actions based on the "From" address that is used as the display name of a message | String | 
|   [ses:Recipients](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonses.html#amazonses-policy-keys)  | Filters actions based on the recipient addresses of a message, which include the "To", "CC", and "BCC" addresses | ArrayOfString | 