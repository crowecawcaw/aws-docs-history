# Chunking and parsing with knowledge bases

Chunking and parsing are preprocessing techniques used to prepare and organize textual
data for efficient storage, retrieval, and utilization by a model. You use chunking and
parsing with the following data sources:

- [local file](data-source-document.md "data-source-document.md")
- [Amazon S3 bucket](data-source-project.md#data-source-project-s3 "data-source-project.md#data-source-project-s3")
- [Web crawler](data-source-document-web-crawler.md "data-source-document-web-crawler.md")

###### Topics

- [Chunking](#kb-chunking "#kb-chunking")
- [Parsing](#kb-parsing "#kb-parsing")

## Chunking

When ingesting your data, Amazon Bedrock first splits your documents or content into
manageable chunks for efficient data retrieval. The chunks are then converted to
embeddings and written to a vector index (vector representation of the data), while
maintaining a mapping to the original document. The vector embeddings allow the texts to
be quantitatively compared.

Amazon Bedrock supports different approaches to [chunking](../../../bedrock/latest/userguide/kb-chunking.md "../../../bedrock/latest/userguide/kb-chunking.md"). Amazon Bedrock in SageMaker Unified Studio
supports _default chunking_ which splits content into text chunks of approximately 300
tokens. The chunking process honors sentence boundaries, ensuring that complete
sentences are preserved within each chunk.

You can set the maximum number of source chunks to from the vector store. For more
information, see [Add an Amazon Bedrock Knowledge Base component to a chat agent app](add-kb-component-chat-app.md "add-kb-component-chat-app.md").

## Parsing

Parsing involves analyzing the structure of information to understand its components and
their relationships. With Amazon Bedrock in SageMaker Unified Studio, you can use two types of parser.

- Default parsing – Only parses text in your documents. This parser doesn't incur any usage charges.
- Foundation model parsing – Processes multimodal data,
  including both text and images, using a foundation model. This parser provides
  you the option to customize the prompt used for data extraction. The cost of
  this parser depends on the number of tokens processed by the foundation model.
  For a list of models that support parsing of Amazon Bedrock knowledge base data, see [Supported models and Regions for parsing](../../../bedrock/latest/userguide/knowledge-base-supported.md#knowledge-base-supported-parsing "../../../bedrock/latest/userguide/knowledge-base-supported.md#knowledge-base-supported-parsing").

There are additional costs to using foundation model parsing. This is due to its
use of a foundation model. The cost depends on the amount of data you have. See
[Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/") for more
information on the cost of foundation models.

Amazon Bedrock in SageMaker Unified Studio only supports foundation model parsing with PDF format files. If your files
aren't in PDF format, you must convert them to PDF format before you can apply foundation model
parsing.

There are limits for the types of files and total data that can be parsed using parsing.
For information on the file types for parsing, see [Document formats](../../../bedrock/latest/userguide/knowledge-base-ds.md#kb-ds-supported-doc-formats-limits "../../../bedrock/latest/userguide/knowledge-base-ds.md#kb-ds-supported-doc-formats-limits"). For information on the total data that can be parsed using foundation model
parsing, see [Quotas](../../../bedrock/latest/userguide/quotas.md "../../../bedrock/latest/userguide/quotas.md").

For more information, see [How content chunking and parsing works for knowledge bases](bedrock/latest/userguide/kb-chunking-parsing.md "bedrock/latest/userguide/kb-chunking-parsing.md").

To create a Knowledge Base that uses an embeddings model, vector store, and parsing,
see
[Create an Amazon Bedrock Knowledge Base component](creating-a-knowledge-base-component.md "creating-a-knowledge-base-component.md").
