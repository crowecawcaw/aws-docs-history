# Add a Knowledge Base to your Amazon Bedrock app

You can use Knowledge Base components to store data from an external data source for use in a [chat agent app](create-chat-app.md "create-chat-app.md") or
[flow app](create-flows-app.md "create-flows-app.md"). The data source for a Knowledge Base can be a [document](data-source-document.md "data-source-document.md"), such as a PDF file, or content from a [web crawler](data-source-document-web-crawler.md "data-source-document-web-crawler.md") that gathers content from specific
source URLs. When you create a Knowledge Base, you specify an embeddings model to convert the data into numerical vector representations and a vector store
for storing and managing your embeddings. Vector stores can be easily indexed for efficient retrieval in a process known as
_retrieval augmented generation (RAG)_. RAG enables foundation models to generate more accurate responses by providing relevant context from the vector store.

The data source for a knowledge base can be one of the following:

- A [document](data-source-document.md "data-source-document.md"), such as a PDF file
- A [web crawler](data-source-document-web-crawler.md "data-source-document-web-crawler.md") that gathers content from specific
  source URLs
- A data source already in your project, such as an Amazon S3 bucket, or structured data in Amazon Redshift
  You can then use the knowledge base in a [chat agent app](create-chat-app.md "create-chat-app.md") and a [flow app](create-flows-app.md "create-flows-app.md").

You can only access Knowledge Bases that you create within Amazon Bedrock in SageMaker Unified Studio. You can't access Knowledge Bases that you
create in the Amazon Bedrock console or AWS SDK.

For more information, see [Build and manage knowledge bases for
retrieval and responses](../../../bedrock/latest/userguide/knowledge-base-resource.md "../../../bedrock/latest/userguide/knowledge-base-resource.md") in the _Amazon Bedrock User Guide_.

###### Topics

- [Create an Amazon Bedrock Knowledge Base component](creating-a-knowledge-base-component.md "creating-a-knowledge-base-component.md")
- [Add an Amazon Bedrock Knowledge Base component to a chat agent app](add-kb-component-chat-app.md "add-kb-component-chat-app.md")
- [Add a Knowledge Base component to a flow app](add-kb-component-prompt-flow-app.md "add-kb-component-prompt-flow-app.md")
- [Synchronize an Amazon Bedrock Knowledge Base](kb-sync.md "kb-sync.md")
