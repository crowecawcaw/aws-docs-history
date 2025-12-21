**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# List Vaults (GET vaults)

## Description

This operation lists all vaults owned by the calling user’s account. The list returned in
the response is ASCII-sorted by vault name.

By default, this operation returns up to 10 items per request. If there are more vaults to
list, the `marker` field in the response body contains the vault Amazon
Resource Name (ARN) at which to continue the list with a new List Vaults request;
otherwise, the `marker` field is `null`. In your next List Vaults
request you set the `marker` parameter to the value Amazon Glacier (Amazon Glacier) returned in the
responses to your previous List Vaults request. You can also limit the number of vaults
returned in the response by specifying the `limit` parameter in the request.

## Requests

To get a list of vaults, you send a `GET` request to the
_vaults_ resource.

### Syntax

```
GET /`AccountId`/vaults HTTP/1.1
Host: glacier.`Region`.amazonaws.com
Date: `Date`
Authorization: `SignatureValue`
x-amz-glacier-version: 2012-06-01
```

###### Note

The `AccountId` value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request.
If you specify your account ID, do not include any hyphens ('-') in the ID.

### Request Parameters

This operation uses the following request parameters.

| Name     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Required |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `limit`  | The maximum number of vaults to be returned. The default limit is 10. The number of<br>vaults returned might be fewer than the specified limit, but the<br>number of returned vaults never exceeds the limit.<br>Type: String<br>Constraints: Minimum integer value of 1. Maximum integer value of 10.                                                                                                                                                                                                                                                     | No       |
| `marker` | A string used for pagination. `marker` specifies the vault ARN after which<br>the listing of vaults should begin. (The vault specified by<br>`marker` is not included in the returned<br>list.) Get the `marker` value from a previous<br>List Vaults response. You need to include the<br>`marker` only if you are continuing the<br>pagination of results started in a previous List Vaults<br>request. Specifying an empty value ("") for the marker<br>returns a list of vaults starting from the first<br>vault.<br>Type: String<br>Constraints: None | No       |

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
  "Marker": ***String***
  "VaultList": [
   {
    "CreationDate": ***String***,
    "LastInventoryDate": ***String***,
    "NumberOfArchives": ***Number***,
    "SizeInBytes": ***Number***,
    "VaultARN": ***String***,
    "VaultName": ***String***
   },
   ...
  ]
}
```

### Response Headers

This operation uses only response headers that are common to most responses. For information about common response headers, see
[Common Response Headers](api-common-response-headers.md "api-common-response-headers.md").

### Response Body

The response body contains the following JSON fields.

**CreationDate**

The date the vault was created, in Coordinated Universal Time (UTC).

_Type_: String. A string representation in the ISO 8601 date format, for example `2013-03-20T17:03:43.221Z`.

**LastInventoryDate**

The date of the last vault inventory, in Coordinated Universal Time (UTC). This field
can be null if an inventory has not yet run on the vault, for
example, if you just created the vault. For information about
initiating an inventory for a vault, see [Initiate Job (POST jobs)](api-initiate-job-post.md "api-initiate-job-post.md").

_Type_: A string representation in the ISO 8601 date format, for example `2013-03-20T17:03:43.221Z`.

**Marker**

The `vaultARN` that represents where to continue pagination of the results.
You use the `marker` in another List Vaults request to
obtain more vaults in the list. If there are no more vaults, this
value is `null`.

_Type_: String

**NumberOfArchives**

The number of archives in the vault as of the last inventory date.

_Type_: Number

**SizeInBytes**

The total size, in bytes, of all the archives in the vault including any per-archive
overhead, as of the last inventory date.

_Type_: Number

**VaultARN**

The Amazon Resource Name (ARN) of the vault.

_Type_: String

**VaultList**

An array of objects, with each object providing a description of a vault.

_Type_: Array

**VaultName**

The vault name.

_Type_: String

### Errors

For information about Amazon Glacier
exceptions and error messages, see [Error Responses](api-error-responses.md "api-error-responses.md").

## Examples

### Example: List All Vaults

The following example lists vaults. Because the `marker` and `limit`
parameters are not specified in the request, up to 10 vaults are returned.

#### Example Request

```
GET /-/vaults HTTP/1.1
Host: glacier.us-west-2.amazonaws.com
x-amz-Date: 20170210T120000Z
x-amz-glacier-version: 2012-06-01
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20141123/us-west-2/glacier/aws4_request,SignedHeaders=host;x-amz-date;x-amz-glacier-version,Signature=9257c16da6b25a715ce900a5b45b03da0447acf430195dcb540091b12966f2a2
```

#### Example Response

The `Marker` is `null` indicating there are no more vaults to
list.

```
HTTP/1.1 200 OK
x-amzn-RequestId: AAABZpJrTyioDC_HsOmHae8EZp_uBSJr6cnGOLKp_XJCl-Q
Date: Wed, 10 Feb 2017 12:02:00 GMT
Content-Type: application/json
Content-Length: 497

{
  "Marker": null,
  "VaultList": [
   {
    "CreationDate": "2012-03-16T22:22:47.214Z",
    "LastInventoryDate": "2012-03-21T22:06:51.218Z",
    "NumberOfArchives": 2,
    "SizeInBytes": 12334,
    "VaultARN": "arn:aws:glacier:us-west-2:012345678901:vaults/examplevault1",
    "VaultName": "examplevault1"
   },
   {
    "CreationDate": "2012-03-19T22:06:51.218Z",
    "LastInventoryDate": "2012-03-21T22:06:51.218Z",
    "NumberOfArchives": 0,
    "SizeInBytes": 0,
    "VaultARN": "arn:aws:glacier:us-west-2:012345678901:vaults/examplevault2",
    "VaultName": "examplevault2"
   },
   {
    "CreationDate": "2012-03-19T22:06:51.218Z",
    "LastInventoryDate": "2012-03-25T12:14:31.121Z",
    "NumberOfArchives": 0,
    "SizeInBytes": 0,
    "VaultARN": "arn:aws:glacier:us-west-2:012345678901:vaults/examplevault3",
    "VaultName": "examplevault3"
   }
  ]
}
```

### Example: Partial List of Vaults

The following example returns two vaults starting at the vault specified by the
`marker`.

#### Example Request

```
GET /-/vaults?limit=2&marker=arn:aws:glacier:us-west-2:012345678901:vaults/examplevault1 HTTP/1.1
Host: glacier.us-west-2.amazonaws.com
x-amz-Date: 20170210T120000Z
x-amz-glacier-version: 2012-06-01
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20141123/us-west-2/glacier/aws4_request,SignedHeaders=host;x-amz-date;x-amz-glacier-version,Signature=9257c16da6b25a715ce900a5b45b03da0447acf430195dcb540091b12966f2a2
```

#### Example Response

Two vaults are returned in the list. The `Marker` contains the
vault ARN to continue pagination in another List Vaults request.

```
HTTP/1.1 200 OK
x-amzn-RequestId: AAABZpJrTyioDC_HsOmHae8EZp_uBSJr6cnGOLKp_XJCl-Q
Date: Wed, 10 Feb 2017 12:02:00 GMT
Content-Type: application/json
Content-Length: 497

{
  "Marker": "arn:aws:glacier:us-west-2:012345678901:vaults/examplevault3",
  "VaultList": [
   {
    "CreationDate": "2012-03-16T22:22:47.214Z",
    "LastInventoryDate": "2012-03-21T22:06:51.218Z",
    "NumberOfArchives": 2,
    "SizeInBytes": 12334,
    "VaultARN": "arn:aws:glacier:us-west-2:012345678901:vaults/examplevault1",
    "VaultName": "examplevault1"
   },
   {
    "CreationDate": "2012-03-19T22:06:51.218Z",
    "LastInventoryDate": "2012-03-21T22:06:51.218Z",
    "NumberOfArchives": 0,
    "SizeInBytes": 0,
    "VaultARN": "arn:aws:glacier:us-west-2:012345678901:vaults/examplevault2",
    "VaultName": "examplevault2"
   }
  ]
}
```

## Related Sections

- [Create Vault (PUT vault)](api-vault-put.md "api-vault-put.md")
- [Delete Vault (DELETE vault)](api-vault-delete.md "api-vault-delete.md")
- [Initiate Job (POST jobs)](api-initiate-job-post.md "api-initiate-job-post.md")
- [Identity and Access Management for Amazon Glacier](security-iam.md "security-iam.md")

## See Also

For more information about using this API in one of the language-specific Amazon SDKs,
see the following:

- [AWS Command Line Interface](../../../cli/latest/reference/glacier/list-vaults.md "../../../cli/latest/reference/glacier/list-vaults.md")
