NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Installing the Agent on a secured network

The AWS Application Migration Service AWS Replication Agent installer needs network access to Application Migration Service and Amazon S3
endpoints. If your on premises network is not open to Application Migration Service and Amazon S3 endpoints, then you can
install the Agent with the aid of PrivateLink.

You can connect your on premises network to the subnet in your staging area VPC using
AWS Virtual Private Network or AWS Direct Connect. To use the Site-to-Site VPN or Direct Connect, you must [use private IP in the replication settings](replication-server-settings.md#use-private-ip "replication-server-settings.md#use-private-ip").

## Create a VPC endpoint for AWS Application Migration Service

To allow the AWS Replication Agent installer to communicate with Application Migration Service, create an
interface VPC endpoint for Application Migration Service in your staging area subnet. For more information, see
[Creating an interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint.html "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint.html") in the _Amazon VPC User
Guide_.

If the AWS replication agents are installed with a principal using [AWSApplicationMigrationAgentInstallationPolicy](security-iam-awsmanpol-AWSApplicationMigrationAgentInstallationPolicy.md#security-iam-awsmanpol-AWSApplicationMigrationAgentInstallationPolicy.title "security-iam-awsmanpol-AWSApplicationMigrationAgentInstallationPolicy.md#security-iam-awsmanpol-AWSApplicationMigrationAgentInstallationPolicy.title") and a VPCE policy is used (to scope
down access), add this statement to your policy:

```
{
       "Effect": "Allow",
       "Principal": "*",
       "Action": "execute-api:Invoke",
       "Resource": "arn:aws:execute-api:<region>:*:*/POST/CreateSessionForMgn"
}
```

## Use the created VPC Endpoint for

AWS Application Migration Service

Once you have created the VPC Endpoint, the AWS Replication Agent can connect to
Application Migration Service via Site-to-Site VPN/Direct Connect by using the --endpoint installation parameter.
Learn more about [Private DNS for interface endpoints](../../../vpc/latest/privatelink/vpce-interface.md#vpce-private-dns "../../../vpc/latest/privatelink/vpce-interface.md#vpce-private-dns") in the _Amazon VPC User
Guide._

Run the AWS Replication Agent installer with the --endpoint parameter. Enter your
endpoint-specific DNS hostname within the parameter. The installer is then able to
connect to Application Migration Service via the endpoint over your Site-to-Site VPN/Direct Connect connection.

## Create an Amazon S3 endpoint for

AWS Application Migration Service

To allow the AWS Replication Agent installer to communicate with Amazon S3, create an interface
Amazon S3 endpoint for Application Migration Service in your staging area subnet. For more information, see [Endpoints for
Amazon S3](../../../vpc/latest/privatelink/vpc-endpoints-s3.md "../../../vpc/latest/privatelink/vpc-endpoints-s3.md") in the _Amazon VPC User Guide_.

## Use the created Amazon S3 Endpoint for

AWS Application Migration Service

Once you have created the Amazon VPC Endpoint, the AWS Replication Agent can connect to Amazon S3 via
Site-to-Site VPN/Direct Connect by using the --s3-endpoint installation parameter. Learn more about [Private DNS for interface endpoints](../../../vpc/latest/privatelink/vpce-interface.md#vpce-private-dns "../../../vpc/latest/privatelink/vpce-interface.md#vpce-private-dns") in the _Amazon VPC User
Guide._

Run the AWS Replication Agent installer with the --s3-endpoint parameter. Enter your
endpoint-specific DNS hostname. The installer is then able to connect to Application Migration Service via the
endpoint over your Site-to-Site VPN/Direct Connect connection.

## Prescriptive guidance

A detailed guide for rehosting servers using Application Migration Service over private networks is available
here:

[Migrating on-premises servers to AWS over private networks by using Application Migration Service.](../../../prescriptive-guidance/latest/rehost-servers-over-private-networks-mgn/welcome.md "../../../prescriptive-guidance/latest/rehost-servers-over-private-networks-mgn/welcome.md")
