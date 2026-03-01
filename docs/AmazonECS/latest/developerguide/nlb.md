# Use a Network Load Balancer for Amazon ECS

A Network Load Balancer makes routing decisions at the transport layer (TCP/SSL). It can handle
millions of requests per second. After the load balancer receives a connection, it
selects a target from the target group for the default rule using a flow hash routing
algorithm. It attempts to open a TCP connection to the selected target on the port
specified in the listener configuration. It forwards the request without modifying the
headers. Network Load Balancers support dynamic host port mapping. For example, if your task's container
definition specifies port 80 for an NGINX container port, and port 0 for the host port,
then the host port is dynamically chosen from the ephemeral port range of the container
instance (such as 32768 to 61000 on the latest Amazon ECS-optimized AMI). When the task is
launched, the NGINX container is registered with the Network Load Balancer as an instance ID and port
combination, and traffic is distributed to the instance ID and port corresponding to
that container. This dynamic mapping allows you to have multiple tasks from a single
service on the same container instance. For more information, see the
[User Guide for Network Load Balancers](../../../elasticloadbalancing/latest/network.md "../../../elasticloadbalancing/latest/network.md").

For information about the best practices for setting parameters to speed up you
deployments see:

- [Optimize load balancer health check parameters for Amazon ECS](load-balancer-healthcheck.md "load-balancer-healthcheck.md")
- [Optimize load balancer connection draining parameters for Amazon ECS](load-balancer-connection-draining.md "load-balancer-connection-draining.md")
  Consider the following when using Network Load Balancers with Amazon ECS:

- Amazon ECS requires the service-linked IAM role which provides the permissions
  needed to register and deregister targets with your load balancer when tasks are
  created and stopped. For more information, see [Using service-linked roles for Amazon ECS](using-service-linked-roles.md "using-service-linked-roles.md").
- You cannot attach more than five target groups to a service.
- For services in an IPv6-only configuration, you must set the target group IP
  address type of the Network Load Balancer to `dualstack`.
- For services with tasks using the `awsvpc` network mode, when you
  create a target group for your service, you must choose `ip` as the
  target type, not `instance`. This is because tasks that use the
  `awsvpc` network mode are associated with an elastic network
  interface, not an Amazon EC2 instance.
- Your load balancer subnet configuration must include all Availability Zones
  that your container instances reside in.
- After you create a service, the load balancer configuration can't be changed from the AWS Management Console. You can use the AWS Copilot, AWS CloudFormation, AWS CLI or SDK to modify the load balancer configuration for the `ECS` rolling deployment controller only, not AWS CodeDeploy blue/green or external. When you add, update, or remove a load balancer configuration, Amazon ECS starts a new deployment with the updated Elastic Load Balancing configuration. This causes tasks to register to and deregister from load balancers. We recommend that you verify this on a test environment before you update the Elastic Load Balancing configuration. For information about how to modify the configuration, see [UpdateService](../APIReference/API_UpdateService.md "../APIReference/API_UpdateService.md") in the _Amazon Elastic Container Service API Reference_.
- If a service task fails the load balancer health check criteria, the task is
  stopped and restarted. This process continues until your service reaches the
  number of desired running tasks.
- When you use a Gateway Load Balancer configured with IP addresses as targets and Client IP
  Preservation off, requests are seen as coming from the Gateway Load Balancers private IP
  address. This means that services behind an Gateway Load Balancer are effectively open to the
  world as soon as you allow incoming requests and health checks in the target
  security group.
- For Fargate tasks, you must use platform version `1.4.0` (Linux)
  or `1.0.0` (Windows).
- If you are experiencing problems with your load balancer-enabled services, see
  [Troubleshooting service load balancers in Amazon ECS](troubleshoot-service-load-balancers.md "troubleshoot-service-load-balancers.md").
- When using `instance` target type, your tasks and load balancer
  must be in the same VPC. When using `ip` target type, cross-VPC
  connectivity is supported.
- The Network Load Balancer client IP address preservation is compatible with Fargate
  targets.
- Use a unique target group for each service.

Using the same target group for multiple services might lead to issues during
service deployments.

- You must specify target groups that are associated with a Network Load Balancer.
  For information about how to create a Network Load Balancer, see [Create a
  Network Load Balancer](../../../elasticloadbalancing/latest/network/create-network-load-balancer.md "../../../elasticloadbalancing/latest/network/create-network-load-balancer.md") in _Network Load Balancers_

###### Important

If your service's task definition uses the `awsvpc` network mode (which
is required for Fargate), you must choose
`ip` as the target type, not `instance`. This is because
tasks that use the `awsvpc` network mode are associated with an elastic
network interface, not an Amazon EC2 instance.

You cannot register instances by instance ID if they have the following instance
types: C1, CC1, CC2, CG1, CG2, CR1, G1, G2, HI1, HS1, M1, M2, M3, and T1. You can
register instances of these types by IP address.
