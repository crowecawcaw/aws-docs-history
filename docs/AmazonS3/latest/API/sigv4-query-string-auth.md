# Authenticating Requests: Using Query Parameters (AWS
 Signature Version 4)

As described in the authentication overview (see [Authentication Methods](sig-v4-authenticating-requests.md#auth-methods-intro "sig-v4-authenticating-requests.md#auth-methods-intro")), you can provide authentication information
 using query string parameters. Using query parameters to authenticate requests is useful
 when you want to express a request entirely in a URL. This method is also referred as
 presigning a URL. 

A use case scenario for presigned URLs is that you can grant temporary access to your Amazon
 S3 resources. For example, you can embed a presigned URL on your website or
 alternatively use it in command line client (such as Curl) to download objects.

###### Note

You can also use the AWS CLI to create presigned URLs. For more information, see 
 [`presign`](https://docs.aws.amazon.com/cli/latest/reference/s3/presign.html "https://docs.aws.amazon.com/cli/latest/reference/s3/presign.html") in the 
 *AWS CLI Command Reference*.

The following is an example presigned URL. 





```
https://examplebucket.s3.amazonaws.com/test.txt
?X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=`<your-access-key-id>`/20130721/us-east-1/s3/aws4_request
&X-Amz-Date=20130721T201207Z
&X-Amz-Expires=86400
&X-Amz-SignedHeaders=host
&X-Amz-Signature=`<signature-value>`  
```
In the example URL, note the following:





* The line feeds are added for readability.
* The `X-Amz-Credential` value in the URL shows the "/" character
 only for readability. In practice, it should be encoded as `%2F`. For example:






```
&X-Amz-Credential=`<your-access-key-id>`%2F20130721%2Fus-east-1%2Fs3%2Faws4_request
```
The following table describes the query parameters in the URL that provide authentication
 information. 



| Query String Parameter Name | Example Value |
| --- | --- |
| `X-Amz-Algorithm` | Identifies the version of AWS Signature and the algorithm that you
 used to calculate the signature. 
For AWS Signature Version 4, you set this parameter value to
 `AWS4-HMAC-SHA256`. This string identifies AWS
 Signature Version 4 (AWS4) and the HMAC-SHA256 algorithm
 (HMAC-SHA256).  |
| `X-Amz-Credential` | In addition to your access key ID, this parameter also provides scope (AWS Region and
 service) for which the signature is valid. This value must match the
 scope you use in signature calculations, discussed in the following
 section. The general form for this parameter value is as
 follows:


```
`<your-access-key-id>`/`<date>`/`<AWS Region>`/`<AWS-service>`/aws4_request
```

For example: 


```
`AKIAIOSFODNN7EXAMPLE/20130721/us-east-1/s3/aws4_request`
```

For Amazon S3, the `AWS-service` string is
 `s3`. For a list of S3 `AWS-region` strings, see
 [Regions and
 Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region "https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region") in the *AWS General Reference*. |
| `X-Amz-Date` | The date and time format must follow the ISO 8601 standard, and
 must be formatted with the
 "`yyyyMMdd`T`HHmmss`Z"
 format. For example if the date and time was "08/01/2016
 15:32:41.982-700" then it must first be converted to UTC
 (Coordinated Universal Time) and then submitted as
 "20160801T223241Z".  |
| `X-Amz-Expires` | Provides the time period, in seconds, for which the generated
 presigned URL is valid. For example, `86400` (24 hours).
 This value is an integer. The minimum value you can set is 1, and
 the maximum is 604800 (seven days).
A presigned URL can be valid for a maximum of seven days because
 the signing key you use in signature calculation is valid for up to
 seven days.  |
| `X-Amz-SignedHeaders` | Lists the headers that you used to calculate the signature. The following headers are
 required in the signature calculations:


* The HTTP `host` header.
* Any `x-amz-*` headers that you plan to add
 to the request.


Note For added security, you should sign all the request
 headers that you plan to include in your request. |
| `X-Amz-Signature` | Provides the signature to authenticate your request. This
 signature must match the signature Amazon S3 calculates; otherwise, Amazon S3
 denies the request. For example, `733255ef022bec3f2a8701cd61d4b371f3f28c9f193a1f02279211d48d5193d7`
Signature calculations are described in the following
 section. |
| `X-Amz-Security-Token` | Optional credential parameter if using credentials sourced from the STS service. |

## Calculating a Signature


The following diagram illustrates the signature calculation process. 






![Diagram showing AWS request signing process with Canonical Request, StringToSign, and Signature steps.](../../../images/AmazonS3/latest/API/images/sigV4-using-query-params.png)


The following table describes the functions that are shown in the diagram. 
 You need to implement code for these functions.




| Function | Description |
| --- | --- |
| `Lowercase()` | Convert the string to lowercase. |
| `Hex()` | Lowercase base 16 encoding. |
| `SHA256Hash()` | Secure Hash Algorithm (SHA) cryptographic hash function. |
| `HMAC-SHA256()` | Computes HMAC by using the SHA256 algorithm with the signing key provided. This is the final signature. |
| `Trim()` | Remove any leading or trailing whitespace.  |
| `UriEncode()` | URI encode every byte. UriEncode() must enforce the following rules:

* URI encode every byte except the unreserved
 characters: 'A'-'Z', 'a'-'z', '0'-'9', '-', '.',
 '\_', and '~'.
* The space character is a reserved character and must be
 encoded as "%20" (and not as "+").
* Each URI encoded byte is formed by a '%' and the
 two-digit hexadecimal value of the byte.
* Letters in the hexadecimal value must be uppercase, for
 example "%1A".
* Encode the forward slash character, '/', everywhere 
 except in
 the object key name. For example, if the object key name is
 `photos/Jan/sample.jpg`, the forward
 slash in the key name is not encoded.

ImportantThe standard UriEncode functions provided by your development platform may not work
 because of differences in implementation and
 related ambiguity in the underlying RFCs. We recommend that you write your own custom UriEncode
 function to ensure that your encoding will
 work.
To see an example of a UriEncode function in Java, see
 [Java Utilities](https://github.com/aws/aws-sdk-java/blob/master/aws-java-sdk-core/src/main/java/com/amazonaws/util/SdkHttpUtils.java#L66 "https://github.com/aws/aws-sdk-java/blob/master/aws-java-sdk-core/src/main/java/com/amazonaws/util/SdkHttpUtils.java#L66")
 on the GitHub website. |


For more information about the signing process (details of creating a canonical request,
 string to sign, and signature calculations), see [Signature Calculations for the Authorization Header:
 Transferring Payload in a Single Chunk (AWS Signature Version 4)](sig-v4-header-based-auth.md "sig-v4-header-based-auth.md").
 The process is generally the same except that the creation of
 **CanonicalRequest** in a presigned URL differs as
 follows:






* You don't include a payload hash in the **Canonical Request**, because
 when you create a presigned URL, you don't know the payload content
 because the URL is used to upload an arbitrary payload. Instead, you use
 a constant string `UNSIGNED-PAYLOAD`.
* The **Canonical Query String** must include all the
 query parameters from the preceding table except for
 `X-Amz-Signature`.
* For S3, you must include the `X-Amz-Security-Token` query parameter in the URL if using credentials sourced from the STS service.
* **Canonical Headers** must include the HTTP
 `host` header. If you plan to include any of the
 `x-amz-*`  headers, these headers must also be added for
 signature calculation. You can optionally add all other headers that you
 plan to include in your request. For added security, you should sign as
 many headers as possible. If you add a signed header that is also a
 signed query parameter, and they differ in value, you will receive an
 `InvalidRequest` error as the input is conflicting.

## An Example


Suppose you have an object `test.txt` in your
 `examplebucket` bucket. You want to share this object with others for
 a period of 24 hours (86400 seconds) by creating a presigned URL. 






```
https://examplebucket.s3.amazonaws.com/test.txt
?X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE%2F20130524%2Fus-east-1%2Fs3%2Faws4_request
&X-Amz-Date=20130524T000000Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host
&X-Amz-Signature=`<signature-value>`
```

The following steps illustrate first the signature calculations and then
 construction of the presigned URL. The example makes the following additional
 assumptions:






* Request timestamp is `Fri, 24 May 2013 00:00:00
 GMT`.
* The bucket is in the US East (N. Virginia) region,
 and the credential `Scope` and the `Signing
 Key` calculations use `us-east-1` as the region
 specifier. 
 For more information, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region "https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region") in
 the *AWS General Reference*.

You can use this example as a test case to verify the signature that your code
 calculates; however, you must use the same bucket name, object key, time stamp, and
 the following example credentials:




| Parameter | Value |
| --- | --- |
| `AWSAccessKeyId` | `AKIAIOSFODNN7EXAMPLE` |
| `AWSSecretAccessKey` | `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY` |


1. ###### StringToSign


	1. ###### CanonicalRequest
	
	
	
	
	
	
	```
	GET
	/test.txt
	X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE%2F20130524%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20130524T000000Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host
	host:examplebucket.s3.amazonaws.com
	
	host
	UNSIGNED-PAYLOAD
	```
	2. ###### StringToSign
	
	
	
	
	
	
	```
	AWS4-HMAC-SHA256
	20130524T000000Z
	20130524/us-east-1/s3/aws4_request
	3bfa292879f6447bbcda7001decf97f4a54dc650c8942174ae0a9121cf58ad04
	```
2. ###### SigningKey






```
*signing key* = HMAC-SHA256(HMAC-SHA256(HMAC-SHA256(HMAC-SHA256("AWS4" + "`<YourSecretAccessKey>`","20130524"),"us-east-1"),"s3"),"aws4_request")
```
3. ###### Signature






```
aeeed9bbccd4d02ee5c0109b86d86835f995330da4c265957d157751f604d404
```




Now you have all information to construct a presigned URL. The resulting URL for this
 example is shown as follows (you can use this to compare your presigned URL):



```
https://examplebucket.s3.amazonaws.com/test.txt?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE%2F20130524%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20130524T000000Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=aeeed9bbccd4d02ee5c0109b86d86835f995330da4c265957d157751f604d404
```

## Example 2


The following is an example (unrelated to the previous example) showing a presigned URL with the `X-Amz-Security-Token` parameter.



```
https://examplebucket.s3.us-east-1.amazonaws.com/test.txt
?X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE%2F20130524%2Fus-east-1%2Fs3%2Faws4_request
&X-Amz-Date=20200524T000000Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host
&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIBSUbVdj9YGs2g0HkHsOHFdkwOozjARSKHL987NhhOC8AiBPepRU1obMvIbGU0T%2BWphFPgK%2Fqpxaf5Snvm5M57XFkCqlAgjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDQ3MjM4NTU0NDY2MCIM83pULBe5%2F%2BNm1GZBKvkBVslSaJVgwSef7SsoZCJlfJ56weYl3QCwEGr2F4BmCZZyFpmWEYzWnhNK1AnHMj5nkfKlKBx30XAT5PZGVrmq4Vkn9ewlXQy1Iu3QJRi9Tdod8Ef9%2FyajTaUGh76%2BF5u5a4O115jwultOQiKomVwO318CO4l8lv%2F3HhMOkpdanMXn%2B4PY8lvM8RgnzSu90jOUpGXEOAo%2F6G8OqlMim3%2BZmaQmasn4VYRvESEd7O72QGZ3%2BvDnDVnss0lSYjlv8PP7IujnvhZRnj0WoeOyMe1lL0wTG%2Fa9usH5hE52w%2FYUJccOn0OaZuyROuVsRV4Q70sbWQhUvYUt%2B0tUMKzm8vsFOp4BaNZFqobbjtb36Y92v%2Bx5kY6i0s8QE886jJtUWMP5ldMziClGx3p0mN5dzsYlM3GyiJ%2FO1mWkPQDwg3mtSpOA9oeeuAMPTA7qMqy9RNuTKBDSx9EW27wvPzBum3SJhEfxv48euadKgrIX3Z79ruQFSQOc9LUrDjR%2B4SoWAJqK%2BGX8Q3vPSjsLxhqhEMWd6U4TXcM7ku3gxMbzqfT8NDg%3D
&X-Amz-Signature=`<signature-value>`
```
