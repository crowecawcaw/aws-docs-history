# Using the API for Amazon EC2

###### Important

As of **October 14, 2022**, HTTP responses from
the Amazon EC2 APIs no longer include a reason-phrase element. As recommended by
[RFC7230](https://datatracker.ietf.org/doc/html/rfc7230#section-3.1.2 "https://datatracker.ietf.org/doc/html/rfc7230#section-3.1.2"),
you should ensure that your applications do not make use of the reason-phrase content.
Ensure that your applications use the 3-digit status-code element included in the
HTTP response instead.

We provide the Query API for Amazon EC2, as well as software development kits (SDK) for AWS
that enable you to access Amazon EC2 from your preferred programming language. For more information,
see the [Amazon EC2 Developer Guide](../devguide.md "../devguide.md").

###### Contents

- [Required knowledge](#required-knowledge "#required-knowledge")
- [Available APIs for Amazon EC2](#using-libraries "#using-libraries")
- [Actions by service](OperationList-query.md "OperationList-query.md")
- [Query requests](Query-Requests.md "Query-Requests.md")
- [CORS support](cors-support.md "cors-support.md")
- [VM Import Manifest](manifest.md "manifest.md")
- [Common query parameters](#CommonParameters "#CommonParameters")
- [Permissions](ec2-api-permissions.md "ec2-api-permissions.md")
- [Troubleshooting API request errors](query-api-troubleshooting.md "query-api-troubleshooting.md")
- [Error codes](errors-overview.md "errors-overview.md")

## Required knowledge

If you plan to access Amazon EC2 through an API, you should be familiar with the
following:

- XML
- Web services
- HTTP requests
- One or more programming languages, such as Java, PHP, Perl, Python, Ruby, C#,
  or C++.

## Available APIs for Amazon EC2

The Amazon EC2 Query API provides HTTP or HTTPS requests that use the HTTP verb GET or POST
and a Query parameter named `Action`.

AWS provides libraries, sample code, tutorials, and other resources for software
developers who prefer to build applications using language-specific APIs instead of
submitting a request over HTTP or HTTPS. These libraries provide basic functions that
automatically take care of tasks such as cryptographically signing your requests,
retrying requests, and handling error responses, so that it is easier for you to get
started.

For more information, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md") in the _Amazon EC2 Developer Guide_.

## Common query parameters

Most Amazon EC2 API actions support the parameters described in the following tables. The common
parameters vary depending on whether you're using Signature Version 2 or Signature Version 4 to
sign your requests. For more information, see [Signing AWS API requests](../../../IAM/latest/UserGuide/reference_aws-signing.md "../../../IAM/latest/UserGuide/reference_aws-signing.md") in the _IAM User Guide_.

###### Contents

- [Parameters for Signature Version 4](#common-parameters-sigv4 "#common-parameters-sigv4")
- [Parameters for Signature Version 2](#common-parameters-sigv2 "#common-parameters-sigv2")

### Parameters for Signature Version 4

| Name                   | Description                                                                                                                                                                                                                                                                                                        | Required |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| `Action`               | The action to perform.<br>Example: `RunInstances`                                                                                                                                                                                                                                                                  | Yes      |
| `Version`              | The API version to use.                                                                                                                                                                                                                                                                                            | Yes      |
| `X-Amz-Algorithm`      | The hash algorithm you use to create the request signature.<br>Example: `AWS4-HMAC-SHA256`                                                                                                                                                                                                                         | Yes      |
| `X-Amz-Credential`     | The credential scope for the request, in the format<br>`access-key-ID`/`YYYYMMDD`/`region`/`service`/`aws4_request`<br>Example: `AKIDEXAMPLE/20140707/us-east-1/ec2/aws4_request`                                                                                                                                  | Yes      |
| `X-Amz-Date`           | The date and time at which the request is signed, in the format YYYYMMDDThhmmssZ. The<br>date must match the date that's included in the credential scope for the<br>`X-Amz-Credential` parameter, or the date used in an<br>`Authorization` header (see the note below the table).<br>Example: `20140707T150456Z` | Yes      |
| `X-Amz-SignedHeaders`  | The headers you are including as part of the request. At a minimum, you must include the<br>`host` header. If you include an `x-amz-date` header in your<br>request, you must include it in the list of signed headers.<br>Example: `content-type;host;user-agent`                                                 | Yes      |
| `X-Amz-Signature`      | A signature derived from your secret access key.<br>Example: `ced6826de92d2bdeed8f846f0bf508e8559example`                                                                                                                                                                                                          | Yes      |
| `X-Amz-Security-Token` | The temporary security token obtained through a call to AWS Security Token Service.<br>Example: `AQoEXAMPLEH4aoAH0gNCAPyJxz4BlCFFxWNE1OPTgk5TthT+FvwqnKwRcOIfrRh3c/L`                                                                                                                                              | No       |
| `DryRun`               | Checks whether you have the required permissions for the action, without actually making the request.<br>If you have the required permissions, the request returns `DryRunOperation`; otherwise, it<br>returns `UnauthorizedOperation`.                                                                            | No       |

The `X-Amz-Algorithm`, `X-Amz-Credential`,
`X-Amz-SignedHeaders`, and `X-Amz-Signature` parameters can either
be specified as separate parameters in the query string, or their values can be included in
a single `Authorization` header. For more information, see [Signing AWS API requests](../../../IAM/latest/UserGuide/reference_aws-signing.md "../../../IAM/latest/UserGuide/reference_aws-signing.md") in the _IAM User Guide_.

### Parameters for Signature Version 2

| Name               | Description                                                                                                                                                                                                                                                                          | Required                                                                                        |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| `Action`           | The action to perform.<br>Example: `RunInstances`                                                                                                                                                                                                                                    | Yes                                                                                             |
| `Version`          | The API version to use.                                                                                                                                                                                                                                                              | Yes                                                                                             |
| `AWSAccessKeyId`   | The access key ID for the request sender. This identifies the account which will be<br>charged for usage of the service. The account that's associated with the access key<br>ID must be signed up for Amazon EC2, or the request isn't accepted.<br>Example: `AKIAIOSFODNN7EXAMPLE` | Yes                                                                                             |
| `Expires`          | The date and time at which the signature included in the request expires, in the<br>format YYYY-MM-DDThh:mm:ssZ. For more information, see [ISO 8601](http://www.w3.org/TR/NOTE-datetime "http://www.w3.org/TR/NOTE-datetime").<br>Example: `2006-07-07T15:04:56Z`                   | Conditional. Requests must include either `Timestamp` or<br>`Expires`, but cannot contain both. |
| `Timestamp`        | The date and time at which the request is signed,<br>in the format YYYY-MM-DDThh:mm:ssZ. For more information, see<br>[ISO 8601](http://www.w3.org/TR/NOTE-datetime "http://www.w3.org/TR/NOTE-datetime").<br>Example: `2006-07-07T15:04:56Z`                                        | Conditional. Requests must include either `Timestamp` or<br>`Expires`, but cannot contain both. |
| `Signature`        | The request signature.<br>Example: `Qnpl4Qk/7tINHzfXCiT7VEXAMPLE`                                                                                                                                                                                                                    | Yes                                                                                             |
| `SignatureMethod`  | The hash algorithm you use to create the request signature. Valid values:<br>`HmacSHA256`                                                                                                                                                                                            | `HmacSHA1`.<br>Example: `HmacSHA256`                                                            | Yes |
| `SignatureVersion` | The signature version you use to sign the request. Set this value to `2`.<br>Example: `2`                                                                                                                                                                                            | Yes                                                                                             |
| `DryRun`           | Checks whether you have the required permissions for the action, without<br>actually making the request. If you have the required permissions, the request<br>returns `DryRunOperation`; otherwise, it returns<br>`UnauthorizedOperation`.                                           | No                                                                                              |
| `SecurityToken`    | The temporary security token obtained through a call to AWS Security Token Service.<br>Example: `AQoEXAMPLEH4aoAH0gNCAPyJxz4BlCFFxWNE1OPTgk5TthT+FvwqnKwRcOIfrRh3c/L`                                                                                                                | No                                                                                              |

Parameter values must be URL-encoded. This is true for any Query parameter passed to Amazon EC2
and is typically necessary in the `Signature` parameter. Some clients do
this automatically, but this is not the norm.
