

# Data retrieval APIs for Amazon SES
<a name="amazonses"></a>

Amazon SES provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="ses-DescribeActiveReceiptRuleSet"></a>[DescribeActiveReceiptRuleSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_DescribeActiveReceiptRuleSet.html) | Return the metadata and receipt rules for the receipt rule set that is currently active | Read | 
| <a name="ses-DescribeConfigurationSet"></a>[DescribeConfigurationSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_DescribeConfigurationSet.html) | Return the details of the specified configuration set | Read | 
| <a name="ses-DescribeReceiptRule"></a>[DescribeReceiptRule](https://docs.aws.amazon.com/ses/latest/APIReference/API_DescribeReceiptRule.html) | Return the details of the specified receipt rule | Read | 
| <a name="ses-DescribeReceiptRuleSet"></a>[DescribeReceiptRuleSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_DescribeReceiptRuleSet.html) | Return the details of the specified receipt rule set | Read | 
| <a name="ses-GetAccountSendingEnabled"></a>[GetAccountSendingEnabled](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetAccountSendingEnabled.html) | Return the email sending status of your account | Read | 
| <a name="ses-GetCustomVerificationEmailTemplate"></a>[GetCustomVerificationEmailTemplate](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetCustomVerificationEmailTemplate.html) | Return the custom email verification template for the template name you specify | Read | 
| <a name="ses-GetIdentityDkimAttributes"></a>[GetIdentityDkimAttributes](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetIdentityDkimAttributes.html) | Return the current status of Easy DKIM signing for an entity | Read | 
| <a name="ses-GetIdentityMailFromDomainAttributes"></a>[GetIdentityMailFromDomainAttributes](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetIdentityMailFromDomainAttributes.html) | Return the custom MAIL FROM attributes for a list of identities (email addresses and/or domains) | Read | 
| <a name="ses-GetIdentityNotificationAttributes"></a>[GetIdentityNotificationAttributes](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetIdentityNotificationAttributes.html) | Return a structure describing identity notification attributes for a list of verified identities (email addresses and/or domains), | Read | 
| <a name="ses-GetIdentityPolicies"></a>[GetIdentityPolicies](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetIdentityPolicies.html) | Return the requested sending authorization policies for the given identity (an email address or a domain) | Read | 
| <a name="ses-GetIdentityVerificationAttributes"></a>[GetIdentityVerificationAttributes](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetIdentityVerificationAttributes.html) | Return the verification status and (for domain identities) the verification token for a list of identities | Read | 
| <a name="ses-GetSendQuota"></a>[GetSendQuota](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetSendQuota.html) | Return the user's current sending limits | Read | 
| <a name="ses-GetSendStatistics"></a>[GetSendStatistics](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetSendStatistics.html) | Returns the user's sending statistics | Read | 
| <a name="ses-GetTemplate"></a>[GetTemplate](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetTemplate.html) | Return the template object, which includes the subject line, HTML par, and text part for the template you specify | Read | 
| <a name="ses-ListConfigurationSets"></a>[ListConfigurationSets](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListConfigurationSets.html) | List all of the configuration sets for your account | List | 
| <a name="ses-ListCustomVerificationEmailTemplates"></a>[ListCustomVerificationEmailTemplates](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListCustomVerificationEmailTemplates.html) | List all of the existing custom verification email templates for your account | List | 
| <a name="ses-ListIdentities"></a>[ListIdentities](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListIdentities.html) | List the email identities for your account | List | 
| <a name="ses-ListIdentityPolicies"></a>[ListIdentityPolicies](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListIdentityPolicies.html) | List all of the email templates for your account | List | 
| <a name="ses-ListReceiptFilters"></a>[ListReceiptFilters](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListReceiptFilters.html) | List the IP address filters associated with your account | Read | 
| <a name="ses-ListReceiptRuleSets"></a>[ListReceiptRuleSets](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListReceiptRuleSets.html) | List the receipt rule sets that exist under your account | Read | 
| <a name="ses-ListTemplates"></a>[ListTemplates](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListTemplates.html) | List the email templates present in your account | List | 
| <a name="ses-ListVerifiedEmailAddresses"></a>[ListVerifiedEmailAddresses](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListVerifiedEmailAddresses.html) | List all of the email addresses that have been verified in your account | Read | 