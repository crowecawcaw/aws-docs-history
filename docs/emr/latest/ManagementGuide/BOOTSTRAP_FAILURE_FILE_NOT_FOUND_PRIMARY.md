# BOOTSTRAP_FAILURE_FILE_NOT_FOUND_PRIMARY

## Overview

The `BOOTSTRAP_FAILURE_FILE_NOT_FOUND_PRIMARY` error indicates that
the primary instance can’t find the bootstrap action script that the instance
just downloaded from the specified Amazon S3 bucket.

## Resolution

To resolve this error, confirm that your primary instance has appropriate
access to the bootstrap action script.

To troubleshoot the failed EMR cluster, refer to the `ErrorDetail` information returned from the `DescribeCluster` and `ListClusters` APIs. For more information, see [Error codes with ErrorDetail
information in Amazon EMR](emr-troubleshoot-error-errordetail.md "emr-troubleshoot-error-errordetail.md"). The `ErrorData` array within `ErrorDetail` returns the following information for this error code:

**`primary-instance-id`**

The ID of the primary instance where the bootstrap action
failed.

**`bootstrap-action`**

The ordinal number for the bootstrap action that failed. A script
with a `bootstrap-action` value of `1` is the
first bootstrap action to run on the instance.

**`amazon-s3-path`**

The Amazon S3 location of the bootstrap action that failed.

**`public-doc`**

The public URL of the documentation for the error code.

## Steps to

complete

Perform the following steps to identify and fix the root cause of the
bootstrap action error. Then launch a new cluster.

1. To find the relevant bootstrap action script in Amazon S3, use the
   `amazon-s3-path` value from the `ErrorData`
   array.
2. Review the bootstrap action log files in Amazon S3 to identify the root
   cause for the failure. To learn more on how to view Amazon EMR logs, see
   [View Amazon EMR log files](emr-manage-view-web-log-files.md "emr-manage-view-web-log-files.md").

###### Note

If you didn't turn on logs for your cluster, you must create a new
cluster with the same configurations and bootstrap actions. To
ensure the cluster logs are turned on, see [Configure Amazon EMR cluster logging and debugging](emr-plan-debugging.md "emr-plan-debugging.md"). 3. Review the `stdout` log for your bootstrap actions and
confirm that there are no custom processes that delete files in the
`/emr/instance-controller/lib/bootstrap-actions` folder
on your primary instances. You can find the `stdout` log for
the bootstrap action in this Amazon S3 location:

```
s3://`amzn-s3-demo-bucket`/logs/Your_Cluster_Id/node/Primary_Instance_Id/bootstrap-actions/Failed_Bootstrap_Action_Number/stdout.gz
```

4. Launch a new cluster with your updated bootstrap action.
