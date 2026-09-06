

# `pcluster export-cluster-logs`
<a name="pcluster.export-cluster-logs-v3"></a>

Export the logs of the cluster to a local `tar.gz` archive by passing through an Amazon S3 Bucket.

```
pcluster export-cluster-logs [-h]
                 --cluster-name {{CLUSTER_NAME}}
                [--bucket {{BUCKET_NAME}}]
                [--bucket-prefix {{BUCKET_PREFIX}}]
                [--debug]
                [--end-time {{END_TIME}}]
                [--filters {{FILTER}} [{{FILTER}} ...]]
                [--keep-s3-objects {{KEEP_S3_OBJECTS}}]
                [--output-file {{OUTPUT_FILE}}]
                [--region {{REGION}}]
                [--start-time {{START_TIME}}]
```

**Note**  
The `export-cluster-logs` command waits for CloudWatch Logs to complete the export of logs, so it is expected to experience a period of time without any output.

## Named arguments
<a name="pcluster-v3.export-cluster-logs.namedargs"></a>

**-h, --help**  
Shows the help text for `pcluster export-cluster-logs`.

**--bucket {{BUCKET\_NAME}}**  
Specifies the name of the Amazon S3 bucket to export cluster logs data to. It must be in the same Region as the cluster.  
+ You must add permissions to the Amazon S3 bucket policy to grant CloudWatch access. For more information, see [ Set permissions on an Amazon S3 bucket](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/S3ExportTasks.html#S3Permissions) in the *CloudWatch Logs User Guide*.
+ Starting with AWS ParallelCluster version **3.12.0**, the `--bucket` option is **optional**. If the option is not specified, either the AWS ParallelCluster regional default bucket (`parallelcluster-hash-v1-DO-NOT-DELETE`) will be used, or if the Amazon S3 bucket pointed to by `CustomS3Bucket` is specified in the cluster configuration, that will be used. If you do not specify the `--bucket` option and you use the default AWS ParallelCluster bucket, you cannot export logs to the `parallelcluster/` folder, because it is a protected folder reserved for internal use.
If the AWS ParallelCluster default bucket is used, pcluster will take care of configuring the bucket policy. If you customized the bucket policy and then upgrade to AWS ParallelCluster version **3.12.0**, the bucket policy will be overridden and you will need to reapply your changes.

**--cluster-name, -n {{CLUSTER\_NAME}}**  
Specifies the name of the cluster.

**--bucket-prefix {{BUCKET\_PREFIX}}**  
Specifies the path in the Amazon S3 bucket where exported logs data is to be stored.  
By default, the bucket-prefix is:  

```
{{cluster-name}}-logs-{{202209061743}}.tar.gz
```
`{{202209061743}}` is an example of the time in `%Y%m%d%H%M` format.  
Starting with AWS ParallelCluster version **3.12.0**, if you don't specify the `--bucket` option and you use the default AWS ParallelCluster bucket, you cannot export logs to the `parallelcluster/` folder, because it is a protected folder reserved for internal use.

**--debug**  
Enables debug logging.

**--end-time {{END\_TIME}}**  
Specifies the end of the time range to collect log events, expressed in ISO 8601 format (`YYYY-MM-DDThh:mm:ssZ`, for example `2021-01-01T20:00:00Z`'). Events with a timestamp equal to or later than this time are not included. Time elements (e.g. minutes and seconds) may be omitted. The default value is the current time.

**--filters {{FILTER}} [{{FILTER}} ...]**  
Specifies filters for the log. Format: `Name=a,Values=1 Name=b,Values=2,3`. Supported filters are:    
`private-dns-name`  
Specifies the short form of the private DNS name of the instance (e.g. `ip-10-0-0-101`).  
`node-type`  
Specifies the node type, the only accepted value for this filter is `HeadNode`.

**--keep-s3-objects {{KEEP\_S3\_OBJECTS}}**  
If `true`, the exported objects exports to Amazon S3 are kept. (Defaults to `false`.)

**--output-file {{OUTPUT\_FILE}}**  
Specifies the file path to save the log archive to. If this is provided, then the logs are saved locally. Otherwise they are uploaded to Amazon S3 with the URL returned in the output. Default is to upload to Amazon S3.

**--region, -r {{REGION}}**  
Specifies the AWS Region to use. The AWS Region must be specified, using the `AWS_DEFAULT_REGION` environment variable, the `region` setting in the `[default]` section of the `~/.aws/config` file, or the `--region` parameter.

**--start-time {{START\_TIME}}**  
Specifies the start of the time range, expressed in ISO 8601 format (`YYYY-MM-DDThh:mm:ssZ`, for example `2021-01-01T20:00:00Z`). Log events with a timestamp equal to this time or later than this time are included. If not specified, the default is the time the cluster was created.

**Example using AWS ParallelCluster version 3.1.4:**

```
$ pcluster export-cluster-logs --bucket {{cluster-v3-bucket}} -n {{cluster-v3}}
{
  "url": "https://cluster-v3-bucket..."
}
```

## Cannot retrieve the logs?
<a name="pcluster-v3.export-cluster-logs.retrieve-logs"></a>

If you cannot retrieve the logs using the `export-cluster-logs` command, then do one of the following:
+ Retrieve the logs manually from the CloudWatch log group of the cluster.
+ If the log group is empty, SSH into cluster nodes and retrieve the logs listed in [Troubleshooting node initialization issues](troubleshooting-v3-scaling-issues.md#troubleshooting-v3-node-init).
+ If cluster nodes are not accessible because the cluster failed to create, then recreate the cluster with option `--rollback-on-failure false` and retrieve the logs from the nodes.