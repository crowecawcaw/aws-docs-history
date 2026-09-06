

# Amazon Detective and interface VPC endpoints (AWS PrivateLink)
<a name="detective-security-vpc-endpoints-privatelink"></a>

You can establish a private connection between your VPC and Amazon Detective by creating an *interface VPC endpoint*. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink), a technology that enables you to privately access Detective APIs without an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. Instances in your VPC don't need public IP addresses to communicate with Detective APIs. Traffic between your VPC and Detective does not leave the Amazon network. 

Each interface endpoint is represented by one or more [Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in your subnets. 

For more information, see [Interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html) in the *AWS PrivateLink Guide*. 

## Considerations for Detective VPC endpoints
<a name="vpc-endpoint-considerations"></a>

Before you set up an interface VPC endpoint for Detective, ensure that you review [Interface endpoint properties and limitations](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html#vpce-interface-limitations) in the *AWS PrivateLink Guide*. 

Detective supports making calls to all of its API actions from your VPC. 

Detective supports FIPS in the following Regions:
+ US East (N. Virginia)
+ US East (Ohio)
+ US West (N. California)
+ US West (Oregon)
+ Canada (Central)

## Creating an interface VPC endpoint for Detective
<a name="vpc-endpoint-create"></a>

You can create a VPC endpoint for the Detective service using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Create an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html#create-interface-endpoint) in the *AWS PrivateLink Guide*.

Create a VPC endpoint for Detective using the following service name:

 
+ com.amazonaws.{{region}}.detective
+ com.amazonaws.{{region}}.detective-fips

If you enable private DNS for the endpoint, you can make API requests to Detective using its default DNS name for the Region, for example, `api.detective.{{us-east-1}}.amazonaws.com`. For more information, see [Amazon Detective endpoints](https://docs.aws.amazon.com/general/latest/gr/detective.html) in the *Amazon Web Services General Reference*. 

For more information, see [Access a service through an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html#access-service-though-endpoint) in the *AWS PrivateLink Guide*.

## Creating a VPC endpoint policy for Detective
<a name="vpc-endpoint-policy"></a>

You can attach an endpoint policy to your VPC endpoint that controls access to Detective. The policy specifies the following information:
+ The principal that can perform actions.
+ The actions that can be performed.
+ The resources on which actions can be performed.

For more information, see [Control access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *AWS PrivateLink Guide*. 

**Example: VPC endpoint policy for Detective actions**  
The following is an example of an endpoint policy for Detective. When attached to an endpoint, this policy grants access to the listed Detective actions for all principals on all resources.

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "detective:ListGraphs",
            "detective:ListMembers"
         ],
         "Resource":"*"
      }
   ]
}
```

## Shared subnets
<a name="sh-vpc-endpoint-shared-subnets"></a>

You can't create, describe, modify, or delete VPC endpoints in subnets that are shared with you. However, you can use the VPC endpoints in subnets that are shared with you. For information about VPC sharing, see [Share your VPC with other accounts](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-sharing.html) in the *Amazon VPC User Guide*.