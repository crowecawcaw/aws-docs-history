

# Actions, resources, and condition keys for AWS Application Discovery Service
<a name="list_discovery"></a>

AWS Application Discovery Service (service prefix: `discovery`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/application-discovery/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/application-discovery/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/application-discovery/latest/userguide/security_iam_service-with-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/discovery/discovery.json) for this service.

**Topics**
+ [API operations defined by AWS Application Discovery Service](#list_discovery-operations)
+ [Actions defined by AWS Application Discovery Service](#list_discovery-actions-as-permissions)
+ [Resource types defined by AWS Application Discovery Service](#list_discovery-resources-for-iam-policies)
+ [Condition keys for AWS Application Discovery Service](#list_discovery-policy-keys)

## API operations defined by AWS Application Discovery Service
<a name="list_discovery-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_discovery-actions-as-permissions).




- **   AssociateConfigurationItemsToApplication  **
  - **IAM action:**  [discovery:AssociateConfigurationItemsToApplication](#list_discovery-action-AssociateConfigurationItemsToApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDeleteAgents  **
  - **IAM action:**  [discovery:BatchDeleteAgents](#list_discovery-action-BatchDeleteAgents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDeleteImportData  **
  - **IAM action:**  [discovery:BatchDeleteImportData](#list_discovery-action-BatchDeleteImportData) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateApplication  **
  - **IAM action:**  [discovery:CreateApplication](#list_discovery-action-CreateApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateTags  **
  - **IAM action:**  [discovery:CreateTags](#list_discovery-action-CreateTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   DeleteApplications  **
  - **IAM action:**  [discovery:DeleteApplications](#list_discovery-action-DeleteApplications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTags  **
  - **IAM action:**  [discovery:DeleteTags](#list_discovery-action-DeleteTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   DescribeAgents  **
  - **IAM action:**  [discovery:DescribeAgents](#list_discovery-action-DescribeAgents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeBatchDeleteConfigurationTask  **
  - **IAM action:**  [discovery:DescribeBatchDeleteConfigurationTask](#list_discovery-action-DescribeBatchDeleteConfigurationTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeConfigurations  **
  - **IAM action:**  [discovery:DescribeConfigurations](#list_discovery-action-DescribeConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeContinuousExports  **
  - **IAM action:**  [discovery:DescribeContinuousExports](#list_discovery-action-DescribeContinuousExports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeExportConfigurations  **
  - **IAM action:**  [discovery:DescribeExportConfigurations](#list_discovery-action-DescribeExportConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeExportTasks  **
  - **IAM action:**  [discovery:DescribeExportTasks](#list_discovery-action-DescribeExportTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeImportTasks  **
  - **IAM action:**  [discovery:DescribeImportTasks](#list_discovery-action-DescribeImportTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeTags  **
  - **IAM action:**  [discovery:DescribeTags](#list_discovery-action-DescribeTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisassociateConfigurationItemsFromApplication  **
  - **IAM action:**  [discovery:DisassociateConfigurationItemsFromApplication](#list_discovery-action-DisassociateConfigurationItemsFromApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ExportConfigurations  **
  - **IAM action:**  [discovery:ExportConfigurations](#list_discovery-action-ExportConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetDiscoverySummary  **
  - **IAM action:**  [discovery:GetDiscoverySummary](#list_discovery-action-GetDiscoverySummary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListConfigurations  **
  - **IAM action:**  [discovery:ListConfigurations](#list_discovery-action-ListConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServerNeighbors  **
  - **IAM action:**  [discovery:ListServerNeighbors](#list_discovery-action-ListServerNeighbors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   StartBatchDeleteConfigurationTask  **
  - **IAM action:**  [discovery:StartBatchDeleteConfigurationTask](#list_discovery-action-StartBatchDeleteConfigurationTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartContinuousExport  **
  - **IAM action:**  [discovery:StartContinuousExport](#list_discovery-action-StartContinuousExport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartDataCollectionByAgentIds  **
  - **IAM action:**  [discovery:StartDataCollectionByAgentIds](#list_discovery-action-StartDataCollectionByAgentIds) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartExportTask  **
  - **IAM action:**  [discovery:StartExportTask](#list_discovery-action-StartExportTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartImportTask  **
  - **IAM action:**  [discovery:StartImportTask](#list_discovery-action-StartImportTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopContinuousExport  **
  - **IAM action:**  [discovery:StopContinuousExport](#list_discovery-action-StopContinuousExport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopDataCollectionByAgentIds  **
  - **IAM action:**  [discovery:StopDataCollectionByAgentIds](#list_discovery-action-StopDataCollectionByAgentIds) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateApplication  **
  - **IAM action:**  [discovery:UpdateApplication](#list_discovery-action-UpdateApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Application Discovery Service
<a name="list_discovery-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [AssociateConfigurationItemsToApplication](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_AssociateConfigurationItemsToApplication.html)  | Grants permission to AssociateConfigurationItemsToApplication API. AssociateConfigurationItemsToApplication associates one or more configuration items with an application |  |   | Write | 
|   [BatchDeleteAgents](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_BatchDeleteAgents.html)  | Grants permission to BatchDeleteAgents API. BatchDeleteAgents deletes one or more agents/data collectors associated with your account, each identified by its agent ID. Deleting a data collector does not delete the previous data collected |  |   | Write | 
|   [BatchDeleteImportData](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_BatchDeleteImportData.html)  | Grants permission to BatchDeleteImportData API. BatchDeleteImportData deletes one or more Migration Hub import tasks, each identified by their import ID. Each import task has a number of records, which can identify servers or applications |  |   | Write | 
|   [CreateApplication](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_CreateApplication.html)  | Grants permission to CreateApplication API. CreateApplication creates an application with the given name and description |  |   | Write | 
|   [CreateTags](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_CreateTags.html)  | Grants permission to CreateTags API. CreateTags creates one or more tags for configuration items. Tags are metadata that help you categorize IT assets. This API accepts a list of multiple configuration items |  |   | Tagging, Write | 
|   [DeleteApplications](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DeleteApplications.html)  | Grants permission to DeleteApplications API. DeleteApplications deletes a list of applications and their associations with configuration items |  |   | Write | 
|   [DeleteTags](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DeleteTags.html)  | Grants permission to DeleteTags API. DeleteTags deletes the association between configuration items and one or more tags. This API accepts a list of multiple configuration items |  | [aws:TagKeys](#list_discovery-aws_TagKeys) | Tagging, Write | 
|   [DescribeAgents](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeAgents.html)  | Grants permission to DescribeAgents API. DescribeAgents lists agents or the Connector by ID or lists all agents/Connectors associated with your user if you did not specify an ID |  |   | Read | 
|   [DescribeBatchDeleteConfigurationTask](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeBatchDeleteConfigurationTask.html)  | Grants permission to DescribeBatchDeleteConfigurationTask API. DescribeBatchDeleteConfigurationTask returns attributes about a batched deletion task to delete a set of configuration items. The supplied task ID should be the task ID receieved from the output of StartBatchDeleteConfigurationTask |  |   | Read | 
|   [DescribeConfigurations](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeConfigurations.html)  | Grants permission to DescribeConfigurations API. DescribeConfigurations retrieves attributes for a list of configuration item IDs. All of the supplied IDs must be for the same asset type (server, application, process, or connection). Output fields are specific to the asset type selected. For example, the output for a server configuration item includes a list of attributes about the server, such as host name, operating system, and number of network cards |  |   | Read | 
|   [DescribeContinuousExports](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeContinuousExports.html)  | Grants permission to DescribeContinuousExports API. DescribeContinuousExports lists exports as specified by ID. All continuous exports associated with your user can be listed if you call DescribeContinuousExports as is without passing any parameters |  |   | Read | 
|   [DescribeExportConfigurations](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeExportConfigurations.html)  | Grants permission to DescribeExportConfigurations API. DescribeExportConfigurations retrieves the status of a given export process. You can retrieve status from a maximum of 100 processes |  |   | Read | 
|   [DescribeExportTasks](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeExportTasks.html)  | Grants permission to DescribeExportTasks API. DescribeExportTasks retrieve status of one or more export tasks. You can retrieve the status of up to 100 export tasks |  |   | Read | 
|   [DescribeImportTasks](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeImportTasks.html)  | Grants permission to DescribeImportTasks API. DescribeImportTasks returns an array of import tasks for your user, including status information, times, IDs, the Amazon S3 Object URL for the import file, and more |  |   | List | 
|   [DescribeTags](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeTags.html)  | Grants permission to DescribeTags API. DescribeTags retrieves a list of configuration items that are tagged with a specific tag. Or retrieves a list of all tags assigned to a specific configuration item |  |   | Read | 
|   [DisassociateConfigurationItemsFromApplication](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DisassociateConfigurationItemsFromApplication.html)  | Grants permission to DisassociateConfigurationItemsFromApplication API. DisassociateConfigurationItemsFromApplication disassociates one or more configuration items from an application |  |   | Write | 
|   [ExportConfigurations](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_ExportConfigurations.html)  | Grants permission to ExportConfigurations API. ExportConfigurations exports all discovered configuration data to an Amazon S3 bucket or an application that enables you to view and evaluate the data. Data includes tags and tag associations, processes, connections, servers, and system performance |  |   | Write | 
|   [GetDiscoverySummary](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_GetDiscoverySummary.html)  | Grants permission to GetDiscoverySummary API. GetDiscoverySummary retrieves a short summary of discovered assets |  |   | Read | 
|   [GetNetworkConnectionGraph](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_GetNetworkConnectionGraph.html)  | Grants permission to GetNetworkConnectionGraph API. GetNetworkConnectionGraph accepts input list of one of - Ip Addresses, server ids or node ids. Returns a list of nodes and edges which help customer visualize network connection graph. This API is used for visualize network graph functionality in MigrationHub console |  |   | Read | 
|   [ListConfigurations](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_ListConfigurations.html)  | Grants permission to ListConfigurations API. ListConfigurations retrieves a list of configuration items according to criteria you specify in a filter. The filter criteria identify relationship requirements |  |   | List | 
|   [ListServerNeighbors](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_ListServerNeighbors.html)  | Grants permission to ListServerNeighbors API. ListServerNeighbors retrieves a list of servers which are one network hop away from a specified server |  |   | List | 
|   [StartBatchDeleteConfigurationTask](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StartBatchDeleteConfigurationTask.html)  | Grants permission to StartBatchDeleteConfigurationTask API. StartBatchDeleteConfigurationTask starts an asynchronous batch deletion of your configuration items. All of the supplied IDs must be for the same asset type (server, application, process, or connection). Output is a unique task ID you can use to check back on the deletions progress |  |   | Write | 
|   [StartContinuousExport](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StartContinuousExport.html)  | Grants permission to StartContinuousExport API. StartContinuousExport start the continuous flow of agent's discovered data into Amazon Athena |  |   | Write | 
|   [StartDataCollectionByAgentIds](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StartDataCollectionByAgentIds.html)  | Grants permission to StartDataCollectionByAgentIds API. StartDataCollectionByAgentIds instructs the specified agents or Connectors to start collecting data |  |   | Write | 
|   [StartExportTask](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StartExportTask.html)  | Grants permission to StartExportTask API. StartExportTask export the configuration data about discovered configuration items and relationships to an S3 bucket in a specified format |  |   | Write | 
|   [StartImportTask](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StartImportTask.html)  | Grants permission to StartImportTask API. StartImportTask starts an import task. The Migration Hub import feature allows you to import details of your on-premises environment directly into AWS without having to use the Application Discovery Service (ADS) tools such as the Discovery Connector or Discovery Agent. This gives you the option to perform migration assessment and planning directly from your imported data including the ability to group your devices as applications and track their migration status |  |   | Write | 
|   [StopContinuousExport](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StopContinuousExport.html)  | Grants permission to StopContinuousExport API. StopContinuousExport stops the continuous flow of agent's discovered data into Amazon Athena |  |   | Write | 
|   [StopDataCollectionByAgentIds](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StopDataCollectionByAgentIds.html)  | Grants permission to StopDataCollectionByAgentIds API. StopDataCollectionByAgentIds instructs the specified agents or Connectors to stop collecting data |  |   | Write | 
|   [UpdateApplication](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_UpdateApplication.html)  | Grants permission to UpdateApplication API. UpdateApplication updates metadata about an application |  |   | Write | 

## Resource types defined by AWS Application Discovery Service
<a name="list_discovery-resources-for-iam-policies"></a>

AWS Application Discovery Service does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS Application Discovery Service
<a name="list_discovery-policy-keys"></a>

AWS Application Discovery Service defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 