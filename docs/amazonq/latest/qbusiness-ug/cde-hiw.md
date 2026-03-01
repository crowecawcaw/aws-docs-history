# How Amazon Q Business document enrichment works

To understand and use document enrichments, familiarize yourself with the key
Amazon Q Business concepts that this topic outlines.

###### Topics

- [Document enrichment concepts](#cde-hiw-concepts "#cde-hiw-concepts")
- [Document enrichment process overview](#cde-hiw-process "#cde-hiw-process")

## Document enrichment concepts

Amazon Q Business extracts _document
attributes_ from any document that you ingest into an Amazon Q index. Document attributes or structural metadata can include
document title, document type, and time and date created. You can map document
attributes to fields in an Amazon Q Business index to better structure
your data for retrieval and chat. For more information, see [Document attributes and types](doc-attributes.md "doc-attributes.md") and [Filtering using document attributes](metadata-filtering.md "metadata-filtering.md").

###### Note

Although document attributes and index fields are distinct concepts, in
practice they’re used interchangeably because their values overlap and they
structurally correspond to each other. That is, document attributes ==
document metadata == index fields.

## Document enrichment process overview

The overall process of document enrichment is as follows:

- You configure document enrichment when you create or update your
  Amazon Q Business data source, or add or upload your documents
  directly into Amazon Q Business index. The exact process for
  configuration depends on the methods you choose:
  - If you use the API and want to configure document enrichment
    for a data source connector, you use the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md")
    and [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md")
    operations to provide your configuration details.
  - If you use the API and choose to directly upload documents
    into your index using the [BatchPutDocument](../api-reference/API_BatchPutDocument.md "../api-reference/API_BatchPutDocument.md") operation, you
    must configure document enrichment with each request.
  - If you use the console, can only configure document enrichment
    for a data source connected to your Amazon Q Business
    application environment. You select **Document
    enrichments** under
    **Enhancements** from the left navigation
    pane and configure enrichments. You can choose to use both
    configuration options or either one. You can also choose whether
    you want to apply your configuration to the original
    pre-extraction data or to the structured post-extraction
    data.

- After you configure and activate your document enrichment
  configuration, you can use inline configuration or basic logic to alter
  your data. For more information, see [Using basic operations](cde-basic-operations.md "cde-basic-operations.md").
- If you chose to configure advanced data manipulation by using a
  Lambda function, Amazon Q Business applies the
  configured function (depending on what you’ve chosen) to either your
  original pre-extraction data or your structured post-extraction data.
  For more information, see [Using Lambda
  functions](cde-lambda-operations.md "cde-lambda-operations.md").
- Finally, your altered and enriched documents are ingested into your
  Amazon Q Business index.

If a configuration isn't valid during any point in this process, Amazon Q returns an error.
