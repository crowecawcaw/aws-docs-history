**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) will no longer accept new customers starting December 15, 2025, with no impact to existing customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Complete Multipart Upload (POST uploadID)

## Description

You call this multipart upload operation to inform Amazon Glacier (Amazon Glacier) that all the
archive parts have been uploaded and Amazon Glacier can now assemble the archive from the
uploaded parts.

For information about multipart upload, see [Uploading Large Archives in Parts (Multipart Upload)](uploading-archive-mpu.md "uploading-archive-mpu.md").

After assembling and saving the archive to the vault, Amazon Glacier returns the archive ID
of the newly created archive resource. After you upload an archive, you should save the
archive ID returned to retrieve the archive at a later point.

In the request, you must include the computed SHA256 tree hash of the entire archive
you have uploaded. For information about computing a SHA256 tree hash, see [Computing Checksums](checksum-calculations.md "checksum-calculations.md"). On the
server side, Amazon Glacier also constructs the SHA256 tree hash of the assembled archive. If
the values match, Amazon Glacier saves the archive to the vault; otherwise, it returns an
error, and the operation fails. The [List Parts (GET uploadID)](api-multipart-list-parts.md "api-multipart-list-parts.md") operation returns list of parts uploaded
for a specific multipart upload. It includes checksum information for each uploaded part
that can be used to debug a bad checksum issue.

Additionally, Amazon Glacier also checks for any missing content ranges. When uploading
parts, you specify range values identifying where each part fits in the final assembly
of the archive. When assembling the final archive Amazon Glacier checks for any missing
content ranges and if there are any missing content ranges, Amazon Glacier returns an error
and the Complete Multipart Upload operation fails.

Complete Multipart Upload is an idempotent operation. After your first successful
complete multipart upload, if you call the operation again within a short period, the
operation will succeed and return the same archive ID. This is useful in the event you
experience a network issue or receive a 500 server error, in which case you can repeat
your Complete Multipart Upload request and get the same archive ID without creating
duplicate archives. Note, however, that after the multipart upload completes, you cannot
call the List Parts operation and the multipart upload will not appear in List Multipart
Uploads response, even if idempotent complete is possible.

## Requests

To complete a multipart upload, you send an HTTP POST request to the URI of the upload ID
that Amazon Glacier created in response to your Initiate Multipart Upload request. This is
the same URI you used when uploading parts. In addition to the common required headers,
you must include the result of the SHA256 tree hash of the entire archive and the total
size of the archive in bytes.

### Syntax

```
POST /`AccountId`/vaults/`VaultName`/multipart-uploads/`uploadID`
Host: glacier.`Region`.amazonaws.com
Date: `date`
Authorization: `SignatureValue`
x-amz-sha256-tree-hash: `SHA256 tree hash of the archive`
x-amz-archive-size: `ArchiveSize in bytes`
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

| Name                      | Description                                                                                                                                                                                                                                                                                                                                                                     | Required |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `x-amz-archive-size`      | The total size, in bytes, of the entire archive. This value should be the sum of<br>all the sizes of the individual parts that you<br>uploaded.<br>Type: String<br>Default: None<br>Constraints: None                                                                                                                                                                           | Yes      |
| `x-amz-sha256-tree-hash`​ | The SHA256 tree hash of the entire archive. It is the tree hash of SHA256 tree<br>hash of the individual parts. If the value you specify in<br>the request does not match the SHA256 tree hash of the final<br>assembled archive as computed by Amazon Glacier, Amazon Glacier<br>returns an error and the request fails.<br>Type: String<br>Default: None<br>Constraints: None | Yes      |

### Request Elements

This operation does not use request elements.

## Responses

Amazon Glacier (Amazon Glacier) creates a SHA256 tree hash of the entire archive. If the value matches the SHA256
tree hash of the entire archive you specified in the request, Amazon Glacier adds the archive
to the vault. In response it returns the HTTP `Location` header with the URL
path of the newly added archive resource. If the archive size or SHA256 that you sent in
the request does not match, Amazon Glacier will return an error and the upload remains
in the incomplete state. It is possible to retry the Complete Multipart Upload operation
later with correct values, at which point you can successfully create an archive. If a
multipart upload does not complete, then eventually Amazon Glacier will reclaim the
upload ID.

### Syntax

```
HTTP/1.1 201 Created
x-amzn-RequestId: **x-amzn-RequestId**
Date: **Date**
Location: ***Location***
x-amz-archive-id: ***ArchiveId***
```

### Response Headers

A successful response includes the following response headers, in addition to the response headers that are common to all operations. For more information about common response headers, see
[Common Response Headers](api-common-response-headers.md "api-common-response-headers.md").

| Name               | Description                                                                                                                                  |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `Location`         | The relative URI path of the newly created archive. This URL includes the archive<br>ID that is generated by Amazon Glacier.<br>Type: String |
| `x-amz-archive-id` | The ID of the archive. This value is also included as part<br>of the `Location` header.<br>Type: String                                      |

### Response Fields

This operation does not return a response body.

## Example

### Example Request

In this example, an HTTP POST request is sent to the URI that was returned by an Initiate
Multipart Upload request. The request specifies both the SHA256 tree hash of the
entire archive and the total archive size.

```
POST /-/vaults/examplevault/multipart-uploads/OW2fM5iVylEpFEMM9_HpKowRapC3vn5sSL39_396UW9zLFUWVrnRHaPjUJddQ5OxSHVXjYtrN47NBZ-khxOjyEXAMPLE HTTP/1.1
Host: glacier.us-west-2.amazonaws.com
z-amz-Date: 20170210T120000Z
x-amz-sha256-tree-hash:1ffc0f54dd5fdd66b62da70d25edacd0
x-amz-archive-size:8388608
x-amz-glacier-version: 2012-06-01
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20141123/us-west-2/glacier/aws4_request,SignedHeaders=host;x-amz-date;x-amz-glacier-version,Signature=9257c16da6b25a715ce900a5b45b03da0447acf430195dcb540091b12966f2a2
```

### Example Response

The following example response shows that Amazon Glacier successfully created an archive from
the parts you uploaded. The response includes the archive ID with complete path.

```
HTTP/1.1 201 Created
x-amzn-RequestId: AAABZpJrTyioDC_HsOmHae8EZp_uBSJr6cnGOLKp_XJCl-Q
Date: Wed, 10 Feb 2017 12:00:00 GMT
Location: /111122223333/vaults/examplevault/archives/NkbByEejwEggmBz2fTHgJrg0XBoDfjP4q6iu87-TjhqG6eGoOY9Z8i1_AUyUsuhPAdTqLHy8pTl5nfCFJmDl2yEZONi5L26Omw12vcs01MNGntHEQL8MBfGlqrEXAMPLEArchiveId
x-amz-archive-id: NkbByEejwEggmBz2fTHgJrg0XBoDfjP4q6iu87-TjhqG6eGoOY9Z8i1_AUyUsuhPAdTqLHy8pTl5nfCFJmDl2yEZONi5L26Omw12vcs01MNGntHEQL8MBfGlqrEXAMPLEArchiveId
```

You can now send HTTP requests to the URI of the newly added resource/archive. For example,
you can send a GET request to retrieve the archive.

## Related Sections

- [Initiate Multipart Upload (POST
  multipart-uploads)](api-multipart-initiate-upload.md "api-multipart-initiate-upload.md")
- [Upload Part (PUT uploadID)](api-upload-part.md "api-upload-part.md")
- [Abort Multipart Upload (DELETE uploadID)](api-multipart-abort-upload.md "api-multipart-abort-upload.md")
- [List Multipart Uploads (GET multipart-uploads)](api-multipart-list-uploads.md "api-multipart-list-uploads.md")
- [List Parts (GET uploadID)](api-multipart-list-parts.md "api-multipart-list-parts.md")
- [Uploading Large Archives in Parts (Multipart Upload)](uploading-archive-mpu.md "uploading-archive-mpu.md")
- [Delete Archive (DELETE archive)](api-archive-delete.md "api-archive-delete.md")
- [Identity and Access Management for Amazon Glacier](security-iam.md "security-iam.md")
