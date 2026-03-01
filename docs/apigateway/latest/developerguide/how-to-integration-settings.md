# Integrations for REST APIs in API Gateway

After setting up an API method, you must integrate it with an endpoint in the backend. A
backend endpoint is also referred to as an integration endpoint and can be a Lambda function,
an HTTP webpage, or an AWS service action.

As with the API method, the API integration has an integration request and an integration
response. An integration request encapsulates an HTTP request received by the backend. It
might or might not differ from the method request submitted by the client. An integration
response is an HTTP response encapsulating the output returned by the backend.

Setting up an integration request involves the following: configuring how to pass
client-submitted method requests to the backend; configuring how to transform the request
data, if necessary, to the integration request data; and specifying which Lambda function to
call, specifying which HTTP server to forward the incoming request to, or specifying the
AWS service action to invoke.

Setting up an integration response (applicable to non-proxy integrations only) involves
the following: configuring how to pass the backend-returned result to a method response of a
given status code, configuring how to transform specified integration response parameters to
preconfigured method response parameters, and configuring how to map the integration
response body to the method response body according to the specified body-mapping templates.

Programmatically, an integration request is encapsulated by the [`Integration`](../api/API_Integration.md "../api/API_Integration.md") resource and
an integration response by the [`IntegrationResponse`](../api/API_IntegrationResponse.md "../api/API_IntegrationResponse.md") resource of API Gateway.

To set up an integration request, you create an [`Integration`](../api/API_Integration.md "../api/API_Integration.md") resource and
use it to configure the integration endpoint URL. You then set the IAM permissions to
access the backend, and specify mappings to transform the incoming request data before
passing it to the backend. To set up an integration response for non-proxy integration, you
create an [`IntegrationResponse`](../api/API_IntegrationResponse.md "../api/API_IntegrationResponse.md") resource and use it to set its target
method response. You then configure how to map backend output to the method response.

###### Topics

- [Set up an integration request in API Gateway](api-gateway-integration-settings-integration-request.md "api-gateway-integration-settings-integration-request.md")
- [Set up an integration response in API Gateway](api-gateway-integration-settings-integration-response.md "api-gateway-integration-settings-integration-response.md")
- [Lambda integrations for REST APIs in API Gateway](set-up-lambda-integrations.md "set-up-lambda-integrations.md")
- [HTTP integrations for REST APIs in API Gateway](setup-http-integrations.md "setup-http-integrations.md")
- [Stream the integration response for your proxy integrations in API Gateway](response-transfer-mode.md "response-transfer-mode.md")
- [Private integrations for REST APIs in API Gateway](private-integration.md "private-integration.md")
- [Mock integrations for REST APIs in API Gateway](how-to-mock-integration.md "how-to-mock-integration.md")
