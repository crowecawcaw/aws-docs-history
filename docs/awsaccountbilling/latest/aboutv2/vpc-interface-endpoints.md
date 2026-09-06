

# Access AWS Billing and Cost Management using an interface endpoint (AWS PrivateLink)
<a name="vpc-interface-endpoints"></a>

You can use AWS PrivateLink to create a private connection between your VPC and AWS Billing and Cost Management. You can access Billing and Cost Management as if it were in your VPC, without the use of an internet gateway, NAT device, VPN connection, or Direct Connect connection. Instances in your VPC don't need public IP addresses to access Billing and Cost Management.

You establish this private connection by creating an *interface endpoint*, powered by AWS PrivateLink. We create an endpoint network interface in each subnet that you enable for the interface endpoint. These are requester-managed network interfaces that serve as the entry point for traffic destined for Billing and Cost Management.

For more information, see [Access AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html) in the *AWS PrivateLink Guide*.

For a complete list of service names, see [AWS services that integrate with AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/aws-services-privatelink-support.html).

## Considerations for Billing and Cost Management
<a name="vpc-endpoint-considerations"></a>

Before you set up an interface endpoint for Billing and Cost Management, review [Considerations](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#considerations-interface-endpoints) in the *AWS PrivateLink Guide*.

Billing and Cost Management supports making calls to all of its API actions through the interface endpoint.

VPC endpoint policies are not supported for Billing and Cost Management. By default, full access to Billing and Cost Management is allowed through the interface endpoint. Alternatively, you can associate a security group with the endpoint network interfaces to control traffic to Billing and Cost Management through the interface endpoint.

## Create an interface endpoint for Billing and Cost Management
<a name="vpc-endpoint-create"></a>

You can create an interface endpoint for Billing and Cost Management using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Create an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws) in the *AWS PrivateLink Guide*.

Create an interface endpoint for Billing and Cost Management using the following service name:

```
com.amazonaws.{{region}}.service-name
```

If you enable private DNS for the interface endpoint, you can make API requests to Billing and Cost Management using its default Regional DNS name. For example, `service-name.us-east-1.amazonaws.com`.

## Create an endpoint policy for your interface endpoint
<a name="vpc-endpoint-policy"></a>

An endpoint policy is an IAM resource that you can attach to an interface endpoint. The default endpoint policy allows full access to Billing and Cost Management through the interface endpoint. To control the access allowed to Billing and Cost Management from your VPC, attach a custom endpoint policy to the interface endpoint.

An endpoint policy specifies the following information:
+ The principals that can perform actions (AWS accounts, IAM users, and IAM roles).
+ The actions that can be performed.
+ The resources on which the actions can be performed.

For more information, see [Control access to services using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *AWS PrivateLink Guide*.

**Example: VPC endpoint policy for AWS Price List API**  
The following is an example of a custom endpoint policy. When you attach this policy to your interface endpoint, all users that have access to the endpoint are can access AWS Price List API.

```
{
    "Statement": [
        {
            "Action": "pricing:*",
            "Effect": "Allow",
            "Principal": "*",
            "Resource": "*"
        }
    ]
}
```

To use the bulk file download for Price List API through AWS PrivateLink, you must also enable Amazon S3 access through AWS PrivateLink. For more information, see [AWS PrivateLink for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html) in the *Amazon S3 User Guide*.