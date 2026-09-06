

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Installing the Agent on a secured network
<a name="installing-agent-blocked"></a>

The AWS Transform MGN AWS Replication Agent installer needs network access to MGN and Amazon S3 endpoints. If your on premises network is not open to MGN and Amazon S3 endpoints, then you can install the Agent with the aid of PrivateLink.

You can connect your on premises network to the subnet in your staging area VPC using AWS Virtual Private Network or AWS Direct Connect. To use the Site-to-Site VPN or Direct Connect, you must [use private IP in the replication settings](replication-server-settings.md#use-private-ip) (not supported for IPv6).

## Create a VPC endpoint for AWS Transform MGN
<a name="installing-agent-blocked-create"></a>

To allow the AWS Replication Agent installer to communicate with MGN, create an interface VPC endpoint for MGN in your staging area subnet. For more information, see [Creating an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint) in the *Amazon VPC User Guide*.

If the AWS replication agents are installed with a principal using [ AWSApplicationMigrationAgentInstallationPolicy ](security-iam-awsmanpol-AWSApplicationMigrationAgentInstallationPolicy.md#security-iam-awsmanpol-AWSApplicationMigrationAgentInstallationPolicy.title) and a VPCE policy is used (to scope down access), add this statement to your policy:

```
{
       "Effect": "Allow",
       "Principal": "*",
       "Action": "execute-api:Invoke",
       "Resource": "arn:aws:execute-api:<region>:*:*/POST/CreateSessionForMgn"
}
```

## Use the created VPC Endpoint for AWS Transform MGN
<a name="installing-agent-blocked-use"></a>

Once you have created the VPC Endpoint, the AWS Replication Agent can connect to MGN via Site-to-Site VPN/Direct Connect by using the --endpoint installation parameter. Learn more about [Private DNS for interface endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html#vpce-private-dns) in the *Amazon VPC User Guide.*

Run the AWS Replication Agent installer with the --endpoint parameter. Enter your endpoint-specific DNS hostname within the parameter. The installer is then able to connect to MGN via the endpoint over your Site-to-Site VPN/Direct Connect connection.

## Create an Amazon S3 endpoint for AWS Transform MGN
<a name="installing-agent-blocked-create-s3"></a>

To allow the AWS Replication Agent installer to communicate with Amazon S3, create an interface Amazon S3 endpoint for MGN in your staging area subnet. For more information, see [Endpoints for Amazon S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html) in the *Amazon VPC User Guide*.

## Use the created Amazon S3 Endpoint for AWS Transform MGN
<a name="installing-agent-blocked-use-s3"></a>

Once you have created the Amazon VPC Endpoint, the AWS Replication Agent can connect to Amazon S3 via Site-to-Site VPN/Direct Connect by using the --s3-endpoint installation parameter. Learn more about [Private DNS for interface endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html#vpce-private-dns) in the *Amazon VPC User Guide.*

Run the AWS Replication Agent installer with the --s3-endpoint parameter. Enter your endpoint-specific DNS hostname. The installer is then able to connect to Amazon S3 via the endpoint over your Site-to-Site VPN/Direct Connect connection.

## Prescriptive guidance
<a name="Prescriptive-guidance"></a>

 A detailed guide for rehosting servers using MGN over private networks is available here: 

[Migrating on-premises servers to AWS over private networks by using MGN.](https://docs.aws.amazon.com/prescriptive-guidance/latest/rehost-servers-over-private-networks-mgn/welcome.html)