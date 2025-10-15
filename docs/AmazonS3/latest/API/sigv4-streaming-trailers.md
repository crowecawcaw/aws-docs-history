# Signature calculations for trailing headers
 (chunked uploads) (AWS Signature Version 4)

When authenticating requests using the
 `Authorization` header, you can also upload the payload in
 chunks. When you send the data for the object in chunks, you
 also have the option of including trailing headers. (For more information, see [Signature Calculations for the Authorization Header:
 Transferring Payload in Multiple Chunks (Chunked Upload) (AWS Signature Version
 4)](sigv4-streaming.md "sigv4-streaming.md").) This section describes the steps
 you need to take when you want to include a trailing header at the end of your multiple chunk
 upload.

 

###### Important

When you are including trailing headers, you must send the following in your initial header: 


* You must set `x-amz-content-sha256` to an appropriate value that indicates
 a trailer will be included. To see the acceptable values for `x-amz-content-sha256`,
 see [Authenticating Requests: Using the
 Authorization Header (AWS Signature Version 4)](sigv4-auth-using-authorization-header.md "sigv4-auth-using-authorization-header.md").
* You must set `x-amz-trailer` to indicate the contents your are including in
 your trailing header.

 Trailing headers are only sent after the chunks have been uploaded. Previous chunks are sent
 as normal and signed as described in the previous sections, including sending the final chunk
 with a payload of 0 bytes. The trailing headers are included as their own chunk and sent
 after the final chunk with a payload of 0 bytes. For example, if your data ended with a 100 KB
 chunk, you would send the following:
 


* Previous data chunks
* 100 KB final chunk of the object
* 0 bytes chunk signifying the end of the object
* Trailing headers chunk

## Examples: Checking signature
 calculations


You can use the examples in this section as a reference to check signature
 calculations in your code. Before you review the examples, note the following:


 



* The signature calculations in these examples use the following example
 security credentials.




| Parameter | Value |
| --- | --- |
| `AWSAccessKeyId` | `AKIAIOSFODNN7EXAMPLE` |
| `AWSSecretAccessKey` | `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY` |
* All examples use the request timestamp 20130524T000000Z (`Fri, 24 May 2013 00:00:00
 GMT`).
* All examples use `examplebucket` as the bucket name.
* The bucket is assumed to be in the
 US East (N. Virginia) Region, and the credential `Scope` and the
 `Signing Key` calculations use `us-east-1` as the
 Region specifier. 
 For more information, see [Regions and endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region "https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region") in the
 *Amazon Web Services General Reference*.
* You can use either path style or virtual-hosted style requests. The following
 examples use virtual-hosted style requests, for example: 



```
https://examplebucket.s3.amazonaws.com/photos/photo1.jpg
```

For more information, see [Virtual
 Hosting of Buckets](../userguide/VirtualHosting.md "../userguide/VirtualHosting.md") in the
 *Amazon Simple Storage Service User Guide*.

The following example sends a `PUT` request to upload an object. The
 signature calculations assume the following:


 



* You are uploading a 65 KB text file, and the file content is a
 one-character string made up of the letter 'a'.
* The chunk size is 64 KB. As a result, the payload is uploaded in three
 chunks, 64 KB, 1 KB, and the final chunk with 0 bytes of chunk data.
* The resulting object has the key name `chunkObject.txt`.
* You are requesting `REDUCED_REDUNDANCY` as the storage class by
 adding the `x-amz-storage-class` request header.
* The transfer is including a CRC32C checksum value as a trailing header.

For information about the API action, see [PutObject](API_PutObject.md "API_PutObject.md"). The general request syntax is as follows: 



```
PUT /examplebucket/chunkObject.txt HTTP/1.1
Host: s3.amazonaws.com
x-amz-date: 20130524T000000Z 
x-amz-storage-class: REDUCED_REDUNDANCY
Authorization: `SignatureToBeCalculated`
x-amz-content-sha256: STREAMING-AWS4-HMAC-SHA256-PAYLOAD-TRAILER
Content-Encoding: aws-chunked
x-amz-decoded-content-length: 66560
x-amz-trailer: x-amz-checksum-crc32c
Content-Length: 66824
`<Payload>`
```


The following steps show signature calculations.


1. ###### Seed signature — Create String to Sign


	1. ###### CanonicalRequest
	
	
	 
	
	
	
	```
	PUT
	/examplebucket/chunkObject.txt
	
	content-encoding:aws-chunked
	host:s3.amazonaws.com
	x-amz-content-sha256:STREAMING-AWS4-HMAC-SHA256-PAYLOAD-TRAILER
	x-amz-date:20130524T000000Z
	x-amz-decoded-content-length:66560
	x-amz-storage-class:REDUCED_REDUNDANCY
	x-amz-trailer:x-amz-checksum-crc32c
	
	content-encoding;host;x-amz-content-sha256;x-amz-date;x-amz-decoded-content-length;x-amz-storage-class;x-amz-trailer
	STREAMING-AWS4-HMAC-SHA256-PAYLOAD-TRAILER
	```
	
	In the canonical request, the third line is empty because there
	 are no query parameters in the request. The last line is the
	 constant string provided as the value of the hashed Payload, which
	 should be same as the value of `x-amz-content-sha256
	 header`.
	2. ###### StringToSign
	
	
	 
	
	
	
	```
	AWS4-HMAC-SHA256
	20130524T000000Z
	20130524/us-east-1/s3/aws4_request
	44d48b8c2f70eae815a0198cc73d7a546a73a93359c070abbaa5e6c7de112559
	```
	
	 
	
	
	 
	
	
	###### Note
	
	For information about each of line in the string to sign, see
	 the diagram that explains seed signature calculation.
2. ###### SigningKey


 



```
*signing key* = HMAC-SHA256(HMAC-SHA256(HMAC-SHA256(HMAC-SHA256("AWS4" + "`<YourSecretAccessKey>`","20130524"),"us-east-1"),"s3"),"aws4_request")						
```
3. ###### Seed Signature


 



```
106e2a8a18243abcf37539882f36619c00e2dfc72633413f02d3b74544bfeb8e
```
4. ###### Authorization header


The resulting Authorization header is as follows:


 



```
AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20130524/us-east-1/s3/aws4_request,SignedHeaders=content-encoding;content-length;host;x-amz-content-sha256;x-amz-date;x-amz-decoded-content-length;x-amz-storage-class,Signature=106e2a8a18243abcf37539882f36619c00e2dfc72633413f02d3b74544bfeb8e
```
5. ###### Chunk 1: (65536 bytes, with value 97 for letter 'a')


	1. Chunk string to sign:
	
	
	
	```
	AWS4-HMAC-SHA256-PAYLOAD
	20130524T000000Z
	20130524/us-east-1/s3/aws4_request
	106e2a8a18243abcf37539882f36619c00e2dfc72633413f02d3b74544bfeb8e
	e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
	bf718b6f653bebc184e1479f1935b8da974d701b893afcf49e701f3e2f9f9c5a
	```
	
	 
	
	
	###### Note
	
	For information about each line in the string to sign, see the diagram in the preceding topic ([Calculating the Seed
	 Signature](sigv4-streaming.md#sigv4-chunked-upload-sig-calculation-chunk0 "sigv4-streaming.md#sigv4-chunked-upload-sig-calculation-chunk0")) that shows various components of the string to
	 sign. For example, the last three lines consist of the following:
	
	
	
		* `previous-signature`
		* `hash("")`
		* `hash(`current-chunk-data`)`
	2. Chunk signature:
	
	
	
	```
	b474d8862b1487a5145d686f57f013e54db672cee1c953b3010fb58501ef5aa2
	```
	3. Chunk data sent:
	
	
	
	```
	10000;chunk-signature=b474d8862b1487a5145d686f57f013e54db672cee1c953b3010fb58501ef5aa2
	<65536-bytes>
	```
6. ###### Chunk 2: (1024 bytes, with value 97 for letter 'a')


	1. Chunk string to sign:
	
	
	
	```
	AWS4-HMAC-SHA256-PAYLOAD
	20130524T000000Z
	20130524/us-east-1/s3/aws4_request
	b474d8862b1487a5145d686f57f013e54db672cee1c953b3010fb58501ef5aa2
	e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
	2edc986847e209b4016e141a6dc8716d3207350f416969382d431539bf292e4a
	```
	2. Chunk signature:
	
	
	
	```
	1c1344b170168f8e65b41376b44b20fe354e373826ccbbe2c1d40a8cae51e5c7
	```
	3. Chunk data sent:
	
	
	
	```
	400;chunk-signature=1c1344b170168f8e65b41376b44b20fe354e373826ccbbe2c1d40a8cae51e5c7
	<1024-bytes>
	```
7. ###### Chunk 3: (0 byte data)


	1. Chunk string to sign:
	
	
	
	```
	AWS4-HMAC-SHA256-PAYLOAD
	20130524T000000Z
	20130524/us-east-1/s3/aws4_request
	1c1344b170168f8e65b41376b44b20fe354e373826ccbbe2c1d40a8cae51e5c7
	e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
	e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
	```
	2. Chunk signature:
	
	
	
	```
	2ca2aba2005185cf7159c6277faf83795951dd77a3a99e6e65d5c9f85863f992
	```
	3. Chunk data sent:
	
	
	
	```
	0;chunk-signature=2ca2aba2005185cf7159c6277faf83795951dd77a3a99e6e65d5c9f85863f992
	```
8. ###### Chunk 4: Trailing headers


	1. Trailer chunk string to sign:
	
	
	
	```
	AWS4-HMAC-SHA256-TRAILER
	20130524T000000Z
	20130524/us-east-1/s3/aws4_request
	2ca2aba2005185cf7159c6277faf83795951dd77a3a99e6e65d5c9f85863f992
	1e376db7e1a34a8ef1c4bcee131a2d60a1cb62503747488624e10995f448d774
	```
	
	###### Note
	
	The last two lines are `previous-signature` (the 0 byte data chunk signature), `hash`(`trailing-checksum-header-name`:`base64-encoded-trailing-checksum-value`\n).
	
	The hash is calculated as follows with no whitespace: 
	
	
	
		* The trailing checksum header name
		* A colon (`:`)
		* The base64-encoded trailing checksum value
		* A newline character (`\n`).In this example, where we are using the `crc32c` hash algorithm, with the base64-encoded checksum value `sOO8/Q==`, we can represent the computation as follows: `hash('x-amz-checksum-crc32c:sOO8/Q==\n')`.
	2. Chunk signature:
	
	
	
	```
	d81f82fc3505edab99d459891051a732e8730629a2e4a59689829ca17fe2e435
	```
	3. Chunk data sent:
	
	
	
	```
	x-amz-checksum-crc32c:sOO8/Q==
	x-amz-trailer-signature:d81f82fc3505edab99d459891051a732e8730629a2e4a59689829ca17fe2e435
	```
