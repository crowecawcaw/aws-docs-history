# Invoking Lambda functions with tenant isolation

When invoking a function that has tenant isolation enabled, you must provide a `tenant-id` parameter.
This parameter ensures that your function invocation is processed in an execution environment dedicated to that specific tenant.

## Invoking functions with tenant isolation (AWS CLI)

**Synchronous invocation**

For synchronous invocations, add the `--tenant-id` parameter to your [Invoke](../api/API_Invoke.md "../api/API_Invoke.md") command:

```
`aws lambda invoke \
 --function-name `image-analysis` \
 --tenant-id `blue` \
 response.json`
```

**Asynchronous invocation**

For asynchronous invocations, include both the `--tenant-id` and `--invocation-type Event` parameters:

```
`aws lambda invoke \
 --function-name `image-analysis` \
 --tenant-id `blue` \
 --invocation-type Event \
 response.json`
```

## Invoking functions with tenant isolation (API)

When using the [Invoke](../api/API_Invoke.md "../api/API_Invoke.md") API action directly, include the tenant identifier using the `X-Amzn-Tenant-Id` parameter in your request.

**Example API request**

```
POST /2015-03-31/functions/`image-analysis`/invocations HTTP/1.1
Host: lambda.`us-east-1`.amazonaws.com
Content-Type: application/json
Authorization: AWS4-HMAC-SHA256 Credential=...
`X-Amz-Tenant-Id:` `blue`

{
    "key1": "value1",
    "key2": "value2"
}
```

## Invoking functions with tenant isolation (API Gateway)

When using API Gateway to trigger tenant-isolated Lambda functions, you can pass the tenant identifier via query parameters or request headers, as shown below:

**Using query parameters**

Configure your API Gateway integration to pass the tenant ID as a query parameter:

```
GET /api/process?tenant-id=`blue`&data=`sample` HTTP/1.1
Host: `your-api-id`.execute-api.`us-east-1`.amazonaws.com
```

**Using request headers**

You can also pass the tenant ID through custom headers:

```
POST /api/process HTTP/1.1
Host: `your-api-id`.execute-api.`us-east-1`.amazonaws.com
Content-Type: application/json
`X-Tenant-ID`: `blue`

{
    "data": "sample payload"
}
```

## Invoking functions with tenant isolation (SDK)

When using AWS SDKs to invoke tenant-isolated functions, include the tenant identifier in your invocation request.

Python

```
import boto3
import json

lambda_client = boto3.client('lambda')

response = lambda_client.invoke(
    FunctionName='`image-analysis`',
    TenantId='`blue`',
    Payload=json.dumps({
        'key1': 'value1',
        'key2': 'value2'
    })
)

result = json.loads(response['Payload'].read())
```

Node.js

```
const AWS = require('aws-sdk');
const lambda = new AWS.Lambda();

const params = {
    FunctionName: '`image-analysis`',
    TenantId: '`blue`',
    Payload: JSON.stringify({
        key1: 'value1',
        key2: 'value2'
    })
};

lambda.invoke(params, (err, data) => {
    if (err) {
        console.error(err);
    } else {
        const result = JSON.parse(data.Payload);
        console.log(result);
    }
});
```

Java

```
import software.amazon.awssdk.services.lambda.LambdaClient;
import software.amazon.awssdk.services.lambda.model.InvokeRequest;
import software.amazon.awssdk.services.lambda.model.InvokeResponse;
import software.amazon.awssdk.core.SdkBytes;

public class TenantIsolationExample {

    public static void main(String[] args) {
        LambdaClient lambdaClient = LambdaClient.create();

        String payload = "{\"key1\": \"value1\", \"key2\": \"value2\"}";

        InvokeRequest request = InvokeRequest.builder()
                .functionName("`image-analysis`")
                .tenantId("`blue`")
                .payload(SdkBytes.fromUtf8String(payload))
                .build();

        InvokeResponse response = lambdaClient.invoke(request);
    }
}
```
