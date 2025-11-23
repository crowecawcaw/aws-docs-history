# Binary media types for

REST APIs in API Gateway

In API Gateway, the API request and response have a text or binary payload. A text payload is a
`UTF-8`-encoded JSON string. A binary payload is anything other than a text payload. The binary payload
can be, for example, a JPEG file, a GZip file, or an XML file. The API configuration required to support binary
media depends on whether your API uses proxy or non-proxy integrations.

If you use a proxy integration with payload
response streaming, you don't need to configure your binary media types. For more information, see [Stream the integration response for your proxy integrations in API Gateway](response-transfer-mode.md "response-transfer-mode.md").

## AWS Lambda proxy integrations

To handle binary payloads for AWS Lambda proxy integrations, you must base64-encode your function's response.
You must also configure the [binaryMediaTypes](../api/API_RestApi.md#apigw-Type-RestApi-binaryMediaTypes "../api/API_RestApi.md#apigw-Type-RestApi-binaryMediaTypes") for your API. Your API's `binaryMediaTypes` configuration is a list of
content types that your API treats as binary data. Example binary media types include `image/png` or
`application/octet-stream`. You can use the wildcard
character (`*`) to cover multiple media types.

API Gateway uses the first `Accept` header from clients to determine if a
response should return binary media. To return binary media when you can't control the order of `Accept` header
values, such as requests from a browser, set your API's binary media types to `*/*`.

For example code, see [Return binary media from a Lambda proxy
integration in API Gateway](lambda-proxy-binary-media.md "lambda-proxy-binary-media.md").

If you use a Lambda proxy integration with payload response streaming, you don't need to configure your binary
media types. For more information, see [Set up a Lambda proxy integration with payload response streaming in API Gateway](response-transfer-mode-lambda.md "response-transfer-mode-lambda.md").

## Non-proxy integrations

To handle binary payloads for non-proxy integrations, you add the media types to the
[binaryMediaTypes](../api/API_RestApi.md#apigw-Type-RestApi-binaryMediaTypes "../api/API_RestApi.md#apigw-Type-RestApi-binaryMediaTypes") list of the `RestApi`
resource. Your API's `binaryMediaTypes` configuration is a list of content
types that your API treats as binary data. Alternatively, you can set the [contentHandling](../api/API_Integration.md#contentHandling "../api/API_Integration.md#contentHandling")
properties on the [Integration](../api/API_Integration.md "../api/API_Integration.md")
and the [IntegrationResponse](../api/API_IntegrationResponse.md "../api/API_IntegrationResponse.md") resources. The `contentHandling` value can be `CONVERT_TO_BINARY`, `CONVERT_TO_TEXT`, or
undefined.

###### Note

For `MOCK` or private integrations, setting the `contentHandling` properties isn't supported in the AWS Management Console. You must use the
AWS CLI, CloudFormation, or an SDK to set the `contentHandling` properties.

Depending on the `contentHandling` value, and whether the
`Content-Type` header of the response or the `Accept` header of the incoming request matches an entry in the
`binaryMediaTypes` list, API Gateway can encode the raw binary
bytes as a base64-encoded string, decode a base64-encoded string back to its raw bytes, or
pass the body through without modification.

You must configure the API as follows to support binary payloads for your API in API Gateway:

- Add the desired binary media types to the `binaryMediaTypes` list on the [RestApi](../api/API_RestApi.md "../api/API_RestApi.md") resource. If this
  property and the `contentHandling` property are
  not defined, the payloads are handled as UTF-8 encoded JSON strings.
- Address the `contentHandling` property of the
  [Integration](../api/API_Integration.md "../api/API_Integration.md")
  resource.
  - To have the request payload converted from a base64-encoded string to
    its binary blob, set the property to
    `CONVERT_TO_BINARY`.
  - To have the request payload converted from a binary blob to a
    base64-encoded string, set the property to
    `CONVERT_TO_TEXT`.
  - To pass the payload through without modification, leave the property
    undefined. To pass a binary payload through without modification, you
    must also ensure that the `Content-Type` matches one of the
    `binaryMediaTypes` entries, and that [passthrough
    behaviors](integration-passthrough-behaviors.md "integration-passthrough-behaviors.md") are enabled for the API.

- Set the `contentHandling` property of the [IntegrationResponse](../api/API_IntegrationResponse.md "../api/API_IntegrationResponse.md") resource. The `contentHandling`
  property, `Accept` header in client requests, and your API's
  `binaryMediaTypes` combined determine how API Gateway handles content
  type conversions. For details, see [Content type conversions in
  API Gateway](api-gateway-payload-encodings-workflow.md "api-gateway-payload-encodings-workflow.md").

###### Important

When a request contains multiple media types in its `Accept` header, API Gateway honors only the first `Accept` media type. If you can't control the order of the `Accept` media types and the media type of your binary
content isn't the first in the list, add the first `Accept` media type in the `binaryMediaTypes`
list of your API. API Gateway handles all content types in this list as binary.

For example, to send a JPEG file using an `<img>`
element in a browser, the browser might send `Accept:image/webp,image/*,*/*;q=0.8` in a request. By adding `image/webp` to the `binaryMediaTypes` list, the endpoint receives the JPEG file as binary.

For detailed information about how API Gateway handles the text and binary payloads, see [Content type conversions in
API Gateway](api-gateway-payload-encodings-workflow.md "api-gateway-payload-encodings-workflow.md").
