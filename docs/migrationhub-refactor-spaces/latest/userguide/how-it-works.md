AWS Migration Hub Refactor Spaces will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub Refactor Spaces, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# How Refactor Spaces works

When you start to use AWS Migration Hub Refactor Spaces, you can use one or more AWS accounts. You can use a
single account for testing. However, when you're ready to refactor, we recommend that you
start with the following three accounts:

- One account for the existing application.
- One account for the first new microservice.
- One account to act as the refactor _environment owner_ where
  Refactor Spaces configures cross-account networking and routes traffic.
  First, you create a Refactor Spaces environment in the account that you choose as the
  environment owner. Then, you share the environment with the other two accounts with
  AWS Resource Access Manager. The Refactor Spaces console does this for you. Refactor Spaces automatically shares the
  resources that it creates within the environment with the other accounts. To do this, it
  orchestrates AWS Identity and Access Management (IAM) resource-based policies.

The refactor environment provides unified networking across accounts. To do this, it
orchestrates Amazon API Gateway, a Network Load Balancer, AWS Transit Gateway, AWS Resource Access Manager, and security groups. The refactor
environment contains your existing application and new microservices. After you create a
refactor environment, you create a Refactor Spaces application within the environment. The
Refactor Spaces application contains services and routes, and it provides a single endpoint to
expose the application to external callers.

An application supports routing to services that run in containers, serverless compute,
and Amazon Elastic Compute Cloud (Amazon EC2) with public or private visibility. Services within an application can
have one of two endpoint types: a URL (HTTP and HTTPS) in a VPC, or an AWS Lambda function.
After an application contains a service, you add a default route to direct all traffic from
the application proxy to the service that represents the existing application. As you break
out or add new capabilities in containers or serverless compute, you add new services and
routes to redirect traffic to the new services.

When you create the default route, it defaults to an active state. You can toggle the
route to the inactive state to stop sending traffic to the default route. To send the
traffic to a new route, create a new route in an active state, or activate a route that is
inactive.

For services with URL endpoints in a VPC, Refactor Spaces uses Transit Gateway to automatically bridge
all service VPCs within the environment. This means that any AWS resources that you launch
in a service VPC can communicate directly with all other service VPCs that you add to the
environment. To route traffic to service endpoints with private URLs when you create
environments without a transit gateway, you must configure VPC to VPC connectivity between
your network infrastructure and the Refactor Spaces application VPC. You can apply
additional cross-account routing constraints with VPC security groups. When you create
routes that point to services with Lambda endpoints, Refactor Spaces orchestrates Amazon API Gateway Lambda
integration to call the function across AWS accounts.

###### Environments without a network bridge

You can create environments without a network bridge so that you can use your existing
network infrastructure to bridge communications across multiple AWS accounts. When you
create an application in an environment without a bridge, you must connect your network
infrastructure to the application proxy to route traffic to service endpoints with
private URLs. You can connect VPCs across accounts in several ways, including [VPC
Peering](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md"), [Transit Gateway](../../../vpc/latest/tgw/what-is-transit-gateway.md "../../../vpc/latest/tgw/what-is-transit-gateway.md"), or [AWS PrivateLink](vpc-interface-endpoints.md "vpc-interface-endpoints.md").
For more information, see the [Amazon VPC-to-Amazon VPC connectivity options](../../../whitepapers/latest/aws-vpc-connectivity-options/amazon-vpc-to-amazon-vpc-connectivity-options.md "../../../whitepapers/latest/aws-vpc-connectivity-options/amazon-vpc-to-amazon-vpc-connectivity-options.md") in the _Amazon
Virtual Private Cloud Connectivity Options_ AWS whitepaper.
