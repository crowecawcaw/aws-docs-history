# Code examples for Amazon SES using AWS SDKs

The following code examples show how to use Amazon SES with an AWS software development kit (SDK).

For a complete list of AWS SDK developer guides and code examples, see
[Using Amazon SES with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.

###### Code examples

- [Amazon SES](service_code_examples_ses.md "service_code_examples_ses.md")
  - [Basics](service_code_examples_ses_basics.md "service_code_examples_ses_basics.md")
    - [Actions](service_code_examples_ses_actions.md "service_code_examples_ses_actions.md")
      - [CreateReceiptFilter](ses_example_ses_CreateReceiptFilter_section.md "ses_example_ses_CreateReceiptFilter_section.md")
      - [CreateReceiptRule](ses_example_ses_CreateReceiptRule_section.md "ses_example_ses_CreateReceiptRule_section.md")
      - [CreateReceiptRuleSet](ses_example_ses_CreateReceiptRuleSet_section.md "ses_example_ses_CreateReceiptRuleSet_section.md")
      - [CreateTemplate](ses_example_ses_CreateTemplate_section.md "ses_example_ses_CreateTemplate_section.md")
      - [DeleteIdentity](ses_example_ses_DeleteIdentity_section.md "ses_example_ses_DeleteIdentity_section.md")
      - [DeleteReceiptFilter](ses_example_ses_DeleteReceiptFilter_section.md "ses_example_ses_DeleteReceiptFilter_section.md")
      - [DeleteReceiptRule](ses_example_ses_DeleteReceiptRule_section.md "ses_example_ses_DeleteReceiptRule_section.md")
      - [DeleteReceiptRuleSet](ses_example_ses_DeleteReceiptRuleSet_section.md "ses_example_ses_DeleteReceiptRuleSet_section.md")
      - [DeleteTemplate](ses_example_ses_DeleteTemplate_section.md "ses_example_ses_DeleteTemplate_section.md")
      - [DescribeReceiptRuleSet](ses_example_ses_DescribeReceiptRuleSet_section.md "ses_example_ses_DescribeReceiptRuleSet_section.md")
      - [GetIdentityVerificationAttributes](ses_example_ses_GetIdentityVerificationAttributes_section.md "ses_example_ses_GetIdentityVerificationAttributes_section.md")
      - [GetSendQuota](ses_example_ses_GetSendQuota_section.md "ses_example_ses_GetSendQuota_section.md")
      - [GetSendStatistics](ses_example_ses_GetSendStatistics_section.md "ses_example_ses_GetSendStatistics_section.md")
      - [GetTemplate](ses_example_ses_GetTemplate_section.md "ses_example_ses_GetTemplate_section.md")
      - [ListIdentities](ses_example_ses_ListIdentities_section.md "ses_example_ses_ListIdentities_section.md")
      - [ListReceiptFilters](ses_example_ses_ListReceiptFilters_section.md "ses_example_ses_ListReceiptFilters_section.md")
      - [ListTemplates](ses_example_ses_ListTemplates_section.md "ses_example_ses_ListTemplates_section.md")
      - [SendBulkTemplatedEmail](ses_example_ses_SendBulkTemplatedEmail_section.md "ses_example_ses_SendBulkTemplatedEmail_section.md")
      - [SendEmail](ses_example_ses_SendEmail_section.md "ses_example_ses_SendEmail_section.md")
      - [SendRawEmail](ses_example_ses_SendRawEmail_section.md "ses_example_ses_SendRawEmail_section.md")
      - [SendTemplatedEmail](ses_example_ses_SendTemplatedEmail_section.md "ses_example_ses_SendTemplatedEmail_section.md")
      - [UpdateTemplate](ses_example_ses_UpdateTemplate_section.md "ses_example_ses_UpdateTemplate_section.md")
      - [VerifyDomainIdentity](ses_example_ses_VerifyDomainIdentity_section.md "ses_example_ses_VerifyDomainIdentity_section.md")
      - [VerifyEmailIdentity](ses_example_ses_VerifyEmailIdentity_section.md "ses_example_ses_VerifyEmailIdentity_section.md")

  - [Scenarios](service_code_examples_ses_scenarios.md "service_code_examples_ses_scenarios.md")
    - [Build an Amazon Transcribe streaming app](ses_example_cross_TranscriptionStreamingApp_section.md "ses_example_cross_TranscriptionStreamingApp_section.md")
    - [Copy email and domain identities across Regions](ses_example_ses_Scenario_ReplicateIdentities_section.md "ses_example_ses_Scenario_ReplicateIdentities_section.md")
    - [Create a web application to track DynamoDB data](ses_example_cross_DynamoDBDataTracker_section.md "ses_example_cross_DynamoDBDataTracker_section.md")
    - [Create a web application to track Amazon Redshift data](ses_example_cross_RedshiftDataTracker_section.md "ses_example_cross_RedshiftDataTracker_section.md")
    - [Create an Aurora Serverless work item tracker](ses_example_cross_RDSDataTracker_section.md "ses_example_cross_RDSDataTracker_section.md")
    - [Detect PPE in images](ses_example_cross_RekognitionPhotoAnalyzerPPE_section.md "ses_example_cross_RekognitionPhotoAnalyzerPPE_section.md")
    - [Detect objects in images](ses_example_cross_RekognitionPhotoAnalyzer_section.md "ses_example_cross_RekognitionPhotoAnalyzer_section.md")
    - [Detect people and objects in a video](ses_example_cross_RekognitionVideoDetection_section.md "ses_example_cross_RekognitionVideoDetection_section.md")
    - [Generate credentials to connect to an SMTP endpoint](ses_example_ses_Scenario_GenerateSmtpCredentials_section.md "ses_example_ses_Scenario_GenerateSmtpCredentials_section.md")
    - [Use Step Functions to invoke Lambda functions](ses_example_cross_ServerlessWorkflows_section.md "ses_example_cross_ServerlessWorkflows_section.md")
    - [Verify an email identity and send messages](ses_example_ses_Scenario_SendEmail_section.md "ses_example_ses_Scenario_SendEmail_section.md")

- [Amazon SES API v2](service_code_examples_sesv2.md "service_code_examples_sesv2.md")
  - [Basics](service_code_examples_sesv2_basics.md "service_code_examples_sesv2_basics.md")
    - [Actions](service_code_examples_sesv2_actions.md "service_code_examples_sesv2_actions.md")
      - [CreateContact](sesv2_example_sesv2_CreateContact_section.md "sesv2_example_sesv2_CreateContact_section.md")
      - [CreateContactList](sesv2_example_sesv2_CreateContactList_section.md "sesv2_example_sesv2_CreateContactList_section.md")
      - [CreateEmailIdentity](sesv2_example_sesv2_CreateEmailIdentity_section.md "sesv2_example_sesv2_CreateEmailIdentity_section.md")
      - [CreateEmailTemplate](sesv2_example_sesv2_CreateEmailTemplate_section.md "sesv2_example_sesv2_CreateEmailTemplate_section.md")
      - [DeleteContactList](sesv2_example_sesv2_DeleteContactList_section.md "sesv2_example_sesv2_DeleteContactList_section.md")
      - [DeleteEmailIdentity](sesv2_example_sesv2_DeleteEmailIdentity_section.md "sesv2_example_sesv2_DeleteEmailIdentity_section.md")
      - [DeleteEmailTemplate](sesv2_example_sesv2_DeleteEmailTemplate_section.md "sesv2_example_sesv2_DeleteEmailTemplate_section.md")
      - [GetEmailIdentity](sesv2_example_sesv2_GetEmailIdentity_section.md "sesv2_example_sesv2_GetEmailIdentity_section.md")
      - [ListContactLists](sesv2_example_sesv2_ListContactLists_section.md "sesv2_example_sesv2_ListContactLists_section.md")
      - [ListContacts](sesv2_example_sesv2_ListContacts_section.md "sesv2_example_sesv2_ListContacts_section.md")
      - [SendEmail](sesv2_example_sesv2_SendEmail_section.md "sesv2_example_sesv2_SendEmail_section.md")

  - [Scenarios](service_code_examples_sesv2_scenarios.md "service_code_examples_sesv2_scenarios.md")
    - [Newsletter scenario](sesv2_example_sesv2_NewsletterWorkflow_section.md "sesv2_example_sesv2_NewsletterWorkflow_section.md")
