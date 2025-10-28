# Set up a gateway response using

the API Gateway REST API

Before customizing a gateway response using the API Gateway REST API, you must have already
created an API and have obtained its identifier. To retrieve the API identifier, you can
follow [restapi:gateway-responses](../api/API_GetGatewayResponses.md "../api/API_GetGatewayResponses.md") link relation and examine the result.

###### To customize a gateway response using the API Gateway REST API

1. To overwrite an entire [GatewayResponse](../api/API_GatewayResponse.md "../api/API_GatewayResponse.md") instance, call the [gatewayresponse:put](../api/API_PutGatewayResponse.md "../api/API_PutGatewayResponse.md") action. Specify a desired [responseType](../api/API_GatewayResponse.md#responseType "../api/API_GatewayResponse.md#responseType") in the URL path parameter, and supply in the request
   payload the [statusCode](../api/API_GatewayResponse.md#statusCode "../api/API_GatewayResponse.md#statusCode"), [responseParameters](../api/API_GatewayResponse.md#responseParameters "../api/API_GatewayResponse.md#responseParameters"), and [responseTemplates](../api/API_GatewayResponse.md#responseTemplates "../api/API_GatewayResponse.md#responseTemplates") mappings.
2. To update part of a `GatewayResponse` instance, call the [gatewayresponse:update](../api/API_UpdateGatewayResponse.md "../api/API_UpdateGatewayResponse.md") action. Specify a desired
   `responseType` in the URL path parameter, and supply in the
   request payload the individual `GatewayResponse` properties you
   want—for example, the `responseParameters` or the
   `responseTemplates` mapping.
