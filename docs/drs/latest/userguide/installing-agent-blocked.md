

# Installing the agent on a secured network
<a name="installing-agent-blocked"></a>

The AWS Replication Agent installer needs network access to AWS Elastic Disaster Recovery and S3 endpoints. If your on-premises network is not open to AWS Elastic Disaster Recovery and S3 endpoints, you can install the agent by using PrivateLink.

VPC endpoints created through PrivateLink handle only **management traffic** between the AWS Replication Agent and the AWS Elastic Disaster Recovery service. Management traffic includes agent installation, authentication, and API communication.

**Replication traffic** (the actual data replication between your source servers and the replication servers in AWS) does not use VPC endpoints. Replication traffic flows directly between the source and replication servers over your VPN or DirectConnect connection. To enable private replication, activate the private IP option in the replication settings. VPC endpoints are not required for private replication.

You can connect your on-premises network to the subnet in your staging area VPC using AWS VPN or DirectConnect. To use AWS VPN or DirectConnect, you must activate private IP in the replication settings.

The following topics describe the connectivity prerequisites that enable you to install the agent. All of the settings apply to the target account (or the staging account in a multi-account scenario) and Region where you want to handle the recovery.

## Create a VPC Endpoint for AWS Elastic Disaster Recovery
<a name="installing-agent-blocked-create"></a>

To allow the AWS Replication Agent installer to communicate with AWS Elastic Disaster Recovery, create an interface VPC endpoint for AWS Elastic Disaster Recovery in your staging area subnet. This VPC endpoint is used exclusively for management traffic; replication data is transmitted directly between the source and replication servers. For more information, see [Creating an Interface Endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint) in the Amazon VPC User Guide.

If the AWS replication agents are installed with a principal using [ AWSElasticDisasterRecoveryAgentInstallationPolicy ](security-iam-awsmanpol-AWSElasticDisasterRecoveryAgentInstallationPolicy.md) and a VPCE policy is used (to scope down access), add the following statement to your policy:

```
{
     "Effect": "Allow",
     "Principal": "*",
     "Action": "execute-api:Invoke",
     "Resource": "arn:aws:execute-api:<region>:*.*/POST/CreateSessionForDrs"
     }
```

## Use the created VPC Endpoint for AWS Elastic Disaster Recovery
<a name="installing-agent-blocked-use"></a>

After you create the VPC Endpoint, the AWS Replication Agent can connect to AWS Elastic Disaster Recovery through VPN or DirectConnect by using the `--endpoint` installation parameter. For more information, see [Private DNS for interface endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html#vpce-private-dns) in the Amazon VPC User Guide.

Run the AWS Replication Agent installer with the `--endpoint` parameter. Enter your endpoint-specific DNS hostname within the parameter. The installer then connects to AWS Elastic Disaster Recovery through the endpoint over your VPN or DirectConnect connection.

Example of an interface endpoint DNS name: `vpce-0123456789-abcdef.drs.<REGION>.vpce.amazonaws.com`

## Create an S3 Endpoint for AWS Elastic Disaster Recovery
<a name="installing-agent-blocked-create-s3"></a>

To allow the AWS Replication Agent installer to communicate with S3, create an interface S3 endpoint for AWS Elastic Disaster Recovery in your staging area subnet. For more information, see [Endpoints for Amazon S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html) in the Amazon VPC User Guide. The endpoint requires a security group that allows connection from the agent, enabling it to download components it needs for the installation.

## Use the created S3 Endpoint for AWS Elastic Disaster Recovery
<a name="installing-agent-blocked-use-s3"></a>

After you create the interface VPC Endpoint, the AWS Replication Agent can connect to S3 through VPN or DirectConnect by using the `--s3-endpoint` installation parameter. For more information, see [Private DNS for interface endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html#vpce-private-dns) in the Amazon VPC User Guide.

Run the AWS Replication Agent installer with the `--s3-endpoint` parameter. Enter your endpoint-specific DNS hostname. The installer then connects to S3 through the endpoint over your VPN or DirectConnect connection.

Example of an interface endpoint DNS name: `vpce-0123456789-abcdef.s3.<REGION>.vpce.amazonaws.com`

## Preparing the AWS VPC
<a name="preparing-aws-vpc-s3"></a>

To prepare the staging area subnet in a private subnet, create two more endpoints to ensure the successful creation of the replication servers.
+ **EC2 Interface Endpoint** – Used to establish connectivity to the EC2 endpoint from the staging area subnet.
+ **S3 Gateway Endpoint** – Used by the replication servers to download the replication software from S3.

For more information about setting up AWS Elastic Disaster Recovery with a site-to-site VPN connection, see [Cross-Region AWS Elastic Disaster Recovery agent installation in a secured network](https://aws.amazon.com/blogs/storage/cross-region-aws-elastic-disaster-recovery-agent-installation-in-a-secured-network).