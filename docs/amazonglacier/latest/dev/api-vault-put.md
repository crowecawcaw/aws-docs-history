**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Create Vault (PUT vault)

## Description

This operation creates a new vault with the specified name.  The name of the vault
must be unique within an AWS Region for an AWS account. You can create up to 1,000 vaults per
account. For information on creating more vaults, go to the [Amazon Glacier product detail page](http://aws.amazon.com/glacier "http://aws.amazon.com/glacier").

You must use the following guidelines when naming a vault.

- Names can be between 1 and 255 characters long.
- Allowed characters are a–z, A–Z, 0–9, '\_' (underscore), '-' (hyphen),
  and '.' (period).

This operation is idempotent, you can send the same request
multiple times and it has no further effect after the first time Amazon Glacier (Amazon Glacier) creates
the specified vault.

## Requests

### Syntax

To create a vault, send an HTTP PUT request to the URI of the vault to be
created.

```
PUT /`AccountId`/vaults/`VaultName` HTTP/1.1
Host: glacier.`Region`.amazonaws.com
Date: `Date`
Authorization: `SignatureValue`
Content-Length: `Length`
x-amz-glacier-version: 2012-06-01
```

###### Note

The `AccountId` value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request.
If you specify your account ID, do not include any hyphens ('-') in the ID.

### Request Parameters

This operation does not use request parameters.

### Request Headers

This operation uses only request headers that are common to all operations. For information about common request headers, see
[Common Request Headers](api-common-request-headers.md "api-common-request-headers.md").

### Request Body

The request body for this operation must be empty (0 bytes).

## Responses

### Syntax

```
HTTP/1.1 201 Created
x-amzn-RequestId: **x-amzn-RequestId**
Date: **Date**
Location: ***Location***
```

### Response Headers

A successful response includes the following response headers, in addition to the response headers that are common to all operations. For more information about common response headers, see
[Common Response Headers](api-common-response-headers.md "api-common-response-headers.md").

| Name       | Description                                                          |
| ---------- | -------------------------------------------------------------------- |
| `Location` | The relative URI path of the vault that was created.<br>Type: String |

### Response Body

This operation does not return a response body.

### Errors

For information about Amazon Glacier
exceptions and error messages, see [Error Responses](api-error-responses.md "api-error-responses.md").

## Examples

### Example Request

The following example sends an HTTP PUT request to create a vault named
`examplevault`.

```
PUT /-/vaults/examplevault HTTP/1.1
Host: glacier.us-west-2.amazonaws.com
x-amz-Date: 20170210T120000Z
x-amz-glacier-version: 2012-06-01
Content-Length: 0
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20141123/us-west-2/glacier/aws4_request,SignedHeaders=host;x-amz-date;x-amz-glacier-version,Signature=9257c16da6b25a715ce900a5b45b03da0447acf430195dcb540091b12966f2a2
```

### Example Response

Amazon Glacier creates the vault and returns the relative URI path of the vault in the
`Location` header. The account ID is always displayed in the
`Location` header regardless of whether the account ID or a hyphen
('`-`') was specified in the request.

```
HTTP/1.1 201 Created
x-amzn-RequestId: AAABZpJrTyioDC_HsOmHae8EZp_uBSJr6cnGOLKp_XJCl-Q
Date: Wed, 10 Feb 2017 12:02:00 GMT
Location: /111122223333/vaults/examplevault
```

## Related Sections

- [List Vaults (GET vaults)](api-vaults-get.md "api-vaults-get.md")
- [Delete Vault (DELETE vault)](api-vault-delete.md "api-vault-delete.md")
- [Identity and Access Management for Amazon Glacier](security-iam.md "security-iam.md")

## See Also

For more information about using this API in one of the language-specific Amazon SDKs,
see the following:

- [AWS Command Line Interface](../../../cli/latest/reference/glacier/create-vault.md "../../../cli/latest/reference/glacier/create-vault.md")
