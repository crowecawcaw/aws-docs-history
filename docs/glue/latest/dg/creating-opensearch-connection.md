# Creating a OpenSearch Service connection

**Prerequisites**:

- Identify the domain endpoint, `aosEndpoint` and port,
  `aosPort` you would
  like to read from, or create the resource by following instructions in the Amazon OpenSearch Service documentation.
  For more information on creating a domain, see [Creating and managing
  Amazon OpenSearch Service domains](../../../opensearch-service/latest/developerguide/createupdatedomains.md "../../../opensearch-service/latest/developerguide/createupdatedomains.md") in the Amazon OpenSearch Service documentation.

An Amazon OpenSearch Service domain endpoint will have the following default form,
https://search-`domainName`-`unstructuredIdContent`.`region`.es.amazonaws.com.
For more information on identifying your domain endpoint, see [Creating and managing
Amazon OpenSearch Service domains](../../../opensearch-service/latest/developerguide/createupdatedomains.md "../../../opensearch-service/latest/developerguide/createupdatedomains.md") in the Amazon OpenSearch Service documentation.

Identify or generate HTTP basic authentication credentials, `aosUser` and
`aosPassword` for your domain.

###### To configure a connection to OpenSearch Service:

1. In AWS Secrets Manager, create a secret using your OpenSearch Service credentials.
   To create a secret in Secrets Manager, follow the tutorial available in [Create an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the AWS Secrets Manager documentation.
   After creating the secret, keep the Secret name, `secretName` for the next step.
   - When selecting **Key/value pairs**, create a pair for
     the key `USERNAME` with the value `aosUser`.
   - When selecting **Key/value pairs**, create a pair for
     the key `PASSWORD` with the value `aosPassword`.

2. In the AWS Glue console, create a connection by following the steps in [Adding an AWS Glue connection](console-connections.md "console-connections.md").
   After creating the connection, keep the connection name, `connectionName`, for future use in AWS Glue.
   - When selecting a **Connection type**, select OpenSearch Service.
   - When selecting a Domain endpoint, provide `aosEndpoint`.
   - When selecting a port, provide `aosPort`.
   - When selecting an **AWS Secret**, provide `secretName`.
