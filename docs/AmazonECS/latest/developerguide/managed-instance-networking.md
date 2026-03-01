# Amazon ECS task networking for Amazon ECS Managed Instances

The networking behavior of Amazon ECS tasks running on Amazon ECS Managed Instances is determined by the
_network mode_ specified in the task definition. You must specify a
network mode in the task definition. You will not be able to run tasks on Amazon ECS Managed Instances
using a task definition that doesn't specify a network mode. Amazon ECS Managed Instances supports the
following networking modes, ensuring backward compatibility for migrating workloads from
Fargate or Amazon ECS on Amazon EC2:

| Network mode | Description                                                                                                                                                                                                                                                   |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `awsvpc`     | Each task receives its own elastic network interface (ENI) and private<br>IPv4 address. This provides the same networking properties as Amazon EC2<br>instances and is compatible with traditional Fargate tasks. Uses ENI<br>trunking for high task density. |
| `host`       | Tasks share the host's network namespace directly. Container<br>networking is tied to the underlying host instance.                                                                                                                                           |

## Using a VPC in IPv6-only mode

In an IPv6-only configuration, your Amazon ECS tasks communicate exclusively over IPv6. To
set up VPCs and subnets for an IPv6-only configuration, you must add an IPv6 CIDR block
to the VPC and create subnets that include only an IPv6 CIDR block. For more information
see [Add
IPv6 support for your VPC](../../../vpc/latest/userguide/vpc-migrate-ipv6-add.md "../../../vpc/latest/userguide/vpc-migrate-ipv6-add.md") and [Create a subnet](../../../vpc/latest/userguide/create-subnets.md "../../../vpc/latest/userguide/create-subnets.md") in the
_Amazon VPC User Guide_. You must also update route tables with IPv6
targets and configure security groups with IPv6 rules. For more information, see [Configure
route tables](../../../vpc/latest/userguide/VPC_Route_Tables.md "../../../vpc/latest/userguide/VPC_Route_Tables.md") and [Configure security
group rules](../../../vpc/latest/userguide/working-with-security-group-rules.md "../../../vpc/latest/userguide/working-with-security-group-rules.md") in the _Amazon VPC User Guide_.

The following considerations apply:

- You can update an IPv4-only or dualstack Amazon ECS service to an IPv6-only
  configuration by either updating the service directly to use IPv6-only subnets
  or by creating a parallel IPv6-only service and using Amazon ECS blue-green
  deployments to shift traffic to the new service. For more information about
  Amazon ECS blue-green deployments, see [Amazon ECS blue/green deployments](deployment-type-blue-green.md "deployment-type-blue-green.md").
- An IPv6-only Amazon ECS service must use dualstack load balancers with IPv6 target groups. If you're
  migrating an existing Amazon ECS service that's behind a Application Load Balancer or a Network Load Balancer, you can
  create a new dualstack load balancer and shift traffic from the old load
  balancer, or update the IP address type of the existing load balancer.

For more
information about Network Load Balancers, see [Create a Network Load Balancer](../../../elasticloadbalancing/latest/network/create-network-load-balancer.md "../../../elasticloadbalancing/latest/network/create-network-load-balancer.md") and
[Update the IP address types for your Network Load Balancer](../../../elasticloadbalancing/latest/network/load-balancer-ip-address-type.md "../../../elasticloadbalancing/latest/network/load-balancer-ip-address-type.md") in the _User Guide for Network Load Balancers_. For more information about Application Load Balancers, see [Create an Application Load Balancer](../../../elasticloadbalancing/latest/application/create-application-load-balancer.md "../../../elasticloadbalancing/latest/application/create-application-load-balancer.md") and [Update the IP address types for your Application Load Balancer](../../../elasticloadbalancing/latest/application/load-balancer-ip-address-type.md "../../../elasticloadbalancing/latest/application/load-balancer-ip-address-type.md") in the _User Guide for
Application Load Balancers_.

- For Amazon ECS tasks in an IPv6-only configuration to communicate with IPv4-only
  endpoints, you can set up DNS64 and NAT64 for
  network address translation from IPv6 to IPv4. For more information, see [DNS64 and NAT64](../../../vpc/latest/userguide/nat-gateway-nat64-dns64.md "../../../vpc/latest/userguide/nat-gateway-nat64-dns64.md") in the
  _Amazon VPC User Guide_.
- Amazon ECS workloads in an IPv6-only configuration must use Amazon ECR dualstack image URI endpoints when pulling images from Amazon ECR. For more information, see [Getting started with making requests over IPv6](../../../AmazonECR/latest/userguide/ecr-requests.md#ipv6-access-getting-started "../../../AmazonECR/latest/userguide/ecr-requests.md#ipv6-access-getting-started") in the
  _Amazon Elastic Container Registry User Guide_.

###### Note

Amazon ECR doesn't support dualstack interface VPC endpoints that tasks in an
IPv6-only configuration can use. For more information, see [Getting started with making requests over IPv6](../../../AmazonECR/latest/userguide/ecr-requests.md#ipv6-access-getting-started "../../../AmazonECR/latest/userguide/ecr-requests.md#ipv6-access-getting-started") in the
_Amazon Elastic Container Registry User Guide_.

- Amazon ECS Exec isn't supported in an IPv6-only configuration.
