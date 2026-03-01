**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Abort Multipart Upload (DELETE uploadID)

## Description

This command for multipart upload operation stops a multipart upload identified by the upload
ID.

After the Abort Multipart Upload request succeeds, you cannot use the upload ID to
upload any more parts or perform any other operations. Stopping a completed multipart
upload fails. However, stopping an already-stopped upload will succeed, for a short
time.

This operation is idempotent.

For information about multipart upload, see [Uploading Large Archives in Parts (Multipart Upload)](uploading-archive-mpu.md "uploading-archive-mpu.md").

## Requests

To stop a multipart upload, send an HTTP `DELETE` request to the URI of the
`multipart-uploads` subresource of the vault and identify the specific
multipart upload ID as part of the URI.

### Syntax

```
DELETE /`AccountId`/vaults/`VaultName`/multipart-uploads/`uploadID` HTTP/1.1
Host: glacier.`Region`.amazonaws.com
Date: `Date`
Authorization: `SignatureValue`
x-amz-glacier-version: 2012-06-01
```

###### Note

The `AccountId` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.

### Request Parameters

This operation does not use request parameters.

### Request Headers

This operation uses only request headers that are common to all operations. For information about common request headers, see
[Common Request Headers](api-common-request-headers.md "api-common-request-headers.md").

### Request Body

This operation does not have a request body.

## Responses

### Syntax

```
HTTP/1.1 204 No Content
x-amzn-RequestId: **x-amzn-RequestId**
Date: **Date**
```

### Response Headers

This operation uses only response headers that are common to most responses. For information about common response headers, see
[Common Response Headers](api-common-response-headers.md "api-common-response-headers.md").

### Response Body

This operation does not return a response body.

### Errors

For information about Amazon Glacier
exceptions and error messages, see [Error Responses](api-error-responses.md "api-error-responses.md").

## Example

### Example Request

In the following example, a `DELETE` request is sent to the URI of a multipart
upload ID resource.

```
DELETE /-/vaults/examplevault/multipart-uploads/OW2fM5iVylEpFEMM9_HpKowRapC3vn5sSL39_396UW9zLFUWVrnRHaPjUJddQ5OxSHVXjYtrN47NBZ-khxOjyEXAMPLE  HTTP/1.1
Host: glacier.us-west-2.amazonaws.com
x-amz-Date: 20170210T120000Z
x-amz-glacier-version: 2012-06-01
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20141123/us-west-2/glacier/aws4_request,SignedHeaders=host;x-amz-date;x-amz-glacier-version,Signature=9257c16da6b25a715ce900a5b45b03da0447acf430195dcb540091b12966f2a2
```

### Example Response

```
HTTP/1.1 204 No Content
x-amzn-RequestId: AAABZpJrTyioDC_HsOmHae8EZp_uBSJr6cnGOLKp_XJCl-Q
Date: Wed, 10 Feb 2017 12:00:00 GMT
```

## Related Sections

- [Initiate Multipart Upload (POST multipart-uploads)](api-multipart-initiate-upload.md "api-multipart-initiate-upload.md")
- [Upload Part (PUT uploadID)](api-upload-part.md "api-upload-part.md")
- [Complete Multipart Upload (POST uploadID)](api-multipart-complete-upload.md "api-multipart-complete-upload.md")
- [List Multipart Uploads (GET multipart-uploads)](api-multipart-list-uploads.md "api-multipart-list-uploads.md")
- [List Parts (GET uploadID)](api-multipart-list-parts.md "api-multipart-list-parts.md")
- [Uploading Large Archives in Parts (Multipart Upload)](uploading-archive-mpu.md "uploading-archive-mpu.md")
- [Identity and Access Management for Amazon Glacier](security-iam.md "security-iam.md")
