# Advanced endpoint configuration

You can configure advanced settings for your endpoints in AWS Database Migration Service (AWS DMS) to setup
control over how source and target endpoints behave during the migration process. As
part of the advanced setup you can configure AWS DMS VPC peering to enable secure
communication between VPCs, DMS Security Groups to control inbound and outbound traffic,
Newtwork Access Control lists (NACLs) as additional layer of security, and VPC endpoints
for AWS Secrets Manager.

You can set these configurations during endpoint creation or modified later through
the AWS DMS Console or API, to fine-tune the migration processes based on specific
database engine requirements and performance needs.

Following, you can find out more details about advanced endpoint configuration.

###### Topics

- [VPC peering configuration for
  AWS DMS.](CHAP_Advanced.Endpoints.vpc.md "CHAP_Advanced.Endpoints.vpc.md")
- [Security group configuration
  for AWS DMS](CHAP_Advanced.Endpoints.md "CHAP_Advanced.Endpoints.md")
- [Network Access Control List (NACL)
  configuration for AWS DMS](CHAP_Advanced.Ednpoints.md "CHAP_Advanced.Ednpoints.md")
- [Configuring AWS DMS secrets
  manager VPC Endpoint](CHAP_Advanced.Endpoints.md "CHAP_Advanced.Endpoints.md")
- [Additional
  considerations](#CHAP_secretsmanager.additionalconsiderations "#CHAP_secretsmanager.additionalconsiderations")

## Additional

considerations

You must consider the following additional configuration information:

**Replication instance security group:**

- Ensure that the security group associated with your replication instance
  allows outbound traffic to the VPC endpoint on port 443 (HTTPS).

**VPC DNS settings:**

- Confirm that **DNS resolution** and **DNS
  hotnames** are enabled in your VPC. This allows your instances
  to resolve the VPC endpoint DNS names. You can confirm that by navigating to
  VPCs in the [Amazon VPC
  console](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/") and select your VPC to verify that **DNS
  resolution** and **DNS hotnames** are set to
  "**Yes**".

**Testing connectivity:**

- From your replication instance, you can perform a DNS lookup to ensure it
  resolves the VPC endpoint: `nslookup
secretsmanager.<region>amazonaws.com`. It must return the Ip
  address associated with your VPC endpoint
