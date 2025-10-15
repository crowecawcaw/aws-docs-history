# Common response headers

The following table describes response headers that are common to most Amazon S3
 responses.



|  Name  |  Description  |
| --- | --- |
| `Access-Control-Allow-Credentials` | A Boolean that determines if the server allows CORS requests to contain
 credentials. If the `Access-Control-Allow-Origin` request header is set to
 `'*'` then the `Access-Control-Allow-Credentials` response
 header will be omitted, else it is set to `true` when CORS evaluation is
 successful. 
Type: Boolean
Default: None |
| `Access-Control-Allow-Headers`  | A list of HTTP headers allowed for your CORS requests. The
 `Access-Control-Allow-Headers` response header is returned for successful
 CORS evaluations and explicitly specifies all allowed
 `Access-Control-Request-Headers`. 
Type: String
Default: None |
| `Access-Control-Allow-Methods` | A list that specifies which HTTP methods are allowed. Amazon S3 will only allow CORS requests from allowed CORS methods when the CORS evaluation is successful. 
Type: String
Default: None |
| `Access-Control-Allow-Origin` | The location of the allowed origin. Amazon S3 will only send the `Access-Control-Allow-Origin` response header when the CORS evaluation is successful. If the request origin matches `'*'` in the CORS configuration's allowed origins then the `'*'` is returned in this response header instead of the original origin.
 
Type: String
Default: None |
|  `Access-Control-Expose-Headers` | A list that allows a server to identify a response header that exposes access for applications when the CORS evaluation is successful.
Type: String
Default: None |
| `Access-Control-Max-Age` | The time in seconds that your browser can cache the response for a CORS
 pre-flight request as identified by the resource, the HTTP method, and the origin. The
 `Access-Control-Max-Age` response header is only returned when the CORS
 evaluation is successful. 
Type: Integer
Default: None |
| `Vary` | A list that indicates which request headers the CORS evaluation result varies on. The `Vary` response header is only returned when the CORS evaluation is successful. 
Type: String
Default: None |
| `Content-Length` | The length in bytes of the body in the response.
Type: String
Default: None |
| `Content-Type` | The MIME type of the content. For example, `Content-Type: text/html;
 charset=utf-8`. 
Type: String
Default: None |
| `Connection` | A value that specifies whether the connection to the server is open or
 closed.
Type: Enum
Valid Values: `open` | `close`
Default: None |
| `Date` | The date and time that Amazon S3 responded; for example, Wed, 01 Mar 2006 12:00:00
 GMT.
Type: String
Default: None |
| `ETag` | The entity tag (ETag) represents a specific version of the object. The ETag
 reflects changes only to the contents of an object, not its metadata. The ETag might
 or might not be an MD5 digest of the object data. Whether or not it is depends on how
 the object was created and how it is encrypted, as follows:

* Objects created through the AWS Management Console or by the `PUT` Object,
 `POST Object`, or `Copy` operation: 


	+ Objects that are plaintext or encrypted by server-side encryption with
	 Amazon S3 managed keys (SSE-S3) have ETags that are an MD5 digest of their data.
	+ Objects encrypted by server-side encryption with customer-provided keys
	 (SSE-C) or AWS Key Management Service (AWS KMS) keys (SSE-KMS) have ETags that are not an MD5
	 digest of their object data.
* Objects created by either the Multipart Upload or Upload Part Copy operation
 have ETags that are not MD5 digests, regardless of the method of
 encryption.

Type: String |
| `Server` | The name of the server that created the response.
Type: String
Default: `AmazonS3`
 |
| `x-amz-delete-marker` | A value that specifies whether the object returned was (`true`) or was
 not (`false`) a delete marker.
Type: Boolean
Valid Values: `true` | `false`
Default: false |
| `x-amz-id-2` | A special token that is used together with the `x-amz-request-id`
 header to help AWS troubleshoot problems. For information about Support using these
 request IDs, see [Troubleshooting Amazon S3](../userguide/troubleshooting.md#get-request-ids "../userguide/troubleshooting.md#get-request-ids").
Type: String
Default: None |
| `x-amz-request-id` | A value created by Amazon S3 that uniquely identifies the request. This value is used
 together with the `x-amz-id-2` header to help AWS troubleshoot problems.
 For information about Support using these request IDs, see  [Troubleshooting
 Amazon S3](../userguide/troubleshooting.md#get-request-ids "../userguide/troubleshooting.md#get-request-ids").
Type: String
Default: None |
| `x-amz-server-side-encryption` | The server-side encryption algorithm used when storing this object in Amazon S3
 (for example, `AES256`, `aws:kms`). 
Valid Values: `AES256` | `aws:kms` |
| `x-amz-version-id` | The version of the object. When you enable versioning, Amazon S3 generates a random
 number for objects added to a bucket. The value is UTF-8 encoded and URL ready. When
 you `PUT` an object in a bucket where versioning has been suspended, the
 version ID is always `null`.
Type: String
Valid Values: `null` | any URL-ready, UTF-8 encoded string
Default: null |
