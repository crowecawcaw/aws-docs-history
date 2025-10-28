# How content chunking works for knowledge bases

When ingesting your data, Amazon Bedrock first splits your documents or content into manageable chunks for efficient data
retrieval. The chunks are then converted to embeddings and written to a vector index (vector representation
of the data), while maintaining a mapping to the original document. The vector embeddings allow the texts to
be quantitatively compared.

###### Topics

- [Standard chunking](#kb-standard-chunking "#kb-standard-chunking")
- [Hierarchical chunking](#kb-hiearchical-chunking "#kb-hiearchical-chunking")
- [Semantic chunking](#kb-semantic-chunking "#kb-semantic-chunking")

## Standard chunking

Amazon Bedrock supports the following standard approaches to chunking:

- Fixed-size chunking: You can configure the desired chunk size by specifying the number of tokens per
  chunk, and an overlap percentage, providing flexibility to align with your specific requirements. You can
  set the maximum number of tokens that must not exceed for a chunk and the overlap percentage between consecutive
  chunks.
- Default chunking: Splits content into text chunks of approximately 300 tokens. The chunking process honors
  sentence boundaries, ensuring that complete sentences are preserved within each chunk.

You can also choose no chunking for your documents. Each document is treated a single text chunk. You might want
to pre-process your documents by splitting them into separate files before choosing no chunking as your chunking
approach/strategy. If you choose no chunking for your documents, you cannot view page number in citation or filter by
the _x-amz-bedrock-kb-document-page-number_ metadata field/attribute.

## Hierarchical chunking

Hierarchical chunking involves organizing information into nested structures of child and parent chunks.
When creating a data source, you are able to define the parent chunk size, child chunk size and the number of
tokens overlapping between each chunk. During retrieval, the system initially retrieves child chunks, but replaces
them with broader parent chunks so as to provide the model with more comprehensive context.

Small text embeddings are more precise, but retrieval aims for comprehensive context. A
hierarchical chunking system balances these needs by replacing retrieved child chunks with
their parent chunks when appropriate.

###### Note

- Since child chunks get replaced by parent chunks during retrieval, the returned number of results might be less than the requested amount.
- Hierarchical chunking is not supported when using S3 vector bucket as your vector store.

For hierarchical chunking, Amazon Bedrock knowledge bases supports specifying two levels or the following depth for chunking:

- Parent: You set the maximum parent chunk token size.
- Child: You set the maximum child chunk token size.

You also set the overlap tokens between chunks. This is the absolute number of overlap tokens
between consecutive parent chunks and consecutive child chunks.

## Semantic chunking

Semantic chunking is a natural language processing technique that divides text
into meaningful chunks to enhance understanding and information retrieval. It aims to improve
retrieval accuracy by focusing on the semantic content rather than just syntactic structure.
By doing so, it may facilitate more precise extraction and manipulation of relevant information.

When configuring semantic chunking, you have the option to specify the following
hyper parameters.

- Maximum tokens: The maximum number of tokens that should be included in a single chunk,
  while honoring sentence boundaries.
- Buffer size: For a given sentence, the buffer size defines the number of surrounding sentences
  to be added for embeddings creation. For example, a buffer size of 1 results in 3 sentences (current,
  previous and next sentence) to be combined and embedded. This parameter can influence how much text
  is examined together to determine the boundaries of each chunk, impacting the granularity and coherence
  of the resulting chunks. A larger buffer size might capture more context but can also introduce noise,
  while a smaller buffer size might miss important context but ensures more precise chunking.
- Breakpoint percentile threshold: The percentile threshold of sentence distance/dissimilarity
  to draw breakpoints between sentences. A higher threshold requires sentences to be more
  distinguishable in order to be split into different chunks. A higher threshold results in fewer
  chunks and typically larger average chunk size.

###### Note

There are additional costs to using semantic chunking due to its use of a
foundation model. The cost depends on the amount of data you have. See
[Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/") for more
information on the cost of foundation models.
