

# POST Object
<a name="RESTObjectPOST"></a>

## Description
<a name="RESTObjectPOST-description"></a>

The `POST` operation adds an object to a specified bucket by using HTML forms. `POST` is an alternate form of `PUT` that enables browser-based uploads as a way of putting objects in buckets. Parameters that are passed to `PUT` through HTTP headers are instead passed as form fields to `POST` in the multipart/form-data encoded message body. To add an object to a bucket, you must have `WRITE` access on the bucket. Amazon S3 never stores partial objects. If you receive a successful response, you can be confident that the entire object was stored.

Amazon S3 is a distributed system. Unless you've enabled versioning for a bucket, if Amazon S3 receives multiple write requests for the same object simultaneously, only the last version of the object written is stored.

To ensure that data is not corrupted while traversing the network, use the `Content-MD5` form field. When you use this form field, Amazon S3 checks the object against the provided MD5 value. If they do not match, Amazon S3 returns an error. Additionally, you can calculate the MD5 value while posting an object to Amazon S3 and compare the returned `ETag` to the calculated MD5 value. The ETag reflects only changes to the contents of an object, not its metadata.

**Note**  
To configure your application to send the request headers before sending the request body, use the HTTP status code 100 (Continue). For `POST` operations, using this status code helps you avoid sending the message body if the message is rejected based on the headers (for example, because of an authentication failure or redirect). For more information about the HTTP status code 100 (Continue), go to Section 8.2.3 of [http://www.ietf.org/rfc/rfc2616.txt](http://www.ietf.org/rfc/rfc2616.txt).

Amazon S3 automatically encrypts all new objects that are uploaded to an S3 bucket. The encryption setting of an uploaded object depends on the default encryption configuration of the destination bucket. By default, all buckets have a default encryption configuration that uses server-side encryption with Amazon S3 managed keys (SSE-S3). 

If the destination bucket has an encryption configuration that uses server-side encryption with an AWS Key Management Service (AWS KMS) key (SSE-KMS), dual-layer server-side encryption with an AWS KMS key (DSSE-KMS), or a customer-provi ded encryption key (SSE-C), Amazon S3 uses the corresponding KMS key or customer-provided key to encrypt the uploaded object. When uploading an object, if you want to change the encryption setting of the uploaded object, you can specify the type of server-side encryption. You can configure SSE-S3, SSE-KMS, DSSE-KMS, or SSE-C. For more information, see [Protecting data using server-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html) in the *Amazon Simple Storage Service User Guide*.

**Important**  
When constructing your request, make sure that the `file` field is the last field in the form.

## Requests
<a name="RESTObjectPOST-requests"></a>

### Syntax
<a name="RESTObjectPOST-requests-syntax"></a>

```
 1. POST / HTTP/1.1
 2. Host: {{destinationBucket}}.s3.amazonaws.com
 3. User-Agent: {{browser_data}}
 4. Accept: {{file_types}}
 5. Accept-Language: {{Regions}}
 6. Accept-Encoding: {{encoding}}
 7. Accept-Charset: {{character_set}}
 8. Keep-Alive: 300
 9. Connection: keep-alive
10. Content-Type: multipart/form-data; boundary=9431149156168
11. Content-Length: {{length}}
12. 
13. --9431149156168
14. Content-Disposition: form-data; name="key"
15. 
16. acl
17. --9431149156168
18. Content-Disposition: form-data; name="tagging"
19. 
20. <Tagging><TagSet><Tag><Key>{{Tag Name}}</Key><Value>{{Tag Value}}</Value></Tag></TagSet></Tagging>
21. --9431149156168
22. Content-Disposition: form-data; name="success_action_redirect"
23. 
24. success_redirect
25. --9431149156168
26. Content-Disposition: form-data; name="Content-Type"
27. 
28. content_type
29. --9431149156168
30. Content-Disposition: form-data; name="x-amz-meta-uuid"
31. 
32. uuid
33. --9431149156168
34. Content-Disposition: form-data; name="x-amz-meta-tag"
35. 
36. metadata
37. --9431149156168
38. Content-Disposition: form-data; name="AWSAccessKeyId"
39. 
40. access-key-id
41. --9431149156168
42. Content-Disposition: form-data; name="Policy"
43. 
44. encoded_policy
45. --9431149156168
46. Content-Disposition: form-data; name="Signature"
47. 
48. signature=
49. --9431149156168
50. Content-Disposition: form-data; name="file"; filename="{{MyFilename.jpg}}"
51. Content-Type: image/jpeg
52. 
53. file_content
54. --9431149156168
55. Content-Disposition: form-data; name="submit"
56. 
57. Upload to Amazon S3
58. --9431149156168--
```

### Request Parameters
<a name="RESTObjectPOST-requests-request-parameters"></a>

This implementation of the operation does not use request parameters.

### Form Fields
<a name="RESTObjectPOST-requests-form-fields"></a>

This operation can use the following form fields.


| Name | Description | Required | 
| --- | --- | --- | 
| AWSAccessKeyId | The AWS access key ID of the owner of the bucket who grants an Anonymous user access for a request that satisfies the set of constraints in the policy.<br />Type: String<br />Default: None<br />Constraints: Required if a policy document is included with the request.  | Conditional | 
| acl | The specified Amazon S3 access control list (ACL). If the specified ACL is not valid, an error is generated. For more information about ACLs, see [Access control list (ACL) overview](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html) in the *Amazon Simple Storage Service User Guide*. <br />Type: String<br />Default: private<br /> Valid Values: `private \| public-read \| public-read-write \| aws-exec-read \| authenticated-read \| bucket-owner-read \| bucket-owner-full-control `  | No | 
| Cache-Control, Content-Type, Content-Disposition, Content-Encoding, Expires | The REST-specific headers. For more information, see [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html).<br />Type: String<br />Default: None | No | 
| file | The file or text content. <br />The file or text content must be the last field in the form.<br />You cannot upload more than one file at a time.<br />Type: File or text content<br />Default: None | Yes | 
| key | The name of the uploaded key.<br />To use the file name provided by the user, use the `${filename}` variable. For example, if a user named Mary uploads the file `example.jpg` and you specify `/user/mary/${filename}`, the key name is `/user/mary/example.jpg`.<br />For more information, see [Object key and metadata](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingMetadata.html) in the *Amazon Simple Storage Service User Guide*.<br />Type: String<br />Default: None | Yes | 
| policy | The security policy that describes what is permitted in the request. Requests without a security policy are considered anonymous and work only on publicly writable buckets. For more information, see [HTML forms](https://docs.aws.amazon.com/AmazonS3/latest/userguide/HTTPPOSTForms.html) and [Upload examples](https://docs.aws.amazon.com/AmazonS3/latest/userguide/HTTPPOSTExamples.html) in the *Amazon Simple Storage Service User Guide*. <br />Type: String<br />Default: None<br />Constraints: A security policy is required if the bucket is not publicly writable. | Conditional | 
| success\_action\_redirect, redirect | The URL to which the client is redirected upon a successful upload.<br />If `success_action_redirect` is not specified, Amazon S3 returns the empty document type specified in the `success_action_status` field.<br />If Amazon S3 cannot interpret the URL, it acts as if the field is not present.<br />If the upload fails, Amazon S3 displays an error and does not redirect the user to a URL.<br />Type: String<br />Default: None The `redirect` field name is deprecated, and support for the `redirect` field name will be removed in the future.   | No | 
| success\_action\_status | If you don't specify `success_action_redirect`, the status code is returned to the client when the upload succeeds.<br />This field accepts the values `200`, `201`, or `204` (the default).<br />If the value is set to `200` or `204`, Amazon S3 returns an empty document with a 200 or 204 status code.<br />If the value is set to `201`, Amazon S3 returns an XML document with a 201 status code. <br />If the value is not set or if it is set to a value that is not valid, Amazon S3 returns an empty document with a 204 status code. <br />Type: String<br />Default: None | No | 
| tagging | The specified set of tags to add to the object. To add tags, use the following encoding scheme.<br /> <pre><Tagging><br />  <TagSet><br />    <Tag><br />      <Key>{{TagName}}</Key><br />      <Value>{{TagValue}}</Value><br />    </Tag><br />    ...<br />  </TagSet><br /></Tagging></pre><br />For more information, see [Object tagging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-tagging.html) in the *Amazon Simple Storage Service User Guide*.<br />Type: String<br />Default: None | No | 
| x-amz-storage-class | The storage class to use for storing the object. If you don't specify a class, Amazon S3 uses the default storage class, `STANDARD`. Amazon S3 supports other storage classes. For more information, see [Storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html) in the *Amazon Simple Storage Service User Guide*. <br />Type: String<br />Default: `STANDARD`<br />Valid values: `REDUCED_REDUNDANCY` \|`EXPRESS_ONEZONE` \| `DEEP_ARCHIVE` \| `GLACIER` \| `GLACIER_IR` \| `INTELLIGENT_TIERING` \| `ONEZONE_IA` \| `STANDARD` \| `STANDARD_IA`  | No | 
| x-amz-meta-\* | Headers starting with this prefix are user-defined metadata. Each one is stored and returned as a set of key-value pairs. Amazon S3 doesn't validate or interpret user-defined metadata. For more information, see [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html).<br />Type: String<br />Default: None | No | 
| x-amz-security-token | The Amazon DevPay security token. <br />Each request that uses Amazon DevPay requires two `x-amz-security-token` form fields: one for the product token and one for the user token.<br />Type: String<br />Default: None | No | 
| x-amz-signature | (AWS Signature Version 4) The HMAC-SHA256 hash of the security policy.<br />Type: String<br />Default: None | Conditional | 
| x-amz-website-redirect-location  | If the bucket is configured as a website, this field redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata. For information about object metadata, see [Object key and metadata](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingMetadata.html) in the *Amazon Simple Storage Service User Guide*.<br />In the following example, the request header sets the redirect to an object (`anotherPage.html`) in the same bucket:<br />`x-amz-website-redirect-location: /anotherPage.html`<br />In the following example, the request header sets the object redirect to another website:<br />`x-amz-website-redirect-location: http://www.example.com/`<br />For more information about website hosting in Amazon S3, see [Hosting websites on Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html) and [How to configure website page redirects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-page-redirect.html) in the *Amazon Simple Storage Service User Guide*.<br />Type: String<br />Default: None<br />Constraints: The value must be prefixed by `/`, `http://`, or `https://`. The length of the value is limited to 2 KB. |  No  | 

#### Additional Checksum Request Form Fields
<a name="post-object-additional-checksums"></a>

When uploading an object, you can specify various checksums that you would like to use to verify your data integrity. You can specify one additional checksum algorithm for Amazon S3 to use. For more information about additional checksum values, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon Simple Storage Service User Guide*.


|  Name  |  Description  |  Required  | 
| --- | --- | --- | 
|  x-amz-checksum-algorithm  | Indicates the algorithm used to create the checksum for the object. If a value is specified, you must include the matching checksum header. Otherwise, your request will generate a 400 error.<br />Possible values include `CRC32`, `CRC32C`, `SHA1`, and `SHA256`. | No | 
|  x-amz-checksum-crc32  | Specifies the base64-encoded, 32-bit CRC32 checksum of the object.<br />This parameter is required if the value of `x-amz-checksum-algorithm` is `CRC32`. | Conditional | 
|  x-amz-checksum-crc32c  | Specifies the base64-encoded, 32-bit CRC32C checksum of the object.<br />This parameter is required if the value of `x-amz-checksum-algorithm` is `CRC32C`. | Conditional | 
|  x-amz-checksum-sha1  | Specifies the base64-encoded, 160-bit SHA-1 digest of the object.<br />This parameter is required if the value of `x-amz-checksum-algorithm` is `SHA1`. | Conditional | 
|  x-amz-checksum-sha256  | Specifies the base64-encoded, 256-bit SHA-256 digest of the object.<br />This parameter is required if the value of `x-amz-checksum-algorithm` is `SHA256`. | Conditional | 

#### Server-Side Encryption Specific Request Form Fields
<a name="post-object-sse-specific-request-headers"></a>

Server-side encryption is data encryption at rest. Amazon S3 encrypts your data while writing it to disks in AWS data centers and decrypts your data when you access it. When uploading an object, you can specify the type of server-side encryption that you want Amazon S3 to use for encrypting the object. 

There are four types of server-side encryption: 
+ **Server-side encryption with Amazon S3 managed keys (SSE-S3)** – Starting May 2022, all Amazon S3 buckets have encryption configured by default. The default option for server-side encryption is with SSE-S3. Each object is encrypted with a unique key. As an additional safeguard, SSE-S3 encrypts the key itself with a root key that it regularly rotates. SSE-S3 uses one of the strongest block ciphers available, 256-bit Advanced Encryption Standard (AES-256), to encrypt your data.
+ **Server-side encryption with AWS KMS keys (SSE-KMS)** – SSE-KMS is provided through an integration of the AWS KMS service with Amazon S3. With AWS KMS, you have more control over your keys. For example, you can view separate keys, edit control policies, and follow the keys in AWS CloudTrail. Additionally, you can create and manage customer managed keys or use AWS managed keys that are unique to you, your service, and your Region.
+ **Dual-layer server-side encryption with AWS KMS keys (DSSE-KMS)** – Dual-layer server-side encryption with AWS KMS keys (DSSE-KMS) is similar to SSE-KMS, but applies two individual layers of object-level encryption instead of one layer. 
+ **Server-side encryption with customer-provided keys (SSE-C)** – With SSE-C, you manage the encryption keys, and Amazon S3 manages the encryption as it writes to disks, and the decryption when you access your objects. 
**Note**  
If you have server-side encryption with customer-provided keys (SSE-C) blocked for your general purpose bucket, you will get an HTTP 403 Access Denied error when you specify the SSE-C request headers while writing new data to your bucket. For more information, see [Blocking or unblocking SSE-C for a general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/blocking-unblocking-s3-c-encryption-gpb.html).

For more information, see [ Protecting data using server-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html) in the *Amazon Simple Storage Service User Guide*.

Depending on which type of server-side encryption you want to use, specify the following form fields. 
+ **Use SSE-S3, SSE-KMS, or DSSE-KMS** – If you want to use these types of server-side encryption, specify the following form fields in the request.     
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonS3/latest/developerguide/RESTObjectPOST.html)
**Note**  
If you specify `x-amz-server-side-encryption:aws:kms` or `x-amz-server-side-encryption:aws:kms:dsse`, but do not provide `x-amz-server-side-encryption-aws-kms-key-id`, Amazon S3 uses the AWS managed key (`aws/S3`) to protect the data.
+ **Use SSE-C** – If you want to manage your own encryption keys, you must provide all the following form fields in the request. 
**Note**  
If you use SSE-C, the `ETag` value that Amazon S3 returns in the response is not the MD5 of the object.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonS3/latest/developerguide/RESTObjectPOST.html)

### Responses
<a name="RESTObjectPOST-requests-responses"></a>

#### Response Headers
<a name="RESTObjectPOST-requests-responses-response-headers"></a>

This implementation of the operation can include the following response headers in addition to the response headers common to all responses. For more information, see [Common Response Headers](RESTCommonResponseHeaders.md).


|  Name  |  Description  | 
| --- | --- | 
|  x-amz-checksum-crc32  | The base64-encoded, 32-bit CRC32 checksum of the object.<br />Type: String | 
|  x-amz-checksum-crc32c  | The base64-encoded, 32-bit CRC32C checksum of the object.<br />Type: String | 
|  x-amz-checksum-sha1  | The base64-encoded, 160-bit SHA-1 digest of the object.<br />Type: String | 
|  x-amz-checksum-sha256  | The base64-encoded, 256-bit SHA-256 digest of the object.<br />Type: String | 
|  x-amz-expiration  | If an `Expiration` action is configured for the object as part of the bucket's lifecycle configuration, Amazon S3 returns this header.  The header value includes an `expiry-date` component and a URL-encoded `rule-id` component.  For version-enabled buckets, this header applies only to current versions. Amazon S3 does not provide a header to indicate when a noncurrent version is eligible for permanent deletion. For more information, see [PutBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html).<br />Type: String | 
|  success\_action\_redirect, redirect  | The URL to which the client is redirected on a successful upload.<br />Type: String<br />Ancestor: PostResponse | 
|  x-amz-server-side-encryption  | The server-side encryption algorithm that was used when storing this object in Amazon S3 (for example, `AES256`, `aws:kms`, `aws:kms:dsse`).<br />Type: String | 
|  x-amz-server-side-encryption-aws-kms-key-id  | If the `x-amz-server-side-encryption` header has a valid value of `aws:kms`, this header specifies the ID of the KMS key that was used to encrypt the object.<br />Type: String | 
|  x-amz-server-side-encryption-bucket-key-enabled  | If `x-amz-server-side-encryption` has a valid value of `aws:kms`, this header indicates whether the object is encrypted with SSE-KMS by using an S3 Bucket Key. If this header is set to `true`, the object uses an S3 Bucket Key with SSE-KMS.<br />Type: Boolean | 
|  x-amz-server-side-encryption-customer-algorithm  | If SSE-C was requested, the response includes this header, which confirms the encryption algorithm that was used.<br />Type: String<br />Valid Values: `AES256` | 
|  x-amz-server-side-encryption-customer-key-MD5  | If SSE-C was requested, the response includes this header to verify round-trip message integrity of the customer-provided encryption key.<br />Type: String | 
| x-amz-version-id | Version of the object.<br />Type: String | 

#### Response Elements
<a name="RESTObjectPOST-requests-responses-response-elements"></a>


|  Name  |  Description  | 
| --- | --- | 
|  Bucket  | The name of the bucket that the object was stored in.<br />Type: String<br />Ancestor: PostResponse | 
|  ETag  | The entity tag (ETag) is an MD5 hash of the object that you can use to do conditional `GET` operations by using the `If-Modified` request tag with the `GET` request operation. `ETag` reflects changes only to the contents of an object, not to its metadata.<br />Type: String<br />Ancestor: PostResponse | 
|  Key  | The object key name.<br />Type: String<br />Ancestor: PostResponse | 
|  Location  | The URI of the object.<br />Type: String<br />Ancestor: PostResponse | 

#### Special Errors
<a name="RESTObjectPOST-requests-responses-special-errors"></a>

This implementation of the operation does not return special errors. For general information about Amazon S3 errors and a list of error codes, see [Error Responses](ErrorResponses.md).

## Examples
<a name="RESTObjectPOST-requests-examples"></a>

### Sample Request
<a name="ExampleVersionObjectPost"></a>

```
1. POST /Neo HTTP/1.1
2. Content-Length: 4
3. Host: quotes.s3.amazonaws.com
4. Date: Wed, 01 Mar  2006 12:00:00 GMT
5. Authorization: {{authorization string}}
6. Content-Type: text/plain
7. Expect: the 100-continue HTTP status code
8. 
9. {{ObjectContent}}
```

### Sample Response with Versioning Suspended
<a name="RESTObjectPOST-requests-examples-sample-response-with-versioning-suspended"></a>

The following is a sample response when bucket versioning is suspended:

```
 1. HTTP/1.1 100 Continue
 2. HTTP/1.1 200 OK
 3. x-amz-id-2: LriYPLdmOdAiIfgSm/F1YsViT1LW94/xUQxMsF7xiEb1a0wiIOIxl+zbwZ163pt7
 4. x-amz-request-id: 0A49CE4060975EAC
 5. x-amz-version-id: default
 6. Date: Wed, 12 Oct 2009 17:50:00 GMT
 7. ETag: "1b2cf535f27731c974343645a3985328"
 8. Content-Length: 0
 9. Connection: close
10. Server: AmazonS3
```

In this response, the version ID is `null`.

### Sample Response with Versioning Enabled
<a name="RESTObjectPOST-requests-examples-sample-response-with-versioning-enabled"></a>

The following is a sample response when bucket versioning is enabled.

```
 1. HTTP/1.1 100 Continue
 2. HTTP/1.1 200 OK
 3. x-amz-id-2: LriYPLdmOdAiIfgSm/F1YsViT1LW94/xUQxMsF7xiEb1a0wiIOIxl+zbwZ163pt7
 4. x-amz-request-id: 0A49CE4060975EAC
 5. x-amz-version-id: 43jfkodU8493jnFJD9fjj3HHNVfdsQUIFDNsidf038jfdsjGFDSIRp
 6. Date: Wed, 01 Mar  2006 12:00:00 GMT
 7. ETag: "828ef3fdfa96f00ad9f27c383fc9ac7f"
 8. Content-Length: 0
 9. Connection: close
10. Server: AmazonS3
```

## Related Resources
<a name="RESTObjectPOST-requests-related-resources"></a>
+  [CopyObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html) 
+  [POST Object](#RESTObjectPOST) 
+  [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) 