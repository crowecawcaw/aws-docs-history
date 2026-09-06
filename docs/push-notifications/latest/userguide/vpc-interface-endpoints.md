

# Access AWS End User Messaging Push using an interface endpoint (AWS PrivateLink)
<a name="vpc-interface-endpoints"></a>

You can use AWS PrivateLink to create a private connection between your VPC and AWS End User Messaging Push. You can access AWS End User Messaging Push as if it were in your VPC, without the use of an internet gateway, NAT device, VPN connection, or Direct Connect connection. Instances in your VPC don't need public IP addresses to access AWS End User Messaging Push.

You establish this private connection by creating an *interface endpoint*, powered by AWS PrivateLink. We create an endpoint network interface in each subnet that you enable for the interface endpoint. These are requester-managed network interfaces that serve as the entry point for traffic destined for AWS End User Messaging Push.

For more information, see [Access AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html) in the *AWS PrivateLink Guide*.

## Considerations for AWS End User Messaging Push
<a name="vpc-endpoint-considerations"></a>

Before you set up an interface endpoint for AWS End User Messaging Push, review [Considerations](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#considerations-interface-endpoints) in the *AWS PrivateLink Guide*.

AWS End User Messaging Push supports making calls to all of its API actions through the interface endpoint.

VPC endpoint policies are not supported for AWS End User Messaging Push. By default, full access to AWS End User Messaging Push is allowed through the interface endpoint. Alternatively, you can associate a security group with the endpoint network interfaces to control traffic to AWS End User Messaging Push through the interface endpoint.

## Create an interface endpoint for AWS End User Messaging Push
<a name="vpc-endpoint-create"></a>

You can create an interface endpoint for AWS End User Messaging Push using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Create an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws) in the *AWS PrivateLink Guide*.

Create an interface endpoint for AWS End User Messaging Push using the following service name:

```
com.amazonaws.{{region}}.pinpoint
```

If you enable private DNS for the interface endpoint, you can make API requests to AWS End User Messaging Push using its default Regional DNS name. For example, `com.amazonaws.us-east-1.pinpoint`.

## Create an endpoint policy for your interface endpoint
<a name="vpc-endpoint-policy"></a>

An endpoint policy is an IAM resource that you can attach to an interface endpoint. The default endpoint policy allows full access to AWS End User Messaging Push through the interface endpoint. To control the access allowed to AWS End User Messaging Push from your VPC, attach a custom endpoint policy to the interface endpoint.

An endpoint policy specifies the following information:
+ The principals that can perform actions (AWS accounts, IAM users, and IAM roles).
+ The actions that can be performed.
+ The resources on which the actions can be performed.

For more information, see [Control access to services using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *AWS PrivateLink Guide*.

**Example: VPC endpoint policy for AWS End User Messaging Push actions**  
The following is an example of a custom endpoint policy. When you attach this policy to your interface endpoint, it grants access to the listed AWS End User Messaging Push actions for all principals on all resources.

```
{
   "Statement": [
      {
         "Principal": "*",
         "Effect": "Allow",
         "Action": [
             "mobiletargeting:CreateApp",
             "mobiletargeting:DeleteApp"
         ],
         "Resource":"*"
      }
   ]
}
```