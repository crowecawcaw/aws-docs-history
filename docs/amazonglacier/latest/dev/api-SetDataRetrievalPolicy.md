**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) will no longer accept new customers starting December 15, 2025, with no impact to existing customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Set Data Retrieval Policy (PUT policy)

## Description

This operation sets and then enacts a data retrieval policy in the AWS Region specified in the `PUT` request. You can set one
policy per AWS Region for an AWS account. The policy is enacted within a few minutes of a
successful `PUT` operation.

The set policy operation does not affect retrieval jobs that were in progress before the policy was
enacted. For more information about data retrieval policies, see [Amazon Glacier Data Retrieval Policies](data-retrieval-policy.md "data-retrieval-policy.md").

## Requests

### Syntax

To set a data retrieval policy, send an HTTP PUT request to the data retrieval policy URI as shown in
the following syntax example.

```
PUT /`AccountId`/policies/data-retrieval HTTP/1.1
Host: glacier.`Region`.amazonaws.com
Date: `Date`
Authorization: `SignatureValue`
Content-Length: `Length`
x-amz-glacier-version: 2012-06-01

{
  "Policy":
    {
      "Rules":[
         {
             "Strategy": ***String***,
             "BytesPerHour": ***Number***
         }
       ]
    }
}
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

The request body contains the following JSON fields.

**BytesPerHour**

The maximum number of bytes that can be retrieved in an hour.

This field is required only if the value of the Strategy field is
`BytesPerHour`. Your PUT operation will be rejected if the Strategy field
is not set to `BytesPerHour` and you set this field.

_Type_: Number

_Required_: Yes, if the Strategy field is set to
`BytesPerHour`. Otherwise, no.

_Valid Values_: Minimum integer value of 1. Maximum integer value
of 2^63 - 1 inclusive.

**Rules**

The policy rule. Although this is a list type, currently there must be only one
rule, which contains a Strategy field and optionally a BytesPerHour field.

_Type_: Array

_Required_: Yes

**Strategy**

The type of data retrieval policy to set.

_Type_: String

_Required_: Yes

Valid values: `BytesPerHour`|`FreeTier`|`None`.
`BytesPerHour` is equivalent to selecting **Max Retrieval
Rate** in the console. `FreeTier` is equivalent to selecting
**Free Tier Only** in the console. `None` is equivalent
to selecting **No Retrieval Policy** in the console. For more
information about selecting data retrieval policies in the console, see
[Amazon Glacier Data Retrieval Policies](data-retrieval-policy.md "data-retrieval-policy.md").

## Responses

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

The following example sends an HTTP PUT request with the Strategy field set to
`BytesPerHour`.

```
PUT /-/policies/data-retrieval HTTP/1.1
Host: glacier.us-west-2.amazonaws.com
x-amz-Date: 20170210T120000Z
x-amz-glacier-version: 2012-06-01
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20141123/us-west-2/glacier/aws4_request,SignedHeaders=host;x-amz-date;x-amz-glacier-version,Signature=9257c16da6b25a715ce900a5b45b03da0447acf430195dcb540091b12966f2a2

{
  "Policy":
    {
      "Rules":[
         {
             "Strategy":"BytesPerHour",
             "BytesPerHour":10737418240
          }
       ]
    }
}
```

The following example sends an HTTP PUT request with the Strategy field set to `FreeTier`.

```
PUT /-/policies/data-retrieval HTTP/1.1
Host: glacier.us-west-2.amazonaws.com
x-amz-Date: 20170210T120000Z
x-amz-glacier-version: 2012-06-01
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20141123/us-west-2/glacier/aws4_request,SignedHeaders=host;x-amz-date;x-amz-glacier-version,Signature=9257c16da6b25a715ce900a5b45b03da0447acf430195dcb540091b12966f2a2

{
  "Policy":
    {
      "Rules":[
         {
             "Strategy":"FreeTier"
          }
       ]
    }
}
```

The following example sends an HTTP PUT request with the Strategy field set to `None`.

```
PUT /-/policies/data-retrieval HTTP/1.1
Host: glacier.us-west-2.amazonaws.com
x-amz-Date: 20170210T120000Z
x-amz-glacier-version: 2012-06-01
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20141123/us-west-2/glacier/aws4_request,SignedHeaders=host;x-amz-date;x-amz-glacier-version,Signature=9257c16da6b25a715ce900a5b45b03da0447acf430195dcb540091b12966f2a2

{
  "Policy":
    {
      "Rules":[
         {
             "Strategy":"None"
          }
       ]
    }
}
```

### Example Response

If the request was successful Amazon Glacier (Amazon Glacier) sets the policy and returns a `HTTP 204 No Content` as
shown in the following example.

```
HTTP/1.1 204 No Content
x-amzn-RequestId: AAABZpJrTyioDC_HsOmHae8EZp_uBSJr6cnGOLKp_XJCl-Q
Date: Wed, 10 Feb 2017 12:02:00 GMT
```

## Related Sections

- [Get Data Retrieval Policy (GET policy)](api-GetDataRetrievalPolicy.md "api-GetDataRetrievalPolicy.md")

- [Initiate Job (POST jobs)](api-initiate-job-post.md "api-initiate-job-post.md")
