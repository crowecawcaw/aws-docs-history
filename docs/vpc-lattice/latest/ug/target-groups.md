# Target groups in VPC Lattice

A VPC Lattice target group is a collection of targets, or compute resources, that run your
application or service. The supported target types include EC2 instances, IP addresses, Lambda functions, Application Load Balancers, Amazon ECS tasks, and Kubernetes Pods. You can also attach existing services to your target
groups. For more information about using Kubernetes with VPC Lattice, see the [AWS Gateway API Controller User
Guide](https://www.gateway-api-controller.eks.aws.dev/ "https://www.gateway-api-controller.eks.aws.dev/").

Each _target group_ is used to route requests to one or more registered
targets. When you create a listener rule, you specify a target group and conditions. When a
rule condition is met, traffic is forwarded to the corresponding target group. You can
create different target groups for different types of requests. For example, create one
target group for general requests and other target groups for requests that include specific
rule conditions, such as a path or header value.

![A service with a listener, listener rules, and two target groups.](/images/vpc-lattice/latest/ug/images/service.png)
You define health check settings for your service on a per target group basis. Each target
group uses the default health check settings, unless you override them when you create the
target group or modify them later on. After you specify a target group in a rule for a
listener, the service continually monitors the health of all targets registered with the
target group. The service routes requests to the registered targets that are healthy.

To specify a target group in a rule for a service listener, the target group must be
in the same account as the service.

VPC Lattice target groups are similar to the target groups provided by ELB, but they
are not interchangeable.

###### Contents

- [Create a target group](create-target-group.md "create-target-group.md")
- [Register targets](register-targets.md "register-targets.md")
- [Configure health checks](target-group-health-checks.md "target-group-health-checks.md")
- [Routing configuration](#target-group-routing-configuration "#target-group-routing-configuration")
- [Routing algorithm](#target-group-routing-algorithm "#target-group-routing-algorithm")
- [Target type](#target-type "#target-type")
- [IP address type](#target-group-ip-address-type "#target-group-ip-address-type")
- [HTTP targets](http-targets.md "http-targets.md")
- [Lambda functions as targets](lambda-functions.md "lambda-functions.md")
- [Application Load Balancers as targets](alb-target.md "alb-target.md")
- [Protocol version](#target-group-protocol-version "#target-group-protocol-version")
- [Update tags](target-group-tags.md "target-group-tags.md")
- [Delete a target group](delete-target-group.md "delete-target-group.md")

## Routing configuration

By default, a service routes requests to its targets using the protocol and port
number that you specified when you created the target group. Alternatively, you can
override the port used for routing traffic to a target when you register it with the
target group.

Target groups support the following protocols and ports:

- **Protocols**: HTTP, HTTPS, TCP
- **Ports**: 1-65535

If a target group is configured with the HTTPS protocol or uses HTTPS health checks,
the TLS connections to the targets use the security policy from the listener. VPC Lattice
establishes TLS connections with the targets using certificates that you install on the
targets. VPC Lattice does not validate these certificates. Therefore, you can use
self-signed certificates or certificates that have expired. The traffic between VPC Lattice
and the targets is authenticated at the packet level, so it is not at risk of
man-in-the-middle attacks or spoofing even if the certificates on the targets are not
valid.

TCP target groups are supported only with [TLS listeners](tls-listeners.md "tls-listeners.md").

## Routing algorithm

By default, the round robin routing algorithm is used to route requests to healthy
targets.

When the VPC Lattice service receives a request, it uses the following process:

1. Evaluates the listener rules in priority order to determine which rule to
   apply.
2. Selects a target from the target group for the rule action, using the default
   round robin algorithm. Routing is performed independently for each target group,
   even when a target is registered with multiple target groups.

If a target group contains only unhealthy targets, the requests are routed to all
targets, regardless of their health status. This means that if all targets fail health
checks at the same time, the VPC Lattice service fails open. The effect of the fail-open
is to allow traffic to all targets, regardless of their health status, based on the
round robin algorithm.

## Target type

When you create a target group, you specify its target type, which determines the type
of target you specify when registering targets with this target group. After you create
a target group, you can't change its target type.

The following are the possible target types:

`INSTANCE`

The targets are specified by instance ID.

`IP`

The targets are IP addresses.

`LAMBDA`

The target is a Lambda function.

`ALB`

The target is an Application Load Balancer.

###### Considerations

- When the target type is `IP`, you must specify IP addresses from
  the subnets of the VPC for the target group. If you need to register IP
  addresses from outside this VPC, create a target group of type `ALB`
  and register the IP addresses with the Application Load Balancer.
- When the target type is `IP`, you can't register VPC endpoints
  or publicly routable IP addresses.
- When the target type is `LAMBDA`, you can register a single Lambda
  function. When the service receives a request for the Lambda function, it
  invokes the Lambda function. If you would like to register multiple lambda
  functions to a service, you need to use multiple target groups.
- When the target type is `ALB`, you can register a single internal
  Application Load Balancer as the target of up to two VPC Lattice services. To do this, register the
  Application Load Balancer with two separate target groups, used by two different VPC Lattice services.
  Additionally, the targeted Application Load Balancer must have at least one listener whose port
  matches the target group port.
- You can automatically register your ECS tasks with a VPC Lattice target group
  at launch. The target group must have a target type of `IP`. For more
  information, see [Use VPC Lattice
  with your Amazon ECS services](../../../AmazonECS/latest/developerguide/ecs-vpc-lattice.md "../../../AmazonECS/latest/developerguide/ecs-vpc-lattice.md") in the _Amazon Elastic Container Service Developer Guide_.

Alternatively, register the Application Load Balancer for your Amazon ECS service with a VPC Lattice target
group of type `ALB`. For more information, see
[Use load balancing to distribute Amazon ECS service traffic](../../../AmazonECS/latest/developerguide/service-load-balancing.md "../../../AmazonECS/latest/developerguide/service-load-balancing.md")
in the _Amazon Elastic Container Service Developer Guide_.

- To register an EKS pod as a target, use the [AWS Gateway API Controller](https://www.gateway-api-controller.eks.aws.dev/ "https://www.gateway-api-controller.eks.aws.dev/"), which gets the IP addresses from the
  Kubernetes service.
- If the target group protocol is TCP, the only supported target types are
  `INSTANCE`, `IP`, or `ALB`.

## IP address type

When you create a target group with a target type of `IP`, you can
specify an IP address type for the target group. This specifies what type of
addresses the load balancer uses to send requests and health checks to targets.
The possible values are `IPv4` and `IPv6`. The default is
`IPV4`.

###### Considerations

- If you create a target group with an IP address type of `IPv6`,
  the VPC that you specify for the target group must have an IPv6 address range.
- The IP addresses that you register with a target group must match the
  IP address type of the target group. For example, you can't register an IPv6
  address with a target group if its IP address type is `IPv4`.
- The IP addresses that you register with a target group must be within the
  IP address range of the VPC that you specified for the target group.

## Protocol version

By default, services send requests to targets using HTTP/1.1. You can use the protocol
version to send requests to targets using HTTP/2 or gRPC.

The following table summarizes the result for the combinations of request protocol and
target group protocol version.

| Request protocol | Protocol version | Result                          |
| ---------------- | ---------------- | ------------------------------- |
| HTTP/1.1         | HTTP/1.1         | Success                         |
| HTTP/2           | HTTP/1.1         | Success                         |
| gRPC             | HTTP/1.1         | Error                           |
| HTTP/1.1         | HTTP/2           | Error                           |
| HTTP/2           | HTTP/2           | Success                         |
| gRPC             | HTTP/2           | Success if targets support gRPC |
| HTTP/1.1         | gRPC             | Error                           |
| HTTP/2           | gRPC             | Success if a POST request       |
| gRPC             | gRPC             | Success                         |

###### Considerations for the gRPC protocol version

- The only supported listener protocol is HTTPS.
- The only supported target types are `INSTANCE` and
  `IP`.
- The service parses gRPC requests and routes the gRPC calls to the appropriate
  target groups based on the package, service, and method.
- You can't use Lambda functions as targets.

###### Considerations for the HTTP/2 protocol version

- The only supported listener protocol is HTTPS. You can choose either HTTP or
  HTTPS for the target group protocol.
- The only supported listener rules are forward and fixed response.
- The only supported target types are `INSTANCE` and
  `IP`.
- The service supports streaming from clients. The service does not support
  streaming to the targets.
