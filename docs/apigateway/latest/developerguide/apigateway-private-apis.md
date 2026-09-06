

# Private REST APIs in API Gateway
<a name="apigateway-private-apis"></a>

A private API is a REST API that is only callable from within an Amazon VPC. You can access your API using an [interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html), which is an endpoint network interface that you create in your VPC. Interface endpoints are powered by AWS PrivateLink, a technology that enables you to privately access AWS services by using private IP addresses.

You can also use Direct Connect to establish a connection from an on-premises network to Amazon VPC and then access your private API over that connection. In all cases, traffic to your private API uses secure connections and is isolated from the public internet. Traffic doesn't leave the Amazon network.

## Best practices for private APIs
<a name="apigateway-private-api-best-practices"></a>

We recommend that you use the following best practices when you create your private API:
+ Use a single VPC endpoint to access multiple private APIs. This reduces the number of VPC endpoints that you might need.
+ Associate your VPC endpoint to your API. This creates a Route 53 alias DNS record and simplifies invoking your private API.
+ Turn on private DNS for your VPC. When you turn on private DNS for your VPC, you can invoke your API within a VPC without passing the `Host` or `x-apigw-api-id` header.

  If you turn on private DNS, you can’t access the default endpoint for public APIs. To access the default endpoint for public APIs, you can turn off private DNS, create a private hosted zone for each private API in your VPC, and then provision the required records in Route 53. This allows your private API to resolve while you can still invoke public default endpoint from your VPC. For more information, see [Creating a private hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-creating.html).
+ Restrict access to your private API to specific VPCs or VPC endpoints. Add `aws:SourceVpc` or `aws:SourceVpce` conditions to your API's resource policy to restrict access.
+ For the most secure data perimeter, you can create a VPC endpoint policy. This controls access to the VPC endpoints that can invoke your private API.

## Considerations for private APIs
<a name="apigateway-private-api-considerations"></a>

The following considerations might impact your use of private APIs:
+ Only REST APIs are supported.
+ You cannot convert a private API to an edge-optimized API.
+ Private APIs only support TLS 1.2. Earlier TLS versions are not supported.
+ If you make a request using HTTP/2 protocol, the request is enforced to use HTTP/1.1 protocol.
+ You can't set the IP address type for private APIs to only allow IPv4 addresses to invoke your private API. Only dualstack is supported. For more information, see [IP address types for REST APIs in API Gateway](api-gateway-ip-address-type.md).
+ To send traffic using your private API, you can use all IP address types supported by Amazon VPC. You can send dualstack and IPv6 traffic by configuring the settings on your VPC endpoint. You can't modify this using API Gateway. For more information, see [Add IPv6 support for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-migrate-ipv6-add.html).
+ VPC endpoints for private APIs are subject to the same limitations as other interface VPC endpoints. For more information, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *AWS PrivateLink Guide*. For more information about using API Gateway with shared VPCs and shared subnets, see [Shared subnets](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#interface-endpoint-shared-subnets) in the *AWS PrivateLink Guide*.

## Next steps for private APIs
<a name="apigateway-private-api-next-steps"></a>

 To learn how to create a private API and associate a VPC endpoint see, [Create a private API](apigateway-private-api-create.md). To follow a tutorial where you create dependencies in CloudFormation and a private API in the AWS Management Console, see [Tutorial: Create a private REST API](private-api-tutorial.md).