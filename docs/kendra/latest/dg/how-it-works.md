# How Amazon Kendra works

Amazon Kendra provides search and Retrieval Augmented Generation (RAG) functionality
for your application. It indexes your documents directly—or from your third-party
document repository—and intelligently serves relevant information to your users. You
can use Amazon Kendra to create an updatable index of documents of a variety of types.
For a list of document types supported by Amazon Kendra, see [Types of
documents](index-document-types.md "index-document-types.md").

Amazon Kendra integrates with other services. You can connect an Amazon Kendra GenAI
Enterprise Edition index to [Amazon Q Business](../../../amazonq/latest/qbusiness-ug/what-is.md "../../../amazonq/latest/qbusiness-ug/what-is.md") and [Amazon Bedrock](../../../bedrock/latest/userguide/what-is-bedrock.md "../../../bedrock/latest/userguide/what-is-bedrock.md")
for creating your RAG chat solution. Or, you can power [Amazon Lex chat bots](../../../lexv2/latest/dg/faq-bot-kendra-search.md "../../../lexv2/latest/dg/faq-bot-kendra-search.md")
with Amazon Kendra search to provide useful answers to users' questions. You can also
use an [Amazon Simple Storage Service bucket](data-source-s3.md "data-source-s3.md") as a data source for Amazon Kendra to connect to
and index your documents.

Amazon Kendra has the following components:

- An [_index_](create-index.md "create-index.md") that holds your documents and makes
  them searchable.
- A [_data source_](data-source.md "data-source.md") that stores your documents and
  Amazon Kendra connects to. You can automatically synchronize a data source
  with an Amazon Kendra index so that your index stays updated with your source
  repository.
- A [_document addition API_](in-adding-documents.md "in-adding-documents.md") that adds
  documents directly to an index.
- A [_retrieve API_](../APIReference/API_Retrieve.md "../APIReference/API_Retrieve.md") that retrieves
  relevant passages or text excerpts given an input query.
- A [_query API_](../APIReference/API_Query.md "../APIReference/API_Query.md") that searches an index
  given an input query.
  You can use Amazon Kendra through the console or the API. You can create, update, and
  delete indexes. Deleting an index deletes all of its data source connectors and permanently
  deletes all of your document information from Amazon Kendra.

###### Topics

- [Indexes
  in Amazon Kendra](hiw-index.md "hiw-index.md")
- [Documents](hiw-documents.md "hiw-documents.md")
- [Data sources](hiw-data-source.md "hiw-data-source.md")
- [Queries](hiw-query.md "hiw-query.md")
- [Tags](tagging.md "tagging.md")
