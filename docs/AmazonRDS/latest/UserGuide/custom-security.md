# Security in Amazon RDS Custom

Familiarize yourself with the security considerations for RDS Custom.

For more information about security for RDS Custom, see the following topics.

- [Securing your Amazon S3 bucket against the
  confused deputy problem](custom-security.md "custom-security.md")
- [Rotating RDS Custom for Oracle credentials for compliance
  programs](custom-security.md "custom-security.md")

## How RDS Custom securely manages tasks on

your behalf

RDS Custom uses the following tools and techniques to securely run operations on your behalf:

**AWSServiceRoleForRDSCustom service-linked role**

A _service-linked role_ is predefined by the service
and includes all permissions that the service needs to call other
AWS services on your behalf. For RDS Custom,
`AWSServiceRoleForRDSCustom` is a service-linked role that is
defined according to the principle of least privilege. RDS Custom uses the
permissions in `AmazonRDSCustomServiceRolePolicy`, which is the
policy attached to this role, to perform most provisioning and all off-host
management tasks. For more information, see [AmazonRDSCustomServiceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonRDSCustomServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonRDSCustomServiceRolePolicy.md").

When it performs tasks on the host, RDS Custom automation uses credentials
from the service-linked role to run commands using AWS Systems Manager. You can audit
the command history through the Systems Manager command history and
AWS CloudTrail. Systems Manager connects to your RDS Custom DB instance using your
networking setup. For more information, see [Step 4: Configure IAM for
RDS Custom for Oracle](custom-setup-orcl.md#custom-setup-orcl.iam-vpc "custom-setup-orcl.md#custom-setup-orcl.iam-vpc").

**Temporary IAM credentials**

When provisioning or deleting resources, RDS Custom sometimes uses temporary
credentials derived from the credentials of the calling IAM principal.
These IAM credentials are restricted by the IAM policies attached to
that principal and expire after the operation is completed. To learn about
the permissions required for IAM principals who use RDS Custom, see [Step 5: Grant required permissions to your
IAM user or role](custom-setup-orcl.md#custom-setup-orcl.iam-user "custom-setup-orcl.md#custom-setup-orcl.iam-user").

**Amazon EC2 instance profile**

An EC2 instance profile is a container for an IAM role that you can use
to pass role information to an EC2 instance. An EC2 instance underlies an
RDS Custom DB instance. You provide an instance profile when you create an RDS Custom
DB instance. RDS Custom uses EC2 instance profile credentials when it performs
host-based management tasks such as backups. For more information, see [Create your IAM role and instance profile
manually](custom-setup-orcl.md#custom-setup-orcl.iam "custom-setup-orcl.md#custom-setup-orcl.iam").

**SSH key pair**

When RDS Custom creates the EC2 instance that underlies a DB instance, it creates an
SSH key pair on your behalf. The key uses the naming prefix
`do-not-delete-rds-custom-ssh-privatekey-db-` or
`rds-custom!oracle-do-not-delete-`db_resource_id-uuid`-ssh-privatekey`.
AWS Secrets Manager stores this SSH private key as a secret in your AWS account.
Amazon RDS doesn't store, access, or use these credentials. For more information,
see [Amazon EC2 key pairs and Linux
instances](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md").

## SSL certificates

RDS Custom DB instances don't support managed SSL certificates. If you want to deploy SSL, you
can self-manage SSL certificates in your own wallet and create an SSL listener to secure
the connections between the client database or for database replication. For more
information, see [Configuring Transport Layer Security Authentication](https://docs.oracle.com/en/database/oracle/oracle-database/19/dbseg/configuring-secure-sockets-layer-authentication.html#GUID-6AD89576-526F-4D6B-A539-ADF4B840819F "https://docs.oracle.com/en/database/oracle/oracle-database/19/dbseg/configuring-secure-sockets-layer-authentication.html#GUID-6AD89576-526F-4D6B-A539-ADF4B840819F") in the Oracle Database
documentation.
