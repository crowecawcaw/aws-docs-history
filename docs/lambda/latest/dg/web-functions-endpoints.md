

# Lambda Web Function endpoints
<a name="web-functions-endpoints"></a>

An endpoint is a child resource of a Web Function that provides a network entry point for HTTP traffic. Each endpoint includes a unique domain name with TLS and an authentication type. It also has settings for geographic scope, scaling, throttling, and traffic routing. A Web Function can have up to 10 endpoints, each with independent configuration.

The following sections explain endpoint types, domain names, authentication, and replication. For information about scaling and throttling settings, see [Scaling behavior for Lambda Web Functions](web-functions-scaling.md). For information about auto-deployment modes and traffic routing, see [Deployment patterns](web-functions-deployment.md).

## Endpoint types
<a name="web-functions-endpoint-types"></a>

The endpoint type determines how Lambda deploys your Web Function across AWS Regions and how traffic is routed to it. You choose the endpoint type when you create the endpoint. The endpoint type cannot be changed after creation.

**HomeRegion**  
Runs your Web Function in a single AWS Region. Lambda serves requests from the Region where you created the endpoint. Lambda allocates a single regional domain name for the endpoint.  
Use **HomeRegion** for applications that do not require multi-Region availability, or when you want to start with the simplest configuration.

**MultiRegion**  
Runs your Web Function in multiple AWS Regions. You specify the target Regions when you create the endpoint. Lambda adds the home Region automatically. The endpoint must include at least one other Region. To route traffic to a revision, you set the endpoint's revision weights. Lambda then replicates your code and configuration to all specified Regions automatically. Lambda allocates a single global domain name. It uses latency-based routing to send each request to the Region that typically provides the lowest latency for the caller. Lambda doesn't perform health-based failover.  
You manage the Web Function from a single home Region. Lambda handles replication to the other Regions. Clients connect to one domain name.  
Use **MultiRegion** for global applications that need low latency for users in multiple geographic locations.

**PerRegion**  
Runs your Web Function in multiple AWS Regions, with a separate regional domain name in each Region. You specify the target Regions when you create the endpoint. Lambda adds the home Region automatically. The endpoint must include at least one other Region. Lambda sets up the endpoint in each specified Region automatically. Each Region has its own independent domain name.  
Unlike **MultiRegion**, Lambda does not perform automatic latency-based routing. You manage how traffic reaches each regional domain, for example with your own Route 53 routing policy or a CloudFront distribution.  
Use **PerRegion** when you need control over routing decisions per Region, for example to implement geographic restrictions, custom failover logic, or Region-specific traffic policies.

The Regions and endpoint type cannot be updated after creation. To change these, create a new endpoint with the configuration that you want, migrate traffic to the new endpoint's domain name, and then delete the old endpoint.

For details about how Lambda replicates your Web Function across Regions and routes traffic, see [Multi-Region deployment](web-functions-endpoint-replication.md).

## Domain name
<a name="web-functions-endpoint-domain"></a>

Lambda allocates a unique domain name to each endpoint when you create it. Clients send HTTPS requests to this domain to invoke your Web Function. The domain supports HTTPS, and Lambda manages the TLS certificate for the domain. You don't create, renew, or manage certificates yourself.

The domain name format depends on the endpoint type:
+ **HomeRegion** and **PerRegion** – Each Region has a domain in the format:

  ```
  {{domain-id}}.{{shard-id}}.lambda-web.{{region}}.on.aws
  ```

  Example: `bcdfghjklmnpqrst.b7t.lambda-web.ap-northeast-3.on.aws`
+ **MultiRegion** – A single global domain in the format:

  ```
  {{domain-id}}.lambda-web.global.on.aws
  ```

  Example: `bcdfghjklmn.lambda-web.global.on.aws`

  Lambda uses latency-based routing to select a Region for each client.

You can retrieve the domain name from the `GetWebFunctionEndpoint` response or from the Lambda console after the endpoint reaches the **Active** state.

**Note**  
Web Function endpoints don't support attaching a custom domain name directly. Clients that call the endpoint's domain must use the Lambda-allocated domain name. To serve traffic on your own domain, put an Amazon CloudFront distribution in front of the endpoint and use the Lambda-allocated domain name as the origin.

## Authentication type
<a name="web-functions-endpoint-auth"></a>

The `authType` setting controls whether Lambda authenticates incoming HTTP requests before passing them to your application. You can update this setting on an existing endpoint.

**ApplicationManaged**  
Lambda does not authenticate incoming requests. All HTTP requests are forwarded directly to your application. You are responsible for handling authentication in your application code.

**IamAuth**  
Lambda validates the signature of each request. Sign requests with AWS Signature Version 4 (SigV4) for **HomeRegion** and **PerRegion** domains, and with Signature Version 4a (SigV4a) for a **MultiRegion** global domain. Only callers with the `lambda:InvokeWebFunctionEndpoint` permission can invoke the endpoint.

For full details on authentication, including CloudFront integration and resource-based policies, see [Lambda Web Function endpoint access control](web-functions-endpoint-access-control.md).

## Auto-deployment mode
<a name="web-functions-endpoint-auto-deploy"></a>

The `autoDeploymentMode` setting controls whether Lambda automatically routes traffic to new revisions each time you deploy your application. You can update this setting on an existing endpoint.

If you omit `autoDeploymentMode` in an API request, it defaults to `Disabled`. The Lambda console and the `aws lambda-web deploy` command use `LatestRevision` for new `HomeRegion` endpoints. `LatestRevision` is supported only for `HomeRegion` endpoints, so `MultiRegion` and `PerRegion` endpoints always use `Disabled`. When using `Disabled`, specify `revisionWeights` that total 100.

**LatestRevision**  
Lambda automatically routes 100% of traffic to the newest active revision. Use for development and staging environments. LatestRevision mode is available only for **HomeRegion** endpoints.

**Disabled**  
Lambda does not change traffic routing when you create a new revision. You control routing manually with revision weights. Use for production environments. Disabled mode is available for all endpoint types. **MultiRegion** and **PerRegion** endpoints always use Disabled mode.

For details on deployment patterns, rollback, and mode switching behavior, see [Deployment patterns](web-functions-deployment.md).

## Scaling and throttling
<a name="web-functions-endpoint-scaling-summary"></a>

Each endpoint has scaling and throttling settings that control capacity. You can update these settings on an existing endpoint with `update-web-function-endpoint`. Omit `--scaling-config` or `--throttle-config` to keep its current value, or pass an empty object (`'{}'`) to clear a previously set value. To remove a rate limit, pass an empty `--throttle-config` object. A `rateLimit` of 0 blocks all traffic.
+ **`maxEnvironments`** – Optional. The maximum number of execution environments for the endpoint in each Region. When not set, the endpoint scales as needed within the account quotas.
+ **`rateLimit`** – Maximum requests per second. This setting is optional. When it's not set, the endpoint is limited by the per-endpoint request rate quota of 10,000 RPS and by the account quotas. The rate limit applies to the endpoint as a whole, across all execution environments. It is not a per-environment limit. For **MultiRegion** and **PerRegion** endpoints, each Region enforces the limit independently. Excess requests receive HTTP 429.

For details on how these settings interact with revision-level concurrency and guidance on choosing values, see [Scaling behavior for Lambda Web Functions](web-functions-scaling.md).

## Creating and managing endpoints
<a name="web-functions-endpoint-manage"></a>

### Creating an endpoint
<a name="web-functions-endpoint-create"></a>

**To create a HomeRegion endpoint (AWS CLI)**
+ 

  ```
  aws lambda-web create-web-function-endpoint \
      --function-name {{my-web-app}} \
      --endpoint-name {{my-endpoint}} \
      --endpoint-type HomeRegion \
      --auth-type ApplicationManaged \
      --auto-deployment-mode LatestRevision
  ```

**To create a MultiRegion endpoint (AWS CLI)**
+ 

  ```
  aws lambda-web create-web-function-endpoint \
      --function-name {{my-web-app}} \
      --endpoint-name {{my-global-endpoint}} \
      --endpoint-type MultiRegion \
      --regions {{us-east-1}} {{eu-west-1}} {{ap-northeast-1}} \
      --auth-type ApplicationManaged \
      --revision-weights '[{"revisionId": "{{rev-a1b2c}}", "weight": 100}]'
  ```

  MultiRegion and PerRegion endpoints require revision weights, because **LatestRevision** auto-deployment is not available for them. For more information, see [Deployment patterns](web-functions-deployment.md).

### Listing endpoints
<a name="web-functions-endpoint-list"></a>

```
aws lambda-web list-web-function-endpoints \
    --function-name {{my-web-app}}
```

The response includes each endpoint's name, type, domain name, state, and configuration.

### Getting endpoint details
<a name="web-functions-endpoint-get"></a>

```
aws lambda-web get-web-function-endpoint \
    --function-name {{my-web-app}} \
    --endpoint-name {{my-endpoint}}
```

The response includes the endpoint's domain name, state, authentication type, auto-deployment mode, scaling settings, revision weights, and (for `MultiRegion` and `PerRegion` endpoints) each Region's state and update status in the `regionalEndpoints` field.

### Updating an endpoint
<a name="web-functions-endpoint-update"></a>

You can update the following properties on an existing endpoint:
+ `description`
+ `authType`
+ `autoDeploymentMode`
+ `revisionWeights`
+ `scalingConfig`
+ `throttleConfig`

You *cannot* update the following properties. To change these, create a new endpoint with the configuration that you want, migrate traffic to the new endpoint's domain name, and then delete the old endpoint.
+ `endpointType` (HomeRegion, MultiRegion, PerRegion)
+ `regions` (the endpoint's target Regions)

### Deleting an endpoint
<a name="web-functions-endpoint-delete"></a>

```
aws lambda-web delete-web-function-endpoint \
    --function-name {{my-web-app}} \
    --endpoint-name {{my-endpoint}}
```

When you delete an endpoint, it enters the **Deleting** state. Lambda stops routing new requests to the endpoint and retires its domain name. For a `PerRegion` endpoint, Lambda retires the domain name in each Region. Lambda never assigns a deleted endpoint's domain names to another endpoint in any account. Lambda drains in-flight requests. It lets requests that are already in progress finish and rejects new requests to the endpoint's domain names. For `MultiRegion` and `PerRegion` endpoints, Lambda removes the endpoint from all Regions. After deletion is complete, Lambda permanently removes the endpoint.

Deleting an endpoint does not delete the Web Function or its revisions. Revisions remain available for use by other endpoints.