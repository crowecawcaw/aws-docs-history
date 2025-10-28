**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) will no longer accept new customers starting December 15, 2025, with no impact to existing customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Delete Archive (DELETE archive)

## Description

This operation deletes an archive from a vault. You can delete one archive at a time from a vault.
To delete the archive you must provide its archive ID in the delete request.
You can get the archive ID by downloading the vault inventory for the vault that contains the archive.
For more information about downloading the vault inventory,
see [Downloading a Vault Inventory in Amazon Glacier](vault-inventory.md "vault-inventory.md").

After you delete an archive, you might still
be able to make a successful request to initiate a job to retrieve the deleted archive,
but the archive retrieval job will fail.

Archive retrievals that are in progress for an archive ID when you delete the
archive might or might not succeed according to the following scenarios:

- If the archive retrieval job is actively preparing the data for download when Amazon Glacier (Amazon Glacier)
  receives the delete archive request, the archival retrieval operation might fail.
- If the archive retrieval job has successfully prepared the archive for download when
  Amazon Glacier receives the delete archive request, you will be able to
  download the output.

For more information about archive retrieval, see
[Downloading an Archive in Amazon Glacier](downloading-an-archive.md "downloading-an-archive.md").

This operation is idempotent. Attempting
to delete an already-deleted archive does not result in an error.

## Requests

To delete an archive you send a `DELETE` request to the archive resource
URI.

### Syntax

```
DELETE /`AccountId`/vaults/`VaultName`/archives/`ArchiveID` HTTP/1.1
Host: glacier.`Region`.amazonaws.com
x-amz-Date: `Date`
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

## Examples

The following example demonstrates how to delete an archive from the vault named
`examplevault`.

### Example Request

The ID of the archive to be deleted is specified as a subresource of
`archives`.

```
DELETE /-/vaults/examplevault/archives/NkbByEejwEggmBz2fTHgJrg0XBoDfjP4q6iu87-TjhqG6eGoOY9Z8i1_AUyUsuhPAdTqLHy8pTl5nfCFJmDl2yEZONi5L26Omw12vcs01MNGntHEQL8MBfGlqrEXAMPLEArchiveId HTTP/1.1
Host: glacier.us-west-2.amazonaws.com
x-amz-Date: 20170210T120000Z
x-amz-glacier-version: 2012-06-01
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20141123/us-west-2/glacier/aws4_request,SignedHeaders=host;x-amz-date;x-amz-glacier-version,Signature=9257c16da6b25a715ce900a5b45b03da0447acf430195dcb540091b12966f2a2
```

### Example Response

If the request is successful, Amazon Glacier responds with `204 No Content` to
indicate that the archive is deleted.

```
HTTP/1.1 204 No Content
x-amzn-RequestId: AAABZpJrTyioDC_HsOmHae8EZp_uBSJr6cnGOLKp_XJCl-Q
Date: Wed, 10 Feb 2017 12:00:00 GMT
```

## Related Sections

- [Initiate Multipart Upload (POST
  multipart-uploads)](api-multipart-initiate-upload.md "api-multipart-initiate-upload.md")
- [Upload Archive (POST archive)](api-archive-post.md "api-archive-post.md")
- [Identity and Access Management for Amazon Glacier](security-iam.md "security-iam.md")
