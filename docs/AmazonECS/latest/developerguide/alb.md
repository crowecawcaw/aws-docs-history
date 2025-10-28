# Use an Application Load Balancer for Amazon ECS

An Application Load Balancer makes routing decisions at the application layer (HTTP/HTTPS), supports
path-based routing, and can route requests to one or more ports on each container
instance in your cluster. Application Load Balancers support dynamic host port mapping. For example, if your
task's container definition specifies port 80 for an NGINX container port, and port 0
for the host port, then the host port is dynamically chosen from the ephemeral port
range of the container instance (such as 32768 to 61000 on the latest
Amazon ECS-optimized AMI). When the task launches, the NGINX container is registered with the
Application Load Balancer as an instance ID and port combination, and traffic is distributed to the instance
ID and port corresponding to that container. This dynamic mapping allows you to have
multiple tasks from a single service on the same container instance. For more
information, see the [User Guide for Application Load Balancers](../../../elasticloadbalancing/latest/application.md "../../../elasticloadbalancing/latest/application.md").

For information about the best practices for setting parameters to speed up you
deployments see:

- [Optimize load balancer health
  check parameters for Amazon ECS](load-balancer-healthcheck.md "load-balancer-healthcheck.md")
- [Optimize load balancer
  connection draining parameters for Amazon ECS](load-balancer-connection-draining.md "load-balancer-connection-draining.md")
  Consider the following when using Application Load Balancers with Amazon ECS:

- Amazon ECS requires the service-linked IAM role which provides the permissions
  needed to register and deregister targets with your load balancer when tasks are
  created and stopped. For more information, see [Using service-linked roles for
  Amazon ECS](using-service-linked-roles.md "using-service-linked-roles.md").
- For services in an IPv6-only configuration, you must set the target group IP
  address type of the Application Load Balancer to `dualstack` or
  `dualstack-without-public-ipv4`.
- For services with tasks using the `awsvpc` network mode, when you
  create a target group for your service, you must choose `ip` as the
  target type, not `instance`. This is because tasks that use
  the `awsvpc` network mode are associated with an elastic network
  interface, not an Amazon EC2 instance.
- If your service requires access to multiple load balanced ports, such as port
  80 and port 443 for an HTTP/HTTPS service, you can configure two listeners. One
  listener is responsible for HTTPS that forwards the request to the service, and
  another listener that is responsible for redirecting HTTP requests to the
  appropriate HTTPS port. For more information, see [Create a listener to your
  Application Load Balancer](../../../elasticloadbalancing/latest/application/create-listener.md "../../../elasticloadbalancing/latest/application/create-listener.md") in the _User Guide for Application Load Balancers_.
- Your load balancer subnet configuration must include all Availability Zones
  that your container instances reside in.
- After you create a service, the load balancer configuration can't be changed from the AWS Management Console. You can use the AWS Copilot, AWS CloudFormation, AWS CLI or SDK to modify the load balancer configuration for the `ECS` rolling deployment controller only, not AWS CodeDeploy blue/green or external. When you add, update, or remove a load balancer configuration, Amazon ECS starts a new deployment with the updated Elastic Load Balancing configuration. This causes tasks to register to and deregister from load balancers. We recommend that you verify this on a test environment before you update the Elastic Load Balancing configuration. For information about how to modify the configuration, see [UpdateService](../APIReference/API_UpdateService.md "../APIReference/API_UpdateService.md") in the _Amazon Elastic Container Service API Reference_.
- If a service task fails the load balancer health check criteria, the task is
  stopped and restarted. This process continues until your service reaches the
  number of desired running tasks.
- If you are experiencing problems with your load balancer-enabled services, see
  [Troubleshooting service load
  balancers in Amazon ECS](troubleshoot-service-load-balancers.md "troubleshoot-service-load-balancers.md").
- When using `instance` target type, your tasks and load balancer
  must be in the same VPC. When using `ip` target type, cross-VPC
  connectivity is supported.
- Use a unique target group for each service.

Using the same target group for multiple services might lead to issues during
service deployments.

- You must specify target groups that are associated with an Application Load Balancer.
  For information about how to create an Application Load Balancer, see [Create an Application Load Balancer](../../../elasticloadbalancing/latest/application/create-application-load-balancer.md "../../../elasticloadbalancing/latest/application/create-application-load-balancer.md") in _Application Load Balancers_
