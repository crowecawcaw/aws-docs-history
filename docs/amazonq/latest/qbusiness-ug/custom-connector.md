# Connecting Amazon Q custom connector to Amazon Q Business

Use a custom data source when you have a repository that Amazon Q Business doesn’t
yet provide a data source connector for. When you create a custom data source, you have
complete control over how the documents to index are selected. Amazon Q only
provides metric information that you can use to monitor your data source sync jobs. You must
create and run the crawler that determines the documents your data source indexes.

**You can use a custom data source connector to:**

- See the same run history metrics that Amazon Q data sources provide
  even when you can't use Amazon Q data sources to sync your
  repositories.
- Create a consistent sync monitoring experience between Amazon Q data
  sources and custom data sources.
- See sync metrics for a data source connector that you created using the [BatchPutDocument](../api-reference/API_BatchPutDocument.md "../api-reference/API_BatchPutDocument.md") and [BatchDeleteDocument](../api-reference/API_BatchDeleteDocument.md "../api-reference/API_BatchDeleteDocument.md") API operations.
  You can create an Amazon Q custom data source connector using either the
  AWS Management Console or the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md").

**When you create a custom data source using the
`CreateDataSource` API operation:**

- The action returns an ID to use when you synchronize the data source.
- You only need to provide a `Name` and optionally a `Description`.
- Set the `Configuration` parameter as follows:

```
"configuration": {
"type": "CUSTOM",
"version": "1.0.0"
}
```

- When indexing documents later, you must specify the main title of your documents using the [Document](../api-reference/API_Document.md "../api-reference/API_Document.md") object, and `_source_uri` in [DocumentAttribute](../api-reference/API_DocumentAttribute.md "../api-reference/API_DocumentAttribute.md"). The main title is
  required so that `DocumentTitle` and `DocumentURI` are
  included in the [ChatSync](../api-reference/API_ChatSync.md "../api-reference/API_ChatSync.md") or [Chat](../api-reference/API_Chat.md "../api-reference/API_Chat.md") response.
  **When you create a custom data source using the
  console:**

- The console returns an ID to use when you synchronize the data source.
- Give your data source a name, and optionally a description and resource
  tags.
- After the data source is created, a data source ID is shown. Copy this ID to use
  when you synchronize the data source with the index.

###### Topics

- [Creating an Amazon Q custom connector](custom-connector-hiw.md "custom-connector-hiw.md")
- [Required attributes](custom-required-attributes.md "custom-required-attributes.md")
- [Viewing metrics](custom-metrics.md "custom-metrics.md")
