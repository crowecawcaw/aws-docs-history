# VALIDATION_ERROR_SECURITY_GROUP_NOT_FROM_ONE_VPC

## Overview

When your cluster and the security groups that you assign to your cluster
belong to different virtual private clouds (VPCs), the cluster terminates with a
`VALIDATION_ERROR_SECURITY_GROUP_NOT_FROM_ONE_VPC` error. For
more information about security groups, see [Specifying Amazon EMR-managed and additional security
groups](emr-sg-specify.md "emr-sg-specify.md") and [Control network traffic with security groups for your Amazon EMR cluster](emr-security-groups.md "emr-security-groups.md").

## Resolution

To resolve this error, use security groups that belong to the same VPC as the
cluster.

To troubleshoot the failed EMR cluster, refer to the `ErrorDetail` information returned from the `DescribeCluster` and `ListClusters` APIs. For more information, see [Error codes with ErrorDetail
information in Amazon EMR](emr-troubleshoot-error-errordetail.md "emr-troubleshoot-error-errordetail.md"). The `ErrorData` array within `ErrorDetail` returns the following information for this error code:

**`vpc`**

For each security-group:VPC pair, the ID for the VPC that the
security group belongs to.

**`security-group`**

For each security-group:VPC pair, the ID for the security
group.

**`public-doc`**

The public URL of the documentation for the error code.

## Steps to

complete

Perform the following steps to identify and fix the error:

1. Review the security group IDs that are listed in the
   `ErrorData` array and confirm that they belong to the VPC
   where you want to launch the EMR cluster.
2. Navigate to the Amazon VPC Console. Choose **Security
   groups** to list all of the security groups within the
   Region that you select. Find the security groups from the same VPC as
   your cluster, and then modify your security group configuration.
3. Launch a new cluster with security groups from the same VPC as the
   cluster.
