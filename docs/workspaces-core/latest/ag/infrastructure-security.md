

# Infrastructure security in Amazon WorkSpaces Instances
<a name="infrastructure-security"></a>

As a managed service, Amazon WorkSpaces Core is protected by AWS global network security. For information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/). To design your AWS environment using the best practices for infrastructure security, see [Infrastructure Protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html) in *Security Pillar AWS Well‐Architected Framework*.

You use AWS published API calls to access Amazon WorkSpaces Core through the network. Clients must support the following:
+ Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
+ Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these modes.

Refer to [Infrastructure security in Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/infrastructure-security.html).

## Make Amazon WorkSpaces Instances API requests through a VPC interface endpoint
<a name="interface-vpc-endpoint"></a>

You can connect directly to Amazon WorkSpaces Instances API endpoints through an [interface endpoint](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpce-interface.html) in your virtual private cloud (VPC) instead of connecting over the internet. When you use a VPC interface endpoint, communication between your VPC and the Amazon WorkSpaces API endpoint is conducted entirely and securely within the AWS network.

The Amazon WorkSpaces Instances API endpoints support [Amazon Virtual Private Cloud](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Introduction.html) (Amazon VPC) interface endpoints that are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink/). Each VPC endpoint is represented by one or more [network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) (also known as elastic network interfaces, or ENIs) with private IP addresses in your VPC subnets.

The VPC interface endpoint connects your VPC directly to the Amazon WorkSpaces Instances API endpoint without an internet gateway, NAT device, VPN connection, or Direct Connect connection. The instances in your VPC don't need public IP addresses to communicate with the Amazon WorkSpaces Instances API endpoint.

You can create an interface endpoint to connect to Amazon WorkSpaces Instances with either the AWS Management Console or AWS Command Line Interface (AWS CLI) commands. For instructions, see [Creating an Interface Endpoint](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpce-interface.html#create-interface-endpoint).

*After you have created a VPC endpoint*, you can use the following example CLI commands that use the `endpoint-url` parameter to specify interface endpoints to the Amazon WorkSpaces Instances API endpoint:

```
aws workspaces-instances list-regions --region us-west-2 \
--endpoint https://workspaces-instances.us-west-2.api.aws
```

If you enable private DNS hostnames for your VPC endpoint, you don't need to specify the endpoint URL. The Amazon WorkSpaces Instances API DNS hostname that the CLI and Amazon WorkSpaces Instances SDK use by default (workspaces-instances.{{externalRegion.api.aws}}) resolves to your VPC endpoint.

The Amazon WorkSpaces Instances API endpoint supports VPC endpoints in all AWS Regions where both [Amazon VPC](https://docs.aws.amazon.com/general/latest/gr/rande.html#vpc_region) and [Amazon WorkSpaces Instances](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services) are available. Amazon WorkSpaces supports making calls to all of its [public APIs](https://docs.aws.amazon.com/workspaces/latest/api/welcome.html) inside your VPC.

To learn more about AWS PrivateLink, see the [AWS PrivateLink documentation](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Introduction.html#what-is-privatelink). For the price of VPC endpoints, see [VPC Pricing](https://aws.amazon.com/vpc/pricing/). To learn more about VPC and endpoints, see [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html).

To see a list of Amazon WorkSpaces Instances API endpoints by Region, see [WorkSpaces API Endpoints](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html#workspaces_api_endpoints).

**Note**  
Amazon WorkSpaces Instances API endpoints with AWS PrivateLink are not supported for Federal Information Processing Standard (FIPS) Amazon WorkSpaces Instances API endpoints.

## Create a VPC endpoint policy for Amazon WorkSpaces Instances
<a name="api-private-link-policy"></a>

You can create a policy for Amazon VPC endpoints for Amazon WorkSpaces Instances to specify the following:
+ The principal that can perform actions.
+ The actions that can be performed.
+ The resources on which actions can be performed.

For more information, see [Controlling Access to Services with VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the *Amazon VPC User Guide*.

**Note**  
VPC endpoint policies aren't supported for Federal Information Processing Standard (FIPS) Amazon WorkSpaces Instances endpoints.

The following example VPC endpoint policy specifies that all users who have access to the VPC interface endpoint are allowed to invoke the Amazon WorkSpaces hosted endpoint named `vpce-00b4e19feaf8b3eee` and VPC `vpc-0ecfe75f77ce1aa61`.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 

    "Statement": [
        {
            "Action": "workspaces-instances:ListRegions",
            "Condition": {
                "StringEquals": {
                    "aws:SourceVpc": "vpc-0ecfe75f77ce1aa61",
                    "aws:SourceVpce": "vpce-00b4e19feaf8b3eee"
                }
            },
            "Effect": "Allow",
            "Principal": {
                "AWS": "*"
            },
            "Resource": "*",
            "Sid": "AllowPortalsAccess"
        }
    ]
}
```

------

**Note**  
In this example, users can still take other Amazon WorkSpaces Instances API actions from outside the VPC. To restrict API calls to those from within the VPC, see [Identity and access management for WorkSpaces Instances](workspaces-access-control.md) for information about using identity-based policies to control access to Amazon WorkSpaces Instances API endpoints.

## Connect your private network to your VPC
<a name="notebook-private-link-vpn"></a>

To call the Amazon WorkSpaces Instances API through your VPC, you have to connect from an instance that is inside the VPC, or connect your private network to your VPC by using AWS Virtual Private Network (Site-to-Site VPN) or Direct Connect. For information, see [VPN Connections](https://docs.aws.amazon.com/vpc/latest/userguide/vpn-connections.html) in the *Amazon Virtual Private Cloud User Guide*. For information about AWS Direct Connect, see [Creating a Connection](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-connection.html) in the *Direct Connect User Guide*.