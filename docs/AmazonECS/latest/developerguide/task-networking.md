# Amazon ECS task networking options for EC2

The networking behavior of Amazon ECS tasks that are hosted on Amazon EC2 instances is dependent on
the _network mode_ that's defined in the task definition. We recommend
that you use the `awsvpc` network mode unless you have a specific need to use a
different network mode.

The following are the available network modes.

| Network mode | Linux containers on EC2 | Windows containers on EC2 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------ | ----------------------- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `awsvpc`     | Yes                     | Yes                       | The task is allocated its own elastic network interface (ENI) and a<br>primary private IPv4 or IPv6 address. This gives the task the same<br>networking properties as Amazon EC2 instances.                                                                                                                                                                                                                                                                                                                                  |
| `bridge`     | Yes                     | No                        | The task uses Docker's built-in virtual network on Linux, which runs inside each Amazon EC2<br>instance that hosts the task. The built-in virtual network on Linux uses the `bridge` Docker<br>network driver. This is the default network mode<br>on Linux if a network mode isn't specified in the task<br>definition.                                                                                                                                                                                                     |
| `host`       | Yes                     | No                        | The task uses the host's network which bypasses Docker's built-in virtual network<br>by mapping container ports directly to the ENI of the Amazon EC2 instance that hosts<br>the task. Dynamic port mappings can’t be used in this network mode. A container<br>in a task definition that uses this mode must specify a specific<br>`hostPort` number. A port number on a host can’t be used by multiple<br>tasks. As a result, you can’t run multiple tasks of the same task definition<br>on a single Amazon EC2 instance. |
| `none`       | Yes                     | No                        | The task has no external network connectivity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `default`    | No                      | Yes                       | The task uses Docker's built-in virtual network on Windows, which runs inside each Amazon EC2 instance that hosts the task. The built-in virtual network on Windows uses the `nat` Docker network driver. This is the default network<br>mode on Windows if a network mode isn't specified in the task<br>definition.                                                                                                                                                                                                        |

For more information about Docker networking on Linux, see [Networking overview](https://docs.docker.com/engine/network/ "https://docs.docker.com/engine/network/") in the
_Docker Documentation_.

For more information about Docker networking on Windows, see [Windows container networking](https://learn.microsoft.com/en-us/virtualization/windowscontainers/container-networking/architecture "https://learn.microsoft.com/en-us/virtualization/windowscontainers/container-networking/architecture") in the Microsoft _Containers on Windows Documentation_.

## Using a VPC in IPv6-only mode

In an IPv6-only configuration, your Amazon ECS tasks communicate exclusively over IPv6. To
set up VPCs and subnets for an IPv6-only configuration, you must add an IPv6 CIDR block
to the VPC and create new subnets that include only an IPv6 CIDR block. For more
information see [Add IPv6 support for your
VPC](../../../vpc/latest/userguide/vpc-migrate-ipv6-add.md "../../../vpc/latest/userguide/vpc-migrate-ipv6-add.md") and [Create a subnet](../../../vpc/latest/userguide/create-subnets.md "../../../vpc/latest/userguide/create-subnets.md") in the
_Amazon VPC User Guide_.

You must also update route tables with IPv6
targets and configure security groups with IPv6 rules. For more information, see [Configure
route tables](../../../vpc/latest/userguide/VPC_Route_Tables.md "../../../vpc/latest/userguide/VPC_Route_Tables.md") and [Configure security
group rules](../../../vpc/latest/userguide/working-with-security-group-rules.md "../../../vpc/latest/userguide/working-with-security-group-rules.md") in the _Amazon VPC User Guide_.

The following considerations apply:

- You can update an IPv4-only or dualstack Amazon ECS service to an IPv6-only
  configuration by either updating the service directly to use IPv6-only subnets
  or by creating a parallel IPv6-only service and using Amazon ECS blue-green
  deployments to shift traffic to the new service. For more information about
  Amazon ECS blue-green deployments, see [Amazon ECS blue/green deployments](deployment-type-blue-green.md "deployment-type-blue-green.md").
- An IPv6-only Amazon ECS service must use dualstack load balancers with IPv6 target
  groups. If you're migrating an existing Amazon ECS service that's behind a Application Load Balancer or a
  Network Load Balancer, you can create a new dualstack load balancer and shift traffic from the
  old load balancer, or update the IP address type of the existing load balancer.

For more information about Network Load Balancers, see [Create a Network Load Balancer](../../../elasticloadbalancing/latest/network/create-network-load-balancer.md "../../../elasticloadbalancing/latest/network/create-network-load-balancer.md") and [Update the IP address types for your Network Load Balancer](../../../elasticloadbalancing/latest/network/load-balancer-ip-address-type.md "../../../elasticloadbalancing/latest/network/load-balancer-ip-address-type.md") in the _User
Guide for Network Load Balancers_. For more information about Application Load Balancers, see [Create an Application Load Balancer](../../../elasticloadbalancing/latest/application/create-application-load-balancer.md "../../../elasticloadbalancing/latest/application/create-application-load-balancer.md") and [Update the IP address types for your Application Load Balancer](../../../elasticloadbalancing/latest/application/load-balancer-ip-address-type.md "../../../elasticloadbalancing/latest/application/load-balancer-ip-address-type.md") in the _User
Guide for Application Load Balancers_.

- IPv6-only configuration isn't supported on Windows. You must use
  Amazon ECS-optimized Linux AMIs to run tasks in an IPv6-only configuration. For more
  information about Amazon ECS-optimized Linux AMIs, see [Amazon ECS-optimized Linux AMIs](ecs-optimized_AMI.md "ecs-optimized_AMI.md").
- When you launch a container instance for running tasks in an IPv6-only
  configuration, you must set a primary IPv6 address for the instance by using the
  `--enable-primary-ipv6` EC2 parameter.

###### Note

Without a primary IPv6 address, tasks running on the container instance in
the host or bridge network modes will fail to register with load balancers
or with AWS Cloud Map.

For more information about the `--enable-primary-ipv6` for running
Amazon EC2 instances, see [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md") in
the _AWS CLI Command Reference_.

For more information about launching container instances using the AWS Management Console,
see [Launching an Amazon ECS Linux container
instance](launch_container_instance.md "launch_container_instance.md").

- By default, the Amazon ECS container agent will try to detect the container
  instance's compatibility for an IPv6-only configuration by looking at the
  instance's default IPv4 and IPv6 routes. To override this behavior, you can set
  the `ECS_INSTANCE_IP_COMPATIBILITY` parameter to `ipv4`
  or `ipv6` in the instance's `/etc/ecs/ecs.config`
  file.
- Tasks must use version `1.99.1` or later of the container agent.
  For information about how to check the agent version your instance is using and
  updating it if needed, see [Updating the Amazon ECS container agent](ecs-agent-update.md "ecs-agent-update.md").
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

### AWS Regions that support IPv6-only mode for Amazon ECS

You can run tasks in an IPv6-only configuration in the following AWS regions that Amazon ECS is available in:

- US East (Ohio)
- US East (N. Virginia)
- US West (N. California)
- US West (Oregon)
- Africa (Cape Town)
- Asia Pacific (Hong Kong)
- Asia Pacific (Hyderabad)
- Asia Pacific (Jakarta)
- Asia Pacific (Melbourne)
- Asia Pacific (Mumbai)
- Asia Pacific (Osaka)
- Asia Pacific (Seoul)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Tokyo)
- Canada (Central)
- Canada West (Calgary)
- China (Beijing)
- China (Ningxia)
- Europe (Frankfurt)
- Europe (London)
- Europe (Milan)
- Europe (Paris)
- Europe (Spain)
- Israel (Tel Aviv)
- Middle East (Bahrain)
- Middle East (UAE)
- South America (São Paulo)
- AWS GovCloud (US-East)
- AWS GovCloud (US-West)
