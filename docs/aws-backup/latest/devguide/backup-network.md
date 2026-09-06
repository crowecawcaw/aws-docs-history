

# AWS Backup network
<a name="backup-network"></a>

## AWS Backup endpoints
<a name="backup-endpoints"></a>

AWS Backup offers both public and private endpoints for your connectivity needs. For these endpoints, AWS Backup supports both Internet Protocols version 4 (IPv4) and version 6 (IPv6) for resource types that support IPv6.

The newer public endpoint `backup.{{[Region]}}.api.aws` has dual-stack capabilities and can resolve either or both IPv4 endpoints and IPv6 endpoints. When you make a request to a dual-stack AWS Backup API endpoint, the endpoint will resolve to the address determined by the configuration of the protocol used by your network and client.

The older endpoint `backup.{{[Region]}}.amazonaws.com` can be used for calls that reference only IPv4.

You can view the [public service endpoints for AWS Backup](https://docs.aws.amazon.com/general/latest/gr/bk.html) in the Amazon Web Services General Reference. You can view the steps for setting up private endpoints in [AWS Backup through VPC](#backup-privatelink).

## AWS Backup through VPC endpoints
<a name="backup-privatelink"></a>

You can establish a private connection between your virtual private cloud (VPC) and AWS Backup by creating an interface VPC endpoint. Interface endpoints are powered by [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/), a technology that enables you to access the AWS Backup API without using an internet gateway, NAT device, VPN connection, or Direct Connect connection. Instances in your VPC don't need public IP addresses to communicate with AWS Backup API endpoints. Your instances also don't need public IP addresses to use any of the available AWS Backup API and Backup gateway API operations.

For more information, see [Access AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html) in the *AWS PrivateLink Guide*.

### Considerations for Amazon VPC endpoints
<a name="considerations-for-vpc-endpoints"></a>

All AWS Backup operations relevant to managing your resources are available from your VPC using AWS PrivateLink.

VPC endpoint policies are supported for Backup endpoints. By default, full access to Backup operations is allowed through the endpoint. Alternatively, you can associate a security group with the endpoint network interfaces to control traffic to AWS Backup through the interface endpoint.

You can select IPv4, IPv6, or dual stack when created an endpoint. You will receive the same DNS names (which will have both IPv4 and IPv6 addresses if you select dual stack).

### Create an AWS Backup VPC endpoint
<a name="creating-backup-vpc-endpoint"></a>

You can create a VPC endpoint for AWS Backup using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Create an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws) in the *AWS PrivateLink Guide*.

PrivateLink endpoints use the same name structure of IPv4, though each endpoint can be configured for IPv4, IPv6, or dual stack.

Create a VPC endpoint for AWS Backup using the service name `com.amazonaws.{{region}}.backup`.

In China (Beijing) Region and China (Ningxia) Region, the service name should be `cn.com.amazonaws.{{region}}.backup`.

For Backup dataplane endpoints, use `com.amazonaws.{{region}}.backup-storage`. Only SAP Hana supports dataplane endpoints and may require a [ BackInt agent update](https://docs.aws.amazon.com/sap/latest/sap-hana/aws-backint-agent-backup.html#backint-backup-install).

For Backup gateway endpoints, use `com.amazonaws.{{region}}.backup-gateway`.

The following TCP ports must be allowed in the security group when creating a VPC endpoint for backup Gateway:
+ TCP 443
+ TCP 1026
+ TCP 1027
+ TCP 1028
+ TCP 1031
+ TCP 2222


| Protocol | Port | Direction | Source | Destination | Usage | 
| --- | --- | --- | --- | --- | --- | 
| TCP | 443 (HTTPS) | Outbound | Backup Gateway | AWS | For communication from Backup Gateway to the AWS service endpoint | 

### Use a VPC endpoint
<a name="use-vpc-endpoint"></a>

If you enable private DNS for the endpoint, you can make API requests to AWS Backup with the VPC endpoint using its default DNS name for the AWS Region, for example `backup.us-east-1.api.aws`.

However, for the China (Beijing) Region and China (Ningxia) Region AWS Regions, API requests should be made with the VPC endpoint using `backup.cn-north-1.amazonaws.com.cn` and `backup.cn-northwest-1.amazonaws.com.cn`, respectively.

### Creating a VPC endpoint policy
<a name="creating-vpc-endpoint-policy"></a>

 You can attach an endpoint policy to your VPC endpoint that controls access to the Amazon Backup API. The policy specifies:
+ The principal that can perform actions.
+ The actions that can be performed.
+ The resources on which actions can be performed.

**Important**  
When a non-default policy is applied to an interface VPC endpoint for AWS Backup, certain failed API requests, such as those failing from `RequestLimitExceeded`, might not be logged to AWS CloudTrail or Amazon CloudWatch.

For more information, see [Control access to services using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *AWS PrivateLink Guide*.

**Example: VPC endpoint policy for AWS Backup actions**

The following is an example of an endpoint policy for AWS Backup. When attached to an endpoint, this policy grants access to the listed AWS Backup actions for all principles on all resources.

```
{
  "Statement":[
    {
      "Action":"backup:*",
      "Effect":"Allow",
      "Principal":"*",
      "Resource":"*"
    }
  ]
}
```

**Example: VPC endpoint policy that denies all access from a specified AWS account**

The following VPC endpoint policy denies AWS account `123456789012` all access to resources using the endpoint. The policy allows all actions from other accounts.

------
#### [ JSON ]

****  

```
{
  "Id":"Policy1645236617225",
  "Version":"2012-10-17",		 	 	 
  "Statement":[
    {
      "Sid":"Stmt1645236612384",
      "Action":"backup:*",
      "Effect":"Deny",
      "Resource":"*",
      "Principal":{
        "AWS":[
          "123456789012"
        ]
      }
    }
  ]
}
```

------

For more information about available API responses, see the [API Guide](https://docs.aws.amazon.com/aws-backup/latest/devguide/api-reference.html).