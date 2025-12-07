# Vector search

Vector search in Amazon OpenSearch Service enables you to search for semantically similar content using
machine learning embeddings rather than traditional keyword matching. Vector search converts
your data (text, images, audio, etc.) into high-dimensional numerical vectors (embeddings)
that capture the semantic meaning of the content. When you perform a search, OpenSearch
compares the vector representation of your query against the stored vectors to find the most
similar items.

Vector search includes the following key components.

**Vector fields**

OpenSearch supports the `knn_vector` field type to store dense
vectors with configurable dimensions (up to 16,000).

**Search methods**

- **k-NN (k-nearest neighbors)**: Finds the
  k most similar vectors
- **Approximate k-NN**: Uses algorithms
  like HNSW (Hierarchical Navigable Small World) for faster searches on
  large datasets

**Distance metrics**

Supports various similarity calculations including:

- Euclidean distance
- Cosine similarity
- Dot product

###### Common use cases

Vector search supports the following common use cases.

- **Semantic search**: Find documents with similar
  meaning, not just matching keywords
- **Recommendation systems**: Suggest similar products,
  content, or users
- **Image search**: Find visually similar images
- **Anomaly detection**: Identify outliers in data
  patterns
- **RAG (Retrieval Augmented Generation)**: Enhance LLM
  responses with relevant context

###### Integration with machine learning

OpenSearch integrates with the following machine learning services and models:

- **Amazon Bedrock**: For generating embeddings using
  foundation models
- **Amazon SageMaker AI**: For custom ML model deployment
- **Hugging Face models**: Pre-trained embedding
  models
- **Custom models**: Your own trained embedding
  models
  With vector search, you can build sophisticated AI-powered applications that understand
  context and meaning, going far beyond traditional text matching capabilities.
