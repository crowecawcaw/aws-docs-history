# Prerequisites for Amazon EC2 instance topology

Before you describe the instance topology for your instances, ensure that your instances
meet the following requirements.

###### Requirements to describe the topology of your instances

- [AWS Regions](#inst-net-topology-prereqs-regions "#inst-net-topology-prereqs-regions")
- [Instance types](#inst-net-topology-prereqs-instance-types "#inst-net-topology-prereqs-instance-types")
- [Instance state](#inst-net-topology-prereqs-instance-state "#inst-net-topology-prereqs-instance-state")
- [IAM permission](#ec2-instance-topology-iam-permissions "#ec2-instance-topology-iam-permissions")

## AWS Regions

Supported AWS Regions:

- US East (N. Virginia), US East (Ohio), US West (N. California),
  US West (Oregon)
- Asia Pacific (Melbourne), Asia Pacific (Mumbai), Asia Pacific (Seoul),
  Asia Pacific (Singapore), Asia Pacific (Sydney),
  Asia Pacific (Tokyo)
- Canada (Central)
- Europe (Frankfurt), Europe (Ireland), Europe (London),
  Europe (Paris), Europe (Spain), Europe (Stockholm)
- Israel (Tel Aviv)
- South America (São Paulo)
- AWS GovCloud (US-West)

## Instance types

Supported instance types:

- Returns 3 network nodes in the response
  - `hpc6a.48xlarge` | `hpc6id.32xlarge` |
    `hpc7a.12xlarge` | `hpc7a.24xlarge` |
    `hpc7a.48xlarge` | `hpc7a.96xlarge` |
    `hpc7g.4xlarge` | `hpc7g.8xlarge` |
    `hpc7g.16xlarge`
  - `p3dn.24xlarge` | `p4d.24xlarge` |
    `p4de.24xlarge` | `p5.48xlarge` |
    `p5e.48xlarge` | `p5en.48xlarge` |
    `p6e-gb200.36xlarge`
  - `trn1.2xlarge` | `trn1.32xlarge` |
    `trn1n.32xlarge` | `trn2.48xlarge` |
    `trn2u.48xlarge`

- Returns 4 network nodes in the response
  - `p6-b200.48xlarge`

The available instance types vary by Region. For more information, see
[Amazon EC2 instance types by Region](../../../ec2/latest/instancetypes/ec2-instance-regions.md "../../../ec2/latest/instancetypes/ec2-instance-regions.md").

## Instance state

Instances must be in the `running` state. You can’t get instance
topology information for instances that are in another state.

## IAM permission

Your IAM identity (user, user group, or role) requires the following IAM
permission:

- `ec2:DescribeInstanceTopology`
