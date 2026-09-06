

# Troubleshoot issues with response streaming in API Gateway
<a name="response-streaming-troubleshoot"></a>

The following troubleshooting guidance might help resolve issues with your APIs that use response streaming.

## General troubleshooting
<a name="response-streaming-general-troubleshooting"></a>

You can use the [TestInvokeMethod](https://docs.aws.amazon.com/apigateway/latest/api/API_TestInvokeMethod.html) or the console's test tab to test your stream response. The following considerations might impact your use of test invoke for response streaming:
+ When you test your method, API Gateway buffers your streamed response payload. Once any of the following conditions have been met, API Gateway returns a one-time response containing the buffered payload:
  + The request is complete
  + 35 seconds have elapsed
  + More than 1 MB of response payload has been buffered
+ If more than 35 seconds elapse before your method returns an HTTP response status and all headers, then the response status returned in TestInvokeMethod is 0.
+ API Gateway doesn't produce any execution logs.

After you've deployed your API, you can test your stream response by using a curl command. We recommend that you use the `-i` option to include protocol response headers in the output. To see the response data as it arrives, use the curl option `--no-buffer`

## Troubleshoot cURL errors
<a name="response-streaming-troubleshoot-curl-error"></a>

If you're testing an integration and you receive the error `curl: (18) transfer closed with outstanding read data remaining`, make sure the timeout of your integration is long enough. If you're using a Lambda function, you need to update the response timeout of the Lambda function. For more information, see [Configure Lambda function timeout](https://docs.aws.amazon.com/lambda/latest/dg/configuration-timeout.html).

## Troubleshoot using access logging
<a name="response-streaming-troubleshoot-access-logging"></a>

You can use access logs for your REST API stage to log and troubleshoot your response stream. In addition to the existing variables, you can use the following access log variables:

`$context.integration.responseTransferMode`  
The response transfer mode of your integration. This can be either `BUFFERED` or `STREAMED`.

`$context.integration.timeToAllHeaders`  
The time between when API Gateway establishes the integration connection to when it receives all integration response headers from the client.

`$context.integration.timeToFirstContent`  
The time between when API Gateway establishes the integration connection to when it receives the first content bytes.

`$context.integration.latency` or `$context.integrationLatency`  
The time when API Gateway establishes the integration connection to when the integration response stream is complete.

The following figure shows how these access log variables represent different components of a response stream.

![Access log variables for response streaming in API Gateway](http://docs.aws.amazon.com/apigateway/latest/developerguide/images/response-streaming-figure.png)


For more information about access logs, see [Set up CloudWatch logging for REST APIs in API Gateway](set-up-logging.md). You can also use X-Ray to monitor your response stream. For more information, see [Trace user requests to REST APIs using X-Ray in API Gateway](apigateway-xray.md).