

# Amazon GuardDuty and interface VPC endpoints (AWS PrivateLink)
<a name="security-vpc-endpoints"></a>

You can establish a private connection between your VPC and Amazon GuardDuty by creating an *interface VPC endpoint*. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink), a technology that enables you to privately access GuardDuty APIs without an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. Instances in your VPC don't need public IP addresses to communicate with GuardDuty APIs. Traffic between your VPC and GuardDuty does not leave the Amazon network. 

Each interface endpoint is represented by one or more [Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in your subnets. 

For more information, see [Interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html) in the *AWS PrivateLink Guide*. 

## Considerations for GuardDuty VPC endpoints
<a name="vpc-endpoint-considerations"></a>

Before you set up an interface VPC endpoint for GuardDuty, ensure that you review [Interface endpoint properties and limitations](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html#vpce-interface-limitations) in the *AWS PrivateLink Guide*. 

GuardDuty supports making calls to all of its API actions from your VPC. 

## Creating an interface VPC endpoint for GuardDuty
<a name="vpc-endpoint-create"></a>

You can create a VPC endpoint for the GuardDuty service using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Create an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html#create-interface-endpoint) in the *AWS PrivateLink Guide*.

Create a VPC endpoint for GuardDuty using the following service name:

 
+ com.amazonaws.{{region}}.guardduty
+ com.amazonaws.{{region}}.guardduty-fips (FIPS endpoint)

If you enable private DNS for the endpoint, you can make API requests to GuardDuty using its default DNS name for the Region, for example, `guardduty.us-east-1.amazonaws.com`. 

For more information, see [Access a service through an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html#access-service-though-endpoint) in the *AWS PrivateLink Guide*.

## Creating a VPC endpoint policy for GuardDuty
<a name="vpc-endpoint-policy"></a>

You can attach an endpoint policy to your VPC endpoint that controls access to GuardDuty. The policy specifies the following information:
+ The principal that can perform actions.
+ The actions that can be performed.
+ The resources on which actions can be performed.

For more information, see [Control access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *AWS PrivateLink Guide*. 

**Example: VPC endpoint policy for GuardDuty actions**  
The following is an example of an endpoint policy for GuardDuty. When attached to an endpoint, this policy grants access to the listed GuardDuty actions for all principals on all resources.

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "guardduty:listDetectors",
            "guardduty:getDetector",
            "guardduty:getFindings"
         ],
         "Resource":"*"
      }
   ]
}
```

## Shared subnets
<a name="sh-vpc-endpoint-shared-subnets"></a>

You can't create, describe, modify, or delete VPC endpoints in subnets that are shared with you. However, you can use the VPC endpoints in subnets that are shared with you. For information about VPC sharing, see [Share your VPC with other accounts](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-sharing.html) in the *Amazon VPC User Guide*.