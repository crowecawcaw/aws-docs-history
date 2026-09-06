

# BOOTSTRAP\_FAILURE\_PRIMARY\_WITH\_NON\_ZERO\_CODE
<a name="BOOTSTRAP_FAILURE_PRIMARY_WITH_NON_ZERO_CODE"></a>

## Overview
<a name="BOOTSTRAP_FAILURE_BA_DOWNLOAD_FAILED_WITH_NON_ZERO_CODE_overview"></a>

When a cluster terminates with a `BOOTSTRAP_FAILURE_PRIMARY_WITH_NON_ZERO_CODE` error, a bootstrap action has failed in the primary instance. For more information about bootstrap actions, see [Create bootstrap actions to install additional software with an Amazon EMR cluster](emr-plan-bootstrap.md).

## Resolution
<a name="BOOTSTRAP_FAILURE_BA_DOWNLOAD_FAILED_WITH_NON_ZERO_CODE_resolution"></a>

To resolve this error, review the details returned in the API error, modify your bootstrap action script, and create a new cluster with the updated bootstrap action.

To troubleshoot the failed EMR cluster, refer to the `ErrorDetail` information returned from the `DescribeCluster` and `ListClusters` APIs. For more information, see [Error codes with ErrorDetail information in Amazon EMR](emr-troubleshoot-error-errordetail.md). The `ErrorData` array within `ErrorDetail` returns the following information for this error code:

**`primary-instance-id`**  
The ID of the primary instance where the bootstrap action failed.

**`bootstrap-action`**  
The ordinal number for the bootstrap action that failed. A script with a `bootstrap-action` value of `1` is the first bootstrap action to run on the instance.

**`return-code`**  
The return code for the bootstrap action that failed.

**`amazon-s3-path`**  
The Amazon S3 location of the bootstrap action that failed.

**`public-doc`**  
The public URL of the documentation for the error code.

## Steps to complete
<a name="BOOTSTRAP_FAILURE_BA_DOWNLOAD_FAILED_WITH_NON_ZERO_CODE_stc"></a>

Perform the following steps to identify and fix the root cause of the bootstrap action error. Then launch a new cluster.

1. Review the bootstrap action log files in Amazon S3 to identify the root cause for the failure. To learn more on how to view Amazon EMR logs, see [View Amazon EMR log files](emr-manage-view-web-log-files.md). 

1. If you turned on cluster logs when you created the instance, refer to the `stdout` log for more information. You can find the `stdout` log for the bootstrap action in this Amazon S3 location: 

   ```
   s3://{{amzn-s3-demo-bucket}}/logs/Your_Cluster_Id/node/Primary_Instance_Id/bootstrap-actions/Failed_Bootstrap_Action_Number/stdout.gz 
   ```

   For more information on cluster logs, see [Configure Amazon EMR cluster logging and debugging](emr-plan-debugging.md).

1. To determine the bootstrap action failure, review the exceptions in the `stdout` logs, and the `return-code` value in `ErrorData`.

1. Use your findings from the previous step to revise your bootstrap action so that it avoids exceptions or can gracefully handle exceptions when they occur.

1. Launch a new cluster with your updated bootstrap action.