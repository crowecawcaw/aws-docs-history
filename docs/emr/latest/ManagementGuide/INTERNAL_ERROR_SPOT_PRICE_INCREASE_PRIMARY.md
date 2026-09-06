

# INTERNAL\_ERROR\_SPOT\_PRICE\_INCREASE\_PRIMARY
<a name="INTERNAL_ERROR_SPOT_PRICE_INCREASE_PRIMARY"></a>

## Overview
<a name="INTERNAL_ERROR_SPOT_PRICE_INCREASE_PRIMARY_overview"></a>

A cluster terminates with an `INTERNAL_ERROR_SPOT_PRICE_INCREASE_PRIMARY` error when Amazon EMR can't fulfill your Spot Instance request for the primary node because instances aren't available at or below your maximum Spot price. For more information, see [Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) in the *Amazon EC2 User Guide*.

## Resolution
<a name="INTERNAL_ERROR_SPOT_PRICE_INCREASE_PRIMARY_resolution"></a>

To resolve this error, specify instance types for your cluster that are within your price target, or increase your price limit for the same instance type.

To troubleshoot the failed EMR cluster, refer to the `ErrorDetail` information returned from the `DescribeCluster` and `ListClusters` APIs. For more information, see [Error codes with ErrorDetail information in Amazon EMR](emr-troubleshoot-error-errordetail.md). The `ErrorData` array within `ErrorDetail` returns the following information for this error code:

**`primary-instance-id`**  
The ID for the primary instance of the cluster that failed.

**`instance-type`**  
The instance type that is out of capacity.

**`availability-zone`**  
The Availability Zone where your subnet resides.

**`public-doc`**  
The public URL of the documentation for the error code.

## Steps to complete
<a name="INTERNAL_ERROR_SPOT_PRICE_INCREASE_PRIMARY_stc"></a>

Perform the following steps to troubleshoot your cluster configuration strategy, and then launch a new cluster:

1. Review the best practices for Amazon EC2 Spot Instances and review your cluster configuration strategy. For more information, see [Best practices for EC2 Spot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-best-practices.html) in the *Amazon EC2 User Guide* and [Configuring Amazon EMR cluster instance types and best practices for Spot instances](emr-plan-instances-guidelines.md).

1. Modify your instance type configurations or Availability Zone and create a new cluster with your updated request.

1. If the issue persists, use On-Demand capacity for your primary instance.