

# Multi-Region deployment
<a name="web-functions-endpoint-replication"></a>

For **MultiRegion** and **PerRegion** endpoints, Lambda replicates runtime artifacts to all target Regions so your application can serve traffic close to end users. You manage the Web Function entirely from the home Region. Replicated resources are not visible or modifiable in replica Regions.

The following diagram shows how the control plane in the home Region prepares a revision and replicates its code and configuration to a replica Region, and how clients reach **MultiRegion** and **PerRegion** endpoints. A replica Region has no control plane. A **MultiRegion** endpoint has one global domain that routes by latency, not by Region health. For a **PerRegion** endpoint, you manage how clients reach the Regional domain in each Region, for example with Route 53 records or CloudFront. You set the endpoint type and Regions when you create the endpoint, and you can't change them later.

![A deployer manages the Web Function in the home Region, which replicates code and configuration to a replica Region. Clients reach a MultiRegion endpoint through one global domain and a PerRegion endpoint through a Regional domain in each Region.](https://docs.aws.amazon.com/lambda/latest/dg/images/web-functions-multi-region-flow.png)


**Topics**
+ [What Lambda replicates](#web-functions-endpoint-replication-what)
+ [Replica visibility](#web-functions-endpoint-replication-visibility)
+ [When replication occurs](#web-functions-endpoint-replication-trigger)
+ [How routing works](#web-functions-endpoint-replication-routing)
+ [Replication failures](#web-functions-endpoint-replication-failure)
+ [Eventual consistency](#web-functions-endpoint-replication-consistency)

## What Lambda replicates
<a name="web-functions-endpoint-replication-what"></a>

Lambda replicates the following to each target Region:
+ **Prepared code artifact** – The internal runtime artifact that Lambda derives from the versioned Amazon S3 source object.
+ **Revision configuration** – Timeout, concurrency, environment variables, and runtime settings.
+ **Resource-based policies** – Policies attached to the Web Function that grant access to it.
+ **Tags** – The tags on the Web Function.

Quotas for Web Functions apply per AWS Region. Each target Region enforces its own account quotas on the replicated endpoint. For example, execution environment scaling in a replica Region is bounded by that Region's account vCPU quota. For the account quotas, see [Account quotas](web-functions-scaling.md#web-functions-scaling-quotas).

## Replica visibility
<a name="web-functions-endpoint-replication-visibility"></a>

Replicated resources are **not visible** in replica Regions. The control plane for a Web Function is served only in its home Region, so all API requests must be sent to the home Region. This includes:
+ List, get, and describe requests for the Web Function, its revisions, and its endpoints.
+ Create, update, and delete requests for the function, revisions, and endpoint configuration.

An API request sent to a replica Region's control plane endpoint fails, regardless of where the caller is located. The replicated runtime artifacts exist only for the data plane to serve traffic.

## When replication occurs
<a name="web-functions-endpoint-replication-trigger"></a>

Replication is triggered when you create or update a **MultiRegion** or **PerRegion** endpoint. Specifically, replication occurs when:
+ You create a MultiRegion or PerRegion endpoint with revision weights pointing to a revision.
+ You update the revision weights on a MultiRegion or PerRegion endpoint to include a new revision.
+ You update other endpoint settings, such as `authType`, `scalingConfig`, or `throttleConfig`, on a MultiRegion or PerRegion endpoint.

Creating a revision alone does not trigger replication. The revision must be included in the revision weights of an endpoint that has target Regions configured. Because only **Disabled** auto-deployment mode is available for MultiRegion and PerRegion endpoints, replication is always the result of an endpoint change that you make.

## How routing works
<a name="web-functions-endpoint-replication-routing"></a>

The routing behavior depends on the endpoint type:

**MultiRegion**  
Lambda provides a single global domain name. Requests are routed using latency-based routing. Requests are routed to the Region that typically provides the lowest network latency for the caller, based on latency measurements that Route 53 collects over time. Because internet latency changes, Lambda doesn't guarantee that every request goes to the lowest-latency Region. Lambda automatically manages routes for you.

**PerRegion**  
Lambda provides a separate regional domain name in each target Region. You are responsible for managing how traffic reaches each regional domain. For example, you can configure your own Route 53 routing policy or place a CloudFront distribution in front of the regional domains.

## Replication failures
<a name="web-functions-endpoint-replication-failure"></a>

Replication can fail in a Region because of a transient service issue. If you encrypt your Web Function with a customer managed key, a missing key replica in the target Region also causes replication to fail. For the multi-Region key requirements, see [Configuring a customer managed key](web-functions-encryption.md#web-functions-encryption-key-requirements).

The effect of a replication failure depends on whether you are creating or updating the endpoint. If replication fails in any Region while Lambda creates the endpoint, the endpoint moves to the **Failed** state and is not invokable in any Region. To retry, delete the endpoint and create it again. If replication fails in a Region during an endpoint update, the failure is limited to that Region. The endpoint stays invokable, and the other Regions continue to operate normally.

When replication of a new revision fails in a Region, that Region continues serving traffic using the previous revision that was successfully deployed. The endpoint does not roll back. It continues operating with the last known good state in each Region.

You can view each Region's state and update status in the `regionalEndpoints` field of the `GetWebFunctionEndpoint` response. Each Region's entry includes:
+ `state` and `stateReason` – The Region's deployment state during endpoint creation.
+ `updateStatus` and `updateStatusReason` – The result of the most recent update (for example, a revision deployment) to that Region.

To resolve a replication failure, address the root cause (for example, create a AWS KMS key replica in the affected Region). To retry a failed endpoint update after you address the root cause, call `UpdateWebFunctionEndpoint` again. You can repeat the same settings or specify only the function name and endpoint name. Either request starts a new deployment to the target Regions. This works only while the endpoint is **Active**. If endpoint creation failed, delete the endpoint and create it again.

## Eventual consistency
<a name="web-functions-endpoint-replication-consistency"></a>

Replication of runtime artifacts is eventually consistent. Don't assume that every Region runs the new configuration until each Region's `updateStatus` in `regionalEndpoints` reports `Successful`.

Resource-based policy changes can finish propagating after code and configuration changes. During the replication window, requests in replica Regions might be evaluated against the previous version of the policy. For more information, see [Replication and eventual consistency](web-functions-permissions.md#web-functions-permissions-resource-policy-replication).