**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Delete Vault (DELETE vault)

## Description

This operation deletes a vault. Amazon Glacier (Amazon Glacier) will delete a vault only if there are
no archives in the vault as per the last inventory and there have been no writes to the
vault since the last inventory. If either of these conditions is not satisfied, the
vault deletion fails (that is, the vault is not removed) and Amazon Glacier returns an error.

You can use the [Describe Vault (GET vault)](api-vault-get.md "api-vault-get.md")
operation that provides vault information, including the number of archives in the
vault; however, the information is based on the vault inventory Amazon Glacier last
generated.

This operation is idempotent.

###### Note

When you delete a vault, the vault access policy attached to the vault is also
deleted. For more information about vault access policies, see [Vault Access Policies](vault-access-policy.md "vault-access-policy.md").

## Requests

To delete a vault, send a `DELETE` request to the vault resource
URI.

### Syntax

```
DELETE /`AccountId`/vaults/`VaultName` HTTP/1.1
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

## Examples

### Example Request

The following example deletes a vault named `examplevault`. The example
request is a `DELETE` request to the URI of the resource (the vault) to
delete.

```
DELETE /-/vaults/examplevault HTTP/1.1
Host: glacier.us-west-2.amazonaws.com
x-amz-Date: 20170210T120000Z
x-amz-glacier-version: 2012-06-01
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20141123/us-west-2/glacier/aws4_request,SignedHeaders=host;x-amz-date;x-amz-glacier-version,Signature=9257c16da6b25a715ce900a5b45b03da0447acf430195dcb540091b12966f2a2
```

### Example Response

```
HTTP/1.1 204 No Content
x-amzn-RequestId: AAABZpJrTyioDC_HsOmHae8EZp_uBSJr6cnGOLKp_XJCl-Q
Date: Wed, 10 Feb 2017 12:02:00 GMT
```

## Related Sections

- [Create Vault (PUT vault)](api-vault-put.md "api-vault-put.md")
- [List Vaults (GET vaults)](api-vaults-get.md "api-vaults-get.md")
- [Initiate Job (POST jobs)](api-initiate-job-post.md "api-initiate-job-post.md")
- [Identity and Access Management for Amazon Glacier](security-iam.md "security-iam.md")

## See Also

For more information about using this API in one of the language-specific Amazon SDKs,
see the following:

- [AWS Command Line Interface](../../../cli/latest/reference/glacier/delete-vault.md "../../../cli/latest/reference/glacier/delete-vault.md")
