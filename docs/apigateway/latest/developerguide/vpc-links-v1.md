# Private integration using VPC links V1 (legacy)

###### Note

The following implementation of private integrations uses VPC links V1. VPC links V1 are legacy resources. We recommend
that you use [VPC links V2 for REST APIs](apigateway-vpc-links-v2.md "apigateway-vpc-links-v2.md").

To create a private integration, you must first create a Network Load Balancer. Your Network Load Balancer must have a [listener](../../../elasticloadbalancing/latest/network/load-balancer-listeners.md "../../../elasticloadbalancing/latest/network/load-balancer-listeners.md")
that routes requests to resources in your VPC. To improve the availability of your API, ensure that your Network Load Balancer
routes traffic to resources in more than one Availability Zone in the AWS Region. Then, you create a VPC link
that you use to connect your API and your Network Load Balancer. After you create a VPC link, you create private integrations to
route traffic from your API to resources in your VPC through your VPC link and Network Load Balancer. The Network Load Balancer and
API must be owned by the same AWS account.

###### Topics

- [Set up a Network Load Balancer
  for API Gateway private integrations (legacy)](set-up-nlb-for-vpclink-using-console.md "set-up-nlb-for-vpclink-using-console.md")
- [Grant permissions for API Gateway to create a VPC
  link (legacy)](grant-permissions-to-create-vpclink.md "grant-permissions-to-create-vpclink.md")
- [Set up an API Gateway API with private
  integrations using the AWS CLI (legacy)](set-up-api-with-vpclink-cli.md "set-up-api-with-vpclink-cli.md")
- [API Gateway accounts used for private integrations (legacy)](set-up-api-with-vpclink-accounts.md "set-up-api-with-vpclink-accounts.md")
