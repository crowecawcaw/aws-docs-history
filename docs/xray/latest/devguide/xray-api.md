

# Use the X-Ray API
<a name="xray-api"></a>

If the X-Ray SDK doesn’t support your programming language, you can use either the X-Ray APIs directly or the AWS Command Line Interface (AWS CLI) to call X-Ray API commands. Use the following guidance to choose how you interact with the API:
+ Use the AWS CLI for simpler syntax using pre-formatted commands or with options inside your request.
+ Use the X-Ray API directly for maximum flexibility and customization for requests that you make to X-Ray.

If you use the [X-Ray API](https://docs.aws.amazon.com/xray/latest/api/Welcome.html) directly instead of the AWS CLI, you must parametrize your request in the correct data format and may also have to configure authentication and error handling.

The following diagram shows guidance to choose how to interact with the X-Ray API:

![X-Ray displays detailed information about application requests.](http://docs.aws.amazon.com/xray/latest/devguide/images/api-vs-cli.png)


Use the X-Ray API to send trace data to directly to X-Ray. The X-Ray API supports all functions available in the X-Ray SDK including the following common actions:
+ [PutTraceSegments](https://docs.aws.amazon.com/xray/latest/api/API_PutTraceSegments.html) – Uploads segment documents to X-Ray. 
+ [BatchGetTraces](https://docs.aws.amazon.com/xray/latest/api/API_BatchGetTraces.html) – Retrieves a list of traces in a list of trace IDs. Each retrieved trace is a collection of segment documents from a single request.
+ [GetTraceSummaries](https://docs.aws.amazon.com/xray/latest/api/API_GetTraceSummaries.html) – Retrieves IDs and annotations for traces. You can specify a `FilterExpression` to retrieve a subset of trace summaries.
+ [GetTraceGraph](https://docs.aws.amazon.com/xray/latest/api/API_GetTraceGraph.html) – Retrieves a service graph for a specific trace ID.
+ [GetServiceGraph](https://docs.aws.amazon.com/xray/latest/api/API_GetServiceGraph.html) – Retrieves a JSON formatted document that describes services that process incoming requests and call downstream requests.

You can also use the AWS Command Line Interface (AWS CLI) inside your application code to programmatically interact with X-Ray. The AWS CLI supports all functions available in the X-Ray SDK including those for other AWS services. The following functions are versions of the API operations listed previously with a simpler format:
+ [put-trace-segments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/put-trace-segments.html) – Uploads segment documents to X-Ray.
+ [batch-get-traces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/batch-get-traces.html) – Retrieves a list of traces in a list of trace IDs. Each retrieved trace is a collection of segment documents from a single request.
+ [get-trace-summaries](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/get-trace-summaries.html) – Retrieves IDs and annotations for traces. You can specify a `FilterExpression` to retrieve a subset of trace summaries.
+ [get-trace-graph](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/get-trace-graph.html) – Retrieves a service graph for a specific trace ID.
+ [get-service-graph](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/get-service-graph.html) – Retrieves a `JSON` formatted document that describes services that process incoming requests and call downstream requests.

To get started, you must install the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) for your operating system. AWS supports Linux, macOS and Windows operating systems. For more information about the list of X-Ray commands, see the [AWS CLI Command Reference guide for X-Ray](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/index.html).

**Topics**
+ [Using the AWS X-Ray API with the AWS CLI](xray-api-tutorial.md)
+ [Sending trace data to AWS X-Ray](xray-api-sendingdata.md)
+ [Getting data from AWS X-Ray](xray-api-gettingdata.md)
+ [Configuring sampling, groups, and encryption settings with the AWS X-Ray API](xray-api-configuration.md)
+ [Using sampling rules with the X-Ray API](xray-api-sampling.md)
+ [AWS X-Ray segment documents](xray-api-segmentdocuments.md)