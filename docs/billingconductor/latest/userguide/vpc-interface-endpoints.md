

# Access AWS Billing Conductor using an interface endpoint (AWS PrivateLink)
<a name="vpc-interface-endpoints"></a>

You can use AWS PrivateLink to create a private connection between your VPC and AWS Billing Conductor. You can access Billing Conductor as if it were in your VPC, without the use of an internet gateway, NAT device, VPN connection, or Direct Connect connection. Instances in your VPC don't need public IP addresses to access Billing Conductor.

You establish this private connection by creating an *interface endpoint*, powered by AWS PrivateLink. We create an endpoint network interface in each subnet that you enable for the interface endpoint. These are requester-managed network interfaces that serve as the entry point for traffic destined for Billing Conductor.

For more information, see [Access AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html) in the *AWS PrivateLink Guide*.

## Considerations for Billing Conductor
<a name="vpc-endpoint-considerations"></a>

Before you set up an interface endpoint for Billing Conductor, review [Considerations](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#considerations-interface-endpoints) in the *AWS PrivateLink Guide*.

Billing Conductor supports making calls to all of its API actions through the interface endpoint.

VPC endpoint policies are not supported for Billing Conductor. By default, full access to Billing Conductor is allowed through the interface endpoint. Alternatively, you can associate a security group with the endpoint network interfaces to control traffic to Billing Conductor through the interface endpoint.

## Create an interface endpoint for Billing Conductor
<a name="vpc-endpoint-create"></a>

You can create an interface endpoint for Billing Conductor using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Create an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws) in the *AWS PrivateLink Guide*.

Create an interface endpoint for Billing Conductor using the following service name:

```
com.amazonaws.{{region}}.service-name
```

If you enable private DNS for the interface endpoint, you can make API requests to Billing Conductor using its default Regional DNS name. For example, `service-name.us-east-1.amazonaws.com`.

## Create an endpoint policy for your interface endpoint
<a name="vpc-endpoint-policy"></a>

An endpoint policy is an IAM resource that you can attach to an interface endpoint. The default endpoint policy allows full access to Billing Conductor through the interface endpoint. To control the access allowed to Billing Conductor from your VPC, attach a custom endpoint policy to the interface endpoint.

An endpoint policy specifies the following information:
+ The principals that can perform actions (AWS accounts, IAM users, and IAM roles).
+ The actions that can be performed.
+ The resources on which the actions can be performed.

For more information, see [Control access to services using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *AWS PrivateLink Guide*.

**Example: VPC endpoint policy for Billing Conductor actions**  
The following is an example of a custom endpoint policy. When you attach this policy to your interface endpoint, it grants access to the listed Billing Conductor actions for all principals on all resources.

```
{
   "Statement": [
      {
         "Principal": "*",
         "Effect": "Allow",
         "Action": "billingconductor:*",
         "Resource":"*"
      }
   ]
}
```