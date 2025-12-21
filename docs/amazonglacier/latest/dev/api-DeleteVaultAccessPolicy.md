**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Delete Vault Access Policy (DELETE

access-policy)

## Description

This operation deletes the access policy associated with the specified vault. The
operation is eventually consistent—that is, it might take some time for Amazon Glacier (Amazon Glacier)
to completely remove the access policy, and you might still see the effect of the policy
for a short time after you send the delete request.

This operation is idempotent. You can invoke delete multiple times, even if there is
no policy associated with the vault. For more information about vault access policies,
see [Vault Access Policies](vault-access-policy.md "vault-access-policy.md").

## Requests

To delete the current vault access policy, send an HTTP `DELETE` request to
the URI of the vault's `access-policy` subresource.

### Syntax

```
DELETE /`AccountId`/vaults/`vaultName`/access-policy HTTP/1.1
Host: glacier.`Region`.amazonaws.com
Date: `Date`
Authorization: `SignatureValue`
x-amz-glacier-version: 2012-06-01
```

###### Note

The `AccountId` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.

### Request

Parameters

This operation does not use request parameters.

### Request

Headers

This operation uses only request headers that are common to all operations. For information about common request headers, see
[Common Request Headers](api-common-request-headers.md "api-common-request-headers.md").

### Request Body

This operation does not have a request body.

## Responses

In response, Amazon Glacier returns `204 No Content` if the policy is successfully
deleted.

### Syntax

```
HTTP/1.1 204 No Content
x-amzn-RequestId: **x-amzn-RequestId**
Date: **Date**
```

### Response

Headers

This operation uses only response headers that are common to most responses. For information about common response headers, see
[Common Response Headers](api-common-response-headers.md "api-common-response-headers.md").

### Response

Body

This operation does not return a response body.

### Errors

For information about Amazon Glacier
exceptions and error messages, see [Error Responses](api-error-responses.md "api-error-responses.md").

## Examples

The following example demonstrates how to delete a vault access policy.

### Example

Request

In this example, a `DELETE` request is sent to the
`access-policy` subresource of the vault named
`examplevault`.

```
DELETE /-/vaults/examplevault/access-policy HTTP/1.1
Host: glacier.us-west-2.amazonaws.com
x-amz-Date: 20170210T120000Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20141123/us-west-2/glacier/aws4_request,SignedHeaders=host;x-amz-date;x-amz-glacier-version,Signature=9257c16da6b25a715ce900a5b45b03da0447acf430195dcb540091b12966f2a2
x-amz-glacier-version: 2012-06-01

```

### Example

Response

In response, if the policy is successfully deleted Amazon Glacier returns a `204 No
 Content` as shown in the following example.

```
HTTP/1.1 204 No Content
x-amzn-RequestId: AAABZpJrTyioDC_HsOmHae8EZp_uBSJr6cnGOLKp_XJCl-Q
Date: Wed, 10 Feb 2017 12:00:00 GMT

```

## Related Sections

- [Get Vault Access Policy (GET access-policy)](api-GetVaultAccessPolicy.md "api-GetVaultAccessPolicy.md")

- [Set Vault Access Policy (PUT access-policy)](api-SetVaultAccessPolicy.md "api-SetVaultAccessPolicy.md")

## See Also

For more information about using this API in one of the language-specific Amazon SDKs,
see the following:

- [AWS Command Line Interface](../../../cli/latest/reference/glacier/delete-vault-access-policy.md "../../../cli/latest/reference/glacier/delete-vault-access-policy.md")
