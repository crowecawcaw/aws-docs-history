# Connecting Amazon Q Business data sources

A _data source_ allows you to combine data from different
places into one central index for your Amazon Q Business application. Amazon Q Business provides several easy ways to connect your data.

Before adding any data, you need to set up a retriever and an index for your application.
Once that's done, you can add data in three ways:

- **Upload documents directly** – Upload
  documents directly using the console or using the [BatchPutDocument](../api-reference/API_BatchPutDocument.md "../api-reference/API_BatchPutDocument.md") API
  operation.
- **Connecting a Amazon Q Business data source**
  – Use the AWS Management Console or the the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") API operation to
  connect a supported data source connector to your Amazon Q Business
  application.

###### Note

You must create an Amazon Q Business index to store your data before you connect a
data source to your application.

- **Connecting Amazon Kendra data sources** – Use
  existing Amazon Kendra data sources by connecting a [Amazon Kendra
  index](../../../kendra/latest/dg/create-index.md "../../../kendra/latest/dg/create-index.md") as a retriever.

If you're connecting a Amazon Kendra GenAI Enterprise Edition index from an Amazon Q Business
application, you can detach it and use it with other AWS Gen AI services, like
Amazon Bedrock. Detaching an Amazon Kendra index automatically deletes the retriever
Amazon Q Business created for it. For a list of features supported by Amazon Kendra GenAI
Enterprise indices, see [Amazon Kendra GenAI Enterprise Edition
index](../../../kendra/latest/dg/hiw-index-types.md#kendra-gen-ai-index "../../../kendra/latest/dg/hiw-index-types.md#kendra-gen-ai-index").

###### Note

Amazon Q Business uses user email ID to determine end user access to
documents in an index. When you connect an Amazon Kendra index to Amazon Q Business, Amazon Q Business relays the user’s identifying email ID to Amazon Kendra to
enable document filtering for end users. If data sources connected to your Amazon Kendra
index don’t use email-ID based document filtering, or the email ID is not
present, Amazon Q Business generates responses only from public
documents.

###### Topics

- [Creating an index for an Amazon Q Business application](select-retriever.md "select-retriever.md")
- [Uploading files](upload-docs.md "upload-docs.md")
- [Connecting Amazon Q Business data source connectors](supported-connectors.md "supported-connectors.md")
- [Troubleshooting data source connectors](troubleshooting-data-sources.md "troubleshooting-data-sources.md")
- [Managing Amazon Q Business data source resources](managing-resources-data-sources.md "managing-resources-data-sources.md")
