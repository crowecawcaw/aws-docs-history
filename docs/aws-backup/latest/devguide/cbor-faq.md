# FAQs on supported protocols

The AWS Backup Gateway service is adding SDK support for the
[Smithy RPC v2 CBOR](https://smithy.io/2.0/additional-specs/protocols/smithy-rpc-v2.html "https://smithy.io/2.0/additional-specs/protocols/smithy-rpc-v2.html")
protocol in addition to the existing
[AWS JSON](https://smithy.io/2.0/aws/protocols/aws-json-1_0-protocol.html "https://smithy.io/2.0/aws/protocols/aws-json-1_0-protocol.html")
protocol. The Smithy RPC v2 CBOR protocol is more performant
than AWS JSON for most workloads. AWS SDKs will prioritize
the protocol that is the most performant for each language.

## What are the AWS JSON and Smithy RPC v2 CBOR protocols, and how do they differ?

A wire protocol acts as a mediator between a client and the
service. The AWS SDK handles the serialization (converting
an object to the wire format) and deserialization (converting
the wire format back to an object) between the client and
server transparently for both protocols.

**AWS JSON** - JSON is one of
the most widely used and accepted data formats for
communication between systems. This service uses AWS JSON
as a medium to communicate between an AWS SDK client and
the server. An HTTP request for a service API operation
accepts input in the form of JSON, the operation is executed,
and the response is returned to the SDK client in the form
of JSON.

**Smithy RPC v2 CBOR** - Smithy
RPC v2 CBOR (Concise Binary Object Representation) is a
protocol developed by Amazon for more efficient data
transmission. It is a data format designed to keep message
sizes compact and to allow the format to evolve without
requiring version negotiation between systems. The key
difference from AWS JSON is that AWS JSON uses
human-readable text (like `{"name": "John"}`),
while Smithy RPC v2 CBOR uses a binary format (sequences of
1s and 0s). This binary approach creates smaller data
packages that travel faster over the network and reduces
serialization time since computers process binary data
directly.

## How do I get started with the Smithy RPC v2 CBOR protocol?

To get started, use the latest AWS SDK/CLI version to use
the Smithy RPC v2 CBOR protocol for this service. The SDK
will automatically use the Smithy RPC v2 CBOR protocol when
available. Upgrade your AWS SDK to the specified version or
any subsequent version.

Starting 2026-07-23, the following AWS SDKs will use
the Smithy RPC v2 CBOR protocol, while the other SDKs will
continue using the AWS JSON protocol:

- AWS SDK for C++
- AWS SDK for Go V2
- AWS SDK for Java 2.x
- AWS SDK for .NET v4
- AWS Tools for PowerShell v5
- AWS SDK for Swift
- AWS SDK for Kotlin

## What are the risks of enabling the Smithy RPC v2 CBOR protocol?

The added support of Smithy RPC v2 CBOR in the SDKs is
expected to be fully transparent and effortless for customers.
However, if you are using a custom implementation of the
AWS SDK, or a combination of custom clients and the AWS
SDK, that depends on AWS JSON-specific serialization
behavior, it may be incompatible with the Smithy RPC v2 CBOR
protocol.

## What if my solution does not support Smithy RPC v2 CBOR?

To use the AWS JSON protocol, downgrade your SDK to a
version released before 2026-07-23.

## What AWS Regions support the Smithy RPC v2 CBOR protocol?

The Smithy RPC v2 CBOR protocol is supported in all
[AWS Regions](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md")
where this service is available.

## What latency improvements can I expect when upgrading to SDK versions that support Smithy RPC v2 CBOR?

Smithy RPC v2 CBOR provides up to 13% lower latency and up
to 15% reduction in payload size compared to AWS JSON. The
binary encoding eliminates the overhead of JSON text parsing
and string escaping, which reduces both network transfer time
and serialization cost.

## Will the AWS JSON protocol be deprecated?

AWS JSON protocol will continue to be supported through
older versions of SDKs. Also, some language-specific SDKs
will continue using AWS JSON as it is more performant than
Smithy RPC v2 CBOR due to the available JSON implementation
for the language being faster than its CBOR implementation.

## Where can I find more information about Smithy RPC v2 CBOR?

You can find more information about the AWS JSON protocol at
[AWS JSON 1.0 protocol](https://smithy.io/2.0/aws/protocols/aws-json-1_0-protocol.html "https://smithy.io/2.0/aws/protocols/aws-json-1_0-protocol.html")
and
[AWS JSON 1.1 protocol](https://smithy.io/2.0/aws/protocols/aws-json-1_1-protocol.html "https://smithy.io/2.0/aws/protocols/aws-json-1_1-protocol.html")
in the Smithy documentation, and about Smithy RPC v2 CBOR at
[Smithy RPC v2 CBOR protocol](https://smithy.io/2.0/additional-specs/protocols/smithy-rpc-v2.html "https://smithy.io/2.0/additional-specs/protocols/smithy-rpc-v2.html")
in the Smithy documentation.
