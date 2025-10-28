# AWS.Compute.EKSManagedNode

AWS TNB supports EKS Managed Node groups to automate the provisioning and lifecycle
management of nodes (Amazon EC2 instances) for Amazon EKS Kubernetes clusters. To create an EKS Node
group, do the following:

- Choose the Amazon Machine Images (AMI) for your cluster workers nodes by providing
  either the ID of the AMI or the AMI type.
- Provide an Amazon EC2 key pair for SSH access and the scaling properties for your node
  group.
- Ensure that your node group is associated with an Amazon EKS cluster.
- Provide the subnets for the worker nodes.
- Optionally, attach security groups, node labels, and a placement group to your
  node group.

## Syntax

```
tosca.nodes.AWS.Compute.EKSManagedNode:
  capabilities:
    compute:
      properties:
        ami_type: String
        ami_id: String
        instance_types: List
        key_pair: String
        root_volume_encryption: Boolean
        root_volume_encryption_key_arn: String
        root_volume_size: Integer
    scaling:
      properties:
        desired_size: Integer
        min_size: Integer
        max_size: Integer
  properties:
    node_role: String
    tags: List
    kubernetes_version: String
  requirements:
    cluster: String
    subnets: List
    network_interfaces: List
    security_groups: List
    placement_group: String
    user_data: String
    labels: List
```

## Capabilities

###### `compute`

Properties that define the computing parameters for the Amazon EKS managed node group,
such as, Amazon EC2 instance types and Amazon EC2 instance AMIs.

`ami_type`

The Amazon EKS-supported AMI type.

Required: Yes

Type: String

Possible values: `AL2_x86_64` | `AL2_x86_64_GPU` |
`AL2_ARM_64` | `AL2023_x86_64` |
`AL2023_ARM_64` | `AL2023_x86_64_NVIDIA` |
`AL2023_x86_64_NEURON` | `CUSTOM` |
`BOTTLEROCKET_ARM_64` | `BOTTLEROCKET_x86_64` |
`BOTTLEROCKET_ARM_64_NVIDIA` |
`BOTTLEROCKET_x86_64_NVIDIA`

`ami_id`

The ID of the AMI.

Required: No

Type: String

###### Note

If both `ami_type` and `ami_id` are specified in
the template, AWS TNB will use only the `ami_id` value to
create `EKSManagedNode`.

`instance_types`

The instance size.

Required: Yes

Type: List

`key_pair`

The EC2 Key pair to enable SSH access.

Required: Yes

Type: String

`root_volume_encryption`

Enables Amazon EBS encryption for the Amazon EBS root volume. If this property is not
provided, AWS TNB encrypts Amazon EBS root volumes by default.

Required: No

Default: true

Type: Boolean

`root_volume_encryption_key_arn`

The ARN of the AWS KMS key. AWS TNB supports regular key ARN, multi-region
key ARN and alias ARN.

Required: No

Type: String

###### Note

- If `root_volume_encryption` is false, do not include
  `root_volume_encryption_key_arn`.
- AWS TNB supports root volume encryption of Amazon EBS-backed
  AMI’s.
- If the AMI's root volume is already encrypted, you must include the
  `root_volume_encryption_key_arn` for AWS TNB to
  re-encrypt the root volume.
- If the AMI's root volume is not encrypted, AWS TNB uses the
  `root_volume_encryption_key_arn` to encrypt the root
  volume.

If you do not include `root_volume_encryption_key_arn`,
AWS TNB uses the default key provided by AWS Key Management Service to encrypt the
root volume.

- AWS TNB does not decrypt an encrypted AMI.

`root_volume_size`

The size of the Amazon Elastic Block Store root volume in GiBs.

Required: No

Default: 20

Type: Integer

Possible values: 1 to 16,384

###### `scaling`

Properties that define the scaling parameters for the Amazon EKS managed node group,
such as, the desired number of Amazon EC2 instances, and minimum and maximum number of
Amazon EC2 instances in the node group.

`desired_size`

The number of instances in this NodeGroup.

Required: Yes

Type: Integer

`min_size`

The minimum number of instances in this NodeGroup.

Required: Yes

Type: Integer

`max_size`

The maximum number of instances in this NodeGroup.

Required: Yes

Type: Integer

## Properties

`node_role`

The ARN of the IAM role that is attached to the Amazon EC2 instance.

Required: Yes

Type: String

`tags`

The tags to be attached to the resource.

Required: No

Type: List

`kubernetes_version`

The Kubernetes version for the Managed Node group. AWS TNB supports
Kubernetes versions 1.25 through 1.32. Consider the following:

- Specify either the `kubernetes_version` or
  `ami_id`. Do not specify both.
- The `kubernetes_version` must be less than or equal to the
  AWS.Compute.EKSManagedNode version.
- There can be a difference of 3 versions between the
  AWS.Compute.EKSManagedNode version and
  `kubernetes_version`.
- If neither the `kubernetes_version` or `ami_id`
  are specified, AWS TNB will use the latest AMI of the
  `AWS.Compute.EKSManagedNode` version to create
  `EKSManagedNode`

Required: No

Type: String

Possible values: 1.25 | 1.26 | 1.27 | 1.28 | 1.29 | 1.30 | 1.31 | 1.32

## Requirements

`cluster`

An [AWS.Compute.EKS](node-eks.md "node-eks.md") node.

Required: Yes

Type: String

`subnets`

An [AWS.Networking.Subnet](node-subnet.md "node-subnet.md") node.

Required: Yes

Type: List

`network_interfaces`

An [AWS.Networking.ENI](node-eni.md "node-eni.md") node. Ensure that
the network interfaces and subnets are set to the same Availability Zone or
instantiation will fail.

When you set `network_interfaces`, AWS TNB obtains the
permission related to ENIs from the `multus_role` property if you
included the `multus` property in the [AWS.Compute.EKS](node-eks.md "node-eks.md") node. Otherwise,
AWS TNB obtains the permission related to ENIs from the [node_role](#node_eks_managed_node_node_role "#node_eks_managed_node_node_role") property.

Required: No

Type: List

`security_groups`

An [AWS.Networking.SecurityGroup](node-networking-security-group.md "node-networking-security-group.md") node.

Required: No

Type: List

`placement_group`

A [tosca.nodes.AWS.Compute.PlacementGroup](node-compute-placement-group.md "node-compute-placement-group.md") node.

Required: No

Type: String

`user_data`

A [tosca.nodes.AWS.Compute.UserData](node-compute-user-data.md "node-compute-user-data.md") node reference. A user data
script is passed to the Amazon EC2 instances launched by the managed node group. Add
the permissions required to run custom user data to the node_role passed to the
node group.

Required: No

Type: String

`labels`

A list of node labels. A node label must have a name and a value. Create a
label using the following criteria:

- The name and value must be separated by `=`.
- The name and value can each be up to 63 characters in length.
- The label can include letters (A-Z, a-z,), numbers (0-9) and the
  following characters: `[-, _, ., *, ?]`
- The name and value must start and end with an alphanumeric,
  `?`, or `*` character.

For example, `myLabelName1=*NodeLabelValue1`

Required: No

Type: List

## Example

```
SampleEKSManagedNode:
  type: tosca.nodes.AWS.Compute.EKSManagedNode
  capabilities:
    compute:
      properties:
        ami_type: "AL2_x86_64"
        instance_types:
          - "t3.xlarge"
        key_pair: "SampleKeyPair"
        root_volume_encryption: true
        root_volume_encryption_key_arn: "arn:aws:kms:`us-west-2:111122223333`:key/`1234abcd-12ab-34cd-56ef-1234567890ab`"
        root_volume_size: `1500`
    scaling:
      properties:
        desired_size: 1
        min_size: 1
        max_size: 1
  properties:
    node_role: "arn:aws:iam::${AWS::TNB::AccountId}:role/`SampleRole`"
    tags:
      - "Name=SampleVPC"
      - "Environment=Testing"
    kubernetes_version:
      - "1.30"
  requirements:
    cluster: SampleEKS
    subnets:
      - SampleSubnet
    network_interfaces:
      - SampleENI01
      - SampleENI02
    security_groups:
      - SampleSecurityGroup01
      - SampleSecurityGroup02
    placement_group: SamplePlacementGroup
    user_data: CustomUserData
    labels:
      - "sampleLabelName001=sampleLabelValue001"
      - "sampleLabelName002=sampleLabelValue002"
```
