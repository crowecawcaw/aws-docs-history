# VALIDATION_ERROR_SUBNET_NOT_FROM_ONE_VPC

## Overview

When your cluster and the subnets that you reference for your cluster belong
to different virtual private clouds (VPCs), the cluster terminates with a
`VALIDATION_ERROR_SUBNET_NOT_FROM_ONE_VPC` error. You can launch
clusters with Amazon EMR with the instance fleets configuration across subnets in a
VPC. For more information about instance fleets, see [Planning and configuring instance fleets for your Amazon EMR cluster](emr-instance-fleet.md "emr-instance-fleet.md") in the
_Amazon EMR Management Guide_.

## Resolution

To resolve this error, use subnets that belong to the same VPC as the
cluster.

To troubleshoot the failed EMR cluster, refer to the `ErrorDetail` information returned from the `DescribeCluster` and `ListClusters` APIs. For more information, see [Error codes with ErrorDetail
information in Amazon EMR](emr-troubleshoot-error-errordetail.md "emr-troubleshoot-error-errordetail.md"). The `ErrorData` array within `ErrorDetail` returns the following information for this error code:

**`vpc`**

For each subnet:VPC pair, the ID for the VPC that the subnet
belongs to.

**`subnet`**

For each subnet:VPC pair, the ID for the subnet.

**`public-doc`**

The public URL of the documentation for the error code.

## Steps to

complete

Perform the following steps to identify and fix the error:

1. Review the subnet IDs that are listed in the `ErrorData`
   array and confirm that they belong to the VPC where you want to launch
   the EMR cluster.
2. Modify your subnet configurations. You can use one of the following
   methods to find all available public and private subnets in a
   VPC.
   - Navigate to the Amazon VPC Console. Choose
     **Subnets** and list all of the subnets
     that reside within the AWS Region for your cluster. To find
     only public or private subnets, apply the **Auto-assign
     public IPv4 address** filter. To find and select
     subnets in the VPC that your cluster uses, use the
     **Filter by VPC** option. For more
     information on how to create subnets, see [Create a
     subnet](../../../vpc/latest/userguide/create-subnets.md "../../../vpc/latest/userguide/create-subnets.md") in the _Amazon Virtual Private Cloud User
     Guide_.
   - Use the AWS CLI to find all available public and private subnets
     in the VPC that your cluster uses. For more information, see the
     [describe-subnets](https://amazonaws.com/ec2/describe-subnets.html "https://amazonaws.com/ec2/describe-subnets.html") API. To create new subnets in a
     VPC, see the [create-subnet](https://amazonaws.com/ec2/create-subnet.html "https://amazonaws.com/ec2/create-subnet.html") API.

3. Launch a new cluster with subnets from the same VPC as the
   cluster.
