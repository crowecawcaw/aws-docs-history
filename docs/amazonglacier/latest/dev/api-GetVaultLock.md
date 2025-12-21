**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Get Vault Lock (GET lock-policy)

## Description

This operation retrieves the following attributes from the `lock-policy`
subresource set on the specified vault:

- The vault lock policy set on the vault.
- The state of the vault lock, which is either `InProgess` or
  `Locked`.
- When the lock ID expires. The lock ID is used to complete the vault locking
  process.
- When the vault lock was initiated and put into the `InProgress`
  state.

A vault lock is put into the `InProgress` state by calling [Initiate Vault Lock (POST lock-policy)](api-InitiateVaultLock.md "api-InitiateVaultLock.md"). A vault
lock is put into the `Locked` state by calling [Complete Vault Lock (POST lockId)](api-CompleteVaultLock.md "api-CompleteVaultLock.md"). You can
stop the vault locking process by calling [Abort Vault Lock (DELETE lock-policy)](api-AbortVaultLock.md "api-AbortVaultLock.md"). For more information about the vault locking
process, see [Amazon Glacier Vault Lock](vault-lock.md "vault-lock.md").

If there is no vault lock policy set on the vault, the operation returns a `404
 Not found` error. For more information about vault lock policies, see [Vault Lock Policies](vault-lock-policy.md "vault-lock-policy.md").

## Requests

To return the current vault lock policy and other attributes, send an HTTP `GET`
request to the URI of the vault's `lock-policy` subresource as shown in the
following syntax example.

### Syntax

```
GET /`AccountId`/vaults/`vaultName`/lock-policy HTTP/1.1
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

### Request Headers

This operation uses only request headers that are common to all operations. For information about common request headers, see
[Common Request Headers](api-common-request-headers.md "api-common-request-headers.md").

### Request Body

This operation does not have a request body.

## Responses

In response, Amazon Glacier (Amazon Glacier) returns the vault access policy in JSON format in the body of the
response.

### Syntax

```
HTTP/1.1 200 OK
x-amzn-RequestId: **x-amzn-RequestId**
Date: **Date**
Content-Type: application/json
Content-Length: ***length***

{
  "Policy": "***string***",
  "State": "***string***",
  "ExpirationDate": "***string***",
  "CreationDate":"***string***"
}
```

### Response Headers

This operation uses only response headers that are common to most responses. For information about common response headers, see
[Common Response Headers](api-common-response-headers.md "api-common-response-headers.md").

### Response Body

The response body contains the following JSON fields.

**Policy**

The vault lock policy as a JSON string, which uses "\" as an escape character.

Type: String

**State**

The state of the vault lock.

Type: String

Valid values: `InProgress``|`Locked``

**ExpirationDate**

The UTC date and time at which the lock ID expires. This value can be `null`
if the vault lock is in a `Locked` state.

_Type_: A string representation in the ISO 8601 date format, for example `2013-03-20T17:03:43.221Z`.

**CreationDate**

The UTC date and time at which the vault lock was put into the `InProgress`
state.

_Type_: A string representation in the ISO 8601 date format, for example `2013-03-20T17:03:43.221Z`.

### Errors

For information about Amazon Glacier
exceptions and error messages, see [Error Responses](api-error-responses.md "api-error-responses.md").

## Examples

The following example demonstrates how to get a vault lock policy.

### Example Request

In this example, a `GET` request is sent to the URI of a vault's `lock-policy` subresource.

```
GET /-/vaults/examplevault/lock-policy HTTP/1.1
Host: glacier.us-west-2.amazonaws.com
x-amz-Date: 20170210T120000Z
x-amz-glacier-version: 2012-06-01
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20141123/us-west-2/glacier/aws4_request,SignedHeaders=host;x-amz-date;x-amz-glacier-version,Signature=9257c16da6b25a715ce900a5b45b03da0447acf430195dcb540091b12966f2a2
```

### Example Response

If the request was successful, Amazon Glacier returns the vault access policy as a JSON string in the
body of the response. The returned JSON string uses "\" as an escape character, as
shown in the [Initiate Vault Lock (POST lock-policy)](api-InitiateVaultLock.md "api-InitiateVaultLock.md")
example request. However, the following
example shows the returned JSON string without escape characters for readability.

```
HTTP/1.1 200 OK
x-amzn-RequestId: AAABZpJrTyioDC_HsOmHae8EZp_uBSJr6cnGOLKp_XJCl-Q
Date: Wed, 10 Feb 2017 12:00:00 GMT
Content-Type: application/json
Content-Length: length

{
  "Policy": "
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Sid": "Define-vault-lock",
          "Principal": {
            "AWS": "arn:aws:iam::999999999999:root"
          },
          "Effect": "Deny",
          "Action": "glacier:DeleteArchive",
          "Resource": [
            "arn:aws:glacier:us-west-2:999999999999:vaults/examplevault"
          ],
          "Condition": {
            "NumericLessThanEquals": {
              "glacier:ArchiveAgeInDays": "365"
            }
          }
        }
      ]
    }
  ",
  "State": "InProgress",
  "ExpirationDate": "exampledate",
  "CreationDate": "exampledate"
}
```

## Related Sections

- [Abort Vault Lock (DELETE lock-policy)](api-AbortVaultLock.md "api-AbortVaultLock.md")

- [Complete Vault Lock (POST lockId)](api-CompleteVaultLock.md "api-CompleteVaultLock.md")

- [Initiate Vault Lock (POST lock-policy)](api-InitiateVaultLock.md "api-InitiateVaultLock.md")

## See Also

For more information about using this API in one of the language-specific Amazon SDKs,
see the following:

- [AWS Command Line Interface](../../../cli/latest/reference/glacier/get-vault-lock.md "../../../cli/latest/reference/glacier/get-vault-lock.md")
