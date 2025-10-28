# VALIDATION_ERROR_INSTANCE_TYPE_NOT_SUPPORTED

## Overview

A cluster terminates with a
`VALIDATION_ERROR_INSTANCE_TYPE_NOT_SUPPORTED` error when the
AWS Region and Availability Zones for your cluster don't support the specified
instance type for one or more instance groups. Amazon EMR might support an instance
type in one Availability Zone within a Region but not another. The subnet that you
select for a cluster determines the Availability Zone within the Region. For a list of
instance types and Regions that Amazon EMR supports, see [Supported instance types with Amazon EMR](emr-supported-instance-types.md "emr-supported-instance-types.md").

## Resolution

To resolve this error, specify instance types for your cluster that Amazon EMR
supports in the Region and Availability Zone where you request the cluster.

To troubleshoot the failed EMR cluster, refer to the `ErrorDetail` information returned from the `DescribeCluster` and `ListClusters` APIs. For more information, see [Error codes with ErrorDetail
information in Amazon EMR](emr-troubleshoot-error-errordetail.md "emr-troubleshoot-error-errordetail.md"). The `ErrorData` array within `ErrorDetail` returns the following information for this error code:

**`instance-types`**

The list of unsupported instance types.

**`availability-zones`**

The list of Availability Zones that your subnet resolves to.

**`public-doc`**

The public URL of the documentation for the error code.

## Steps to

complete

Perform the following steps to identify and fix the error:

1. Use the AWS CLI to retrieve the available instance types in an
   Availability Zone. To do this, you can use the `ec2 describe-instance-type-offerings` command to
   filter available instance types by location (AWS Region or Availability Zone).
   For example, the following command returns the instance types that are
   offered in the specified AZ,
   `us-east-2a`.

```
aws ec2 describe-instance-type-offerings --location-type "availability-zone" --filters Name=location,Values=`us-east-2a` --region `us-east-2` --query "InstanceTypeOfferings[*].[InstanceType]" --output text | sort
```

To learn more about how to discover available instance types, see
[Find an Amazon
EC2 instance type](../../../AWSEC2/latest/UserGuide/instance-discovery.md "../../../AWSEC2/latest/UserGuide/instance-discovery.md"). 2. After you determine the instance types that are available in the same
Region and Availability Zone as the cluster, choose one of the following
resolutions to continue:

    1. Create a new cluster, and choose a subnet for the cluster that
     is in an Availability Zone where the instance type that you selected is
     available and supported by Amazon EMR.
    2. Create a new cluster in the same Region and Amazon EC2 subnet as
     the cluster that failed, but with an instance type that is
     supported in that location by Amazon EMR.

For a list of instance types and Regions that Amazon EMR supports, see [Supported instance types with Amazon EMR](emr-supported-instance-types.md "emr-supported-instance-types.md"). To compare the capabilities
of the instance types, see [Amazon EC2 instance types](https://aws.amazon.com/ec2/instance-types "https://aws.amazon.com/ec2/instance-types").
