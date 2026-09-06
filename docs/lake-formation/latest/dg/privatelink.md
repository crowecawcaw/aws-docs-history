

# AWS Lake Formation and interface VPC endpoints (AWS PrivateLink)
<a name="privatelink"></a>

Amazon VPC is an AWS service that you can use to launch AWS resources in a virtual network that you define. With a VPC, you have control over your network settings, such the IP address range, subnets, route tables, and network gateways. 

If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can establish a private connection between your VPC and Lake Formation. You use this connection so that Lake Formation can communicate with the resources in your VPC without going through the public internet.

You can establish a private connection between your VPC and AWS Lake Formation by creating an *interface VPC endpoint*. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink), a technology that enables you to privately access Lake Formation APIs without an internet gateway, NAT device, VPN connection, or Direct Connect connection. Instances in your VPC don't need public IP addresses to communicate with Lake Formation APIs. Traffic between your VPC and Lake Formation does not leave the Amazon network. 

Each interface endpoint is represented by one or more [Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in your subnets. 

For more information, see [Interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html) in the *Amazon VPC User Guide*. 

## Considerations for Lake Formation VPC endpoints
<a name="vpc-endpoint-considerations"></a>

Before you set up an interface VPC endpoint for Lake Formation, ensure that you review [Interface endpoint properties and limitations](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#vpce-interface-limitations) in the *Amazon VPC User Guide*. 

Lake Formation supports making calls to all of its API actions from your VPC. You can use Lake Formation with VPC endpoints in all AWS Regions that support both Lake Formation and Amazon VPC endpoints. 

## Creating an interface VPC endpoint for Lake Formation
<a name="vpc-endpoint-create"></a>

You can create a VPC endpoint for the Lake Formation service using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint) in the *Amazon VPC User Guide*.

Create a VPC endpoint for Lake Formation using the following service name: 
+ com.amazonaws.{{region}}.lakeformation 

If you enable private DNS for the endpoint, you can make API requests to Lake Formation using its default DNS name for the Region, for example, `lakeformation.us-east-1.amazonaws.com`. 

For more information, see [Accessing a service through an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#access-service-though-endpoint) in the *Amazon VPC User Guide*.

## Creating a VPC endpoint policy for Lake Formation
<a name="vpc-endpoint-policy"></a>

Lake Formation supports VPC endpoint policies. An endpoint policy is a resource-based policy that you attach to a VPC endpoint to control which AWS principals can use the endpoint to access an AWS service. 

You can attach an endpoint policy to your VPC endpoint that controls access to Lake Formation. The policy specifies the following information:
+ The principal that can perform actions.
+ The actions that can be performed.
+ The resources on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the *Amazon VPC User Guide*. 

**Example: VPC endpoint policy for Lake Formation actions**

The following example VPC endpoint policy for Lake Formation allows for credential vending using Lake Formation permissions. You might use this policy to run queries using Lake Formation permissions from an Amazon Redshift cluster or an Amazon EMR cluster located in a private subnet.

```
{
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "lakeformation:GetDataAccess",
            "Resource": "*",
            "Principal": "*"
        }
    ]
}
```

**Note**  
If you don't attach a policy when you create an endpoint, a default policy that allows full access to the service is attached.

For more information, see these topics in the Amazon VPC documentation:
+ [What Is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
+ [Create an Interface Endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html#create-interface-endpoint)
+ [Use VPC endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html#vpc-endpoint-policies)