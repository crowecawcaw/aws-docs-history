# Prerequisites for Amazon EC2

topology

To describe your Amazon EC2 topology, ensure that your instances and Capacity Reservations meet the
following prerequisites.

###### Prerequisites for:

- [AWS Regions](#inst-net-topology-prereqs-regions "#inst-net-topology-prereqs-regions")
- [Instance types](#inst-net-topology-prereqs-instance-types "#inst-net-topology-prereqs-instance-types")
- [State](#inst-net-topology-prereqs-instance-state "#inst-net-topology-prereqs-instance-state")
- [IAM permissions](#ec2-instance-topology-iam-permissions "#ec2-instance-topology-iam-permissions")

## AWS Regions

Supported AWS Regions:

- US East (N. Virginia), US East (Ohio), US West (N. California),
  US West (Oregon)
- Africa (Cape Town)
- Asia Pacific (Jakarta), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad),
  Asia Pacific (Melbourne), Asia Pacific (Mumbai), Asia Pacific (Osaka),
  Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney),
  Asia Pacific (Tokyo)
- Canada (Central)
- Europe (Frankfurt), Europe (Ireland), Europe (London),
  Europe (Paris), Europe (Spain), Europe (Stockholm),
  Europe (Zurich)
- Israel (Tel Aviv)
- Middle East (Bahrain), Middle East (UAE)
- South America (São Paulo)
- AWS GovCloud (US-West)

The DescribeCapacityReservationTopology API is not supported in
Israel (Tel Aviv) and AWS GovCloud (US-West).

## Instance types

Supported instance types:

- Returns **3\* network nodes** in the response:
  - `g6e.xlarge` | `g6e.2xlarge` | `g6e.4xlarge` | `g6e.8xlarge` | `g6e.12xlarge` | `g6e.16xlarge` | `g6e.24xlarge` | `g6e.48xlarge` | `g7e.2xlarge` | `g7e.4xlarge` | `g7e.8xlarge` | `g7e.12xlarge` | `g7e.24xlarge` | `g7e.48xlarge`
  - `hpc6a.48xlarge` | `hpc6id.32xlarge` | `hpc7g.4xlarge` | `hpc7g.8xlarge` | `hpc7g.16xlarge` | `hpc7a.12xlarge` | `hpc7a.24xlarge` | `hpc7a.48xlarge` | `hpc7a.96xlarge`
  - `p3dn.24xlarge` | `p4d.24xlarge` | `p4de.24xlarge` | `p5.48xlarge` | `p5e.48xlarge` | `p5en.48xlarge` | `p6e-gb200.36xlarge`
  - `trn1.2xlarge` | `trn1.32xlarge` | `trn1n.32xlarge` | `trn2.48xlarge` | `trn2u.48xlarge`

- Returns **4\* network nodes** in the response:
  - `p6-b200.48xlarge` | `p6-b300.48xlarge`

\* The number of network nodes returned is only applicable when using the
DescribeInstanceTopology API. For the DescribeCapacityReservationTopology API, the
number of network nodes returned will vary depending on the type and state of the
Capacity Reservation.

The available instance types vary by Region. For more information, see [Amazon EC2 instance types by
Region](../../../ec2/latest/instancetypes/ec2-instance-regions.md "../../../ec2/latest/instancetypes/ec2-instance-regions.md").

## State

- For `DescribeInstanceTopology` – Instances must be
  in the `running` state.
- For `DescribeCapacityReservationTopology` – Capacity Reservations
  must be in the `pending` or `active` state.

You can’t get topology information for instances or Capacity Reservations in any other
state.

## IAM permissions

Your IAM identity (user, user group, or role) requires the following
permissions:

- `ec2:DescribeInstanceTopology`
- `ec2:DescribeCapacityReservationTopology`
