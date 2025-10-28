# INTERNAL_ERROR_EC2_INSUFFICIENT_CAPACITY_AZ

## Overview

A cluster terminates with an
`INTERNAL_ERROR_EC2_INSUFFICIENT_CAPACITY_AZ` error when the
selected Availability Zone doesn't have enough capacity to fulfill your Amazon EC2 instance
type request. The subnet that you select for a cluster determines the Availability Zone.
For more information about subnets for Amazon EMR, see [Configure networking in a VPC for Amazon EMR](emr-plan-vpc-subnet.md "emr-plan-vpc-subnet.md").

## Resolution

To resolve this error, modify your instance type configurations and create a
new cluster with your updated request.

To troubleshoot the failed EMR cluster, refer to the `ErrorDetail` information returned from the `DescribeCluster` and `ListClusters` APIs. For more information, see [Error codes with ErrorDetail
information in Amazon EMR](emr-troubleshoot-error-errordetail.md "emr-troubleshoot-error-errordetail.md"). The `ErrorData` array within `ErrorDetail` returns the following information for this error code:

**`instance-type`**

The instance type that is out of capacity.

**`availability-zone`**

The Availability Zone that your subnet resolves to.

**`public-doc`**

The public URL of the documentation for the error code.

## Steps to

complete

Perform the following steps to identify and fix the root cause of the cluster
configuration error:

- Review the best practices for cluster configuration. See [Configuring Amazon EMR cluster instance types and best practices for Spot instances](emr-plan-instances-guidelines.md "emr-plan-instances-guidelines.md") in the
  _Amazon EMR Management Guide_.
- Troubleshoot the launch issues and review your configuration. See
  [Troubleshoot instance launch issues](../../../AWSEC2/latest/UserGuide/troubleshooting-launch.md "../../../AWSEC2/latest/UserGuide/troubleshooting-launch.md") in the
  _Amazon EC2 User Guide_.
- Launch a new cluster with your updated cluster configuration.
