

# Actions, resources, and condition keys for Amazon Neptune Analytics
<a name="list_neptune-graph"></a>

Amazon Neptune Analytics (service prefix: `neptune-graph`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/security.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/neptune-graph/neptune-graph.json) for this service.

**Topics**
+ [API operations defined by Amazon Neptune Analytics](#list_neptune-graph-operations)
+ [Actions defined by Amazon Neptune Analytics](#list_neptune-graph-actions-as-permissions)
+ [Resource types defined by Amazon Neptune Analytics](#list_neptune-graph-resources-for-iam-policies)
+ [Condition keys for Amazon Neptune Analytics](#list_neptune-graph-policy-keys)

## API operations defined by Amazon Neptune Analytics
<a name="list_neptune-graph-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_neptune-graph-actions-as-permissions).




- **   CancelExportTask  **
  - **IAM action:**  [neptune-graph:CancelExportTask](#list_neptune-graph-action-CancelExportTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelImportTask  **
  - **IAM action:**  [neptune-graph:CancelImportTask](#list_neptune-graph-action-CancelImportTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateGraph  **
  - **IAM action:**  [neptune-graph:CreateGraph](#list_neptune-graph-action-CreateGraph)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [neptune-graph:TagResource](#list_neptune-graph-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateGraphSnapshot  **
  - **IAM action:**  [neptune-graph:CreateGraphSnapshot](#list_neptune-graph-action-CreateGraphSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [neptune-graph:TagResource](#list_neptune-graph-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateGraphUsingImportTask  **
  - **IAM action:**  [neptune-graph:CreateGraphUsingImportTask](#list_neptune-graph-action-CreateGraphUsingImportTask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [neptune-graph:TagResource](#list_neptune-graph-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** neptune-graph.amazonaws.com / **Access level:** Write

- **   CreatePrivateGraphEndpoint  **
  - **IAM action:**  [neptune-graph:CreatePrivateGraphEndpoint](#list_neptune-graph-action-CreatePrivateGraphEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGraph  **
  - **IAM action:**  [neptune-graph:DeleteGraph](#list_neptune-graph-action-DeleteGraph) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGraphSnapshot  **
  - **IAM action:**  [neptune-graph:DeleteGraphSnapshot](#list_neptune-graph-action-DeleteGraphSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePrivateGraphEndpoint  **
  - **IAM action:**  [neptune-graph:DeletePrivateGraphEndpoint](#list_neptune-graph-action-DeletePrivateGraphEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetExportTask  **
  - **IAM action:**  [neptune-graph:GetExportTask](#list_neptune-graph-action-GetExportTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGraph  **
  - **IAM action:**  [neptune-graph:GetGraph](#list_neptune-graph-action-GetGraph) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGraphSnapshot  **
  - **IAM action:**  [neptune-graph:GetGraphSnapshot](#list_neptune-graph-action-GetGraphSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetImportTask  **
  - **IAM action:**  [neptune-graph:GetImportTask](#list_neptune-graph-action-GetImportTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPrivateGraphEndpoint  **
  - **IAM action:**  [neptune-graph:GetPrivateGraphEndpoint](#list_neptune-graph-action-GetPrivateGraphEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListExportTasks  **
  - **IAM action:**  [neptune-graph:ListExportTasks](#list_neptune-graph-action-ListExportTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListGraphSnapshots  **
  - **IAM action:**  [neptune-graph:ListGraphSnapshots](#list_neptune-graph-action-ListGraphSnapshots) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListGraphs  **
  - **IAM action:**  [neptune-graph:ListGraphs](#list_neptune-graph-action-ListGraphs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListImportTasks  **
  - **IAM action:**  [neptune-graph:ListImportTasks](#list_neptune-graph-action-ListImportTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListPrivateGraphEndpoints  **
  - **IAM action:**  [neptune-graph:ListPrivateGraphEndpoints](#list_neptune-graph-action-ListPrivateGraphEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [neptune-graph:ListTagsForResource](#list_neptune-graph-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ResetGraph  **
  - **IAM action:**  [neptune-graph:ResetGraph](#list_neptune-graph-action-ResetGraph) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RestoreGraphFromSnapshot  **
  - **IAM action:**  [neptune-graph:RestoreGraphFromSnapshot](#list_neptune-graph-action-RestoreGraphFromSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [neptune-graph:TagResource](#list_neptune-graph-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   StartExportTask  **
  - **IAM action:**  [neptune-graph:StartExportTask](#list_neptune-graph-action-StartExportTask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [neptune-graph:TagResource](#list_neptune-graph-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** neptune-graph.amazonaws.com / **Access level:** Write

- **   StartGraph  **
  - **IAM action:**  [neptune-graph:StartGraph](#list_neptune-graph-action-StartGraph) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartImportTask  **
  - **IAM action:**  [neptune-graph:StartImportTask](#list_neptune-graph-action-StartImportTask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** neptune-graph.amazonaws.com / **Access level:** Write

- **   StopGraph  **
  - **IAM action:**  [neptune-graph:StopGraph](#list_neptune-graph-action-StopGraph) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [neptune-graph:TagResource](#list_neptune-graph-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [neptune-graph:UntagResource](#list_neptune-graph-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateGraph  **
  - **IAM action:**  [neptune-graph:UpdateGraph](#list_neptune-graph-action-UpdateGraph) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Neptune Analytics
<a name="list_neptune-graph-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CancelExportTask](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_CancelExportTask.html)  **
  - **Description:** Grants permission to cancel an ongoing export task
  - **Resource types (\*required):** [export-task\*](#list_neptune-graph-resource-export-task)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelImportTask](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_CancelImportTask.html)  **
  - **Description:** Grants permission to cancel an ongoing import task
  - **Resource types (\*required):** [import-task\*](#list_neptune-graph-resource-import-task)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CancelQuery](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_CancelQuery.html)  **
  - **Description:** Grants permission to cancel a query
  - **Resource types (\*required):** [graph\*](#list_neptune-graph-resource-graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateGraph](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_CreateGraph.html)  **
  - **Description:** Grants permission to create a new graph
  - **Resource types (\*required):** [graph\*](#list_neptune-graph-resource-graph)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_neptune-graph-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_neptune-graph-aws_TagKeys)<br />[neptune-graph:PublicConnectivity](#list_neptune-graph-neptune-graph_PublicConnectivity)
  - **Access level:** Write

- **   [CreateGraphSnapshot](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_CreateGraphSnapshot.html)  **
  - **Description:** Grants permission to create a new snapshot from an existing graph
  - **Resource types (\*required):** [graph\*](#list_neptune-graph-resource-graph) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_neptune-graph-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_neptune-graph-aws_TagKeys)
  - **Resource types (\*required):** [graph-snapshot\*](#list_neptune-graph-resource-graph-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_neptune-graph-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_neptune-graph-aws_TagKeys)
  - **Access level:** Write

- **   [CreateGraphUsingImportTask](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_CreateGraphUsingImportTask.html)  **
  - **Description:** Grants permission to create a new graph while importing data into the new graph
  - **Resource types (\*required):** [graph\*](#list_neptune-graph-resource-graph) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_neptune-graph-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_neptune-graph-aws_TagKeys)<br />[neptune-graph:PublicConnectivity](#list_neptune-graph-neptune-graph_PublicConnectivity)
  - **Resource types (\*required):** [import-task\*](#list_neptune-graph-resource-import-task) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_neptune-graph-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_neptune-graph-aws_TagKeys)<br />[neptune-graph:PublicConnectivity](#list_neptune-graph-neptune-graph_PublicConnectivity)
  - **Access level:** Write

- **   [CreatePrivateGraphEndpoint](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_CreatePrivateGraphEndpoint.html)  **
  - **Description:** Grants permission to create a new private graph endpoint to access the graph from within a vpc
  - **Resource types (\*required):** [graph\*](#list_neptune-graph-resource-graph)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_neptune-graph-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_neptune-graph-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteDataViaQuery](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ExecuteQuery.html)  **
  - **Description:** Grants permission to delete data via query APIs on the graph
  - **Resource types (\*required):** [graph\*](#list_neptune-graph-resource-graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteGraph](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_DeleteGraph.html)  **
  - **Description:** Grants permission to delete a graph
  - **Resource types (\*required):** [graph\*](#list_neptune-graph-resource-graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteGraphSnapshot](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_DeleteGraphSnapshot.html)  **
  - **Description:** Grants permission to delete a snapshot
  - **Resource types (\*required):** [graph-snapshot\*](#list_neptune-graph-resource-graph-snapshot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePrivateGraphEndpoint](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_DeletePrivateGraphEndpoint.html)  **
  - **Description:** Grants permission to delete a private graph endpoint of a graph
  - **Resource types (\*required):** [graph\*](#list_neptune-graph-resource-graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetEngineStatus](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/#GetEngineStatus)  **
  - **Description:** Grants permission to get the engine status of the graph
  - **Resource types (\*required):** [graph\*](#list_neptune-graph-resource-graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetExportTask](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_GetExportTask.html)  **
  - **Description:** Grants permission to get details about an export task
  - **Resource types (\*required):** [export-task\*](#list_neptune-graph-resource-export-task)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetGraph](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_GetGraph.html)  **
  - **Description:** Grants permission to get details about a graph
  - **Resource types (\*required):** [graph\*](#list_neptune-graph-resource-graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetGraphSnapshot](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_GetGraphSnapshot.html)  **
  - **Description:** Grants permission to get details about a snapshot
  - **Resource types (\*required):** [graph-snapshot\*](#list_neptune-graph-resource-graph-snapshot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetGraphSummary](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_GetGraphSummary.html)  **
  - **Description:** Grants permission to get the summary for the data in the graph
  - **Resource types (\*required):** [graph\*](#list_neptune-graph-resource-graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetImportTask](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_GetImportTask.html)  **
  - **Description:** Grants permission to get details about an import task
  - **Resource types (\*required):** [import-task\*](#list_neptune-graph-resource-import-task)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetPrivateGraphEndpoint](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_GetPrivateGraphEndpoint.html)  **
  - **Description:** Grants permission to get details about a private graph endpoint of a graph
  - **Resource types (\*required):** [graph\*](#list_neptune-graph-resource-graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetQueryStatus](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_GetQuery.html)  **
  - **Description:** Grants permission to check the status of a given query
  - **Resource types (\*required):** [graph\*](#list_neptune-graph-resource-graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetStatisticsStatus](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/#GetStatisticsStatus)  **
  - **Description:** Grants permission to get the statistics for the data in the graph
  - **Resource types (\*required):** [graph\*](#list_neptune-graph-resource-graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListExportTasks](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ListExportTasks.html)  **
  - **Description:** Grants permission to list the export tasks in your account
  - **Resource types (\*required):** [export-task\*](#list_neptune-graph-resource-export-task)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListGraphSnapshots](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ListGraphSnapshots.html)  **
  - **Description:** Grants permission to list the snapshots in your account
  - **Resource types (\*required):** [graph-snapshot\*](#list_neptune-graph-resource-graph-snapshot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListGraphs](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ListGraphs.html)  **
  - **Description:** Grants permission to list the graphs in your account
  - **Resource types (\*required):** [graph\*](#list_neptune-graph-resource-graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListImportTasks](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ListImportTasks.html)  **
  - **Description:** Grants permission to list the import tasks in your account
  - **Resource types (\*required):** [import-task\*](#list_neptune-graph-resource-import-task)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListPrivateGraphEndpoints](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ListPrivateGraphEndpoints.html)  **
  - **Description:** Grants permission to list the private graph endpoints for a given graph
  - **Resource types (\*required):** [graph\*](#list_neptune-graph-resource-graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListQueries](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ListQueries.html)  **
  - **Description:** Grants permission to check the status of all active queries
  - **Resource types (\*required):** [graph\*](#list_neptune-graph-resource-graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to lists tag for a Neptune Analytics resource
  - **Resource types (\*required):** [graph](#list_neptune-graph-resource-graph) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [graph-snapshot](#list_neptune-graph-resource-graph-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ReadDataViaQuery](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ExecuteQuery.html)  **
  - **Description:** Grants permission to read data via query APIs on the graph
  - **Resource types (\*required):** [graph\*](#list_neptune-graph-resource-graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ResetGraph](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ResetGraph.html)  **
  - **Description:** Grants permission to reset a graph which deletes all data within the graph
  - **Resource types (\*required):** [graph\*](#list_neptune-graph-resource-graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RestoreGraphFromSnapshot](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_RestoreGraphFromSnapshot.html)  **
  - **Description:** Grants permission to create a new graph from an existing snapshot
  - **Resource types (\*required):** [graph\*](#list_neptune-graph-resource-graph) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_neptune-graph-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_neptune-graph-aws_TagKeys)<br />[neptune-graph:PublicConnectivity](#list_neptune-graph-neptune-graph_PublicConnectivity)
  - **Resource types (\*required):** [graph-snapshot\*](#list_neptune-graph-resource-graph-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_neptune-graph-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_neptune-graph-aws_TagKeys)<br />[neptune-graph:PublicConnectivity](#list_neptune-graph-neptune-graph_PublicConnectivity)
  - **Access level:** Write

- **   [StartExportTask](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_StartExportTask.html)  **
  - **Description:** Grants permission to export data from an existing graph
  - **Resource types (\*required):** [export-task\*](#list_neptune-graph-resource-export-task) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_neptune-graph-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_neptune-graph-aws_TagKeys)
  - **Resource types (\*required):** [graph\*](#list_neptune-graph-resource-graph) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_neptune-graph-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_neptune-graph-aws_TagKeys)
  - **Access level:** Write

- **   [StartGraph](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_StartGraph.html)  **
  - **Description:** Grants permission to start a graph
  - **Resource types (\*required):** [graph\*](#list_neptune-graph-resource-graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartImportTask](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_StartImportTask.html)  **
  - **Description:** Grants permission to import data into an existing graph
  - **Resource types (\*required):** [graph\*](#list_neptune-graph-resource-graph) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [import-task\*](#list_neptune-graph-resource-import-task) / **Condition keys:**  
  - **Access level:** Write

- **   [StopGraph](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_StopGraph.html)  **
  - **Description:** Grants permission to stop a graph
  - **Resource types (\*required):** [graph\*](#list_neptune-graph-resource-graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_TagResource.html)  **
  - **Description:** Grants permission to tag a Neptune Analytics resource
  - **Resource types (\*required):** [graph](#list_neptune-graph-resource-graph) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_neptune-graph-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_neptune-graph-aws_TagKeys)
  - **Resource types (\*required):** [graph-snapshot](#list_neptune-graph-resource-graph-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_neptune-graph-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_neptune-graph-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a Neptune Analytics resource
  - **Resource types (\*required):** [graph](#list_neptune-graph-resource-graph) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_neptune-graph-aws_TagKeys)
  - **Resource types (\*required):** [graph-snapshot](#list_neptune-graph-resource-graph-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_neptune-graph-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateGraph](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_UpdateGraph.html)  **
  - **Description:** Grants permission to modify a graph
  - **Resource types (\*required):** [graph\*](#list_neptune-graph-resource-graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)<br />[neptune-graph:PublicConnectivity](#list_neptune-graph-neptune-graph_PublicConnectivity)
  - **Access level:** Write

- **   [WriteDataViaQuery](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ExecuteQuery.html)  **
  - **Description:** Grants permission to write data via query APIs on the graph
  - **Resource types (\*required):** [graph\*](#list_neptune-graph-resource-graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Neptune Analytics
<a name="list_neptune-graph-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [export-task](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/iam-resources.html#export-task)  | arn:${Partition}:neptune-graph:${Region}:${Account}:export-task/${ResourceId} |   | 
|  [graph](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/iam-resources.html#graph)  | arn:${Partition}:neptune-graph:${Region}:${Account}:graph/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_) | 
|  [graph-snapshot](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/iam-resources.html#graph-snapshot)  | arn:${Partition}:neptune-graph:${Region}:${Account}:graph-snapshot/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_neptune-graph-aws_ResourceTag___TagKey_) | 
|  [import-task](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/iam-resources.html#import-task)  | arn:${Partition}:neptune-graph:${Region}:${Account}:import-task/${ResourceId} |   | 

## Condition keys for Amazon Neptune Analytics
<a name="list_neptune-graph-policy-keys"></a>

Amazon Neptune Analytics defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag's key and value in a request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys in a request | ArrayOfString | 
|   [neptune-graph:PublicConnectivity](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/iam-condition-keys.html#publicconnectivity)  | Filters access by the value of the public connectivity parameter provided in the request or its default value, if unspecified. All access to graphs is IAM authenticated | Bool | 