# Create routes for HTTP APIs in API Gateway

Routes direct incoming API requests to backend resources. Routes consist of two parts: an
HTTP method and a resource path—for example, `GET /pets`. You can define
specific HTTP methods for your route. Or, you can use the `ANY` method to match
all methods that you haven't defined for a resource. You can create a `$default`
route that acts as a catch-all for requests that don’t match any other routes.

###### Note

API Gateway decodes URL-encoded request parameters before passing them to your backend integration.

## Working with path variables

You can use path variables in HTTP API routes.

For example, the `GET /pets/{petID}` route catches a `GET`
request that a client submits to
`https://`api-id`.execute-api.`us-east-2`.amazonaws.com/pets/6`.

A _greedy path variable_ catches all child resources of a route. To
create a greedy path variable, add `+` to the variable name—for
example, `{proxy+}`. The greedy path variable must be at the end of the
resource path.

## Working with query string parameters

By default, API Gateway sends query string parameters to your backend integration if they
are included in a request to an HTTP API.

For example, when a client sends a request to
`https://`api-id`.execute-api.`us-east-2`.amazonaws.com/pets`?id=4&type=dog``,
 the query string parameters `?id=4&type=dog` are sent to your
integration.

## Working with the `$default` route

The `$default` route catches requests that don't explicitly match other
routes in your API.

When the `$default` route receives a request, API Gateway sends the full request
path to the integration. For example, you can create an API with only a
`$default` route and integrate it on the `ANY` method with the
`https://petstore-demo-endpoint.execute-api.com` HTTP endpoint. When you
send a request to
`https://`api-id`.execute-api.`us-east-2`.amazonaws.com/store/checkout`,
API Gateway sends a request to
`https://petstore-demo-endpoint.execute-api.com/store/checkout`.

To learn more about HTTP integrations, see [Create HTTP proxy integrations for HTTP APIs](http-api-develop-integrations-http.md "http-api-develop-integrations-http.md").

## Routing API requests

When a client sends an API request, API Gateway first determines which [stage](http-api-stages.md "http-api-stages.md") to route the request to. If the request explicitly matches a stage,
API Gateway sends the request to that stage. If no stage fully matches the request, API Gateway
sends the request to the `$default` stage. If there's no
`$default` stage, then the API returns `{"message":"Not
 Found"}` and does not generate CloudWatch logs.

After selecting a stage, API Gateway selects a route. API Gateway selects the route with the
most-specific match, using the following priorities:

1. Full match for a route and method.
2. Match for a route and method with a greedy path variable (`{proxy+}`).
3. The `$default` route.

If no routes match a request, API Gateway returns `{"message":"Not Found"}` to
the client.

For example, consider an API with a `$default` stage and the following
example routes:

1. `GET /pets/dog/1`
2. `GET /pets/dog/{id}`
3. `GET /pets/{proxy+}`
4. `ANY /{proxy+}`
5. `$default`

The following table summarizes how API Gateway routes requests to the example
routes.

| Request                                                              | Selected route       | Explanation                                                                                                                                                        |
| -------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `GET https://`api-id`.execute-api.`region`.amazonaws.com/pets/dog/1` | `GET /pets/dog/1`    | The request fully matches this static route.                                                                                                                       |
| `GET https://`api-id`.execute-api.`region`.amazonaws.com/pets/dog/2` | `GET /pets/dog/{id}` | The request fully matches this route.                                                                                                                              |
| `GET https://`api-id`.execute-api.`region`.amazonaws.com/pets/cat/1` | `GET /pets/{proxy+}` | The request doesn't fully match a route. The route with a<br>`GET` method and a greedy path variable catches this<br>request.                                      |
| `POST https://`api-id`.execute-api.`region`.amazonaws.com/test/5`    | `ANY /{proxy+}`      | The `ANY` method matches all methods that you haven't<br>defined for a route. Routes with greedy path variables have higher<br>priority than the `$default` route. |
