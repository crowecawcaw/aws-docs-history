**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) will no longer accept new customers starting December 15, 2025, with no impact to existing customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Abort Vault Lock (DELETE lock-policy)

## Description

This operation stops the vault locking process if the vault lock is not in the
`Locked` state. If the vault lock is in the `Locked` state
when this operation is requested, the operation returns an
`AccessDeniedException` error. Stopping the vault locking process removes
the vault lock policy from the specified vault.

A vault lock is put into the `InProgress` state by calling [Initiate Vault Lock (POST lock-policy)](api-InitiateVaultLock.md "api-InitiateVaultLock.md"). A vault
lock is put into the `Locked` state by calling [Complete Vault Lock (POST lockId)](api-CompleteVaultLock.md "api-CompleteVaultLock.md"). You can get
the state of a vault lock by calling [Get Vault Lock (GET lock-policy)](api-GetVaultLock.md "api-GetVaultLock.md"). For more information about the vault locking
process, see [Amazon Glacier Vault Lock](vault-lock.md "vault-lock.md"). For more
information about vault lock policies, see [Vault Lock Policies](vault-lock-policy.md "vault-lock-policy.md").

This operation is idempotent. You can successfully invoke this operation multiple
times, if the vault lock is in the `InProgress` state or if there is no
policy associated with the vault.

## Requests

To delete the vault lock policy, send an HTTP `DELETE` request to the URI
of the vault's `lock-policy` subresource.

### Syntax

```
DELETE /`AccountId`/vaults/`vaultName`/lock-policy HTTP/1.1
Host: glacier.`Region`.amazonaws.com
Date: `Date`
Authorization: `SignatureValue`
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

This operation does not have a request body.

## Responses

If the policy is successfully deleted, Amazon Glacier returns an `HTTP 204 No
 Content` response.

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

The following example demonstrates how to stop the vault locking process.

### Example Request

In this example, a `DELETE` request is sent to the
`lock-policy` subresource of the vault named
`examplevault`.

```
DELETE /-/vaults/examplevault/lock-policy HTTP/1.1
Host: glacier.us-west-2.amazonaws.com
x-amz-Date: 20170210T120000Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20141123/us-west-2/glacier/aws4_request,SignedHeaders=host;x-amz-date;x-amz-glacier-version,Signature=9257c16da6b25a715ce900a5b45b03da0447acf430195dcb540091b12966f2a2
x-amz-glacier-version: 2012-06-01

```

### Example Response

If the policy is successfully deleted Amazon Glacier returns an `HTTP 204 No
 Content` response, as shown in the following example.

```
HTTP/1.1 204 No Content
x-amzn-RequestId: AAABZpJrTyioDC_HsOmHae8EZp_uBSJr6cnGOLKp_XJCl-Q
Date: Wed, 10 Feb 2017 12:00:00 GMT

```

## Related Sections

- [Complete Vault Lock (POST lockId)](api-CompleteVaultLock.md "api-CompleteVaultLock.md")

- [Get Vault Lock (GET lock-policy)](api-GetVaultLock.md "api-GetVaultLock.md")

- [Initiate Vault Lock (POST lock-policy)](api-InitiateVaultLock.md "api-InitiateVaultLock.md")

## See Also

For more information about using this API in one of the language-specific Amazon SDKs,
see the following:

- [AWS Command Line Interface](../../../cli/latest/reference/glacier/abort-vault-lock.md "../../../cli/latest/reference/glacier/abort-vault-lock.md")
