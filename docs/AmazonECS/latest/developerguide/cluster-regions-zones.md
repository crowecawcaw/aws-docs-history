# Amazon ECS applications in shared subnets, Local Zones, and Wavelength Zones

Amazon ECS supports workloads that use Local Zones, Wavelength Zones, and AWS Outposts for when low
latency or local data processing is a requirement.

- You can use Local Zones as an extension of an AWS Region to place resources
  in multiple locations closer to your end users.
- You can use Wavelength Zones to build applications that deliver ultra-low
  latencies to 5G devices and end users. Wavelength deploys standard AWS compute and
  storage services to the edge of telecommunication carriers' 5G networks.
- AWS Outposts brings native AWS services, infrastructure, and operating models to
  virtually any data center, co-location space, or on-premises facility.

###### Important

Amazon ECS on AWS Fargate workloads aren't supported in Local Zones, Wavelength Zones, or
on AWS Outposts at this time.

For information about the differences between Local Zones, Wavelength Zones, and AWS Outposts ,
see [How should I think about when to use
AWS Wavelength, AWS Local Zones, or AWS Outposts for applications requiring low latency or
local data processing](https://aws.amazon.com/wavelength/faqs/ "https://aws.amazon.com/wavelength/faqs/") in the AWS Wavelength FAQs.

## Shared subnets

You can use _VPC sharing_ to share subnets with other AWS
accounts within the same AWS Organizations.

You can use shared VPCs for EC2 with the following
considerations:

- The owner of the VPC subnet must share a subnet with a participant account
  before that account can use it for Amazon ECS resources.
- You can't use the VPC default security group for your container instances
  because it belongs to the owner. Additionally, participants can't launch
  instances using security groups that are owned by other participants or the
  owner.
- In a shared subnet, the participant and the owner separately controls the
  security groups within each respective account. The subnet owner can see
  security groups that are created by the participants but cannot perform any
  actions on them. If the subnet owner wants to remove or modify these security
  groups, the participant that created the security group must take the
  action.
- The shared VPC owner cannot view, update or delete a cluster that a
  participant creates in the shared subnet. This is in addition to the VPC
  resources that each account has different access to. For more information, see
  [Responsibilities and permissions for owners and participants](../../../vpc/latest/userguide/vpc-sharing.md#vpc-share-limitations "../../../vpc/latest/userguide/vpc-sharing.md#vpc-share-limitations") in the
  _Amazon VPC User Guide_.

You can use shared VPCs for Fargate with the following
considerations::

- The owner of the VPC subnet must share a subnet with a participant account
  before that account can use it for Amazon ECS resources.
- You can't create a service or run a task using the default security group for
  the VPC because it belongs to the owner. Additionally, participants can't create
  a service or run a task using security groups that are owned by other
  participants or the owner.
- In a shared subnet, the participant and the owner separately controls the
  security groups within each respective account. The subnet owner can see
  security groups that are created by the participants but cannot perform any
  actions on them. If the subnet owner wants to remove or modify these security
  groups, the participant that created the security group must take the
  action.
- The shared VPC owner cannot view, update or delete a cluster that a
  participant creates in the shared subnet. This is in addition to the VPC
  resources that each account has different access to. For more information, see
  [Responsibilities and permissions for owners and participants](../../../vpc/latest/userguide/vpc-sharing.md#vpc-share-limitations "../../../vpc/latest/userguide/vpc-sharing.md#vpc-share-limitations") in the
  _Amazon VPC User Guide_.

For more information about VPC subnet sharing, see [Share your VPC with other
accounts](../../../vpc/latest/userguide/vpc-sharing.md#vpc-share-limitations "../../../vpc/latest/userguide/vpc-sharing.md#vpc-share-limitations") in the _Amazon VPC User Guide_.

## Local Zones

A _Local Zone_ is an extension of an AWS Region in close
geographic proximity to your users. Local Zones have their own connections to the
internet and support Direct Connect. Resources that are created in a Local Zone can serve
local users with low-latency communications. For more information, see [AWS Local
Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/ "https://aws.amazon.com/about-aws/global-infrastructure/localzones/").

A Local Zone is represented by a Region code followed by an identifier that indicates
the location (for example, `us-west-2-lax-1a`).

To use a Local Zone, you must opt in to the zone. After you opt in, you must create an
Amazon VPC and subnet in the Local Zone.

You can launch Amazon EC2 instances, Amazon FSx file servers, and Application Load Balancers to use for your Amazon ECS
clusters and tasks.

For more information, see [What is AWS Local Zones?](../../../local-zones/latest/ug/what-is-aws-local-zones.md "../../../local-zones/latest/ug/what-is-aws-local-zones.md") in the _AWS Local Zones User Guide_.

## Wavelength Zones

You can use _AWS Wavelength_ to build applications that deliver
ultra-low latency to mobile devices and end users. Wavelength deploys standard AWS compute
and storage services to the edge of telecommunication carriers' 5G networks. You can
extend an Amazon Virtual Private Cloud to one or more Wavelength Zones. Then, you can use AWS resources such
as Amazon EC2 instances to run applications that require ultra-low latency and a connection
to AWS services in the Region.

A Wavelength Zone is an isolated Zone in the carrier location where the Wavelength
infrastructure is deployed. Wavelength Zones are tied to an AWS Region. A Wavelength Zone is a
logical extension of a Region, and is managed by the control plane in the Region.

A Wavelength Zone is represented by a Region code followed by an identifier that indicates
the Wavelength Zone (for example, `us-east-1-wl1-bos-wlz-1`).

To use a Wavelength Zone, you must opt in to the Zone. After you opt in, you must create
an Amazon VPC and subnet in the Wavelength Zone. Then, you can launch your Amazon EC2 instances in the
Zone to use for your Amazon ECS clusters and tasks.

For more information, see [Get started with
AWS Wavelength](../../../wavelength/latest/developerguide/get-started-wavelength.md "../../../wavelength/latest/developerguide/get-started-wavelength.md") in the _AWS Wavelength Developer Guide_.

Wavelength Zones aren't available in all AWS Regions. For information about the Regions
that support Wavelength Zones, see [Available
Wavelength Zones](../../../wavelength/latest/developerguide/available-wavelength-zones.md "../../../wavelength/latest/developerguide/available-wavelength-zones.md") in the _AWS Wavelength Developer Guide_.
