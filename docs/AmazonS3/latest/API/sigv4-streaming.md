# Signature Calculations for the Authorization Header:
 Transferring Payload in Multiple Chunks (Chunked Upload) (AWS Signature Version
 4)

As described in the [Overview](sigv4-auth-using-authorization-header.md#sigv4-auth-header-overview "sigv4-auth-using-authorization-header.md#sigv4-auth-header-overview"), when authenticating requests using the
 `Authorization` header, you have an option of uploading the payload in
 chunks. You can send data in fixed size or variable size chunks. This section describes the
 signature calculation process in chunked upload, how you create the chunk body, and how the
 delayed signing works where you first upload the chunk, and send its signature in the
 subsequent chunk. The example section (see [Example: PUT Object](#example-signature-calculations-streaming "#example-signature-calculations-streaming")) shows signature calculations
 and resulting `Authorization` headers that you can use as a test suite to verify
 your code.

 

###### Note

When transferring data in a series of chunks, you must do one of the following: 


* Explicitly specify the total content length (object length in bytes plus
 metadata in each chunk) using the `Content-Length` HTTP header. To do
 this, you must pre-compute the total length of the payload, including the
 metadata that you send in each chunk, before starting your request.
* Specify the `Transfer-Encoding` HTTP header. If you include the
 `Transfer-Encoding` header and specify any value other than
 `identity`, you must omit the `Content-Length`
 header.
For all requests, you must include the `x-amz-decoded-content-length`
 header, specifying the size of the object in bytes.

Each chunk signature calculation includes the signature of the previous chunk. To begin,
 you create a *seed* signature using only the headers. You use the seed
 signature in the signature calculation of the first chunk. For each subsequent chunk, you
 create a chunk signature that includes the signature of the previous chunk. Thus, the chunk
 signatures are chained together; that is, the signature of chunk *n* is a
 function *F(chunk n, signature(chunk n-1))*. The chaining ensures that
 you send the chunks in the correct order.

To perform a chunked upload, do the following:

 


1. Decide the payload chunk size. You need this when you write the code.


The chunk size must be at least 8 KB. We recommend a chunk size of a least 64 KB for better
 performance. This chunk size applies to all chunks except the last one. The last
 chunk you send can be smaller than 8 KB. If your payload is small and can fit into
 one chunk, then it can be smaller than the 8 KB.
2. Create the seed signature for inclusion in the first chunk. For more information,
 see [Calculating the Seed
 Signature](#sigv4-chunked-upload-sig-calculation-chunk0 "#sigv4-chunked-upload-sig-calculation-chunk0").
3. Create the first chunk and stream it. For more information, see [Defining the Chunk Body](#sigv4-chunked-body-definition "#sigv4-chunked-body-definition").
4. For each subsequent chunk, calculate the chunk signature that includes the
 previous signature in the string you sign, construct the chunk, and send it. For
 more information, see [Defining the Chunk Body](#sigv4-chunked-body-definition "#sigv4-chunked-body-definition").
5. Send the final additional chunk, which is the same as the other chunks in the
 construction, but it has zero data bytes. For more information, see [Defining the Chunk Body](#sigv4-chunked-body-definition "#sigv4-chunked-body-definition").

## Calculating the Seed
 Signature


The following diagram illustrates the process of calculating the seed
 signature.


 



![Diagram showing the process of calculating the seed signature.](../../../images/AmazonS3/latest/API/images/sigV4-auth-header-chunked-seed-signature.png)

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

 For information about the signing process, see [Signature Calculations for the Authorization Header:
 Transferring Payload in a Single Chunk (AWS Signature Version 4)](sig-v4-header-based-auth.md "sig-v4-header-based-auth.md"). The
 process is the same, except that the creation of `CanonicalRequest` differs
 as follows:



* In addition to the request headers you plan to add, you must include the
 following headers:




| Header | Description |
| --- | --- |
| `x-amz-content-sha256` | This header is required for all AWS Signature Version 4
 requests. Set the value to
 `STREAMING-AWS4-HMAC-SHA256-PAYLOAD` to
 indicate that the signature covers only headers and that
 there is no payload. |
| `Content-Encoding` | Set the value to `aws-chunked`. 
Amazon S3 supports multiple content encoding values. You can specify your custom content-encoding when using the Signature Version 4 streaming API.
For example:

```
Content-Encoding : aws-chunked,gzip
```

Amazon S3 stores the resulting object without the `aws-chunked` value in the `content-encoding` header. If `aws-chunked` is the only value that you pass in the `content-encoding` header, S3 considers the `content-encoding` header empty and does not return this header when your retrieve the object.  |
| `x-amz-decoded-content-length` |  Set the value to the length, in bytes, of the data to be
 chunked, without counting any metadata. For example, if you are
 uploading a 4 GB file, set the value to 4294967296. This is the
 raw size of the object to be uploaded (data you want to store in
 Amazon S3). |
| `Content-Length` | Set the value to the actual size of the transmitted HTTP body, which includes the
 length of your data (value set for
 `x-amz-decoded-content-length`), plus chunk
 metadata. Each chunk has metadata, such as the signature of
 the previous chunk. Chunk calculations are discussed in the
 following section. If you include the
 `Transfer-Encoding` header and specify any
 value other than `identity`, you must not include
 the `Content-Length`
 header. |

You send the first chunk with the seed signature. You must construct the chunk as
 described in the following section.


## Defining the Chunk Body


All chunks include some metadata. Each chunk must conform to the following
 structure:


 



```
string(IntHexBase(`chunk-size`)) + ";chunk-signature=" + `signature` + \r\n + `chunk-data` + \r\n                    
```

Where:


 



* `IntHexBase()` is a function that you write to convert an integer
 chunk-size to hexadecimal. For example, if chunk-size is 65536, hexadecimal
 string is "10000".
* `chunk-size` is the size, in bytes, of the
 chunk-data, without metadata. For example, if you are uploading a 65 KB object
 and using a chunk size of 64 KB, you upload the data in three chunks: the first
 would be 64 KB, the second 1 KB, and the final chunk with 0 bytes.
* `signature`
 
 For each chunk, you calculate the signature using the following string to sign.
 For the first chunk, you use the seed-signature as the previous signature. 



 



![Diagram of the process of calculating the seed signature showing various components of the string to sign.](../../../images/AmazonS3/latest/API/images/sigV4-auth-header-chunk-signature.png)


 The size of the final chunk data that you send is 0, although the chunk body still
 contains metadata, including the signature of the previous chunk.


## Example: PUT Object


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
 For more information, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region "https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region") in the
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

For information about the API action, see [PutObject](API_PutObject.md "API_PutObject.md"). The general request syntax is as follows: 



```
PUT /examplebucket/chunkObject.txt HTTP/1.1
Host: s3.amazonaws.com
x-amz-date: 20130524T000000Z 
x-amz-storage-class: REDUCED_REDUNDANCY
Authorization: `SignatureToBeCalculated`
x-amz-content-sha256: STREAMING-AWS4-HMAC-SHA256-PAYLOAD
Content-Encoding: aws-chunked
x-amz-decoded-content-length: 66560
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
	content-length:66824
	host:s3.amazonaws.com
	x-amz-content-sha256:STREAMING-AWS4-HMAC-SHA256-PAYLOAD
	x-amz-date:20130524T000000Z
	x-amz-decoded-content-length:66560
	x-amz-storage-class:REDUCED_REDUNDANCY
	
	content-encoding;content-length;host;x-amz-content-sha256;x-amz-date;x-amz-decoded-content-length;x-amz-storage-class
	STREAMING-AWS4-HMAC-SHA256-PAYLOAD
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
	cee3fed04b70f867d036f722359b0b1f2f0e5dc0efadbc082b76c4c60e316455
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
4f232c4386841ef735655705268965c44a0e4690baa4adea153f7db9fa80a0a9
```
4. ###### Authorization header


The resulting Authorization header is as follows:


 



```
AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20130524/us-east-1/s3/aws4_request,SignedHeaders=content-encoding;content-length;host;x-amz-content-sha256;x-amz-date;x-amz-decoded-content-length;x-amz-storage-class,Signature=4f232c4386841ef735655705268965c44a0e4690baa4adea153f7db9fa80a0a9
```
5. ###### Chunk 1: (65536 bytes, with value 97 for letter 'a')


	1. Chunk string to sign:
	
	
	
	```
	AWS4-HMAC-SHA256-PAYLOAD
	20130524T000000Z
	20130524/us-east-1/s3/aws4_request
	4f232c4386841ef735655705268965c44a0e4690baa4adea153f7db9fa80a0a9
	e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
	bf718b6f653bebc184e1479f1935b8da974d701b893afcf49e701f3e2f9f9c5a
	```
	
	 
	
	
	###### Note
	
	For information about each line in the string to sign, see the
	 preceding diagram that shows various components of the string to
	 sign (for example, the last three lines are,
	 `previous-signature`, `hash("")`, and
	 `hash(current-chunk-data)`).
	2. Chunk signature:
	
	
	
	```
	ad80c730a21e5b8d04586a2213dd63b9a0e99e0e2307b0ade35a65485a288648
	```
	3. Chunk data sent:
	
	
	
	```
	10000;chunk-signature=ad80c730a21e5b8d04586a2213dd63b9a0e99e0e2307b0ade35a65485a288648
	<65536-bytes>
	```
6. ###### Chunk 2: (1024 bytes, with value 97 for letter 'a')


	1. Chunk string to sign:
	
	
	
	```
	AWS4-HMAC-SHA256-PAYLOAD
	20130524T000000Z
	20130524/us-east-1/s3/aws4_request
	ad80c730a21e5b8d04586a2213dd63b9a0e99e0e2307b0ade35a65485a288648
	e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
	2edc986847e209b4016e141a6dc8716d3207350f416969382d431539bf292e4a
	```
	2. Chunk signature:
	
	
	
	```
	0055627c9e194cb4542bae2aa5492e3c1575bbb81b612b7d234b86a503ef5497
	```
	3. Chunk data sent:
	
	
	
	```
	400;chunk-signature=0055627c9e194cb4542bae2aa5492e3c1575bbb81b612b7d234b86a503ef5497
	<1024 bytes>
	```
7. ###### Chunk 3: (0 byte data)


	1. Chunk string to sign:
	
	
	
	```
	AWS4-HMAC-SHA256-PAYLOAD
	20130524T000000Z
	20130524/us-east-1/s3/aws4_request
	0055627c9e194cb4542bae2aa5492e3c1575bbb81b612b7d234b86a503ef5497
	e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
	e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
	```
	2. Chunk signature:
	
	
	
	```
	b6c6ea8a5354eaf15b3cb7646744f4275b71ea724fed81ceb9323e279d449df9
	```
	3. Chunk data sent:
	
	
	
	```
	0;chunk-signature=b6c6ea8a5354eaf15b3cb7646744f4275b71ea724fed81ceb9323e279d449df9
	```
