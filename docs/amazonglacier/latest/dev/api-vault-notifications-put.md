**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) will no longer accept new customers starting December 15, 2025, with no impact to existing customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Set Vault Notification Configuration (PUT

notification-configuration)

## Description

Retrieving an archive and a vault inventory are asynchronous operations in Amazon Glacier (Amazon Glacier) for which
you must first initiate a job and wait for the job to complete before you can download
the job output. You can configure a vault to post a message to an Amazon Simple Notification Service (Amazon SNS) topic
when these jobs complete. You can use this operation to set notification configuration on the vault.
For more information,
see [Configuring Vault Notifications in Amazon Glacier](configuring-notifications.md "configuring-notifications.md").

To configure vault notifications, send a PUT request to the
`notification-configuration` subresource of the vault. A notification
configuration is specific to a vault; therefore, it is also referred to as a vault
subresource. The request should include a JSON document that provides an Amazon Simple Notification Service (Amazon SNS) topic and the events for which you want Amazon Glacier to
send notifications to the topic.

You can configure a vault to publish a notification for the following vault events:

- `ArchiveRetrievalCompleted`— This event
  occurs when a job that was initiated for an archive retrieval is completed
  ([Initiate Job (POST jobs)](api-initiate-job-post.md "api-initiate-job-post.md")). The status of the completed
  job can be `Succeeded` or `Failed`. The notification
  sent to the SNS topic is the same output as returned from [Describe Job (GET JobID)](api-describe-job-get.md "api-describe-job-get.md").
- `InventoryRetrievalCompleted`— This event
  occurs when a job that was initiated for an inventory retrieval is completed
  ([Initiate Job (POST jobs)](api-initiate-job-post.md "api-initiate-job-post.md")). The status of the completed
  job can be `Succeeded` or `Failed`. The notification
  sent to the SNS topic is the same output as returned from [Describe Job (GET JobID)](api-describe-job-get.md "api-describe-job-get.md").

Amazon SNS topics must grant permission to the vault to be allowed to publish notifications
to the topic.

## Requests

To set notification configuration on your vault, send a PUT request to the URI of the
vault's `notification-configuration` subresource. You specify the
configuration in the request body. The configuration includes the Amazon SNS topic name
and an array of events that trigger notification to each topic.

### Syntax

```
PUT /`AccountId`/vaults/`VaultName`/notification-configuration HTTP/1.1
Host: glacier.`Region`.amazonaws.com
Date: `Date`
Authorization: `SignatureValue`
x-amz-glacier-version: 2012-06-01

{
   "SNSTopic": `String`,
   "Events":[`String`, ...]
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

The JSON in the request body contains the following fields.

**Events**

An array of one or more events for which you want Amazon Glacier to send
notification.

_Valid Values_: `ArchiveRetrievalCompleted` |
`InventoryRetrievalCompleted`

_Required_: yes

_Type_: Array

**SNSTopic**

The Amazon SNS topic ARN. For more information, go to [Getting Started with Amazon SNS](../../../sns/latest/gsg/Welcome.md "../../../sns/latest/gsg/Welcome.md") in the _Amazon Simple Notification Service Getting Started Guide_.

_Required_: yes

_Type_: String

## Responses

In response, Amazon Glacier (Amazon Glacier) returns `204 No Content` if the notification configuration
is accepted.

### Syntax

```
HTTP/1.1 204 No Content
x-amzn-RequestId: **x-amzn-RequestId**
Date: **Date**
```

### Response Headers

This operation uses only request headers that are common to all operations. For information about common request headers, see
[Common Request Headers](api-common-request-headers.md "api-common-request-headers.md").

### Response Body

This operation does not return a response body.

### Errors

For information about Amazon Glacier
exceptions and error messages, see [Error Responses](api-error-responses.md "api-error-responses.md").

## Examples

The following example demonstrates how to configure vault notification.

### Example Request

The following request sets the `examplevault` notification configuration so that
notifications for two events (`ArchiveRetrievalCompleted` and
`InventoryRetrievalCompleted`
) are sent to the Amazon SNS topic
`arn:aws:sns:us-west-2:012345678901:mytopic`.

```
PUT /-/vaults/examplevault/notification-policy HTTP/1.1
Host: glacier.us-west-2.amazonaws.com
x-amz-Date: 20170210T120000Z
x-amz-glacier-version: 2012-06-01
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20141123/us-west-2/glacier/aws4_request,SignedHeaders=host;x-amz-date;x-amz-glacier-version,Signature=9257c16da6b25a715ce900a5b45b03da0447acf430195dcb540091b12966f2a2

{
   "Events": ["ArchiveRetrievalCompleted", "InventoryRetrievalCompleted"],
   "SNSTopic": "arn:aws:sns:us-west-2:012345678901:mytopic"
}
```

### Example Response

A successful response returns a `204 No Content`.

```
HTTP/1.1 204 No Content
x-amzn-RequestId: AAABZpJrTyioDC_HsOmHae8EZp_uBSJr6cnGOLKp_XJCl-Q
Date: Wed, 10 Feb 2017 12:00:00 GMT
```

## Related Sections

- [Get Vault Notifications (GET
  notification-configuration)](api-vault-notifications-get.md "api-vault-notifications-get.md")
- [Delete Vault Notifications (DELETE
  notification-configuration)](api-vault-notifications-delete.md "api-vault-notifications-delete.md")
- [Identity and Access Management for Amazon Glacier](security-iam.md "security-iam.md")

## See Also

For more information about using this API in one of the language-specific Amazon SDKs,
see the following:

- [AWS Command Line Interface](../../../cli/latest/reference/glacier/set-vault-notifications.md "../../../cli/latest/reference/glacier/set-vault-notifications.md")
