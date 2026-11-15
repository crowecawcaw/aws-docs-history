

# Limitations and notes for the Pinecone connector
<a name="pinecone-connector-limitations"></a>

The following are limitations and notes for the Pinecone connector:
+ Pinecone is supported as a source only. Writing to Pinecone is not supported.
+ Each connection reads the indexes, collections, and backups of the single Pinecone project that its API key belongs to. To read another project, create a separate connection that uses an API key from that project.
+ Job bookmarks are not supported.