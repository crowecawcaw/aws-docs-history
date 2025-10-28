# AWS.Compute.EKS

Provide the name of the cluster, the desired Kubernetes version, and a role that allows
the Kubernetes control plane to manage the AWS resources required for your NFs. Multus
container network interface (CNI) plugins are enabled. You can attach multiple network
interfaces and apply advanced network configuration to the Kubernetes-based network
functions. You also specify the cluster endpoint access and the subnets for your
cluster.

## Syntax

```
tosca.nodes.AWS.Compute.EKS:
  capabilities:
    multus:
      properties:
        enabled: Boolean
        multus_role: String
    ebs_csi:
      properties:
        enabled: Boolean
        version: String
  properties:
    version: String
    access: String
    cluster_role: String
    tags: List
    ip_family: String
  requirements:
    subnets: List
```

## Capabilities

###### `multus`

Optional. Properties that define the Multus container network interface (CNI)
usage.

If you include `multus`, specify the `enabled` and
`multus_role` properties.

`enabled`

Indicates whether the default Multus capability is enabled.

Required: Yes

Type: Boolean

`multus_role`

The role for Multus network interface management.

Required: Yes

Type: String

###### `ebs_csi`

Properties that define the Amazon EBS Container Storage Interface (CSI) driver
installed in the Amazon EKS cluster.

Enable this plugin to use Amazon EKS self-managed nodes on AWS Outposts, AWS Local
Zones, or AWS Regions. For more information, see [Amazon Elastic Block Store CSI driver](../../../eks/latest/userguide/ebs-csi.md "../../../eks/latest/userguide/ebs-csi.md") in the
**Amazon EKS User Guide**.

`enabled`

Indicates whether the default Amazon EBS CSI driver is installed.

Required: No

Type: Boolean

`version`

The version of the Amazon EBS CSI driver add-on. The version must match one of
the versions returned by the _DescribeAddonVersions_ action.
For more information, see [DescribeAddonVersions](../../../eks/latest/APIReference/API_DescribeAddonVersions.md "../../../eks/latest/APIReference/API_DescribeAddonVersions.md") in the _Amazon EKS API Reference_

Required: No

Type: String

## Properties

`version`

The Kubernetes version for the cluster. AWS Telco Network Builder supports Kubernetes
versions 1.25 through 1.32.

Required: Yes

Type: String

Possible values: 1.25 | 1.26 | 1.27 | 1.28 | 1.29 | 1.30 |
1.31 | 1.32

`access`

The cluster endpoint access.

Required: Yes

Type: String

Possible values: `PRIVATE` | `PUBLIC` |
`ALL`

`cluster_role`

The role for cluster management.

Required: Yes

Type: String

`tags`

Tags to be attached to the resource.

Required: No

Type: List

`ip_family`

Indicates the IP family for service and pod addresses in the cluster.

Allowed value: `IPv4`, `IPv6`

Default value: `IPv4`

Required: No

Type: String

## Requirements

`subnets`

An [AWS.Networking.Subnet](node-subnet.md "node-subnet.md") node.

Required: Yes

Type: List

## Example

```
SampleEKS:
  type: tosca.nodes.AWS.Compute.EKS
  properties:
    version: "1.26"
    access: "ALL"
    cluster_role: "arn:aws:iam::${AWS::TNB::AccountId}:role/`SampleRole`"
    ip_family: "IPv6"
    tags:
      - "Name=SampleVPC"
      - "Environment=Testing"
  capabilities:
    multus:
      properties:
        enabled: true
        multus_role: "arn:aws:iam::${AWS::TNB::AccountId}:role/`MultusRole`"
    ebs_csi:
      properties:
        enabled: true
        version: "v1.16.0-eksbuild.1"
  requirements:
    subnets:
    - SampleSubnet01
    - SampleSubnet02
```
