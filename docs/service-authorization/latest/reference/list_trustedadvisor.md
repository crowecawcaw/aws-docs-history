

# Actions, resources, and condition keys for AWS Trusted Advisor
<a name="list_trustedadvisor"></a>

AWS Trusted Advisor (service prefix: `trustedadvisor`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/awssupport/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/awssupport/latest/user/security.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/trustedadvisor/trustedadvisor.json) for this service.

**Topics**
+ [API operations defined by AWS Trusted Advisor](#list_trustedadvisor-operations)
+ [Actions defined by AWS Trusted Advisor](#list_trustedadvisor-actions-as-permissions)
+ [Permission-only actions for AWS Trusted Advisor](#list_trustedadvisor-permission-only-actions)
+ [Resource types defined by AWS Trusted Advisor](#list_trustedadvisor-resources-for-iam-policies)
+ [Condition keys for AWS Trusted Advisor](#list_trustedadvisor-policy-keys)

## API operations defined by AWS Trusted Advisor
<a name="list_trustedadvisor-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_trustedadvisor-actions-as-permissions).




- **   BatchUpdateRecommendationResourceExclusion  **
  - **IAM action:**  [trustedadvisor:BatchUpdateRecommendationResourceExclusion](#list_trustedadvisor-action-BatchUpdateRecommendationResourceExclusion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetOrganizationRecommendation  **
  - **IAM action:**  [trustedadvisor:GetOrganizationRecommendation](#list_trustedadvisor-action-GetOrganizationRecommendation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRecommendation  **
  - **IAM action:**  [trustedadvisor:DescribeCheckSummaries](#list_trustedadvisor-action-DescribeCheckSummaries)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [trustedadvisor:GetRecommendation](#list_trustedadvisor-action-GetRecommendation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [support:DescribeTrustedAdvisorCheckSummaries](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeTrustedAdvisorCheckSummaries.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListChecks  **
  - **IAM action:**  [trustedadvisor:DescribeChecks](#list_trustedadvisor-action-DescribeChecks)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [trustedadvisor:ListChecks](#list_trustedadvisor-action-ListChecks)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [support:DescribeTrustedAdvisorChecks](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeTrustedAdvisorChecks.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListOrganizationRecommendationAccounts  **
  - **IAM action:**  [trustedadvisor:ListOrganizationRecommendationAccounts](#list_trustedadvisor-action-ListOrganizationRecommendationAccounts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOrganizationRecommendationResources  **
  - **IAM action:**  [trustedadvisor:ListOrganizationRecommendationResources](#list_trustedadvisor-action-ListOrganizationRecommendationResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOrganizationRecommendations  **
  - **IAM action:**  [trustedadvisor:ListOrganizationRecommendations](#list_trustedadvisor-action-ListOrganizationRecommendations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRecommendationResources  **
  - **IAM action:**  [trustedadvisor:DescribeCheckItems](#list_trustedadvisor-action-DescribeCheckItems)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [trustedadvisor:ListRecommendationResources](#list_trustedadvisor-action-ListRecommendationResources)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [support:DescribeTrustedAdvisorCheckResult](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeTrustedAdvisorCheckResult.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListRecommendations  **
  - **IAM action:**  [trustedadvisor:DescribeCheckSummaries](#list_trustedadvisor-action-DescribeCheckSummaries)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [trustedadvisor:ListRecommendations](#list_trustedadvisor-action-ListRecommendations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [support:DescribeTrustedAdvisorCheckSummaries](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeTrustedAdvisorCheckSummaries.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListRecommendationsForResource  **
  - **IAM action:**  [trustedadvisor:DescribeCheckItems](#list_trustedadvisor-action-DescribeCheckItems)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [trustedadvisor:ListRecommendationsForResource](#list_trustedadvisor-action-ListRecommendationsForResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [support:DescribeTrustedAdvisorCheckResult](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeTrustedAdvisorCheckResult.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   UpdateOrganizationRecommendationLifecycle  **
  - **IAM action:**  [trustedadvisor:UpdateOrganizationRecommendationLifecycle](#list_trustedadvisor-action-UpdateOrganizationRecommendationLifecycle) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRecommendationLifecycle  **
  - **IAM action:**  [trustedadvisor:UpdateRecommendationLifecycle](#list_trustedadvisor-action-UpdateRecommendationLifecycle) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Trusted Advisor
<a name="list_trustedadvisor-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/awssupport/latest/user/get-started-with-aws-trusted-advisor-api.html)  **
  - **Description:** Grants permission to update one or more exclusion status for a list of recommendation resources
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteNotificationConfigurationForDelegatedAdmin](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  **
  - **Description:** Grants permission to the organization management account to delete email notification preferences from a delegated administrator account for Trusted Advisor Priority
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeCheckItems](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  **
  - **Description:** Grants permission to view details for the check items
  - **Resource types (\*required):** [checks\*](#list_trustedadvisor-resource-checks)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeCheckRefreshStatuses](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  **
  - **Description:** Grants permission to view the refresh statuses for AWS Trusted Advisor checks
  - **Resource types (\*required):** [checks\*](#list_trustedadvisor-resource-checks)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeCheckSummaries](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  **
  - **Description:** Grants permission to view AWS Trusted Advisor check summaries
  - **Resource types (\*required):** [checks\*](#list_trustedadvisor-resource-checks)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeChecks](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  **
  - **Description:** Grants permission to view details for AWS Trusted Advisor checks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeNotificationConfigurations](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  **
  - **Description:** Grants permission to get your email notification preferences for Trusted Advisor Priority
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeRisk](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  **
  - **Description:** Grants permission to view risk details in AWS Trusted Advisor Priority
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeRiskResources](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  **
  - **Description:** Grants permission to view affected resources for a risk in AWS Trusted Advisor Priority
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeRisks](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  **
  - **Description:** Grants permission to view risks in AWS Trusted Advisor Priority
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DownloadRisk](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  **
  - **Description:** Grants permission to download a file that contains details about the risk in AWS Trusted Advisor Priority
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetOrganizationRecommendation](https://docs.aws.amazon.com/awssupport/latest/user/get-started-with-aws-trusted-advisor-api.html)  **
  - **Description:** Grants permission to get a specific recommendation within an AWS Organization's organization. This API supports only prioritized recommendations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetRecommendation](https://docs.aws.amazon.com/awssupport/latest/user/get-started-with-aws-trusted-advisor-api.html)  **
  - **Description:** Grants permission to get a specific Recommendation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListChecks](https://docs.aws.amazon.com/awssupport/latest/user/get-started-with-aws-trusted-advisor-api.html)  **
  - **Description:** Grants permission to list a filterable set of Checks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOrganizationRecommendationAccounts](https://docs.aws.amazon.com/awssupport/latest/user/get-started-with-aws-trusted-advisor-api.html)  **
  - **Description:** Grants permission to list the accounts that own the resources for an AWS Organization aggregate recommendation. This API only supports prioritized recommendations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOrganizationRecommendationResources](https://docs.aws.amazon.com/awssupport/latest/user/get-started-with-aws-trusted-advisor-api.html)  **
  - **Description:** Grants permission to list Resources of a Recommendation within an AWS Organization. This API only supports prioritized recommendations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOrganizationRecommendations](https://docs.aws.amazon.com/awssupport/latest/user/get-started-with-aws-trusted-advisor-api.html)  **
  - **Description:** Grants permission to list a filterable set of Recommendations within an AWS Organization. This API only supports prioritized recommendations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRecommendationResources](https://docs.aws.amazon.com/awssupport/latest/user/get-started-with-aws-trusted-advisor-api.html)  **
  - **Description:** Grants permission to list Resources of a Recommendation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRecommendations](https://docs.aws.amazon.com/awssupport/latest/user/get-started-with-aws-trusted-advisor-api.html)  **
  - **Description:** Grants permission to list a filterable set of Recommendations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRecommendationsForResource](https://docs.aws.amazon.com/awssupport/latest/user/get-started-with-aws-trusted-advisor-api.html)  **
  - **Description:** Grants permission to list Recommendation of a Resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [RefreshCheck](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  **
  - **Description:** Grants permission to refresh an AWS Trusted Advisor check
  - **Resource types (\*required):** [checks\*](#list_trustedadvisor-resource-checks)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateNotificationConfigurations](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  **
  - **Description:** Grants permission to create or update your email notification preferences for Trusted Advisor Priority
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateOrganizationRecommendationLifecycle](https://docs.aws.amazon.com/awssupport/latest/user/get-started-with-aws-trusted-advisor-api.html)  **
  - **Description:** Grants permission to update the lifecyle of a Recommendation within an AWS Organization. This API only supports prioritized recommendations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateRecommendationLifecycle](https://docs.aws.amazon.com/awssupport/latest/user/get-started-with-aws-trusted-advisor-api.html)  **
  - **Description:** Grants permission to update the lifecyle of a Recommendation. This API only supports prioritized recommendations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateRiskStatus](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  **
  - **Description:** Grants permission to update the risk status in AWS Trusted Advisor Priority
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Permission-only actions for AWS Trusted Advisor
<a name="list_trustedadvisor-permission-only-actions"></a>

The following actions are defined by AWS Trusted Advisor but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [DescribeAccount](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  **
  - **Description:** Grants permission to view the AWS Support plan and various AWS Trusted Advisor preferences
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeAccountAccess](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  **
  - **Description:** Grants permission to view if the AWS account has enabled or disabled AWS Trusted Advisor
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeCheckStatusHistoryChanges](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  **
  - **Description:** Grants permission to view the results and changed statuses for checks in the last 30 days
  - **Resource types (\*required):** [checks\*](#list_trustedadvisor-resource-checks)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeNotificationPreferences](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  **
  - **Description:** Grants permission to view the notification preferences for the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeOrganization](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  **
  - **Description:** Grants permission to view if the AWS account meets the requirements to enable the organizational view feature
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeOrganizationAccounts](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  **
  - **Description:** Grants permission to view the linked AWS accounts that are in the organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeReports](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  **
  - **Description:** Grants permission to view details for organizational view reports, such as the report name, runtime, date created, status, and format
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeServiceMetadata](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  **
  - **Description:** Grants permission to view information about organizational view reports, such as the AWS Regions, check categories, check names, and resource statuses
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ExcludeCheckItems](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  **
  - **Description:** Grants permission to exclude recommendations for AWS Trusted Advisor checks
  - **Resource types (\*required):** [checks\*](#list_trustedadvisor-resource-checks)
  - **Condition keys:**  
  - **Access level:** Write

- **   [GenerateReport](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  **
  - **Description:** Grants permission to create a report for AWS Trusted Advisor checks in your organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [IncludeCheckItems](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  **
  - **Description:** Grants permission to include recommendations for AWS Trusted Advisor checks
  - **Resource types (\*required):** [checks\*](#list_trustedadvisor-resource-checks)
  - **Condition keys:**  
  - **Access level:** Write

- **   [ListAccountsForParent](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  **
  - **Description:** Grants permission to view, in the Trusted Advisor console, all of the accounts in an AWS organization that are contained by a root or organizational unit (OU)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListOrganizationalUnitsForParent](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  **
  - **Description:** Grants permission to view, in the Trusted Advisor console, all of the organizational units (OUs) in a parent organizational unit or root
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListRoots](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  **
  - **Description:** Grants permission to view, in the Trusted Advisor console, all of the roots that are defined in an AWS organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [SetAccountAccess](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  **
  - **Description:** Grants permission to enable or disable AWS Trusted Advisor for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SetOrganizationAccess](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  **
  - **Description:** Grants permission to enable the organizational view feature for AWS Trusted Advisor
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateNotificationPreferences](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html#trusted-advisor-operations)  **
  - **Description:** Grants permission to update notification preferences for AWS Trusted Advisor
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by AWS Trusted Advisor
<a name="list_trustedadvisor-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [checks](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_TrustedAdvisorCheckDescription.html)  | arn:${Partition}:trustedadvisor:${Region}:${Account}:checks/${CategoryCode}/${CheckId} |   | 

## Condition keys for AWS Trusted Advisor
<a name="list_trustedadvisor-policy-keys"></a>

AWS Trusted Advisor has no service-specific condition keys that can be used in the `Condition` element of policy statements.