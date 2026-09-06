

# Using DynamoDB with LangChain
<a name="ddb-langchain"></a>

[LangChain](https://www.langchain.com/) is a framework for building applications with large language models (LLMs). Two LangChain integrations use DynamoDB: the `DynamoDBChatMessageHistory` class stores conversation history so a model can converse back and forth with a user across sessions, and the `DynamoDBVectorStore` class implements the LangChain vector store interface on DynamoDB vector indexes for similarity search.

## Chat message history
<a name="langchain-chat-history"></a>

The `DynamoDBChatMessageHistory` class, in the `langchain-community` package for Python and the `@langchain/community` package for JavaScript, persists chat messages in a DynamoDB table. The class expects an existing table whose partition key is a string attribute named `SessionId` (configurable through `primary_key_name`). Create the table with the AWS CLI:

```
aws dynamodb create-table \
  --table-name SessionTable \
  --attribute-definitions AttributeName=SessionId,AttributeType=S \
  --key-schema AttributeName=SessionId,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST
```

Install the packages, then read and write history keyed by a session ID:

```
pip install langchain-community boto3
```

```
from langchain_community.chat_message_histories import DynamoDBChatMessageHistory

history = DynamoDBChatMessageHistory(
    table_name="SessionTable",
    session_id="user-42",
)

history.add_user_message("Hello!")
history.add_ai_message("How can I help you today?")

print(history.messages)
```

Each chat session's messages are stored under its `session_id`, so a returning user picks up the conversation where they left off. The constructor also supports composite keys for isolating history by application details such as a user ID (`key`), Time to Live-based expiry of old sessions (`ttl`), and a cap on stored messages (`history_size`). For the full API, see the [Python reference](https://reference.langchain.com/python/langchain-community/chat_message_histories/dynamodb/DynamoDBChatMessageHistory) and the [JavaScript reference](https://reference.langchain.com/javascript/langchain-community/stores/message/dynamodb).

## Vector store backed by vector indexes
<a name="langchain-vector-store"></a>

The `DynamoDBVectorStore` class, in the `langchain-aws` package, implements the LangChain vector store interface using DynamoDB vector indexes (see [Using vector indexes in DynamoDB](VectorSearch.md)). Documents are stored as regular DynamoDB items and searched through the table's vector index with the `SearchVectors` API, so LangChain retrievers and RAG chains run similarity searches directly against the table that holds your data.

Install the package:

```
pip install langchain-aws boto3
```

Provide a table name and an embedding function. The table and vector index are created on first write if they don't exist:

```
from langchain_aws.embeddings import BedrockEmbeddings
from langchain_aws.vectorstores.dynamodb import DynamoDBVectorStore

vector_store = DynamoDBVectorStore.from_texts(
    ["hello", "developer", "wife"],
    embedding=BedrockEmbeddings(model_id="amazon.titan-embed-text-v2:0"),
    table_name="my-documents",
)

docs = vector_store.similarity_search("greeting", k=2)
```

To scope searches, pass `partition_attribute` when you construct the store. The vector index is then created with a search schema partition key on that document metadata field, and each search examines only one value of it, such as a collection, category, or tenant, rather than the whole corpus. Every search then supplies the value through `filter={partition_attribute: value}` or a store-level `default_partition_value`. The partition key is part of the index schema and cannot be changed after the index is created.

Keep the following in mind:
+ Like a global secondary index, the vector index is eventually consistent: a search issued immediately after `add_texts` may not include the just-written documents until the index catches up.
+ `SearchVectors` returns at most the top 100 matches per query, so the store's `k` parameter is capped at 100.
+ The index's dimensions, distance function, and search schema are fixed at creation. The store validates them against an existing index rather than proceeding with a mismatch.

For the full API, see [DynamoDBVectorStore in the langchain-aws repository](https://github.com/langchain-ai/langchain-aws/tree/main/libs/aws/langchain_aws/vectorstores/dynamodb).

## Additional resources
<a name="langchain-additional-resources"></a>
+ [DynamoDBChatMessageHistory Python reference](https://reference.langchain.com/python/langchain-community/chat_message_histories/dynamodb/DynamoDBChatMessageHistory)
+ [DynamoDBChatMessageHistory JavaScript reference](https://reference.langchain.com/javascript/langchain-community/stores/message/dynamodb)
+ [langchain-aws on GitHub](https://github.com/langchain-ai/langchain-aws)
+ [Build a scalable, context-aware chatbot with Amazon DynamoDB, Amazon Bedrock, and LangChain](https://aws.amazon.com/blogs/database/build-a-scalable-context-aware-chatbot-with-amazon-dynamodb-amazon-bedrock-and-langchain/)