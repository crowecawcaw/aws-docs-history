# Interpreting Amazon SQS XML API responses

When you send a request to Amazon SQS, it returns an XML response containing the results of
the request. To understand the structure and details of these responses, refer to the
specific [API
actions](../APIReference/API_Operations.md "../APIReference/API_Operations.md") in the _Amazon Simple Queue Service API Reference_.

## Successful XML response

structure

If the request is successful, the main response element is named after the action,
with `Response` appended (for example,
``ActionName`Response`).

This element contains the following child elements:

- **``ActionName`Result`**
  – Contains an action-specific element. For example, the
  `CreateQueueResult` element contains the
  `QueueUrl` element which, in turn, contains the URL of the
  created queue.
- **`ResponseMetadata`** –
  Contains the `RequestId` which, in turn, contains the Universal
  Unique Identifier (UUID) of the request.

The following is an example successful response in XML format:

```
<CreateQueueResponse
   xmlns=https://sqs.us-east-2.amazonaws.com/doc/2012-11-05/
   xmlns:xsi=http://www.w3.org/2001/XMLSchema-instance
   xsi:type=CreateQueueResponse>
   <CreateQueueResult>
      <QueueUrl>https://sqs.us-east-2.amazonaws.com/770098461991/queue2</QueueUrl>
   </CreateQueueResult>
   <ResponseMetadata>
      <RequestId>cb919c0a-9bce-4afe-9b48-9bdf2412bb67</RequestId>
   </ResponseMetadata>
</CreateQueueResponse>
```

## XML error response

structure

If a request is unsuccessful, Amazon SQS always returns the main response element
`ErrorResponse`. This element contains an `Error` element
and a `RequestId` element.

The `Error` element contains the following child elements:

- **`Type`** – Specifies
  whether the error was a producer or consumer error.
- **`Code`** – Specifies the
  type of error.
- **`Message`** – Specifies
  the error condition in a readable format.
- **`Detail`** – (Optional)
  Specifies additional details about the error.

The `RequestId` element contains the UUID of the request.

The following is an example error response in XML format:

```
<ErrorResponse>
   <Error>
      <Type>Sender</Type>
      <Code>InvalidParameterValue</Code>
      <Message>
         Value (quename_nonalpha) for parameter QueueName is invalid.
         Must be an alphanumeric String of 1 to 80 in length.
      </Message>
   </Error>
   <RequestId>42d59b56-7407-4c4a-be0f-4c88daeea257</RequestId>
</ErrorResponse>
```
