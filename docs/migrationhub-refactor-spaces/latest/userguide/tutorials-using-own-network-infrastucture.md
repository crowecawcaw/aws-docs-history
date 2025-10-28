AWS Migration Hub Refactor Spaces will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub Refactor Spaces, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Tutorials for using Refactor Spaces

with your own network infrastructure

When you use a Refactor Spaces environment without a network bridge, you must configure [VPC to VPC connectivity](../../../whitepapers/latest/aws-vpc-connectivity-options/amazon-vpc-to-amazon-vpc-connectivity-options.md "../../../whitepapers/latest/aws-vpc-connectivity-options/amazon-vpc-to-amazon-vpc-connectivity-options.md") between services with private URL endpoints and an
application proxy VPC. The following tutorials show two common scenarios: connecting through
VPC peering, and through your own transit gateway.

We use two accounts for the tutorials, an environment owner account and a service account.
The service account contains the private service. In the tutorials, this is an Amazon EC2 web
server. Its service VPC is configured to connect with the environment’s application proxy
VPC.

For the VPC peering scenario, traffic that targets services with private URL endpoints,
flows from the application proxy VPC to your service VPC. When you use your own transit
gateway, traffic that targets services with private URL endpoints, flows from the
application proxy VPC to your network through the transit gateway.

For both scenarios, we provide sample CIDR ranges and port numbers. You can use the values
that apply to your configuration.

To avoid connectivity errors, make sure that your VPC CIDR ranges don’t overlap with the
Refactor Spaces application proxy VPC.
