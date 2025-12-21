**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Upload Part (PUT uploadID)

## Description

This multipart upload operation uploads a part of an archive. You can upload archive parts
in any order because in your Upload Part request you specify the range of bytes in the
assembled archive that will be uploaded in this part. You can also upload these parts in
parallel. You can upload up to 10,000 parts for a multipart upload.

For information about multipart upload, see [Uploading Large Archives in Parts (Multipart Upload)](uploading-archive-mpu.md "uploading-archive-mpu.md").

Amazon Glacier (Amazon Glacier) rejects your upload part request if any of the following conditions is
true:

- SHA256 tree hash does not match—To ensure that part
  data is not corrupted in transmission, you compute a SHA256 tree hash of the
  part and include it in your request. Upon receiving the part data, Amazon Glacier
  also computes a SHA256 tree hash. If the two hash values don't match, the
  operation fails. For information about computing a SHA256 tree hash, see
  [Computing Checksums](checksum-calculations.md "checksum-calculations.md").
- SHA256 linear hash does not match—Required for
  authorization, you compute a SHA256 linear hash of the entire uploaded payload and include it in your request.
  For information about computing a SHA256 linear hash, see
  [Computing Checksums](checksum-calculations.md "checksum-calculations.md").
- Part size does not match—The size of each part except the last must match the size that is specified in the
  corresponding [Initiate Multipart Upload (POST
  multipart-uploads)](api-multipart-initiate-upload.md "api-multipart-initiate-upload.md") request. The size of the last part must
  be the same size as, or smaller than, the specified size.

###### Note

If you upload a part whose size is smaller than the part size you specified in your initiate
multipart upload request and that part is not the last part, then the
upload part request will succeed. However, the subsequent Complete
Multipart Upload request will fail.

- Range does not align—The byte range value in the
  request does not align with the part size specified in the corresponding
  initiate request. For example, if you specify a part size of 4194304 bytes
  (4 MB), then 0 to 4194303 bytes (4 MB —1) and 4194304 (4 MB) to
  8388607 (8 MB —1) are valid part ranges. However, if you set a range
  value of 2 MB to 6 MB, the range does not align with the part size and the
  upload will fail.

This operation is idempotent. If you upload the same part multiple times, the data included
in the most recent request overwrites the previously uploaded data.

## Requests

You send this HTTP `PUT` request to the URI of the upload ID that was returned by
your Initiate Multipart Upload request. Amazon Glacier uses the upload ID to associate
part uploads with a specific multipart upload. The request must include a SHA256 tree
hash of the part data (`x-amz-SHA256-tree-hash` header), a SHA256 linear hash of the entire payload (`x-amz-content-sha256` header),
the byte range (`Content-Range` header), and the length of the part in bytes (`Content-Length` header).

### Syntax

```
PUT /`AccountId`/vaults/`VaultName`/multipart-uploads/`uploadID` HTTP/1.1
Host: glacier.`Region`.amazonaws.com
Date: `Date`
Authorization: `SignatureValue`
Content-Range: `ContentRange`
Content-Length: `PayloadSize`
Content-Type: application/octet-stream
x-amz-sha256-tree-hash: `Checksum of the part`
x-amz-content-sha256: `Checksum of the entire payload`
x-amz-glacier-version: 2012-06-01
```

###### Note

The `AccountId` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.

### Request Parameters

This operation does not use request parameters.

### Request Headers

This operation uses the following request headers, in addition to the request headers that are common to all operations.
For more information about the common request headers, see
[Common Request Headers](api-common-request-headers.md "api-common-request-headers.md").

| Name                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Required |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| `Content-Length`          | Identifies the length of the part in bytes.<br>Type: String<br>Default: None<br>Constraints: None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | No       |
| `Content-Range`           | Identifies the range of bytes in the assembled archive that will be uploaded in<br>this part. Amazon Glacier uses this information to assemble the<br>archive in the proper sequence. The format of this header<br>follows [RFC<br>2616](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16 "http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16"). An example header is `Content-Range:bytes<br>0-4194303/*`.<br>Type: String<br>Default: None<br>Constraints: The range cannot be greater than the part size that you specified<br>when you initiated the multipart upload. | Yes      |
| `x-amz-content-sha256`    | The SHA256 checksum (a linear hash) of the uploaded payload.<br>This is not the same value as you specify in the<br>`x-amz-sha256-tree-hash` header.<br>Type: String<br>Default: None<br>Constraints: None                                                                                                                                                                                                                                                                                                                                                                                             | Yes      |
| `x-amz-sha256-tree-hash`​ | Specifies a SHA256 tree hash of the data being uploaded. For information about<br>computing a SHA256 tree<br>hash,<br>see [Computing Checksums](checksum-calculations.md "checksum-calculations.md").<br>Type: String<br>Default: None<br>Constraints: None                                                                                                                                                                                                                                                                                                                                            | Yes      |

### Request Body

The request body contains the data to upload.

## Responses

Upon a successful part upload, Amazon Glacier returns a `204 No Content`
response.

### Syntax

```
HTTP/1.1 204 No Content
x-amzn-RequestId: **x-amzn-RequestId**
Date: **Date**
x-amz-sha256-tree-hash: ***ChecksumComputedByAmazonGlacier***
```

### Response Headers

A successful response includes the following response headers, in addition to the response headers that are common to all operations. For more information about common response headers, see
[Common Response Headers](api-common-response-headers.md "api-common-response-headers.md").

| Name                      | Description                                                                              |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| `x-amz-sha256-tree-hash`​ | The SHA256 tree hash that Amazon Glacier computed for the uploaded part.<br>Type: String |

### Response Body

This operation does not return a response body.

## Example

The following request uploads a 4 MB part. The request sets the byte range to make this the
first part in the archive.

### Example Request

The example sends an HTTP `PUT` request to upload a 4 MB part. The request is
sent to the URI of the Upload ID that was returned by the Initiate Multipart Upload
request. The `Content-Range` header identifies the part as the first 4 MB
data part of the archive.

```
PUT /-/vaults/examplevault/multipart-uploads/OW2fM5iVylEpFEMM9_HpKowRapC3vn5sSL39_396UW9zLFUWVrnRHaPjUJddQ5OxSHVXjYtrN47NBZ-khxOjyEXAMPLE HTTP/1.1
Host: glacier.us-west-2.amazonaws.com
Date: Wed, 10 Feb 2017 12:00:00 GMT
Content-Range:bytes 0-4194303/*
x-amz-sha256-tree-hash:c06f7cd4baacb087002a99a5f48bf953
x-amz-content-sha256:726e392cb4d09924dbad1cc0ba3b00c3643d03d14cb4b823e2f041cff612a628
Content-Length: 4194304
Authorization: Authorization=AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20141123/us-west-2/glacier/aws4_request,SignedHeaders=host;x-amz-content-sha256;x-amz-date;x-amz-glacier-version,Signature=16b9a9e220a37e32f2e7be196b4ebb87120ca7974038210199ac5982e792cace
```

To upload the next part, the procedure is the same; however, you must calculate a new
SHA256 tree hash of the part you are uploading and also specify a new byte range to
indicate where the part will go in the final assembly. The following request uploads
another part using the same upload ID. The request specifies the next 4 MB of the
archive after the previous request and a part size of 4 MB.

```
PUT /-/vaults/examplevault/multipart-uploads/OW2fM5iVylEpFEMM9_HpKowRapC3vn5sSL39_396UW9zLFUWVrnRHaPjUJddQ5OxSHVXjYtrN47NBZ-khxOjyEXAMPLE HTTP/1.1
Host: glacier.us-west-2.amazonaws.com
Date: Wed, 10 Feb 2017 12:00:00 GMT
Content-Range:bytes 4194304-8388607/*
Content-Length: 4194304
x-amz-sha256-tree-hash:f10e02544d651e2c3ce90a4307427493
x-amz-content-sha256:726e392cb4d09924dbad1cc0ba3b00c3643d03d14cb4b823e2f041cff612a628
x-amz-glacier-version: 2012-06-01
Authorization: Authorization=AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20120525/us-west-2/glacier/aws4_request, SignedHeaders=host;x-amz-content-sha256;x-amz-date;x-amz-glacier-version, Signature=16b9a9e220a37e32f2e7be196b4ebb87120ca7974038210199ac5982e792cace
```

The parts can be uploaded in any order; Amazon Glacier uses the range specification for each
part to determine the order in which to assemble them.

### Example Response

```
HTTP/1.1 204 No Content
x-amzn-RequestId: AAABZpJrTyioDC_HsOmHae8EZp_uBSJr6cnGOLKp_XJCl-Q
x-amz-sha256-tree-hash: c06f7cd4baacb087002a99a5f48bf953
Date: Wed, 10 Feb 2017 12:00:00 GMT
```

## Related Sections

- [Initiate Multipart Upload (POST
  multipart-uploads)](api-multipart-initiate-upload.md "api-multipart-initiate-upload.md")
- [Upload Part (PUT uploadID)](api-upload-part.md "api-upload-part.md")
- [Complete Multipart Upload (POST uploadID)](api-multipart-complete-upload.md "api-multipart-complete-upload.md")
- [Abort Multipart Upload (DELETE uploadID)](api-multipart-abort-upload.md "api-multipart-abort-upload.md")
- [List Multipart Uploads (GET multipart-uploads)](api-multipart-list-uploads.md "api-multipart-list-uploads.md")
- [List Parts (GET uploadID)](api-multipart-list-parts.md "api-multipart-list-parts.md")
- [Uploading Large Archives in Parts (Multipart Upload)](uploading-archive-mpu.md "uploading-archive-mpu.md")
- [Identity and Access Management for Amazon Glacier](security-iam.md "security-iam.md")
