# Response streaming for Lambda functions

Lambda functions can stream response payloads back to clients through [Lambda function URLs](urls-configuration.md "urls-configuration.md") or by using the [InvokeWithResponseStream](API_InvokeWithResponseStream.md "API_InvokeWithResponseStream.md") API (via the AWS SDK or direct API calls). Response
streaming can benefit latency sensitive applications by improving time to first byte (TTFB)
performance. This is because you can send partial responses back to the client as they become
available. Additionally, response streaming functions can return payloads up to 200 MB, compared to the 6 MB maximum for
buffered responses. Streaming a response also means that your function doesn’t need to fit the entire
response in memory. For very large responses, this can reduce the amount of memory you need to
configure for your function.

The speed at which Lambda streams your responses depends on the response size. The streaming rate for
the first 6 MB of your function’s response is uncapped. For responses larger than 6 MB, the remainder of the response
is subject to a bandwidth cap. For more information on streaming bandwidth, see [Bandwidth limits for response streaming](#config-rs-bandwidth-cap "#config-rs-bandwidth-cap").

Streaming responses incurs a cost. For more information, see [AWS Lambda Pricing](https://aws.amazon.com/lambda/pricing/ "https://aws.amazon.com/lambda/pricing/").

Lambda supports response streaming on Node.js managed runtimes. For other languages, you can [use a
custom runtime with a custom Runtime API integration](runtimes-custom.md#runtimes-custom-response-streaming "runtimes-custom.md#runtimes-custom-response-streaming") to stream responses or use the [Lambda Web Adapter](https://github.com/awslabs/aws-lambda-web-adapter "https://github.com/awslabs/aws-lambda-web-adapter").

###### Note

When testing your function through the Lambda console, you'll always see responses as buffered.

###### Topics

- [Bandwidth limits for response streaming](#config-rs-bandwidth-cap "#config-rs-bandwidth-cap")
- [VPC compatibility with response streaming](#config-rs-vpc-compatibility "#config-rs-vpc-compatibility")
- [Writing response streaming-enabled Lambda functions](config-rs-write-functions.md "config-rs-write-functions.md")
- [Invoking a response streaming enabled function using Lambda function URLs](config-rs-invoke-furls.md "config-rs-invoke-furls.md")
- [Tutorial: Creating a response streaming Lambda
  function with a function URL](response-streaming-tutorial.md "response-streaming-tutorial.md")

## Bandwidth limits for response streaming

The first 6 MB of your function’s response payload has uncapped bandwidth. After this initial burst, Lambda streams your response at a
maximum rate of 2 MBps. If your function responses never exceed 6 MB, then this bandwidth limit never applies.

###### Note

Bandwidth limits only apply to your function’s response payload, and not to network access by your function.

The rate of uncapped bandwidth varies depending on a number of factors, including your function’s processing speed. You can normally
expect a rate higher than 2 MBps for the first 6 MB of your function’s response. If your function is streaming a response to a destination
outside of AWS, the streaming rate also depends on the speed of the external internet connection.

## VPC compatibility with response streaming

When using Lambda functions in a VPC environment, there are important considerations for response streaming:

- Lambda function URLs do not support response streaming within a VPC environment.
- You can use response streaming within a VPC by invoking your Lambda function through the AWS SDK using the `InvokeWithResponseStream` API. This requires setting up the appropriate VPC endpoints for Lambda.
- For VPC environments, you'll need to create an interface VPC endpoint for Lambda to enable communication between your resources in the VPC and the Lambda service.

A typical architecture for response streaming in a VPC might include:

```
Client in VPC -> Interface VPC endpoint for Lambda -> Lambda function -> Response streaming back through the same path
```
