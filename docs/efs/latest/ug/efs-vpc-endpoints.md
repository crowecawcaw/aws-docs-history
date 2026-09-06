

# Working with interface VPC endpoints in Amazon EFS
<a name="efs-vpc-endpoints"></a>

To establish a private connection between your virtual private cloud (VPC) and the Amazon EFS API, you can create an interface VPC endpoint. The endpoint provides secure connectivity to the Amazon EFS API without requiring an internet gateway, NAT instance, or virtual private network (VPN) connection. For more information, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *Amazon VPC User Guide*. 

Interface VPC endpoints are powered by AWS PrivateLink, a feature that enables private communication between AWS services using private IP addresses. To use AWS PrivateLink, create an interface VPC endpoint for Amazon EFS in your VPC using the Amazon VPC console, API, or CLI. Doing this creates an elastic network interface in your subnet with a private IP address that serves Amazon EFS API requests. You can also access a VPC endpoint from on-premises environments or from other VPCs using Site-to-Site VPN, Direct Connect, or VPC peering. To learn more, see [Connect your VPC to services using AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-services-overview.html) in the *Amazon VPC User Guide*. 

## Creating an interface endpoint for Amazon EFS
<a name="create-vpce-efs"></a>

To create an interface VPC endpoint for Amazon EFS, use one of the following:
+ `com.amazonaws.{{region}}.elasticfilesystem` – Creates an endpoint for Amazon EFS API operations.
+ **`com.amazonaws.{{region}}.elasticfilesystem-fips`** – Creates an endpoint for the Amazon EFS API that complies with [Federal Information Processing Standard (FIPS) 140-2](https://aws.amazon.com/compliance/fips/).

For a complete list of Amazon EFS endpoints, see [Amazon Elastic File System endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/elasticfilesystem.html) in the *Amazon Web Services General Reference*. 

For more information about how to create an interface endpoint, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *Amazon VPC User Guide*.

## Creating a VPC endpoint policy for Amazon EFS
<a name="create-vpce-policy-efs"></a>

To control access to the Amazon EFS API, you can attach an AWS Identity and Access Management (IAM) policy to your VPC endpoint. The policy specifies the following:
+ The principal that can perform actions.
+ The actions that can be performed.
+ The resources on which actions can be performed. 

For more information, see [Control access to VPC endpoints using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *Amazon VPC User Guide*.

The following example shows a VPC endpoint policy that denies everyone permission to create an EFS file system through the endpoint. The example policy also grants everyone permission to perform all other actions. 

```
{
   "Statement": [
        {
            "Action": "*",
            "Effect": "Allow",
            "Resource": "*",
            "Principal": "*"
        },
        {
            "Action": "elasticfilesystem:CreateFileSystem",
            "Effect": "Deny",
            "Resource": "*",
            "Principal": "*"
        }
    ]
}
```