

# Actions, resources, and condition keys for AWS Support
<a name="list_support"></a>

AWS Support (service prefix: `support`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/awssupport/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/awssupport/latest/user/security.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/support/support.json) for this service.

**Topics**
+ [API operations defined by AWS Support](#list_support-operations)
+ [Actions defined by AWS Support](#list_support-actions-as-permissions)
+ [Resource types defined by AWS Support](#list_support-resources-for-iam-policies)
+ [Condition keys for AWS Support](#list_support-policy-keys)

## API operations defined by AWS Support
<a name="list_support-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_support-actions-as-permissions).




- **   AddAttachmentsToSet  **
  - **IAM action:**  [support:AddAttachmentsToSet](#list_support-action-AddAttachmentsToSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AddCommunicationToCase  **
  - **IAM action:**  [support:AddCommunicationToCase](#list_support-action-AddCommunicationToCase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CompleteAttachmentUpload  **
  - **IAM action:**  [support:AddAttachmentsToSet](#list_support-action-AddAttachmentsToSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [support:UploadAttachment](#list_support-action-UploadAttachment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateCase  **
  - **IAM action:**  [support:CreateCase](#list_support-action-CreateCase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAttachment  **
  - **IAM action:**  [support:DescribeAttachment](#list_support-action-DescribeAttachment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAttachmentUploadStatus  **
  - **IAM action:**  [support:AddAttachmentsToSet](#list_support-action-AddAttachmentsToSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [support:UploadAttachment](#list_support-action-UploadAttachment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DescribeCases  **
  - **IAM action:**  [support:DescribeCases](#list_support-action-DescribeCases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCommunications  **
  - **IAM action:**  [support:DescribeCommunications](#list_support-action-DescribeCommunications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCreateCaseOptions  **
  - **IAM action:**  [support:DescribeCreateCaseOptions](#list_support-action-DescribeCreateCaseOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeServices  **
  - **IAM action:**  [support:DescribeServices](#list_support-action-DescribeServices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSeverityLevels  **
  - **IAM action:**  [support:DescribeSeverityLevels](#list_support-action-DescribeSeverityLevels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSupportedLanguages  **
  - **IAM action:**  [support:DescribeSupportedLanguages](#list_support-action-DescribeSupportedLanguages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTrustedAdvisorCheckRefreshStatuses  **
  - **IAM action:**  [support:DescribeTrustedAdvisorCheckRefreshStatuses](#list_support-action-DescribeTrustedAdvisorCheckRefreshStatuses) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTrustedAdvisorCheckResult  **
  - **IAM action:**  [support:DescribeTrustedAdvisorCheckResult](#list_support-action-DescribeTrustedAdvisorCheckResult)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [trustedadvisor:DescribeCheckItems](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [trustedadvisor:ListRecommendationResources](https://docs.aws.amazon.com/awssupport/latest/user/get-started-with-aws-trusted-advisor-api.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [trustedadvisor:ListRecommendationsForResource](https://docs.aws.amazon.com/awssupport/latest/user/get-started-with-aws-trusted-advisor-api.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   DescribeTrustedAdvisorCheckSummaries  **
  - **IAM action:**  [support:DescribeTrustedAdvisorCheckSummaries](#list_support-action-DescribeTrustedAdvisorCheckSummaries)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [trustedadvisor:DescribeCheckSummaries](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [trustedadvisor:GetRecommendation](https://docs.aws.amazon.com/awssupport/latest/user/get-started-with-aws-trusted-advisor-api.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [trustedadvisor:ListRecommendations](https://docs.aws.amazon.com/awssupport/latest/user/get-started-with-aws-trusted-advisor-api.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   DescribeTrustedAdvisorChecks  **
  - **IAM action:**  [support:DescribeTrustedAdvisorChecks](#list_support-action-DescribeTrustedAdvisorChecks)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [trustedadvisor:DescribeChecks](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [trustedadvisor:ListChecks](https://docs.aws.amazon.com/awssupport/latest/user/get-started-with-aws-trusted-advisor-api.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   GetAttachmentDownloadLink  **
  - **IAM action:**  [support:DescribeAttachment](#list_support-action-DescribeAttachment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [support:DownloadAttachment](#list_support-action-DownloadAttachment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetAttachmentUploadLinks  **
  - **IAM action:**  [support:AddAttachmentsToSet](#list_support-action-AddAttachmentsToSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [support:UploadAttachment](#list_support-action-UploadAttachment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   RefreshTrustedAdvisorCheck  **
  - **IAM action:**  [support:RefreshTrustedAdvisorCheck](#list_support-action-RefreshTrustedAdvisorCheck) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ResolveCase  **
  - **IAM action:**  [support:ResolveCase](#list_support-action-ResolveCase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Support
<a name="list_support-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [AddAttachmentsToSet](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_AddAttachmentsToSet.html)  | Grants permission to add one or more attachments to an AWS Support case |  |   | Write | 
|   [AddCommunicationToCase](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_AddCommunicationToCase.html)  | Grants permission to add a customer communication to an AWS Support case |  |   | Write | 
|   [AddRelatedItemToCase](https://docs.aws.amazon.com/awssupport/latest/user/accessing-support.html)  | Grants permission to add a related item to an AWS Support case. This is an internally managed function |  |   | Write | 
|   [CreateCase](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_CreateCase.html)  | Grants permission to creates a new AWS Support case |  |   | Write | 
|   [DescribeAttachment](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeAttachment.html)  | Grants permission to describe attachment detail |  |   | Read | 
|   [DescribeCaseAttributes](https://docs.aws.amazon.com/awssupport/latest/user/accessing-support.html)  | Grants permission to allow secondary services to read AWS Support case attributes.This is an internally managed function |  |   | Read | 
|   [DescribeCaseOptions](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeCaseOptions.html)  | Grants permission to describe the available options for a single AWS Support case. This is an internally managed function |  |   | Read | 
|   [DescribeCases](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeCases.html)  | Grants permission to list AWS Support cases that matches the given inputs |  |   | Read | 
|   [DescribeCommunication](https://docs.aws.amazon.com/awssupport/latest/user/accessing-support.html)  | Grants permission to get a single communication and attachments for a single AWS Support case |  |   | Read | 
|   [DescribeCommunications](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeCommunications.html)  | Grants permission to list the communications and attachments for one or more AWS Support cases |  |   | Read | 
|   [DescribeCreateCaseOptions](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeCreateCaseOptions.html)  | Grants permission to describes the available options for creating a support case |  |   | Read | 
|   [DescribeIssueTypes](https://docs.aws.amazon.com/awssupport/latest/user/accessing-support.html)  | Grants permission to return issue types for AWS Support cases |  |   | Read | 
|   [DescribeRelatedItems](https://docs.aws.amazon.com/awssupport/latest/user/accessing-support.html)  | Grants permission to list the related items for an AWS Support case. This is an internally managed function |  |   | Read | 
|   [DescribeServices](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeServices.html)  | Grants permission to list AWS services and categories that applies to each service |  |   | Read | 
|   [DescribeSeverityLevels](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeSeverityLevels.html)  | Grants permission to list severity levels that can be assigned to an AWS Support case |  |   | Read | 
|   [DescribeSupportLevel](https://docs.aws.amazon.com/awssupport/latest/user/accessing-support.html)  | Grants permission to return the support level for an AWS Account identifier |  |   | Read | 
|   [DescribeSupportedLanguages](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeSupportedLanguages.html)  | Grants permission to describes the available support languages for a given category code, service code and issue type |  |   | Read | 
|   [DescribeTrustedAdvisorCheckRefreshStatuses](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeTrustedAdvisorCheckRefreshStatuses.html)  | Grants permission to get the status of a Trusted Advisor refresh check based on a list of check identifiers |  |   | Read | 
|   [DescribeTrustedAdvisorCheckResult](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeTrustedAdvisorCheckResult.html)  | Grants permission to get the results of the Trusted Advisor check that has the specified check identifier |  |   | Read | 
|   [DescribeTrustedAdvisorCheckSummaries](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeTrustedAdvisorCheckSummaries.html)  | Grants permission to get the summaries of the results of the Trusted Advisor checks that have the specified check identifiers |  |   | Read | 
|   [DescribeTrustedAdvisorChecks](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeTrustedAdvisorChecks.html)  | Grants permission to get a list of all available Trusted Advisor checks, including name, identifier, category and description |  |   | Read | 
|   [DisconnectLiveContactForCase](https://docs.aws.amazon.com/awssupport/latest/user/accessing-support.html)  | Grants permission to disconnect a live contact on AWS Support Center. This is an internally managed function |  |   | Write | 
|   [DownloadAttachment](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_GetAttachmentDownloadLink.html)  | Grants permission to get a presigned URL to download an attachment from an AWS Support case |  |   | Read | 
|   [GetInteraction](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_GetInteraction.html)  | Grants permission to retrieve personalized troubleshooting assistance for account and technical issues for a specific interaction |  |   | Read | 
|   [InitiateCallForCase](https://docs.aws.amazon.com/awssupport/latest/user/accessing-support.html)  | Grants permission to initiate a call on AWS Support Center. This is an internally managed function |  |   | Write | 
|   [InitiateChatForCase](https://docs.aws.amazon.com/awssupport/latest/user/accessing-support.html)  | Grants permission to initiate a chat on AWS Support Center.This is an internally managed function |  |   | Write | 
|   [InitiateLiveContactForCase](https://docs.aws.amazon.com/awssupport/latest/user/accessing-support.html)  | Grants permission to initiate a live contact on AWS Support Center. This is an internally managed function |  |   | Write | 
|   [ListInteractionEntries](https://docs.aws.amazon.com/awssupport/latest/user/accessing-support.html)  | Grants permission to retrieve a list of entries within a specific interaction, including messages, status updates, or other relevant data points |  |   | Read | 
|   [ListInteractions](https://docs.aws.amazon.com/awssupport/latest/user/accessing-support.html)  | Grants permission to retrieve a list of interactions, potentially with filters or pagination |  |   | Read | 
|   [PutCaseAttributes](https://docs.aws.amazon.com/awssupport/latest/user/accessing-support.html)  | Grants permission to allow secondary services to attach attributes to AWS Support cases. This is an internally managed function |  |   | Write | 
|   [RateCaseCommunication](https://docs.aws.amazon.com/awssupport/latest/user/accessing-support.html)  | Grants permission to rate an AWS Support case communication |  |   | Write | 
|   [RefreshTrustedAdvisorCheck](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_RefreshTrustedAdvisorCheck.html)  | Grants permission to requests a refresh of the Trusted Advisor check that has the specified check identifier |  |   | Write | 
|   [ResolveCase](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_ResolveCase.html)  | Grants permission to resolve an AWS Support case |  |   | Write | 
|   [ResolveInteraction](https://docs.aws.amazon.com/awssupport/latest/user/accessing-support.html)  | Grants permission to mark a specific interaction as resolved by its unique identifier, indicating that the issue has been addressed and no further action is needed |  |   | Write | 
|   [SearchForCases](https://docs.aws.amazon.com/awssupport/latest/user/accessing-support.html)  | Grants permission to return a list of AWS Support cases that matches the given inputs |  |   | Read | 
|   [StartInteraction](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_StartInteraction.html)  | Grants permission to start a specific interaction to receive personalized troubleshooting assistance for account and technical issues |  |   | Write | 
|   [UpdateCaseSeverity](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_UpdateCaseSeverity.html)  | Grants permission to update the severity for a single AWS Support case. This is an internally managed function |  |   | Write | 
|   [UpdateInteraction](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_UpdateInteraction.html)  | Grants permission to update a specific interaction to receive personalized troubleshooting assistance for account and technical issues |  |   | Write | 
|   [UploadAttachment](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_GetAttachmentUploadLinks.html)  | Grants permission to get a presigned URL to upload an attachment to an AWS Support case |  |   | Write | 

## Resource types defined by AWS Support
<a name="list_support-resources-for-iam-policies"></a>

AWS Support does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS Support
<a name="list_support-policy-keys"></a>

AWS Support has no service-specific condition keys that can be used in the `Condition` element of policy statements.