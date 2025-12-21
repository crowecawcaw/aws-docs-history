**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# List Provisioned Capacity (GET

provisioned-capacity)

This operation lists the provisioned capacity units for the specified AWS account. For
more information about provisioned capacity, see [Archive
Retrieval Options](downloading-an-archive-two-steps.md#api-downloading-an-archive-two-steps-retrieval-options "downloading-an-archive-two-steps.md#api-downloading-an-archive-two-steps-retrieval-options").

A provisioned capacity unit lasts for one month starting at the date and time of purchase,
which is the start date. The unit expires on the expiration date, which is exactly one month
after the start date to the nearest second.

If the start date is on the 31st day of a month, the expiration date is the last day of
the next month. For example, if the start date is August 31, the expiration date is
September 30. If the start date is January 31, the expiration date is February 28. You can
see this functionality in the [Example
Response](#api-ListProvisionedCapacity-example1-response "#api-ListProvisionedCapacity-example1-response").

## Request Syntax

To list the provisioned retrieval capacity for an account, send an HTTP GET request to
the provisioned-capacity URI as shown in the following syntax example.

```
GET /`AccountId`/provisioned-capacity HTTP/1.1
Host: glacier.`Region`.amazonaws.com
Date: `Date`
Authorization: `SignatureValue`
x-amz-glacier-version: 2012-06-01

```

###### Note

The `AccountId` value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request.
If you specify your account ID, do not include any hyphens ('-') in the ID.

## Request

Parameters

This operation does not use request parameters.

## Request Headers

This operation uses only request headers that are common to all operations. For information about common request headers, see
[Common Request Headers](api-common-request-headers.md "api-common-request-headers.md").

## Request Body

This operation does not have a request body.

## Responses

If the operation is successful, the service sends back an HTTP `200 OK`
response.

### Response Syntax

```
HTTP/1.1 200 OK
x-amzn-RequestId: **x-amzn-RequestId**
Date: **Date**
Content-Type: application/json
Content-Length: ***Length***
{
   "ProvisionedCapacityList":
      {
         "**CapacityId**" : "**string**",
         "**StartDate**" : "**string**"
         "**ExpirationDate**" : "**string**"
      }
}
```

### Response Headers

This operation uses only response headers that are common to most responses. For information about common response headers, see
[Common Response Headers](api-common-response-headers.md "api-common-response-headers.md").

### Response Body

The response body contains the following JSON fields.

**CapacityId**

The ID that identifies the provisioned capacity unit.

_Type_: String.

**StartDate**

The date that the provisioned capacity unit was purchased, in
Coordinated Universal Time (UTC).

_Type_: String. A string representation in the ISO 8601 date format, for example `2013-03-20T17:03:43.221Z`.

**ExpirationDate**

The date that the provisioned capacity unit expires, in Coordinated
Universal Time (UTC).

_Type_: String. A string representation in the ISO 8601 date format, for example `2013-03-20T17:03:43.221Z`.

### Errors

For information about Amazon Glacier
exceptions and error messages, see [Error Responses](api-error-responses.md "api-error-responses.md").

## Examples

The following example lists the provisioned capacity units for an account.

### Example

Request

In this example, a GET request is sent to retrieve a list of the provisioned
capacity units for the specified account.

```
GET /123456789012/priority-capacity HTTP/1.1
Host: glacier.us-west-2.amazonaws.com
x-amz-Date: 20170210T120000Z
x-amz-glacier-version: 2012-06-01
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20141123/us-west-2/glacier/aws4_request,SignedHeaders=host;x-amz-date;x-amz-glacier-version,Signature=9257c16da6b25a715ce900a5b45b03da0447acf430195dcb540091b12966f2a2
```

### Example

Response

If the request was successful, Amazon Glacier (Amazon Glacier) returns a `HTTP 200 OK` with a list
of provisioned capacity units for the account as shown in the following
example.

The provisioned capacity unit listed first is an example of a unit with a start
date of January 31, 2017 and expiration date of February 28, 2017. As stated
earlier, if the start date is on the 31st day of a month, the expiration date is the
last day of the next month.

```
HTTP/1.1 200 OK
x-amzn-RequestId: AAABZpJrTyioDC_HsOmHae8EZp_uBSJr6cnGOLKp_XJCl-Q
Date: Wed, 10 Feb 2017 12:02:00 GMT
Content-Type: application/json
Content-Length: *length*

{
   "ProvisionedCapacityList",
      {
         "CapacityId": "zSaq7NzHFQDANTfQkDen4V7z",
         "StartDate": "2017-01-31T14:26:33.031Z",
         "ExpirationDate": "2017-02-28T14:26:33.000Z",
      },
      {
         "CapacityId": "yXaq7NzHFQNADTfQkDen4V7z",
         "StartDate": "2016-12-13T20:11:51.095Z"",
         "ExpirationDate": "2017-01-13T20:11:51.000Z" ",
      },
      ...
}
```

## Related Sections

- [Purchase Provisioned Capacity (POST
  provisioned-capacity)](api-PurchaseProvisionedCapacity.md "api-PurchaseProvisionedCapacity.md")
