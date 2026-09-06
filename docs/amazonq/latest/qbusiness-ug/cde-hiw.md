

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# How Amazon Q Business document enrichment works
<a name="cde-hiw"></a>

To understand and use document enrichments, familiarize yourself with the key Amazon Q Business concepts that this topic outlines.

**Topics**
+ [Document enrichment concepts](#cde-hiw-concepts)
+ [Document enrichment process overview](#cde-hiw-process)

## Document enrichment concepts
<a name="cde-hiw-concepts"></a>

Amazon Q Business extracts *document attributes* from any document that you ingest into an Amazon Q index. Document attributes or structural metadata can include document title, document type, and time and date created. You can map document attributes to fields in an Amazon Q Business index to better structure your data for retrieval and chat. For more information, see [Document attributes and types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-attributes.html) and [Filtering using document attributes](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/metadata-filtering.html).

**Note**  
Although document attributes and index fields are distinct concepts, in practice they’re used interchangeably because their values overlap and they structurally correspond to each other. That is, document attributes == document metadata == index fields.

## Document enrichment process overview
<a name="cde-hiw-process"></a>

The overall process of document enrichment is as follows:
+ You configure document enrichment when you create or update your Amazon Q Business data source, or add or upload your documents directly into Amazon Q Business index. The exact process for configuration depends on the methods you choose:
  + If you use the API and want to configure document enrichment for a data source connector, you use the [CreateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataSource.html) and [UpdateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateDataSource.html) operations to provide your configuration details.
  + If you use the API and choose to directly upload documents into your index using the [BatchPutDocument](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_BatchPutDocument.html) operation, you must configure document enrichment with each request.
  + If you use the console, can only configure document enrichment for a data source connected to your Amazon Q Business application environment. You select **Document enrichments** under **Enhancements** from the left navigation pane and configure enrichments. You can choose to use both configuration options or either one. You can also choose whether you want to apply your configuration to the original pre-extraction data or to the structured post-extraction data.
+ After you configure and activate your document enrichment configuration, you can use inline configuration or basic logic to alter your data. For more information, see [Using basic operations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cde-basic-operations.html).
+ If you chose to configure advanced data manipulation by using a Lambda function, Amazon Q Business applies the configured function (depending on what you’ve chosen) to either your original pre-extraction data or your structured post-extraction data. For more information, see [Using Lambda functions](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cde-lambda-operations.html).
+ Finally, your altered and enriched documents are ingested into your Amazon Q Business index.

If a configuration isn't valid during any point in this process, Amazon Q returns an error.