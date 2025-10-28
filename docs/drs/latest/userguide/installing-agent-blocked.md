# Installing the agent on a secured network

The AWS DRS AWS Replication Agent installer needs network access to
AWS Elastic Disaster Recovery and S3 endpoints. If your on premise network is not open to Elastic
Disaster Recovery and S3 endpoints, then you can install the Agent with the aid of
PrivateLink.

You can connect your on premise network to the subnet in your staging area VPC using AWS
VPN or DirectConnect. To use the AWS VPN or DirectConnect, you must activate private IP in
the replication settings.

These topics describe the connectivity prerequisites that enable you to install the
agent. All of the settings apply to the target account (or the staging account in a
multi-account scenario) and Region where you want to handle the recovery.

## Create a VPC Endpoint for AWS Elastic Disaster Recovery

To allow the AWS Replication Agent installer to communicate with AWS Elastic Disaster Recovery, create an
interface VPC endpoint for AWS Elastic Disaster Recovery in your staging area subnet. This VPC endpoint is
used exclusively for management traffic; replication data is transmitted directly
between the source and replication servers. For more information, see [Creating an Interface Endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint.html "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint.html") in the Amazon VPC User Guide.

If the AWS replication agents are installed with a principal using
[AWSElasticDisasterRecoveryAgentInstallationPolicy](security-iam-awsmanpol-AWSElasticDisasterRecoveryAgentInstallationPolicy.md#security-iam-awsmanpol-AWSElasticDisasterRecoveryAgentInstallationPolicy.title "security-iam-awsmanpol-AWSElasticDisasterRecoveryAgentInstallationPolicy.md#security-iam-awsmanpol-AWSElasticDisasterRecoveryAgentInstallationPolicy.title") and a VPCE policy is used (to scope down access), add the following statement to your policy:

```
`{
 "Effect": "Allow",
 "Principal": "*",
 "Action": "execute-api:Invoke",
 "Resource": "arn:aws:execute-api:<region>::*/POST/CreateSessionForDrs"
 }`
```

## Use the created VPC Endpoint for AWS Elastic Disaster Recovery

Once you have created the VPC Endpoint, the AWS Replication Agent can connect to Elastic
Disaster Recovery via VPN/DirectConnect by using the --endpoint installation parameter. Learn
more about [Private DNS for interface endpoints](../../../vpc/latest/privatelink/vpce-interface.md#vpce-private-dns "../../../vpc/latest/privatelink/vpce-interface.md#vpce-private-dns") in the _Amazon VPC User
Guide_.

Run the AWS Replication Agent installer with the --endpoint parameter. Enter your
endpoint-specific DNS hostname within the parameter. The installer is then able to
connect to AWS Elastic Disaster Recovery via the endpoint over your VPN/DirectConnect connection.

Example of an interface endpoint DNS name:
vpce-0123456789-abcdef.drs.<REGION>.vpce.amazonaws.com

## Create a S3 Endpoint for AWS Elastic Disaster Recovery

To allow the AWS Replication Agent installer to communicate with S3, create an
interface S3 endpoint for AWS Elastic Disaster Recovery in your staging area subnet. For more information,
see [Endpoints for Amazon S3](../../../vpc/latest/privatelink/vpc-endpoints-s3.md "../../../vpc/latest/privatelink/vpc-endpoints-s3.md") in the _Amazon VPC User
Guide_. The endpoint requires a security group that allows connection from
the agent, enabling it to download components it needs for the installation.

## Use the created S3 Endpoint for AWS Elastic Disaster Recovery

Once you have created the interface VPC Endpoint, the AWS Replication Agent can connect
to S3 via VPN/DirectConnect by using the --s3-endpoint installation parameter. Learn
more about [Private DNS for interface endpoints](../../../vpc/latest/privatelink/vpce-interface.md#vpce-private-dns "../../../vpc/latest/privatelink/vpce-interface.md#vpce-private-dns") in the _Amazon VPC User Guide_.

Run the AWS Replication Agent installer with the --s3-endpoint parameter. Enter your
endpoint-specific DNS hostname. The installer is then able to connect to Elastic
Disaster Recovery via the endpoint over your VPN/DirectConnect connection.

Example of an interface endpoint DNS name:
vpce-0123456789-abcdef.s3.<REGION>.vpce.amazonaws.com

## Preparing the AWS VPC

To prepare the staging area subnet in a private subnet, two more endpoints have to be created to ensure
the successful creation of the replication servers.

- EC2 Interface Endpoint: used to establish connectivity to EC2 endpoint from the staging area
  subnet
- S3 Gateway Endpoint: used by the replication servers to download the replication
  software from S3

For more information about setting up AWS Elastic Disaster Recovery with a site-to-site
VPN connection, [visit this blog post](https://aws.amazon.com/blogs/storage/cross-region-aws-elastic-disaster-recovery-agent-installation-in-a-secured-network "https://aws.amazon.com/blogs/storage/cross-region-aws-elastic-disaster-recovery-agent-installation-in-a-secured-network").
