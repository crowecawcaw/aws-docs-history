

# Route asynchronous inference requests through an inference router

Use `InvokeInferenceRouterAsync` to send requests to asynchronous inference endpoints through an inference router. For information about asynchronous endpoints, see [Asynchronous inference](async-inference.md). For the AWS Regions where asynchronous routing is available, see [Tools and Regions](inference-router.md#inference-router-tools).

## Configure an asynchronous routing target
<a name="inference-router-async-config"></a>

Add `AsyncInferenceConfig` to the routing target. The following rules apply:
+ Every destination must be an asynchronous endpoint. Inference components and real-time endpoints aren't supported, and a real-time routing target can't contain an asynchronous endpoint. `CreateInferenceRouter` and `UpdateInferenceRouter` reject a destination of the wrong mode. If SageMaker AI can't check an endpoint, for example because it isn't found or can't be read in time, the endpoint is accepted, and requests to it fail if it's the wrong mode.
+ The input, `S3OutputPath`, and `S3FailurePath` buckets must be in the router's AWS Region and owned by the router's AWS account. `CreateInferenceRouter` and `UpdateInferenceRouter` don't check the owner. A request whose input or output bucket is owned by another account fails, even if the bucket policy allows access.

```json
{
  "Name": "{{my-async-model}}",
  "Destinations": [
    { "ResourceArn": "arn:aws:sagemaker:us-west-2:{{111122223333}}:endpoint/{{my-async-usw2}}" },
    { "ResourceArn": "arn:aws:sagemaker:us-east-1:{{111122223333}}:endpoint/{{my-async-use1}}" }
  ],
  "AsyncInferenceConfig": {
    "OutputConfig": {
      "S3OutputPath": "s3://{{amzn-s3-demo-bucket}}/output/",
      "S3FailurePath": "s3://{{amzn-s3-demo-bucket}}/failure/",
      "NotificationConfig": {
        "ErrorTopic": "arn:aws:sns:us-west-2:{{111122223333}}:{{my-error-topic}}"
      }
    },
    "ClientConfig": { "MaxTimeInBacklogSeconds": 900 }
  }
}
```

In the example, replace the following values:
+ {{my-async-model}} – the name of your routing target.
+ {{111122223333}} – your AWS account ID.
+ {{my-async-usw2}} and {{my-async-use1}} – the names of your asynchronous endpoints.
+ {{amzn-s3-demo-bucket}} – the name of your Amazon S3 bucket.
+ {{my-error-topic}} – the name of your Amazon SNS topic.

`MaxTimeInBacklogSeconds` (60–21,600 seconds, default 900) is how long a request can wait at one destination before the router moves it to another destination. You can also set `KmsKeyId` in `OutputConfig`, and `SuccessTopic` in `NotificationConfig`. If any destination is in another Region or account, specify `KmsKeyId` as a key ARN or alias ARN. The router publishes one notification for each request: to `SuccessTopic` when the request completes, or to `ErrorTopic` when it fails or can't be placed on any destination.

By default, the router uses destinations in the router's Region first, and then destinations in other Regions in the order that you list them (`LocalRegionFirst`). To choose destinations by instance type first and by Region second, set `RoutingPreference` to `InstancePoolOrder`. This value is available only for asynchronous routing targets. With this setting, every destination must be an endpoint that lists the same two or more instance types, each with a different priority, in the same priority order.

To use it, add the following field to the routing target from the previous example.

```json
"RoutingPreference": "InstancePoolOrder"
```

## Permissions for asynchronous requests
<a name="inference-router-async-permissions"></a>

The caller needs `sagemaker:InvokeInferenceRouterAsync` on the router and `sagemaker:InvokeEndpointAsync` on every destination. The caller also needs `s3:PutObject` on the `S3FailurePath`, `sns:Publish` on the routing target's topics, and, if you set `KmsKeyId`, `kms:GenerateDataKey` on that key.

Each destination endpoint's execution role reads the input and writes the output. It needs `s3:GetObject` on the input, `s3:PutObject` on the `S3OutputPath`, and, if you set `KmsKeyId`, `kms:GenerateDataKey` on that key.

## Destinations in other accounts
<a name="inference-router-async-cross-account"></a>

An asynchronous routing target can include endpoints in other accounts. Set up the endpoint policy as described in [Route requests to endpoints in other AWS accounts](inference-router-cross-account.md). The following also apply:
+ SageMaker AI checks the mode of an endpoint in another account with your credentials, so the check works only if both your IAM policy and the endpoint policy allow `sagemaker:DescribeEndpoint`. Otherwise the endpoint is accepted unchecked.
+ The destination's execution role reads your input and writes the output, so your bucket policy must allow it the Amazon S3 permissions in [Permissions for asynchronous requests](#inference-router-async-permissions).
+ Set the output bucket's Object Ownership to *Bucket owner enforced* (the default for new buckets). If ACLs are enabled on the bucket, the destination's account owns the output objects and you can't read them.
+ If you set `KmsKeyId`, the key policy must allow the destination's execution role `kms:GenerateDataKey`. Without `KmsKeyId`, the output uses your bucket's default encryption, so a bucket policy that requires the `x-amz-server-side-encryption` header denies it.

## Invoke asynchronously
<a name="inference-router-async-invoke"></a>

Upload the input to Amazon S3 in the router's Region, then call `InvokeInferenceRouterAsync`.

```bash
aws sagemaker-inference-router-runtime invoke-inference-router-async \
    --region {{us-west-2}} \
    --inference-router-name {{my-router}} \
    --routing-target-name {{my-async-model}} \
    --input-location s3://{{amzn-s3-demo-bucket}}/input/{{request.json}} \
    --content-type application/json
```

In the command, replace the following values:
+ {{us-west-2}} – the router's Region.
+ {{my-router}} – the name of your inference router.
+ {{my-async-model}} – the name of your asynchronous routing target.
+ {{amzn-s3-demo-bucket}} and {{request.json}} – the Amazon S3 bucket and object key of your input.

The following is example output.

```json
{
    "InferenceId": "{{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}",
    "OutputLocation": "s3://{{amzn-s3-demo-bucket}}/output/{{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}.out",
    "FailureLocation": "s3://{{amzn-s3-demo-bucket}}/failure/{{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}-error.out"
}
```

The locations don't change if the request moves to another destination. Asynchronous responses don't include the routed resource or routing reason headers.

You can also send the following optional inputs:
+ `InferenceId`
+ `Accept`
+ `CustomAttributes`
+ `S3OutputPathExtension`
+ `Filename`
+ `RequestTTLSeconds` – the request's time to live (TTL), 60–21,600 seconds (default 21,600)
+ `InvocationTimeoutSeconds` – 1–3,600 seconds (default 900)

The destination's asynchronous inference limits apply to the input. For the permissions that the caller and each destination need, see [Permissions for asynchronous requests](#inference-router-async-permissions).

## How asynchronous requests move between destinations
<a name="inference-router-async-failover"></a>
+ The router places a new request on the first destination in its order (by default, the local Region first, then the order that you list them). Destinations that recently returned server errors, or that have been waiting for capacity for longer than `MaxTimeInBacklogSeconds`, go to the end of the order.
+ If a destination refuses a new request, for example because it throttles or denies it, the router tries the next one.
+ If a destination doesn't start a request within `MaxTimeInBacklogSeconds`, the router moves it to another destination. A shorter backlog, or slow processing, doesn't move it.
+ After your model starts processing a request, the request doesn't move, even if it fails or times out.
+ If no destination can take the request before `RequestTTLSeconds` runs out, or every destination has been tried, the router writes a failure object to the `FailureLocation` and publishes to the routing target's `ErrorTopic`.

If a destination endpoint has its own notification topics, it also publishes to them.

`CrossRegionTrafficConfig` doesn't apply to asynchronous endpoints. To see where a request ran, check the `async.placement.attempts` metric or the destination's `InvokeEndpointAsync` CloudTrail events.