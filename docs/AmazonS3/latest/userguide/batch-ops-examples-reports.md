# Examples: S3 Batch Operations completion reports

When you create an S3 Batch Operations job, you can request a completion report for all tasks
or just for failed tasks. As long as at least one task has been invoked successfully,
S3 Batch Operations generates a report for jobs that have completed, failed, or been
canceled.

The completion report contains additional information for each task, including the object
key name and version, status, error codes, and descriptions of any errors. The description
of errors for each failed task can be used to diagnose issues that occur during job
creation, such as permissions. For **Compute checksum** jobs, the completion report contains
checksum values for every object.

###### Note

Completion reports are always encrypted with Amazon S3 managed keys (SSE-S3).

###### Example— Top-level manifest result file

The top-level `manifest.json` file contains the locations of each
succeeded report and (if the job had any failures) the location of failed reports, as
shown in the following example.

```
{
    "Format": "Report_CSV_20180820",
    "ReportCreationDate": "2019-04-05T17:48:39.725Z",
    "Results": [
        {
            "TaskExecutionStatus": "succeeded",
            "Bucket": "my-job-reports",
            "MD5Checksum": "83b1c4cbe93fc893f54053697e10fd6e",
            "Key": "job-f8fb9d89-a3aa-461d-bddc-ea6a1b131955/results/6217b0fab0de85c408b4be96aeaca9b195a7daa5.csv"
        },
        {
            "TaskExecutionStatus": "failed",
            "Bucket": "my-job-reports",
            "MD5Checksum": "22ee037f3515975f7719699e5c416eaa",
            "Key": "job-f8fb9d89-a3aa-461d-bddc-ea6a1b131955/results/b2ddad417e94331e9f37b44f1faf8c7ed5873f2e.csv"
        }
    ],
    "ReportSchema": "Bucket, Key, VersionId, TaskStatus, ErrorCode, HTTPStatusCode, ResultMessage"
}
```

**Succeeded task reports**

Succeeded tasks reports contain the following for the _successful_
tasks:

- `Bucket`
- `Key`
- `VersionId`
- `TaskStatus`
- `ErrorCode`
- `HTTPStatusCode`
- `ResultMessage`
  **Failed task reports**

Failed task reports contain the following information for all
_failed_ tasks:

- `Bucket`
- `Key`
- `VersionId`
- `TaskStatus`
- `ErrorCode`
- `HTTPStatusCode`
- `ResultMessage`

###### Example— Lambda function task report

In the following example, the Lambda function successfully copied the Amazon S3 object to
another bucket. The returned Amazon S3 response is passed back to S3 Batch Operations and is then
written into the final completion report.

```
`amzn-s3-demo-bucket1`,image_17775,,succeeded,200,,"{u'CopySourceVersionId': 'xVR78haVKlRnurYofbTfYr3ufYbktF8h', u'CopyObjectResult': {u'LastModified': datetime.datetime(2019, 4, 5, 17, 35, 39, tzinfo=tzlocal()), u'ETag': '""fe66f4390c50f29798f040d7aae72784""'}, 'ResponseMetadata': {'HTTPStatusCode': 200, 'RetryAttempts': 0, 'HostId': 'nXNaClIMxEJzWNmeMNQV2KpjbaCJLn0OGoXWZpuVOFS/iQYWxb3QtTvzX9SVfx2lA3oTKLwImKw=', 'RequestId': '3ED5852152014362', 'HTTPHeaders': {'content-length': '234', 'x-amz-id-2': 'nXNaClIMxEJzWNmeMNQV2KpjbaCJLn0OGoXWZpuVOFS/iQYWxb3QtTvzX9SVfx2lA3oTKLwImKw=', 'x-amz-copy-source-version-id': 'xVR78haVKlRnurYofbTfYr3ufYbktF8h', 'server': 'AmazonS3', 'x-amz-request-id': '3ED5852152014362', 'date': 'Fri, 05 Apr 2019 17:35:39 GMT', 'content-type': 'application/xml'}}}"
`amzn-s3-demo-bucket1`,image_17763,,succeeded,200,,"{u'CopySourceVersionId': '6HjOUSim4Wj6BTcbxToXW44pSZ.40pwq', u'CopyObjectResult': {u'LastModified': datetime.datetime(2019, 4, 5, 17, 35, 39, tzinfo=tzlocal()), u'ETag': '""fe66f4390c50f29798f040d7aae72784""'}, 'ResponseMetadata': {'HTTPStatusCode': 200, 'RetryAttempts': 0, 'HostId': 'GiCZNYr8LHd/Thyk6beTRP96IGZk2sYxujLe13TuuLpq6U2RD3we0YoluuIdm1PRvkMwnEW1aFc=', 'RequestId': '1BC9F5B1B95D7000', 'HTTPHeaders': {'content-length': '234', 'x-amz-id-2': 'GiCZNYr8LHd/Thyk6beTRP96IGZk2sYxujLe13TuuLpq6U2RD3we0YoluuIdm1PRvkMwnEW1aFc=', 'x-amz-copy-source-version-id': '6HjOUSim4Wj6BTcbxToXW44pSZ.40pwq', 'server': 'AmazonS3', 'x-amz-request-id': '1BC9F5B1B95D7000', 'date': 'Fri, 05 Apr 2019 17:35:39 GMT', 'content-type': 'application/xml'}}}"
`amzn-s3-demo-bucket1`,image_17860,,succeeded,200,,"{u'CopySourceVersionId': 'm.MDD0g_QsUnYZ8TBzVFrp.TmjN8PJyX', u'CopyObjectResult': {u'LastModified': datetime.datetime(2019, 4, 5, 17, 35, 40, tzinfo=tzlocal()), u'ETag': '""fe66f4390c50f29798f040d7aae72784""'}, 'ResponseMetadata': {'HTTPStatusCode': 200, 'RetryAttempts': 0, 'HostId': 'F9ooZOgpE5g9sNgBZxjdiPHqB4+0DNWgj3qbsir+sKai4fv7rQEcF2fBN1VeeFc2WH45a9ygb2g=', 'RequestId': '8D9CA56A56813DF3', 'HTTPHeaders': {'content-length': '234', 'x-amz-id-2': 'F9ooZOgpE5g9sNgBZxjdiPHqB4+0DNWgj3qbsir+sKai4fv7rQEcF2fBN1VeeFc2WH45a9ygb2g=', 'x-amz-copy-source-version-id': 'm.MDD0g_QsUnYZ8TBzVFrp.TmjN8PJyX', 'server': 'AmazonS3', 'x-amz-request-id': '8D9CA56A56813DF3', 'date': 'Fri, 05 Apr 2019 17:35:40 GMT', 'content-type': 'application/xml'}}}"

```

The following example report shows a case in which the AWS Lambda function timed out,
causing failures to exceed the failure threshold. It is then marked as a
`PermanentFailure`.

```
`amzn-s3-demo-bucket1`,image_14975,,failed,200,PermanentFailure,"Lambda returned function error: {""errorMessage"":""2019-04-05T17:35:21.155Z 2845ca0d-38d9-4c4b-abcf-379dc749c452 Task timed out after 3.00 seconds""}"
`amzn-s3-demo-bucket1`,image_15897,,failed,200,PermanentFailure,"Lambda returned function error: {""errorMessage"":""2019-04-05T17:35:29.610Z 2d0a330b-de9b-425f-b511-29232fde5fe4 Task timed out after 3.00 seconds""}"
`amzn-s3-demo-bucket1`,image_14819,,failed,200,PermanentFailure,"Lambda returned function error: {""errorMessage"":""2019-04-05T17:35:22.362Z fcf5efde-74d4-4e6d-b37a-c7f18827f551 Task timed out after 3.00 seconds""}"
`amzn-s3-demo-bucket1`,image_15930,,failed,200,PermanentFailure,"Lambda returned function error: {""errorMessage"":""2019-04-05T17:35:29.809Z 3dd5b57c-4a4a-48aa-8a35-cbf027b7957e Task timed out after 3.00 seconds""}"
`amzn-s3-demo-bucket1`,image_17644,,failed,200,PermanentFailure,"Lambda returned function error: {""errorMessage"":""2019-04-05T17:35:46.025Z 10a764e4-2b26-4d8c-9056-1e1072b4723f Task timed out after 3.00 seconds""}"
`amzn-s3-demo-bucket1`,image_17398,,failed,200,PermanentFailure,"Lambda returned function error: {""errorMessage"":""2019-04-05T17:35:44.661Z 1e306352-4c54-4eba-aee8-4d02f8c0235c Task timed out after 3.00 seconds""}"

```

###### Example— Compute checksum task report

In the following example, the **Compute checksum** operation successfully calculated the
checksum for the uploaded object while at rest. The returned Amazon S3 response is
passed back to S3 Batch Operations, and is then written into the final completion
report:

```
`amzn-s3-demo-bucket1`,s3-standard-1mb-test-object,,succeeded,200,,"{""checksum_base64"":""bS9TOQ\u003d\u003d"",""etag"":""3c3c1813042989094598e4b57ecbdc82"",""checksumAlgorithm"":""CRC32"",""checksumType"":""FULL_OBJECT"",""checksum_hex"":""6D2F5339""}"
```

The following example report shows what happens when a **Compute checksum** operation
fails, resulting in a failed task report:

```
`amzn-s3-demo-bucket1`,image_14975,,failed,200,PermanentFailure,"error details: {""failureMessage"":"Task 2845ca0d-38d9-4c4b-abcf-379dc749c452 SSE-C encryption type is not supported for this operation", ""errorCode"": "400"}"
`amzn-s3-demo-bucket1`,image_14975,,failed,200,PermanentFailure,"error details: {""failureMessage"":"Task 2845ca0d-38d9-4c4b-abcf-379dc749c452 Key not found", ""errorCode"": "404"}"
`amzn-s3-demo-bucket1`,image_14975,,failed,200,PermanentFailure,"error details: {""failureMessage"":"Task 2845ca0d-38d9-4c4b-abcf-379dc749c452 Internal server error, please retry", ""errorCode"": "500"}"
```
