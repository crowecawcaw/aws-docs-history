# Use Amazon VPC Lattice to connect, observe, and secure your Amazon ECS

services

Amazon VPC Lattice is a fully managed application networking service that enables Amazon ECS customers to observe, secure, and
monitor applications built across AWS compute services, VPCs, and accounts—without requiring any code changes.

VPC Lattice uses target groups, which are a collection of compute resources. These targets run your
application or service and can be Amazon EC2 instances, IP addresses, Lambda functions, and Application Load Balancers. By
associating their Amazon ECS services with a VPC Lattice target group, customers can now enable Amazon ECS tasks as IP
targets in VPC Lattice. Amazon ECS automatically registers tasks to the VPC Lattice target group when tasks for the
registered service are launched.

###### Note

When using five VPC Lattice configurations, your deployment time may be slightly longer than when using
fewer configurations.

A listener rule is used to forward traffic to a specified target group when the conditions are met. A
listener checks for connection requests using the protocol on the port you configured. A service routes
requests to it's registered targets based on the rules that you define when you configured your
listener.

Amazon ECS also automatically replaces a task if it becomes unhealthy according to VPC Lattice health checks.
Once associated with VPC Lattice, Amazon ECS customers can also take advantage of many other cross-compute
connectivity, security, and observability features in VPC Lattice like connecting to services across clusters,
VPCs, and accounts with AWS Resource Access Manager, IAM integration for authorization and authentication, and advanced
traffic management features.

Amazon ECS customers can benefit from VPC Lattice in the following ways.

- Increased developer productivity ‐ VPC Lattice boosts developer productivity by letting you
  focus on building features, while VPC Lattice handles networking, security and observability
  challenges in a uniform way across all compute platforms.
- Better security posture ‐ VPC Lattice enables your developers to easily authenticate and secure
  communication across applications and compute platforms, enforce encryption in transit, and apply
  granular access controls with VPC Lattice Auth policies. This allows you to adopt a stronger security
  posture that meets industry leading regulatory and compliance requirements.
- Improved application scalability and resilience ‐ VPC Lattice lets you create a network of
  deployed applications with features like path, header, and method-based routing, authentication,
  authorization, and monitoring. These benefits are provided with no resource overhead on workloads
  and can support multi-cluster deployments that generate millions of requests per second without
  adding significant latency.
- Deployment flexibility with heterogeneous infrastructure ‐ VPC Lattice provides consistent
  features across all compute services like Amazon ECS, Fargate, Amazon EC2, Amazon EKS, and Lambda and allows your
  organization the flexibility to choose suitable infrastructure for each application.

## How VPC Lattice works with other Amazon ECS services

Using VPC Lattice with Amazon ECS may change the way you use other Amazon ECS services, while others stay the
same.

###### Application Load Balancers

You no longer need to create a specific Application Load Balancer to use with the Application Load Balancer target group type in VPC Lattice
that then links to the Amazon ECS service. You only need to configure your Amazon ECS service with a VPC Lattice
target group instead. You can also still choose to use Application Load Balancer with Amazon ECS at the same time.

###### Amazon ECS rolling deployments

Only Amazon ECS rolling deployments work with VPC Lattice, and Amazon ECS safely brings tasks into and removes them
from services during deployment. Code deploy and Blue/Green deployments aren't supported.

To learn more about VPC Lattice, see the [Amazon VPC Lattice User Guide](../../../vpc-lattice/latest/ug/what-is-vpc-lattice.md "../../../vpc-lattice/latest/ug/what-is-vpc-lattice.md").

###### Note

VPC Lattice isn't supported on Amazon ECS Anywhere.
