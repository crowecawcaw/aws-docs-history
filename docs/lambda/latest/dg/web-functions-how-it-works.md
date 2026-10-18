

# Core concepts
<a name="web-functions-how-it-works"></a>

Understanding the following core concepts helps you deploy and manage web applications effectively. This page covers the resource model of a Web Function, the lifecycle states of each resource, and how Lambda handles incoming HTTP requests.

The **resource model** defines the structure of a Web Function. A Web Function is the top-level resource. It contains revisions (immutable snapshots of your code and configuration) and endpoints (network entry points that route HTTP traffic to your revisions).

**Revision states** and **endpoint states** track the progress of those resources as Lambda creates, deploys, and deletes them. Monitoring these states tells you when Lambda has finished creating, deploying, or deleting a resource and helps you diagnose failures.

**Execution environments** are the isolated compute instances where your web server and application run. Each execution environment handles multiple concurrent HTTP requests. Lambda creates and removes environments automatically based on your Web Function configuration and traffic.

The following sections provide detailed information about each core concept.

## Resource model
<a name="web-functions-resource-model"></a>

A Lambda Web Function consists of three resource types in a parent-child hierarchy. The Web Function is the top-level resource. Revisions and endpoints are child resources of the Web Function. Deploying code or changing revision configuration creates a new revision. The following diagram shows a Web Function whose endpoints route traffic to its revisions.

![A Web Function contains endpoints and revisions. The prod endpoint sends 90 percent of traffic to revision 1 and 10 percent to revision 2. The staging endpoint sends all traffic to revision 2.](https://docs.aws.amazon.com/lambda/latest/dg/images/web-functions-resource-model.png)


**Web Function**  
The top-level resource that represents your web application. A Web Function has a name, an ARN, and its own lifecycle state (**Pending**, **Active**, **Failed**, or **Deleting**). It can contain revisions and endpoints; all revisions and endpoints belong to a single parent Web Function.

**Revision**  
An immutable snapshot of your application code and configuration. You create a new revision each time you change your code or revision configuration, such as the request timeout, the maximum number of concurrent requests per execution environment, or environment variables. Because revisions are immutable, you can always roll back to a previous version of your application by routing traffic to an earlier revision. You can distribute traffic between two revisions at once for canary or blue-green deployments.

**Endpoint**  
A network entry point that routes HTTP traffic to your revisions. Each endpoint has a unique domain name with TLS, an authentication type that controls access, and scaling settings that define capacity. When you create an endpoint, you choose its endpoint type, which sets its geographic scope. **HomeRegion** serves traffic from the home Region only. **MultiRegion** serves traffic from several Regions behind one global domain, which routes each request to a Region based on network latency, on a best-effort basis. **PerRegion** serves traffic from several Regions, each with its own Regional domain, and you control how clients reach each Region. A Web Function can have multiple endpoints, each with independent configuration. You configure revision weights on an endpoint to route traffic to one or two active revisions.

## Revision states
<a name="web-functions-revision-states"></a>

A revision moves through the following states during its lifecycle. You can check the current state by calling `GetWebFunctionRevision` or viewing the revision details in the Lambda console.


| State | Description | What happens next | 
| --- | --- | --- | 
| Pending | Lambda is creating the revision. This includes downloading your code from Amazon S3 and validating the configuration. | The revision transitions to Active when creation succeeds, or to Failed if an error occurs. | 
| Active | The revision was created successfully and is ready to be put behind an endpoint. | The revision remains Active until you delete it, Lambda deletes it during automatic revision cleanup (see [Revision limits and automatic cleanup](web-functions-revisions.md#web-functions-revisions-limits)), or you remove access to the source code. If Lambda loses access to the code, for example because the referenced Amazon S3 object version was deleted, the revision moves to Failed (see [Object lifecycle](web-functions-code-s3.md#web-functions-code-s3-lifecycle)). | 
| Failed | Lambda couldn't create the revision. Problems that Lambda detects when you submit the request don't produce a Failed revision. For example, if the AWS KMS key has insufficient permissions, the request fails with a client exception, and Lambda doesn't create a revision. | Check the stateReason field in the GetWebFunctionRevision response for details. Create a new revision to fix the issue. Failed revisions cannot serve traffic. | 

## Endpoint states
<a name="web-functions-endpoint-states"></a>

An endpoint has two state fields: `state` tracks the overall lifecycle, and `updateStatus` tracks endpoint updates after initial creation. You can check both by calling `GetWebFunctionEndpoint`.


| State | Description | What happens next | 
| --- | --- | --- | 
| Pending | Lambda is creating the endpoint. This includes allocating a domain name, provisioning TLS, and configuring routing. For MultiRegion and PerRegion endpoints, this also includes replicating the configuration to other AWS Regions. | The endpoint transitions to Active when creation succeeds in all target Regions, or to Failed if an error occurs. | 
| Active | The endpoint is ready to receive HTTP traffic at its domain name. Clients can send requests to the endpoint. | The endpoint remains Active. Lambda tracks subsequent endpoint updates in the updateStatus field without changing the endpoint's overall state. | 
| Failed | Creation failed. For MultiRegion and PerRegion endpoints, this can indicate a failure in one or more target Regions. | Check the stateReason field for details. For MultiRegion and PerRegion endpoints, check the regionalEndpoints entries for the state and stateReason of each Region. | 
| Deleting | Lambda is deleting the endpoint and retiring its domain name. For MultiRegion and PerRegion endpoints, Lambda removes the endpoint from all Regions. | After deletion completes, the endpoint is permanently removed. Its domain name is retired, and Lambda never assigns it to another endpoint in any account. This operation cannot be reversed. | 

For an existing endpoint, Lambda keeps `state` set to `Active` during an endpoint update. Check `updateStatus` to determine whether the most recent update is `InProgress`, `Successful`, or `Failed`. For example, when you change an endpoint's revision weights, `updateStatus` is `InProgress` while `state` stays `Active`. When the new weights are in effect, `updateStatus` changes to `Successful`.

**InProgress**  
Lambda is applying the endpoint update.

**Successful**  
The most recent endpoint update completed and is in effect.

**Failed**  
The most recent endpoint update failed. Check the `updateStatusReason` field and `regionalEndpoints` for details. For `MultiRegion` and `PerRegion` endpoints, some Regions might use the previous configuration while other Regions use the requested configuration. Correct the reported cause, and then call `UpdateWebFunctionEndpoint` again with the intended configuration to reconcile the endpoint.

The Web Function state, revision states, and endpoint states are independent. A Web Function can be in the **Active** state while one of its endpoints is still **Pending** or has **Failed**. Similarly, a revision can be **Active** even if no endpoint is currently routing traffic to it.

An **Active** revision, an **Active** endpoint, or a **Successful** endpoint update doesn't confirm that your server starts. Lambda doesn't check that your server listens when it creates or updates an endpoint to use a revision. After each deployment, send a test request and check your application logs.

## Execution environments
<a name="web-functions-execution-environments"></a>

An execution environment is an isolated compute instance where your web server and application run. When traffic arrives at your endpoint, Lambda routes requests to execution environments that are running the active revision's code.

Lambda manages execution environments automatically:

1. **Scale up** – When traffic increases, Lambda creates additional execution environments and starts your HTTP server in each one. Lambda scales up new environments ahead of demand to keep headroom, so requests rarely wait for a new environment to start (a cold start). When a Web Function scales from zero (the first request after a period of no traffic), there is a brief cold start delay while Lambda creates an execution environment. The request waits while the execution environment initializes. The request might still fail if your application does not start or if a request-rate, execution environment, or account limit applies. For details, see [Scaling behavior for Lambda Web Functions](web-functions-scaling.md).

1. **Scale down** – When traffic decreases, Lambda removes execution environments that it no longer needs, after in-flight requests finish on a best-effort basis. Lambda scales to zero environments when there is no traffic.

The number of execution environments and their concurrency are controlled by two settings:
+ **`maxEnvironments`** (endpoint setting) – The maximum number of execution environments that Lambda can create for the endpoint in each Region. This setting is optional. When it is not set, Lambda scales execution environments as needed, subject to your account quotas.
+ **`maxConcurrencyPerEnvironment`** (revision setting) – The maximum number of HTTP requests that a single execution environment handles at the same time. Valid values are 1–128. The default is 64.

Lambda sets a dynamic concurrency limit for each execution environment. This limit never exceeds `maxConcurrencyPerEnvironment`. An upper bound for endpoint concurrency is `maxEnvironments` multiplied by this dynamic limit. Actual capacity might be lower because Lambda adjusts per-environment concurrency based on resource utilization and applies endpoint and account limits. For example, suppose that you set `maxEnvironments` to 20 and `maxConcurrencyPerEnvironment` to 64. The endpoint then handles up to 1,280 concurrent requests in a Region. It handles fewer if Lambda sets the dynamic limit below 64. For guidance on these settings, see [Scaling behavior for Lambda Web Functions](web-functions-scaling.md).

## Request handling
<a name="web-functions-request-model"></a>

Your Web Function code runs as a standard HTTP server that listens on a port. Lambda sends incoming HTTP requests to your server and returns the responses to clients. You can use any Node.js web framework, middleware, or router.

The request lifecycle works as follows:

1. A client sends an HTTP request to the endpoint's domain name.

1. Lambda authenticates the request (for **IamAuth** endpoints) or passes it through (for **ApplicationManaged** endpoints).

1. Lambda routes the request to an execution environment based on the endpoint's revision weights.

1. The execution environment's HTTP server processes the request and returns a response.

1. Lambda returns the response to the client.

Each request can run for up to 900 seconds (15 minutes). You can configure the timeout from 3 to 900 seconds using the revision's `timeoutSeconds` setting. The default timeout is 30 seconds.

Each Web Function execution environment handles multiple concurrent requests, so your application code must be safe for concurrent use. For details on the concurrency model, see [Node.js execution model](web-functions-runtimes.md#web-functions-runtimes-execution-model).