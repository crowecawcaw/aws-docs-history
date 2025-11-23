# Spark Connect support

Spark Connect is a client-server architecture for Apache Spark that decouples the application client from the Spark cluster's driver process, allowing remote connectivity to Spark from supported clients. Spark Connect also enables interactive debugging during development directly from your favorite IDEs/clients.

From Apache Spark version 3.5 release version onward, Athena supports Spark Connect as an AWS endpoint accessible using the `GetSessionEndpoint` API.

## API/CLI examples (GetSessionEndpoint)

You can use the `GetSessionEndpoint` API to get the Spark Connect endpoint for an interactive session.

```
aws athena get-session-endpoint \
  --region "REGION" \
  --session-id "SESSION_ID"
```

This API returns the Spark Connect endpoint URL for that session.

```
{
  "EndpointUrl": "ENDPOINT_URL",
  "AuthToken": "AUTH_TOKEN",
  "AuthTokenExpirationTime": "AUTH_TOKEN_EXPIRY_TIME"
}
```
