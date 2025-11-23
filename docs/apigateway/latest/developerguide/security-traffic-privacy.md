# Internetwork traffic privacy

Using Amazon API Gateway, you can create private REST APIs that can be accessed only from your
Amazon Virtual Private Cloud (VPC). The VPC uses an [interface
VPC endpoint](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md"), which is an endpoint network interface that you create in your
VPC. Using [resource
policies](apigateway-private-api-create.md#apigateway-private-api-set-up-resource-policy "apigateway-private-api-create.md#apigateway-private-api-set-up-resource-policy"), you can allow or deny access to your API from selected VPCs and VPC
endpoints, including across AWS accounts. Each endpoint can be used to access multiple
private APIs. You can also use Direct Connect to establish a connection from an on-premises
network to Amazon VPC and access your private API over that connection. In all cases, traffic to
your private API uses secure connections and does not leave the Amazon network; it is
isolated from the public internet. To learn more, see [Private REST APIs in API Gateway](apigateway-private-apis.md "apigateway-private-apis.md").
