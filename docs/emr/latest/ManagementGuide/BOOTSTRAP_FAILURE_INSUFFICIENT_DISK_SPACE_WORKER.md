

# BOOTSTRAP\_FAILURE\_INSUFFICIENT\_DISK\_SPACE\_WORKER
<a name="BOOTSTRAP_FAILURE_INSUFFICIENT_DISK_SPACE_WORKER"></a>

## Overview
<a name="BOOTSTRAP_FAILURE_INSUFFICIENT_DISK_SPACE_WORKER_overview"></a>

 The `BOOTSTRAP_FAILURE_INSUFFICIENT_DISK_SPACE_WORKER` error indicates that one or more worker instances do not have enough disk space when installing necessary software. 

## Resolution
<a name="BOOTSTRAP_FAILURE_INSUFFICIENT_DISK_SPACE_WORKER_resolution"></a>

 To resolve this error, confirm that your worker instances have sufficient disk space on the root volume. 

To troubleshoot the failed EMR cluster, refer to the `ErrorDetail` information returned from the `DescribeCluster` and `ListClusters` APIs. For more information, see [Error codes with ErrorDetail information in Amazon EMR](emr-troubleshoot-error-errordetail.md). The `ErrorData` array within `ErrorDetail` returns the following information for this error code:

**`worker-instance-ids`**  
The IDs of the worker instances with insufficient disk space.

**`public-doc`**  
The public URL of the documentation for the error code.

## Steps to complete
<a name="BOOTSTRAP_FAILURE_INSUFFICIENT_DISK_SPACE_WORKER_stc"></a>

1.  Review the best practices for your cluster’s EBS root device volume. See [Customizing the Amazon EBS root device volume](emr-custom-ami-root-volume-size.md) in the *Amazon EMR Management Guide*. 

1. Launch a new cluster with a larger EBS root device volume size.