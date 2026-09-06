

 **This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/).

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/).

# Get Vault Notifications (GET notification-configuration)
<a name="api-vault-notifications-get"></a>

## Description
<a name="api-vault-notifications-get-description"></a>

This operation retrieves the `notification-configuration` subresource set on the vault (see [Set Vault Notification Configuration (PUT notification-configuration)](api-vault-notifications-put.md). If notification configuration for a vault is not set, the operation returns a `404 Not Found` error. For more information about vault notifications, see [Configuring Vault Notifications in Amazon Glacier](configuring-notifications.md). 

## Requests
<a name="api-vault-notifications-get-requests"></a>

To retrieve the notification configuration information, send a `GET` request to the URI of a vault's `notification-configuration` subresource.

### Syntax
<a name="api-vault-notifications-get-requests-syntax"></a>

```
1. GET /{{AccountId}}/vaults/{{VaultName}}/notification-configuration HTTP/1.1
2. Host: glacier.{{Region}}.amazonaws.com
3. Date: {{Date}}
4. Authorization: {{SignatureValue}}
5. x-amz-glacier-version: 2012-06-01
```

 

**Note**  
The `AccountId` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.

### Request Parameters
<a name="api-vault-notifications-get-requests-parameters"></a>

This operation does not use request parameters.

### Request Headers
<a name="api-vault-notifications-get-requests-headers"></a>

This operation uses only request headers that are common to all operations. For information about common request headers, see [Common Request Headers](api-common-request-headers.md).

### Request Body
<a name="api-vault-notifications-get-requests-elements"></a>

This operation does not have a request body.

## Responses
<a name="api-vault-notifications-get-responses"></a>

### Syntax
<a name="api-vault-notifications-get-responses-syntax"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: x-amzn-RequestId
Date: Date
Content-Type: application/json
Content-Length: length
{
  "Events": [
    String,
    ...
  ],
  "SNSTopic": String
}
```

### Response Headers
<a name="api-vault-notifications-get-responses-headers"></a>

This operation uses only response headers that are common to most responses. For information about common response headers, see [Common Response Headers](api-common-response-headers.md).

### Response Body
<a name="api-vault-notifications-get-responses-elements"></a>

The response body contains the following JSON fields.

 

**Events**  
A list of one or more events for which Amazon Glacier (Amazon Glacier) will send a notification to the specified Amazon SNS topic. For information about vault events for which you can configure a vault to publish notifications, see [Set Vault Notification Configuration (PUT notification-configuration)](api-vault-notifications-put.md).  
*Type*: Array

**SNSTopic**  
The Amazon Simple Notification Service (Amazon SNS) topic Amazon Resource Name (ARN). For more information, see [Getting Started with Amazon SNS](https://docs.aws.amazon.com/sns/latest/gsg/Welcome.html) in the *Amazon Simple Notification Service Getting Started Guide*.  
*Type*: String

### Errors
<a name="api-vault-notifications-get-responses-errors"></a>

For information about Amazon Glacier exceptions and error messages, see [Error Responses](api-error-responses.md).

## Examples
<a name="api-vault-notifications-get-examples"></a>

The following example demonstrates how to retrieve the notification configuration for a vault.

### Example Request
<a name="api-vault-notifications-get-example-request"></a>

In this example, a `GET` request is sent to the `notification-configuration` subresource of a vault.

```
1. GET /-/vaults/examplevault/notification-configuration HTTP/1.1
2. Host: glacier.us-west-2.amazonaws.com
3. x-amz-Date: 20170210T120000Z
4. x-amz-glacier-version: 2012-06-01
5. Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20141123/us-west-2/glacier/aws4_request,SignedHeaders=host;x-amz-date;x-amz-glacier-version,Signature=9257c16da6b25a715ce900a5b45b03da0447acf430195dcb540091b12966f2a2
```

### Example Response
<a name="api-vault-notifications-get-example-response"></a>

A successful response shows the audit logging configuration document in the body of the response in JSON format. In this example, the configuration shows that notifications for two events (`ArchiveRetrievalCompleted` and `InventoryRetrievalCompleted`) are sent to the Amazon SNS topic `arn:aws:sns:us-west-2:012345678901:mytopic`.

```
 1. HTTP/1.1 200 OK
 2. x-amzn-RequestId: AAABZpJrTyioDC_HsOmHae8EZp_uBSJr6cnGOLKp_XJCl-Q
 3. Date: Wed, 10 Feb 2017 12:00:00 GMT
 4. Content-Type: application/json
 5. Content-Length: 150
 6.   
 7. {
 8.   "Events": [
 9.     "ArchiveRetrievalCompleted",
10.     "InventoryRetrievalCompleted"
11.   ],
12.   "SNSTopic": "arn:aws:sns:us-west-2:012345678901:mytopic"
13. }
```

## Related Sections
<a name="related-sections-vault-notifications-get"></a>

 
+ [Delete Vault Notifications (DELETE notification-configuration)](api-vault-notifications-delete.md)
+ [Set Vault Notification Configuration (PUT notification-configuration)](api-vault-notifications-put.md)
+ [Identity and Access Management for Amazon Glacier](security-iam.md)

## See Also
<a name="api-vault-notifications-get_SeeAlso"></a>

For more information about using this API in one of the language-specific Amazon SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/reference/glacier/get-vault-notifications.html) 