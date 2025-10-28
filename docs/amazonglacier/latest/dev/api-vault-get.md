**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) will no longer accept new customers starting December 15, 2025, with no impact to existing customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Describe Vault (GET vault)

## Description

This operation returns information about a vault, including the vault Amazon Resource
Name (ARN), the date the vault was created, the number of archives contained within the
vault, and the total size of all the archives in the vault. The number of archives and
their total size are as of the last vault inventory Amazon Glacier (Amazon Glacier) generated (see [Working with Vaults in Amazon Glacier](working-with-vaults.md "working-with-vaults.md")). Amazon Glacier generates
vault inventories approximately daily. This means that if you add or remove an archive
from a vault, and then immediately send a Describe Vault request, the response might not
reflect the changes.

## Requests

To get information about a vault, send a `GET` request to the URI of the
specific vault resource.

### Syntax

```
GET /`AccountId`/vaults/`VaultName` HTTP/1.1
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
HTTP/1.1 200 OK
x-amzn-RequestId: **x-amzn-RequestId**
Date: **Date**
Content-Type: application/json
Content-Length: ***Length***

{
  "CreationDate" : ***String***,
  "LastInventoryDate" : ***String***,
  "NumberOfArchives" : ***Number***,
  "SizeInBytes" : ***Number***,
  "VaultARN" : ***String***,
  "VaultName" : ***String***
}
```

### Response Headers

This operation uses only response headers that are common to most responses. For information about common response headers, see
[Common Response Headers](api-common-response-headers.md "api-common-response-headers.md").

### Response Body

The response body contains the following JSON fields.

**CreationDate**

The UTC date when the vault was created.

_Type_: A string representation in the ISO 8601 date format, for example `2013-03-20T17:03:43.221Z`.

**LastInventoryDate**

The UTC date when Amazon Glacier completed the last vault inventory. For
information about initiating an inventory for a vault, see [Initiate Job (POST jobs)](api-initiate-job-post.md "api-initiate-job-post.md").

_Type_: A string representation in the ISO 8601 date format, for example `2013-03-20T17:03:43.221Z`.

**NumberOfArchives**

The number of archives in the vault as per the last vault inventory.
This field will return null if an inventory has not yet run on the
vault, for example, if you just created the vault.

_Type_: Number

**SizeInBytes**

The total size in bytes of the archives in the vault including any
per-archive overhead, as of the last inventory date. This field will
return `null` if an inventory has not yet run on the vault,
for example, if you just created the vault.

_Type_: Number

**VaultARN**

The Amazon Resource Name (ARN) of the vault.

_Type_: String

**VaultName**

The vault name that was specified at creation time. The vault name is
also included in the vault's ARN.

_Type_: String

### Errors

For information about Amazon Glacier
exceptions and error messages, see [Error Responses](api-error-responses.md "api-error-responses.md").

## Examples

### Example Request

The following example demonstrates how to get information about the vault named
`examplevault`.

```
GET /-/vaults/examplevault HTTP/1.1
Host: glacier.us-west-2.amazonaws.com
x-amz-Date: 20170210T120000Z
x-amz-glacier-version: 2012-06-01
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20141123/us-west-2/glacier/aws4_request,SignedHeaders=host;x-amz-date;x-amz-glacier-version,Signature=9257c16da6b25a715ce900a5b45b03da0447acf430195dcb540091b12966f2a2
```

### Example Response

```
HTTP/1.1 200 OK
x-amzn-RequestId: AAABZpJrTyioDC_HsOmHae8EZp_uBSJr6cnGOLKp_XJCl-Q
Date: Wed, 10 Feb 2017 12:02:00 GMT
Content-Type: application/json
Content-Length: 260

{
  "CreationDate" : "2012-02-20T17:01:45.198Z",
  "LastInventoryDate" : "2012-03-20T17:03:43.221Z",
  "NumberOfArchives" : 192,
  "SizeInBytes" : 78088912,
  "VaultARN" : "arn:aws:glacier:us-west-2:012345678901:vaults/examplevault",
  "VaultName" : "examplevault"
}
```

## Related Sections

- [Create Vault (PUT vault)](api-vault-put.md "api-vault-put.md")
- [List Vaults (GET vaults)](api-vaults-get.md "api-vaults-get.md")
- [Delete Vault (DELETE vault)](api-vault-delete.md "api-vault-delete.md")
- [Initiate Job (POST jobs)](api-initiate-job-post.md "api-initiate-job-post.md")
- [Identity and Access Management for Amazon Glacier](security-iam.md "security-iam.md")

## See Also

For more information about using this API in one of the language-specific Amazon SDKs,
see the following:

- [AWS Command Line Interface](../../../cli/latest/reference/glacier/describe-vault.md "../../../cli/latest/reference/glacier/describe-vault.md")
