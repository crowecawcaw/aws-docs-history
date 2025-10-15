# Authenticating Requests: Using the
 Authorization Header (AWS Signature Version 4)

###### Topics

* [Overview](#sigv4-auth-header-overview "#sigv4-auth-header-overview")
* [Signature Calculations for the Authorization Header:
 Transferring Payload in a Single Chunk (AWS Signature Version 4)](sig-v4-header-based-auth.md "sig-v4-header-based-auth.md")
* [Signature Calculations for the Authorization Header:
 Transferring Payload in Multiple Chunks (Chunked Upload) (AWS Signature Version
 4)](sigv4-streaming.md "sigv4-streaming.md")
* [Signature calculations for trailing headers
 (chunked uploads) (AWS Signature Version 4)](sigv4-streaming-trailers.md "sigv4-streaming-trailers.md")
## Overview


Using the HTTP `Authorization` header is the most common method of providing
 authentication information. Except for [POST
 requests](RESTObjectPOST.md "RESTObjectPOST.md") and requests that are signed by using query parameters, all Amazon S3
 operations use the `Authorization` request header to provide
 authentication information. 


The following is an example of the `Authorization` header value. Line
 breaks are added to this example for readability:






```
Authorization: AWS4-HMAC-SHA256 
Credential=AKIAIOSFODNN7EXAMPLE/20130524/us-east-1/s3/aws4_request, 
SignedHeaders=host;range;x-amz-date,
Signature=fe5f80f77d5fa3beca038a248ff027d0445342fe2855ddc963176630326f1024
```


 The following table describes the various components of the `Authorization` header value in
 the preceding example:




| Component | Description |
| --- | --- |
| `AWS4-HMAC-SHA256` | The algorithm that was used to calculate the signature.
 You must provide this value when you use AWS Signature
 Version 4 for authentication.
The string specifies AWS Signature Version 4 (`AWS4`) and
 the signing algorithm (`HMAC-SHA256`). |
| `Credential` | Your access key ID and the scope information, which includes the date, Region, and
 service that were used to calculate the signature. 
This string has the following form:


```
``<your-access-key-id>`/`<date>`/`<aws-region>`/`<aws-service>`/aws4_request`
```

Where:


* `<date>` value is
 specified using `YYYYMMDD`
 format.
* `<aws-service>`
 value is `s3` when sending request to
 Amazon S3.
 |
| `SignedHeaders` |  A semicolon-separated list of request headers that you
 used to compute `Signature`. The list includes
 header names only, and the header names must be in
 lowercase. For example:
 
```
host;range;x-amz-date
```
 |
| `Signature` | The 256-bit signature expressed as 64 lowercase hexadecimal characters. For example:
 
```
fe5f80f77d5fa3beca038a248ff027d0445342fe2855ddc963176630326f1024
```
Note
 that the signature calculations vary depending on the option you
 choose to transfer the payload.  |


The signature calculations vary depending on the method you choose to transfer the request
 payload. S3 supports the following options:






* Transfer payload in a single chunk
 – In this case, you have the following signature
 calculation options:







	+ **Signed payload option** – You can 
	 optionally compute the entire payload checksum and
	 include it in signature calculation. This provides added
	 security but you need to read your payload twice or
	 buffer it in memory. 
	
	
	For example, in order to upload a file, you need to read the file first to
	 compute a payload hash for signature calculation and again
	 for transmission when you create the request. For smaller
	 payloads, this approach might be preferable. However, for
	 large files, reading the file twice can be inefficient, 
	 so you might want to upload data in chunks instead. 
	
	
	We recommend you include payload checksum for added
	 security.
	+ **Unsigned payload option** – 
	 Do not include payload checksum in signature calculation.
For step-by-step instructions to calculate signature and construct the Authorization
 header value, see [Signature Calculations for the Authorization Header:
 Transferring Payload in a Single Chunk (AWS Signature Version 4)](sig-v4-header-based-auth.md "sig-v4-header-based-auth.md").
* Transfer payload in multiple chunks (chunked upload) – 
 In this case you transfer payload
 in chunks. You can transfer a payload in chunks regardless of the
 payload size.


You can break up your payload into chunks. These can be fixed or
 variable-size chunks. By uploading data in chunks, you avoid reading the
 entire payload to calculate the signature. Instead, for the first chunk,
 you calculate a seed signature that uses only the request headers. The
 second chunk contains the signature for the first chunk, and each
 subsequent chunk contains the signature for the chunk that precedes it.
 At the end of the upload, you send a final chunk with 0 bytes of data
 that contains the signature of the last chunk of the payload. For more
 information, see [Signature Calculations for the Authorization Header:
 Transferring Payload in Multiple Chunks (Chunked Upload) (AWS Signature Version
 4)](sigv4-streaming.md "sigv4-streaming.md").

When signing your requests, you can use either AWS Signature Version 4 or AWS Signature Version 4A.
 The key difference between the two is determined by how the signature is calculated. With
 AWS Signature Version 4A, the signature does not include Region-specific information and is calculated
 using the `AWS4-ECDSA-P256-SHA256` algorithm.


In addition to these options, you have the option of including a trailer with your request.
 In order to include a trailer with your request, you need to specify that in the header by
 setting `x-amz-content-sha256` to the appropriate value. If you are using a trailing
 header, you must include `x-amz-trailer` in the header and specify the trailing header names
 as a string in a comma-separated list. All trailing headers are written after the final chunk. If you're
 uploading the data in multiple chunks, you must send a final chunk with 0 bytes of data before sending
 the trailing header.
 


When you send a request, you must tell Amazon S3 which of the preceding options you have
 chosen in your signature calculation, by adding the
 `x-amz-content-sha256` header with one of the following
 values:








| Header value | Description |
| --- | --- |
| Actual payload checksum value | This value is the actual checksum of your object and is only possible
 when you are uploading the data in a single chunk. |
| UNSIGNED-PAYLOAD | Use this when you are uploading the object as a single unsigned chunk. |
| STREAMING-UNSIGNED-PAYLOAD-TRAILER | Use this when sending an unsigned payload over multiple chunks. In this
 case you also have a trailing header after the chunk is uploaded. |
| STREAMING-AWS4-HMAC-SHA256-PAYLOAD | Use this when sending a payload over multiple chunks, and the chunks
 are signed using `AWS4-HMAC-SHA256`. This produces a SigV4
 signature. |
| STREAMING-AWS4-HMAC-SHA256-PAYLOAD-TRAILER | Use this when sending a payload over multiple chunks, and the chunks
 are signed using `AWS4-HMAC-SHA256`. This produces a SigV4
 signature. In addition, the digest for the chunks is included as a
 trailing header. |
| STREAMING-AWS4-ECDSA-P256-SHA256-PAYLOAD | Use this when sending a payload over multiple chunks, and the chunks
 are signed using `AWS4-ECDSA-P256-SHA256`. This produces a
 SigV4A signature. |
| STREAMING-AWS4-ECDSA-P256-SHA256-PAYLOAD-TRAILER | Use this when sending a payload over multiple chunks, and the chunks
 are signed using `AWS4-ECDSA-P256-SHA256`. This produces a
 SigV4A signature. In addition, the digest for the chunks is included
 as a trailing header. |



Upon receiving the request, Amazon S3 re-creates the string to sign using information in the
 `Authorization` header and the `date` header. It then
 verifies with authentication service the signatures match. The request date can be
 specified by using either the HTTP `Date` or the `x-amz-date`
 header. If both headers are present, `x-amz-date` takes precedence. 


If the signatures match, Amazon S3 processes your request; otherwise, your request
 will fail.
 



For more information, see the following topics:


[Signature Calculations for the Authorization Header:
 Transferring Payload in a Single Chunk (AWS Signature Version 4)](sig-v4-header-based-auth.md "sig-v4-header-based-auth.md")


[Signature Calculations for the Authorization Header:
 Transferring Payload in Multiple Chunks (Chunked Upload) (AWS Signature Version
 4)](sigv4-streaming.md "sigv4-streaming.md")


[Signature calculations for trailing headers
 (chunked uploads) (AWS Signature Version 4)](sigv4-streaming-trailers.md "sigv4-streaming-trailers.md")
