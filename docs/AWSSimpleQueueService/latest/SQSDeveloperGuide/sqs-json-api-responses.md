

# Interpreting Amazon SQS JSON API responses
<a name="sqs-json-api-responses"></a>

When you send a request to Amazon SQS, it returns a JSON response with the results. The response structure depends on the API action you used.

To understand the details of these responses, see:
+ The specific API action in the [API actions](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_Operations.html) in the *Amazon Simple Queue Service API Reference*
+ The [Amazon SQS AWS JSON protocol FAQs](sqs-json-faqs.md)

## Successful JSON response structure
<a name="sqs-json-api-successful-response-structure"></a>

If the request is successful, the main response element is `x-amzn-RequestId`, which contains the Universal Unique Identifier (UUID) of the request, as well as other appended response field(s). For example, the following [`CreateQueue`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_CreateQueue.html) response contains the `QueueUrl` field, which, in turn, contains the URL of the created queue.

```
HTTP/1.1 200 OK
x-amzn-RequestId: <requestId>
Content-Length: <PayloadSizeBytes>
Date: <Date>
Content-Type: application/x-amz-json-1.0
{
    "QueueUrl":"https://sqs.us-east-1.amazonaws.com/111122223333/MyQueue"
}
```

## JSON error response structure
<a name="sqs-api-error-response-structure"></a>

If a request is unsuccessful, Amazon SQS returns the main response, including the HTTP header and the body.

In the HTTP header, `x-amzn-RequestId` contains the UUID of the request. `x-amzn-query-error` contains two pieces of information: the type of error, and whether the error was a producer or consumer error. 

In the response body, `"__type"` indicates other error details, and `Message` indicates the error condition in a readable format. 

The following is an example error response in JSON format:

```
HTTP/1.1 400 Bad Request
x-amzn-RequestId: 66916324-67ca-54bb-a410-3f567a7a0571
x-amzn-query-error: AWS.SimpleQueueService.NonExistentQueue;Sender
Content-Length: <PayloadSizeBytes>
Date: <Date>
Content-Type: application/x-amz-json-1.0
{
    "__type": "com.amazonaws.sqs#QueueDoesNotExist",
    "message": "The specified queue does not exist."
}
```