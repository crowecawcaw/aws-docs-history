

# Security
<a name="aurora-faq-security"></a>

**Topics**
+ [Does Amazon Aurora run in Amazon Virtual Private Cloud (Amazon VPC)?](#aurora-faq-does-amazon-aurora-run-in-amazon-virtual-private-cloud-amazo)
+ [Does Amazon Aurora support dynamic data masking?](#aurora-faq-does-amazon-aurora-support-dynamic-data-masking)
+ [Does Amazon Aurora support encryption?](#aurora-faq-does-amazon-aurora-support-encryption)
+ [How do I connect to my Aurora database securely?](#aurora-faq-how-do-i-connect-to-my-aurora-database-securely)
+ [Is Amazon Aurora HIPAA eligible?](#aurora-faq-is-amazon-aurora-hipaa-eligible)
+ [How does Amazon Aurora integrate with Amazon GuardDuty?](#aurora-faq-how-does-amazon-aurora-integrate-with-amazon-guardduty)
+ [Where can I find Aurora security updates?](#aurora-faq-where-can-i-find-aurora-security-updates)

## Does Amazon Aurora run in Amazon Virtual Private Cloud (Amazon VPC)?
<a name="aurora-faq-does-amazon-aurora-run-in-amazon-virtual-private-cloud-amazo"></a>

Yes, Aurora DB instances can be created in a [VPC](https://aws.amazon.com/vpc/). This gives you complete control over who can access your Aurora databases, including defining virtual network topologies that closely resemble traditional on-premises networks.

For streamlined setup, you can create an Aurora serverless instance without a VPC using [express configuration](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.CreatingConnecting.AuroraPostgreSQL.html).

## Does Amazon Aurora support dynamic data masking?
<a name="aurora-faq-does-amazon-aurora-support-dynamic-data-masking"></a>

Yes. Amazon Aurora PostgreSQL supports native [dynamic data masking](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Security.DynamicMasking.html) though the pg\_columnmask extension. Dynamic data masking lets you obscure sensitive column values at query time — such as personally identifiable information (PII), payment data, and health records — without altering the data stored on disk, helping you meet regulatory requirements like GDPR, HIPAA, and PCI DSS.

## Does Amazon Aurora support encryption?
<a name="aurora-faq-does-amazon-aurora-support-encryption"></a>

Yes. Amazon Aurora uses SSL (AES-256) to secure connections between the database instance and your application. You can encrypt databases at rest using keys you manage through [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms/).

When encryption is enabled, data stored at rest in the underlying storage is encrypted, along with automated backups, snapshots, and replicas in the same cluster. Encryption and decryption are handled seamlessly. For more information, see the [Amazon RDS User's Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption).

Note: Encrypting an existing unencrypted Aurora instance is not currently supported. To encrypt an existing database, create a new encrypted DB instance and migrate your data into it.

## How do I connect to my Aurora database securely?
<a name="aurora-faq-how-do-i-connect-to-my-aurora-database-securely"></a>

Aurora databases must be accessed through the database port entered on database creation. This provides an additional layer of security for your data. Step-by-step instructions on how to connect to your Amazon Aurora database are provided in the [Amazon Aurora Connectivity Guide](https://d1.awsstatic.com/product-marketing/Aurora/RDS_Aurora_Connectivity_Guide_v5-2.pdf).

## Is Amazon Aurora HIPAA eligible?
<a name="aurora-faq-is-amazon-aurora-hipaa-eligible"></a>

Yes, both the MySQL- and PostgreSQL-compatible editions of Aurora are [HIPAA eligible](https://aws.amazon.com/compliance/hipaa-eligible-services-reference/). You can use them to build HIPAA-compliant applications and store protected health information (PHI) under an executed Business Associate Addendum (BAA) with AWS. If you have already entered into a BAA with AWS, no further action is necessary to begin using these services in the account(s) covered by your BAA. More information about using AWS to build compliant applications is available at [Healthcare Providers](https://aws.amazon.com/health/providers/).

## How does Amazon Aurora integrate with Amazon GuardDuty?
<a name="aurora-faq-how-does-amazon-aurora-integrate-with-amazon-guardduty"></a>

Aurora is integrated with [Amazon GuardDuty](https://aws.amazon.com/guardduty/) to help identify potential threats to data stored in Aurora databases. GuardDuty RDS Protection profiles and monitors login activity using tailored ML models to detect suspicious logins. For more information, see [Monitoring threats with GuardDuty RDS Protection](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/guard-duty-rds-protection.html) and the [GuardDuty RDS Protection User Guide](https://docs.aws.amazon.com/guardduty/latest/ug/rds-protection.html).

## Where can I find Aurora security updates?
<a name="aurora-faq-where-can-i-find-aurora-security-updates"></a>

You can find a current list of CVEs at [Amazon Aurora Security Updates](https://aws.amazon.com/rds/aurora/faqs/security-updates/).