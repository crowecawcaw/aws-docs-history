# Import an edge-optimized API into API Gateway

You can import an API's OpenAPI definition file to create a new edge-optimized API by
specifying the `EDGE` endpoint type as an additional input, besides the OpenAPI
file, to the import operation. You can do so using the API Gateway console, AWS CLI, or an AWS SDK.

For a tutorial on using the Import API feature
from the API Gateway console, see [Tutorial: Create a REST API by importing an
example](api-gateway-create-api-from-example.md "api-gateway-create-api-from-example.md").

###### Topics

- [Import an edge-optimized API
  using the API Gateway console](#import-edge-optimized-api-with-console "#import-edge-optimized-api-with-console")
- [Import an edge-optimized API
  using the AWS CLI](#import-edge-optimized-api-with-awscli "#import-edge-optimized-api-with-awscli")

## Import an edge-optimized API

using the API Gateway console

To import an edge-optimized API using the API Gateway console, do
the following:

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway "https://console.aws.amazon.com/apigateway").
2. Choose **Create API**.
3. Under **REST API**, choose **Import**.
4. Copy an API's OpenAPI definition and paste it into the code editor, or choose
   **Choose file** to load an OpenAPI file from a local
   drive.
5. For **API endpoint type**,
   select **Edge-optimized**.
6. Choose **Create API** to start importing the OpenAPI
   definitions.

## Import an edge-optimized API

using the AWS CLI

The following [import-rest-api](../../../cli/latest/reference/apigateway/import-rest-api.md "../../../cli/latest/reference/apigateway/import-rest-api.md") command
imports an API from an OpenAPI definition file to create a new edge-optimized API:

```
aws apigateway import-rest-api \
    --fail-on-warnings \
    --body 'file://path/to/API_OpenAPI_template.json'
```

or with an explicit specification of the `endpointConfigurationTypes` query
string parameter to `EDGE`:

```
aws apigateway import-rest-api \
    --parameters endpointConfigurationTypes=EDGE \
    --fail-on-warnings \
    --body 'file://path/to/API_OpenAPI_template.json'
```
