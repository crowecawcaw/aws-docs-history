

# AWS Abuse Signal API and interface VPC endpoints (AWS PrivateLink)

You can establish a private connection between your VPC and AWS Abuse Signal API by creating an *interface VPC endpoint*. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink). With AWS PrivateLink, you can privately access AWS Abuse Signal API without an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. Instances in your VPC don’t need public IP addresses to communicate with AWS Abuse Signal API. Traffic between your VPC and AWS Abuse Signal API doesn’t leave the Amazon network.

Each interface endpoint is represented by one or more [Elastic network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in your subnets.

For more information, see [Access AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html) in the *Amazon VPC User Guide*.

## Considerations for AWS Abuse Signal API VPC endpoints
<a name="vpc-endpoint-considerations"></a>

Before you set up an interface VPC endpoint for AWS Abuse Signal API, review the prerequisites in [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *Amazon VPC User Guide*.

AWS Abuse Signal API supports making calls to all of its API actions from your VPC.

AWS Abuse Signal API supports interface VPC endpoints and VPC endpoint policies in all AWS Regions where AWS Abuse Signal API is available.

## Creating an interface VPC endpoint for AWS Abuse Signal API
<a name="vpc-endpoint-create"></a>

You can create a VPC endpoint for the AWS Abuse Signal API service using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *Amazon VPC User Guide*.

Create a VPC endpoint for AWS Abuse Signal API using the following service name:
+ com.amazonaws.{{region}}.abuse

If you enable private DNS for the endpoint, you can make API requests to AWS Abuse Signal API using the default DNS name for the Region. For example, use `abuse.us-east-1.amazonaws.com`.

**Note**  
Because the hostname is identical to the public endpoint, your client code and request signing do not change when you move to AWS PrivateLink; only DNS resolution differs. The operations, request/response shapes, and authentication are identical on both paths.

For more information, see [Access AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html) in the *Amazon VPC User Guide*.

## Creating a VPC endpoint policy for AWS Abuse Signal API
<a name="vpc-endpoint-policy"></a>

You can attach an endpoint policy to your VPC endpoint that controls access to AWS Abuse Signal API. The policy specifies the following information:
+ The principal that can perform actions.
+ The actions that can be performed.
+ The resources on which actions can be performed.

For more information, see [Control access to VPC endpoints using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *Amazon VPC User Guide*.

**Example: VPC endpoint policy for AWS Abuse Signal API actions**  
The following is an example of an endpoint policy for AWS Abuse Signal API. When attached to an endpoint, this policy grants access to the listed AWS Abuse Signal API actions for all principals on all resources.

```json
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "abuse:CreateAbuseReport",
            "abuse:GetAbuseReportStatus",
            "abuse:ListAbuseReportStatuses"
         ],
         "Resource":"*"
      }
   ]
}
```