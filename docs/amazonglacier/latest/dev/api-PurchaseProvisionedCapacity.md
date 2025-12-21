**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Purchase Provisioned Capacity (POST

provisioned-capacity)

This operation purchases a provisioned capacity unit for an AWS account.

A provisioned capacity unit lasts for one month starting at the date and time of purchase,
which is the start date. The unit expires on the expiration date, which is exactly one month
after the start date to the nearest second.

If the start date is on the 31st day of a month, the expiration date is the last day of the
next month. For example, if the start date is August 31, the expiration date is September 30.
If the start date is January 31, the expiration date is February 28.

Provisioned capacity helps ensure that your retrieval capacity for expedited retrievals is
available when you need it. Each unit of capacity ensures that at least three expedited
retrievals can be performed every five minutes and provides up to 150 MB/s of retrieval
throughput. For more information about provisioned capacity, see [Archive
Retrieval Options](downloading-an-archive-two-steps.md#api-downloading-an-archive-two-steps-retrieval-options "downloading-an-archive-two-steps.md#api-downloading-an-archive-two-steps-retrieval-options").

###### Note

There is a limit of two provisioned capacity units per AWS account.

## Requests

To purchase provisioned capacity unit for an AWS account send an HTTP `POST`
request to the provisioned-capacity URI.

### Syntax

```
POST /`AccountId`/provisioned-capacity HTTP/1.1
Host: glacier.`Region`.amazonaws.com
Date: `Date`
Authorization: `SignatureValue`
Content-Length: `Length`
x-amz-glacier-version: 2012-06-01

```

###### Note

The `AccountId` value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request.
If you specify your account ID, do not include any hyphens ('-') in the ID.

### Request

Parameters

#### Request

Headers

This operation uses only request headers that are common to all operations. For information about common request headers, see
[Common Request Headers](api-common-request-headers.md "api-common-request-headers.md").

#### Request

Body

This operation does not have a request body.

## Responses

If the operation request is successful, the service returns an HTTP `201
 Created` response.

### Syntax

```
HTTP/1.1 201 Created
x-amzn-RequestId: **x-amzn-RequestId**
Date: **Date**
x-amz-capacity-id: `CapacityId`
```

### Response

Headers

A successful response includes the following response headers, in addition to the response headers that are common to all operations. For more information about common response headers, see
[Common Response Headers](api-common-response-headers.md "api-common-response-headers.md").

| Name                | Description                                                           |
| ------------------- | --------------------------------------------------------------------- |
| `x-amz-capacity-id` | The ID that identifies the provisioned capacity unit.<br>Type: String |

### Response

Body

This operation does not return a response body.

### Errors

This operation includes the following error or errors, in addition to the possible errors common to all Amazon Glacier operations. For information about Amazon Glacier
errors and a list of error codes, see [Error Responses](api-error-responses.md "api-error-responses.md").

| Code                     | Description                                                                                      | HTTP Status Code  | Type   |
| ------------------------ | ------------------------------------------------------------------------------------------------ | ----------------- | ------ |
| `LimitExceededException` | Returned if the given request would exceed the account's limit of<br>provisioned capacity units. | `400 Bad Request` | Client |

## Examples

The following example purchases provisioned capacity for an account.

### Example

Request

The following example sends an HTTP POST request to purchase a provisioned capacity
unit.

```
POST /123456789012/provisioned-capacity HTTP/1.1
Host: glacier.us-west-2.amazonaws.com
x-amz-Date: 20170210T120000Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20141123/us-west-2/glacier/aws4_request,SignedHeaders=host;x-amz-date;x-amz-glacier-version,Signature=9257c16da6b25a715ce900a5b45b03da0447acf430195dcb540091b12966f2a2
Content-Length: `length`
x-amz-glacier-version: 2012-06-01

```

### Example

Response

If the request was successful, Amazon Glacier (Amazon Glacier) returns an `HTTP 201 Created`
response, as shown in the following example.

```
HTTP/1.1 201 Created
x-amzn-RequestId: AAABZpJrTyioDC_HsOmHae8EZp_uBSJr6cnGOLKp_XJCl-Q
Date: Wed, 10 Feb 2017 12:02:00 GMT
x-amz-capacity-id: zSaq7NzHFQDANTfQkDen4V7z
```

## Related Sections

- [List Provisioned Capacity (GET
  provisioned-capacity)](api-ListProvisionedCapacity.md "api-ListProvisionedCapacity.md")
