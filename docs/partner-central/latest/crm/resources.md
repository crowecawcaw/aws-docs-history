# Integration resources

AWS provides the following resources to help you create a custom integration.

###### Topics

- [Field definitions](#custom-field-definitions "#custom-field-definitions")
- [Standard values](#standard-values "#standard-values")
- [Sample inbound files](#sample-inbound-files "#sample-inbound-files")
- [Sample outbound files](#sample-outbound-files "#sample-outbound-files")
- [Sample processed results](#sample-processed-results "#sample-processed-results")
- [Sample test cases](#sample-test-cases "#sample-test-cases")
- [Sample code snippets](#sample-code-snippets "#sample-code-snippets")

## Field definitions

The links in the following sections list all the fields, explaining their data types,
usage, and any constraints or formatting rules that apply. They serve as a reference to
ensure that when partners and AWS exchange data, it’s correctly formatted and
understood.

The following links take you to GitHub.

- [Opportunity](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/opportunity-samples/Opportunity-Fields.csv "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/opportunity-samples/Opportunity-Fields.csv")
- [Lead](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/lead-samples/Leads-Fields.csv "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/lead-samples/Leads-Fields.csv")

## Standard values

These lists outline the standard values and enumerations for various fields. They help
to maintain consistency in the data exchanged, and ensure that both parties have a common
understanding of the values used.

The following links take you to GitHub.

- [Opportunity](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/opportunity-samples/Opportunity_-_StandardValues.csv "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/opportunity-samples/Opportunity_-_StandardValues.csv")
- [Lead](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/lead-samples/Lead_-_StandardValues.csv "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/lead-samples/Lead_-_StandardValues.csv")

## Sample inbound files

The following sample files show the structure of the JSON payload for a file sent from a
partner to AWS.

The following links take you to GitHub.

- [Opportunity](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/opportunity-samples/Opportunity-Create-Inbound-Sample.json "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/opportunity-samples/Opportunity-Create-Inbound-Sample.json")
- [Lead](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/lead-samples/Lead-Update-Inbound-Sample.json "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/lead-samples/Lead-Update-Inbound-Sample.json")

## Sample outbound files

The following sample files show the structure of the JSON payload for a file sent from
AWS to a partner.

The following links take you to GitHub.

- [Opportunity](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/opportunity-samples/Opportunity-Outbound-Sample.json "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/opportunity-samples/Opportunity-Outbound-Sample.json")
- [Lead](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/lead-samples/Lead-Outbound-Sample.json "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/lead-samples/Lead-Outbound-Sample.json")

## Sample processed results

The following files show a typical result after AWS processes a payload sent by a
partner.

The following links take you to GitHub.

- [Opportunity](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/opportunity-samples/Opportunity-Results-Success-Sample.json "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/opportunity-samples/Opportunity-Results-Success-Sample.json")
- [Lead](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/lead-samples/Lead-Results-Success-Sample.json "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/lead-samples/Lead-Results-Success-Sample.json")

## Sample test cases

The following links take you to GitHub.

- [Opportunity](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/opportunity-samples/Opportunity%20-%20Testing%20Scenarios.xlsx "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/opportunity-samples/Opportunity%20-%20Testing%20Scenarios.xlsx")
- [Lead](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/lead-samples/Lead%20-%20Testing%20Scenarios.xlsx "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/lead-samples/Lead%20-%20Testing%20Scenarios.xlsx")

## Sample code snippets

The following links take you to GitHub.

- [ace_read_s3.py](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/code-snippets/ace_read_s3.py "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/code-snippets/ace_read_s3.py")
- [Apex_Sample_REST_API_Code.cls](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/code-snippets/Apex_Sample_REST_API_Code.cls "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/code-snippets/Apex_Sample_REST_API_Code.cls")
- [S3_Authentication.cls](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/code-snippets/S3_Authentication.cls "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/code-snippets/S3_Authentication.cls")
- [Sample_AceOutboundBatch.cls](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/code-snippets/Sample_AceOutboundBatch.cls "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/code-snippets/Sample_AceOutboundBatch.cls")
- [SFDC apex s3 sample.txt](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/code-snippets/SFDC_apex_s3_sample.txt "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/code-snippets/SFDC_apex_s3_sample.txt")
- [Apex_get_files_from_s3_ace_partner_test.cls](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/code-snippets/Apex_get_files_from_s3_ace_partner_test.cls "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/code-snippets/Apex_get_files_from_s3_ace_partner_test.cls")
- [s3_ace_partner_test.cls](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/code-snippets/s3_ace_partner_test.cls "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/code-snippets/s3_ace_partner_test.cls")
