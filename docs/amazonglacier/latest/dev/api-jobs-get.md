**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# List Jobs (GET jobs)

## Description

This operation lists jobs for a vault, including jobs that are in-progress and jobs
that have recently finished.

###### Note

Amazon Glacier (Amazon Glacier) retains recently completed jobs for a period before deleting them; however,
it eventually removes completed jobs. The output of completed jobs can be retrieved.
Retaining completed jobs for a period of time after they have completed enables you
to get a job output in the event you miss the job completion notification, or your
first attempt to download it fails. For example, suppose that you start an archive
retrieval job to download an archive. After the job completes, you start to download
the archive but encounter a network error. In this scenario, you can retry and
download the archive while the job exists.

The `List Jobs` operation supports pagination. You should always check the
response `Marker` field. If there are no more jobs to list, the
`Marker` field is set to `null`. If there are more jobs to
list, the `Marker` field is set to a non-null value, which you can use to
continue the pagination of the list. To return a list of jobs that begins at a specific
job, set the `marker` request parameter to the `Marker` value for
that job that you obtained from a previous `List Jobs` request.

You can set a maximum limit for the number of jobs returned in the response by specifying
the `limit` parameter in the request. The default limit is 50. The number of
jobs returned might be fewer than the limit, but the number of returned jobs never
exceeds the limit.

Additionally, you can filter the jobs list returned by specifying the optional
`statuscode` parameter or `completed` parameter, or both.
Using the `statuscode` parameter, you can specify to return only jobs that
match either the `InProgress`, `Succeeded`, or `Failed`
status. Using the `completed` parameter, you can specify to return only jobs
that were completed (`true`) or jobs that were not completed
(`false`).

## Requests

### Syntax

To return a list of jobs of all types, send a `GET` request to the URI of the
vault's `jobs` subresource.

```
GET /`AccountId`/vaults/`VaultName`/jobs HTTP/1.1
Host: glacier.`Region`.amazonaws.com
Date: `Date`
Authorization: `SignatureValue`
x-amz-glacier-version: 2012-06-01
```

###### Note

The `AccountId` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.

### Request Parameters

| Name         | Description                                                                                                                                                                                                                                                                                                                                                      | Required |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `completed`  | The state of the jobs to return. You can specify `true` or<br>`false`.<br>Type: Boolean<br>Constraints: None                                                                                                                                                                                                                                                     | No       |
| `limit`      | The maximum number of jobs to be returned. The default limit is 50. The number of jobs<br>returned might be fewer than the specified limit, but the number<br>of returned jobs never exceeds the limit.<br>Type: String<br>Constraints: Minimum integer value of 1. Maximum integer value of 50.                                                                 | No       |
| `marker`     | An opaque string used for pagination that specifies the job at which the listing of<br>jobs should begin. You get the `marker` value from a<br>previous `List Jobs` response. You only need to<br>include the `marker` if you are continuing the<br>pagination of the results started in a previous `List<br>Jobs` request.<br>Type: String<br>Constraints: None | No       |
| `statuscode` | The type of job status to return.<br>Type: String<br>Constraints: One of the values `InProgress`, `Succeeded`, or<br>`Failed`.                                                                                                                                                                                                                                   | No       |

### Request Headers

This operation uses only response headers that are common to most responses. For information about common response headers, see
[Common Response Headers](api-common-response-headers.md "api-common-response-headers.md").

### Request Body

This operation does not have a request body.

## Responses

### Syntax

```
HTTP/1.1 200 OK
x-amzn-RequestId: **x-amzn-RequestId**
Date: **Date**
Location: ***Location***
Content-Type: application/json
Content-Length: ***Length***

{
    "JobList": [
        {
            "Action": "`string`",
            "ArchiveId": "`string`",
            "ArchiveSHA256TreeHash": "`string`",
            "ArchiveSizeInBytes": `number`,
            "Completed": `boolean`,
            "CompletionDate": "`string`",
            "CreationDate": "`string`",
            "InventoryRetrievalParameters": {
                "EndDate": "`string`",
                "Format": "`string`",
                "Limit": "`string`",
                "Marker": "`string`",
                "StartDate": "`string`"
            },
            "InventorySizeInBytes": `number`,
            "JobDescription": "`string`",
            "JobId": "`string`",
            "JobOutputPath": "`string`",
            "OutputLocation": {
                "S3": {
                    "AccessControlList": [
                        {
                            "Grantee": {
                                "DisplayName": "`string`",
                                "EmailAddress": "`string`",
                                "ID": "`string`",
                                "Type": "`string`",
                                "URI": "`string`"
                            },
                            "Permission": "`string`"
                        }
                    ],
                    "BucketName": "`string`",
                    "CannedACL": "`string`",
                    "Encryption": {
                        "EncryptionType": "`string`",
                        "KMSContext": "`string`",
                        "KMSKeyId": "`string`"
                    },
                    "Prefix": "`string`",
                    "StorageClass": "`string`",
                    "Tagging": {
                        "`string`": "`string`"
                    },
                    "UserMetadata": {
                        "`string`": "`string`"
                    }
                }
            },
            "RetrievalByteRange": "`string`",
            "SelectParameters": {
                "Expression": "`string`",
                "ExpressionType": "`string`",
                "InputSerialization": {
                    "csv": {
                        "Comments": "`string`",
                        "FieldDelimiter": "`string`",
                        "FileHeaderInfo": "`string`",
                        "QuoteCharacter": "`string`",
                        "QuoteEscapeCharacter": "`string`",
                        "RecordDelimiter": "`string`"
                    }
                },
                "OutputSerialization": {
                    "csv": {
                        "FieldDelimiter": "`string`",
                        "QuoteCharacter": "`string`",
                        "QuoteEscapeCharacter": "`string`",
                        "QuoteFields": "`string`",
                        "RecordDelimiter": "`string`"
                    }
                }
            },
            "SHA256TreeHash": "`string`",
            "SNSTopic": "`string`",
            "StatusCode": "`string`",
            "StatusMessage": "`string`",
            "Tier": "`string`",
            "VaultARN": "`string`"
        }
    ],
    "Marker": "`string`"
}
```

### Response Headers

This operation uses only response headers that are common to most responses. For information about common response headers, see
[Common Response Headers](api-common-response-headers.md "api-common-response-headers.md").

### Response Body

The response body contains the following JSON fields.

**JobList**

A list of job objects. Each job object contains metadata describing the job.

_Type_: Array of [GlacierJobDescription](api-GlacierJobDescription.md "api-GlacierJobDescription.md") objects

**Marker**

An opaque string that represents where to continue pagination of the results. You use
the `marker` value in a new `List Jobs` request to
obtain more jobs in the list. If there are no more jobs to list, this
value is `null`.

_Type_: String

### Errors

For information about Amazon Glacier
exceptions and error messages, see [Error Responses](api-error-responses.md "api-error-responses.md").

## Examples

The following examples demonstrate how to return information about vault jobs. The first
example returns a list of two jobs, and the second example returns a subset of
jobs.

### Example: Return All Jobs

#### Example Request

The following `GET` request returns the jobs for a vault.

```
GET /-/vaults/examplevault/jobs  HTTP/1.1
Host: glacier.us-west-2.amazonaws.com
x-amz-Date: 20170210T120000Z
x-amz-glacier-version: 2012-06-01
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20141123/us-west-2/glacier/aws4_request,SignedHeaders=host;x-amz-date;x-amz-glacier-version,Signature=9257c16da6b25a715ce900a5b45b03da0447acf430195dcb540091b12966f2a2
```

#### Example Response

The following response includes an archive retrieval job and an inventory retrieval job
that contains a marker used to continue pagination of the vault inventory
retrieval. The response also shows the `Marker` field set to
`null`, which indicates there are no more jobs to list.

```
HTTP/1.1 200 OK
x-amzn-RequestId: AAABZpJrTyioDC_HsOmHae8EZp_uBSJr6cnGOLKp_XJCl-Q
Date: Wed, 10 Feb 2017 12:00:00 GMT
Content-Type: application/json
Content-Length: 1444

{
  "JobList": [
    {
      "Action": "ArchiveRetrieval",
      "ArchiveId": "BDfaUQul0dVzYwAMr8YSa_6_8abbhZq-i1oT69g8ByClfJyBgAGBkWl2QbF5os851P7Y7KdZDOHWJIn4rh1ZHaOYD3MgFhK_g0oDPesW34uHQoVGwoIqubf6BgUEfQm_wrU4Jlm3cA",
      "ArchiveSizeInBytes": 1048576,
      "ArchiveSHA256TreeHash": "25499381569ab2f85e1fd0eb93c5406a178ab77c5933056eb5d6e7d4adda609b",
      "Completed": true,
      "CompletionDate": "2012-05-01T00:00:09.304Z",
      "CreationDate": "2012-05-01T00:00:06.663Z",
      "InventorySizeInBytes": null,
      "JobDescription": null,
      "JobId": "hDe9t9DTHXqFw8sBGpLQQOmIM0-JrGtu1O_YFKLnzQ64548qJc667BRWTwBLZC76Ygy1jHYruqXkdcAhRsh0hYv4eVRU",
      "RetrievalByteRange": "0-1048575",
      "SHA256TreeHash": "25499381569ab2f85e1fd0eb93c5406a178ab77c5933056eb5d6e7d4adda609b",
      "SNSTopic": null,
      "StatusCode": "Succeeded",
      "StatusMessage": "Succeeded",
      "Tier": "Bulk",
      "VaultARN": "arn:aws:glacier:us-west-2:012345678901:vaults/examplevault"
    },
    {
      "Action": "InventoryRetrieval",
      "ArchiveId": null,
      "ArchiveSizeInBytes": null,
      "ArchiveSHA256TreeHash": null,
      "Completed": true,
      "CompletionDate": "2013-05-11T00:25:18.831Z",
      "CreationDate": "2013-05-11T00:25:14.981Z",
      "InventorySizeInBytes": 1988,
      "JobDescription": null,
      "JobId": "2cvVOnBL36btzyP3pobwIceiaJebM1bx9vZOOUtmNAr0KaVZ4WkWgVjiPldJ73VU7imlm0pnZriBVBebnqaAcirZq_C5",
      "RetrievalByteRange": null,
      "SHA256TreeHash": null,
      "SNSTopic": null,
      "StatusCode": "Succeeded",
      "StatusMessage": "Succeeded",
      "VaultARN": "arn:aws:glacier:us-west-2:012345678901:vaults/examplevault"
      "InventoryRetrievalParameters": {
          "StartDate": "2013-11-12T13:43:12Z",
          "EndDate": "2013-11-20T08:12:45Z",
          "Limit": "120000",
          "Format": "JSON",
          "Marker": "vyS0t2jHQe5qbcDggIeD50chS1SXwYMrkVKo0KHiTUjEYxBGCqRLKaiySzdN7QXGVVV5XZpNVG67pCZ_uykQXFMLaxOSu2hO_-5C0AtWMDrfo7LgVOyfnveDRuOSecUo3Ueq7K0"
    }
  ],
  "Marker": null
}
```

### Example: Return a Partial List of

Jobs

#### Example Request

The following `GET` request returns the job specified by the
`marker` parameter. Setting the `limit` parameter as
`2` specifies that up to two jobs are returned.

```
GET /-/vaults/examplevault/jobs?marker=HkF9p6o7yjhFx-K3CGl6fuSm6VzW9T7esGQfco8nUXVYwS0jlb5gq1JZ55yHgt5vP54ZShjoQzQVVh7vEXAMPLEjobID&limit=2  HTTP/1.1
Host: glacier.us-west-2.amazonaws.com
x-amz-Date: 20170210T120000Z
x-amz-glacier-version: 2012-06-01
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20141123/us-west-2/glacier/aws4_request,SignedHeaders=host;x-amz-date;x-amz-glacier-version,Signature=9257c16da6b25a715ce900a5b45b03da0447acf430195dcb540091b12966f2a2
```

#### Example Response

The following response shows two jobs returned and the `Marker` field set to a
non-null value that can be used to continue pagination of the job list.

```
HTTP/1.1 200 OK
x-amzn-RequestId: AAABZpJrTyioDC_HsOmHae8EZp_uBSJr6cnGOLKp_XJCl-Q
Date: Wed, 10 Feb 2017 12:00:00 GMT
Content-Type: application/json
Content-Length: 1744

{
  "JobList": [
    {
      "Action": "ArchiveRetrieval",
      "ArchiveId": "58-3KpZfcMPUznvMZNPaKyJx9wODCsWTnqcjtx2CjKZ6b-XgxEuA8yvZOYTPQfd7gWR4GRm2XR08gcnWbLV4VPV_kDWtZJKi0TFhKKVPzwrZnA4-FXuIBfViYUIVveeiBE51FO4bvg",
      "ArchiveSizeInBytes": 8388608,
      "ArchiveSHA256TreeHash": "106086b256ddf0fedf3d9e72f461d5983a2566247ebe7e1949246bc61359b4f4",
      "Completed": true,
      "CompletionDate": "2012-05-01T00:25:20.043Z",
      "CreationDate": "2012-05-01T00:25:16.344Z",
      "InventorySizeInBytes": null,
      "JobDescription": "aaabbbccc",
      "JobId": "s4MvaNHIh6mOa1f8iY4ioG2921SDPihXxh3Kv0FBX-JbNPctpRvE4c2_BifuhdGLqEhGBNGeB6Ub-JMunR9JoVa8y1hQ",
      "RetrievalByteRange": "0-8388607",
      "SHA256TreeHash": "106086b256ddf0fedf3d9e72f461d5983a2566247ebe7e1949246bc61359b4f4",
      "SNSTopic": null,
      "StatusCode": "Succeeded",
      "StatusMessage": "Succeeded",
      "Tier": "Bulk",
      "VaultARN": "arn:aws:glacier:us-west-2:012345678901:vaults/examplevault"
    },
    {
      "Action": "ArchiveRetrieval",
      "ArchiveId": "2NVGpf83U6qB9M2u-Ihh61yoFLRDEoh7YLZWKBn80A2i1xG8uieBwGjAr4RkzOHA0E07ZjtI267R03Z-6Hxd8pyGQkBdciCSH1-Lw63Kx9qKpZbPCdU0uTW_WAdwF6lR6w8iSyKdvw",
      "ArchiveSizeInBytes": 1048576,
      "ArchiveSHA256TreeHash": "3d2ae052b2978727e0c51c0a5e32961c6a56650d1f2e4ceccab6472a5ed4a0",
      "Completed": true,
      "CompletionDate": "2012-05-01T16:59:48.444Z",
      "CreationDate": "2012-05-01T16:59:42.977Z",
      "InventorySizeInBytes": null,
      "JobDescription": "aaabbbccc",
      "JobId": "CQ_tf6fOR4jrJCL61Mfk6VM03oY8lmnWK93KK4gLig1UPAbZiN3UV4G_5nq4AfmJHQ_dOMLOX5k8ItFv0wCPN0oaz5dG",
      "RetrievalByteRange": "0-1048575",
      "SHA256TreeHash": "3d2ae052b2978727e0c51c0a5e32961c6a56650d1f2e4ceccab6472a5ed4a0",
      "SNSTopic": null,
      "StatusCode": "Succeeded",
      "StatusMessage": "Succeeded",
      "Tier": "Standard",
      "VaultARN": "arn:aws:glacier:us-west-2:012345678901:vaults/examplevault"
    }
  ],
  "Marker": "CQ_tf6fOR4jrJCL61Mfk6VM03oY8lmnWK93KK4gLig1UPAbZiN3UV4G_5nq4AfmJHQ_dOMLOX5k8ItFv0wCPN0oaz5dG"
}
```

## Related Sections

- [Describe Job (GET JobID)](api-describe-job-get.md "api-describe-job-get.md")
- [Identity and Access Management for Amazon Glacier](security-iam.md "security-iam.md")
