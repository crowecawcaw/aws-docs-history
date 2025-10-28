AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# Exporting HealthOmics read sets to an Amazon S3 bucket

You can export read sets as a batch export job to an Amazon S3 bucket. To do so, first
create an IAM policy that has write access to the bucket, similar to the following
IAM policy example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket1",
 "arn:aws:s3:::amzn-s3-demo-bucket1/*"
 ]
 }
 ]
}`

```

JSON

```
`{
"Version":"2012-10-17",
"Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "omics.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
]
}`

```

After the IAM policy is in place, begin your read set export job. The following example shows you
how to do this by using the **start-read-set-export-job** API operation. In the following
example, replace all parameters, such as `sequence store ID`,
`destination` , `role ARN`, and
`sources`, with your input.

```
aws omics start-read-set-export-job
--sequence-store-id ``sequence store id`` \
--destination ``valid s3 uri`` \
--role-arn ``role ARN`` \
--sources ``readSetId=read set id_1`` ``readSetId=read set id_2``
```

You receive the following response with information on the origin sequence store
and the destination Amazon S3 bucket.

```
{
"id": <job-id>,
"sequenceStoreId": <sequence-store-id>,
"destination": <destination-s3-uri>,
"status": "SUBMITTED",
"creationTime": "2022-10-22T01:33:38.079000+00:00"
}
```

After the job starts, you can determine its status by using the
**get-read-set-export-job** API operation, as shown in the following. Replace the
`sequence store ID` and `job ID`
with your sequence store ID and job ID, respectively.

```
aws omics get-read-set-export-job --id ``job-id`` --sequence-store-id ``sequence store ID``
```

You can view all export jobs initialized for a sequence store by using the **list-read-set-export-jobs** API operation, as shown in the following. Replace the
`sequence store ID` with your sequence store ID.

```
aws omics list-read-set-export-jobs --sequence-store-id ``sequence store ID``.
```

```
{
"exportJobs": [
  {
      "id": <job-id>,
      "sequenceStoreId": <sequence-store-id>,
      "destination": <destination-s3-uri>,
      "status": "COMPLETED",
      "creationTime": "2022-10-22T01:33:38.079000+00:00",
      "completionTime": "2022-10-22T01:34:28.941000+00:00"
  }
]
}
```

In addition to exporting your read sets, you can also share them by using the Amazon S3 access URIs. To
learn more, see [Accessing HealthOmics read sets with Amazon S3 URIs](s3-access.md "s3-access.md").
