

# HTTP targets: API Gateway and API destinations
<a name="eb-custom-bus-target-http"></a>

To call an HTTP endpoint, set `TargetArn` either to an API Gateway execute-api ARN, such as `arn:aws:execute-api:us-east-1:111122223333:a1b2c3d4e5/prod/POST/orders`, or to an EventBridge API destination ARN for any other HTTPS endpoint with its connection's credentials, and add `HttpParameters`. The request body is the transformed event.

## Parameters
<a name="eb-custom-bus-target-http-parameters"></a>


| Parameter | What it sets | 
| --- | --- | 
| PathParameterValues | Values for path variables in the endpoint, in order | 
| HeaderParameters | HTTP headers to add | 
| QueryStringParameters | Query string parameters to add | 
| InvocationTimeoutSeconds | How long EventBridge waits for the response, 1 to 30 seconds, default 30 | 

## Delivery role
<a name="eb-custom-bus-target-http-role"></a>

For an API Gateway endpoint, the role needs `execute-api:Invoke` on the method's ARN. For an API destination, the role needs `events:InvokeApiDestination` on the API destination.

## Batching and payload
<a name="eb-custom-bus-target-http-batching"></a>

One HTTP request carries the batch as a JSON array unless `MaxBatchSize` is 1. A response outside the 2xx range is a failed delivery. See [Batching deliveries to a target](eb-custom-bus-batching.md).