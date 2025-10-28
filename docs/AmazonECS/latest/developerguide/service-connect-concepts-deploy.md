# Amazon ECS Service Connect components

When you use Amazon ECS Service Connect, you configure each Amazon ECS service to run a server
application that receives network requests (client-server service) or to run a client
application that makes the requests (client service).

When you prepare to start using Service Connect, start with a client-server service. You
can add a Service Connect configuration to a new service or an existing service. Amazon ECS
creates a Service Connect endpoint in the namespace. Additionally, Amazon ECS creates a new
deployment in the service to replace the tasks that are currently running.

Existing tasks and other applications can continue to connect to existing endpoints, and
external applications. If a client-server service adds tasks by scaling out, new connections
from clients will be balanced between all of the tasks. If a client-server service is
updated, new connections from clients will be balanced between the tasks of the new
version.

Existing tasks can't resolve and connect to the new endpoint. Only new tasks with a
Service Connect configuration in the same namespace and that start running after this
deployment can resolve and connect to this endpoint.

This means that the operator of the client application determines when the configuration
of their app changes, even though the operator of the server application can change their
configuration at any time. The list of endpoints in the namespace can change every time that
any service in the namespace is deployed. Existing tasks and replacement tasks continue to
behave the same as they did after the most recent deployment.

Consider the following examples.

First, assume that you are creating an application that is available to the public
internet in a single AWS CloudFormation template and single AWS CloudFormation stack. The public discovery and
reachability should be created last by AWS CloudFormation, including the frontend client service. The
services need to be created in this order to prevent an time period when the frontend client
service is running and available the public, but a backend isn't. This eliminates error
messages from being sent to the public during that time period. In AWS CloudFormation, you must use
the `dependsOn` to indicate to AWS CloudFormation that multiple Amazon ECS services can't be made
in parallel or simultaneously. You should add the `dependsOn` to the frontend
client service for each backend client-server service that the client tasks connect
to.

Second, assume that a frontend service exists without Service Connect configuration. The
tasks are connecting to an existing backend service. Add a client-server Service Connect
configuration to the backend service first, using the same name in the
**DNS** or `clientAlias` that the frontend uses. This
creates a new deployment, so all the deployment rollback detection or AWS Management Console, AWS CLI,
AWS SDKs and other methods to roll back and revert the backend service to the previous
deployment and configuration. If you are satisfied with the performance and behavior of the
backend service, add a client or client-server Service Connect configuration to the
frontend service. Only the tasks in the new deployment use the Service Connect proxy that
is added to those new tasks. If you have issues with this configuration, you can roll back
and revert to your previous configuration by using the deployment rollback detection or
AWS Management Console, AWS CLI, AWS SDKs and other methods to roll back and revert the backend service
to the previous deployment and configuration. If you use another service discovery system
that is based on DNS instead of Service Connect, any frontend or client applications begin
using new endpoints and changed endpoint configuration after the local DNS cache expires,
commonly taking multiple hours.

## Networking

By default, the Service Connect proxy listens on the `containerPort` from
the task definition port mapping. Your security group rules must allow incoming
(ingress) traffic to this port from the subnets where clients will run.

Even if you set a port number in the Service Connect service configuration, this
doesn't change the port for the client-server service that the Service Connect proxy
listens on. When you set this port number, Amazon ECS changes the port of the endpoint that
the client services connect to, on the Service Connect proxy inside those tasks. The
proxy in the client service connects to the proxy in the client-server service using the
`containerPort`.

If you want to change the port that the Service Connect proxy listens on, change the
`ingressPortOverride` in the Service Connect configuration of the
client-server service. If you change this port number, you must allow inbound traffic on
this port that is used by traffic to this service.

Traffic that your applications send to Amazon ECS services configured for Service Connect
require that the Amazon VPC and subnets have route table rules and network ACL rules that
allow the `containerPort` and `ingressPortOverride` port numbers
that you are using.

You can use Service Connect to send traffic between VPCs. The same requirements for
the route table rules, network ACLs, and security groups apply to both VPCs.

For example, two clusters create tasks in different VPCs. A service in each cluster is
configured to use the same namespace. The applications in these two services can resolve
every endpoint in the namespace without any VPC DNS configuration. However, the proxies
can't connect unless the VPC peering, VPC, or subnet route tables, and VPC network ACLs
allow the traffic on the `containerPort` and `ingressPortOverride`
port numbers.

For tasks that use the `bridge` networking mode, you must create a security
group with an inbound rule that allows traffic on the upper dynamic port range. Then,
assign the security group to all the EC2 instances in the Service Connect
cluster.

## Service Connect proxy

If you create or update a service with Service Connect configuration, Amazon ECS adds a
new container to each new task as it is started. This pattern of using a separate
container is called a `sidecar`. This container isn't present in the task
definition and you can't configure it. Amazon ECS manages the Container configuration in the
service. This allows you to reuse the same task definitions between multiple services,
namespaces, and tasks without Service Connect.

###### Proxy resources

- For task definitions, you must set the CPU and memory parameters.

We recommend adding an additional 256 CPU units and at least 64 MiB of memory
to your task CPU and memory for the Service Connect proxy container. On
AWS Fargate, the lowest amount of memory that you can set is 512 MiB of memory. On
Amazon EC2, task definition memory is required.

- For the service, you set the log configuration in the Service Connect
  configuration.
- If you expect tasks in this service to receive more than 500 requests per
  second at their peak load, we recommend adding 512 CPU units to your task CPU in
  this task definition for the Service Connect proxy container.
- If you expect to create more than 100 Service Connect services in the
  namespace or 2000 tasks in total across all Amazon ECS services within the namespace,
  we recommend adding 128 MiB of memory to your task memory for the
  Service Connect proxy container. You should do this in every task definition
  that is used by all of the Amazon ECS services in the namespace.

###### Proxy configuration

Your applications connect to the proxy in the sidecar container in the same task
as the application is in. Amazon ECS configures the task and containers so that
applications only connect to the proxy when the application is connected to the
endpoint names in the same namespace. All other traffic doesn't use the proxy. The
other traffic includes IP addresses in the same VPC, AWS service endpoints, and
external traffic.

**Load balancing**

Service Connect configures the proxy to use the round-robin strategy for
load balancing between the tasks in a Service Connect endpoint. The local
proxy that is in the task where the connection comes from, picks one of the
tasks in the client-server service that provides the endpoint.

For example, consider a task that runs WordPress in a service that is
configured as a _client service_ in a namespace called
_local_. There is another service with 2 tasks that
run the MySQL database. This service is configured to provide an endpoint
called `mysql` through Service Connect in the same namespace. In
the WordPress task, the WordPress application connects to the database using
the endpoint name. Connections to this name go to the proxy that runs in a
sidecar container in the same task. Then, the proxy can connect to either of
the MySQL tasks using the round-robin strategy.

Load balancing strategies: round-robin

**Outlier detection**

This feature uses data that the proxy has about prior failed connections
to avoid sending new connections to the hosts that had the failed
connections. Service Connect configures the outlier detection feature of
the proxy to provide passive health checks.

Using the previous example, the proxy can connect to either of the MySQL
tasks. If the proxy made multiple connections to a specific MySQL task, and
5 or more of the connections failed in the last 30 seconds, then the proxy
avoids that MySQL task for 30 to 300 seconds.

**Retries**

Service Connect configures the proxy to retry connection that pass
through the proxy and fail, and the second attempt avoids using the host
from the previous connection. This ensures that each connection through
Service Connect doesn't fail for one-off reasons.

Number of retries: 2

**Timeout**

Service Connect configures the proxy to wait a maximum time for your
client-server applications to respond. The default timeout value is 15
seconds, but it can be updated.

Optional parameters:

**idleTimeout** ‐ The amount of time in
seconds a connection stays active while idle. A value of `0`
disables `idleTimeout`.

The `idleTimeout` default for
`HTTP`/`HTTP2`/`GRPC` is 5
minutes.

The `idleTimeout` default for `TCP` is 1
hour.

**perRequestTimeout** ‐ The amount of
time waiting for the upstream to respond with a complete response per
request. A value of `0` turns off `perRequestTimeout`.
This can only be set when the `appProtocol` for application
container is `HTTP`/`HTTP2`/`GRPC`. The
default is 15 seconds.

###### Note

If `idleTimeout` is set to a time that is less than
`perRequestTimeout`, the connection will close when the
`idleTimeout` is reached and not the
`perRequestTimeout`.

## Considerations

Consider the following when using Service Connect:

- Tasks that run in Fargate must use the Fargate Linux platform version
  `1.4.0` or higher to use Service Connect.
- The Amazon ECS agent version on the container instance must be `1.67.2`
  or higher.
- Container instances must run the Amazon ECS-optimized Amazon Linux 2023 AMI version `20230428` or
  later, or Amazon ECS-optimized Amazon Linux 2 AMI version `2.0.20221115` to use Service Connect.
  These versions have the Service Connect agent in addition to the Amazon ECS
  container agent. For more information about the Service Connect agent, see
  [Amazon ECS
  Service Connect Agent](https://github.com/aws/amazon-ecs-service-connect-agent "https://github.com/aws/amazon-ecs-service-connect-agent") on GitHub.
- Container instances must have the `ecs:Poll` permission for the
  resource
  `arn:aws:ecs:`region`:`0123456789012`:task-set/`cluster`/*`.
  If you are using the `ecsInstanceRole`, you don't need to add
  additional permissions. The `AmazonEC2ContainerServiceforEC2Role`
  managed policy has the necessary permissions. For more information, see [Amazon ECS container instance IAM role](instance_IAM_role.md "instance_IAM_role.md").
- Tasks that use the `bridge` network mode and use Service Connect
  don't support the `hostname` container definition parameter.
- Task definitions must set the task memory limit to use Service Connect. For
  more information, see [Service Connect proxy](#service-connect-concepts-proxy "#service-connect-concepts-proxy").
- Task definitions that set container memory limits aren't supported.

You can set container memory limits on your containers, but you must set the
task memory limit to a number greater than the sum of the container memory
limits. The additional CPU and memory in the task limits that aren't allocated
in the container limits are used by the Service Connect proxy container and
other containers that don't set container limits. For more information, see
[Service Connect proxy](#service-connect-concepts-proxy "#service-connect-concepts-proxy").

- You can configure Service Connect to use any AWS Cloud Map namespace in the same
  Region that are either in the same AWS account or are shared
  with your AWS account using AWS Resource Access Manager. For more information about using shared namespaces, see [Amazon ECS Service Connect with shared
  AWS Cloud Map namespaces](service-connect-shared-namespaces.md "service-connect-shared-namespaces.md").
- Each service can belong to only one namespace.
- Only the tasks that services create are supported.
- All endpoints must be unique within a namespace.
- All discovery names must be unique within a namespace.
- You must redeploy existing services before the applications can resolve new
  endpoints. New endpoints that are added to the namespace after the most recent
  deployment won't be added to the task configuration. For more information, see
  [Amazon ECS Service Connect components](service-connect-concepts-deploy.md "service-connect-concepts-deploy.md").
- Service Connect doesn't delete namespaces when clusters are deleted. You must
  delete namespaces in AWS Cloud Map.
- Application Load Balancer traffic defaults to routing through the Service Connect agent in
  `awsvpc` network mode. If you want non-service traffic to bypass
  the Service Connect agent, use the `ingressPortOverride` parameter in your Service Connect
  service configuration.
- Service Connect with TLS does not support `bridge` networking mode. Only
  `awsvpc` networking mode is supported.
- Service Connect isn't available for services running on Amazon ECS Managed Instances.

In `awsvpc` mode, the Service Connect proxy forwards traffic to
the IPv4 localhost `127.0.0.1` for services in IPv4-only and
dualstack configurations. For services in IPv6-only configuration, the proxy
forwards traffic to the IPv6 localhost `::1`. We recommend
configuring your applications to listen to both localhosts for a seamless
experience when a service is updated from IPv4-only or dualstack configuration
to IPv6-only. For more information, see [Amazon ECS task networking options for EC2](task-networking.md "task-networking.md") and [Amazon ECS task networking options for Fargate](fargate-task-networking.md "fargate-task-networking.md").

###### Service Connect doesn't support the following:

- Windows containers
- HTTP 1.0
- Standalone tasks
- Services that use the blue/green powered by CodeDeploy and external deployment
  types
- `External` container instance for Amazon ECS Anywhere aren't supported
  with Service Connect.
- PPv2
- FIPS mode
