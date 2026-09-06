

# Using Aurora PostgreSQL as a Knowledge Base for Amazon Bedrock
<a name="AuroraPostgreSQL.VectorDB"></a>

You can use an Aurora PostgreSQL DB cluster as a Knowledge Base for Amazon Bedrock. For more information, see [Create a vector store in Amazon Aurora](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup.html). A Knowledge Base automatically takes unstructured text data stored in an Amazon S3 bucket, converts it to text chunks and vectors, and stores it in a PostgreSQL database. With the generative AI applications, you can use Agents for Amazon Bedrock to query the data stored in the Knowledge Base and use the results of those queries to augment answers provided by foundational models. This workflow is called Retrieval Augmented Generation (RAG). For more information on RAG, see [Retrieval Augmented Generation (RAG)](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-customize-rag.html).

For detailed information about using Aurora PostgreSQL to build generative AI applications using RAG, see this [blog post](https://aws.amazon.com/blogs/database/build-generative-ai-applications-with-amazon-aurora-and-knowledge-bases-for-amazon-bedrock/).

**Topics**
+ [Prerequisites](#AuroraPostgreSQL.VectorDB.Prereq)
+ [Preparing Aurora PostgreSQL to be used as a Knowledge Base for Amazon Bedrock](#AuroraPostgreSQL.VectorDB.PreparingKB)
+ [Creating a Knowledge Base in the Bedrock console](#AuroraPostgreSQL.VectorDB.CreatingKB)
+ [Quick create an Aurora PostgreSQL Knowledge Base for Amazon Bedrock](AuroraPostgreSQL.quickcreatekb.md)

## Prerequisites
<a name="AuroraPostgreSQL.VectorDB.Prereq"></a>

Familiarize yourself with the following prerequisites to use Aurora PostgreSQL cluster as a Knowledge Base for Amazon Bedrock. At a high level, you need to configure the following services for use with Bedrock:
+ Amazon Aurora PostgreSQL DB cluster created in any of the following versions:
  + 16.1 and all higher versions
  + 15.4 and higher versions
  + 14.9 and higher versions
  + 13.12 and higher versions
  + 12.16 and higher versions
**Note**  
You must enable the `pgvector` extension in your target database and use version 0.5.0 or higher. For more information, see [pgvector v0.5.0 with HNSW indexing](https://aws.amazon.com/about-aws/whats-new/2023/10/amazon-aurora-postgresql-pgvector-v0-5-0-hnsw-indexing/). 
+ RDS Data API
+ A user managed in AWS Secrets Manager. For more information, see [Password management with Amazon Aurora and AWS Secrets Manager](rds-secrets-manager.md).

## Preparing Aurora PostgreSQL to be used as a Knowledge Base for Amazon Bedrock
<a name="AuroraPostgreSQL.VectorDB.PreparingKB"></a>

Follow the steps explained in the below sections to prepare Aurora PostgreSQL to be used as a Knowledge Base for Amazon Bedrock.

### Creating and configuring Aurora PostgreSQL
<a name="AuroraPostgreSQL.VectorDB.CreatingDBC"></a>

To configure Amazon Bedrock with an Aurora PostgreSQL DB cluster, you must first create an Aurora PostgreSQL DB cluster and take note of the important fields for configuring it with Amazon Bedrock. For more information about creating Aurora PostgreSQL DB cluster, see [Creating and connecting to an Aurora PostgreSQL DB cluster](CHAP_GettingStartedAurora.CreatingConnecting.AuroraPostgreSQL.md).
+ Enable Data API while creating Aurora PostgreSQL DB cluster. For more information on the versions supported, see [Using the Amazon RDS Data API](data-api.md).
+ Make sure to note down the Amazon Resource Names (ARN) of your Aurora PostgreSQL DB cluster. You'll need it to configure the DB cluster for use with Amazon Bedrock. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.ARN.html).

### Connecting to a database and installing pgvector
<a name="AuroraPostgreSQL.VectorDB.ConnectingDB"></a>

You can connect to Aurora PostgreSQL using any of the connection utilities. For more detailed information on these utilities, see [Connecting to an Amazon Aurora PostgreSQL DB cluster](Aurora.Connecting.md#Aurora.Connecting.AuroraPostgreSQL). Alternatively, you can use the RDS console query editor to run the queries. You need an Aurora DB cluster with the RDS Data API enabled to use the query editor.

1. Log in to the database with your master user and set up pgvector. Use the following command if the extension is not installed:

   ```
   CREATE EXTENSION IF NOT EXISTS vector;
   ```

   Use `pgvector` 0.5.0 and higher version that supports HNSW indexing. For more information, see [pgvector v0.5.0 with HNSW indexing](https://aws.amazon.com/about-aws/whats-new/2023/10/amazon-aurora-postgresql-pgvector-v0-5-0-hnsw-indexing/).

1. Use the following command to check the version of the `pg_vector` installed:

   ```
   SELECT extversion FROM pg_extension WHERE extname='vector';
   ```

### Setting up database objects and privileges
<a name="AuroraPostgreSQL.VectorDB.SetupDBObjects"></a>

1. Create a specific schema that Bedrock can use to query the data. Use the following command to create a schema:

   ```
   CREATE SCHEMA bedrock_integration;
   ```

1. Create a new role that Bedrock can use to query the database. Use the following command to create a new role:

   ```
   CREATE ROLE bedrock_user WITH PASSWORD '{{password}}' LOGIN;
   ```
**Note**  
Make a note of this password as you will need it later to create a Secrets Manager password.

   If you are using `psql` client, then use the following commands to create a new role:

   ```
   CREATE ROLE bedrock_user LOGIN;
   \PASSWORD {{password}};
   ```

1. Grant the `bedrock_user` permissions to manage the `bedrock_integration` schema. This will provide the ability to create tables or indexes within the schema.

   ```
   GRANT ALL ON SCHEMA bedrock_integration to bedrock_user;
   ```

1. Login as the `bedrock_user` and create a table in the `bedrock_integration schema`.

   ```
   CREATE TABLE bedrock_integration.bedrock_kb (id uuid PRIMARY KEY, embedding vector({{n}}), chunks text, metadata json, custom_metadata jsonb);
   ```

   This command will create the `bedrock_kb` table in the `bedrock_integration` schema with Titan embeddings.

   Replace n in the `vector({{n}})` data type with the appropriate dimension for the embedding model you are using. Use the recommendations below to help select your dimensions:
   + For the Titan v2 model, use `vector(1024)`, or `vector(512)`, or `vector (256)`. To learn more, see [Amazon Titan Embeddings Text](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan-embed-text.html).
   + For the Titan v1.2 model, use `vector(1536)`. To learn more, see [Amazon Titan Multimodal Embeddings G1](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan-embed-mm.html).
   + For the Cohere Embed model, use `vector(1024)`. To learn more, see [Cohere Embed models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-embed.html).
   + For the Cohere Embed Multilingual v3, use `vector(1024)`.

   The first four columns are mandatory. For metadata handling, Bedrock writes data from your metadata files to the `custom_metadata` column. We recommend creating this column if you plan to use metadata and filtering. If you don't create a `custom_metadata` column, add individual columns for each metadata attribute in your table before you begin ingestion. For more information, see [Configure and customize queries and response generation](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html).

1. Follow these steps to create the required indexes that Bedrock uses to query your data:
   + Create an index with the cosine operator which the bedrock can use to query the data.

     ```
     CREATE INDEX ON bedrock_integration.bedrock_kb USING hnsw (embedding vector_cosine_ops);
     ```
   + We recommend you to set the value of `ef_construction` to 256 for `pgvector` 0.6.0 and higher version that use parallel index building.

     ```
     CREATE INDEX ON bedrock_integration.bedrock_kb USING hnsw (embedding vector_cosine_ops) WITH (ef_construction=256);
     ```
   + Create an index which Bedrock can use to query the text data.

     ```
     CREATE INDEX ON bedrock_integration.bedrock_kb USING gin (to_tsvector('simple', chunks));
     ```
   + If you created a column for custom metadata, create an index which Bedrock can use to query the metadata.

     ```
     CREATE INDEX ON bedrock_integration.bedrock_kb USING gin (custom_metadata);
     ```

### Create a secret in Secrets Manager
<a name="AuroraPostgreSQL.VectorDB.SecretManager"></a>

Secrets Manager lets you store your Aurora credentials so that they can be securely transmitted to applications. If you didn't choose the AWS secrets manager option when creating Aurora PostgreSQL DB cluster, you can create a secret now. For more information about creating AWS Secrets Manager database secret, see [AWS Secrets Manager database secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_database_secret.html).

## Creating a Knowledge Base in the Bedrock console
<a name="AuroraPostgreSQL.VectorDB.CreatingKB"></a>

While preparing Aurora PostgreSQL to be used as the vector store for a Knowledge Base, you must gather the following details that you need to provide to Amazon Bedrock console.
+ **Amazon Aurora DB cluster ARN** – The ARN of your DB cluster.
+ **Secret ARN** – The ARN of the AWS Secrets Manager key for your DB cluster.
+ **Database name** – The name of your database. For example, you can use the default database {{postgres}}.
+ **Table name** – We recommend you to provide a schema qualified name while creating the table using the command similar to the following:

  ```
  CREATE TABLE bedrock_integration.bedrock_kb;
  ```

  This command will create the `bedrock_kb` table in the `bedrock_integration` schema.
+ When creating the table, make sure to configure it with the specified columns and data types. You can use your preferred column names instead of those listed in the table. Remember to take a note of the names you chose for reference during the Knowledge Base set up.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.VectorDB.html)

With these details, you can now create a Knowledge Base in the Bedrock console. For more detailed information on setting up a vector index and creating a Knowledge Base information, see [Create a vector store in Amazon Aurora](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-rds.html) and [Create a vector store in Amazon Aurora](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-create.html).

After adding Aurora as your Knowledge Base, you can now ingest your data sources for searching and querying. For more information, see [Ingest your data sources into the Knowledge Base](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-ingest.html).