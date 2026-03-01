# Methods for REST APIs in API Gateway

In API Gateway, an API method embodies a [method
request](../api/API_Method.md "../api/API_Method.md") and a [method
response](../api/API_MethodResponse.md "../api/API_MethodResponse.md"). You set up an API method to define what a client should or must do to
submit a request to access the service at the backend and to define the responses that the
client receives in return. For input, you can choose method request parameters, or an
applicable payload, for the client to provide the required or optional data at run time. For
output, you determine the method response status code, headers, and applicable body as
targets to map the backend response data into, before they are returned to the client. To
help the client developer understand the behaviors and the input and output formats of your
API, you can [document your API](api-gateway-documenting-api.md "api-gateway-documenting-api.md") and [provide proper error messages](api-gateway-gatewayResponse-definition.md#customize-gateway-responses "api-gateway-gatewayResponse-definition.md#customize-gateway-responses") for [invalid requests](api-gateway-method-request-validation.md "api-gateway-method-request-validation.md").

An API method request is an HTTP request. To set up the method request, you configure an
HTTP method (or verb), the path to an API [resource](../api/API_Resource.md "../api/API_Resource.md"), headers, applicable query string parameters. You also configure a
payload when the HTTP method is `POST`, `PUT`, or `PATCH`.
For example, to retrieve a pet using the [PetStore sample API](api-gateway-create-api-from-example.md "api-gateway-create-api-from-example.md"), you define the API method request of `GET
 /pets/{petId}`, where `{petId}` is a path parameter that can take a
number at run time.

```
GET /pets/1
Host: apigateway.us-east-1.amazonaws.com
...
```

If the client specifies an incorrect path, for example, `/pet/1` or
`/pets/one` instead of `/pets/1`, an exception is thrown.

An API method response is an HTTP response with a given status code. For a non-proxy
integration, you must set up method responses to specify the required or optional targets of
mappings. These transform integration response headers or body to associated method response
headers or body. The mapping can be as simple as an [identity transform](https://en.wikipedia.org/wiki/Identity_transform "https://en.wikipedia.org/wiki/Identity_transform") that
passes the headers or body through the integration as-is. For example, the following
`200` method response shows an example of passthrough of a successful
integration response as-is.

```
200 OK
Content-Type: application/json
...

{
    "id": "1",
    "type": "dog",
    "price": "$249.99"
}
```

In principle, you can define a method response corresponding to a specific response from
the backend. Typically, this involves any 2XX, 4XX, and 5XX responses. However, this may not
be practical, because often you may not know in advance all the responses that a backend may
return. In practice, you can designate one method response as the default to handle the
unknown or unmapped responses from the backend. It is good practice to designate the 500
response as the default. In any case, you must set up at least one method response for
non-proxy integrations. Otherwise, API Gateway returns a 500 error response to the client even
when the request succeeds at the backend.

To support a strongly typed SDK, such as a Java SDK, for your API, you should define the
data model for input for the method request, and define the data model for output of the
method response.

## Prerequisites

Before setting up an API method, verify the following:

- You must have the method available in API Gateway. Follow the instructions in [Tutorial: Create a REST API with an HTTP non-proxy integration](api-gateway-create-api-step-by-step.md "api-gateway-create-api-step-by-step.md").
- If you want the method to communicate with a Lambda function, you must have
  already created the Lambda invocation role and Lambda execution role in IAM. You
  must also have created the Lambda function with which your method will
  communicate in AWS Lambda. To create the roles and function, use the instructions
  in [Create a Lambda function for Lambda non-proxy integration](getting-started-lambda-non-proxy-integration.md#getting-started-new-lambda "getting-started-lambda-non-proxy-integration.md#getting-started-new-lambda") of the [Choose an AWS Lambda integration tutorial](getting-started-with-lambda-integration.md "getting-started-with-lambda-integration.md").
- If you want the method to communicate with an HTTP or HTTP proxy integration,
  you must have already created, and have access to, the HTTP endpoint URL with
  which your method will communicate.
- Verify that your certificates for HTTP and HTTP proxy endpoints are supported
  by API Gateway. For details see [API Gateway-supported certificate authorities for HTTP and HTTP proxy integrations in API Gateway](api-gateway-supported-certificate-authorities-for-http-endpoints.md "api-gateway-supported-certificate-authorities-for-http-endpoints.md").

###### Topics

- [Set up a method request in API Gateway](api-gateway-method-settings-method-request.md "api-gateway-method-settings-method-request.md")
- [Set up a method response in API Gateway](api-gateway-method-settings-method-response.md "api-gateway-method-settings-method-response.md")
- [Set up a method using the API Gateway console](how-to-set-up-method-using-console.md "how-to-set-up-method-using-console.md")
