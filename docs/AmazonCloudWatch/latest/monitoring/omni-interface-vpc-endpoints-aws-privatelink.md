

# Interface VPC endpoints (AWS PrivateLink)
<a name="omni-interface-vpc-endpoints-aws-privatelink"></a>

You can establish a private connection between your virtual private cloud (VPC) and CloudWatch Omni by creating an *interface VPC endpoint*. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink/), which you can use to privately access CloudWatch Omni without an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. Instances in your VPC do not need public IP addresses to communicate with the service, and traffic between your VPC and CloudWatch Omni does not leave the AWS network.

Each interface endpoint is represented by one or more [elastic network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in your subnets.

For more information, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *AWS PrivateLink Guide*.

**Endpoint services for CloudWatch Omni**

CloudWatch Omni offers two VPC endpoint services. Create an interface endpoint for each service that you use.


| Endpoint service name | Private DNS name | What it carries | 
| --- | --- | --- | 
| com.amazonaws.{region}.cloudwatch-omni | cloudwatch-omni.{region}.api.aws | The CloudWatch Omni API and telemetry ingestion | 
| com.amazonaws.{region}.cloudwatch-omni-threads | cloudwatch-omni-threads.{region}.api.aws | The WebSocket session that the Omni agent uses, on port 8443 | 

Both endpoint services support private DNS and VPC endpoint policies. Because each private DNS name is the same as the corresponding public hostname, a client in a VPC that has the interface endpoint reaches the service privately with no change to its configuration.

**Considerations for CloudWatch Omni VPC endpoints**

Before you set up an interface VPC endpoint for CloudWatch Omni, review [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *AWS PrivateLink Guide*.
+ The endpoint provides private access to the CloudWatch Omni service endpoint `cloudwatch-omni.{region}.api.aws`, for both the API and telemetry ingestion. All communication uses TLS. The endpoint requires a minimum of TLS 1.2 and supports TLS 1.3 with post-quantum hybrid key exchange.
+ The endpoint is a dual-stack endpoint, supporting both IPv4 and IPv6.
+ CloudWatch Omni supports private DNS for the endpoint. When you enable private DNS, requests to the default service hostname `cloudwatch-omni.{region}.api.aws` resolve to your interface endpoint automatically, so you do not have to change your client endpoint configuration.
+ CloudWatch Omni supports VPC endpoint policies. See the "Create a VPC endpoint policy for CloudWatch Omni" section of this page.
+ The endpoint is available in the AWS Regions where CloudWatch Omni is available.

**Create an interface VPC endpoint for CloudWatch Omni**

You can create an interface VPC endpoint for CloudWatch Omni using either the Amazon VPC console or the AWS Command Line Interface. For more information, see [Create an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws) in the *AWS PrivateLink Guide*.

Create an interface VPC endpoint for CloudWatch Omni using the following service name:

```
com.amazonaws.{region}.cloudwatch-omni
```

For example, in US East (N. Virginia):

```
com.amazonaws.us-east-1.cloudwatch-omni
```

If you enable private DNS for the endpoint, you can make API and telemetry-ingestion requests to CloudWatch Omni using its default DNS name for the Region, `cloudwatch-omni.{region}.api.aws`, and they route through the interface endpoint.

**Create a VPC endpoint policy for CloudWatch Omni**

You can attach an endpoint policy to your VPC endpoint that controls access to CloudWatch Omni. The policy specifies the following information:
+ The principal that can perform actions.
+ The actions that can be performed.
+ The resources on which actions can be performed.

By default, full access to CloudWatch Omni is allowed through the endpoint. To restrict access, attach a custom endpoint policy to the interface endpoint. For more information, see [Control access to services using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *AWS PrivateLink Guide*.