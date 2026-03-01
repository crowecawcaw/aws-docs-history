# Best practices for data source connector configuration in Amazon Q Business

The following list describes best practices for setting up and configuring your
Amazon Q Business data source connector:

- Each document in an index must be unique. Check that there are no
  duplicate documents in a data source, or across any data sources, that you
  plan to connect to an Amazon Q Business retriever.
- If you change your authentication type and credentials, you must update
  your IAM role to access the correct AWS Secrets Manager secret
  ID.
- We recommend that you regularly refresh or rotate your credentials and
  secret. Provide only the necessary access level for your own security. We
  don't recommend the re-use of credentials and secrets across data
  sources.
- IAM roles used for retrievers can't be used for data
  sources. If you're unsure if an existing role is used for a retriever or
  data source, create a new IAM role to avoid errors.
- If your application uses AWS KMS keys, ensure that the IAM role associated with your application environment has
  permission to describe the key, and to encrypt and decrypt data using
  it.
- For on-premises or server data source connectors, Amazon Q Business
  checks if the endpoint information included in Secrets Manager is the
  same as the endpoint information specified in your data source configuration
  details. This helps protect against the [confused deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md"), which is a security issue. The problem
  occurs when a user doesn’t have permission to perform an action. But, by
  using Amazon Q Business as a proxy, the user can access the configured
  secret and perform the action.

If you change your endpoint information later, you must create a new
secret to sync this information.

- Most data sources use regular expression patterns, which are inclusion or
  exclusion patterns referred to as _filters_.

If you specify an inclusion filter, only content that matches the
inclusion filter is indexed. If you specify an inclusion and exclusion
filter, documents that match the exclusion filter aren't indexed, even if
they match the inclusion filter.
