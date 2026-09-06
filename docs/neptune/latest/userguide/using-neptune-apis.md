

# Introduction to using Amazon Neptune APIs
<a name="using-neptune-apis"></a>

The Amazon Neptune management APIs provide SDK support for creating, managing and deleting Neptune DB clusters and instances, while the Neptune data APIs provide SDK support for loading data into your graph, running queries, getting information about the data in your graph, and running machine-learning operations. These APIs are available in all SDK languages. By automatically signing API requests, they greatly simply integrating Neptune into applications.

This page provides information about how to use these APIs.

## IAM Actions with different names than their Neptune data API SDK counterparts
<a name="neptune-apis-shared-iam-actions"></a>

When you're calling a Neptune API methods on a cluster that has IAM authentication enabled, you have to have an IAM policy attached to the user or role making the calls that provides permissions for the actions you want to make. You set those permissions in the policy using corresponding [IAM Actions](iam-dp-actions.md). You can also restrict the actions that can be taken using [IAM Condition keys](iam-data-condition-keys.md).

Most IAM actions have the same name as the API methods that they correspond to, but some methods in the data API have different names, because some are shared by more than one method. The table below lists data methods and their corresponding IAM actions:


| Data API operation name | IAM correspondences | 
| --- | --- | 
| [CancelGremlinQuery](https://docs.aws.amazon.com/neptune/latest/data-api/API_CancelGremlinQuery.html) (cancel\_gremlin\_query) | *Action:* `neptune-db:CancelQuery` | 
| [CancelLoaderJob](https://docs.aws.amazon.com/neptune/latest/data-api/API_CancelLoaderJob.html) (cancel\_loader\_job) | *Action:* `neptune-db:CancelLoaderJob` | 
| [CancelMLDataProcessingJob](https://docs.aws.amazon.com/neptune/latest/data-api/API_CancelMLDataProcessingJob.html) (cancel\_ml\_data\_processing\_job) | *Action:* `neptune-db:CancelMLDataProcessingJob` | 
| [CancelMLModelTrainingJob](https://docs.aws.amazon.com/neptune/latest/data-api/API_CancelMLModelTrainingJob.html) (cancel\_ml\_model\_training\_job) | *Action:* `neptune-db:CancelMLModelTrainingJob` | 
| [CancelOpenCypherQuery](https://docs.aws.amazon.com/neptune/latest/data-api/API_CancelOpenCypherQuery.html) (cancel\_open\_cypher\_query) | *Action:* `neptune-db:CancelQuery` | 
| [CreateMLEndpoint](https://docs.aws.amazon.com/neptune/latest/data-api/API_CreateMLEndpoint.html) (create\_ml\_endpoint) | *Action:* `neptune-db:CreateMLEndpoint` | 
| [DeleteMLEndpoint](https://docs.aws.amazon.com/neptune/latest/data-api/API_DeleteMLEndpoint.html) (delete\_ml\_endpoint) | *Action:* `neptune-db:DeleteMLEndpoint` | 
| [DeletePropertygraphStatistics](https://docs.aws.amazon.com/neptune/latest/data-api/API_DeletePropertygraphStatistics) (delete\_propertygraph\_statistics) | *Action:* `neptune-db:DeleteStatistics` | 
| [DeleteSparqlStatistics](https://docs.aws.amazon.com/neptune/latest/data-api/API_DeleteSparqlStatistics) (delete\_sparql\_statistics) | *Action:* `neptune-db:DeleteStatistics` | 
| [ExecuteFastReset](https://docs.aws.amazon.com/neptune/latest/data-api/API_ExecuteFastReset) execute\_fast\_reset() | *Action:* `neptune-db:ResetDatabase` | 
| [ExecuteGremlinExplainQuery](https://docs.aws.amazon.com/neptune/latest/data-api/API_ExecuteGremlinExplainQuery) (execute\_gremlin\_explain\_query) | *Actions:*+ `neptune-db:ReadDataViaQuery`<br />+ `neptune-db:WriteDataViaQuery`<br />+ `neptune-db:DeleteDataViaQuery`<br />*Condition key:* `neptune-db:QueryLanguage:Gremlin` | 
| [ExecuteGremlinProfileQuery](https://docs.aws.amazon.com/neptune/latest/data-api/API_ExecuteGremlinProfileQuery) (execute\_gremlin\_profile\_query) | *Action:* `neptune-db:ReadDataViaQuery`<br />*Condition key:* `neptune-db:QueryLanguage:Gremlin` | 
| [ExecuteGremlinQuery](https://docs.aws.amazon.com/neptune/latest/data-api/API_ExecuteGremlinQuery) (execute\_gremlin\_query) | *Actions:*+ `neptune-db:ReadDataViaQuery`<br />+ `neptune-db:WriteDataViaQuery`<br />+ `neptune-db:DeleteDataViaQuery`<br />*Condition key:* `neptune-db:QueryLanguage:Gremlin` | 
| [ExecuteOpenCypherExplainQuery](https://docs.aws.amazon.com/neptune/latest/data-api/API_ExecuteOpenCypherExplainQuery) (execute\_open\_cypher\_explain\_query) | *Action:* `neptune-db:ReadDataViaQuery`<br />*Condition key:* `neptune-db:QueryLanguage:OpenCypher` | 
| [ExecuteOpenCypherQuery](https://docs.aws.amazon.com/neptune/latest/data-api/API_ExecuteOpenCypherQuery) (execute\_open\_cypher\_query) | *Actions:*+ `neptune-db:ReadDataViaQuery`<br />+ `neptune-db:WriteDataViaQuery`<br />+ `neptune-db:DeleteDataViaQuery`<br />*Condition key:* `neptune-db:QueryLanguage:OpenCypher` | 
| [GetEngineStatus](https://docs.aws.amazon.com/neptune/latest/data-api/API_GetEngineStatus.html) (get\_engine\_status) | *Action:* `neptune-db:GetEngineStatus` | 
| [GetGremlinQueryStatus](https://docs.aws.amazon.com/neptune/latest/data-api/API_GetGremlinQueryStatus) (get\_gremlin\_query\_status) | *Action:* `neptune-db::GetQueryStatus`<br />*Condition key:* `neptune-db:QueryLanguage:Gremlin` | 
| [GetLoaderJobStatus](https://docs.aws.amazon.com/neptune/latest/data-api/API_GetLoaderJobStatus.html) (get\_loader\_job\_status) | *Action:* `neptune-db:GetLoaderJobStatus` | 
| [GetMLDataProcessingJob](https://docs.aws.amazon.com/neptune/latest/data-api/API_GetMLDataProcessingJob) (get\_ml\_data\_processing\_job) | *Action:* `neptune-db:GetMLDataProcessingJobStatus` | 
| [GetMLEndpoint](https://docs.aws.amazon.com/neptune/latest/data-api/API_GetMLEndpoint) (get\_ml\_endpoint) | *Action:* `neptune-db:GetMLEndpointStatus` | 
| [GetMLModelTrainingJob](https://docs.aws.amazon.com/neptune/latest/data-api/API_GetMLModelTrainingJob) (get\_ml\_model\_training\_job) | *Action:* `neptune-db:GetMLModelTrainingJobStatus` | 
| [GetMLModelTransformJob](https://docs.aws.amazon.com/neptune/latest/data-api/API_GetMLModelTransformJob) (get\_ml\_model\_transform\_job) | *Action:* `neptune-db:GetMLModelTransformJobStatus` | 
| [GetOpenCypherQueryStatus](https://docs.aws.amazon.com/neptune/latest/data-api/API_GetOpenCypherQueryStatus) (get\_open\_cypher\_query\_status) | *Action:* `neptune-db::GetQueryStatus`<br />*Condition key:* `neptune-db:QueryLanguage:OpenCypher` | 
| [GetPropertygraphStatistics](https://docs.aws.amazon.com/neptune/latest/data-api/API_GetPropertygraphStatistics) (get\_propertygraph\_statistics) | *Action:* `neptune-db:GetStatisticsStatus` | `` | 
| [GetPropertygraphStream](https://docs.aws.amazon.com/neptune/latest/data-api/API_GetPropertygraphStream) (get\_propertygraph\_stream) | *Action:* `neptune-db:GetStreamRecords`<br />*Condition keys:*+ `neptune-db:QueryLanguage:Gremlin`<br />+ `neptune-db:QueryLanguage:OpenCypher` | 
| [GetPropertygraphSummary](https://docs.aws.amazon.com/neptune/latest/data-api/API_GetPropertygraphSummary) (get\_propertygraph\_summary) | *Action:* `neptune-db:GetGraphSummary` | 
| [GetRDFGraphSummary](https://docs.aws.amazon.com/neptune/latest/data-api/API_GetRDFGraphSummary) (get\_rdf\_graph\_summary) | *Action:* `neptune-db:GetGraphSummary` | 
| [GetSparqlStatistics](https://docs.aws.amazon.com/neptune/latest/data-api/API_GetSparqlStatistics) (get\_sparql\_statistics) | *Action:* `neptune-db:GetStatisticsStatus` | 
| [GetSparqlStream](https://docs.aws.amazon.com/neptune/latest/data-api/API_GetSparqlStream) (get\_sparql\_stream) | *Action:* `neptune-db::GetStreamRecords`<br />*Condition key:* `neptune-db:QueryLanguage:Sparql` | 
| [ListGremlinQueries](https://docs.aws.amazon.com/neptune/latest/data-api/API_ListGremlinQueries) (list\_gremlin\_queries) | *Action:* `neptune-db::GetQueryStatus`<br />*Condition key:* `neptune-db:QueryLanguage:Gremlin` | 
| [ListMLEndpoints](https://docs.aws.amazon.com/neptune/latest/data-api/API_ListMLEndpoints.html) (list\_ml\_endpoints) | *Action:* `neptune-db:ListMLEndpoints` | `` | 
| [ListMLModelTrainingJobs](https://docs.aws.amazon.com/neptune/latest/data-api/API_ListMLModelTrainingJobs.html) (list\_ml\_model\_training\_jobs) | *Action:* `neptune-db:ListMLModelTrainingJobs` | 
| [ListMLModelTransformJobs](https://docs.aws.amazon.com/neptune/latest/data-api/API_ListMLModelTransformJobs.html) (list\_ml\_model\_transform\_jobs) | *Action:* `neptune-db:ListMLModelTransformJobs` | 
| [ListOpenCypherQueries](https://docs.aws.amazon.com/neptune/latest/data-api/API_ListOpenCypherQueries) (list\_open\_cypher\_queries) | *Action:* `neptune-db::GetQueryStatus`<br />*Condition key:* `neptune-db:QueryLanguage:OpenCypher` | 
| [ManagePropertygraphStatistics](https://docs.aws.amazon.com/neptune/latest/data-api/API_ManagePropertygraphStatistics) (manage\_propertygraph\_statistics) | *Action:* `neptune-db:ManageStatistics` | 
| [ManageSparqlStatistics](https://docs.aws.amazon.com/neptune/latest/data-api/API_ManageSparqlStatistics) (manage\_sparql\_statistics) | *Action:* `neptune-db:ManageStatistics` | 
| [StartLoaderJob](https://docs.aws.amazon.com/neptune/latest/data-api/API_StartLoaderJob.html) (start\_loader\_job) | *Action:* `neptune-db:StartLoaderJob` | 
| [StartMLModelDataProcessingJob](https://docs.aws.amazon.com/neptune/latest/data-api/API_StartMLModelDataProcessingJob.html) (start\_ml\_data\_processing\_job) | *Action:* `neptune-db:StartMLModelDataProcessingJob` | 
| [StartMLModelTrainingJob](https://docs.aws.amazon.com/neptune/latest/data-api/API_StartMLModelTrainingJob.html) (start\_ml\_model\_training\_job) | *Action:* `neptune-db:StartMLModelTrainingJob` | 
| [StartMLModelTransformJob](https://docs.aws.amazon.com/neptune/latest/data-api/API_StartMLModelTransformJob.html) (start\_ml\_model\_transform\_job) | *Action:* `neptune-db:StartMLModelTransformJob` | 