

# Data retrieval APIs for AWS Support
<a name="awssupport"></a>

AWS Support provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="support-DescribeAttachment"></a>[DescribeAttachment](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeAttachment.html) | Describe attachment detail | Read | 
| <a name="support-DescribeCaseAttributes"></a>[DescribeCaseAttributes](https://docs.aws.amazon.com/awssupport/latest/user/accessing-support.html) | Allow secondary services to read AWS Support case attributes.This is an internally managed function | Read | 
| <a name="support-DescribeCaseOptions"></a>[DescribeCaseOptions](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeCaseOptions.html) | Describe the available options for a single AWS Support case. This is an internally managed function | Read | 
| <a name="support-DescribeCases"></a>[DescribeCases](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeCases.html) | List AWS Support cases that matches the given inputs | Read | 
| <a name="support-DescribeCommunication"></a>[DescribeCommunication](https://docs.aws.amazon.com/awssupport/latest/user/accessing-support.html) | Get a single communication and attachments for a single AWS Support case | Read | 
| <a name="support-DescribeCommunications"></a>[DescribeCommunications](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeCommunications.html) | List the communications and attachments for one or more AWS Support cases | Read | 
| <a name="support-DescribeCreateCaseOptions"></a>[DescribeCreateCaseOptions](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeCreateCaseOptions.html) | Describes the available options for creating a support case | Read | 
| <a name="support-DescribeIssueTypes"></a>[DescribeIssueTypes](https://docs.aws.amazon.com/awssupport/latest/user/accessing-support.html) | Return issue types for AWS Support cases | Read | 
| <a name="support-DescribeRelatedItems"></a>[DescribeRelatedItems](https://docs.aws.amazon.com/awssupport/latest/user/accessing-support.html) | List the related items for an AWS Support case. This is an internally managed function | Read | 
| <a name="support-DescribeServices"></a>[DescribeServices](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeServices.html) | List AWS services and categories that applies to each service | Read | 
| <a name="support-DescribeSeverityLevels"></a>[DescribeSeverityLevels](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeSeverityLevels.html) | List severity levels that can be assigned to an AWS Support case | Read | 
| <a name="support-DescribeSupportLevel"></a>[DescribeSupportLevel](https://docs.aws.amazon.com/awssupport/latest/user/accessing-support.html) | Return the support level for an AWS Account identifier | Read | 
| <a name="support-DescribeSupportedLanguages"></a>[DescribeSupportedLanguages](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeSupportedLanguages.html) | Describes the available support languages for a given category code, service code and issue type | Read | 
| <a name="support-DescribeTrustedAdvisorCheckRefreshStatuses"></a>[DescribeTrustedAdvisorCheckRefreshStatuses](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeTrustedAdvisorCheckRefreshStatuses.html) | Get the status of a Trusted Advisor refresh check based on a list of check identifiers | Read | 
| <a name="support-DescribeTrustedAdvisorCheckResult"></a>[DescribeTrustedAdvisorCheckResult](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeTrustedAdvisorCheckResult.html) | Get the results of the Trusted Advisor check that has the specified check identifier | Read | 
| <a name="support-DescribeTrustedAdvisorCheckSummaries"></a>[DescribeTrustedAdvisorCheckSummaries](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeTrustedAdvisorCheckSummaries.html) | Get the summaries of the results of the Trusted Advisor checks that have the specified check identifiers | Read | 
| <a name="support-DescribeTrustedAdvisorChecks"></a>[DescribeTrustedAdvisorChecks](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeTrustedAdvisorChecks.html) | Get a list of all available Trusted Advisor checks, including name, identifier, category and description | Read | 
| <a name="support-DownloadAttachment"></a>[DownloadAttachment](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_GetAttachmentDownloadLink.html) | Get a presigned URL to download an attachment from an AWS Support case | Read | 
| <a name="support-GetInteraction"></a>[GetInteraction](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_GetInteraction.html) | Retrieve personalized troubleshooting assistance for account and technical issues for a specific interaction | Read | 
| <a name="support-ListInteractionEntries"></a>[ListInteractionEntries](https://docs.aws.amazon.com/awssupport/latest/user/accessing-support.html) | Retrieve a list of entries within a specific interaction, including messages, status updates, or other relevant data points | Read | 
| <a name="support-ListInteractions"></a>[ListInteractions](https://docs.aws.amazon.com/awssupport/latest/user/accessing-support.html) | Retrieve a list of interactions, potentially with filters or pagination | Read | 
| <a name="support-SearchForCases"></a>[SearchForCases](https://docs.aws.amazon.com/awssupport/latest/user/accessing-support.html) | Return a list of AWS Support cases that matches the given inputs | Read | 