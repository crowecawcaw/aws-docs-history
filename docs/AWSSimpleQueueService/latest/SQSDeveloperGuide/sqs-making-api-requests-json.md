

# Making query API requests using AWS JSON protocol in Amazon SQS
<a name="sqs-making-api-requests-json"></a>

This topic explains how to construct an Amazon SQS endpoint, make POST requests, and interpret responses.

**Note**  
AWS JSON protocol is supported for most language variants. For a full list of supported language variants, see [What languages are supported for AWS JSON protocol used in Amazon SQS APIs?](sqs-json-faqs.md#json-protocol-supported-languages).

## Constructing an endpoint
<a name="sqs-api-constructing-endpoints-json"></a>

To work with Amazon SQS queues, you must construct an endpoint. For information about Amazon SQS endpoints, see the following pages in the *Amazon Web Services General Reference*:
+ [Regional endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints)
+ [Amazon Simple Queue Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/sqs-service)

Every Amazon SQS endpoint is independent. For example, if two queues are named *MyQueue* and one has the endpoint `sqs.us-east-2.amazonaws.com` while the other has the endpoint `sqs.eu-west-2.amazonaws.com`, the two queues don't share any data with each other.

The following is an example of an endpoint that makes a request to create a queue. 

```
POST / HTTP/1.1
Host: sqs.us-west-2.amazonaws.com
X-Amz-Target: AmazonSQS.CreateQueue
X-Amz-Date: <Date>
Content-Type: application/x-amz-json-1.0
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive 
{
    "QueueName":"MyQueue",
    "Attributes": {
        "VisibilityTimeout": "40"
    },
    "tags": {
        "QueueType": "Production"
    }
}
```

**Note**  
Queue names and queue URLs are case sensitive.  
The structure of {{`AUTHPARAMS`}} depends on the signature of the API request. For more information, see [Signing AWS API Requests](https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html) in the *Amazon Web Services General Reference*.

## Making a POST request
<a name="structure-post-request"></a>

An Amazon SQS POST request sends query parameters as a form in the body of an HTTP request.

The following is an example of an HTTP header with `X-Amz-Target` set to `AmazonSQS.<operationName>`, and an HTTP header with `Content-Type` set to `application/x-amz-json-1.0`.

```
POST / HTTP/1.1
Host: sqs.<region>.<domain>
X-Amz-Target: AmazonSQS.SendMessage
X-Amz-Date: <Date>
Content-Type: application/x-amz-json-1.0
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive 
{
    "QueueUrl": "https://sqs.<region>.<domain>/<awsAccountId>/<queueName>/",
    "MessageBody": "This is a test message"
}
```

This HTTP POST request sends a message to an Amazon SQS queue.

**Note**  
Both HTTP headers `X-Amz-Target` and `Content-Type` are required.  
Your HTTP client might add other items to the HTTP request, according to the client's HTTP version.