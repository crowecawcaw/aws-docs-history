# Notes before enabling real-time vector embedding blueprints

The Managed Service for Apache Flink application will only support unstructured text or JSON data in the input stream.

Two modes of input processing are supported:

- When input data is **unstructured text**, the entire text message is embedded. The vector DB contains the original text and the generated embedding.
- When the input data is in **JSON** format, the application gives you the ability to configure and specify one or more keys within the JSON object value to use for the embedding process. If there is more than one key, all keys are vectorized together and indexed in the vector DB. The vector DB will contain the original message and the generated embedding.
  **Embedding Generation**: The application supports all text embedding models exclusively provided by Bedrock.

**Persist in vector DB store**: The application uses an
existing OpenSearch cluster (provisioned or Serverless) in the customer’s account as a destination for persisting embedded data. When using Opensearch Serverless to create a vector index, always use the vector field name `embedded_data`.

Similar to MSF blueprints, you are expected to manage the infrastructure to run the code associated with the real-time vector embedding blueprint.

Similar to MSF Blueprints, once an MSF application is created, it must be exclusively started in the AWS account using the console or CLI. AWS will not start the MSF application for you. You have to call the StartApplication API (through CLI or console) to get the application running.

**Cross-account movement of data**: The application does not allow you to move data between input stream and vector destinations that live in different AWS accounts.
