**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) will no longer accept new customers starting December 15, 2025, with no impact to existing customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Get Data Retrieval Policy (GET policy)

## Description

This operation returns the current data retrieval policy for the AWS account and AWS Region specified in the
`GET` request. For more information about data retrieval policies, see
[Amazon Glacier Data Retrieval Policies](data-retrieval-policy.md "data-retrieval-policy.md").

## Requests

To return the current data retrieval policy, send an HTTP `GET` request to the data retrieval
policy URI as shown in the following syntax example.

### Syntax

```
GET /`AccountId`/policies/data-retrieval HTTP/1.1
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

### Syntax

```
HTTP/1.1 200 OK
x-amzn-RequestId: **x-amzn-RequestId**
Date: **Date**
Content-Type: application/json
Content-Length: ***length***
{
  "Policy":
    {
      "Rules":[
         {
            "BytesPerHour": ***Number***,
            "Strategy": ***String***
         }
       ]
    }
}
```

### Response Headers

This operation uses only response headers that are common to most responses. For information about common response headers, see
[Common Response Headers](api-common-response-headers.md "api-common-response-headers.md").

### Response Body

The response body contains the following JSON fields.

**BytesPerHour**

The maximum number of bytes that can be retrieved in an hour.

This field will be present only if the value of the **Strategy** field is `BytesPerHour`.

_Type_: Number

**Rules**

The policy rule. Although this is a list type, currently there will be only one rule, which contains a
Strategy field and optionally a BytesPerHour field.

_Type_: Array

**Strategy**

The type of data retrieval policy.

_Type_: String

Valid values: `BytesPerHour`|`FreeTier`|`None`.
`BytesPerHour` is equivalent to selecting **Max Retrieval
Rate** in the console. `FreeTier` is equivalent to selecting
**Free Tier Only** in the console. `None` is equivalent
to selecting **No Retrieval Policy** in the console. For more
information about selecting data retrieval policies in the console, see
[Amazon Glacier Data Retrieval Policies](data-retrieval-policy.md "data-retrieval-policy.md").

### Errors

For information about Amazon Glacier
exceptions and error messages, see [Error Responses](api-error-responses.md "api-error-responses.md").

## Examples

The following example demonstrates how to get a data retrieval policy.

### Example Request

In this example, a `GET` request is sent to the URI of a policy's location.

```
GET /-/policies/data-retrieval HTTP/1.1
Host: glacier.us-west-2.amazonaws.com
x-amz-Date: 20170210T120000Z
x-amz-glacier-version: 2012-06-01
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20141123/us-west-2/glacier/aws4_request,SignedHeaders=host;x-amz-date;x-amz-glacier-version,Signature=9257c16da6b25a715ce900a5b45b03da0447acf430195dcb540091b12966f2a2
```

### Example Response

A successful response shows the data retrieval policy in the body of the response in JSON format.

```
HTTP/1.1 200 OK
x-amzn-RequestId: AAABZpJrTyioDC_HsOmHae8EZp_uBSJr6cnGOLKp_XJCl-Q
Date: Wed, 10 Feb 2017 12:00:00 GMT
Content-Type: application/json
Content-Length: 85

{
  "Policy":
    {
      "Rules":[
         {
           "BytesPerHour":10737418240,
           "Strategy":"BytesPerHour"
          }
       ]
    }
}
```

## Related Sections

- [Set Data Retrieval Policy (PUT policy)](api-SetDataRetrievalPolicy.md "api-SetDataRetrievalPolicy.md")

- [Initiate Job (POST jobs)](api-initiate-job-post.md "api-initiate-job-post.md")
