# Troubleshooting service load

balancers in Amazon ECS

Amazon ECS services can register tasks with an Elastic Load Balancing load balancer. Load balancer
configuration errors are common causes for stopped tasks. If your stopped tasks were
started by services that use a load balancer, consider the following possible
causes.

**Amazon ECS service-linked role doesn't exist**

The Amazon ECS service-linked role allows Amazon ECS services to register container
instances with Elastic Load Balancing load balancers. The service-linked role must be created
in your account. For more information, see [Using service-linked roles for
Amazon ECS](using-service-linked-roles.md "using-service-linked-roles.md").

**Container instance security group**

If your container is mapped to port 80 on your container instance, your
container instance security group must allow inbound traffic on port 80 for
the load balancer health checks to pass.

**Elastic Load Balancing load balancer not configured for all Availability
Zones**

Your load balancer should be configured to use all of the Availability
Zones in a Region, or at least all of the Availability Zones where your
container instances reside. If a service uses a load balancer and starts a
task on a container instance that resides in an Availability Zone that the
load balancer isn't configured to use, the task never passes the health
check. This results in the task being killed.

**Elastic Load Balancing load balancer health check misconfigured**

The load balancer health check parameters can be overly restrictive or
point to resources that don't exist. If a container instance is determined
to be unhealthy, it's removed from the load balancer. Be sure to verify
that the following parameters are configured correctly for your service load
balancer.

Ping Port

The **Ping Port** value for a load balancer
health check is the port on the container instances that the
load balancer checks to determine if it is healthy. If this port
is misconfigured, the load balancer likely deregisters your
container instance from itself. This port should be configured
to use the `hostPort` value for the container in your
service's task definition that you're using with the health
check.

Ping Path

This is part of the load balancer healthcheck. It is an endpoint
on your application that can resturn a successful status code (for
example, 200) when the application is healthy. This value is often
set to `index.html`, but if your service doesn't respond
to that request, then the health check fails. If your container
doesn't have an `index.html` file, you can set this to
`/` to target the base URL for the container
instance.

Response Timeout

This is the amount of time that your container has to return a
response to the health check ping. If this value is lower than
the amount of time required for a response, the health check
fails.

Health Check Interval

This is the amount of time between health check pings. The
shorter your health check intervals are, the faster your
container instance can reach the **Unhealthy
Threshold**.

Unhealthy Threshold

This is the number of times your health check can fail before
your container instance is considered unhealthy. If you have an
unhealthy threshold of 2, and a health check interval of 30
seconds, then your task has 60 seconds to respond to the health
check ping before it's assumed unhealthy. You can raise the
unhealthy threshold or the health check interval to give your
tasks more time to respond.

**Unable to update the service**
`servicename`**: Load balancer container name or
port changed in task definition**

If your service uses a load balancer, you can use the AWS CLI or SDK to
modify the load balancer configuration. For information about how to modify
the configuration, see [UpdateService](../APIReference/API_UpdateService.md "../APIReference/API_UpdateService.md") in the _Amazon Elastic Container Service API
Reference_. If you update the task definition for the service,
the container name and container port that are specified in the load
balancer configuration must remain in the task definition.

**You've reached the limit on the number of tasks that you can run
concurrently.**

For a new account, your quotas might be lower that the
service quotas. The service quota for your account can be viewed in the Service Quotas
console. To request a quota increase, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the
_Service Quotas User Guide_.
