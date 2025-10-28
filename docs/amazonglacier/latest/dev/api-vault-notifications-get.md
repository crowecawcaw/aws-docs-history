**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) will no longer accept new customers starting December 15, 2025, with no impact to existing customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Get Vault Notifications (GET

notification-configuration)

## Description

This operation retrieves the `notification-configuration` subresource set on the
vault (see [Set Vault Notification Configuration (PUT
notification-configuration)](api-vault-notifications-put.md "api-vault-notifications-put.md"). If notification configuration for a
vault is not set, the operation returns a `404 Not Found` error. For more
information about vault notifications, see [Configuring Vault Notifications in Amazon Glacier](configuring-notifications.md "configuring-notifications.md").

## Requests

To retrieve the notification configuration information, send a `GET` request to
the URI of a vault's `notification-configuration` subresource.

### Syntax

```
GET /`AccountId`/vaults/`VaultName`/notification-configuration HTTP/1.1
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
Content-Length: ***length***
{
  "Events": [
    ***String***,
    ...
  ],
  "SNSTopic": ***String***
}
```

### Response Headers

This operation uses only response headers that are common to most responses. For information about common response headers, see
[Common Response Headers](api-common-response-headers.md "api-common-response-headers.md").

### Response Body

The response body contains the following JSON fields.

**Events**

A list of one or more events for which Amazon Glacier (Amazon Glacier) will send a notification to the
specified Amazon SNS topic. For information about vault events for
which you can configure a vault to publish notifications, see [Set Vault Notification Configuration (PUT
notification-configuration)](api-vault-notifications-put.md "api-vault-notifications-put.md").

_Type_: Array

**SNSTopic**

The Amazon Simple Notification Service (Amazon SNS) topic Amazon Resource Name (ARN).
For more information, see [Getting Started with Amazon SNS](../../../sns/latest/gsg/Welcome.md "../../../sns/latest/gsg/Welcome.md") in the _Amazon Simple Notification Service Getting Started Guide_.

_Type_: String

### Errors

For information about Amazon Glacier
exceptions and error messages, see [Error Responses](api-error-responses.md "api-error-responses.md").

## Examples

The following example demonstrates how to retrieve the notification configuration for a
vault.

### Example Request

In this example, a `GET` request is sent to the
`notification-configuration` subresource of a vault.

```
GET /-/vaults/examplevault/notification-configuration HTTP/1.1
Host: glacier.us-west-2.amazonaws.com
x-amz-Date: 20170210T120000Z
x-amz-glacier-version: 2012-06-01
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20141123/us-west-2/glacier/aws4_request,SignedHeaders=host;x-amz-date;x-amz-glacier-version,Signature=9257c16da6b25a715ce900a5b45b03da0447acf430195dcb540091b12966f2a2
```

### Example Response

A successful response shows the audit logging configuration document in the body of the
response in JSON format. In this example, the configuration shows that notifications
for two events (`ArchiveRetrievalCompleted` and
`InventoryRetrievalCompleted`) are sent to the Amazon SNS topic
`arn:aws:sns:us-west-2:012345678901:mytopic`.

```
HTTP/1.1 200 OK
x-amzn-RequestId: AAABZpJrTyioDC_HsOmHae8EZp_uBSJr6cnGOLKp_XJCl-Q
Date: Wed, 10 Feb 2017 12:00:00 GMT
Content-Type: application/json
Content-Length: 150

{
  "Events": [
    "ArchiveRetrievalCompleted",
    "InventoryRetrievalCompleted"
  ],
  "SNSTopic": "arn:aws:sns:us-west-2:012345678901:mytopic"
}
```

## Related Sections

- [Delete Vault Notifications (DELETE
  notification-configuration)](api-vault-notifications-delete.md "api-vault-notifications-delete.md")
- [Set Vault Notification Configuration (PUT
  notification-configuration)](api-vault-notifications-put.md "api-vault-notifications-put.md")
- [Identity and Access Management for Amazon Glacier](security-iam.md "security-iam.md")

## See Also

For more information about using this API in one of the language-specific Amazon SDKs,
see the following:

- [AWS Command Line Interface](../../../cli/latest/reference/glacier/get-vault-notifications.md "../../../cli/latest/reference/glacier/get-vault-notifications.md")
