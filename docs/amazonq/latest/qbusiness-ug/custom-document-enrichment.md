# Document enrichment in Amazon Q Business

###### Important

This section assumes that you understand [document attributes](doc-attributes.md "doc-attributes.md") and [metadata controls](mapping-doc-attributes.md "mapping-doc-attributes.md") in Amazon Q Business.

###### Note

Before you configure document enrichment, you must [create a Amazon Q Business retriever and index](select-retriever.md "select-retriever.md") for your
application.

The Amazon Q Business
_document enrichment_ feature helps you control both **what** documents and document attributes are ingested into your
index and also **how** they're ingested. Using document
enrichment, you can create, modify, or delete document attributes and document content
when you ingest them into your Amazon Q Business index.

You can use document enrichment to provide more structure and context to the data that
the large language model (LLM) powering Amazon Q Business uses to generate
responses. This is done in the following ways:

- **Extracting metadata** – To make data
  easier for the LLM to understand, document enrichment extracts metadata like
  document title, type, and date and organizes these by mapping them to index
  fields.
- **Categorization** – Tagging documents
  with metadata categories helps the LLM recognize both content and context. This
  helps LLMs prioritize relevant sources when answering queries about specific
  categories.
- **Adding custom metadata** – By enriching
  documents with your own custom metadata, you can provide more relevant context
  for the LLM to work with.
- **Improved Relevance** – As a result of
  structured data and metadata enrichment, the LLM can better match user queries
  to the most relevant documents. This can lead to more accurate responses.
  Document enrichment offers two kinds of methods that you can use for your
  solution:

- **Configure basic operations** – Use
  basic operations to add, update, or delete document attributes from your data.
  For example, you can scrub personally identifiable information (PII) by choosing
  to delete any document attributes related to PII.
- **Configure Lambda functions**
  – Use a preconfigured Lambda function to perform more
  customized, advanced document attribute manipulation logic to your data. For
  example, your enterprise data might be stored as scanned images. In that case,
  you can use a Lambda function to run Optical Character recognition
  (OCR) on the scanned documents to extract text from them. Then, each scanned
  document is treated as a text document during ingestion. Finally, during chat,
  Amazon Q Business will factor the textual data extracted from the
  scanned documents when it generates responses.
  When you implement your solution, you can choose to use both document enrichment
  methods together. That is, you can use basic operations to do a first parse of your data
  and then use a Lambda function for more complex operations. For example, you
  could first use a basic function to remove all PII information from your documents using
  document attributes. Then, use a Lambda function to extract text from
  scanned documents.

You can use document enrichment on both the AWS Management Console and with Amazon Q Business
API actions. If you use the console, you can only enrich documents connected to your
application environment using an Amazon Q Business data source.

###### Note

Document enrichment is only supported in an Amazon Q Business application environment
if you use an Amazon Q Business native retriever. If you use an Amazon Kendra retriever, we recommend that you [configure document enrichment](../../../kendra/latest/dg/custom-document-enrichment.md "../../../kendra/latest/dg/custom-document-enrichment.md") in Amazon Kendra.

###### Topics

- [How Amazon Q Business document enrichment works](cde-hiw.md "cde-hiw.md")
- [Using basic operations for Amazon Q Business document enrichment](cde-basic-operations.md "cde-basic-operations.md")
- [Using Lambda functions for Amazon Q Business document enrichment](cde-lambda-operations.md "cde-lambda-operations.md")
