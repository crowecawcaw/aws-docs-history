# AWS Toolkit Experience in Remote

Session

AWS Toolkit is also available in the remote IDE session. In the remote session,
since you are already authenticated and are in a specific project, you are directly
presented with the project resources. Currently the remote session offers:

- The ability to use Data Explorer to browse your project data sources
  within the IDE (S3 buckets, Redshift, Lakehouse)
- The ability for notebook users to pick Language and Compute Connections
  for each cell. This allows you to author polyglot notebooks where each cell
  can use its own language (Python, SQL, Markdown etc) and compute connection
  (Local Python, Athena, Redshift etc). This enables you to run code against
  your Spark and SQL connections from your local IDE through Amazon SageMaker Unified Studio
  Spaces.
