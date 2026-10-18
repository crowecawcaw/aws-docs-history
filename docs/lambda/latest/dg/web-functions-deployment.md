

# Deployment patterns
<a name="web-functions-deployment"></a>

To release a new version of your AWS Lambda Web Function application, you create a new revision. Endpoints with `autoDeploymentMode` set to **LatestRevision** route all traffic to it after it becomes **Active**. Endpoints with `autoDeploymentMode` set to **Disabled** keep serving their current revisions until you update the revision weights. You control how traffic moves from the current revision to the new one using the endpoint's auto-deployment mode and revision weights. The following sections explain both auto-deployment modes, common deployment patterns (canary, blue-green, and rollback), and the rules that govern revision weights.

Changes to `autoDeploymentMode` and `revisionWeights` are asynchronous endpoint updates. Wait for `updateStatus` to become `Successful` before you evaluate the deployment or submit another endpoint update. If an update fails, `updateStatusReason` describes the cause.

The following diagram shows a canary deployment on an endpoint whose auto-deployment mode is **Disabled**. Each weight change is an asynchronous endpoint update.

1. Revision 1 starts with 100 percent of traffic.

1. You route 10 percent of traffic to revision 2 and monitor it.

1. If revision 2 passes your checks, you route all traffic to it.

1. If revision 2 fails, you set the weights back to revision 1 at 100 percent.

![Canary deployment that shifts traffic from revision 1 to revision 2, with a rollback path to revision 1.](https://docs.aws.amazon.com/lambda/latest/dg/images/web-functions-deployment-patterns.png)


## Auto-deployment modes
<a name="web-functions-deployment-modes"></a>

The `autoDeploymentMode` setting on an endpoint controls whether Lambda automatically routes traffic to new revisions when you deploy. You set this when you create the endpoint, and you can change it on an existing endpoint.

If you omit `autoDeploymentMode`, it defaults to `Disabled`. `LatestRevision` is supported only for `HomeRegion` endpoints, so `MultiRegion` and `PerRegion` endpoints always use `Disabled`. When using `Disabled`, you set `revisionWeights` on the endpoint, as described in [Revision weights](#web-functions-deployment-weights).

**LatestRevision**  
Each time a new revision becomes **Active**, Lambda routes 100% of the endpoint's traffic to it. You do not need to update revision weights, and you can't set revision weights while the endpoint is in this mode. Use this mode for development and staging environments where you want automatic deployment without manual intervention.

**Disabled**  
Lambda does not change traffic routing when you create a new revision. You control traffic routing manually by setting revision weights. Use this mode for production environments where you want to control the rollout of new revisions with canary or blue-green deployment patterns.

**To change the auto-deployment mode (AWS CLI)**

1. Use the AWS Command Line Interface (AWS CLI) to update the endpoint and disable automatic deployment.

   ```
   aws lambda-web update-web-function-endpoint \
       --function-name {{my-web-app}} \
       --endpoint-name {{my-endpoint}} \
       --auto-deployment-mode Disabled
   ```

1. Wait until the endpoint update is complete.

   ```
   aws lambda-web wait web-function-endpoint-updated \
       --function-name {{my-web-app}} \
       --endpoint-name {{my-endpoint}}
   ```

### Switching between modes
<a name="web-functions-deployment-modes-switching"></a>

When you switch from **LatestRevision** to **Disabled** without specifying revision weights, the current traffic routing remains unchanged after the update succeeds. The revision that the endpoint routed traffic to before the update continues to receive 100% of traffic, even after you create newer revisions. It keeps that traffic until you update the revision weights. You can also switch the mode and set revision weights in the same `UpdateWebFunctionEndpoint` request.

When you switch from **Disabled** to **LatestRevision**, Lambda updates the endpoint to route 100% of traffic to the latest revision. The latest revision must be **Active**. If it is **Pending** or **Failed**, the request fails with a conflict error. After the update succeeds, the previously configured revision weights no longer apply.

## Revision weights
<a name="web-functions-deployment-weights"></a>

When the auto-deployment mode is **Disabled**, you control traffic routing by assigning weights to revisions. Lambda distributes traffic between revisions in proportion to their weights.

Revision weights are a setting on the endpoint (the `revisionWeights` property), which you change with `UpdateWebFunctionEndpoint`. They are not a setting on the revision.

Revision weights follow these rules:
+ Each weight is an integer from 1 to 100.
+ The weights in a request must sum to exactly 100.
+ Each revision can appear only once in the weights.
+ Each revision in the weights must be in the **Active** state when you set the weights. Otherwise, the API rejects the request.
+ An endpoint routes traffic to a maximum of two revisions at the same time.
+ No weight has a default value. To route all traffic to one revision, specify only that revision with a weight of 100. A revision that isn't in the weights receives no traffic from that endpoint.

Revision identifiers are generated by Lambda when you create a revision. To find revision identifiers for your Web Function, use the following command:

```
aws lambda-web list-web-function-revisions \
    --function-name {{my-web-app}}
```

The response lists revisions in order from newest to oldest, including their identifiers, creation timestamps, and current state.

## Deployment patterns
<a name="web-functions-deployment-patterns"></a>

The following deployment patterns use revision weights to control how traffic moves from your current revision to a new revision. These patterns require the endpoint's auto-deployment mode (the `autoDeploymentMode` endpoint setting) to be **Disabled**. The endpoint that the `aws lambda-web deploy` command creates uses **LatestRevision**. To use these patterns on that endpoint, first switch it to **Disabled**, as shown in [Auto-deployment modes](#web-functions-deployment-modes).

### Canary deployment
<a name="web-functions-deployment-canary"></a>

A canary deployment sends a small percentage of traffic to the new revision so you can monitor for errors before routing all traffic. If the new revision has problems, only a small portion of requests are affected.

**To perform a canary deployment (AWS CLI)**

1. Create a new revision with your updated code.

   ```
   aws lambda-web create-web-function-revision \
       --function-name {{my-web-app}} \
       --build-config '{
         "codeConfig": {
           "s3Object": { "bucket": "{{my-bucket}}", "key": "{{my-app-v2.zip}}" }
         },
         "runtimeConfig": { "runtime": "nodejs24.x" }
       }' \
       --service-config '{
         "executionRoleArn": "arn:aws:iam::{{111122223333}}:role/{{my-web-function-role}}"
       }'
   ```

   Note the revision identifier in the response.

   A new revision doesn't copy settings from the current revision. Any `serviceConfig` setting that you omit takes its default value, for example a `timeoutSeconds` of 30 and no environment variables. Include every setting that the current revision uses, such as `environmentVariables`, `timeoutSeconds`, `maxConcurrencyPerEnvironment`, and `telemetryConfig`. To see the current revision's configuration, run `aws lambda-web get-web-function-revision`.

1. Wait until the new revision is **Active**. The API rejects revision weights that reference a revision that is not **Active**.

   ```
   aws lambda-web wait web-function-revision-active \
       --function-name {{my-web-app}} \
       --revision-id {{rev-def45}}
   ```

1. Route 10% of traffic to the new revision and 90% to the current revision.

   ```
   aws lambda-web update-web-function-endpoint \
       --function-name {{my-web-app}} \
       --endpoint-name {{my-endpoint}} \
       --revision-weights '[{"revisionId": "{{rev-abc12}}", "weight": 90}, {"revisionId": "{{rev-def45}}", "weight": 10}]'
   ```

1. Wait until the endpoint update is complete.

   ```
   aws lambda-web wait web-function-endpoint-updated \
       --function-name {{my-web-app}} \
       --endpoint-name {{my-endpoint}}
   ```

1. Monitor the new revision through application logs or custom metrics. Include a build or revision identifier that you control in them. Web Function metrics don't include a revision dimension. As a result, they can't separate canary errors from errors on the current revision. For details, see [Using CloudWatch metrics with Lambda Web Functions](web-functions-monitoring-metrics.md). If the canary meets the error and latency thresholds that you defined before the rollout, increase its weight.

   ```
   aws lambda-web update-web-function-endpoint \
       --function-name {{my-web-app}} \
       --endpoint-name {{my-endpoint}} \
       --revision-weights '[{"revisionId": "{{rev-abc12}}", "weight": 50}, {"revisionId": "{{rev-def45}}", "weight": 50}]'
   ```

1. Wait until the endpoint update is complete.

   ```
   aws lambda-web wait web-function-endpoint-updated \
       --function-name {{my-web-app}} \
       --endpoint-name {{my-endpoint}}
   ```

1. When you are confident the new revision is healthy, route all traffic to it.

   ```
   aws lambda-web update-web-function-endpoint \
       --function-name {{my-web-app}} \
       --endpoint-name {{my-endpoint}} \
       --revision-weights '[{"revisionId": "{{rev-def45}}", "weight": 100}]'
   ```

1. Wait until the endpoint update is complete.

   ```
   aws lambda-web wait web-function-endpoint-updated \
       --function-name {{my-web-app}} \
       --endpoint-name {{my-endpoint}}
   ```

### Blue-green deployment
<a name="web-functions-deployment-blue-green"></a>

A blue-green deployment keeps the current revision serving traffic while you validate the new revision, and then switches all traffic to the new revision in one endpoint update. The following procedure validates with an even traffic split. To validate without production traffic, use a separate test endpoint, as described in [Deployment considerations](#web-functions-deployment-considerations).

**To perform a blue-green deployment (AWS CLI)**

1. Create a new revision with your updated code, and wait until it is **Active**. Use the same commands shown in the preceding canary deployment procedure.

1. Split traffic evenly between the two revisions.

   ```
   aws lambda-web update-web-function-endpoint \
       --function-name {{my-web-app}} \
       --endpoint-name {{my-endpoint}} \
       --revision-weights '[{"revisionId": "{{rev-abc12}}", "weight": 50}, {"revisionId": "{{rev-def45}}", "weight": 50}]'
   ```

1. Wait until the endpoint update is complete.

   ```
   aws lambda-web wait web-function-endpoint-updated \
       --function-name {{my-web-app}} \
       --endpoint-name {{my-endpoint}}
   ```

1. Monitor both revisions through application logs or custom metrics. Include a build or revision identifier that you control in them. When the new revision meets the health criteria that you defined before the rollout, route all traffic to it.

   ```
   aws lambda-web update-web-function-endpoint \
       --function-name {{my-web-app}} \
       --endpoint-name {{my-endpoint}} \
       --revision-weights '[{"revisionId": "{{rev-def45}}", "weight": 100}]'
   ```

1. Wait until the endpoint update is complete.

   ```
   aws lambda-web wait web-function-endpoint-updated \
       --function-name {{my-web-app}} \
       --endpoint-name {{my-endpoint}}
   ```

### Rolling back
<a name="web-functions-deployment-rollback"></a>

If you detect problems with a new revision (high error rates, increased latency), you can roll back with a single endpoint update that routes all traffic to the previous known-good revision.

**Rolling back in LatestRevision mode**  
While an endpoint's auto-deployment mode is **LatestRevision**, a request that sets only revision weights fails. The following procedure sets the auto-deployment mode to **Disabled** and the revision weights in the same request, so it works in either mode.  
The endpoint then stays in **Disabled** mode until you change it.

**To roll back to a previous revision (AWS CLI)**

1. Update the endpoint to route 100% of traffic to the known-good revision and set the auto-deployment mode to **Disabled**.

   ```
   aws lambda-web update-web-function-endpoint \
       --function-name {{my-web-app}} \
       --endpoint-name {{my-endpoint}} \
       --auto-deployment-mode Disabled \
       --revision-weights '[{"revisionId": "{{rev-abc12}}", "weight": 100}]'
   ```

1. Wait until the endpoint update is complete.

   ```
   aws lambda-web wait web-function-endpoint-updated \
       --function-name {{my-web-app}} \
       --endpoint-name {{my-endpoint}}
   ```

After the update succeeds, Lambda stops routing new requests to the problematic revision. In-flight requests on that revision finish normally. For more information about endpoint update status, see [Endpoint states](web-functions-how-it-works.md#web-functions-endpoint-states).

If the revision you roll back to has few or no running execution environments, Lambda scales it up as traffic shifts to it. Requests can wait while execution environments initialize, which increases latency. Requests can still fail because of startup failures, the endpoint's rate limit or maximum environments, or the account vCPU quota. Some of these failures return HTTP 429 responses.

## Deployment considerations
<a name="web-functions-deployment-considerations"></a>

What triggers a new revision?  
Lambda creates a new revision when you call `CreateWebFunctionRevision`. This includes deploying new application code and changing configuration settings such as timeout, concurrency, or environment variables. Each change produces an immutable revision.

Can I test a new revision before routing production traffic to it?  
Yes. You can only invoke a revision through an endpoint, so there are two approaches:  
+ **Dedicated test endpoint** – Create a separate endpoint for testing. Route traffic to the new revision on the test endpoint first (by setting the test endpoint's revision weights), validate it, and then update the production endpoint's weights to include the new revision.
+ **Minimal weight** – Assign the new revision a weight of 1% on the production endpoint. This sends a small fraction of production traffic to the new revision so you can monitor for errors with minimal customer impact.

What happens to revisions that are not in the revision weights?  
A revision that is not in an endpoint's revision weights receives no traffic from that endpoint. Another endpoint of the same Web Function can still route to it. The revision stays **Active** until you delete it or until automatic cleanup removes it. It moves to **Failed** if Lambda loses access to its Amazon S3 object. For automatic cleanup, see [Revision limits and automatic cleanup](web-functions-revisions.md#web-functions-revisions-limits).

How do I identify which revision is newest?  
Call `ListWebFunctionRevisions`. The response lists revisions in descending order of `createdAt`, so the first revision in the list is the newest.

Can I delete an endpoint while it is routing traffic?  
Yes. When you delete an endpoint, Lambda stops routing new requests to that endpoint, and requests to the endpoint's domain name are rejected after the deletion takes effect. The revisions themselves are not affected and can still be used by other endpoints.

Can I delete a revision while it is receiving traffic?  
No. If any endpoint routes traffic to the revision, including when the `regionalEndpoints` property of a `MultiRegion` or `PerRegion` endpoint references the revision, the `DeleteWebFunctionRevision` request fails with a conflict error. To delete the revision, first update the endpoint's revision weights to remove it from traffic routing on every endpoint, then delete it. Because Lambda blocks deletion while a revision has a weight assigned, deleting a revision never changes the traffic distribution of an endpoint.