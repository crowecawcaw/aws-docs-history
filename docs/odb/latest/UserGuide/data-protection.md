# Data protection in Oracle Database@AWS

For data protection purposes, we recommend that you protect AWS account
credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM).
That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:

- Use multi-factor authentication (MFA) with each account.
- Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
- Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](../../../awscloudtrail/latest/userguide/cloudtrail-trails.md "../../../awscloudtrail/latest/userguide/cloudtrail-trails.md") in the _AWS CloudTrail User Guide_.
- Use AWS encryption solutions, along with all default security controls within AWS services.
- Use advanced managed security services such as Amazon Macie, which assists in discovering
  and securing sensitive data that is stored in Amazon S3.
- If you require FIPS 140-3 validated cryptographic modules when accessing AWS through
  a command line interface or an API, use a FIPS endpoint. For more information about the
  available FIPS endpoints, see [Federal
  Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/").
  We strongly recommend that you never put confidential or sensitive information, such as your
  customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with Oracle Database@AWS or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
  provide a URL to an external server, we strongly recommend that you do not include credentials
  information in the URL to validate your request to that server.

## Data encryption

Exadata databases use Oracle Transparent Data Encryption (TDE) to encrypt your data.
Your data is also protected in temporary tablespaces, undo segments,
redo logs and during internal database operations such as JOIN and SORT. For more information,
see [Data Security](https://docs.oracle.com/en/cloud/paas/exadata-cloud/csexa/data-security.html#GUID-AD8C853F-A30C-4E50-85ED-B161058D6A93 "https://docs.oracle.com/en/cloud/paas/exadata-cloud/csexa/data-security.html#GUID-AD8C853F-A30C-4E50-85ED-B161058D6A93").

## Encryption in transit

Exadata databases use native Oracle Net Services encryption and
integrity capabilities to secure connections to the database. For more information, see
[Security of data in transit](https://docs.oracle.com/en/cloud/paas/exadata-cloud/csexa/data-security.html#GUID-7BDCEED4-E0A4-48D5-972C-7D65E7D1536D "https://docs.oracle.com/en/cloud/paas/exadata-cloud/csexa/data-security.html#GUID-7BDCEED4-E0A4-48D5-972C-7D65E7D1536D").

## Key management

Transparent Data Encryption includes a keystore to securely store master encryption
keys, and a management framework to securely and efficiently manage the keystore and perform
key maintenance operations. For more information, see [To administer Vault encryption keys](https://docs.oracle.com/en-us/iaas/exadatacloud/doc/manage-databases.html#ECSCM-GUID-7F93FC04-ABE6-4D46-87E9-68EA6DC98FAE "https://docs.oracle.com/en-us/iaas/exadatacloud/doc/manage-databases.html#ECSCM-GUID-7F93FC04-ABE6-4D46-87E9-68EA6DC98FAE").
