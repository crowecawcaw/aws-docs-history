# REST API Connections

AWS Glue connectors cover a wide range of data sources both AWS and external. However, there may be proprietary systems or emerging platforms that native AWS Glue connectors do not support.
The AWS Glue REST connector provides a mechanism to configure a customized connector for any data source that has a REST-based API which then works the same way as natively
supported AWS Glue connectors. This capability minimizes the need to build custom libraries or ETL scripts to access these data sources.

To enable the REST API connector, AWS Glue has introduced a new AWS resource - **Connection Type**.
The following operations can be used to manage connectivity to REST API-based data sources:

- **RegisterConnectionType** - Registers a Connection Type in AWS Glue based
  on the configuration provided. For request structure, See
  [RegisterConnectionType](../webapi/API_RegisterConnectionType.md "../webapi/API_RegisterConnectionType.md").
- **DeleteConnectionType** - Deletes a Connection Type configuration in AWS Glue.
  See [DeleteConnectionType](../webapi/API_DeleteConnectionType.md "../webapi/API_DeleteConnectionType.md").
- **DescribeConnectionType** - Returns full details of the supported options
  for a given connection type in AWS Glue. See [DescribeConnectionType](../webapi/API_DescribeConnectionType.md "../webapi/API_DescribeConnectionType.md").
- **ListConnectionTypes** - Returns list of connection types with high-level
  details of what is supported for each AWS Glue connection type. See
  [ListConnectionTypes](../webapi/API_ListConnectionTypes.md "../webapi/API_ListConnectionTypes.md").

## Creating a REST connection type in AWS Glue

To create a REST connection type, use the AWS CLI, AWS SDK or AWS API to invoke the
RegisterConnectionType API. Configuration details are provided based on the REST API being connected to.

###### Note

REST connections cannot be created using AWS Glue console

### Pre-Requisite

Before attempting to configure your AWS Glue REST API connector, you need to familiarize yourself with
the internal workings of the REST API. It helps if you have the REST API documentation for the data
source and a tool for inspecting the request/ response structure.

The following properties of the REST API should be identified:

- Authentication mechanism used for calls made to the REST endpoint. AWS Glue REST API connectors
  support: **basic authentication, OAuth2 - ClientCredentials,
  OAuth2 - Authorization Code, OAuth2 - JWT and custom authentication**.
- Entities (data objects) that you can transfer through the REST endpoint and related metadata (such as
  field names and data types).
- The HTTP request and response structure. This structure includes the HTTP method, endpoint URL,
  headers, query parameters, and the format of the request body and response payload.
- The pagination scheme. AWS Glue REST API connectors support two pagination schemes:
  `cursor-based` and `offset-based` pagination.

### RegisterConnectionType

Registers a ConnectionType in AWS Glue based on the configuration provided. The ConnectionType resource is
a new AWS Glue resource that stores details about how requests and responses are interpreted by the
data source. Today, only the REST protocol is supported.
It encapsulates details about the REST API source such as:

- **Connection properties** - Defines BaseUrl to connect to REST
  API and any additional request parameters needed to take input during AWS Glue CreateConnection.
- **Authentication configuration** - Defines how requests to the
  REST API are authenticated. This configuration is used when creating an AWS Glue Connection for the
  Connection Type.
- **REST configuration** - Defines HTTP request and response
  configuration to read data from REST API source. The following properties need to be configured at either the
  **Global** or **Entity** level:
  - **Request method** - Defines the REST HTTP Method.
  - **Response configuration** - Defines how the API response should
    be interpreted (including Records or Error locations in the body).
  - **Pagination configuration** - Defines the strategy that the REST API
    uses for paginating the resulting records and how the pagination properties are to be
    sent/ retrieved.
  - **Validation endpoint configuration** - Defines the endpoint
    to be called to validate an AWS Glue connection.
  - **Entity configurations** - Defines the REST entities that the
    connector supports and their schema.

### RegisterConnectionType Request Syntax

See [RegisterConnectionType](../webapi/API_RegisterConnectionType.md "../webapi/API_RegisterConnectionType.md")

Once a REST API connection type has been registered, it is ready to be used to create connections to
the configured data source. Refer to [Connecting to REST APIs](connecting-to-data-rest-api.md "connecting-to-data-rest-api.md")
for detailed instructions.
