# Building RAG systems with Amazon Nova

Retrieval-Augmented Generation (RAG) optimizes the output of a large language model (LLM)
by referencing an authoritative knowledge base outside of its training data sources before
it generates a response. This approach helps give the model current information and ground
it in domain-specific or proprietary data. It also provides a controllable information
source, which you can use to set access controls to specific content and troubleshoot issues
in the responses.

RAG works by connecting a _generator_ (often an LLM) to a content
database (such as a knowledge store) through a _retriever_. The retriever
is responsible for finding relevant information. In most enterprise applications, the
content database is a vector store, the retriever is an embedding model, and the generator
is an LLM. For more information, see [Retrieval Augmented
Generation](https://aws.amazon.com/what-is/retrieval-augmented-generation/ "https://aws.amazon.com/what-is/retrieval-augmented-generation/") and [Bedrock
Knowledge Bases](../../../bedrock/latest/userguide/kb-how-it-works.md "../../../bedrock/latest/userguide/kb-how-it-works.md").

A RAG system has several components. This guide focuses on how to use Amazon Nova as an LLM
in any RAG system.

You can use Amazon Nova models as the LLM within a Text RAG system. With Amazon Nova models,
you have the flexibility to build a RAG system with Amazon Bedrock Knowledge bases
or build your own RAG system. You can also associate your knowledge base with an Agent in
Amazon Bedrock Agents to add RAG capabilities to the Agent. For more information,
see [Automate
tasks in your application using conversational agents](../../../bedrock/latest/userguide/agents.md "../../../bedrock/latest/userguide/agents.md").

###### Topics

- [Using Amazon Bedrock Knowledge Bases](rag-br-knowledge.md "rag-br-knowledge.md")
- [Building a custom RAG system with Amazon Nova](rag-building.md "rag-building.md")
- [Using Amazon Nova for Multimodal RAG](rag-multimodal.md "rag-multimodal.md")
