**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Set Vault Access Policy (PUT access-policy)

## Description

This operation configures an access policy for a vault and will overwrite an existing
policy. To configure a vault access policy, send a `PUT` request to the
`access-policy` subresource of the vault. You can set one access policy per vault
and the policy can be up to 20 KB in size. For more information about vault access
policies, see [Vault Access Policies](vault-access-policy.md "vault-access-policy.md").

## Requests

### Syntax

To set a vault access policy, send an HTTP `PUT` request to the URI of
the vault's `access-policy` subresource as shown in the following syntax
example.

```
PUT /`AccountId`/vaults/`vaultName`/access-policy HTTP/1.1
Host: glacier.`Region`.amazonaws.com
Date: `Date`
Authorization: `SignatureValue`
Content-Length: `Length`
x-amz-glacier-version: 2012-06-01

{
  "Policy": "***string***"
}
```

###### Note

The `AccountId` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.

### Request Parameters

This operation does not use request parameters.

### Request Headers

This operation uses only request headers that are common to all operations. For information about common request headers, see
[Common Request Headers](api-common-request-headers.md "api-common-request-headers.md").

### Request Body

The request body contains the following JSON fields.

**Policy**

The vault access policy as a JSON string, which uses "\" as an escape character.

Type: String

Required: Yes

## Responses

In response, Amazon Glacier returns `204 No Content` if the policy is
accepted.

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

The following example sends an HTTP `PUT` request to the URI of the vault's
`access-policy` subresource. The `Policy` JSON string uses
"\" as an escape character.

```
PUT /-/vaults/examplevault/access-policy HTTP/1.1
Host: glacier.us-west-2.amazonaws.com
x-amz-Date: 20170210T120000Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20141123/us-west-2/glacier/aws4_request,SignedHeaders=host;x-amz-date;x-amz-glacier-version,Signature=9257c16da6b25a715ce900a5b45b03da0447acf430195dcb540091b12966f2a2
Content-Length: length
x-amz-glacier-version: 2012-06-01

{"Policy":"{\"Version\":\"2012-10-17\",		 	 	 \"Statement\":[{\"Sid\":\"Define-owner-access-rights\",\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::999999999999:root\"},\"Action\":\"glacier:DeleteArchive\",\"Resource\":\"arn:aws:glacier:us-west-2:999999999999:vaults/examplevault\"}]}"}

```

### Example Response

If the request was successful, Amazon Glacier (Amazon Glacier) returns a `HTTP 204 No Content` as
shown in the following example.

```
HTTP/1.1 204 No Content
x-amzn-RequestId: AAABZpJrTyioDC_HsOmHae8EZp_uBSJr6cnGOLKp_XJCl-Q
Date: Wed, 10 Feb 2017 12:02:00 GMT
```

## Related Sections

- [Delete Vault Access Policy (DELETE access-policy)](api-DeleteVaultAccessPolicy.md "api-DeleteVaultAccessPolicy.md")

- [Get Vault Access Policy (GET access-policy)](api-GetVaultAccessPolicy.md "api-GetVaultAccessPolicy.md")

## See Also

For more information about using this API in one of the language-specific Amazon SDKs,
see the following:

- [AWS Command Line Interface](../../../cli/latest/reference/glacier/set-vault-access-policy.md "../../../cli/latest/reference/glacier/set-vault-access-policy.md")
