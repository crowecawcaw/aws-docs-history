

# Request signature examples
<a name="reference_sigv-examples"></a>

The following examples of AWS signing requests show you how you can use SigV4 to sign requests sent without the AWS SDK or AWS command line tool.

## Browser based Amazon S3 upload using HTTP POST
<a name="signature-v4-examples-s3-browser"></a>

 [Authenticating Requests: Browser-Based Uploads](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-authentication-HTTPPOST.html) describes the signature and relevant information that Amazon S3 uses to calculate the signature upon receiving the request.

[Example: Browser-Based Upload using HTTP POST (Using AWS Signature Version 4)](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-post-example.html) provides more information with a sample POST policy and a form that you can use to upload a file. The example policy and fictitious credentials show you the workflow and resulting signature and policy hash.

## VPC Lattice authenticated requests
<a name="signature-v4-examples-lattice"></a>

 [Examples for Signature Version 4 (SigV4) authenticated requests](https://docs.aws.amazon.com/vpc-lattice/latest/ug/sigv4-authenticated-requests.html) provides Python and Java examples showing how you can perform request signing with and without custom interceptors.

## Using Signature Version 4 with Amazon Translate
<a name="signature-v4-examples-translate"></a>

 [Live Translations in the Metaverse](https://aws.amazon.com/blogs/spatial/live-translations-in-the-metaverse/) shows how to build an application that produces a near real-time translation solution. This speech-to-speech translator solution uses AWS SigV4 in event stream encoding to produce real-time transcriptions.

## Using Signature Version 4 with Neptune
<a name="signature-v4-examples-neptune"></a>

[Example: Connecting to Neptune Using Python with Signature Version 4 Signing](https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth-connecting-python.html) shows how to make signed requests to Neptune using Python. This example includes variations for using an access key or temporary credentials.

## Signing HTTP requests to Amazon Glacier
<a name="signature-v4-examples-streaming-glacier"></a>

[Example Signature Calculation for Streaming API](https://docs.aws.amazon.com/amazonglacier/latest/dev/amazon-glacier-signing-requests.html) walks you through the details of creating a signature for Upload Archive (POST archive), one of the two streaming APIs in Amazon Glacier.

## Making HTTP Requests to Amazon SWF
<a name="signature-v4-examples-swf"></a>

[Making HTTP Requests to Amazon SWF](https://docs.aws.amazon.com/amazonswf/latest/developerguide/UsingJSON-swf.html#HTTPHeader) shows the header contents for a JSON request to Amazon SWF.

## Signature calculation for streaming APIs in Amazon OpenSearch Service
<a name="signature-v4-examples-open-search"></a>

[Signing an Amazon OpenSearch Service search request with AWS SDK for PHP Version 3](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/service_es-data-plane.html) includes an example of how to send signed HTTP requests to Amazon OpenSearch Service.

## Example projects in AWS samples repository
<a name="signature-v4-examples-sdk"></a>

The following example projects show how to sign requests to make Rest API requests to AWS services with common languages such as Python, Node.js, Java, C\#, Go and Rust. 

### Signature Version 4a projects
<a name="signature-v4-examples-sigv4a"></a>

The [sigv4-signing-examples](https://github.com/aws-samples/sigv4-signing-examples) project provides examples of how to sign requests with SigV4 to make Rest API requests to AWS services with common languages such as Python, Node.js, Java, C\#, Go and Rust.

The [sigv4a-signing-examples](https://github.com/aws-samples/sigv4a-signing-examples) project provides examples for signing multi-Region API requests, for example [ Multi-Region Access Points in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPoints.html).

### Publish to AWS IoT Core
<a name="signature-v4-examples-iot-python"></a>

[Python code to publish to AWS IoT Core using HTTPs protocol](https://github.com/aws-samples/aws-iot-core-python-node-sigv4-https) provides guidance on how to publish messages to AWS IoT Core using HTTPS protocol and AWS SigV4 authentication. It has two reference implementations - one in Python and other in NodeJs.

[.Net Framework application to publish to AWS IoT Core using HTTPs protocol](https://github.com/aws-samples/aws-iot-core-http-sigv4-dotnet-app) provides guidance on how to publish messages to AWS IoT Core using HTTPS protocol and AWS SigV4 authentication. This project also includes a .NET core equivalent implementation.