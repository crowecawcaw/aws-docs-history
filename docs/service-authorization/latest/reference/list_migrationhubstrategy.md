

# Actions, resources, and condition keys for AWS Migration Hub Strategy Recommendations
<a name="list_migrationhubstrategy"></a>

AWS Migration Hub Strategy Recommendations (service prefix: `migrationhub-strategy`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/migrationhub-strategy/migrationhub-strategy.json) for this service.

**Topics**
+ [API operations defined by AWS Migration Hub Strategy Recommendations](#list_migrationhubstrategy-operations)
+ [Actions defined by AWS Migration Hub Strategy Recommendations](#list_migrationhubstrategy-actions-as-permissions)
+ [Resource types defined by AWS Migration Hub Strategy Recommendations](#list_migrationhubstrategy-resources-for-iam-policies)
+ [Condition keys for AWS Migration Hub Strategy Recommendations](#list_migrationhubstrategy-policy-keys)

## API operations defined by AWS Migration Hub Strategy Recommendations
<a name="list_migrationhubstrategy-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_migrationhubstrategy-actions-as-permissions).




- **   GetApplicationComponentDetails  **
  - **IAM action:**  [migrationhub-strategy:GetApplicationComponentDetails](#list_migrationhubstrategy-action-GetApplicationComponentDetails) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetApplicationComponentStrategies  **
  - **IAM action:**  [migrationhub-strategy:GetApplicationComponentStrategies](#list_migrationhubstrategy-action-GetApplicationComponentStrategies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAssessment  **
  - **IAM action:**  [migrationhub-strategy:GetAssessment](#list_migrationhubstrategy-action-GetAssessment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetImportFileTask  **
  - **IAM action:**  [migrationhub-strategy:GetImportFileTask](#list_migrationhubstrategy-action-GetImportFileTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLatestAssessmentId  **
  - **IAM action:**  [migrationhub-strategy:GetLatestAssessmentId](#list_migrationhubstrategy-action-GetLatestAssessmentId) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPortfolioPreferences  **
  - **IAM action:**  [migrationhub-strategy:GetPortfolioPreferences](#list_migrationhubstrategy-action-GetPortfolioPreferences) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPortfolioSummary  **
  - **IAM action:**  [migrationhub-strategy:GetPortfolioSummary](#list_migrationhubstrategy-action-GetPortfolioSummary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRecommendationReportDetails  **
  - **IAM action:**  [migrationhub-strategy:GetRecommendationReportDetails](#list_migrationhubstrategy-action-GetRecommendationReportDetails) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetServerDetails  **
  - **IAM action:**  [migrationhub-strategy:GetServerDetails](#list_migrationhubstrategy-action-GetServerDetails) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetServerStrategies  **
  - **IAM action:**  [migrationhub-strategy:GetServerStrategies](#list_migrationhubstrategy-action-GetServerStrategies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAnalyzableServers  **
  - **IAM action:**  [migrationhub-strategy:ListAnalyzableServers](#list_migrationhubstrategy-action-ListAnalyzableServers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListApplicationComponents  **
  - **IAM action:**  [migrationhub-strategy:ListApplicationComponents](#list_migrationhubstrategy-action-ListApplicationComponents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCollectors  **
  - **IAM action:**  [migrationhub-strategy:ListCollectors](#list_migrationhubstrategy-action-ListCollectors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListImportFileTask  **
  - **IAM action:**  [migrationhub-strategy:ListImportFileTask](#list_migrationhubstrategy-action-ListImportFileTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServers  **
  - **IAM action:**  [migrationhub-strategy:ListServers](#list_migrationhubstrategy-action-ListServers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutPortfolioPreferences  **
  - **IAM action:**  [migrationhub-strategy:PutPortfolioPreferences](#list_migrationhubstrategy-action-PutPortfolioPreferences) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartAssessment  **
  - **IAM action:**  [migrationhub-strategy:StartAssessment](#list_migrationhubstrategy-action-StartAssessment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartImportFileTask  **
  - **IAM action:**  [migrationhub-strategy:StartImportFileTask](#list_migrationhubstrategy-action-StartImportFileTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartRecommendationReportGeneration  **
  - **IAM action:**  [migrationhub-strategy:StartRecommendationReportGeneration](#list_migrationhubstrategy-action-StartRecommendationReportGeneration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopAssessment  **
  - **IAM action:**  [migrationhub-strategy:StopAssessment](#list_migrationhubstrategy-action-StopAssessment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateApplicationComponentConfig  **
  - **IAM action:**  [migrationhub-strategy:UpdateApplicationComponentConfig](#list_migrationhubstrategy-action-UpdateApplicationComponentConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateServerConfig  **
  - **IAM action:**  [migrationhub-strategy:UpdateServerConfig](#list_migrationhubstrategy-action-UpdateServerConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Migration Hub Strategy Recommendations
<a name="list_migrationhubstrategy-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [GetAntiPattern](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetAntiPattern.html)  | Grants permission to get details of each anti pattern that collector should look at in a customer's environment |  |   | Read | 
|   [GetApplicationComponentDetails](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetApplicationComponentDetails.html)  | Grants permission to get details of an application |  |   | Read | 
|   [GetApplicationComponentStrategies](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetApplicationComponentStrategies.html)  | Grants permission to get a list of all recommended strategies and tools for an application running in a server |  |   | Read | 
|   [GetAssessment](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetAssessment.html)  | Grants permission to retrieve status of an on-going assessment |  |   | Read | 
|   [GetImportFileTask](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetImportFileTask.html)  | Grants permission to get details of a specific import task |  |   | Read | 
|   [GetLatestAssessmentId](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetLatestAssessmentId.html)  | Grants permission to retrieve the latest assessment id |  |   | Read | 
|   [GetMessage](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetMessage.html)  | Grants permission to the collector to receive information from the service |  |   | Read | 
|   [GetPortfolioPreferences](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetPortfolioPreferences.html)  | Grants permission to retrieve customer migration/Modernization preferences |  |   | Read | 
|   [GetPortfolioSummary](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetPortfolioSummary.html)  | Grants permission to retrieve overall summary (number-of servers to rehost etc as well as overall number of anti patterns) |  |   | Read | 
|   [GetRecommendationReportDetails](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetRecommendationReportDetails.html)  | Grants permission to retrieve detailed information about a recommendation report |  |   | Read | 
|   [GetServerDetails](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetServerDetails.html)  | Grants permission to get info about a specific server |  |   | Read | 
|   [GetServerStrategies](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetServerStrategies.html)  | Grants permission to get recommended strategies and tools for a specific server |  |   | Read | 
|   [ListAnalyzableServers](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ListAnalyzableServers.html)  | Grants permission to get a list of all analyzable servers in a customer's vcenter environment |  |   | List | 
|   [ListAntiPatterns](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ListAntiPatterns.html)  | Grants permission to get a list of all anti patterns that collector should look for in a customer's environment |  |   | List | 
|   [ListApplicationComponents](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ListApplicationComponents.html)  | Grants permission to get a list of all applications running on servers on customer's servers |  |   | List | 
|   [ListCollectors](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ListCollectors.html)  | Grants permission to get a list of all collectors installed by the customer |  |   | List | 
|   [ListImportFileTask](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ListImportFileTask.html)  | Grants permission to get list of all imports performed by the customer |  |   | List | 
|   [ListJarArtifacts](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ListJarArtifacts.html)  | Grants permission to get a list of binaries that collector should assess |  |   | List | 
|   [ListServers](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ListServers.html)  | Grants permission to get a list of all servers in a customer's environment |  |   | List | 
|   [PutLogData](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_PutLogData.html)  | Grants permission to the collector to send logs to the service |  |   | Write | 
|   [PutMetricData](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_PutMetricData.html)  | Grants permission to the collector to send metrics to the service |  |   | Write | 
|   [PutPortfolioPreferences](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_PutPortfolioPreferences.html)  | Grants permission to save customer's Migration/Modernization preferences |  |   | Write | 
|   [RegisterCollector](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_RegisterCollector.html)  | Grants permission to register the collector to receive an ID and to start receiving messages from the service |  |   | Write | 
|   [SendMessage](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_SendMessage.html)  | Grants permission to the collector to send information to the service |  |   | Write | 
|   [StartAssessment](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_StartAssessment.html)  | Grants permission to start assessment in a customer's environment (collect data from all servers and provide recommendations) |  |   | Write | 
|   [StartImportFileTask](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_StartImportFileTask.html)  | Grants permission to start importing data from a file provided by customer |  |   | Write | 
|   [StartRecommendationReportGeneration](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_StartRecommendationReportGeneration.html)  | Grants permission to start generating a recommendation report |  |   | Write | 
|   [StopAssessment](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_StopAssessment.html)  | Grants permission to stop an on-going assessment |  |   | Write | 
|   [UpdateApplicationComponentConfig](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_UpdateApplicationComponentConfig.html)  | Grants permission to update details for an application |  |   | Write | 
|   [UpdateCollectorConfiguration](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_UpdateCollectorConfiguration.html)  | Grants permission to the collector to send configuration information to the service |  |   | Write | 
|   [UpdateServerConfig](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_UpdateServerConfig.html)  | Grants permission to update info on a server along with the recommended strategy |  |   | Write | 

## Resource types defined by AWS Migration Hub Strategy Recommendations
<a name="list_migrationhubstrategy-resources-for-iam-policies"></a>

AWS Migration Hub Strategy Recommendations does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS Migration Hub Strategy Recommendations
<a name="list_migrationhubstrategy-policy-keys"></a>

AWS Migration Hub Strategy Recommendations has no service-specific condition keys that can be used in the `Condition` element of policy statements.