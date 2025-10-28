# View data source information for your Amazon Bedrock knowledge base

You can view information about a data source for your knowledge base, such as the settings and sync history.

To monitor your knowledge base, including any data sources for your knowledge base, see [Knowledge base logging using Amazon CloudWatch](knowledge-bases-logging.md "knowledge-bases-logging.md").

Choose the tab for your preferred method, and then follow the steps:

Console

###### To view information about a data source

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. In the left navigation pane, choose **Knowledge bases**.
3. In the **Data source** section, select the data source for which you want to view details.
4. The **Data source overview** contains details about the data source.
5. The **Sync history** contains details about when the data source was synced. To see reasons for why a sync event failed, select a sync event and choose **View warnings**.

API
To get information about a data source, send a [GetDataSource](../APIReference/API_agent_GetDataSource.md "../APIReference/API_agent_GetDataSource.md") request with a [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt") and specify the `dataSourceId` and the `knowledgeBaseId` of the knowledge base that it belongs to.

To list information about a knowledge base's data sources, send a [ListDataSources](../APIReference/API_agent_ListDataSources.md "../APIReference/API_agent_ListDataSources.md") request with a [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt") and specify the ID of the knowledge base.

- To set the maximum number of results to return in a response, use the `maxResults` field.
- If there are more results than the number you set, the response returns a `nextToken`. You can use this value in another `ListDataSources` request to see the next batch of results.

To get information a sync event for a data source, send a [GetIngestionJob](../APIReference/API_agent_GetIngestionJob.md "../APIReference/API_agent_GetIngestionJob.md") request with a [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"). Specify the `dataSourceId`, `knowledgeBaseId`, and `ingestionJobId`.

To list the sync history for a data source in a knowledge base, send a [ListIngestionJobs](../APIReference/API_agent_ListIngestionJobs.md "../APIReference/API_agent_ListIngestionJobs.md") request with a [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"). Specify the ID of the knowledge base and data source. You can set the following specifications.

- Filter for results by specifying a status to search for in the `filters` object.
- Sort by the time that the job was started or the status of a job by specifying the `sortBy` object. You can sort in ascending or descending order.
- Set the maximum number of results to return in a response in the `maxResults` field. If there are more results than the number you set, the response returns a `nextToken` that you can send in another [ListIngestionJobs](../APIReference/API_agent_ListIngestionJobs.md "../APIReference/API_agent_ListIngestionJobs.md") request to see the next batch of jobs.
