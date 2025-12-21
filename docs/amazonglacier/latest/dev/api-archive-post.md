**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Upload Archive (POST archive)

## Description

This operation adds an archive to a vault. For a successful upload, your data is
durably persisted. In response, Amazon Glacier (Amazon Glacier) returns the archive ID in the
`x-amz-archive-id` header of the response. You should save the archive ID
returned so that you can access the archive later.

You must provide a SHA256 tree hash of the data you are uploading. For information
about computing a SHA256 tree hash, see [Computing Checksums](checksum-calculations.md "checksum-calculations.md").

###### Note

The SHA256 tree hash is only required for the Upload Archive (POST archive) action
when using the API. It is not required when using the AWS CLI.

When uploading an archive, you can optionally specify an archive description of up to
1,024 printable ASCII characters. Amazon Glacier returns the archive description when you
either retrieve the archive or get the vault inventory. Amazon Glacier does not interpret the
description in any way. An archive description does not need to be unique. You cannot
use the description to retrieve or sort the archive list.

Except for the optional archive description, Amazon Glacier does not support any additional
metadata for the archives. The archive ID is an opaque sequence of characters from which
you cannot infer any meaning about the archive. So you might maintain metadata about the
archives on the client-side. For more information, see [Working with Archives in Amazon Glacier](working-with-archives.md "working-with-archives.md").

Archives are immutable. After you upload an archive, you cannot edit the archive or
its description.

## Requests

To upload an archive, you use the HTTP `POST` method and scope the request
to the `archives` subresource of the vault in which you want to save the
archive. The request must include the archive payload size, checksum (SHA256 tree hash),
and can optionally include a description of the archive.

### Syntax

```
POST /`AccountId`/vaults/`VaultName`/archives
Host: glacier.`Region`.amazonaws.com
x-amz-glacier-version: 2012-06-01
Date: `Date`
Authorization: `SignatureValue`
x-amz-archive-description: `Description`
x-amz-sha256-tree-hash: `SHA256 tree hash`
x-amz-content-sha256: `SHA256 linear hash`
Content-Length: `Length`

<Request body.>
```

###### Note

The `AccountId` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.

### Request Parameters

This implementation of the operation does not use request parameters.

### Request Headers

This operation uses the following request headers, in addition to the request headers that are common to all operations.
For more information about the common request headers, see
[Common Request Headers](api-common-request-headers.md "api-common-request-headers.md").

| Name                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Required |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `Content-Length`            | The size of the object, in bytes. For more information, go to<br>[http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.13](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.13 "http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.13").<br>Type: Number<br>Default: None<br>Constraints: None                                                                                                                                                                                                                                                                                                                                                        | Yes      |
| `x-amz-archive-description` | The optional description of the archive you are uploading. It<br>can be a plain language description or some identifier you<br>choose to assign. The description need not be unique across<br>archives. When you retrieve a vault inventory (see [Initiate Job (POST jobs)](api-initiate-job-post.md "api-initiate-job-post.md")), it includes this<br>description for each of the archives it returns in<br>response.<br>Type: String<br>Default: None<br>Constraints: The description must be less than or equal to<br>1,024 characters. The allowable characters are 7-bit ASCII<br>without control codes, specifically ASCII values 32—126<br>decimal or 0x20—0x7E hexadecimal. | No       |
| `x-amz-content-sha256`      | The SHA256 checksum (a linear hash) of the payload. This is<br>not the same value as you specify in the<br>`x-amz-sha256-tree-hash` header.<br>Type: String<br>Default: None<br>Constraints: None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Yes      |
| `x-amz-sha256-tree-hash`    | The user-computed checksum, SHA256 tree hash, of the payload.<br>For information on computing the SHA256 tree hash, see [Computing Checksums](checksum-calculations.md "checksum-calculations.md"). If Amazon Glacier<br>computes a different checksum of the payload, it will reject the<br>request.<br>Type: String<br>Default: None<br>Constraints: None                                                                                                                                                                                                                                                                                                                         | Yes      |

### Request Body

The request body contains the data to upload.

## Responses

In response, Amazon Glacier durably stores the archive and returns a URI path to the
archive ID.

### Syntax

```
HTTP/1.1 201 Created
x-amzn-RequestId: **x-amzn-RequestId**
Date: **Date**
x-amz-sha256-tree-hash: ***ChecksumComputedByAmazonGlacier***
Location: ***Location***
x-amz-archive-id: ***ArchiveId***
```

### Response Headers

A successful response includes the following response headers, in addition to the response headers that are common to all operations. For more information about common response headers, see
[Common Response Headers](api-common-response-headers.md "api-common-response-headers.md").

| Name                      | Description                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------------------- |
| `Location`                | The relative URI path of the newly added archive resource.<br>Type: String                              |
| `x-amz-archive-id`        | The ID of the archive. This value is also included as part of<br>the `Location` header.<br>Type: String |
| `x-amz-sha256-tree-hash`​ | The checksum of the archive computed by Amazon Glacier.<br>Type: String                                 |

### Response Body

This operation does not return a response body.

### Errors

For information about Amazon Glacier
exceptions and error messages, see [Error Responses](api-error-responses.md "api-error-responses.md").

## Examples

### Example Request

The following example shows a request to upload an archive.

```
POST /-/vaults/examplevault/archives HTTP/1.1
Host: glacier.us-west-2.amazonaws.com
x-amz-Date: 20170210T120000Z
x-amz-sha256-tree-hash: beb0fe31a1c7ca8c6c04d574ea906e3f97b31fdca7571defb5b44dca89b5af60
x-amz-content-sha256: 7f2fe580edb35154041fa3d4b41dd6d3adaef0c85d2ff6309f1d4b520eeecda3
Content-Length: 2097152
x-amz-glacier-version: 2012-06-01
Authorization: Authorization=AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20141123/us-west-2/glacier/aws4_request,SignedHeaders=host;x-amz-content-sha256;x-amz-date;x-amz-glacier-version,Signature=16b9a9e220a37e32f2e7be196b4ebb87120ca7974038210199ac5982e792cace

<Request body (2097152 bytes).>
```

### Example Response

The successful response below has a `Location` header where you can get
the ID that Amazon Glacier assigned to the archive.

```
HTTP/1.1 201 Created
x-amzn-RequestId: AAABZpJrTyioDC_HsOmHae8EZp_uBSJr6cnGOLKp_XJCl-Q
Date: Wed, 10 Feb 2017 12:00:00 GMT
x-amz-sha256-tree-hash: beb0fe31a1c7ca8c6c04d574ea906e3f97b31fdca7571defb5b44dca89b5af60
Location: /111122223333/vaults/examplevault/archives/NkbByEejwEggmBz2fTHgJrg0XBoDfjP4q6iu87-TjhqG6eGoOY9Z8i1_AUyUsuhPAdTqLHy8pTl5nfCFJmDl2yEZONi5L26Omw12vcs01MNGntHEQL8MBfGlqrEXAMPLEArchiveId
x-amz-archive-id: NkbByEejwEggmBz2fTHgJrg0XBoDfjP4q6iu87-TjhqG6eGoOY9Z8i1_AUyUsuhPAdTqLHy8pTl5nfCFJmDl2yEZONi5L26Omw12vcs01MNGntHEQL8MBfGlqrEXAMPLEArchiveId
```

## Related Sections

- [Working with Archives in Amazon Glacier](working-with-archives.md "working-with-archives.md")
- [Uploading Large Archives in Parts (Multipart Upload)](uploading-archive-mpu.md "uploading-archive-mpu.md")
- [Delete Archive (DELETE archive)](api-archive-delete.md "api-archive-delete.md")
- [Identity and Access Management for Amazon Glacier](security-iam.md "security-iam.md")
