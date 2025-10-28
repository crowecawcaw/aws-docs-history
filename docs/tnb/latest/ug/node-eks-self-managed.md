# AWS.Compute.EKSSelfManagedNode

AWS TNB supports Amazon EKS self-managed nodes to automate the provisioning and lifecycle
management of nodes (Amazon EC2 instances) for Amazon EKS Kubernetes clusters. To create an Amazon EKS
node group, do the following:

- Choose the Amazon Machine Images (AMI) for your cluster workers nodes by providing
  either the ID of the AMI.
- Provide an Amazon EC2 key pair for SSH access.
- Ensure that your node group is associated with an Amazon EKS cluster.
- Provide the instance type and desired, minimum, and maximum sizes.
- Provide the subnets for the worker nodes.
- Optionally, attach security groups, node labels, and a placement group to your
  node group.

## Syntax

```
tosca.nodes.AWS.Compute.EKSSelfManagedNode:
  capabilities:
    compute:
      properties:
        ami_id: String
        instance_type: String
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

###### `*compute*`

Properties that define the computing parameters for the Amazon EKS self-managed nodes,
such as, Amazon EC2 instance types and Amazon EC2 instance AMIs.

`ami_id`

The AMI ID used to launch the instance. AWS TNB supports instances that
leverage IMDSv2. For more information, see [IMDS version](imds-version.md "imds-version.md").

###### Note

You can update the AMI ID for `EKSSelfManagedNode`. The Amazon EKS
version of the AMI must be the same as or up to 2 versions lower than the
Amazon EKS cluster version. For example if the Amazon EKS cluster version is 1.31,
then the Amazon EKS AMI version must be 1.31, 1.30, or 1.29.

Required: Yes

Type: String

`instance_type`

The instance size.

Required: Yes

Type: String

`key_pair`

The Amazon EC2 key pair to enable SSH access.

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
AWS TNB uses AWS Managed Services to encrypt the root volume.

- AWS TNB does not decrypt an encrypted AMI.

`root_volume_size`

The size of the Amazon Elastic Block Store root volume in GiBs.

Required: No

Default: 20

Type: Integer

Possible values: 1 to 16,384

###### `*scaling*`

Properties that define the scaling parameters for the Amazon EKS self-managed nodes,
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

The tags to be attached to the resource. Tags will be propagated to the
instances created by the resource.

Required: No

Type: List

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
AWS TNB obtains the permission related to ENIs from the [node_role](#node_eks_self_managed_node_role "#node_eks_self_managed_node_role") property.

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
script is passed to the Amazon EC2 instances launched by the self-managed node
group. Add the permissions required for executing custom user data to the
node_role passed to the node group.

Required: No

Type: String

`labels`

A list of node labels. A node label must have a name and a value. Create a
label using the following criteria:

- The name and value must be separated by `=`.
- The name and value can each be up to 63 characters in length.
- The label can include letters (A-Z, a-z,), numbers (0-9), and the
  following characters: `[-, _, ., *, ?]`
- The name and value must start and end with an alphanumeric,
  `?`, or `*` character.

For example, `myLabelName1=*NodeLabelValue1`

Required: No

Type: List

## Example

```
SampleEKSSelfManagedNode:
  type: tosca.nodes.AWS.Compute.EKSSelfManagedNode
  capabilities:
    compute:
      properties:
        ami_id: "ami-123123EXAMPLE"
        instance_type: "c5.large"
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
    node_role: "arn:aws:iam::${AWS::TNB::AccountId}:role/`SampleNodeRole`"
    tags:
      - "Name=SampleVPC"
      - "Environment=Testing"
  requirements:
    cluster: SampleEKSCluster
    subnets:
      - SampleSubnet
    network_interfaces:
      - SampleNetworkInterface01
      - SampleNetworkInterface02
    security_groups:
      - SampleSecurityGroup01
      - SampleSecurityGroup02
    placement_group: SamplePlacementGroup
    user_data: CustomUserData
    labels:
      - "sampleLabelName001=sampleLabelValue001"
      - "sampleLabelName002=sampleLabelValue002"
```
