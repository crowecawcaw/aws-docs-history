**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) will no longer accept new customers starting December 15, 2025, with no impact to existing customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Initiate Multipart Upload (POST

multipart-uploads)

## Description

This operation initiates a multipart upload (see [Uploading Large Archives in Parts (Multipart Upload)](uploading-archive-mpu.md "uploading-archive-mpu.md")).
Amazon Glacier (Amazon Glacier) creates a multipart upload
resource and returns its ID in the response. You use this Upload ID in subsequent
multipart upload operations.

When you initiate a multipart upload, you specify the part size in number of bytes. The part
size must be a mebibyte (MiB) (1024 kibibytes [KiB]) multiplied by a power of 2—for example, 1048576
(1 MiB), 2097152 (2 MiB), 4194304 (4 MiB), 8388608 (8 MiB), and so on. The minimum allowable
part size is 1 MiB, and the maximum is 4 gibibytes (GiB).

Every part you upload using this upload ID, except the last one, must have the same size.
The last one can be the same size or smaller. For example, suppose you want to upload a
16.2 MiB file. If you initiate the multipart upload with a part size of 4 MiB, you will
upload four parts of 4 MiB each and one part of 0.2 MiB.

###### Note

You don't need to know the size of the archive when you start a multipart upload because
Amazon Glacier does not require you to specify the overall archive size.

After you complete the multipart upload, Amazon Glacier removes the multipart upload resource
referenced by the ID. Amazon Glacier will also remove the multipart upload resource if you
cancel the multipart upload or it may be removed if there is no activity for a period of
24 hours. The ID may still be available after 24 hours, but applications should not
expect this behavior.

## Requests

To initiate a multipart upload, you send an HTTP `POST` request to the URI of the
`multipart-uploads` subresource of the vault in which you want to save
the archive. The request must include the part size and can optionally include a
description of the archive.

### Syntax

```
POST /`AccountId`/vaults/`VaultName`/multipart-uploads
Host: glacier.us-west-2.amazonaws.com
Date: `Date`
Authorization: `SignatureValue`
x-amz-glacier-version: 2012-06-01
x-amz-archive-description: `ArchiveDescription`
x-amz-part-size: `PartSize`
```

###### Note

The `AccountId` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.

### Request Parameters

This operation does not use request parameters.

### Request Headers

This operation uses the following request headers, in addition to the request headers that are common to all operations.
For more information about the common request headers, see
[Common Request Headers](api-common-request-headers.md "api-common-request-headers.md").

| Name                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Required |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `x-amz-part-size`           | The size of each part except the last, in bytes. The last part can be smaller than<br>this part size.<br>Type: String<br>Default: None<br>Constraints: The part size must be a mebibyte (1024 KiB) multiplied by a power of<br>2—for example, 1048576 (1 MiB), 2097152 (2 MiB), 4194304 (4 MiB), 8388608 (8 MiB), and so on. The minimum allowable part size<br>is 1 MiB, and the maximum is 4 GiB (4096 MiB).                                                                                                                                                                                                                                                                        | Yes      |
| `x-amz-archive-description` | Archive description you are uploading in parts. It can be a plain-language<br>description or some unique identifier you choose to assign. When<br>you retrieve a vault inventory (see [Initiate Job (POST jobs)](api-initiate-job-post.md "api-initiate-job-post.md") ), the inventory<br>includes this description for each of the archives it returns in<br>response. Leading spaces in archive descriptions are<br>removed.<br>Type: String<br>Default: None<br>Constraints: The description must be less than or equal to 1024 bytes. The<br>allowable characters are 7 bit ASCII without control codes,<br>specifically ASCII values 32-126 decimal or 0x20-0x7E<br>hexadecimal. | No       |

### Request Body

This operation does not have a request body.

## Responses

In the response, Amazon Glacier creates a multipart upload resource identified by an ID and
returns the relative URI path of the multipart upload ID.

### Syntax

```
HTTP/1.1 201 Created
x-amzn-RequestId: **x-amzn-RequestId**
Date: **Date**
Location: ***Location***
x-amz-multipart-upload-id: ***multiPartUploadId***
```

### Response Headers

A successful response includes the following response headers, in addition to the response headers that are common to all operations. For more information about common response headers, see
[Common Response Headers](api-common-response-headers.md "api-common-response-headers.md").

| Name                        | Description                                                                                                                                                                                        |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Location`                  | The relative URI path of the multipart upload ID Amazon Glacier created. You use this<br>URI path to scope your requests to upload parts, and to complete<br>the multipart upload.<br>Type: String |
| `x-amz-multipart-upload-id` | The ID of the multipart upload. This value is also included<br>as part of the `Location` header.<br>Type: String                                                                                   |

### Response Body

This operation does not return a response body.

### Errors

For information about Amazon Glacier
exceptions and error messages, see [Error Responses](api-error-responses.md "api-error-responses.md").

## Example

### Example Request

The following example initiates a multipart upload by sending an HTTP `POST`
request to the URI of the `multipart-uploads` subresource of a vault
named `examplevault`. The request includes headers to specify the part
size of 4 MiB (4194304 bytes) and the optional archive description.

```
POST /-/vaults/examplevault/multipart-uploads
Host: glacier.us-west-2.amazonaws.com
x-amz-Date: 20170210T120000Z
x-amz-archive-description: MyArchive-101
x-amz-part-size: 4194304
x-amz-glacier-version: 2012-06-01
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20141123/us-west-2/glacier/aws4_request,SignedHeaders=host;x-amz-date;x-amz-glacier-version,Signature=9257c16da6b25a715ce900a5b45b03da0447acf430195dcb540091b12966f2a2
```

### Example Response

Amazon Glacier creates a multipart upload resource and adds it to the
`multipart-uploads` subresource of the vault. The
`Location` response header includes the relative URI path to the
multipart upload ID.

```
HTTP/1.1 201 Created
x-amzn-RequestId: AAABZpJrTyioDC_HsOmHae8EZp_uBSJr6cnGOLKp_XJCl-Q
Date: Wed, 10 Feb 2017 12:00:00 GMT
Location: /111122223333/vaults/examplevault/multipart-uploads/OW2fM5iVylEpFEMM9_HpKowRapC3vn5sSL39_396UW9zLFUWVrnRHaPjUJddQ5OxSHVXjYtrN47NBZ-khxOjyEXAMPLE
x-amz-multipart-upload-id: OW2fM5iVylEpFEMM9_HpKowRapC3vn5sSL39_396UW9zLFUWVrnRHaPjUJddQ5OxSHVXjYtrN47NBZ-khxOjyEXAMPLE
```

For information about uploading individual parts, see [Upload Part (PUT uploadID)](api-upload-part.md "api-upload-part.md").

## Related Sections

- [Upload Part (PUT uploadID)](api-upload-part.md "api-upload-part.md")
- [Complete Multipart Upload (POST uploadID)](api-multipart-complete-upload.md "api-multipart-complete-upload.md")
- [Abort Multipart Upload (DELETE uploadID)](api-multipart-abort-upload.md "api-multipart-abort-upload.md")
- [List Multipart Uploads (GET multipart-uploads)](api-multipart-list-uploads.md "api-multipart-list-uploads.md")
- [List Parts (GET uploadID)](api-multipart-list-parts.md "api-multipart-list-parts.md")
- [Delete Archive (DELETE archive)](api-archive-delete.md "api-archive-delete.md")
- [Uploading Large Archives in Parts (Multipart Upload)](uploading-archive-mpu.md "uploading-archive-mpu.md")
- [Identity and Access Management for Amazon Glacier](security-iam.md "security-iam.md")
