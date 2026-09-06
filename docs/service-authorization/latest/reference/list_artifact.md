

# Actions, resources, and condition keys for AWS Artifact
<a name="list_artifact"></a>

AWS Artifact (service prefix: `artifact`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/artifact/latest/ug/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/artifact/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/artifact/latest/ug/getting-started.html#create-iam-policy) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/artifact/artifact.json) for this service.

**Topics**
+ [API operations defined by AWS Artifact](#list_artifact-operations)
+ [Actions defined by AWS Artifact](#list_artifact-actions-as-permissions)
+ [Resource types defined by AWS Artifact](#list_artifact-resources-for-iam-policies)
+ [Condition keys for AWS Artifact](#list_artifact-policy-keys)

## API operations defined by AWS Artifact
<a name="list_artifact-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_artifact-actions-as-permissions).




- **   CreateComplianceInquiry  **
  - **IAM action:**  [artifact:CreateComplianceInquiry](#list_artifact-action-CreateComplianceInquiry)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [artifact:TagResource](#list_artifact-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   ExportComplianceInquiry  **
  - **IAM action:**  [artifact:ExportComplianceInquiry](#list_artifact-action-ExportComplianceInquiry) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAccountSettings  **
  - **IAM action:**  [artifact:GetAccountSettings](#list_artifact-action-GetAccountSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetComplianceInquiryMetadata  **
  - **IAM action:**  [artifact:GetComplianceInquiryMetadata](#list_artifact-action-GetComplianceInquiryMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetReport  **
  - **IAM action:**  [artifact:GetReport](#list_artifact-action-GetReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetReportMetadata  **
  - **IAM action:**  [artifact:GetReportMetadata](#list_artifact-action-GetReportMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTermForReport  **
  - **IAM action:**  [artifact:GetTermForReport](#list_artifact-action-GetTermForReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListComplianceInquiries  **
  - **IAM action:**  [artifact:ListComplianceInquiries](#list_artifact-action-ListComplianceInquiries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListComplianceInquiryQueries  **
  - **IAM action:**  [artifact:ListComplianceInquiryQueries](#list_artifact-action-ListComplianceInquiryQueries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCustomerAgreements  **
  - **IAM action:**  [artifact:ListCustomerAgreements](#list_artifact-action-ListCustomerAgreements) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReportVersions  **
  - **IAM action:**  [artifact:ListReportVersions](#list_artifact-action-ListReportVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReports  **
  - **IAM action:**  [artifact:ListReports](#list_artifact-action-ListReports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [artifact:ListTagsForResource](#list_artifact-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutAccountSettings  **
  - **IAM action:**  [artifact:PutAccountSettings](#list_artifact-action-PutAccountSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutComplianceInquiryFeedback  **
  - **IAM action:**  [artifact:PutComplianceInquiryFeedback](#list_artifact-action-PutComplianceInquiryFeedback) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [artifact:TagResource](#list_artifact-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [artifact:UntagResource](#list_artifact-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write



## Actions defined by AWS Artifact
<a name="list_artifact-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptAgreement](https://docs.aws.amazon.com/artifact/latest/APIReference/API_AcceptAgreement.html)  **
  - **Description:** Grants permission to accept an AWS agreement that has not yet been accepted by the customer account
  - **Resource types (\*required):** [agreement\*](#list_artifact-resource-agreement)
  - **Condition keys:**  
  - **Access level:** Write

- **   [AcceptNdaForAgreement](https://docs.aws.amazon.com/artifact/latest/APIReference/API_AcceptNdaForAgreement.html)  **
  - **Description:** Grants permission to accept the terms of an NDA Document for a given agreement resource
  - **Resource types (\*required):** [agreement\*](#list_artifact-resource-agreement)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateComplianceInquiry](https://docs.aws.amazon.com/artifact/latest/APIReference/API_CreateComplianceInquiry.html)  **
  - **Description:** Grants permission to create a compliance inquiry
  - **Resource types (\*required):** [compliance-inquiry\*](#list_artifact-resource-compliance-inquiry)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_artifact-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_artifact-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_artifact-aws_TagKeys)
  - **Access level:** Write

- **   [ExportComplianceInquiry](https://docs.aws.amazon.com/artifact/latest/APIReference/API_ExportComplianceInquiry.html)  **
  - **Description:** Grants permission to export a compliance inquiry
  - **Resource types (\*required):** [compliance-inquiry\*](#list_artifact-resource-compliance-inquiry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_artifact-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAccountSettings](https://docs.aws.amazon.com/artifact/latest/APIReference/API_GetAccountSettings.html)  **
  - **Description:** Grants permission to get the account settings for Artifact
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAgreement](https://docs.aws.amazon.com/artifact/latest/APIReference/API_GetAgreement.html)  **
  - **Description:** Grants permission to get an AWS agreement that has not yet been accepted by the customer account
  - **Resource types (\*required):** [agreement\*](#list_artifact-resource-agreement)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetComplianceInquiryMetadata](https://docs.aws.amazon.com/artifact/latest/APIReference/API_GetComplianceInquiryMetadata.html)  **
  - **Description:** Grants permission to get metadata associated with a compliance inquiry
  - **Resource types (\*required):** [compliance-inquiry\*](#list_artifact-resource-compliance-inquiry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_artifact-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCustomerAgreement](https://docs.aws.amazon.com/artifact/latest/APIReference/API_GetCustomerAgreement.html)  **
  - **Description:** Grants permission to get an AWS agreement that has been accepted by the customer account
  - **Resource types (\*required):** [customer-agreement\*](#list_artifact-resource-customer-agreement)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetNdaForAgreement](https://docs.aws.amazon.com/artifact/latest/APIReference/API_GetNdaForAgreement.html)  **
  - **Description:** Grants permission to retrieve the NDA Document for a given agreement resource
  - **Resource types (\*required):** [agreement\*](#list_artifact-resource-agreement)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetReport](https://docs.aws.amazon.com/artifact/latest/APIReference/API_GetReport.html)  **
  - **Description:** Grants permission to download a report
  - **Resource types (\*required):** [report\*](#list_artifact-resource-report)
  - **Condition keys:** [artifact:ReportCategory](#list_artifact-artifact_ReportCategory)<br />[artifact:ReportSeries](#list_artifact-artifact_ReportSeries)
  - **Access level:** Read

- **   [GetReportMetadata](https://docs.aws.amazon.com/artifact/latest/APIReference/API_GetReportMetadata.html)  **
  - **Description:** Grants permission to download metadata associated with a report
  - **Resource types (\*required):** [report\*](#list_artifact-resource-report)
  - **Condition keys:** [artifact:ReportCategory](#list_artifact-artifact_ReportCategory)<br />[artifact:ReportSeries](#list_artifact-artifact_ReportSeries)
  - **Access level:** Read

- **   [GetTermForReport](https://docs.aws.amazon.com/artifact/latest/APIReference/API_GetTermForReport.html)  **
  - **Description:** Grants permission to download a term associated with a report
  - **Resource types (\*required):** [report\*](#list_artifact-resource-report)
  - **Condition keys:** [artifact:ReportCategory](#list_artifact-artifact_ReportCategory)<br />[artifact:ReportSeries](#list_artifact-artifact_ReportSeries)
  - **Access level:** Read

- **   [ListAgreements](https://docs.aws.amazon.com/artifact/latest/APIReference/API_ListAgreements.html)  **
  - **Description:** Grants permission to list AWS agreements
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListComplianceInquiries](https://docs.aws.amazon.com/artifact/latest/APIReference/API_ListComplianceInquiries.html)  **
  - **Description:** Grants permission to list compliance inquiries submitted by the customer account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListComplianceInquiryQueries](https://docs.aws.amazon.com/artifact/latest/APIReference/API_ListComplianceInquiryQueries.html)  **
  - **Description:** Grants permission to list queries for a compliance inquiry
  - **Resource types (\*required):** [compliance-inquiry\*](#list_artifact-resource-compliance-inquiry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_artifact-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCustomerAgreements](https://docs.aws.amazon.com/artifact/latest/APIReference/API_ListCustomerAgreements.html)  **
  - **Description:** Grants permission to list customer-agreement resources that have been accepted by the customer account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListReportVersions](https://docs.aws.amazon.com/artifact/latest/APIReference/API_ListReportVersions.html)  **
  - **Description:** Grants permission to list report versions in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListReports](https://docs.aws.amazon.com/artifact/latest/APIReference/API_ListReports.html)  **
  - **Description:** Grants permission to list reports in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/artifact/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list all tags on an AWS Artifact resource
  - **Resource types (\*required):** [compliance-inquiry\*](#list_artifact-resource-compliance-inquiry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_artifact-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutAccountSettings](https://docs.aws.amazon.com/artifact/latest/APIReference/API_PutAccountSettings.html)  **
  - **Description:** Grants permission to put account settings for Artifact
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutComplianceInquiryFeedback](https://docs.aws.amazon.com/artifact/latest/APIReference/API_PutComplianceInquiryFeedback.html)  **
  - **Description:** Grants permission to submit feedback on a compliance inquiry response
  - **Resource types (\*required):** [compliance-inquiry\*](#list_artifact-resource-compliance-inquiry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_artifact-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/artifact/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to associate a set of tags with an AWS Artifact resource
  - **Resource types (\*required):** [compliance-inquiry\*](#list_artifact-resource-compliance-inquiry)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_artifact-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_artifact-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_artifact-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TerminateAgreement](https://docs.aws.amazon.com/artifact/latest/APIReference/API_TerminateAgreement.html)  **
  - **Description:** Grants permission to terminate a customer agreement that was previously accepted by the customer account
  - **Resource types (\*required):** [customer-agreement\*](#list_artifact-resource-customer-agreement)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/artifact/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove the association of tags from an AWS Artifact resource
  - **Resource types (\*required):** [compliance-inquiry\*](#list_artifact-resource-compliance-inquiry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_artifact-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_artifact-aws_TagKeys)
  - **Access level:** Tagging, Write



## Resource types defined by AWS Artifact
<a name="list_artifact-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [agreement](https://docs.aws.amazon.com/artifact/latest/ug/managing-agreements.html)  | arn:${Partition}:artifact:::agreement/\* |   | 
|  [compliance-inquiry](https://docs.aws.amazon.com/artifact/latest/ug/managing-compliance-inquiries.html)  | arn:${Partition}:artifact:${Region}:${Account}:compliance-inquiry/\* | [aws:ResourceTag/${TagKey}](#list_artifact-aws_ResourceTag___TagKey_) | 
|  [customer-agreement](https://docs.aws.amazon.com/artifact/latest/ug/managing-agreements.html)  | arn:${Partition}:artifact::${Account}:customer-agreement/\* |   | 
|  [report](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html)  | arn:${Partition}:artifact:${Region}::report/${ReportId}:${Version} | [artifact:ReportCategory](#list_artifact-artifact_ReportCategory)<br />[artifact:ReportSeries](#list_artifact-artifact_ReportSeries) | 

## Condition keys for AWS Artifact
<a name="list_artifact-policy-keys"></a>

AWS Artifact defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [artifact:ReportCategory](https://docs.aws.amazon.com/artifact/latest/ug/using-condition-keys.html)  | Filters access by which category reports are associated with | String | 
|   [artifact:ReportSeries](https://docs.aws.amazon.com/artifact/latest/ug/using-condition-keys.html)  | Filters access by which series reports are associated with | String | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 