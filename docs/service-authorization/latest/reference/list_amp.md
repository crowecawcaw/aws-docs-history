

# Actions, resources, and condition keys for Amazon Managed Service for Prometheus
<a name="list_amp"></a>

Amazon Managed Service for Prometheus (service prefix: `aps`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/prometheus/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/prometheus/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/aps/aps.json) for this service.

**Topics**
+ [API operations defined by Amazon Managed Service for Prometheus](#list_amp-operations)
+ [Actions defined by Amazon Managed Service for Prometheus](#list_amp-actions-as-permissions)
+ [Resource types defined by Amazon Managed Service for Prometheus](#list_amp-resources-for-iam-policies)
+ [Condition keys for Amazon Managed Service for Prometheus](#list_amp-policy-keys)

## API operations defined by Amazon Managed Service for Prometheus
<a name="list_amp-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_amp-actions-as-permissions).




- **   CreateAlertManagerDefinition  **
  - **IAM action:**  [aps:CreateAlertManagerDefinition](#list_amp-action-CreateAlertManagerDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAnomalyDetector  **
  - **IAM action:**  [aps:CreateAnomalyDetector](#list_amp-action-CreateAnomalyDetector)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aps:TagResource](#list_amp-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateLoggingConfiguration  **
  - **IAM action:**  [aps:CreateLoggingConfiguration](#list_amp-action-CreateLoggingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateQueryLoggingConfiguration  **
  - **IAM action:**  [aps:CreateQueryLoggingConfiguration](#list_amp-action-CreateQueryLoggingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateRuleGroupsNamespace  **
  - **IAM action:**  [aps:CreateRuleGroupsNamespace](#list_amp-action-CreateRuleGroupsNamespace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aps:TagResource](#list_amp-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateScraper  **
  - **IAM action:**  [aps:CreateScraper](#list_amp-action-CreateScraper)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aps:TagResource](#list_amp-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** aps.amazonaws.com / **Access level:** Write

- **   CreateWorkspace  **
  - **IAM action:**  [aps:CreateWorkspace](#list_amp-action-CreateWorkspace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aps:TagResource](#list_amp-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAlertManagerDefinition  **
  - **IAM action:**  [aps:DeleteAlertManagerDefinition](#list_amp-action-DeleteAlertManagerDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAnomalyDetector  **
  - **IAM action:**  [aps:DeleteAnomalyDetector](#list_amp-action-DeleteAnomalyDetector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLoggingConfiguration  **
  - **IAM action:**  [aps:DeleteLoggingConfiguration](#list_amp-action-DeleteLoggingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteQueryLoggingConfiguration  **
  - **IAM action:**  [aps:DeleteQueryLoggingConfiguration](#list_amp-action-DeleteQueryLoggingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourcePolicy  **
  - **IAM action:**  [aps:DeleteResourcePolicy](#list_amp-action-DeleteResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRuleGroupsNamespace  **
  - **IAM action:**  [aps:DeleteRuleGroupsNamespace](#list_amp-action-DeleteRuleGroupsNamespace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteScraper  **
  - **IAM action:**  [aps:DeleteScraper](#list_amp-action-DeleteScraper) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteScraperLoggingConfiguration  **
  - **IAM action:**  [aps:DeleteScraperLoggingConfiguration](#list_amp-action-DeleteScraperLoggingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWorkspace  **
  - **IAM action:**  [aps:DeleteWorkspace](#list_amp-action-DeleteWorkspace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAlertManagerDefinition  **
  - **IAM action:**  [aps:DescribeAlertManagerDefinition](#list_amp-action-DescribeAlertManagerDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAnomalyDetector  **
  - **IAM action:**  [aps:DescribeAnomalyDetector](#list_amp-action-DescribeAnomalyDetector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeLoggingConfiguration  **
  - **IAM action:**  [aps:DescribeLoggingConfiguration](#list_amp-action-DescribeLoggingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeQueryLoggingConfiguration  **
  - **IAM action:**  [aps:DescribeQueryLoggingConfiguration](#list_amp-action-DescribeQueryLoggingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeResourcePolicy  **
  - **IAM action:**  [aps:DescribeResourcePolicy](#list_amp-action-DescribeResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRuleGroupsNamespace  **
  - **IAM action:**  [aps:DescribeRuleGroupsNamespace](#list_amp-action-DescribeRuleGroupsNamespace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeScraper  **
  - **IAM action:**  [aps:DescribeScraper](#list_amp-action-DescribeScraper) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeScraperLoggingConfiguration  **
  - **IAM action:**  [aps:DescribeScraperLoggingConfiguration](#list_amp-action-DescribeScraperLoggingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeWorkspace  **
  - **IAM action:**  [aps:DescribeWorkspace](#list_amp-action-DescribeWorkspace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeWorkspaceConfiguration  **
  - **IAM action:**  [aps:DescribeWorkspaceConfiguration](#list_amp-action-DescribeWorkspaceConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDefaultScraperConfiguration  **
  - **IAM action:**  [aps:GetDefaultScraperConfiguration](#list_amp-action-GetDefaultScraperConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAnomalyDetectors  **
  - **IAM action:**  [aps:ListAnomalyDetectors](#list_amp-action-ListAnomalyDetectors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRuleGroupsNamespaces  **
  - **IAM action:**  [aps:ListRuleGroupsNamespaces](#list_amp-action-ListRuleGroupsNamespaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListScrapers  **
  - **IAM action:**  [aps:ListScrapers](#list_amp-action-ListScrapers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [aps:ListTagsForResource](#list_amp-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListWorkspaces  **
  - **IAM action:**  [aps:ListWorkspaces](#list_amp-action-ListWorkspaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutAlertManagerDefinition  **
  - **IAM action:**  [aps:PutAlertManagerDefinition](#list_amp-action-PutAlertManagerDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutAnomalyDetector  **
  - **IAM action:**  [aps:PutAnomalyDetector](#list_amp-action-PutAnomalyDetector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutResourcePolicy  **
  - **IAM action:**  [aps:PutResourcePolicy](#list_amp-action-PutResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutRuleGroupsNamespace  **
  - **IAM action:**  [aps:PutRuleGroupsNamespace](#list_amp-action-PutRuleGroupsNamespace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [aps:TagResource](#list_amp-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [aps:UntagResource](#list_amp-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateLoggingConfiguration  **
  - **IAM action:**  [aps:UpdateLoggingConfiguration](#list_amp-action-UpdateLoggingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateQueryLoggingConfiguration  **
  - **IAM action:**  [aps:UpdateQueryLoggingConfiguration](#list_amp-action-UpdateQueryLoggingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateScraper  **
  - **IAM action:**  [aps:UpdateScraper](#list_amp-action-UpdateScraper)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** aps.amazonaws.com / **Access level:** Write

- **   UpdateScraperLoggingConfiguration  **
  - **IAM action:**  [aps:UpdateScraperLoggingConfiguration](#list_amp-action-UpdateScraperLoggingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateWorkspaceAlias  **
  - **IAM action:**  [aps:UpdateWorkspaceAlias](#list_amp-action-UpdateWorkspaceAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateWorkspaceConfiguration  **
  - **IAM action:**  [aps:UpdateWorkspaceConfiguration](#list_amp-action-UpdateWorkspaceConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Managed Service for Prometheus
<a name="list_amp-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateAlertManagerAlerts](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-CreateAlertManagerAlerts.html)  **
  - **Description:** Grants permission to create alerts
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAlertManagerDefinition](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_CreateAlertManagerDefinition.html)  **
  - **Description:** Grants permission to create an alert manager definition
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAnomalyDetector](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_CreateAnomalyDetector.html)  **
  - **Description:** Grants permission to create an anomaly detector
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLoggingConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_CreateLoggingConfiguration.html)  **
  - **Description:** Grants permission to create a logging configuration
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Write

- **   [CreateQueryLoggingConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_CreateQueryLoggingConfiguration.html)  **
  - **Description:** Grants permission to create a query logging configuration
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRuleGroupsNamespace](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_CreateRuleGroupsNamespace.html)  **
  - **Description:** Grants permission to create a rule groups namespace
  - **Resource types (\*required):** [rulegroupsnamespace\*](#list_amp-resource-rulegroupsnamespace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Write

- **   [CreateScraper](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_CreateScraper.html)  **
  - **Description:** Grants permission to create a scraper
  - **Resource types (\*required):** [cluster\*](#list_amp-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Write

- **   [CreateWorkspace](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_CreateWorkspace.html)  **
  - **Description:** Grants permission to create a workspace
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAlertManagerDefinition](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DeleteAlertManagerDefinition.html)  **
  - **Description:** Grants permission to delete an alert manager definition
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAlertManagerSilence](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-DeleteAlertManagerSilence.html)  **
  - **Description:** Grants permission to delete a silence
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAnomalyDetector](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DeleteAnomalyDetector.html)  **
  - **Description:** Grants permission to delete an anomaly detector
  - **Resource types (\*required):** [anomalydetector\*](#list_amp-resource-anomalydetector) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteLoggingConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DeleteLoggingConfiguration.html)  **
  - **Description:** Grants permission to delete a logging configuration
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteQueryLoggingConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DeleteQueryLoggingConfiguration.html)  **
  - **Description:** Grants permission to delete a query logging configuration
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to delete workspace resource policy
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteRuleGroupsNamespace](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DeleteRuleGroupsNamespace.html)  **
  - **Description:** Grants permission to delete a rule groups namespace
  - **Resource types (\*required):** [rulegroupsnamespace\*](#list_amp-resource-rulegroupsnamespace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteScraper](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DeleteScraper.html)  **
  - **Description:** Grants permission to delete a scraper
  - **Resource types (\*required):** [scraper\*](#list_amp-resource-scraper)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteScraperLoggingConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DeleteScraperLoggingConfiguration.html)  **
  - **Description:** Grants permission to delete a scraper logging configuration
  - **Resource types (\*required):** [scraper\*](#list_amp-resource-scraper)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteWorkspace](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DeleteWorkspace.html)  **
  - **Description:** Grants permission to delete a workspace
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Write

- **   [DescribeAlertManagerDefinition](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeAlertManagerDefinition.html)  **
  - **Description:** Grants permission to describe an alert manager definition
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Read

- **   [DescribeAnomalyDetector](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeAnomalyDetector.html)  **
  - **Description:** Grants permission to describe an anomaly detector
  - **Resource types (\*required):** [anomalydetector\*](#list_amp-resource-anomalydetector) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Read

- **   [DescribeLoggingConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeLoggingConfiguration.html)  **
  - **Description:** Grants permission to describe a logging configuration
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Read

- **   [DescribeQueryLoggingConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeQueryLoggingConfiguration.html)  **
  - **Description:** Grants permission to describe a query logging configuration
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Read

- **   [DescribeResourcePolicy](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeResourcePolicy.html)  **
  - **Description:** Grants permission to describe workspace resource policy
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Read

- **   [DescribeRuleGroupsNamespace](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeRuleGroupsNamespace.html)  **
  - **Description:** Grants permission to describe a rule groups namespace
  - **Resource types (\*required):** [rulegroupsnamespace\*](#list_amp-resource-rulegroupsnamespace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Read

- **   [DescribeScraper](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeScraper.html)  **
  - **Description:** Grants permission to describe a scraper
  - **Resource types (\*required):** [scraper\*](#list_amp-resource-scraper)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Read

- **   [DescribeScraperLoggingConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeScraperLoggingConfiguration.html)  **
  - **Description:** Grants permission to describe a scraper logging configuration
  - **Resource types (\*required):** [scraper\*](#list_amp-resource-scraper)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Read

- **   [DescribeWorkspace](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeWorkspace.html)  **
  - **Description:** Grants permission to describe a workspace
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Read

- **   [DescribeWorkspaceConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeWorkspaceConfiguration.html)  **
  - **Description:** Grants permission to describe workspace configuration
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Read

- **   [GetAlertManagerSilence](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-GetAlertManagerSilence.html)  **
  - **Description:** Grants permission to get a silence
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Read

- **   [GetAlertManagerStatus](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-GetAlertManagerStatus.html)  **
  - **Description:** Grants permission to get current status of an alertmanager
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Read

- **   [GetDefaultScraperConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_GetDefaultScraperConfiguration.html)  **
  - **Description:** Grants permission to get default scraper configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetLabels](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-GetLabels.html)  **
  - **Description:** Grants permission to retrieve AMP workspace labels
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Read

- **   [GetMetricMetadata](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-GetMetricMetadata.html)  **
  - **Description:** Grants permission to retrieve the metadata for AMP workspace metrics
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Read

- **   [GetSeries](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-GetSeries.html)  **
  - **Description:** Grants permission to retrieve AMP workspace time series data
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Read

- **   [ListAlertManagerAlertGroups](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-ListAlertManagerAlertGroups.html)  **
  - **Description:** Grants permission to list groups
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Read

- **   [ListAlertManagerAlerts](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-ListAlertManagerAlerts.html)  **
  - **Description:** Grants permission to list alerts
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Read

- **   [ListAlertManagerReceivers](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-ListAlertManagerReceivers.html)  **
  - **Description:** Grants permission to list receivers
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Read

- **   [ListAlertManagerSilences](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-ListAlertManagerSilences.html)  **
  - **Description:** Grants permission to list silences
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Read

- **   [ListAlerts](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-ListAlerts.html)  **
  - **Description:** Grants permission to list active alerts
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Read

- **   [ListAnomalyDetectors](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ListAnomalyDetectors.html)  **
  - **Description:** Grants permission to list anomaly detectors
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** List

- **   [ListRuleGroupsNamespaces](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ListRuleGroupsNamespaces.html)  **
  - **Description:** Grants permission to list rule groups namespaces
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** List

- **   [ListRules](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-ListRules.html)  **
  - **Description:** Grants permission to list alerting and recording rules
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Read

- **   [ListScrapers](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ListScrapers.html)  **
  - **Description:** Grants permission to list scrapers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags on an AMP resource
  - **Resource types (\*required):** [anomalydetector](#list_amp-resource-anomalydetector) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Resource types (\*required):** [rulegroupsnamespace](#list_amp-resource-rulegroupsnamespace) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Resource types (\*required):** [scraper](#list_amp-resource-scraper) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Resource types (\*required):** [workspace](#list_amp-resource-workspace) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Read

- **   [ListWorkspaces](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ListWorkspaces.html)  **
  - **Description:** Grants permission to list workspaces
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PreviewAnomalyDetector](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-PreviewAnomalyDetector.html)  **
  - **Description:** Grants permission to preview anomaly detection on AMP workspace metrics
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Read

- **   [PutAlertManagerDefinition](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_PutAlertManagerDefinition.html)  **
  - **Description:** Grants permission to update an alert manager definition
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Write

- **   [PutAlertManagerSilences](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-PutAlertManagerSilences.html)  **
  - **Description:** Grants permission to create or update a silence
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Write

- **   [PutAnomalyDetector](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_PutAnomalyDetector.html)  **
  - **Description:** Grants permission to update an anomaly detector
  - **Resource types (\*required):** [anomalydetector\*](#list_amp-resource-anomalydetector) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Write

- **   [PutResourcePolicy](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_PutResourcePolicy.html)  **
  - **Description:** Grants permission to create and update workspace resource policy
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Write

- **   [PutRuleGroupsNamespace](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_PutRuleGroupsNamespace.html)  **
  - **Description:** Grants permission to update a rule groups namespace
  - **Resource types (\*required):** [rulegroupsnamespace\*](#list_amp-resource-rulegroupsnamespace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Write

- **   [QueryMetrics](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-QueryMetrics.html)  **
  - **Description:** Grants permission to run a query on AMP workspace metrics
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Read

- **   [RemoteWrite](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-RemoteWrite.html)  **
  - **Description:** Grants permission to perform a remote write operation to initiate the streaming of metrics to AMP workspace
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag an AMP resource
  - **Resource types (\*required):** [anomalydetector](#list_amp-resource-anomalydetector) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Resource types (\*required):** [rulegroupsnamespace](#list_amp-resource-rulegroupsnamespace) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Resource types (\*required):** [scraper](#list_amp-resource-scraper) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Resource types (\*required):** [workspace](#list_amp-resource-workspace) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag an AMP resource
  - **Resource types (\*required):** [anomalydetector](#list_amp-resource-anomalydetector) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Resource types (\*required):** [rulegroupsnamespace](#list_amp-resource-rulegroupsnamespace) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Resource types (\*required):** [scraper](#list_amp-resource-scraper) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Resource types (\*required):** [workspace](#list_amp-resource-workspace) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateLoggingConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_UpdateLoggingConfiguration.html)  **
  - **Description:** Grants permission to update a logging configuration
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateQueryLoggingConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_UpdateQueryLoggingConfiguration.html)  **
  - **Description:** Grants permission to update a query logging configuration
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateScraper](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_UpdateScraper.html)  **
  - **Description:** Grants permission to update a scraper
  - **Resource types (\*required):** [scraper\*](#list_amp-resource-scraper) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Resource types (\*required):** [workspace](#list_amp-resource-workspace) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateScraperLoggingConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_UpdateScraperLoggingConfiguration.html)  **
  - **Description:** Grants permission to put a scraper logging configuration
  - **Resource types (\*required):** [scraper\*](#list_amp-resource-scraper)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateWorkspaceAlias](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_UpdateWorkspaceAlias.html)  **
  - **Description:** Grants permission to modify the alias of existing AMP workspace
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateWorkspaceConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_UpdateWorkspaceConfiguration.html)  **
  - **Description:** Grants permission to update workspace configuration
  - **Resource types (\*required):** [workspace\*](#list_amp-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys)
  - **Access level:** Write



## Resource types defined by Amazon Managed Service for Prometheus
<a name="list_amp-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [anomalydetector](https://docs.aws.amazon.com/prometheus/latest/userguide/security-iam.html)  | arn:${Partition}:aps:${Region}:${Account}:anomalydetector/${WorkspaceId}/${AnomalyDetectorId} | [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys) | 
|  [cluster](https://docs.aws.amazon.com/eks/latest/userguide/clusters.html)  | arn:${Partition}:eks:${Region}:${Account}:cluster/${ClusterName} | [aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_) | 
|  [rulegroupsnamespace](https://docs.aws.amazon.com/prometheus/latest/userguide/security-iam.html)  | arn:${Partition}:aps:${Region}:${Account}:rulegroupsnamespace/${WorkspaceId}/${Namespace} | [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys) | 
|  [scraper](https://docs.aws.amazon.com/prometheus/latest/userguide/security-iam.html)  | arn:${Partition}:aps:${Region}:${Account}:scraper/${ScraperId} | [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys) | 
|  [workspace](https://docs.aws.amazon.com/prometheus/latest/userguide/security-iam.html)  | arn:${Partition}:aps:${Region}:${Account}:workspace/${WorkspaceId} | [aws:RequestTag/${TagKey}](#list_amp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amp-aws_TagKeys) | 

## Condition keys for Amazon Managed Service for Prometheus
<a name="list_amp-policy-keys"></a>

Amazon Managed Service for Prometheus defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access based on the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access based on the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access based on the tag keys that are passed in the request | ArrayOfString | 