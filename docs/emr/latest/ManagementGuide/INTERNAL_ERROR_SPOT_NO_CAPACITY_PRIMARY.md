# INTERNAL_ERROR_SPOT_NO_CAPACITY_PRIMARY

## Overview

A cluster terminates with a
`INTERNAL_ERROR_SPOT_NO_CAPACITY_PRIMARY` error when there isn't
enough capacity to fulfill a Spot Instance request for your primary node. For
more information, see [Spot
Instances](../../../AWSEC2/latest/UserGuide/using-spot-instances.md "../../../AWSEC2/latest/UserGuide/using-spot-instances.md") in the _Amazon EC2 User Guide_.

## Resolution

To resolve this error, specify instance types for your cluster that are within
your price target, or increase your price limit for the same instance type.

To troubleshoot the failed EMR cluster, refer to the `ErrorDetail` information returned from the `DescribeCluster` and `ListClusters` APIs. For more information, see [Error codes with ErrorDetail
information in Amazon EMR](emr-troubleshoot-error-errordetail.md "emr-troubleshoot-error-errordetail.md"). The `ErrorData` array within `ErrorDetail` returns the following information for this error code:

**`primary-instance-id`**

The ID for the primary instance of the cluster that failed.

**`instance-type`**

The instance type that is out of capacity.

**`availability-zone`**

The Availability Zone that your subnet resolves to.

**`public-doc`**

The public URL of the documentation for the error code.

## Steps to

complete

Perform the following steps to troubleshoot your cluster configuration
strategy, and then launch a new cluster:

1. Review the best practices for Amazon EC2 Spot Instances and review your
   cluster configuration strategy. For more information, see [Best
   practices for EC2 Spot](../../../AWSEC2/latest/UserGuide/spot-best-practices.md "../../../AWSEC2/latest/UserGuide/spot-best-practices.md") in the
   _Amazon EC2 User Guide_ and [Configuring Amazon EMR cluster instance types and best practices for Spot instances](emr-plan-instances-guidelines.md "emr-plan-instances-guidelines.md").
2. Modify your instance type configurations and create a new cluster with
   your updated request.
3. If the issue persists, use On-Demand capacity for your primary
   instance.
