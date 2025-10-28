# Tutorial: View IP address history using the AWS CLI

The scenarios in this section show you how to analyze and audit IP address usage using the AWS CLI. For general information about using the AWS CLI, see [Using the AWS CLI](../../../cli/latest/userguide/cli-chap-using.md "../../../cli/latest/userguide/cli-chap-using.md") in the _AWS Command Line Interface User Guide_.

###### Contents

- [Overview](#cli-tut-view-hist-ipam-overview "#cli-tut-view-hist-ipam-overview")
- [Scenarios](#cli-tut-view-hist-ipam-analyze "#cli-tut-view-hist-ipam-analyze")

## Overview

IPAM automatically retains your IP address monitoring data for up to three years. You can use the historical data to
analyze and audit your network security and routing policies. You can search for historical insights for the following types of resources:

- VPCs
- VPC subnets
- Elastic IP addresses
- EC2 instances that are running
- EC2 network interfaces attached to instances

###### Important

Although IPAM doesn't monitor Amazon EC2 instances or EC2 network interfaces attached to instances,
you can use the Search IP history feature to search for historical data on EC2
instance and network interface CIDRs.

###### Note

- The commands in this tutorial must be run using the account that owns the IPAM and the AWS Region that hosts the IPAM.
- Records of changes to CIDRs are picked up in periodic snapshots, which means that it can take
  some time for records to appear or be updated, and the values for SampledStartTime and
  SampledEndTime can differ from the actual times they occurred.

## Scenarios

The scenarios in this section show you how to analyze and audit IP address usage using the AWS CLI. For more information about the values mentioned in this tutorial like sampled end
time and start time, see [View IP address history](view-history-cidr-ipam.md "view-history-cidr-ipam.md").

###### Scenario 1: Which resources were associated with `10.2.1.155/32`

between 1:00 AM and 9:00 PM on December 27, 2021 (UTC)?

1. Run the following command:

```
aws ec2 get-ipam-address-history --region `us-east-1` --cidr `10.2.1.155/32` --ipam-scope-id `ipam-scope-05b579a1909c5fc7a` --start-time `2021-12-20T01:00:00.000Z` --end-time `2021-12-27T21:00:00.000Z`
```

2. View the results of the analysis. In the example below, the CIDR was allocated to a network
   interface and EC2 instance over the course of the time period. Note that no
   **SampledEndTime** value means the record is still active. For
   more information about the values shown in the following output, see [View IP address history](view-history-cidr-ipam.md "view-history-cidr-ipam.md").

```
{
    "HistoryRecords": [
        {
            "ResourceOwnerId": "123456789012",
            "ResourceRegion": "us-east-1",
            "ResourceType": "network-interface",
            "ResourceId": "eni-0b4e53eb1733aba16",
            "ResourceCidr": "10.2.1.155/32",
            "VpcId": "vpc-0f5ee7e1ba908a378",
            "SampledStartTime": "2021-12-27T20:08:46.672000+00:00"
        },
        {
            "ResourceOwnerId": "123456789012",
            "ResourceRegion": "us-east-1",
            "ResourceType": "instance",
            "ResourceId": "i-064da1f79baed14f3",
            "ResourceCidr": "10.2.1.155/32",
            "VpcId": "vpc-0f5ee7e1ba908a378",
            "SampledStartTime": "2021-12-27T20:08:46.672000+00:00"
        }
    ]
}
```

If the owner ID of the instance to which a network interface is attached
differs from the owner ID of the network interface (as is the case for NAT
gateways, Lambda network interfaces in VPCs, and other AWS services), the
`ResourceOwnerId` is `amazon-aws` rather than the
account ID of the owner of the network interface. The following example shows
the record for a CIDR associated with a NAT gateway:

```
{
    "HistoryRecords": [
        {
            "ResourceOwnerId": "123456789012",
            "ResourceRegion": "us-east-1",
            "ResourceType": "network-interface",
            "ResourceId": "eni-0b4e53eb1733aba16",
            "ResourceCidr": "10.0.0.176/32",
            "VpcId": "vpc-0f5ee7e1ba908a378",
            "SampledStartTime": "2021-12-27T20:08:46.672000+00:00"
        },
        {
            "ResourceOwnerId": "amazon-aws",
            "ResourceRegion": "us-east-1",
            "ResourceType": "instance",
            "ResourceCidr": "10.0.0.176/32",
            "VpcId": "vpc-0f5ee7e1ba908a378",
            "SampledStartTime": "2021-12-27T20:08:46.672000+00:00"
        }
    ]
}
```

###### Scenario 2: Which resources were associated with `10.2.1.0/24` from

December 1, 2021 to December 27, 2021 (UTC)?

1. Run the following command:

```
aws ec2 get-ipam-address-history --region `us-east-1` --cidr `10.2.1.0/24` --ipam-scope-id `ipam-scope-05b579a1909c5fc7a` --start-time `2021-12-01T00:00:00.000Z` --end-time `2021-12-27T23:59:59.000Z`
```

2. View the results of the analysis. In the example below, the CIDR was allocated to a subnet and
   VPC over the course of the time period. Note that no **SampledEndTime** value means the record is still active.
   For more information about the values shown in the
   following output, see [View IP address history](view-history-cidr-ipam.md "view-history-cidr-ipam.md").

```
{
    "HistoryRecords": [
        {
            "ResourceOwnerId": "123456789012",
            "ResourceRegion": "us-east-1",
            "ResourceType": "subnet",
            "ResourceId": "subnet-0864c82a42f5bffed",
            "ResourceCidr": "10.2.1.0/24",
            "VpcId": "vpc-0f5ee7e1ba908a378",
            "SampledStartTime": "2021-12-27T20:08:46.672000+00:00"
        },
        {
            "ResourceOwnerId": "123456789012",
            "ResourceRegion": "us-east-1",
            "ResourceType": "vpc",
            "ResourceId": "vpc-0f5ee7e1ba908a378",
            "ResourceCidr": "10.2.1.0/24",
            "ResourceComplianceStatus": "compliant",
            "ResourceOverlapStatus": "nonoverlapping",
            "VpcId": "vpc-0f5ee7e1ba908a378",
            "SampledStartTime": "2021-12-27T20:08:46.672000+00:00"
        }
    ]
}
```

###### Scenario 3: Which resources were associated with `2605:9cc0:409::/56`

from December 1, 2021 to December 27, 2021 (UTC)?

1. Run the following command, where --region is the IPAM home Region:

```
aws ec2 get-ipam-address-history --region `us-east-1` --cidr `2605:9cc0:409::/56` --ipam-scope-id `ipam-scope-07cb485c8b4a4d7cc` --start-time `2021-12-01T01:00:00.000Z` --end-time `2021-12-27T23:59:59.000Z`
```

2. View the results of the analysis. In the example below, the CIDR was allocated to two
   different VPCs over the course of the time period in a Region outside the IPAM
   home Region. Note that no **SampledEndTime** value means the
   record is still active. For more information about the values shown in the
   following output, see [View IP address history](view-history-cidr-ipam.md "view-history-cidr-ipam.md").

```
{
    "HistoryRecords": [
        {
            "ResourceOwnerId": "123456789012",
            "ResourceRegion": "us-east-2",
            "ResourceType": "vpc",
            "ResourceId": "vpc-01d967bf3b923f72c",
            "ResourceCidr": "2605:9cc0:409::/56",
            "ResourceName": "First example VPC",
            "ResourceComplianceStatus": "compliant",
            "ResourceOverlapStatus": "nonoverlapping",
            "VpcId": "vpc-01d967bf3b923f72c",
            "SampledStartTime": "2021-12-23T20:02:00.701000+00:00",
            "SampledEndTime": "2021-12-23T20:12:59.848000+00:00"
        },
        {
            "ResourceOwnerId": "123456789012",
            "ResourceRegion": "us-east-2",
            "ResourceType": "vpc",
            "ResourceId": "vpc-03e62c7eca81cb652",
            "ResourceCidr": "2605:9cc0:409::/56",
            "ResourceName": "Second example VPC",
            "ResourceComplianceStatus": "compliant",
            "ResourceOverlapStatus": "nonoverlapping",
            "VpcId": "vpc-03e62c7eca81cb652",
            "SampledStartTime": "2021-12-27T15:11:00.046000+00:00"
        }
    ]
}
```

###### Scenario 4: Which resources were associated with `10.0.0.0/24` in the

last 24 hours (assuming the current time is midnight on December 27, 2021
(UTC))?

1. Run the following command:

```
aws ec2 get-ipam-address-history --region `us-east-1` --cidr `10.0.0.0/24` --ipam-scope-id `ipam-scope-05b579a1909c5fc7a` --start-time `2021-12-27T00:00:00.000Z`
```

2. View the results of the analysis. In the example below, the CIDR has been
   allocated to numerous subnets and VPCs over the time period. Note that no
   **SampledEndTime** value means the record is still active. For
   more information about the values shown in the following output, see [View IP address history](view-history-cidr-ipam.md "view-history-cidr-ipam.md").

```
{
    "HistoryRecords": [
        {
            "ResourceOwnerId": "123456789012",
            "ResourceRegion": "us-east-2",
            "ResourceType": "subnet",
            "ResourceId": "subnet-0d1b8f899725aa72d",
            "ResourceCidr": "10.0.0.0/24",
            "ResourceName": "Example name",
            "VpcId": "vpc-042b8a44f64267d67",
            "SampledStartTime": "2021-12-11T16:35:59.074000+00:00",
            "SampledEndTime": "2021-12-28T15:34:00.017000+00:00"
        },
        {
            "ResourceOwnerId": "123456789012",
            "ResourceRegion": "us-east-2",
            "ResourceType": "vpc",
            "ResourceId": "vpc-09754dfd85911abec",
            "ResourceCidr": "10.0.0.0/24",
            "ResourceName": "Example name",
            "ResourceComplianceStatus": "unmanaged",
            "ResourceOverlapStatus": "overlapping",
            "VpcId": "vpc-09754dfd85911abec",
            "SampledStartTime": "2021-12-27T20:07:59.947000+00:00",
            "SampledEndTime": "2021-12-28T15:34:00.017000+00:00"
        },
        {
            "ResourceOwnerId": "123456789012",
            "ResourceRegion": "us-west-2",
            "ResourceType": "vpc",
            "ResourceId": "vpc-0a8347f594bea5901",
            "ResourceCidr": "10.0.0.0/24",
            "ResourceName": "Example name",
            "ResourceComplianceStatus": "unmanaged",
            "ResourceOverlapStatus": "overlapping",
            "VpcId": "vpc-0a8347f594bea5901",
            "SampledStartTime": "2021-12-11T16:35:59.318000+00:00"
        },
        {
            "ResourceOwnerId": "123456789012",
            "ResourceRegion": "us-east-1",
            "ResourceType": "subnet",
            "ResourceId": "subnet-0af7eadb0798e9148",
            "ResourceCidr": "10.0.0.0/24",
            "ResourceName": "Example name",
            "VpcId": "vpc-03298ba16756a8736",
            "SampledStartTime": "2021-12-14T21:07:22.357000+00:00"
        }
    ]
}
```

###### Scenario 5: Which resources are currently associated with `10.2.1.155/32`?

1. Run the following command:

```
aws ec2 get-ipam-address-history --region `us-east-1` --cidr `10.2.1.155/32` --ipam-scope-id `ipam-scope-05b579a1909c5fc7a`
```

2. View the results of the analysis. In the example below, the CIDR was allocated
   to a network interface and EC2 instance over the time period. Note that no
   **SampledEndTime** value means the record is still active. For
   more information about the values shown in the following output, see [View IP address history](view-history-cidr-ipam.md "view-history-cidr-ipam.md").

```
{
    "HistoryRecords": [
        {
            "ResourceOwnerId": "123456789012",
            "ResourceRegion": "us-east-1",
            "ResourceType": "network-interface",
            "ResourceId": "eni-0b4e53eb1733aba16",
            "ResourceCidr": "10.2.1.155/32",
            "VpcId": "vpc-0f5ee7e1ba908a378",
            "SampledStartTime": "2021-12-27T20:08:46.672000+00:00"
        },
        {
            "ResourceOwnerId": "123456789012",
            "ResourceRegion": "us-east-1",
            "ResourceType": "instance",
            "ResourceId": "i-064da1f79baed14f3",
            "ResourceCidr": "10.2.1.155/32",
            "VpcId": "vpc-0f5ee7e1ba908a378",
            "SampledStartTime": "2021-12-27T20:08:46.672000+00:00"
        }
    ]
}
```

###### Scenario 6: Which resources are currently associated with `10.2.1.0/24`?

1. Run the following command:

```
aws ec2 get-ipam-address-history --region `us-east-1` --cidr `10.2.1.0/24` --ipam-scope-id `ipam-scope-05b579a1909c5fc7a`
```

2. View the results of the analysis. In the example below, the CIDR was allocated
   to a VPC and subnet over the time period. Only the results that match this exact
   `/24` CIDR are returned, not all `/32` within the
   `/24` CIDR. Note that no **SampledEndTime**
   value means the record is still active. For more information about the values shown in
   the following output, see [View IP address history](view-history-cidr-ipam.md "view-history-cidr-ipam.md").

```
{
    "HistoryRecords": [
        {
            "ResourceOwnerId": "123456789012",
            "ResourceRegion": "us-east-1",
            "ResourceType": "subnet",
            "ResourceId": "subnet-0864c82a42f5bffed",
            "ResourceCidr": "10.2.1.0/24",
            "VpcId": "vpc-0f5ee7e1ba908a378",
            "SampledStartTime": "2021-12-27T20:08:46.672000+00:00"
        },
        {
            "ResourceOwnerId": "123456789012",
            "ResourceRegion": "us-east-1",
            "ResourceType": "vpc",
            "ResourceId": "vpc-0f5ee7e1ba908a378",
            "ResourceCidr": "10.2.1.0/24",
            "ResourceComplianceStatus": "compliant",
            "ResourceOverlapStatus": "nonoverlapping",
            "VpcId": "vpc-0f5ee7e1ba908a378",
            "SampledStartTime": "2021-12-27T20:08:46.672000+00:00"
        }
    ]
}
```

###### Scenario 7: Which resources are currently associated with `54.0.0.9/32`?

In this example, `54.0.0.9/32` is assigned to an Elastic IP address that is not part of the AWS Organization integrated with your IPAM.

1. Run the following command:

```
aws ec2 get-ipam-address-history --region `us-east-1` --cidr `54.0.0.9/32` --ipam-scope-id `ipam-scope-05b579a1909c5fc7a`
```

2. Since `54.0.0.9/32` is assigned to an Elastic IP address that is
   not part of the AWS Organization integrated with the IPAM in this example, no
   records are returned.

```
{
    "HistoryRecords": []
}
```
