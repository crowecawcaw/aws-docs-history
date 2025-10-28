# View information about documents in your data source

The following topics describe how to view documents in your data source. If your knowledge base is connected to an Amazon S3 data source, you can view the documents in the connected S3 bucket.

###### Note

If you created a new knowledge base by connecting to an S3 data source, you must sync the data source first before you can use these API operations on the data source.

Expand the method that corresponds to your use case:

To view documents in your data source that have been ingested in the AWS Management Console, do the following:

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. In the left navigation pane, choose **Knowledge bases**.
3. In the **Knowledge bases** section, select the knowledge base whose documents you want to view.
4. In the **Data source** section, select the data source whose documents you want to view.
5. The **Documents** section lists the documents in the data source. These documents have also been ingested into the knowledge base.
   With the Amazon Bedrock API, you can view a subset or all of the documents in your data source that have been ingested into the knowledge base. Select the topic that pertains to your use case.

###### Topics

- [View information about a subset of documents in your knowledge base](#kb-direct-ingestion-get "#kb-direct-ingestion-get")
- [View information about all documents in your knowledge base](#kb-direct-ingestion-list "#kb-direct-ingestion-list")

### View information about a subset of documents in your knowledge base

To view information about specific documents in your data source, send a [GetKnowledgeBaseDocuments](../APIReference/API_agent_GetKnowledgeBaseDocuments.md "../APIReference/API_agent_GetKnowledgeBaseDocuments.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt") and specify the IDs of the data source and the knowledge base it's connected to.

For each document that you want to get information for, add a [DocumentIdentifier](../APIReference/API_agent_DocumentIdentifier.md "../APIReference/API_agent_DocumentIdentifier.md") item in the `documentIdentifiers` array in one of the following formats:

- If the data source is a custom one, specify the ID of the document in the `id` field:

```
{
    "custom": {
        "id": "string"
    },
    "dataSourceType": "CUSTOM"
}
```

- If the data source is an Amazon S3 one, specify the S3 URI of the document in the `uri` field:

```
{
    "dataSourceType": "S3",
    "s3": {
        "uri": "string"
    }
}
```

The response returns an array of items, each of which contains information about a document that you requested.

### View information about all documents in your knowledge base

To view information about all documents in a data source, send a [ListKnowledgeBaseDocuments](../APIReference/API_agent_ListKnowledgeBaseDocuments.md "../APIReference/API_agent_ListKnowledgeBaseDocuments.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt") and specify the IDs of tthe data source and the knowledge base it's connected to. You also have the following options:

- Specify the `maxResults` to limit the number of results to return.
- If the results don't fit into a response, a value is returned in the
  `nextToken` field of the response. You can use this value in
  the `nextToken` field of a subsequent request to get the next
  batch of results.
