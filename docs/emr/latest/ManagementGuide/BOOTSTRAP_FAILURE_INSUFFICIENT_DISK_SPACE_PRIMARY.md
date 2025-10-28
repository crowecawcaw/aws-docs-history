#

BOOTSTRAP_FAILURE_INSUFFICIENT_DISK_SPACE_PRIMARY

## Overview

The `BOOTSTRAP_FAILURE_INSUFFICIENT_DISK_SPACE_PRIMARY` error indicates that
the primary instance does not have enough disk space when installing necessary software.

## Resolution

To resolve this error, confirm that your primary instance has sufficient disk space on the root volume.

To troubleshoot the failed EMR cluster, refer to the `ErrorDetail` information returned from the `DescribeCluster` and `ListClusters` APIs. For more information, see [Error codes with ErrorDetail
information in Amazon EMR](emr-troubleshoot-error-errordetail.md "emr-troubleshoot-error-errordetail.md"). The `ErrorData` array within `ErrorDetail` returns the following information for this error code:

**`primary-instance-id`**

The ID of the primary instance with insufficient disk space.

**`public-doc`**

The public URL of the documentation for the error code.

## Steps to complete

1. Review the best practices for your cluster’s EBS root device volume.

See [Customizing the Amazon EBS root device
volume](emr-custom-ami-root-volume-size.md "emr-custom-ami-root-volume-size.md") in the _Amazon EMR Management Guide_. 2. Launch a new cluster with a larger EBS root device volume size.
