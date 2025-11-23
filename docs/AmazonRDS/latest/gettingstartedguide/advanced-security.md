# Advanced security options in Amazon RDS

It's important to secure your Amazon RDS DB instance to protecting your data and ensuring
compliance with organizational and regulatory standards. This section covers advanced network
configurations and encryption techniques to improve your database security.

###### Topics

- [Accessing a DB instance in a VPC](#vpc-peering "#vpc-peering")
- [Enabling SSL/TLS encryption for data in transit](#ssl-tls "#ssl-tls")
- [Encryption at rest with customer managed keys](#encryption-at-rest "#encryption-at-rest")

## Accessing a DB instance in a VPC

When you host an Amazon RDS DB instance within an Amazon Virtual Private Cloud (Amazon VPC), you must understand the
various networking options available to securely connect to your database. By configuring
the VPC environment appropriately, you can access your DB instance from application servers,
on-premises systems, or other VPCs.

For example, consider an application running in an on-premises data center that needs to
connect to a DB instance in a VPC. Using Direct Connect or a VPN connection, you can establish a
private link to securely access the database while keeping the communication isolated from
the public internet.

The following are the main ways to connect to a DB instance:

- **Within the same VPC** – Applications running on
  instances within the same VPC can communicate directly with the DB instance using its
  private IP address. Make sure that appropriate security group and network ACL rules
  allow the necessary traffic.
- **From a different VPC** – If your application
  is in another VPC, establish connectivity through VPC peering, AWS Transit Gateway, or private
  VPC endpoints. Each option has unique benefits and cost implications.
- **From on-premises systems** – Use Direct Connect or a
  VPN connection to create a secure link between your on-premises environment and the VPC
  hosting the DB instance.
- **From public internet** – If you enable public
  access, you can connect to the DB instance using its public endpoint. Carefully manage
  IP whitelisting and encryption in order to maintain security.

**Key considerations**:

- Use security groups to define which traffic can reach the DB instance.
- Restrict access by IP address to minimize the exposure of your DB instance.
- When you use public access, enable Secure Sockets Layer and Transport Layer Security
  (SSL/TLS) for encrypted communication.

For detailed networking scenarios and configurations, see [Scenarios for accessing a DB
instance in a VPC](../UserGuide/USER_VPC.md "../UserGuide/USER_VPC.md") in the _Amazon RDS User Guide_.

## Enabling SSL/TLS encryption for data in transit

To secure communication between your application and an Amazon RDS DB instance, Secure
Sockets Layer and Transport Layer Security (SSL/TLS) encryption protects data transmitted
over the network from interception and tampering. This method is particularly relevant for
applications where data must remain confidential during transit, such as financial records,
personal information, or other sensitive content.

For example, a microservices architecture might include a reporting service that queries
a database hosted in Amazon RDS. Without encryption, malicious actors or network intermediaries
can intercept and potentially modify the data sent across the network. Enable SSL/TLS to
encrypt these interactions and maintain data integrity and confidentiality.

###### To enable encryption in transit

1. Obtain the required certificates by downloading the Amazon RDS SSL/TLS certificates. See
   [Certificate bundles by AWS Region](../UserGuide/UsingWithRDS.md#UsingWithRDS.SSL.CertificatesAllRegions "../UserGuide/UsingWithRDS.md#UsingWithRDS.SSL.CertificatesAllRegions") in the _Amazon RDS User
   Guide_.
2. Adjust your database connection settings to include the certificate and enable
   SSL/TLS. This might involve specifying parameters in the connection string, such as
   `sslmode=require`, depending on the database client.
3. Confirm that the application connects to the DB instance securely by reviewing logs
   or using diagnostic tools to inspect the connection properties.

**Key considerations**:

- Use the most up-to-date version of TLS that your applications and RDS DB instance
  support, so you can use the the latest security features.
- Plan for certificate rotation by monitoring expiration dates and updating
  applications as needed.
- Test the configuration in a staging environment before you apply it in production in
  order to avoid service disruptions.

For implementation details, see to the [Using SSL/TLS to encrypt a
connection to a DB instance or cluster](../UserGuide/UsingWithRDS.md "../UserGuide/UsingWithRDS.md") in the _Amazon RDS User
Guide_.

## Encryption at rest with customer managed keys

With Amazon RDS, you can encrypt your database and backups to ensure that sensitive data
remains secure when you store it. By using AWS Key Management Service (AWS KMS) with customer managed keys, you have full
control over the encryption process. This includes the ability to define key rotation
policies and restrict access to specific users or services.

When you enable encryption at rest, Amazon RDS encrypts all data in your database, including
automated backups, read replicas, and snapshots, using the specified KMS key. This
encryption occurs automatically, with minimal performance overhead for most
workloads.

###### To enable encryption at rest

1. Create a KMS key. In the AWS Management Console, navigate to AWS KMS and create a customer managed key.
   Specify usage policies and rotation settings. For instructions, see [Create a KMS
   key](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the _AWS Key Management Service Developer Guide_.
2. When you launch a new Amazon RDS instance, select the option to enable encryption and
   specify your KMS customer managed key.

![Encryption settings panel with AWS KMS key selection dropdown showing "my-key" option.](images/kms-key.png)

To encrypt existing databases, create a new encrypted DB instance or snapshot and
migrate your data.

**Key considerations**:

- Use IAM policies to tightly restrict who can use or manage the encryption
  keys.
- Enable automatic key rotation for customer managed keys to simplify security
  management.
- Make sure that encryption aligns with your long-term requirements, because you can't
  disable encryption at rest after you enable it.

For more detailed guidance on setting up encryption at rest with AWS KMS, see [Encrypting
Amazon RDS resources](../UserGuide/Overview.md "../UserGuide/Overview.md") in the _Amazon RDS User Guide_.
