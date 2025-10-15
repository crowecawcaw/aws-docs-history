# Authenticating Requests: Browser-Based Uploads Using
 POST (AWS Signature Version 4)

Amazon S3 supports HTTP POST requests so that users can upload content directly to Amazon S3. Using
 HTTP POST to upload content simplifies uploads and reduces upload latency where users upload
 data to store in Amazon S3. This section describes how you authenticate HTTP POST requests. For
 more information about HTTP POST requests, how to create a form, create a POST policy, and
 an example, see [Browser-Based Uploads Using
 POST (AWS Signature Version 4)](sigv4-UsingHTTPPOST.md "sigv4-UsingHTTPPOST.md").

To authenticate an HTTP POST request you do the following:





1. The form must include the following fields to provide signature and relevant
 information that Amazon S3 can use to re-calculate the signature upon receiving
 the request:




| Element Name | Description |
| --- | --- |
| `policy` | The Base64-encoded security policy that describes what
 is permitted in the request. For signature calculation this
 policy is the string you sign. Amazon S3 must get this
 policy so it can re-calculate the signature. |
| `x-amz-algorithm` | The signing algorithm used. For AWS Signature Version
 4, the value is `AWS4-HMAC-SHA256`. |
| `x-amz-credential` | In addition to your access key ID, this provides scope
 information you used in calculating the signing key for
 signature calculation. 
It is a string of the following form:
``<your-access-key-id>`/`<date>`/`<aws-region>`/`<aws-service>`/aws4_request` 
For example:

`AKIAIOSFODNN7EXAMPLE/20130728/us-east-1/s3/aws4_request`.
 . 
For Amazon S3, the *aws-service* string is `s3`. For a list of
 Amazon S3 `aws-region` strings, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region "https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region") in the *AWS General Reference*.  |
| `x-amz-date` | It is the date value in ISO8601 format. For example,
 `20130728T000000Z`. 
It is the same date you used in creating the signing
 key. This must also be the same value you provide in the
 policy (`x-amz-date`) that you signed.  |
| `x-amz-signature` | (AWS Signature Version 4) The HMAC-SHA256 hash of the
 security policy. 
For more information on options for the signature, see [Add the signature to the HTTP request](https://docs.aws.amazon.com/general/latest/gr/sigv4-add-signature-to-request.html "https://docs.aws.amazon.com/general/latest/gr/sigv4-add-signature-to-request.html") in the *AWS General Reference*. |
2. The POST policy must include the following elements:




| Element Name | Description |
| --- | --- |
| `x-amz-algorithm` |  The signing algorithm that you used to calculation the
 signature. For AWS Signature Version 4, the value is
 `AWS4-HMAC-SHA256`.  |
| `x-amz-credential` | In addition to your access key ID, this provides scope
 information you used in calculating the signing key for
 signature calculation. 
It is a string of the following form:
``<your-access-key-id>`/`<date>`/`<aws-region>`/`<aws-service>`/aws4_request` 
For example, 

`AKIAIOSFODNN7EXAMPLE/20130728/us-east-1/s3/aws4_request`.
 .
  |
| `x-amz-date` |  The date value specified in the ISO8601 formatted
 string. For example, "20130728T000000Z". The date must be the
 same that you used in creating the signing key for signature
 calculation.  |
3. For signature calculation the POST policy is the string to sign.
## Calculating a Signature


 The following diagram illustrates the signature calculation process. 


![Diagram showing AWS signature calculation process with StringToSign, SigningKey, and Signature steps.](../../../images/AmazonS3/latest/API/images/sigV4-post.png)



###### To Calculate a signature

1. Create a policy using UTF-8 encoding.
2. Convert the UTF-8-encoded policy to Base64. The result is the string to
 sign.
3. Create the signature as an HMAC-SHA256 hash of the string to sign. You will
 provide the signing key as key to the hash function.
4. Encode the signature by using hex encoding.

For more information about creating HTML forms, security policies, and an example, see
 the following subtopics:




* [Creating an HTML Form (Using AWS Signature Version
 4)](sigv4-HTTPPOSTForms.md "sigv4-HTTPPOSTForms.md")
* [POST Policy](sigv4-HTTPPOSTConstructPolicy.md "sigv4-HTTPPOSTConstructPolicy.md")
* [Example: Browser-Based Upload using HTTP POST (Using AWS
 Signature Version 4)](sigv4-post-example.md "sigv4-post-example.md")
