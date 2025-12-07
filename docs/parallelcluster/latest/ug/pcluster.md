# `pcluster export-image-logs`

Export the logs of the image builder stack to a local `tar.gz` archive by passing through an
Amazon S3 Bucket.

```
pcluster export-image-logs [-h]
                 --image-id `IMAGE_ID`
                [--bucket `BUCKET`]
                [--bucket-prefix `BUCKET_PREFIX`]
                [--debug]
                [--end-time `END_TIME`]
                [--keep-s3-objects `KEEP_S3_OBJECTS`]
                [--output-file `OUTPUT_FILE`]
                [--region `REGION`]
                [--start-time `START_TIME`]
```

###### Note

The `export-image-logs` command waits for CloudWatch Logs to complete the export
of logs, so it is expected to experience a period of time without any output.

## Named arguments

`-h, --help`

Shows the help text for `pcluster export-image-logs`.

`--bucket `BUCKET_NAME``

Specifies the Amazon S3 bucket name to export image build logs to. It must be in the same Region as the image.

###### Note

- You must add permissions to the Amazon S3 bucket policy to grant CloudWatch access. For more
  information, see [Set permissions on an Amazon S3 bucket](../../../AmazonCloudWatch/latest/logs/S3ExportTasks.md#S3Permissions "../../../AmazonCloudWatch/latest/logs/S3ExportTasks.md#S3Permissions") in the _CloudWatch Logs User Guide_.
- Starting with AWS ParallelCluster version **3.12.0**, the `--bucket`
  option is **optional**. If the option is not specified, either the AWS ParallelCluster
  regional default bucket (`parallelcluster-hash-v1-DO-NOT-DELETE`) will be used, or if the
  `CustomS3Bucket` is specified in the image configuration, that will be used.

###### Important

If the AWS ParallelCluster default bucket is used, pcluster will take care of configuring the bucket policy. If you
customize the bucket policy before you upgrade to AWS ParallelCluster version **3.12.0**,
the bucket policy will be overridden and you will need to reapply the changes.

`--image-id, -i `IMAGE_ID``

The image ID whose logs will be exported.

`--bucket-prefix `BUCKET_PREFIX``

Specifies the path in the Amazon S3 bucket where exported logs data is to be stored.

By default, the bucket-prefix is:

```
`ami-id`-logs-`202209061743`.tar.gz
```

`202209061743` is the current time in `%Y%m%d%H%M` format.

###### Note

Starting with AWS ParallelCluster version **3.12.0**, if you don't specify the
`--bucket` option and use the default AWS ParallelCluster bucket, you cannot export logs to the
`parallelcluster/` folder, because it is a protected folder reserved for internal use.

`--debug`

Enables debug logging.

`--end-time `END_TIME``

Specifies the end of the time range to collect log events, expressed in ISO 8601 format
(`YYYY-MM-DDThh:mm:ssZ`, for example `2021-01-01T20:00:00Z`'). Events with a timestamp
equal to or later than this time are not included. Time elements (e.g. minutes and seconds) may be omitted. The
default value is the current time.

`--keep-s3-objects `KEEP_S3_OBJECTS``

If `true`, the exported objects exports to Amazon S3 are kept. (Defaults to `false`.)

`--output-file `OUTPUT_FILE``

Specifies the file path to save the log archive to. If this is provided, then the logs are saved locally.
Otherwise they are uploaded to Amazon S3 with the URL returned in the output. Default is to upload to Amazon S3.

`--region, -r `REGION``

Specifies the AWS Region to use. The AWS Region must be specified, using the `AWS_DEFAULT_REGION`
environment variable, the `region` setting in the `[default]` section of the
`~/.aws/config` file, or the `--region` parameter.

`--start-time `START_TIME``

Specifies the start of the time range, expressed in ISO 8601 format (`YYYY-MM-DDThh:mm:ssZ`, for
example `2021-01-01T20:00:00Z`). Log events with a timestamp equal to this time or later than this
time are included. If not specified, the default is the time the cluster was created.

**Example using AWS ParallelCluster version 3.1.4:**

````
`$` `pcluster export-image-logs --bucket `image-v3-bucket` --image-id `ami-1234abcd5678efgh```{
 "url": "https://image-v3-bucket..."
}`
````
