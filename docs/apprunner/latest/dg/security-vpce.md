# Using App Runner with VPC endpoints

Your AWS application might integrate AWS App Runner services with other AWS services that run in a VPC from [Amazon Virtual Private Cloud](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md")
(Amazon VPC). Parts of your application might make requests to App Runner from within the VPC. For example, you might use AWS CodePipeline to continuously deploy to your App Runner
service. One way to improve the security of your application is to send these App Runner requests (and requests to other AWS services) over a VPC
endpoint.

Using a _VPC endpoint_, you can privately connect your VPC to supported AWS services and VPC endpoint services that are powered by
AWS PrivateLink. You don't need an internet gateway, NAT device, VPN connection, or Direct Connect connection.

Resources in your VPC don't use public IP addresses to interact with App Runner resources. Traffic between your VPC and App Runner doesn't leave the Amazon network.
For more information about VPC endpoints, see [VPC endpoints](../../../vpc/latest/privatelink/vpc-endpoints.md "../../../vpc/latest/privatelink/vpc-endpoints.md") in the
_AWS PrivateLink Guide_.

###### Note

By default, the web application in your App Runner service runs in a VPC that App Runner provides and configures. This VPC is public. It means that
it's connected to the internet. You can optionally associate your
application with a custom VPC. For more information, see [Enabling VPC access for outgoing traffic](network-vpc.md "network-vpc.md").

You can configure your services to access the internet, including AWS
APIs, even when your service is connected to a VPC. For instructions on how to enable public internet access for VPC outbound traffic, see [Considerations when selecting a subnet](network-vpc.md#network-vpc.considerations-subnet "network-vpc.md#network-vpc.considerations-subnet").

App Runner doesn't support creating a VPC endpoint for your application.

## Setting up a VPC endpoint for App Runner

To create the interface VPC endpoint for the App Runner service in your VPC, follow the [Create an interface endpoint](../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint") procedure in the
_AWS PrivateLink Guide_. For **Service Name**, choose
`com.amazonaws.`region`.apprunner`.

## VPC network privacy considerations

###### Important

Using a VPC endpoint for App Runner doesn't ensure that all traffic from your VPC stays off of the internet. The VPC might be public. Moreover, some parts
of your solution might not use VPC endpoints to make AWS API calls. For example, AWS services might call other services using their public
endpoints. If traffic privacy is required for the solution in your VPC, read this section.

To ensure privacy of network traffic in your VPC, consider the following:

- _Enable DNS name_ – Parts of your application might still send requests to App Runner over the internet using the
  `apprunner.`region`.amazonaws.com` public endpoint. If your VPC is configured with internet access, these
  requests succeed with no indication to you. You can prevent this by ensuring that **Enable DNS name** is enabled when you create the
  endpoint. By default, it's set to true. This adds a DNS entry in your VPC that maps the public service endpoint to the interface VPC endpoint.
- _Configure VPC endpoints for additional services_ – Your solution might send requests to other AWS services. For
  example, AWS CodePipeline might send requests to AWS CodeBuild. Configure VPC endpoints for these services, and enable DNS names on these endpoints.
- _Configure a private VPC_ – If possible (if your solution doesn't need internet access at all), set up your VPC as
  private, which means that it has no internet connection. This ensures that a missing VPC endpoint causes a visible error, so that you can add the
  missing endpoint.

## Using endpoint policies to control access with VPC endpoints

VPC endpoint policies are supported for App Runner. By default, full access to
App Runner is allowed through the interface endpoint. VPC endpoint policies can be used to control which AWS principals can access the App Runner endpoint.
Alternatively, you can associate a security group with the endpoint network interfaces to control traffic to App Runner
through the interface endpoint.

## Integrating with interface endpoint

App Runner supports AWS PrivateLink, which provides private connectivity to App Runner and eliminates exposure of traffic to the internet. To enable your application
to send requests to App Runner using AWS PrivateLink, configure a type of VPC endpoint known as an _interface endpoint_.
For more information, see [Interface VPC endpoints (AWS PrivateLink)](../../../vpc/latest/privatelink/vpce-interface.md "../../../vpc/latest/privatelink/vpce-interface.md") in the
_AWS PrivateLink Guide_.
