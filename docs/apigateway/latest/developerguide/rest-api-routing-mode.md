# Send traffic to your APIs through your custom domain name in API Gateway

When you configure the routing mode for your custom domain name, you set how incoming traffic is directed to
your APIs. You send traffic to your APIs using routing rules, API mappings, or routing rules and API mappings. The
following section explains when to use routing rules, when to use API mappings, and how to set the routing mode for
your custom domain name.

## When to use routing rules

When you use routing rules, you direct incoming requests that match certain conditions to specific REST APIs
stages. For example, a rule can route a request to the `production` stage of your `users`
REST API it if contains the header `version:v1` and the base path `/users`. Use routing
rules to create advanced dynamic routing topologies that support use cases like A/B testing or increasing
usage of new versions of your APIs.

We recommend that when directing traffic to a REST API, you use routing rules for your custom domain name. You
can recreate any API mappings by using routing rules. For more information, see [Recreate an API mapping using routing rules](rest-api-routing-rules-recreate-api-mapping.md "rest-api-routing-rules-recreate-api-mapping.md").

For REST APIs, you can also use routing rules and API mappings together. When you use routing rules and API mappings
together, API Gateway always evaluates routing rules before it evaluates any API mappings. Use routing rules and API
mappings together to migrate your current custom domain names or to explore routing rules.

### Considerations for routing rules

The following considerations might impact your use of routing rules:

- WebSocket or HTTP APIs aren't supported as target APIs for routing rules.
- If your custom domain name has API mappings to both REST and HTTP APIs, routing rules isn't
  supported.
- You can create a routing rule for a private custom domain to a private REST API. You can create a
  routing rule for a public custom domain to a Regional or edge-optimized API.
- You can't create a routing rule
  for a public custom domain to a private API. You can't create a routing rule for a private custom domain name to a
  public API.

## Choose between routing rules and API mappings

We recommend that when possible, you use routing rules. Only use API mappings to send traffic to an HTTP or
WebSocket API.
