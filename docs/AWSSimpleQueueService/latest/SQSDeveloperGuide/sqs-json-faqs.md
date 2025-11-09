# Amazon SQS AWS JSON protocol FAQs

This topic covers frequently asked questions about using AWS JSON
protocol with Amazon SQS.

## What is AWS JSON protocol,

and how does it differ from existing Amazon SQS API requests and responses?

JSON is one of the most widely used and accepted wiring methods for communication
between heterogeneous systems. Amazon SQS uses JSON as a medium to communicate between an
AWS SDK client (for example, Java, Python, Golang, JavaScript)
and Amazon SQS server. An HTTP request of an Amazon SQS API operation accepts input in the
form of JSON. The Amazon SQS operation is executed and the response of execution is
shared back to the SDK client in the form of JSON. Compared to AWS
query, JSON is more efficient at transporting data between client and server.

- Amazon SQS AWS JSON protocol acts as a mediator between Amazon SQS
  client and server.
- The server doesn’t understand the programming language in which the Amazon SQS
  operation is created, but it understands the AWS JSON
  protocol.
- The Amazon SQS AWS JSON protocol uses the serialization (convert
  object to JSON format) and deserialization (convert JSON format to object)
  between the Amazon SQS client and server.

## How do I get started with AWS JSON protocols for Amazon SQS?

To get started with the latest AWS SDK version to achieve faster
messaging for Amazon SQS, upgrade your AWS SDK to the specified version or
any subsequent version. To learn more about SDK clients, see the Guide column in the
table below.

The following is a list of SDK versions across language variants for AWS JSON protocol for use with Amazon SQS APIs:

| Language        | SDK client repository                                                                                  | Required SDK client version                                                                                                                                                                                                | Guide                                                                                                                              |
| --------------- | ------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| C++             | [aws/aws-sdk-cpp](https://github.com/aws/aws-sdk-cpp "https://github.com/aws/aws-sdk-cpp")             | [1.11.98](https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.198 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.198")                                                                                             | [AWS SDK for C++](https://aws.amazon.com/sdk-for-cpp/ "https://aws.amazon.com/sdk-for-cpp/")                                       |
| Golang 1.x      | [aws/aws-sdk-go](https://github.com/aws/aws-sdk-go "https://github.com/aws/aws-sdk-go")                | [v1.47.7](https://github.com/aws/aws-sdk-go/releases/tag/v1.47.7 "https://github.com/aws/aws-sdk-go/releases/tag/v1.47.7")                                                                                                 | [AWS SDK for Go](https://aws.amazon.com/sdk-for-go/ "https://aws.amazon.com/sdk-for-go/")                                          |
| Golang 2.x      | [aws/aws-sdk-go-v2](https://github.com/aws/aws-sdk-go-v2 "https://github.com/aws/aws-sdk-go-v2")       | [v1.28.0](https://github.com/aws/aws-sdk-go-v2/blob/release-2023-11-09/service/sqs/CHANGELOG.md#v1270-2023-11-09 "https://github.com/aws/aws-sdk-go-v2/blob/release-2023-11-09/service/sqs/CHANGELOG.md#v1270-2023-11-09") | [AWS SDK for Go V2](https://aws.github.io/aws-sdk-go-v2/docs/ "https://aws.github.io/aws-sdk-go-v2/docs/")                         |
| Java 1.x        | [aws/aws-sdk-java](https://github.com/aws/aws-sdk-java "https://github.com/aws/aws-sdk-java")          | [1.12.585](https://github.com/aws/aws-sdk-java/releases/tag/1.12.585 "https://github.com/aws/aws-sdk-java/releases/tag/1.12.585")                                                                                          | [AWS SDK for Java](https://aws.amazon.com/sdk-for-java/ "https://aws.amazon.com/sdk-for-java/")                                    |
| Java 2.x        | [aws/aws-sdk-java-v2](https://github.com/aws/aws-sdk-java-v2 "https://github.com/aws/aws-sdk-java-v2") | [2.21.19](https://github.com/aws/aws-sdk-java-v2/releases/tag/2.21.19 "https://github.com/aws/aws-sdk-java-v2/releases/tag/2.21.19")                                                                                       | [AWS SDK for Java](https://aws.amazon.com/sdk-for-java/ "https://aws.amazon.com/sdk-for-java/")                                    |
| JavaScript v2.x | [aws/aws-sdk-js](https://github.com/aws/aws-sdk-js "https://github.com/aws/aws-sdk-js")                | [JavaScript on AWS](https://aws.amazon.com/developer/language/javascript/ "https://aws.amazon.com/developer/language/javascript/")                                                                                         |
| JavaScript v3.x | [aws/aws-sdk-js-v3](https://github.com/aws/aws-sdk-js-v3 "https://github.com/aws/aws-sdk-js-v3")       | [v3.447.0](https://github.com/aws/aws-sdk-js-v3/releases/tag/v3.447.0 "https://github.com/aws/aws-sdk-js-v3/releases/tag/v3.447.0")                                                                                        | [JavaScript on AWS](https://aws.amazon.com/developer/language/javascript/ "https://aws.amazon.com/developer/language/javascript/") |
| .NET            | [aws/aws-sdk-net](https://github.com/aws/aws-sdk-net "https://github.com/aws/aws-sdk-net")             | [3.7.681.0](https://github.com/aws/aws-sdk-net/releases/tag/3.7.681.0 "https://github.com/aws/aws-sdk-net/releases/tag/3.7.681.0")                                                                                         | [AWS SDK for .NET](https://aws.amazon.com/sdk-for-net/ "https://aws.amazon.com/sdk-for-net/")                                      |
| PHP             | [aws/aws-sdk-php](https://github.com/aws/aws-sdk-php "https://github.com/aws/aws-sdk-php")             | [3.285.2](https://github.com/aws/aws-sdk-php/releases/tag/3.285.2 "https://github.com/aws/aws-sdk-php/releases/tag/3.285.2")                                                                                               | [AWS SDK for PHP](https://aws.amazon.com/sdk-for-php/ "https://aws.amazon.com/sdk-for-php/")                                       |
| Python-boto3    | [boto/boto3](https://github.com/boto/boto3 "https://github.com/boto/boto3")                            | [1.28.82](https://github.com/boto/boto3/releases/tag/1.28.82 "https://github.com/boto/boto3/releases/tag/1.28.82")                                                                                                         | [AWS SDK for Python (Boto3)](https://aws.amazon.com/sdk-for-python/ "https://aws.amazon.com/sdk-for-python/")                      |
| Python-botocore | [boto/botocore](https://github.com/boto/botocore/ "https://github.com/boto/botocore/")                 | [1.31.82](https://github.com/boto/botocore/releases/tag/1.31.82 "https://github.com/boto/botocore/releases/tag/1.31.82")                                                                                                   | [AWS SDK for Python (Boto3)](https://aws.amazon.com/sdk-for-python/ "https://aws.amazon.com/sdk-for-python/")                      |
| awscli          | [AWS<br>CLI](https://github.com/aws/aws-cli "https://github.com/aws/aws-cli")                          | [1.29.82](https://github.com/aws/aws-cli/releases/tag/1.29.82 "https://github.com/aws/aws-cli/releases/tag/1.29.82")                                                                                                       | [AWSCommand Line Interface](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/")                                             |
| Ruby            | [aws/aws-sdk-ruby](https://github.com/aws/aws-sdk-ruby "https://github.com/aws/aws-sdk-ruby")          | [1.67.0](https://rubygems.org/gems/aws-sdk-sqs/versions/1.67.0 "https://rubygems.org/gems/aws-sdk-sqs/versions/1.67.0")                                                                                                    | [AWS SDK for Ruby](https://aws.amazon.com/sdk-for-ruby/ "https://aws.amazon.com/sdk-for-ruby/")                                    |

## What are the risks of enabling JSON protocol

for my Amazon SQS workloads?

If you are using a custom implementation of AWS SDK or a
combination of custom clients and AWS SDK to interact with Amazon SQS that
generates AWS Query based (aka XML-based) responses, it may be
incompatible with AWS JSON protocol. If you encounter any issues,
contact AWS Support.

## What if I am already on the

latest AWS SDK version, but my open sourced solution does not
support JSON?

You must change your SDK version to the version previous to what you are using.
See [How do I get started with AWS JSON protocols for Amazon SQS?](#json-protocol-getting-started "#json-protocol-getting-started") for more information. AWS SDK versions listed in [How do I get started with AWS JSON protocols for Amazon SQS?](#json-protocol-getting-started "#json-protocol-getting-started") uses JSON wire protocol for
Amazon SQS APIs. If you change your AWS SDK to the previous version, your
Amazon SQS APIs will use the AWS query.

## What languages are supported for

AWS JSON protocol used in Amazon SQS APIs?

Amazon SQS supports all language variants where AWS SDKs are generally
available (GA). Currently, we don't support Kotlin, Rust, or Swift. To learn more
about other language variants, see [Tools to Build on AWS](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/").

## What regions are supported for

AWS JSON protocol used in Amazon SQS APIs

Amazon SQS supports AWS JSON protocol in all [AWS regions](../../../general/latest/gr/sqs-service.md "../../../general/latest/gr/sqs-service.md")
where Amazon SQS is available.

## What latency improvements can I expect

when upgrading to the specified AWS SDK versions for Amazon SQS using
the AWS JSON protocol?

AWS JSON protocol is more efficient at serialization and
deserialization of requests and responses when compared to AWS query
protocol. Based on AWS performance tests for a 5 KB message payload,
JSON protocol for Amazon SQS reduces end-to-end message processing latency by up to 23%,
and reduces application client side CPU and memory usage.

## Will AWS query protocol be

deprecated?

AWS query protocol will continue to be supported. You can continue
using AWS query protocol as long as your AWS SDK
version is set any previous version other that what is listed in [How do I get started with AWS JSON protocols for Amazon SQS](#json-protocol-getting-started "#json-protocol-getting-started").

## Where can I find more information about

AWS JSON protocol?

You can find more information about JSON protocol at [AWS JSON 1.0 protocol](https://smithy.io/2.0/aws/protocols/aws-json-1_0-protocol.html "https://smithy.io/2.0/aws/protocols/aws-json-1_0-protocol.html") in the _Smithy_ documentation. For more about Amazon SQS API requests using
AWS JSON protocol, see [Making query API requests using AWS JSON protocol in Amazon SQS](sqs-making-api-requests-json.md "sqs-making-api-requests-json.md").
