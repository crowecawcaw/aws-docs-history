AWS Migration Hub Refactor Spaces will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub Refactor Spaces, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Step 5: Create a route

This section describes how to create a route.

An application is used to incrementally re-route traffic away from an existing application
to new services. You can also use it to launch new features without touching the existing
application.

If the selected application does not have any routes, the new route becomes the
application’s default route and all traffic is routed to the selected service. If the application
has existing routes, then the route is scoped to a path and verb combination.

When created, the default route defaults to an active state. In this case, state is not a
required input for default route at creation. However, like all other state values the state of
the default route can be updated after creation to an inactive state, but only when all other
routes are also inactive. Conversely, no route can be active without the default route also being
active.

## Routes in environments without a network bridge

When you create a route to a service with a private URL endpoint in an environment without
a network bridge, route creation fails if you don't configure [VPC to VPC connectivity](../../../whitepapers/latest/aws-vpc-connectivity-options/amazon-vpc-to-amazon-vpc-connectivity-options.md "../../../whitepapers/latest/aws-vpc-connectivity-options/amazon-vpc-to-amazon-vpc-connectivity-options.md") between the service VPC and the application proxy VPC.

## Routes with path parameters

Refactor Spaces supports creating routes with path parameters. To include a path parameter
in a route, add the variable in curly braces. For example: `/users/{id}`, where
`{id}` represents the parameter that is forwarded to the service. For URL endpoints
you must parse the path parameters.

When using path parameters with Lambda services, the path parameters are parsed by API
Gateway and are added to the Lambda [event object](../../../apigateway/latest/developerguide/set-up-lambda-proxy-integrations.md#api-gateway-simple-proxy-for-lambda-input-format "../../../apigateway/latest/developerguide/set-up-lambda-proxy-integrations.md#api-gateway-simple-proxy-for-lambda-input-format"). Also, path parameters simplify creating service routes to a higher level
of granularity. For example:

```
/users => lambda1
/users/{userId} => lambda2
/users/{userId}/projects => lambda3
/users/{userId}/projects/{projectId} => lambda4
```

When using path parameters in Refactor Spaces avoid the following scenarios:

- Duplicate path parameters in a route. For example: /users/{id}/version/{id}. Route
  creation fails due to duplicate ‘{id}’ parameter value.
- Multiple parameters in same route level. For example: /users/{id}, /users/{name} causes
  path parameters to collide. Route creation fails because paths can only have 1 path parameter
  at the same route level.
- Parent-level paths with **Include child paths** selected. A route with
  path parameters will fail if the path parameter is at the same route level as another route
  with the same parent path. For example, creating a parent route of `/users/` with
  **Include child paths** selected, will collide if the desired nested route
  `/users/{id}` is at the same level as the parent route. A route at a different
  level than the parent route will not collide.

## Creating a route in Refactor Spaces

1. On the application details page (the page with the application's name as the heading),
   under **Routes**, choose **Create route**.
2. Choose a service for the route.
3. Choose **Create route**.
