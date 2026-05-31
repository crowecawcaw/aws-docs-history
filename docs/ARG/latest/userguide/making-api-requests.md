# Making API requests

Query requests for the AWS Resource Groups are HTTP or HTTPS requests that use an HTTP verb such
as `GET` or `POST`.

## Resource Groups endpoints

An _endpoint_ is a URL that serves as an entry point
for a web service. You can select an appropriate AWS Region endpoint when you make
your requests to reduce latency. For information about the endpoints used by Resource Groups,
see [AWS Resource Groups](../../../general/latest/gr/arg.md "../../../general/latest/gr/arg.md")
in the _Amazon Web Services General Reference_.

## Query parameters

Each query request must include some common parameters to handle authentication and
selection of an action. For more information, see [Common Parameters](../APIReference/CommonParameters.md "../APIReference/CommonParameters.md") in the
_AWS Resource Groups API Reference_.

Some API operations take lists of parameters. These lists are specified using the
following notation:

```
param.member.n
```

Values of `n` are integers starting from 1. All lists of parameters must
follow this notation, including lists that contain only one parameter. A query parameter
list looks like the following example.

```
&attribute.member.1=this
&attribute.member.2=that
```

## Request identifiers

In every response from an AWS Query API, there is a `ResponseMetadata`
element, which contains a `RequestId` element. This string is a unique
identifier that AWS assigns to provide tracking information. Although
`RequestId` is included as part of every response, it isn't listed on the
individual API documentation pages to improve readability and to reduce
redundancy.

## Query API authentication

You can send query requests over either HTTP or HTTPS. Regardless of which protocol
you use, you must include a signature in every query request. For more information about
creating and including a signature, see [Signing AWS API Requests](../../../general/latest/gr/signing_aws_api_requests.md "../../../general/latest/gr/signing_aws_api_requests.md")
in the _Amazon Web Services General Reference_.

## Available libraries

AWS provides libraries, sample code, tutorials, and other resources for software
developers who prefer to build applications using language-specific APIs instead of the
command-line tools and Query API. These libraries provide basic functions (not included
in the APIs), such as request authentication, request retries, and error handling so
that it's easier to get started. Resource Groups libraries and resources are available for the
following languages and platforms:

- [AWS SDK for Go](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/resourcegroups "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/resourcegroups")
- [AWS SDK for Java 2.x](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/resourcegroups/package-summary.html "https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/resourcegroups/package-summary.html")
- [AWS SDK for Java 1.x](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/resourcegroups/package-summary.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/resourcegroups/package-summary.md")
- [AWS SDK for JavaScript](../../../AWSJavaScriptSDK/v3/latest/clients/client-resource-groups/index.md "../../../AWSJavaScriptSDK/v3/latest/clients/client-resource-groups/index.md")
- [AWS SDK for JavaScript in Node.js](../../../AWSJavaScriptSDK/v3/latest/clients/client-resource-groups/index.md "../../../AWSJavaScriptSDK/v3/latest/clients/client-resource-groups/index.md")
- [AWS SDK for .NET](../../../sdkfornet/v3/apidocs/items/ResourceGroups/NResourceGroups.md "../../../sdkfornet/v3/apidocs/items/ResourceGroups/NResourceGroups.md")
- [AWS SDK for PHP](../../../aws-sdk-php/v3/api/api-resource-groups-2017-11-27.md "../../../aws-sdk-php/v3/api/api-resource-groups-2017-11-27.md")
- [AWS SDK for Python (Boto)](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups.html")
- [AWS SDK for Ruby](https://github.com/aws/aws-sdk-ruby/tree/version-3/apis/resource-groups/2017-11-27 "https://github.com/aws/aws-sdk-ruby/tree/version-3/apis/resource-groups/2017-11-27")
- [AWS SDK for Rust](https://crates.io/crates/aws-sdk-resourcegroups "https://crates.io/crates/aws-sdk-resourcegroups")

For more information about libraries and sample code in all languages, see [Sample Code & Libraries](../../../code-library.md "../../../code-library.md").

## Making API requests using the `POST` method

If you don't use one of the AWS SDKs, you can make Resource Groups requests over HTTP
using the `POST` request method. The `POST` method requires that
you specify the operation in the header of the request and provide the data for the
operation in JSON format in the body of the request.

| Header name        | Header value                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `Host`             | The AWS Resource Groups endpoint. For example:<br>`tagging.us-east-1.amazonaws.com`                                                                                                                                                                                                                                                                                                                          |
| `X-Amz-Date`       | You must provide the timestamp in either the HTTP Date header or<br>the AWS *x-amz-date<br>• header. Some HTTP client<br>libraries don't let you set the Date header. When an<br>*x-amz-date<br>• header is present, the system<br>ignores any Date header during the request authentication.<br>The \*x-amz-date<br>• header must be specified in<br>ISO 8601 basic format. For example: `20130315T092054Z` |
| `Authorization`    | The set of authorization parameters that AWS uses to ensure the<br>validity and authenticity of the request. For more information about<br>constructing this header, see [Signature Version 4<br>Signing Process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md") in the<br>_Amazon Web Services General Reference_.                                  |
| `X-Amz-Target`     | Specifies the Resource Groups namespace and version, and the operation<br>that you want to perform.<br>`ResourceGroupsTaggingAPI_20170126.`API_Name``<br>NoteFor the Resource Groups, always use the version **`20170126`**.<br>For example, to call the `GetTagValues` operation, use<br>the following target value.<br>`ResourceGroupsTaggingAPI_20170126.GetTagValues`                                    |
| `Content-Type`     | Specifies the input format. Use the following value.<br>`application/json`                                                                                                                                                                                                                                                                                                                                   |
| `Accept`           | Specifies the response format. Use the following value.<br>`application/json`                                                                                                                                                                                                                                                                                                                                |
| `Content-Length`   | Size of the payload in bytes.                                                                                                                                                                                                                                                                                                                                                                                |
| `Content-Encoding` | Specifies the encoding format of the input and output. Use the<br>following value.<br>`amz-1.0`                                                                                                                                                                                                                                                                                                              |

The following is an example header for an HTTP request to create a resource group that
includes all resources that are tagged `Stage=Test`. In this example, the
`Authorization` line is word-wrapped here for easier reading. Don't word
wrap it in your actual request.

```
POST / HTTP/1.1
Host: resource-groups.us-east-1.amazonaws.com
X-Amz-Date: 20180112T092034Z
Accept-Encoding: identity
Authorization: AWS4-HMAC-SHA256 Credential=REDACTED/20220113/us-west-2/resource-groups/aws4_request,
        SignedHeaders=content-encoding;content-length;content-type;host;x-amz-date;x-amz-target,
        Signature=EXAMPLE5cb91f88f1EXAMPLEa02d3af93dEXAMPLE91e5d03588EXAMPLE88ff1d
Content-Type: application/json
Accept: application/json
Content-Length: 283

{
    "Description": "Resources created for the testing stage.",
    "Name": "QueryGroup",
    "ResourceQuery": {
        "Query": "{\"ResourceTypeFilters\":[\"AWS::AllSupported\"],\"TagFilters\":[{\"Key\":\"Stage\",\"Values\":[\"Test\"]}]}",
         "Type": "TAG_FILTERS_1_0"
    },
    "Tags": {"Department": "Finance"}
}
```
