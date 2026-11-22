

# Turn on debugging messages

While your gateway is in development, you can turn on debugging messages to return details on target configuration issues, including lambda function errors, egress authorizer errors, target specification parameter validation errors. After turning on debugging messages, if an issue occurs when you invoke your gateway, the response will return messages to help you debug.

 **To turn on debugging messages, do one of the following:** 
+ If you use the AgentCore CLI to create a gateway, debugging is off by default. Pass `--exception-level debug` to `agentcore add gateway`, or set the gateway’s `exceptionLevel` to `DEBUG` in `agentcore/agentcore.json`, and then run `agentcore deploy`.
+ If you use the AWS Management Console to create a gateway, debugging is turned on by default. The option is under **Additional configurations** in the **Gateway details** section.
+ If you use the AWS CLI or an AWS SDK, set the `exceptionLevel` value as `DEBUG` when you make a [CreateGateway](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateGateway.html) or [UpdateGateway](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdateGateway.html) request.

When you’re done debugging your gateway, you can update the gateway to turn off debugging messages, such that the message to the end user only shows a generic error.

With debugging turned off, the detailed message isn’t lost. If you configure a log destination for the gateway, the gateway writes the detailed message to your gateway’s application logs. For more information, see [Provided log data](observability-gateway-metrics.md#observability-gateway-logs-provided).

 **To turn off debugging messages, do one of the following:** 
+ In an AgentCore CLI project, set the gateway’s `exceptionLevel` to `NONE` in `agentcore/agentcore.json`, and then run `agentcore deploy`.
+ In the AWS Management Console, expand **Additional configurations** in the **Gateway details** section when you create or edit a gateway and uncheck the checkbox next to **Exception level debug**.
+ In the AWS CLI or an AWS SDK, omit the `exceptionLevel` field when you make a `CreateGateway` or `UpdateGateway` request to turn off debugging.

## Example gateway responses with debugging turned on and off
<a name="gateway-building-debug-ex"></a>

As an example, suppose that the user doesn’t have permissions to invoke a Lambda function that is targeted by the gateway. A request that calls this function would return a different message depending on whether debugging is on or off:
+  **Debugging on** – A detailed error message would be returned in the content’s `text` field and also in the `_meta` field in the response, as in the following example:

  ```json
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
+  **Debugging off** – A generic error message would be returned in the content’s `text` field in the response, as in the following example:

  ```json
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

## Debugging messages on HTTP and inference targets
<a name="gateway-debug-messages-http"></a>

For HTTP and inference targets, the same setting decides whether a detailed message, such as an interceptor Lambda function’s error, reaches the caller. The status code is the same either way.
+  **Debugging on** – The error message contains the details, as in the following example for an HTTP target:

  ```json
  {
    "success": false,
    "error": "{\"errorMessage\": \"Redaction table unavailable\", \"errorType\": \"RuntimeError\", ...}"
  }
  ```
+  **Debugging off** – The error message is a fixed message, as in the following example. Inference targets return the same message in the error format of the request’s API.

  ```json
  {
    "success": false,
    "error": "The request failed. Set the gateway's exceptionLevel to DEBUG to return the error details."
  }
  ```