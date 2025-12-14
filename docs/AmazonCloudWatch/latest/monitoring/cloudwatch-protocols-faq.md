# FAQs on CloudWatch supported protocols

CloudWatch SDKs started using two additional protocols: [AWS JSON 1.1](https://smithy.io/2.0/aws/protocols/aws-json-1_1-protocol.html "https://smithy.io/2.0/aws/protocols/aws-json-1_1-protocol.html") and [Smithy RPC v2 CBOR](https://smithy.io/2.0/additional-specs/protocols/smithy-rpc-v2.html "https://smithy.io/2.0/additional-specs/protocols/smithy-rpc-v2.html"). These protocols are more performant than AWS Query that was previously utilized by the CloudWatch
SDKs and CLIs. AWS SDKs will prioritize the protocol that is the most performant for each language.

## What is the AWS JSON protocol, and how does it differ from existing CloudWatch API requests and responses?

JSON is one of the most widely used and accepted data formats for communication between heterogeneous systems. CloudWatch uses JSON as a medium to communicate between an AWS SDK client (for example, Java, Python, Golang, JavaScript) and CloudWatch server. An HTTP request of an CloudWatch API operation accepts input in the form of JSON. The CloudWatch operation is executed and the response of execution is shared back to the SDK client in the form of JSON. Compared to AWS Query, JSON is more efficient at transporting data between client and server.

- CloudWatch AWS JSON protocol acts as a mediator between CloudWatch client and server.
- The CloudWatch AWS SDK handles the serialization (convert object to JSON format) and de-serialization (convert JSON format to object) between the CloudWatch client and server.

## What is the Smithy RPC v2 CBOR protocol, and how does it differ from existing CloudWatch API requests and responses?

Smithy RPC v2 CBOR (Concise Binary Object Representation) is a protocol developed by Amazon for more efficient data transmission. It's a data format designed to keep message sizes compact, and allow the format to evolve without requiring version negotiation between systems. The key difference from JSON encoding is that JSON uses human-readable text (like "name": "John"), while CBOR uses a binary format (sequences of 1s and 0s). This binary approach creates smaller data packages that travel faster over the network and reduces serialization time since computers process binary data directly.

- CloudWatch RPC v2 CBOR protocol acts as a mediator between CloudWatch client and server.
- The CloudWatch SDK handles the serialization (convert object to CBOR format) and deserialization (convert CBOR format to object) between the CloudWatch client and server.

## How do I get started with the newer protocols for CloudWatch?

To get started, use the latest AWS SDK/CLI version to use the latest supported protocol for CloudWatch. Upgrade your AWS SDK to the specified version or any subsequent version.

| SDK Client Protocol Support | Language     | Protocol                                                                                                                                                                                                     | SDK versions |
| --------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ |
| C++                         | RPC v2 CBOR  | [1.11.708](https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.708 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.708")                                                                              |
| Golang 2.x                  | RPC v2 CBOR  | [1.53.0](https://github.com/aws/aws-sdk-go-v2/releases/tag/service%2Fcloudwatch%2Fv1.53.0 "https://github.com/aws/aws-sdk-go-v2/releases/tag/service%2Fcloudwatch%2Fv1.53.0")                                |
| Java 1.x                    | AWS JSON 1.1 | [1.12.795](https://github.com/aws/aws-sdk-java/releases/tag/1.12.795 "https://github.com/aws/aws-sdk-java/releases/tag/1.12.795")                                                                            |
| Java 2.x                    | RPC v2 CBOR  | [2.40.6](https://github.com/aws/aws-sdk-java-v2/releases/tag/2.40.6 "https://github.com/aws/aws-sdk-java-v2/releases/tag/2.40.6")                                                                            |
| JavaScript v3.x             | AWS JSON 1.1 | [3.949.0](https://github.com/aws/aws-sdk-js-v3/releases/tag/v3.949.0 "https://github.com/aws/aws-sdk-js-v3/releases/tag/v3.949.0")                                                                           |
| .NET v3                     | AWS JSON 1.1 | [3.7.1182.0](https://github.com/aws/aws-sdk-net/releases/tag/3.7.1182.0 "https://github.com/aws/aws-sdk-net/releases/tag/3.7.1182.0")                                                                        |
| .NET v4                     | RPC v2 CBOR  | [4.0.150.0](https://github.com/aws/aws-sdk-net/releases/tag/4.0.150.0 "https://github.com/aws/aws-sdk-net/releases/tag/4.0.150.0")                                                                           |
| PHP                         | AWS JSON 1.1 | [3.367.0](https://github.com/aws/aws-sdk-php/releases/tag/3.367.0 "https://github.com/aws/aws-sdk-php/releases/tag/3.367.0")                                                                                 |
| Python-boto3                | AWS JSON 1.1 | [1.42.7](https://github.com/boto/boto3/releases/tag/1.42.7 "https://github.com/boto/boto3/releases/tag/1.42.7")                                                                                              |
| Python-botocore             | AWS JSON 1.1 | [1.42.7](https://github.com/boto/botocore/releases/tag/1.42.7 "https://github.com/boto/botocore/releases/tag/1.42.7")                                                                                        |
| AWS CLI v1                  | AWS JSON 1.1 | [1.43.13](https://github.com/aws/aws-cli/releases/tag/1.43.13 "https://github.com/aws/aws-cli/releases/tag/1.43.13")                                                                                         |
| AWS CLI v2                  | AWS JSON 1.1 | [2.32.14](https://github.com/aws/aws-cli/releases/tag/2.32.14 "https://github.com/aws/aws-cli/releases/tag/2.32.14")                                                                                         |
| Ruby                        | AWS JSON 1.1 | [1.126.0](https://github.com/aws/aws-sdk-ruby/commit/3b09588cf49079453ef372cdcd51eaab8d8114a9 "https://github.com/aws/aws-sdk-ruby/commit/3b09588cf49079453ef372cdcd51eaab8d8114a9")                         |
| Powershell                  | AWS JSON 1.1 | [5.0.114](https://github.com/aws/aws-tools-for-powershell/commit/22b7f44d079b84fd245273ea554ae57d07e8a017 "https://github.com/aws/aws-tools-for-powershell/commit/22b7f44d079b84fd245273ea554ae57d07e8a017") |
| Rust                        | RPC v2 CBOR  | [1.100.0](https://github.com/awslabs/aws-sdk-rust/releases/tag/release-2025-12-10 "https://github.com/awslabs/aws-sdk-rust/releases/tag/release-2025-12-10")                                                 |
| Swift                       | RPC v2 CBOR  | [1.6.14](https://github.com/awslabs/aws-sdk-swift/releases/tag/1.6.14 "https://github.com/awslabs/aws-sdk-swift/releases/tag/1.6.14")                                                                        |
| Kotlin                      | RPC v2 CBOR  | [1.5.100](https://github.com/aws/aws-sdk-kotlin/releases/tag/v1.5.100 "https://github.com/aws/aws-sdk-kotlin/releases/tag/v1.5.100")                                                                         |

## What are the risks of enabling these new protocols for my CloudWatch workloads?

The migration into these new SDK versions is expected to be fully transparent and effortless for customers. There is one known behavioral change in between protocols related with how `null` values are treated within lists: CloudWatch API calls with list inputs that may contain `null` values will be handled differently in the AWS JSON and Smithy RPC v2 CBOR protocols as compared to the previous AWS Query protocol: In AWS Query protocol, null values within lists are removed, while in JSON/CBOR protocols will be propagated through the API calls.

Additionally, if you are using a custom implementation of AWS SDK or a combination of custom clients and AWS SDK to interact with CloudWatch that generates AWS Query based (aka XML-based) responses, it may be incompatible with AWS JSON or CBOR protocol. If you encounter any issues, contact AWS Support.

## What if I am already on the latest AWS SDK version, but my open sourced solution does not support JSON or CBOR?

You must change your SDK version to a previous version. See the [How do I get started with the newer protocols for CloudWatch?](#getting-started "#getting-started") section and select a version lower than listed. If you change your AWS SDK to the previous version, your CloudWatch APIs will use the AWS Query protocol.

## What regions are supported for AWS JSON and CBOR protocols used in CloudWatch APIs

CloudWatch supports AWS JSON and CBOR protocol in all [AWS regions](../../../general/latest/gr/rande.md#cw_region "../../../general/latest/gr/rande.md#cw_region") where CloudWatch is available.

## What latency improvements can I expect when upgrading to the specified AWS SDK versions for CloudWatch using the newer protocols?

Both JSON and CBOR provide up to 80% lower latency and CPU usage when compared to the AWS Query. Both protocols are up to 20% more efficient in network bandwidth usage.

## Will the AWS Query protocol be deprecated?

AWS Query protocol will continue to be supported. You can continue using the AWS Query protocol as long as your AWS SDK version is set any version before what is listed in [How do I get started with the newer protocols for CloudWatch?](#getting-started "#getting-started").

## Where can I find more information about AWS JSON and Smithy RPC v2 CBOR protocols?

You can find more information about JSON protocol at [AWS JSON 1.1](https://smithy.io/2.0/aws/protocols/aws-json-1_1-protocol.html "https://smithy.io/2.0/aws/protocols/aws-json-1_1-protocol.html") protocol in the Smithy documentation, and about CBOR at [AWS RPC v2 CBOR](https://smithy.io/2.0/additional-specs/protocols/smithy-rpc-v2.html "https://smithy.io/2.0/additional-specs/protocols/smithy-rpc-v2.html") protocol in the Smithy documentation.

For more about CloudWatch API requests, see [Making API Requests](../APIReference/making-api-requests.md "../APIReference/making-api-requests.md") in the CloudWatch API Reference Guide.
