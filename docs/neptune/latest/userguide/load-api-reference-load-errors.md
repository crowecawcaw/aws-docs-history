# Neptune Loader Errors

When an error occurs, a JSON object is returned in the `BODY` of the
response. The `message` object contains a description of the error.

###### Error Categories

- `Error 400`   –   Syntax errors return
  an HTTP `400` bad request error. The message describes the
  error.
- `Error 500`   –   A valid request that
  cannot be processed returns an HTTP `500` internal server
  error. The message describes the error.
  The following are possible error messages from the loader with a description of the
  error.

###### Loader Error Messages

- `Couldn't find the AWS credential for iam_role_arn`  (HTTP 400)

The credentials were not found. Verify the supplied credentials against the IAM
console or AWS CLI output. Make sure that you have added the IAM role specified in
`iamRoleArn` to the cluster.

- `S3 bucket not found for source`  (HTTP 400)

The S3 bucket does not exist. Check the name of the bucket.

- `The source `source-uri` does not exist/not reachable`  (HTTP 400)

No matching files were found in the S3 bucket.

- `Unable to connect to S3 endpoint. Provided source =
`source-uri`and region =`aws-region``  (HTTP 500)

Unable to connect to Amazon S3. Region must match the cluster Region. Ensure that you
have a VPC endpoint. For information about creating a VPC endpoint, see [Creating an Amazon S3 VPC Endpoint](bulk-load-data.md#bulk-load-prereqs-s3 "bulk-load-data.md#bulk-load-prereqs-s3").

- `Bucket is not in provided Region (`aws-region`)`  (HTTP 400)

The bucket must be in the same AWS Region as your Neptune DB instance.

- `Unable to perform S3 list operation`  (HTTP 400)

The IAM user or role provided does not have `List` permissions on the
bucket or the folder. Check the policy or the access control list (ACL) on the
bucket.

- `Start new load operation not permitted on a read replica instance`  (HTTP 405)

Loading is a write operation. Retry load on the read/write cluster endpoint.

- `Failed to start load because of unknown error from S3`  (HTTP 500)

Amazon S3 returned an unknown error. Contact [AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/").

- `Invalid S3 access key`  (HTTP 400)

Access key is invalid. Check the provided credentials.

- `Invalid S3 secret key`  (HTTP 400)

Secret key is invalid. Check the provided credentials.

- `Max concurrent load limit breached`  (HTTP 400)

If a load request is submitted without `"queueRequest" : "TRUE"`,
and a load job is currently running, the request will fail with this error.

- `Failed to start new load for the source "`source name`".
Max load task queue size limit breached. Limit is 64`  (HTTP 400)

Neptune supports queuing up as many as 64 loader jobs at a time. If
an additional load request is submitted to the queue when it already contains 64
jobs, the request fails with this message.
