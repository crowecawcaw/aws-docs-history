# Retrieving responses from indexes in Amazon Kendra

After you create an index, you can start searching your documents.

To search an Amazon Kendra index, you use either the [Retrieve](../APIReference/API_Retrieve.md "../APIReference/API_Retrieve.md") API operation or the [Query](../APIReference/API_Query.md "../APIReference/API_Query.md") API
operation.

The Retrieve API operation
is
ideal for Retrieval Augmented Generation (RAG) use cases. For a
given query, it returns a ranked list of semantically relevant passages of up to 200
token words.
You
can send these to a large language model (LLM) to generate an
answer using RAG. For more information, see [Searching an index](searching.md "searching.md").

The Query API operation is best for document search use cases. For a given query,
it returns a list of ranked documents with 100 word excerpts that are relevant to
the query. This is useful for traditional document search use cases where users are
browsing through a list of ranked documents.

To see what features are supported by the Retrieve and Query API operations for
each index type, see [Index types](hiw-index-types.md "hiw-index-types.md").
