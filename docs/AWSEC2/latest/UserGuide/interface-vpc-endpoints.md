

# Access Amazon EC2 using an interface VPC endpoint
<a name="interface-vpc-endpoints"></a>

You can improve the security posture of your VPC by creating a private connection between resources in your VPC and the Amazon EC2 API. You can access the Amazon EC2 API as if it were in your VPC, without the use of an internet gateway, NAT device, VPN connection, or Direct Connect connection. EC2 instances in your VPC don't need public IP addresses to access the Amazon EC2 API.

For more information, see [Access AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html) in the *AWS PrivateLink Guide*.

**Topics**
+ [Create an interface VPC endpoint](#create-endpoint)
+ [Create an endpoint policy](#endpoint-policy)

## Create an interface VPC endpoint
<a name="create-endpoint"></a>

Create an interface endpoint for Amazon EC2 using the following service name:
+ **com.amazonaws.{{region}}.ec2** — Creates an endpoint for the Amazon EC2 API actions.

For more information, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *AWS PrivateLink Guide*.

## Create an endpoint policy
<a name="endpoint-policy"></a>

An endpoint policy is an IAM resource that you can attach to your interface endpoint. The default endpoint policy allows full access to the Amazon EC2 API through the interface endpoint. To control the access allowed to the Amazon EC2 API from your VPC, attach a custom endpoint policy to the interface endpoint.

An endpoint policy specifies the following information:
+ The principals that can perform actions.
+ The actions that can be performed.
+ The resource on which the actions can be performed.

**Important**  
When a non-default policy is applied to an interface VPC endpoint for Amazon EC2, certain failed API requests, such as those failing from `RequestLimitExceeded`, might not be logged to AWS CloudTrail or Amazon CloudWatch.

For more information, see [ Control access to services using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *AWS PrivateLink Guide*.

The following example shows a VPC endpoint policy that denies permission to create unencrypted volumes or to launch instances with unencrypted volumes. The example policy also grants permission to perform all other Amazon EC2 actions.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
    {
        "Action": "ec2:*",
        "Effect": "Allow",
        "Resource": "*",
        "Principal": "*"
    },
    {
        "Action": [
            "ec2:CreateVolume"
        ],
        "Effect": "Deny",
        "Resource": "*",
        "Principal": "*",
        "Condition": {
            "Bool": {
                "ec2:Encrypted": "false"
            }
        }
    },
    {
        "Action": [
            "ec2:RunInstances"
        ],
        "Effect": "Deny",
        "Resource": "*",
        "Principal": "*",
        "Condition": {
            "Bool": {
                "ec2:Encrypted": "false"
            }
        }
    }]
}
```

------