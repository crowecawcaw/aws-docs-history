# What is AWS PrivateLink?

AWS PrivateLink is a highly available, scalable technology that you can use to privately
connect your VPC to services and resources, as if they were in your VPC. You do not need to
use an internet gateway, NAT device, public IP address, AWS Direct Connect connection, or AWS Site-to-Site VPN
connection to allow communication with the service or resource from your private subnets.
Therefore, you control the specific API endpoints, sites, services, and resources that are
reachable from your VPC.

## Use cases

You can create VPC endpoints to connect clients in your VPC to services and resources
that integrate with AWS PrivateLink. You can create your own VPC endpoint service and
make it available to other AWS customers. For more information, see [AWS PrivateLink concepts](concepts.md "concepts.md").

In the following diagram, the VPC on the left has several Amazon EC2 instances in a private
subnet and five VPC endpoints - three interface VPC endpoints, a resource VPC endpoint
and a service-network VPC endpoint. The first interface VPC endpoint connects to an
AWS service. The second interface VPC endpoint connects to a service hosted by another
AWS account (a VPC endpoint service). The third interface VPC endpoint connects to an
AWS Marketplace partner service. The resource VPC endpoint connects to a database. The
service network VPC endpoint connects to a service network.

![Connect to an AWS service, an endpoint service in another AWS account, a partner service, a VPC resource, or VPC Lattice service network.](images/use-cases.png)

###### Learn more

- [Concepts](concepts.md "concepts.md")
- [Access
  AWS services](privatelink-access-aws-services.md "privatelink-access-aws-services.md")
- [Access SaaS products](privatelink-access-saas.md "privatelink-access-saas.md")
- [Access virtual appliances](vpce-gateway-load-balancer.md "vpce-gateway-load-balancer.md")
- [Share your services](privatelink-share-your-services.md "privatelink-share-your-services.md")

## Work with VPC endpoints

You can create, access, and manage VPC endpoints using any of the following:

- **AWS Management Console** — Provides a web interface
  that you can use to access your AWS PrivateLink resources. Open the Amazon VPC console
  and choose **Endpoints** or **Endpoint
  services**.
- **AWS Command Line Interface (AWS CLI)** — Provides commands
  for a broad set of AWS services, including AWS PrivateLink. For more information
  about commands for AWS PrivateLink, see [ec2](../../../cli/latest/reference/ec2/index.md "../../../cli/latest/reference/ec2/index.md") in the _AWS CLI Command Reference_.
- **AWS CloudFormation** - Create templates that describe your
  AWS resources. You use the templates to provision and manage these resources
  as a single unit. For more information, see the following AWS PrivateLink
  resources:
  - [AWS::EC2::VPCEndpoint](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.md")
  - [AWS::EC2::VPCEndpointConnectionNotification](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointconnectionnotification.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointconnectionnotification.md")
  - [AWS::EC2::VPCEndpointService](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservice.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservice.md")
  - [AWS::EC2::VPCEndpointServicePermissions](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservicepermissions.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservicepermissions.md")
  - [AWS::ElasticLoadBalancingV2::LoadBalancer](../../../AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-loadbalancer.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-loadbalancer.md")

- **AWS SDKs** — Provide language-specific
  APIs. The SDKs take care of many of the connection details, such as calculating
  signatures, handling request retries, and handling errors. For more information,
  see [Tools to Build on
  AWS](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/").
- **Query API** — Provides low-level API
  actions that you call using HTTPS requests. Using the Query API is the most
  direct way to access Amazon VPC. However, it requires that your application handle
  low-level details such as generating the hash to sign the request and handling
  errors. For more information, see [AWS PrivateLink
  actions](../../../AWSEC2/latest/APIReference/operation-list-privatelink.md "../../../AWSEC2/latest/APIReference/operation-list-privatelink.md") in the _Amazon EC2 API Reference_.

## Pricing

For information about the pricing for VPC endpoints, see [AWS PrivateLink Pricing](https://aws.amazon.com/privatelink/pricing/ "https://aws.amazon.com/privatelink/pricing/").
