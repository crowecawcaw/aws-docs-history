# AWS.Networking.SecurityGroup

AWS TNB supports security groups to automate the provisioning of [Amazon EC2
Security Groups](../../../AWSEC2/latest/UserGuide/ec2-security-groups.md "../../../AWSEC2/latest/UserGuide/ec2-security-groups.md") which you can attach to Amazon EKS Kubernetes cluster node
groups.

## Syntax

```
tosca.nodes.AWS.Networking.SecurityGroup
  properties:
    description: String
    name: String
    tags: List
  requirements:
    vpc: String
```

## Properties

`description`

The description of the security group. You can use up to 255 characters to
describe the group. You can include only letters (A-Z and a-z), numbers (0-9),
spaces, and the following special characters: .\_-:/()#,@[]+=&;{}!$\*

Required: Yes

Type: String

`name`

A name for the security group. You can use up to 255 characters for the
name. You can include only letters (A-Z and a-z), numbers (0-9), spaces, and
the following special characters: .\_-:/()#,@[]+=&;{}!$\*

Required: Yes

Type: String

`tags`

The tags that you can attach to the security group resource.

Required: No

Type: List

## Requirements

`vpc`

An [AWS.Networking.VPC](node-vpc.md "node-vpc.md") node.

Required: Yes

Type: String

## Example

```
SampleSecurityGroup001:
  type: tosca.nodes.AWS.Networking.SecurityGroup
  properties:
        description: `"Sample Security Group for Testing"`
        name: `"SampleSecurityGroup"`
        tags:
          - `"Name=SecurityGroup"`
          - `"Environment=Testing"`
      requirements:
        vpc: `SampleVPC`
```
