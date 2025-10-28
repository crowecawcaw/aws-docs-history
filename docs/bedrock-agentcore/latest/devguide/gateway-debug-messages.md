# Turn on debugging messages

While your gateway is in development, you can turn on debugging messages to return details on target configuration issues, including lambda function errors, egress authorizer errors, target specification parameter validation errors.

To turn on debugging messages, set the `exceptionLevel` value as `DEBUG` when you make a [CreateGateway](../../../bedrock-agentcore-control/latest/APIReference/API_CreateGateway.md "../../../bedrock-agentcore-control/latest/APIReference/API_CreateGateway.md") or [UpdateGateway](../../../bedrock-agentcore-control/latest/APIReference/API_UpdateGateway.md "../../../bedrock-agentcore-control/latest/APIReference/API_UpdateGateway.md") request. After turning on debugging messages, if an issue occurs when you submit a request through your gateway, the response will return messages to help you debug.

When you're done debugging your gateway, you can update the gateway and remove the `exceptionLevel` field, such that the message to the end user only shows an unspecified internal error.

###### Example

As an example, suppose that the user doesn't have permissions to invoke a Lambda function that is targeted by the gateway. A request that calls this function would return a different message depending on whether debugging is on or off:

- **Debugging on** – A detailed error message would be returned in the content's `text` field and also in the `_meta` field in the response, as in the following example:

```
{
  "jsonrpc": "2.0",
  "id": 24,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "Access denied while invoking Lambda function arn:aws:lambda:us-west-2:123456789012:function:TestGatewayLambda. Check the permissions on the Lambda function and Gateway execution role, and retry the request."
      }
    ],
    "_meta": {
      "debug": {
        "type": "text",
        "text": "Access denied while invoking Lambda function arn:aws:lambda:us-west-2:123456789012:function:TestGatewayLambda. Check the permissions on the Lambda function and Gateway execution role, and retry the request."
      }
    },
    "isError": true
  }
}
```

- **Debugging off** – A generic error message would be returned in the content's `text` field in the response, as in the following example:

```
{
  "jsonrpc": "2.0",
  "id": 24,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "An internal error occurred. Please retry later."
      }
    ],
    "isError": true
  }
}
```
