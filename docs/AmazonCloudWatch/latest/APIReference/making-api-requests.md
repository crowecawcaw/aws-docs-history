# Making API Requests

Query requests used with Amazon CloudWatch are HTTP or HTTPS requests that use the an HTTP verb such 
 as GET or
 POST, and a Query parameter named `Action` or `Operation`. This
 documentation uses `Action`, although `Operation` is supported for
 backward compatibility.

CloudWatch does not care which HTTP verb you use in a request. 
 POST requests, GET requests, PUT requests, DELETE requests and so on all return the same result.

## Amazon CloudWatch Endpoints


An endpoint is a URL that serves as an entry point for a web service. You can select a
 regional endpoint when you make your requests to reduce latency. For information about
 the endpoints used with CloudWatch, see [Regions and
 Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html "https://docs.aws.amazon.com/general/latest/gr/rande.html") in the *Amazon Web Services General Reference*.


## Query Parameters


Each query request must include some common parameters to handle authentication and
 selection of an action. For more information, see [Common Parameters](CommonParameters.md "CommonParameters.md").


Some API operations take lists of parameters. These lists are specified using the
 following notation: `param.member.n.` Values of n are integers starting
 from 1. All lists of parameters must follow this notation, including lists that
 contain only one parameter. For example, a Query parameter list looks like
 this:



```
&attribute.member.1=this
&attribute.member.2=that
```

## Request Identifiers


In every response from an AWS Query API, there is a `ResponseMetadata`
 element, which contains a `RequestId` element. This string is a unique
 identifier that AWS assigns to provide tracking information. Although
 `RequestId` is included as part of every response, it is not listed on
 the individual API documentation pages to improve readability and to reduce
 redundancy.


## Query API Authentication


You can send query requests over either HTTP or HTTPS. Regardless of which protocol
 you use, you must include a signature in every query request. For more information 
 about creating and including a signature, see [Signing AWS API Requests](https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html "https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html") 
 in the *Amazon Web Services General Reference*.


## Available Libraries


AWS provides libraries, sample code, tutorials, and other resources for software
 developers who prefer to build applications using language-specific APIs instead of the
 command-line tools and Query API. These libraries provide basic functions (not included
 in the APIs), such as request authentication, request retries, and error handling so
 that it is easier to get started. Libraries and resources are available for the
 following languages and platforms:



* [AWS Mobile SDK for Android](https://docs.aws.amazon.com/mobile/sdkforandroid/developerguide/ "https://docs.aws.amazon.com/mobile/sdkforandroid/developerguide/")
* [AWS SDK for Go](https://docs.aws.amazon.com/sdk-for-go/latest/developer-guide/ "https://docs.aws.amazon.com/sdk-for-go/latest/developer-guide/")
* [AWS Mobile SDK for iOS](https://docs.aws.amazon.com/mobile/sdkforios/developerguide/ "https://docs.aws.amazon.com/mobile/sdkforios/developerguide/")
* [AWS SDK for Java 2.x](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ "https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/")
* [AWS SDK for Java](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ "https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/")
* [AWS SDK for JavaScript](https://docs.aws.amazon.com/sdk-for-javascript/latest/developer-guide/ "https://docs.aws.amazon.com/sdk-for-javascript/latest/developer-guide/")
* [AWS SDK for JavaScript in Node.js](https://docs.aws.amazon.com/AWSJavaScriptSDK/guide/node-intro.html "https://docs.aws.amazon.com/AWSJavaScriptSDK/guide/node-intro.html")
* [AWS SDK for .NET](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/ "https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/")
* [AWS SDK for PHP](https://docs.aws.amazon.com/aws-sdk-php/v2/guide/index.html#getting-started "https://docs.aws.amazon.com/aws-sdk-php/v2/guide/index.html#getting-started")
* [AWS SDK for Python (Boto)](http://boto.readthedocs.org/en/latest/ "http://boto.readthedocs.org/en/latest/")
* [AWS SDK for Ruby](https://docs.aws.amazon.com/sdk-for-ruby/latest/developer-guide/ "https://docs.aws.amazon.com/sdk-for-ruby/latest/developer-guide/")

For libraries and sample code in all languages, see [Sample Code & Libraries](http://aws.amazon.com/code "http://aws.amazon.com/code").


## Making API Requests Using the POST Method


If you don't use one of the AWS SDKs, you can make CloudWatch API requests over HTTP using the POST request method. 
 The POST method requires you to specify the operation in the header of the request and provide the data for the 
 operation in JSON format in the body of the request.




| Header name | Header value |
| --- | --- |
| *host* | The Amazon CloudWatch endpoint. For example, `monitoring.us-west-1.amazonaws.com`  |
| *x-amz-date* | You must provide the time stamp in either the HTTP Date header or the AWS *x-amz-date* header. Some HTTP client libraries don't let you set the Date header. When an *x-amz-date* header is present, the system ignores any Date header during the request authentication. The *x-amz-date* header must be specified in ISO 8601 basic format. For example: `20130315T092054Z`  |
| *Authorization* | The set of authorization parameters that AWS uses to ensure the validity and authenticity of the request. For more information about constructing this header, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html "https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html") in the *Amazon Web Services General Reference*. |
| *x-amz-target* | Specifies the CloudWatch operation: `GraniteServiceVersion20100801.`API_Name`` For example, for GetMetricData the target value is the following: `GraniteServiceVersion20100801.GetMetricData` |
| *Content-Type* | Specifies the input format. The valid value is `application/json` |
| *Accept* | Specifies the response format. The valid value is `application/json` |
| *Content-length* | Size of the payload in bytes. |
| *Content-Encoding* | Specifies the encoding format of the input and output. The valid value is `amz-1.0` | The following is an example header for an HTTP request to return metric data in JSON format: ``` POST / HTTP/1.1 host: monitoring.us-east-1.amazonaws.com x-amz-target: GraniteServiceVersion20100801.GetMetricData x-amz-date: 20180112T092034Z Authorization: AWS4-HMAC-SHA256 Credential=REDACTEDREDACTED/20180411/us-east-1/monitoring/aws4_request, SignedHeaders=content-encoding;content-length;content-type;host;x-amz-date;x-amz-target, Signature=e945ed75cb91f88f138445fba02d3af93d96bfd8491e5d03588ae1b65188ff1d Content-Type: application/json Accept: application/json Content-Encoding: amz-1.0 Content-Length: 45 Connection: keep-alive ```
