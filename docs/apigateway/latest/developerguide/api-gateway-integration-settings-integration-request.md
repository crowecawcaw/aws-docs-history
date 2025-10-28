# Set up an

integration request in API Gateway

To set up an integration request, you perform the following required and optional
tasks:

1. Choose an integration type that determines how method request data is passed
   to the backend.
2. For non-mock integrations, specify an HTTP method and the URI of the targeted
   integration endpoint, except for the `MOCK` integration.
3. For integrations with Lambda functions and other AWS service actions, set an
   IAM role with required permissions for API Gateway to call the backend on your
   behalf.
4. For non-proxy integrations, set necessary parameter mappings to map
   predefined method request parameters to appropriate integration request
   parameters.
5. For non-proxy integrations, set necessary body mappings to map the incoming
   method request body of a given content type according to the specified mapping
   template.
6. For non-proxy integrations, specify the condition under which the incoming
   method request data is passed through to the backend as-is.
7. Optionally, specify how to handle type conversion for a binary
   payload.
8. Optionally, declare a cache namespace name and cache key parameters to enable
   API caching.
   Performing these tasks involves creating an [Integration](../api/API_Integration.md "../api/API_Integration.md") resource of API Gateway and
   setting appropriate property values. You can do so using the API Gateway console, AWS CLI
   commands, an AWS SDK, or the API Gateway REST API.

###### Topics

- [Basic tasks of an API integration
  request](integration-request-basic-setup.md "integration-request-basic-setup.md")
- [Choose an API Gateway API integration
  type](api-gateway-api-integration-types.md "api-gateway-api-integration-types.md")
- [Set up a proxy integration with a proxy
  resource](api-gateway-set-up-simple-proxy.md "api-gateway-set-up-simple-proxy.md")
- [Set up an API integration request
  using the API Gateway console](how-to-method-settings-console.md "how-to-method-settings-console.md")
