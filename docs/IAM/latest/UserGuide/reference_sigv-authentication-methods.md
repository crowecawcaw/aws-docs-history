# Authentication methods

###### Important

Unless you are using the AWS SDKs or CLI, you must write code to calculate
signatures that provide authentication information in your requests. Signature
calculation in AWS Signature Version 4 can be a complex undertaking, and we recommend
that you use the AWS SDKs or CLI whenever possible.

You can express authentication information by using one of the following methods.

## HTTP authorization header

The HTTP `Authorization` header is the most common method of authenticating
a request. All REST API operations (except for browser-based uploads using
`POST` requests) require this header.

The following examples show the `Authorization` header value for SigV4 and
SigV4a. Line breaks are added to this example for readability. In your code, the header
must be a continuous string. There is no comma between the algorithm and Credential, but
the other elements must be separated by commas.

###### Example SigV4

```
Authorization: AWS4-HMAC-SHA256
Credential=AKIAIOSFODNN7EXAMPLE/20130524/us-east-1/s3/aws4_request,
SignedHeaders=host;range;x-amz-date,
Signature=fe5f80f77d5fa3beca038a248ff027d0445342fe2855ddc963176630326f1024
```

###### Example SigV4a

```
Authorization: AWS4-ECDSA-P256-SHA256
Credential=AKIAIOSFODNN7EXAMPLE/20130524/s3/aws4_request,
SignedHeaders=host;range;x-amz-date;x-amz-region-set,
Signature=fe5f80f77d5fa3beca038a248ff027d0445342fe2855ddc963176630326f1024
```

The following table describes the various components of the Authorization header value
in the preceding example:

| Component     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Authorization | The algorithm that was used to calculate the signature.<br>• SigV4 – Use `AWS4-HMAC-SHA256`. This<br>string identifies AWS SigV4 (`AWS4`) and the<br>`HMAC-SHA256` algorithm.<br>• SigV4a – Use `AWS4-ECDSA-P256-SHA256`.<br>This string identifies AWS SigV4 (`AWS4`) and<br>the `ECDSA-P256-SHA-256` algorithm.                                                                                                                                                                                                                                                                  |
| Credential    | Your access key ID and the scope information.<br>• SigV4 – Include the date, Region, and service that<br>were used to calculate the signature. This string has the<br>following form:<br>`<your-access-key-id>/<date>/<aws-region>/<aws-service>/aws4_request`<br>• SigV4a – Include the date and service that were<br>used to calculate the signature. This string has the<br>following form:<br>`<your-access-key-id>/<date>/<aws-service>/aws4_request`<br>The <date> value is specified using YYYYMMDD format.<br><aws-service> value is S3 when sending request to Amazon S3. |
| SignedHeaders | A semicolon-separated list of request headers that you used to<br>compute Signature. The list includes header names only, and the<br>header names must be in lowercase. For example:<br>`host;range;x-amz-date`<br>For SigV4a, you must include a region set header that specifies<br>the set of regions the request will be valid in. The header<br>X-Amz-Region-Set is specified as a list of comma separated<br>values.                                                                                                                                                         |
| Signature     | The 256-bit signature expressed as 64 lowercase hexadecimal<br>characters. For<br>example:`fe5f80f77d5fa3beca038a248ff027d0445342fe2855ddc963176630326f1024`<br>Note that the signature calculations vary depending on the option<br>you choose to transfer the payload.                                                                                                                                                                                                                                                                                                           |

## Query string

parameters

You can use a query string to express a request entirely in a URL. In this case, you
use query parameters to provide request information, including the authentication
information. Because the request signature is part of the URL, this type of URL is often
referred to as a presigned URL. You can use presigned URLs to embed clickable links in
HTML, which can be valid for up to seven days. For more information, see [Authenticating Requests: Using Query Parameters (AWS Signature Version 4)](../../../AmazonS3/latest/API/sigv4-query-string-auth.md "../../../AmazonS3/latest/API/sigv4-query-string-auth.md")
in the _Amazon S3 API Reference_.

The following examples show presigned URLs for SigV4 and SigV4a. Line breaks are added
to this example for readability:

###### Example SigV4

```
https://s3.amazonaws.com/amzn-s3-demo-bucket/test.txt ?
X-Amz-Algorithm=AWS4-HMAC-SHA256 &
X-Amz-Credential=<your-access-key-id>/20130721/<region>/s3/aws4_request &
X-Amz-Date=20130721T201207Z &
X-Amz-Expires=86400 &
X-Amz-SignedHeaders=host &X-Amz-Signature=<signature-value>
```

###### Example SigV4a

```
http://s3.amazonaws.com/amzn-s3-demo-bucket/test.txt ?
X-Amz-Algorithm=AWS4-ECDSA-P256-SHA256 &
X-Amz-Credential=<your-access-key-id>/20240721/s3/aws4_request &
X-amz-Region-Set=<regionset> &
X-Amz-Date=20240721T201207Z &
X-Amz-Expires=86400 &
X-Amz-SignedHeaders=host;x-amz-region-set &
X-Amz-Signature=<signature-value>
```

###### Note

The `X-Amz-Credential` value in the URL shows the "/" character only
for readability. In practice, it should be encoded as %2F. For example:

`&X-Amz-Credential=<your-access-key-id>%2F20130721%2Fus-east-1%2Fs3%2Faws4_request`

The following table describes the query parameters in the URL that provide
authentication information.

| Query string parameter name | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| X-Amz-Algorithm             | The version of AWS signature and the algorithm that you used to<br>calculate the signature.<br>• SigV4 – Use `AWS4-HMAC-SHA256`. This<br>string identifies AWS SigV4 (`AWS4`) and the<br>`HMAC-SHA256` algorithm.<br>• SigV4a – Use `AWS4-ECDSA-P256-SHA256`.<br>This string identifies AWS SigV4 (`AWS4`) and<br>the `ECDSA-P256-SHA-256` algorithm.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| X-Amz-Credential            | In addition to your access key ID, this parameter also provides<br>scope for which the signature is valid. This value must match the<br>scope you use in signature calculations, discussed in the following<br>section.<br>• SigV4 – The general form for this parameter value<br>is as follows:<br>`<your-access-key-id>/<date>/<AWS<br>Region>/<AWS-service>/aws4_request`<br>For example:<br>`AKIAIOSFODNN7EXAMPLE/20130721/us-east-1/s3/aws4_request`<br>• SigV4a – The general form for this parameter value<br>is as follows:<br>`<your-access-key-id>/<date>/<AWS-service>/aws4_request`<br>For example:<br>`AKIAIOSFODNN7EXAMPLE/20130721/s3/aws4_request`<br>The region for SigV4a is defined in the region set header<br>`X-Amz-Region-Set`.<br>For a list of AWS regional strings, see [Regional<br>Endpoints](../../../general/latest/gr/rande.md#regional-endpoints "../../../general/latest/gr/rande.md#regional-endpoints") in the _AWS General<br>Reference_. |
| X-Amz-Region-Set            | The set of regions the request will be valid in. The header<br>x-amz-region-set is specified as a list of comma separated<br>values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| X-Amz-Date                  | The date and time format must follow the ISO 8601 standard, and<br>must be formatted with the `yyyyMMddTHHmmssZ` format. For<br>example if the date and time was "08/01/2016 15:32:41.982-700" then<br>it must first be converted to UTC (Coordinated Universal Time) and<br>then submitted as "20160801T223241Z".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| X-Amz-Expires               | Provides the time period, in seconds, for which the generated<br>presigned URL is valid. For example, 86400 (24 hours). This value is<br>an integer. The minimum value you can set is 1, and the maximum is<br>604800 (seven days).A presigned URL can be valid for a maximum of<br>seven days because the signing key you use in signature calculation<br>is valid for up to seven days.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| X-Amz-SignedHeaders         | Lists the headers that you used to calculate the signature. The<br>following headers are required in the signature calculations:<br>• The HTTP host header.<br>• Any x-amz-\* headers that you plan to add to the<br>request.<br>• For SigV4a, X-Amz-Region-Set is required to specify the<br>regions in which the request can be made.<br>For added security, you should sign all the request headers that<br>you plan to include in your request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| X-Amz-Signature             | Provides the signature to authenticate your request. This<br>signature must match the signature the service calculates;<br>otherwise, the service denies the request. For example,<br>`733255ef022bec3f2a8701cd61d4b371f3f28c9f193a1f02279211d48d5193d7`<br>Signature calculations are described in the following<br>section.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| X-Amz-Security-Token        | Optional credential parameter if using credentials sourced from<br>the STS service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
