

# Troubleshooting service load balancers in Amazon ECS

Amazon ECS services can register tasks with an Elastic Load Balancing load balancer. Load balancer configuration errors are common causes for stopped tasks. A task that a service stops because the load balancer reports it as unhealthy has the stopped reason `Task failed ELB health checks in (target-group {{target-group-ARN}})`, or `Task failed ELB health checks in (elb {{load-balancer-name}})` for a Classic Load Balancer. If your stopped tasks were started by services that use a load balancer, consider the following possible causes.

**Health check grace period is too short**  
If your application takes a while to start, the load balancer can report the task as unhealthy before the application is ready. Set the service's health check grace period (`healthCheckGracePeriodSeconds`) to longer than your application takes to start responding. The default is 0. For more information, see [Amazon ECS service definition parameters](service_definition_parameters.md).

**Amazon ECS service-linked role doesn't exist**  
The Amazon ECS service-linked role allows Amazon ECS services to register container instances with Elastic Load Balancing load balancers. The service-linked role must be created in your account. For more information, see [Using service-linked roles for Amazon ECS](using-service-linked-roles.md).

**Container instance security group**  
If your container is mapped to port 80 on your container instance, your container instance security group must allow inbound traffic on port 80 for the load balancer health checks to pass.

**Task security group doesn't allow the load balancer**  
For tasks that use the `awsvpc` network mode, including tasks on Fargate, the task's security group must allow inbound traffic from the load balancer. Allow it on the container port and the health check port. If the load balancer has security groups, use its security group as the source, and make sure the load balancer's security group allows outbound traffic to the task on those ports. For a Network Load Balancer without security groups, allow traffic from the load balancer's private IP addresses, and from your clients' IP addresses if the load balancer preserves client IP addresses. For more information, see [Security groups for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-update-security-groups.html) or [Register targets for your Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/target-group-register-targets.html).

**Elastic Load Balancing load balancer not configured for all Availability Zones**  
Your load balancer should be configured to use all of the Availability Zones in a Region, or at least all of the Availability Zones where your container instances reside. If a service uses a load balancer and starts a task on a container instance that resides in an Availability Zone that the load balancer isn't configured to use, the task never passes the health check. This results in the task being killed.

**Elastic Load Balancing load balancer health check misconfigured**  
The load balancer health check parameters can be overly restrictive or point to resources that don't exist. If a container instance is determined to be unhealthy, it's removed from the load balancer. Be sure to verify that the following parameters are configured correctly for your service load balancer.    
Ping Port  
The **Ping Port** value for a load balancer health check is the port on the container instances that the load balancer checks to determine if it is healthy. If this port is misconfigured, the load balancer likely deregisters your container instance from itself. This port should be configured to use the `hostPort` value for the container in your service's task definition that you're using with the health check.  
Ping Path  
This is part of the load balancer healthcheck. It is an endpoint on your application that can resturn a successful status code (for example, 200) when the application is healthy. This value is often set to `index.html`, but if your service doesn't respond to that request, then the health check fails. If your container doesn't have an `index.html` file, you can set this to `/` to target the base URL for the container instance.  
Response Timeout  
This is the amount of time that your container has to return a response to the health check ping. If this value is lower than the amount of time required for a response, the health check fails.  
Health Check Interval  
This is the amount of time between health check pings. The shorter your health check intervals are, the faster your container instance can reach the **Unhealthy Threshold**.  
Unhealthy Threshold  
This is the number of times your health check can fail before your container instance is considered unhealthy. If you have an unhealthy threshold of 2, and a health check interval of 30 seconds, then your task has 60 seconds to respond to the health check ping before it's assumed unhealthy. You can raise the unhealthy threshold or the health check interval to give your tasks more time to respond.

**Health check success codes don't match the response**  
The target group's success codes are the HTTP status codes that count as healthy. The default is 200 for an Application Load Balancer and 200-399 for a Network Load Balancer that uses HTTP or HTTPS health checks. If the health check path returns a code outside them, such as a redirect on an Application Load Balancer, the health check fails. Change the success codes or the health check path. For more information, see [Health checks for Application Load Balancer target groups](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html) or [Health checks for Network Load Balancer target groups](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/target-group-health-checks.html).

**The application is failing**  
If the task passed health checks and then failed them, the application might be crashing, returning errors, or waiting on a dependency. Check the task's container logs. To test the health check path from inside the container, use ECS Exec, which must be turned on before the task starts. For more information, see [Monitor Amazon ECS containers with ECS Exec](ecs-exec.md).

**The target was removed from the target group**  
If a task's target isn't in its target group, the stopped reason is usually `Task failed ELB health checks in (target-group {{target-group-ARN}}) because target is not found` or `Service {{service-name}}: task remained in deregistered state for too long.` Amazon ECS registers and deregisters the targets of a service's target groups, so leave target registration to Amazon ECS. The service starts a replacement task and registers it.

**Unable to update the service** {{servicename}}**: Load balancer container name or port changed in task definition**  
If your service uses a load balancer, you can use the AWS CLI or SDK to modify the load balancer configuration. For information about how to modify the configuration, see [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html) in the *Amazon Elastic Container Service API Reference*. If you update the task definition for the service, the container name and container port that are specified in the load balancer configuration must remain in the task definition.

**You've reached the limit on the number of tasks that you can run concurrently.**  
For a new account, your quotas might be lower that the service quotas. The service quota for your account can be viewed in the Service Quotas console. To request a quota increase, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*.