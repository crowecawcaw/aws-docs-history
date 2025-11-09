AWS Migration Hub Refactor Spaces is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub Refactor Spaces, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Step 2: Create an application

This step describes how to create an application as part of the Refactor Spaces **Getting
started** wizard. You can also create an application by choosing **Create
application** under **Quick actions** in the Refactor Spaces navigation
pane.

Applications are containers of services and routes that provide multi-account traffic
routing for services in the application. When you create an application, you must provide
Refactor Spaces with a VPC to route traffic from the application to services with private URL
endpoints. For each application, Refactor Spaces orchestrate a proxy with an Amazon API Gateway connected to a
Network Load Balancer through a VPC link.

###### To create an application

1. On the **Create application** page, enter a name for your
   application.
2. Under **Proxy VPC**, choose a proxy virtual private cloud (VPC) or choose
   **Create VPC**.

An application’s proxy needs a VPC. The proxy’s Network Load Balancer is launched in the VPC and an API Gateway
VPC link is configured for the VPC and Network Load Balancer.

When creating an application in an environment without a network bridge, you need to
configure [VPC to VPC connectivity](../../../whitepapers/latest/aws-vpc-connectivity-options/amazon-vpc-to-amazon-vpc-connectivity-options.md "../../../whitepapers/latest/aws-vpc-connectivity-options/amazon-vpc-to-amazon-vpc-connectivity-options.md") between your service VPCs and the Refactor Spaces application proxy
VPC. 3. Under **Proxy endpoint type** select **Regional** or
**Private**.

The proxy’s endpoint can be either Regional or private. Regional API Gateway endpoints are
accessible through the public internet, and private API Gateway endpoints are only accessible through
VPCs. 4. Choose **Next** to move to the **Share environment**
page.
