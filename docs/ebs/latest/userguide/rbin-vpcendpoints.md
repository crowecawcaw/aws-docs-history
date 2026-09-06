

# Create a private connection between a VPC and Recycle Bin
<a name="rbin-vpcendpoints"></a>

You can establish a private connection between your VPC and Recycle Bin by creating an interface VPC endpoint, powered by [AWS PrivateLink](https://aws.amazon.com/privatelink/). You can access Recycle Bin as if it were in your VPC, without using an internet gateway, NAT device, VPN connection, or Direct Connect connection. Instances in your VPC don't need public IP addresses to communicate with Recycle Bin.

We create an endpoint network interface in each subnet that you enable for the interface endpoint.

For more information, see [ Access AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html) in the *AWS PrivateLink Guide*.

## Create an interface VPC endpoint for Recycle Bin
<a name="rbin-vpcendpoint-create"></a>

You can create a VPC endpoint for Recycle Bin using either the Amazon VPC console or the AWS CLI. For more information, see [ Create a VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws) in the *AWS PrivateLink Guide*.

Create a VPC endpoint for Recycle Bin using the following service name: `com.amazonaws.{{region}}.rbin`

If you enable private DNS for the endpoint, you can make API requests to Recycle Bin using its default DNS name for the Region, for example, `rbin.us-east-1.amazonaws.com`.

## Create a VPC endpoint policy for Recycle Bin
<a name="rbin-vpcendpoint-policy"></a>

By default, full access to Recycle Bin is allowed through the endpoint. You can control access to the interface endpoint using VPC endpoint policies. You can attach an endpoint policy to your VPC endpoint that controls access to Recycle Bin. The policy specifies the following information:
+ The **principal** that can perform actions.
+ The **actions** that can be performed.
+ The **resources** on which actions can be performed.

For more information, see [ Controlling access to services with VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html)s in the *Amazon VPC User Guide*.

```
{
    "Statement": [ 
    {
        "Effect": "Allow",
        "Action": "rbin:*",        
        "Resource": "*", 
        "Principal": "*" 
    }, 
    {
        "Effect": "Deny",
        "Action": "rbin:DeleteRule",
        "Resource": "*", 
        "Principal": "*",
        "Condition": {
            "StringEquals" : {
                "rbin:Attribute/ResourceType": "EBS_SNAPSHOT"
            }
        }
    }] 
}
```