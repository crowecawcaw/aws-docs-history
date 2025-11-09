# Interconnect Amazon ECS services

Applications that run in Amazon ECS tasks often need to receive connections from the
internet or to connect to other applications that run in Amazon ECS services. If you need
external connections from the internet, we recommend using Elastic Load Balancing. For more
information about integrated load balancing, see [Use load balancing to distribute Amazon ECS service
traffic](service-load-balancing.md "service-load-balancing.md").

If you need an application to connect to other applications that run in Amazon ECS
services, Amazon ECS provides the following ways to do this without a load
balancer:

- _Amazon ECS Service Connect_

We recommend Service Connect, which provides Amazon ECS configuration for
service discovery, connectivity, and traffic monitoring. With
Service Connect, your applications can use short names and standard ports
to connect to Amazon ECS services in the same cluster, other clusters, including
across VPCs in the same AWS Region.

When you use Service Connect, Amazon ECS manages all of the parts of service
discovery: creating the names that can be discovered, dynamically managing
entries for each task as the tasks start and stop, running an agent in each
task that is configured to discover the names. Your application can look up
the names by using the standard functionality for DNS names and making
connections. If your application does this already, you don't need to modify
your application to use Service Connect.

You provide the complete configuration inside each service and task
definition. Amazon ECS manages changes to this configuration in each service
deployment, to ensure that all tasks in a deployment behave in the same way.
For example, a common problem with DNS as service discovery is controlling a
migration. If you change a DNS name to point to the new replacement IP
addresses, it might take the maximum TTL time before all the clients begin
using the new service. With Service Connect, the client deployment updates
the configuration by replacing the client tasks. You can configure the
deployment circuit breaker and other deployment configuration to affect
Service Connect changes in the same way as any other deployment.

For more information, see [Use Service Connect to connect Amazon ECS services with short
names](service-connect.md "service-connect.md").

- _Amazon ECS service discovery_

Another approach for service-to-service communication is direct
communication using service discovery. In this approach, you can use the
AWS Cloud Map service discovery integration with Amazon ECS. Using service discovery,
Amazon ECS syncs the list of launched tasks to AWS Cloud Map, which maintains a DNS
hostname that resolves to the internal IP addresses of one or more tasks
from that particular service. Other services in the Amazon VPC can use this DNS
hostname to send traffic directly to another container using its internal IP
address.

This approach to service-to-service communication provides low latency.
There are no extra components between the containers. Traffic travels
directly from one container to the other container.

This approach is suitable when using the `awsvpc` network mode,
where each task has its own unique IP address. Most software only supports
the use of DNS `A` records, which resolve directly to IP
addresses. When using the `awsvpc` network mode, the IP address
for each task are an `A` record. However, if you're using
`bridge` network mode, multiple containers could be sharing
the same IP address. Additionally, dynamic port mappings cause the
containers to be randomly assigned port numbers on that single IP address.
At this point, an `A` record is no longer enough for service
discovery. You must also use an `SRV` record. This type of record
can keep track of both IP addresses and port numbers but requires that you
configure applications appropriately. Some prebuilt applications that you
use might not support `SRV` records.

Another advantage of the `awsvpc` network mode is that you have
a unique security group for each service. You can configure this security
group to allow incoming connections from only the specific upstream services
that need to talk to that service.

The main disadvantage of direct service-to-service communication using
service discovery is that you must implement extra logic to have retries and
deal with connection failures. DNS records have a time-to-live (TTL) period
that controls how long they are cached for. It takes some time for the DNS
record to be updated and for the cache to expire so that your applications
can pick up the latest version of the DNS record. So, your application might
end up resolving the DNS record to point at another container that's no
longer there. Your application needs to handle retries and have logic to
ignore bad backends.

For more information, see [Use service discovery to connect Amazon ECS services with
DNS names](service-discovery.md "service-discovery.md")

- _Amazon VPC Lattice_

Amazon VPC Lattice is a managed application networking service that Amazon ECS customers use to observe, secure, and
monitor applications built across AWS compute services, VPCs, and accounts without having to modify their
code.

VPC Lattice uses target groups, which are a collection of compute resources. These targets run your
application or service and can be Amazon EC2 instances, IP addresses, Lambda functions, and Application Load Balancers. By
associating their Amazon ECS services with a VPC Lattice target group, customers can now enable Amazon ECS tasks as IP
targets in VPC Lattice. Amazon ECS automatically registers tasks to the VPC Lattice target group when tasks for the
registered service are launched.

For more information, see [Use Amazon VPC Lattice to connect, observe, and secure your Amazon ECS
services](ecs-vpc-lattice.md "ecs-vpc-lattice.md").

## Network mode

compatibility table

The following table covers the compatibility between these options and the task
network modes. In the table, "client" refers to the application that's making the
connections from inside an Amazon ECS task.

| Interconnection Options | Bridged                                                                         | `awsvpc` | Host                                                                            |
| ----------------------- | ------------------------------------------------------------------------------- | -------- | ------------------------------------------------------------------------------- |
| **Service discovery**   | yes, but requires clients be aware of SRV records in DNS without<br>`hostPort`. | yes      | yes, but requires clients be aware of SRV records in DNS without<br>`hostPort`. |
| **Service Connect**     | yes                                                                             | yes      | no                                                                              |
| VPC Lattice             | yes                                                                             | yes      | yes                                                                             |
