# Request signature examples

The following examples of AWS signing requests show you how you can use SigV4 to
sign requests sent without the AWS SDK or AWS command line tool.

## Browser based Amazon S3 upload using

HTTP POST

[Authenticating
Requests: Browser-Based Uploads](../../../AmazonS3/latest/API/sigv4-authentication-HTTPPOST.md "../../../AmazonS3/latest/API/sigv4-authentication-HTTPPOST.md") describes the signature and relevant
information that Amazon S3 uses to calculate the signature upon receiving the
request.

[Example: Browser-Based Upload using HTTP POST (Using AWS Signature Version 4)](../../../AmazonS3/latest/API/sigv4-post-example.md "../../../AmazonS3/latest/API/sigv4-post-example.md") provides more information with a sample POST policy and a form that
you can use to upload a file. The example policy and fictitious credentials show you
the workflow and resulting signature and policy hash.

## VPC Lattice authenticated

requests

[Examples for
Signature Version 4 (SigV4) authenticated requests](../../../vpc-lattice/latest/ug/sigv4-authenticated-requests.md "../../../vpc-lattice/latest/ug/sigv4-authenticated-requests.md") provides Python and
Java examples showing how you can perform request signing with and without custom
interceptors.

## Using Signature Version 4 with

Amazon Translate

[Live
Translations in the Metaverse](https://aws.amazon.com/blogs/spatial/live-translations-in-the-metaverse/ "https://aws.amazon.com/blogs/spatial/live-translations-in-the-metaverse/") shows how to build an application that
produces a near real-time translation solution. This speech-to-speech translator
solution uses AWS SigV4 in event stream encoding to produce real-time
transcriptions.

## Using Signature Version 4 with

Neptune

[Example:
Connecting to Neptune Using Python with Signature Version 4 Signing](../../../neptune/latest/userguide/iam-auth-connecting-python.md "../../../neptune/latest/userguide/iam-auth-connecting-python.md")
shows how to make signed requests to Neptune using Python. This example includes
variations for using an access key or temporary credentials.

## Signing HTTP requests to

Amazon Glacier

[Example
Signature Calculation for Streaming API](../../../amazonglacier/latest/dev/amazon-glacier-signing-requests.md "../../../amazonglacier/latest/dev/amazon-glacier-signing-requests.md") walks you through the details of
creating a signature for Upload Archive (POST archive), one of the two streaming
APIs in Amazon Glacier.

## Making HTTP Requests to Amazon SWF

[Making HTTP
Requests to Amazon SWF](../../../amazonswf/latest/developerguide/UsingJSON-swf.md#HTTPHeader "../../../amazonswf/latest/developerguide/UsingJSON-swf.md#HTTPHeader") shows the header contents for a JSON request to
Amazon SWF.

## Signature calculation for

streaming APIs in Amazon OpenSearch Service

[Signing an
Amazon OpenSearch Service search request with AWS SDK for PHP Version 3](../../../sdk-for-php/v3/developer-guide/service_es-data-plane.md "../../../sdk-for-php/v3/developer-guide/service_es-data-plane.md") includes an
example of how to send signed HTTP requests to Amazon OpenSearch Service.

## Example projects in AWS samples

repository

The following example projects show how to sign requests to make Rest API requests
to AWS services with common languages such as Python, Node.js, Java, C#, Go and
Rust.

### Signature Version 4a

projects

The [sigv4-signing-examples](https://github.com/aws-samples/sigv4-signing-examples "https://github.com/aws-samples/sigv4-signing-examples") project provides examples of how to sign
requests with SigV4 to make Rest API requests to AWS services with common
languages such as Python, Node.js, Java, C#, Go and Rust.

The [sigv4a-signing-examples](https://github.com/aws-samples/sigv4a-signing-examples "https://github.com/aws-samples/sigv4a-signing-examples") project provides examples for signing
multi-Region API requests, for example [Multi-Region
Access Points in Amazon S3](../../../AmazonS3/latest/userguide/MultiRegionAccessPoints.md "../../../AmazonS3/latest/userguide/MultiRegionAccessPoints.md").

### Publish to AWS IoT Core

[Python code to publish to AWS IoT Core using HTTPs protocol](https://github.com/aws-samples/aws-iot-core-python-node-sigv4-https "https://github.com/aws-samples/aws-iot-core-python-node-sigv4-https") provides
guidance on how to publish messages to AWS IoT Core using HTTPS protocol and AWS
SigV4 authentication. It has two reference implementations - one in Python and
other in NodeJs.

[.Net Framework application to publish to AWS IoT Core using HTTPs
protocol](https://github.com/aws-samples/aws-iot-core-http-sigv4-dotnet-app "https://github.com/aws-samples/aws-iot-core-http-sigv4-dotnet-app") provides guidance on how to publish messages to AWS IoT Core
using HTTPS protocol and AWS SigV4 authentication. This project also includes
a .NET core equivalent implementation.
