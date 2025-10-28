# Making query API requests using AWS query

protocol in Amazon SQS

This topic explains how to construct an Amazon SQS endpoint, make GET and POST requests, and
interpret responses.

## Constructing an endpoint

In order to work with Amazon SQS queues, you must construct an endpoint. For information
about Amazon SQS endpoints, see the following pages in the
_Amazon Web Services General Reference_:

- [Regional endpoints](../../../general/latest/gr/rande.md#sqs_region "../../../general/latest/gr/rande.md#sqs_region")
- [Amazon Simple Queue Service endpoints and
  quotas](../../../general/latest/gr/sqs-service.md "../../../general/latest/gr/sqs-service.md")

Every Amazon SQS endpoint is independent. For example, if two queues are named _MyQueue_ and one has the endpoint
`sqs.us-east-2.amazonaws.com` while the other has the endpoint
`sqs.eu-west-2.amazonaws.com`, the two queues don't share any data with each
other.

The following is an example of an endpoint which makes a request to create a queue.

```
https://sqs.eu-west-2.amazonaws.com/
?Action=CreateQueue
&DefaultVisibilityTimeout=40
&QueueName=MyQueue
&Version=2012-11-05
&`AUTHPARAMS`
```

###### Note

Queue names and queue URLs are case sensitive.

The structure of `AUTHPARAMS` depends on the signature of the API request.
For more information, see [Signing AWS API Requests](../../../general/latest/gr/signing_aws_api_requests.md "../../../general/latest/gr/signing_aws_api_requests.md")
in the _Amazon Web Services General Reference_.

## Making a GET request

An Amazon SQS GET request is structured as a URL which consists of the following:

- **Endpoint** – The resource that the
  request is acting on (the [queue name and URL](sqs-queue-message-identifiers.md#queue-name-url "sqs-queue-message-identifiers.md#queue-name-url")), for example:
  `https://sqs.us-east-2.amazonaws.com/`123456789012`/MyQueue`
- **Action** – The [action](../APIReference/API_Operations.md "../APIReference/API_Operations.md") that you want to
  perform on the endpoint. A question mark (`?`) separates the endpoint
  from the action, for example:
  `?Action=SendMessage&MessageBody=Your%20Message%20Text`
- **Parameters** – Any request parameters.
  Each parameter is separated by an ampersand (`&`), for example:
  `&Version=2012-11-05&`AUTHPARAMS``

The following is an example of a GET request that sends a message to an Amazon SQS
queue.

```
https://sqs.us-east-2.amazonaws.com/`123456789012`/MyQueue
?Action=SendMessage&MessageBody=Your%20message%20text
&Version=2012-11-05
&`AUTHPARAMS`
```

###### Note

Queue names and queue URLs are case sensitive.

Because GET requests are URLs, you must URL-encode all parameter values. Because
spaces aren't allowed in URLs, each space is URL-encoded as `%20`. The
rest of the example isn't URL-encoded to make it easier to read.

## Making a POST request

An Amazon SQS POST request sends query parameters as a form in the body of an HTTP
request.

The following is an example of an HTTP header with `Content-Type` set to
`application/x-www-form-urlencoded`.

```
POST /`123456789012`/MyQueue HTTP/1.1
Host: sqs.us-east-2.amazonaws.com
Content-Type: application/x-www-form-urlencoded
```

The header is followed by a `form-urlencoded` GET request that sends a message to an Amazon SQS
queue. Each parameter is separated by an ampersand (`&`).

```
Action=SendMessage
&MessageBody=Your+Message+Text
&Expires=2020-10-15T12%3A00%3A00Z
&Version=2012-11-05
&`AUTHPARAMS`
```

###### Note

Only the `Content-Type` HTTP header is required. The
`AUTHPARAMS` is the same as for the
GET request.

Your HTTP client might add other items to the HTTP request, according to the
client's HTTP version.
