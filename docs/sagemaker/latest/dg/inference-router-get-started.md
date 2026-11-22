

# Get started with inference routers

In this tutorial, you create an inference router that routes between endpoints in `us-west-2` and `us-east-1`, invoke it with the AWS CLI and the AWS SDK for Python (Boto3), and then delete it.

## Prerequisites
<a name="inference-router-prereqs"></a>
+ A version of the AWS CLI or an AWS SDK that supports inference routers. For more information, see [Tools and Regions](inference-router.md#inference-router-tools).
+ An IAM identity with permissions to manage the router, and to invoke the router and every destination (`sagemaker:InvokeEndpoint`). For the reason, see [How the router authorizes requests to destinations](inference-router-security.md#inference-router-security-confused-deputy). The following policy is an example.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ManageAndInvokeRouter",
      "Effect": "Allow",
      "Action": [
        "sagemaker:CreateInferenceRouter",
        "sagemaker:DescribeInferenceRouter",
        "sagemaker:UpdateInferenceRouter",
        "sagemaker:DeleteInferenceRouter",
        "sagemaker:InvokeInferenceRouter"
      ],
      "Resource": "arn:aws:sagemaker:us-west-2:{{111122223333}}:inference-router/{{my-router}}"
    },
    {
      "Sid": "ListRouters",
      "Effect": "Allow",
      "Action": "sagemaker:ListInferenceRouters",
      "Resource": "*"
    },
    {
      "Sid": "InvokeAndDescribeDestinations",
      "Effect": "Allow",
      "Action": [
        "sagemaker:InvokeEndpoint",
        "sagemaker:DescribeEndpoint",
        "sagemaker:DescribeInferenceComponent"
      ],
      "Resource": [
        "arn:aws:sagemaker:us-west-2:{{111122223333}}:endpoint/{{my-endpoint-usw2}}",
        "arn:aws:sagemaker:us-east-1:{{111122223333}}:endpoint/{{my-endpoint-use1}}"
      ]
    }
  ]
}
```

Without `DescribeEndpoint` or `DescribeInferenceComponent` on a destination, routing still works, but `DescribeInferenceRouter` shows the destination's `RoutingStatus` as `Unknown`. If you tag the router when you create it, you also need `sagemaker:AddTags`. For asynchronous routing targets, also allow `sagemaker:InvokeInferenceRouterAsync` on the router and `sagemaker:InvokeEndpointAsync` on every destination. For more information, see [Route asynchronous inference requests through an inference router](inference-router-async.md).

## Create and use an inference router
<a name="inference-router-get-started-steps"></a>

**To create, invoke, update, and delete an inference router**

1. <a name="inference-router-deploy-endpoints"></a>**Deploy the same model on an endpoint in two Regions.**

   This example uses {{my-endpoint-usw2}} and {{my-endpoint-use1}}. For instructions on deploying models to real-time endpoints, see [Deploy models for real-time inference](realtime-endpoints-deploy-models.md).

   1. Create a real-time endpoint in `us-west-2`.

   1. Create a real-time endpoint with the same model in `us-east-1`.

   1. Wait until both endpoints are `InService`.

   Both endpoints must serve the same model with the same request and response format. The router doesn't check this.

1. <a name="inference-router-routing-targets"></a>**Save the following routing target as `routing-targets.json`.**

   It lists both endpoints as destinations.

   ```json
   [
     {
       "Name": "{{my-model}}",
       "Destinations": [
         { "ResourceArn": "arn:aws:sagemaker:us-west-2:{{111122223333}}:endpoint/{{my-endpoint-usw2}}" },
         { "ResourceArn": "arn:aws:sagemaker:us-east-1:{{111122223333}}:endpoint/{{my-endpoint-use1}}" }
       ]
     }
   ]
   ```

1. <a name="inference-router-create"></a>**Create the router in `us-west-2`.**

   ```bash
   aws sagemaker create-inference-router \
       --region us-west-2 \
       --inference-router-name {{my-router}} \
       --routing-targets file://{{routing-targets.json}}
   ```

   The response contains the router's Amazon Resource Name (ARN) in `InferenceRouterArn`.

1. <a name="inference-router-describe"></a>**Check the router status.**

   ```bash
   aws sagemaker describe-inference-router \
       --region us-west-2 \
       --inference-router-name {{my-router}}
   ```

   The following is example output.

   ```json
   {
       "InferenceRouterName": "{{my-router}}",
       "InferenceRouterArn": "arn:aws:sagemaker:us-west-2:{{111122223333}}:inference-router/{{my-router}}",
       "Status": "InService",
       "RoutingTargets": [
           {
               "Name": "{{my-model}}",
               "Destinations": [
                   {
                       "ResourceArn": "arn:aws:sagemaker:us-west-2:{{111122223333}}:endpoint/{{my-endpoint-usw2}}",
                       "RoutingStatus": "Routable"
                   },
                   {
                       "ResourceArn": "arn:aws:sagemaker:us-east-1:{{111122223333}}:endpoint/{{my-endpoint-use1}}",
                       "RoutingStatus": "Routable"
                   }
               ]
           }
       ],
       "CreationTime": "2026-11-16T10:00:00.000Z",
       "LastModifiedTime": "2026-11-16T10:00:00.000Z"
   }
   ```

   Wait until `Status` is `InService`. If it's `Failed`, see `StatusReason`. For the meaning of `RoutingStatus`, see [How the router chooses a destination](inference-router.md#inference-router-how).

   To list the routers in a Region, run `aws sagemaker list-inference-routers --region us-west-2`.

1. <a name="inference-router-invoke"></a>**Invoke the router.**

   Call `InvokeInferenceRouter` with the router name and the routing target name. The router passes the request body to the destination unchanged.

   ```bash
   aws sagemaker-inference-router-runtime invoke-inference-router \
       --region us-west-2 \
       --inference-router-name {{my-router}} \
       --routing-target-name {{my-model}} \
       --content-type application/json \
       --body fileb://{{input.json}} \
       {{output.json}}
   ```

   The model's response is written to `output.json`. The command prints the destination that served the request and the routing reason.

   ```json
   {
       "ContentType": "application/json",
       "InvokedProductionVariant": "{{AllTraffic}}",
       "InvokedRoutedResourceArn": "arn:aws:sagemaker:us-west-2:{{111122223333}}:endpoint/{{my-endpoint-usw2}}",
       "RoutingReason": "local-preferred"
   }
   ```

   The following example uses Boto3.

   ```py
   import boto3
   from botocore.config import Config
   
   config = Config(
       read_timeout=170,
       retries={"total_max_attempts": 2, "mode": "standard"},
   )
   
   runtime = boto3.client(
       "sagemaker-inference-router-runtime", region_name="us-west-2", config=config
   )
   
   response = runtime.invoke_inference_router(
       InferenceRouterName="{{my-router}}",
       RoutingTargetName="{{my-model}}",
       ContentType="application/json",
       Body=b'{"inputs": "Hello"}',
   )
   
   print(response["InvokedRoutedResourceArn"], response["RoutingReason"])
   print(response["Body"].read())
   ```

   Your model has up to 60 seconds per attempt, the same limit as `InvokeEndpoint`. Because the router can retry once on another destination, set your client read timeout to at least 170 seconds and limit SDK retries, as in the example. For more information, see [Quotas and limits](inference-router.md#inference-router-quotas). For retry settings, see [Configure client retries](inference-router-troubleshoot.md#inference-router-troubleshoot-retries).

   You can also send `Accept`, `CustomAttributes`, and `InferenceId`. The router passes `CustomAttributes` to the destination, and returns the destination's `CustomAttributes` in the response.

1. <a name="inference-router-update"></a>**(Optional) Update the router.**

   `UpdateInferenceRouter` replaces the complete list of routing targets. To add or remove a destination, send every routing target that you want to keep. For example, to add an endpoint in `us-east-2`, change `routing-targets.json` to the following.

   ```json
   [
     {
       "Name": "{{my-model}}",
       "Destinations": [
         { "ResourceArn": "arn:aws:sagemaker:us-west-2:{{111122223333}}:endpoint/{{my-endpoint-usw2}}" },
         { "ResourceArn": "arn:aws:sagemaker:us-east-1:{{111122223333}}:endpoint/{{my-endpoint-use1}}" },
         { "ResourceArn": "arn:aws:sagemaker:us-east-2:{{111122223333}}:endpoint/{{my-endpoint-use2}}" }
       ]
     }
   ]
   ```

   1. Add {{my-endpoint-use2}} to the `Resource` list of the caller's IAM policy.

   1. Update the router.

      ```bash
      aws sagemaker update-inference-router \
          --region us-west-2 \
          --inference-router-name {{my-router}} \
          --routing-targets file://{{routing-targets.json}}
      ```

   Changes apply to new requests within about 2 minutes.

1. <a name="inference-router-list-delete"></a>**Delete the router.**

   Deleting a router doesn't delete its destinations.

   ```bash
   aws sagemaker delete-inference-router \
       --region us-west-2 \
       --inference-router-name {{my-router}}
   ```

1. <a name="inference-router-delete-endpoints"></a>**Delete the endpoints.**
**Important**  
Endpoints continue to incur charges until you delete them.

   For instructions, see [Delete Endpoints and Resources](realtime-endpoints-delete-resources.md).

## Move an application from InvokeEndpoint
<a name="inference-router-migrate"></a>

To move an application that calls `InvokeEndpoint` to an inference router, do the following:

1. Deploy the same model, with the same container and request and response format, as a destination in each Region.

1. Give callers `sagemaker:InvokeInferenceRouter` on the router and keep `sagemaker:InvokeEndpoint` on every destination.

1. Change the client from `sagemaker-runtime` to `sagemaker-inference-router-runtime`, and call `InvokeInferenceRouter` with `InferenceRouterName` and `RoutingTargetName` instead of `EndpointName`. The body, `ContentType`, `Accept`, `CustomAttributes`, and `InferenceId` work as with `InvokeEndpoint`.

1. Set the client read timeout to at least 170 seconds and at most 2 attempts. Your model still has up to 60 seconds per request.

1. Remove `TargetVariant`, `TargetModel`, `InferenceComponentName`, and `SessionId`, and don't use response streaming; the router doesn't support them. To target an inference component, add the component as a destination.

1. Handle the router's own errors: `ThrottlingException` (429) when you exceed the router's request rate, and `ServiceUnavailableException` (503). Read `InvokedRoutedResourceArn` to see which destination served the request.

For asynchronous requests, use `InvokeInferenceRouterAsync`. The input must be in Amazon S3 in the router's Region, and the output and failure locations come from the routing target, not from the endpoint. For more information, see [Route asynchronous inference requests through an inference router](inference-router-async.md).

## Next steps
<a name="inference-router-get-started-next"></a>

For more information, see the following topics:
+ [Route requests to endpoints in other AWS accounts](inference-router-cross-account.md)
+ [Route asynchronous inference requests through an inference router](inference-router-async.md)
+ [Monitor inference routers with Amazon CloudWatch and AWS CloudTrail](inference-router-monitor.md)
+ [Troubleshoot inference routers](inference-router-troubleshoot.md)