# Using APIs with Amazon SQS

This topic provides information about constructing Amazon SQS endpoints, making query API
requests using the GET and POST methods, and using batch API actions. For detailed
information about Amazon SQS [actions](../APIReference/API_Operations.md "../APIReference/API_Operations.md")—including parameters, errors, examples, and [data types](../APIReference/API_Types.md "../APIReference/API_Types.md"), see the [_Amazon Simple Queue Service API Reference_](../APIReference.md "../APIReference.md").

To access Amazon SQS using a variety of programming languages, you can also use [AWS SDKs](https://aws.amazon.com/tools/#sdk "https://aws.amazon.com/tools/#sdk"), which contain the
following automatic functionality:

- Cryptographically signing your service requests
- Retrying requests
- Handling error responses
  For more information, see [Using Amazon SQS with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").

For command line tool information, see the Amazon SQS sections in the [_AWS CLI Command Reference_](../../../cli/latest/reference/sqs/index.md "../../../cli/latest/reference/sqs/index.md")
and the [_AWS Tools for PowerShell Cmdlet Reference_](../../../powershell/latest/reference.md "../../../powershell/latest/reference.md").

**Amazon SQS APIs with AWS JSON protocol**

Amazon SQS uses AWS JSON protocol as the transport mechanism for
all Amazon SQS APIs on the specified [AWS SDK versions](sqs-json-faqs.md#json-protocol-getting-started "sqs-json-faqs.md#json-protocol-getting-started"). AWS JSON protocol provides a higher
throughput, lower latency, and faster application-to-application communication. AWS JSON protocol is more efficient in serialization/deserialization of requests
and responses when compared to AWS query protocol. If you still prefer to use
the AWS query protocol with SQS APIs, see [What languages are supported for
AWS JSON protocol used in Amazon SQS APIs?](sqs-json-faqs.md#json-protocol-supported-languages "sqs-json-faqs.md#json-protocol-supported-languages") for the AWS SDK
versions that support Amazon SQS AWS query protocol.

Amazon SQS uses AWS JSON protocol to communicate between AWS SDK
clients (for example, Java, Python, Golang, JavaScript) and the Amazon SQS server. An HTTP
request of an Amazon SQS API operation accepts JSON formatted input. The Amazon SQS operation is
executed, and the execution response is sent back to the SDK client in JSON format. Compared
to AWS query, AWS JSON is simpler, faster, and more efficient
to transport data between client and server.

- AWS JSON protocol acts as a mediator between the Amazon SQS client and
  server.
- The server doesn’t understand the programming language in which the Amazon SQS
  operation is created, but it understands the AWS JSON
  protocol.
- The AWS JSON protocol uses the serialization (convert object to
  JSON format) and de-serialization (convert JSON format to object) between Amazon SQS
  client and server.
  For more information about AWS JSON protocol with Amazon SQS, see [Amazon SQS AWS JSON protocol FAQs](sqs-json-faqs.md "sqs-json-faqs.md").

AWS JSON protocol is available on the specified [AWS SDK version](sqs-json-faqs.md#json-protocol-getting-started "sqs-json-faqs.md#json-protocol-getting-started"). To review
SDK version and release dates across language variants, see the [AWS SDKs and Tools
version support matrix](../../../sdkref/latest/guide/version-support-matrix.md "../../../sdkref/latest/guide/version-support-matrix.md") in the _AWS SDKs and Tools Reference Guide_
