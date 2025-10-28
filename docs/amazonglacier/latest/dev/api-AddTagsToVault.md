**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) will no longer accept new customers starting December 15, 2025, with no impact to existing customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Add Tags To Vault (POST tags add)

This operation adds the specified tags to a vault. Each tag is composed of a key and a
value. Each vault can have up to 50 tags. If your request would cause the tag limit for the
vault to be exceeded, the operation throws the `LimitExceededException`
error.

If a tag already exists on the vault under a specified key, the existing key value will be
overwritten. For more information about tags, see [Tagging Amazon Glacier Resources](tagging.md "tagging.md").

## Request Syntax

To add tags to a vault, send an HTTP POST request to the tags URI as shown in the
following syntax example.

```
POST /`AccountId`/vaults/`vaultName`/tags?operation=add HTTP/1.1
Host: glacier.`Region`.amazonaws.com
Date: `Date`
Authorization: `SignatureValue`
Content-Length: `Length`
x-amz-glacier-version: 2012-06-01

{
   "Tags":
      {
         "`string`": "`string`",
         "`string`": "`string`"
      }
}
```

###### Note

The `AccountId` value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request.
If you specify your account ID, do not include any hyphens ('-') in the ID.

## Request Parameters

| Name            | Description                                                                                                                                                                                    | Required |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `operation=add` | A single query string parameter `operation` with a value of `add` to distinguish it from [Remove Tags From Vault (POST tags remove)](api-RemoveTagsFromVault.md "api-RemoveTagsFromVault.md"). | Yes      | ### Request Headers This operation uses only request headers that are common to all operations. For information about common request headers, see [Common Request Headers](api-common-request-headers.md "api-common-request-headers.md"). ### Request Body The request body contains the following JSON fields. **Tags** The tags to add to the vault. Each tag is composed of a key and a value. The value can be an empty string. _Type:_ String to String map _Length constraints:_ Minimum length of 1. Maximum length 10. _Required:_ Yes ## Responses If the operation request is successful, the service returns an HTTP `204 No Content` response. ### Syntax `HTTP/1.1 204 No Content x-amzn-RequestId: **x-amzn-RequestId** Date: **Date**` ### Response Headers This operation uses only response headers that are common to most responses. For information about common response headers, see [Common Response Headers](api-common-response-headers.md "api-common-response-headers.md"). ### Response Body This operation does not return a response body. ### Errors For information about Amazon Glacier exceptions and error messages, see [Error Responses](api-error-responses.md "api-error-responses.md"). ## Examples ### Example Request The following example sends an HTTP POST request with the tags to add to the vault. ``POST /-/vaults/examplevault/tags?operation=add HTTP/1.1 Host: glacier.us-west-2.amazonaws.com x-amz-Date: 20170210T120000Z Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20141123/us-west-2/glacier/aws4_request,SignedHeaders=host;x-amz-date;x-amz-glacier-version,Signature=9257c16da6b25a715ce900a5b45b03da0447acf430195dcb540091b12966f2a2 Content-Length: `length` x-amz-glacier-version: 2012-06-01 { "Tags": { "examplekey1": "examplevalue1", "examplekey2": "examplevalue2" } }`` ### Example Response If the request was successful Amazon Glacier returns a `HTTP 204 No Content` as shown in the following example. `HTTP/1.1 204 No Content x-amzn-RequestId: AAABZpJrTyioDC_HsOmHae8EZp_uBSJr6cnGOLKp_XJCl-Q Date: Wed, 10 Feb 2017 12:02:00 GMT` ## Related Sections <br>• [List Tags For Vault (GET tags)](api-ListTagsForVault.md "api-ListTagsForVault.md") <br>• [Remove Tags From Vault (POST tags remove)](api-RemoveTagsFromVault.md "api-RemoveTagsFromVault.md") ## See Also For more information about using this API in one of the language-specific Amazon SDKs, see the following: <br>• [AWS Command Line Interface](../../../cli/latest/reference/glacier/add-tags-to-vault.md "../../../cli/latest/reference/glacier/add-tags-to-vault.md") |
