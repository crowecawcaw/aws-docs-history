# BOOTSTRAP_FAILURE_BA_DOWNLOAD_FAILED_PRIMARY

## Overview

A cluster terminates with the
`BOOTSTRAP_FAILURE_BA_DOWNLOAD_FAILED_PRIMARY` error when the
primary instance can’t download a bootstrap action script from the Amazon S3 location
that you specify. Potential causes include the following:

- The bootstrap action script file isn’t in the specified Amazon S3
  location.
- The service role for Amazon EC2 instances on the cluster (also called the
  _EC2 instance profile for Amazon EMR_) doesn't have
  permissions to access the Amazon S3 bucket where the bootstrap action script
  resides. For more information about service roles, see [Service role for cluster EC2 instances (EC2
  instance profile)](emr-iam-role-for-ec2.md "emr-iam-role-for-ec2.md").

For more information about bootstrap actions, see [Create bootstrap actions to install additional
software with an Amazon EMR cluster](emr-plan-bootstrap.md "emr-plan-bootstrap.md").

## Resolution

To resolve this error, ensure that your primary instance has appropriate
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

###### Troubleshooting steps

1. Use the `amazon-s3-path` value from the
   `ErrorData` array to find the relevant bootstrap action
   script in Amazon S3.
2. If you turned on cluster logs when you created the instance, refer to
   the `stdout` log for more information. You can find the
   `stdout` log for the bootstrap action in this Amazon S3
   location:

```
s3://`amzn-s3-demo-bucket`/logs/Your_Cluster_Id/node/Primary_Instance_Id/bootstrap-actions/Failed_Bootstrap_Action_Number/stdout.gz

```

For more information on cluster logs, see [Configure Amazon EMR cluster logging and debugging](emr-plan-debugging.md "emr-plan-debugging.md"). 3. To determine the bootstrap action failure, review the exceptions in
the `stdout` logs, and the `return-code` value in
`ErrorData`. 4. Use your findings from the previous step to revise your bootstrap
action so that it avoids exceptions or can gracefully handle exceptions
when they occur. 5. Launch a new cluster with your updated bootstrap action.
