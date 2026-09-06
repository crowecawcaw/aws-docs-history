

# Actions, resources, and condition keys for Amazon DevOps Guru
<a name="list_devops-guru"></a>

Amazon DevOps Guru (service prefix: `devops-guru`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/devops-guru/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/devops-guru/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/devops-guru/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/devops-guru/devops-guru.json) for this service.

**Topics**
+ [API operations defined by Amazon DevOps Guru](#list_devops-guru-operations)
+ [Actions defined by Amazon DevOps Guru](#list_devops-guru-actions-as-permissions)
+ [Resource types defined by Amazon DevOps Guru](#list_devops-guru-resources-for-iam-policies)
+ [Condition keys for Amazon DevOps Guru](#list_devops-guru-policy-keys)

## API operations defined by Amazon DevOps Guru
<a name="list_devops-guru-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_devops-guru-actions-as-permissions).




- **   AddNotificationChannel  **
  - **IAM action:**  [devops-guru:AddNotificationChannel](#list_devops-guru-action-AddNotificationChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteInsight  **
  - **IAM action:**  [devops-guru:DeleteInsight](#list_devops-guru-action-DeleteInsight) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAccountHealth  **
  - **IAM action:**  [devops-guru:DescribeAccountHealth](#list_devops-guru-action-DescribeAccountHealth) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAccountOverview  **
  - **IAM action:**  [devops-guru:DescribeAccountOverview](#list_devops-guru-action-DescribeAccountOverview) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAnomaly  **
  - **IAM action:**  [devops-guru:DescribeAnomaly](#list_devops-guru-action-DescribeAnomaly) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEventSourcesConfig  **
  - **IAM action:**  [devops-guru:DescribeEventSourcesConfig](#list_devops-guru-action-DescribeEventSourcesConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFeedback  **
  - **IAM action:**  [devops-guru:DescribeFeedback](#list_devops-guru-action-DescribeFeedback) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeInsight  **
  - **IAM action:**  [devops-guru:DescribeInsight](#list_devops-guru-action-DescribeInsight) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeOrganizationHealth  **
  - **IAM action:**  [devops-guru:DescribeOrganizationHealth](#list_devops-guru-action-DescribeOrganizationHealth) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeOrganizationOverview  **
  - **IAM action:**  [devops-guru:DescribeOrganizationOverview](#list_devops-guru-action-DescribeOrganizationOverview) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeOrganizationResourceCollectionHealth  **
  - **IAM action:**  [devops-guru:DescribeOrganizationResourceCollectionHealth](#list_devops-guru-action-DescribeOrganizationResourceCollectionHealth) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeResourceCollectionHealth  **
  - **IAM action:**  [devops-guru:DescribeResourceCollectionHealth](#list_devops-guru-action-DescribeResourceCollectionHealth) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeServiceIntegration  **
  - **IAM action:**  [devops-guru:DescribeServiceIntegration](#list_devops-guru-action-DescribeServiceIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCostEstimation  **
  - **IAM action:**  [devops-guru:GetCostEstimation](#list_devops-guru-action-GetCostEstimation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourceCollection  **
  - **IAM action:**  [devops-guru:GetResourceCollection](#list_devops-guru-action-GetResourceCollection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAnomaliesForInsight  **
  - **IAM action:**  [devops-guru:ListAnomaliesForInsight](#list_devops-guru-action-ListAnomaliesForInsight) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAnomalousLogGroups  **
  - **IAM action:**  [devops-guru:ListAnomalousLogGroups](#list_devops-guru-action-ListAnomalousLogGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEvents  **
  - **IAM action:**  [devops-guru:ListEvents](#list_devops-guru-action-ListEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInsights  **
  - **IAM action:**  [devops-guru:ListInsights](#list_devops-guru-action-ListInsights) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMonitoredResources  **
  - **IAM action:**  [devops-guru:ListMonitoredResources](#list_devops-guru-action-ListMonitoredResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNotificationChannels  **
  - **IAM action:**  [devops-guru:ListNotificationChannels](#list_devops-guru-action-ListNotificationChannels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOrganizationInsights  **
  - **IAM action:**  [devops-guru:ListOrganizationInsights](#list_devops-guru-action-ListOrganizationInsights) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRecommendations  **
  - **IAM action:**  [devops-guru:ListRecommendations](#list_devops-guru-action-ListRecommendations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutFeedback  **
  - **IAM action:**  [devops-guru:PutFeedback](#list_devops-guru-action-PutFeedback) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveNotificationChannel  **
  - **IAM action:**  [devops-guru:RemoveNotificationChannel](#list_devops-guru-action-RemoveNotificationChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SearchInsights  **
  - **IAM action:**  [devops-guru:SearchInsights](#list_devops-guru-action-SearchInsights) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SearchOrganizationInsights  **
  - **IAM action:**  [devops-guru:SearchOrganizationInsights](#list_devops-guru-action-SearchOrganizationInsights) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   StartCostEstimation  **
  - **IAM action:**  [devops-guru:StartCostEstimation](#list_devops-guru-action-StartCostEstimation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   UpdateEventSourcesConfig  **
  - **IAM action:**  [devops-guru:UpdateEventSourcesConfig](#list_devops-guru-action-UpdateEventSourcesConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateResourceCollection  **
  - **IAM action:**  [devops-guru:UpdateResourceCollection](#list_devops-guru-action-UpdateResourceCollection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateServiceIntegration  **
  - **IAM action:**  [devops-guru:UpdateServiceIntegration](#list_devops-guru-action-UpdateServiceIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon DevOps Guru
<a name="list_devops-guru-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddNotificationChannel](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_AddNotificationChannel.html)  **
  - **Description:** Grants permission to add a notification channel to DevOps Guru
  - **Resource types (\*required):** [topic\*](#list_devops-guru-resource-topic)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteInsight](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_DeleteInsight.html)  **
  - **Description:** Grants permission to delete specified insight in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeAccountHealth](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_DescribeAccountHealth.html)  **
  - **Description:** Grants permission to view the health of operations in your AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeAccountOverview](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_DescribeAccountOverview.html)  **
  - **Description:** Grants permission to view the health of operations within a time range in your AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeAnomaly](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_DescribeAnomaly.html)  **
  - **Description:** Grants permission to list the details of a specified anomaly
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeEventSourcesConfig](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_DescribeEventSourcesConfig.html)  **
  - **Description:** Grants permission to retrieve details about event sources for DevOps Guru
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeFeedback](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_DescribeFeedback.html)  **
  - **Description:** Grants permission to view the feedback details of a specified insight
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeInsight](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_DescribeInsight.html)  **
  - **Description:** Grants permission to list the details of a specified insight
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeOrganizationHealth](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_DescribeOrganizationHealth.html)  **
  - **Description:** Grants permission to view the health of operations in your organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeOrganizationOverview](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_DescribeOrganizationOverview.html)  **
  - **Description:** Grants permission to view the health of operations within a time range in your organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeOrganizationResourceCollectionHealth](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_DescribeOrganizationResourceCollectionHealth.html)  **
  - **Description:** Grants permission to view the health of operations for each AWS CloudFormation stack or AWS Services or accounts specified in DevOps Guru in your organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeResourceCollectionHealth](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_DescribeResourceCollectionHealth.html)  **
  - **Description:** Grants permission to view the health of operations for each AWS CloudFormation stack specified in DevOps Guru
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeServiceIntegration](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_DescribeServiceIntegration.html)  **
  - **Description:** Grants permission to view the integration status of services that can be integrated with DevOps Guru
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCostEstimation](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_GetCostEstimation.html)  **
  - **Description:** Grants permission to list service resource cost estimates
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetResourceCollection](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_GetResourceCollection.html)  **
  - **Description:** Grants permission to list AWS CloudFormation stacks that DevOps Guru is configured to use
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListAnomaliesForInsight](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_ListAnomaliesForInsight.html)  **
  - **Description:** Grants permission to list anomalies of a given insight in your account
  - **Resource types (\*required):** 
  - **Condition keys:** [devops-guru:ServiceNames](#list_devops-guru-devops-guru_ServiceNames)
  - **Access level:** List

- **   [ListAnomalousLogGroups](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_ListAnomalousLogGroups.html)  **
  - **Description:** Grants permission to list log anomalies of a given insight in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEvents](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_ListEvents.html)  **
  - **Description:** Grants permission to list resource events that are evaluated by DevOps Guru
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListInsights](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_ListInsights.html)  **
  - **Description:** Grants permission to list insights in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMonitoredResources](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_ListMonitoredResources.html)  **
  - **Description:** Grants permission to list resource monitored by DevOps Guru in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListNotificationChannels](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_ListNotificationChannels.html)  **
  - **Description:** Grants permission to list notification channels configured for DevOps Guru in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOrganizationInsights](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_ListOrganizationInsights.html)  **
  - **Description:** Grants permission to list insights in your organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRecommendations](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_ListRecommendations.html)  **
  - **Description:** Grants permission to list a specified insight's recommendations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PutFeedback](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_PutFeedback.html)  **
  - **Description:** Grants permission to submit a feedback to DevOps Guru
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RemoveNotificationChannel](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_RemoveNotificationChannel.html)  **
  - **Description:** Grants permission to remove a notification channel from DevOps Guru
  - **Resource types (\*required):** [topic\*](#list_devops-guru-resource-topic)
  - **Condition keys:**  
  - **Access level:** Write

- **   [SearchInsights](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_SearchInsights.html)  **
  - **Description:** Grants permission to search insights in your account
  - **Resource types (\*required):** 
  - **Condition keys:** [devops-guru:ServiceNames](#list_devops-guru-devops-guru_ServiceNames)
  - **Access level:** List

- **   [SearchOrganizationInsights](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_SearchOrganizationInsights.html)  **
  - **Description:** Grants permission to search insights in your organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [StartCostEstimation](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_StartCostEstimation.html)  **
  - **Description:** Grants permission to start the creation of an estimate of the monthly cost
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [UpdateEventSourcesConfig](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_UpdateEventSourcesConfig.html)  **
  - **Description:** Grants permission to update an event source for DevOps Guru
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateResourceCollection](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_UpdateResourceCollection.html)  **
  - **Description:** Grants permission to update the list of AWS CloudFormation stacks that are used to specify which AWS resources in your account are analyzed by DevOps Guru
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateServiceIntegration](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_UpdateServiceIntegration.html)  **
  - **Description:** Grants permission to enable or disable a service that integrates with DevOps Guru
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by Amazon DevOps Guru
<a name="list_devops-guru-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [topic](https://docs.aws.amazon.com/devops-guru/latest/userguide/setting-up.html#setting-up-notifications)  | arn:${Partition}:sns:${Region}:${Account}:${TopicName} |   | 

## Condition keys for Amazon DevOps Guru
<a name="list_devops-guru-policy-keys"></a>

Amazon DevOps Guru defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [devops-guru:ServiceNames](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_ServiceCollection.html)  | Filters access by API to restrict access to given AWS service names | ArrayOfString | 