# Security in Amazon EMR

Security and compliance is a responsibility you share with AWS. This shared
responsibility model can help relieve your operational burden as AWS operates, manages,
and controls the components from the host operating system and virtualization layer down to
the physical security of the facilities in which EMR clusters operate. You assume
responsibility, management, and updating Amazon EMR clusters, as well as configuring the
application software and AWS provided security controls. This differentiation of
responsibility is commonly referred to as security _of_ the cloud versus
security _in_ the cloud.

- Security of the cloud – AWS is responsible for protecting the
  infrastructure that runs AWS services in AWS. AWS also provides you with
  services that you can use securely. Third-party auditors regularly test and verify
  the effectiveness of our security as part of the [AWS compliance programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/"). To learn about the
  compliance programs that apply to Amazon EMR, see [AWS services in scope by compliance
  program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").
- Security in the cloud – you are also responsible to perform all of the
  necessary security configuration and management tasks for securing an Amazon EMR cluster.
  Customers that deploy an Amazon EMR cluster are responsible for management of the
  application software installed on the instances, and the configuration of the
  AWS-provided features such as security groups, encryption and access control
  according to your requirements, applicable laws, and regulations.
  This documentation helps you understand how to apply the shared responsibility model when
  using Amazon EMR. The topics in this chapter show you how to configure Amazon EMR and use other
  AWS services to meet your security and compliance objectives.

## Network and infrastructure security

As a managed service, Amazon EMR is protected by the AWS global network security
procedures that are described in the [Amazon Web Services: Overview of security processes](https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf "https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf") whitepaper. AWS network and
infrastructure protection services give you fine-grained protections at both the host
and network-level boundaries. Amazon EMR supports AWS services and application features
that address your network protection and compliance requirements.

- **Amazon EC2 security groups** act as a virtual
  firewall for Amazon EMR cluster instances, limiting inbound and outbound network
  traffic. For more information, see [Control network
  traffic with security groups](emr-security-groups.md "emr-security-groups.md").
- **Amazon EMR block public access (BPA)** prevents you
  from launching a cluster in a public subnet if the cluster has a security
  configuration that allows inbound traffic from public IP addresses on a port.
  For more information, see [Using Amazon EMR
  block public access](emr-block-public-access.md "emr-block-public-access.md").
- **Secure Shell (SSH)** helps provide a secure way
  for users to connect to the command line on cluster instances. You can also use
  SSH to view web interfaces that applications host on the master node of a
  cluster. For more information, see [Use an EC2 key
  pair for SSH credentials](emr-plan-access-ssh.md "emr-plan-access-ssh.md") and [Connect to a
  cluster](emr-connect-master-node.md "emr-connect-master-node.md").

## Updates to the default Amazon Linux AMI for Amazon EMR

###### Important

EMR clusters that run Amazon Linux or Amazon Linux 2 Amazon Machine Images (AMIs) use default Amazon Linux behavior, and do not
automatically download and install important and critical kernel updates that require a reboot.
This is the same behavior as other Amazon EC2 instances that run the default Amazon Linux AMI. If new Amazon Linux software updates
that require a reboot (such as kernel, NVIDIA, and CUDA updates) become available after
an Amazon EMR release becomes available, EMR cluster instances that run the default AMI do not automatically
download and install those updates. To get kernel updates, you can [customize your Amazon EMR AMI](emr-custom-ami.md "emr-custom-ami.md") to
[use the latest Amazon Linux AMI](../../../AWSEC2/latest/UserGuide/finding-an-ami.md "../../../AWSEC2/latest/UserGuide/finding-an-ami.md").

Depending on the security posture of your application and the length of time that a
cluster runs, you may choose to periodically reboot your cluster to apply security
updates, or create a bootstrap action to customize package installation and updates. You
may also choose to test and then install select security updates on running cluster
instances. For more information, see [Using the default Amazon Linux AMI for Amazon EMR](emr-default-ami.md "emr-default-ami.md"). Note that your networking configuration must
allow for HTTP and HTTPS egress to Linux repositories in Amazon S3, otherwise security
updates will not succeed.

## AWS Identity and Access Management with Amazon EMR

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control
access to AWS resources. IAM administrators control who can be _authenticated_ (signed in) and _authorized_ (have permissions) to use Amazon EMR resources. IAM identities
include users, groups, and roles. An IAM role is similar to an IAM user, but is not
associated with a specific person, and is intended to be assumable by any user who needs
permissions. For more information, see [AWS Identity and Access Management for
Amazon EMR](emr-plan-access-iam.md "emr-plan-access-iam.md"). Amazon EMR uses multiple IAM roles to help you implement access controls
for Amazon EMR clusters. IAM is an AWS service that you can use with no additional
charge.

- **IAM role for Amazon EMR (EMR role)** –
  controls how Amazon EMR service is able to access other AWS services on your
  behalf, such as provisioning Amazon EC2 instances when the Amazon EMR cluster launches.
  For more information, see [Configure IAM service
  roles for Amazon EMR permissions to AWS services and resources](emr-iam-roles.md "emr-iam-roles.md").
- **IAM role for cluster EC2 instances (EC2 instance
  profile)** – a role that is assigned to every EC2 instance
  in the Amazon EMR cluster when the instance launches. Application processes that run
  on the cluster use this role to interact with other AWS services, such as
  Amazon S3. For more information, see [IAM role for
  cluster’s EC2 instances](emr-iam-role-for-ec2.md "emr-iam-role-for-ec2.md").
- **IAM role for applications (runtime role)**
  – an IAM role that you can specify when you submit a job or query to an
  Amazon EMR cluster. The job or query that you submit to your Amazon EMR cluster uses the
  runtime role to access AWS resources, such as objects in Amazon S3. You can specify
  runtime roles with Amazon EMR for Spark and Hive jobs. Bu using runtime roles, you
  can isolate jobs running on the same cluster by using different IAM roles. For
  more information, see [Using IAM
  role as runtime role with Amazon EMR](emr-steps-runtime-roles.md "emr-steps-runtime-roles.md").

Workforce identities refer to users who build or operate workloads in AWS. Amazon EMR
provides support for workforce identities with the following:

- **AWS IAM identity center (Idc)** is the
  recommended AWS service for managing user access to AWS resources. It is a
  single place where you can assign your workforce identities, consistent access
  to multiple AWS accounts and applications. Amazon EMR supports workforce identities
  through trusted identity propagation. With trusted identity propagation
  capability, a user can sign in to the application and that application can pass
  the identity of the user to other AWS services for authorizing access to data
  or resources. For more information see, Enabling support for [AWS
  IAM identity center with Amazon EMR](emr-idc.md "emr-idc.md").

**Lightweight Directory Access Protocol (LDAP)**
is an open, vendor-neutral, industry standard application protocol for accessing
and maintaining information about users, systems, services, and applications
over the network. LDAP is commonly used for user authentication against
corporate identity servers such as Active Directory (AD) and OpenLDAP. By
enabling LDAP with EMR clusters, you allow you users use their existing
credentials to authenticate and access clusters. For more information see,
[enabling support for LDAP with Amazon EMR](ldap.md "ldap.md").

**Kerberos** is a network authentication protocol
designed to provide strong authentication for client/server applications by
using secret-key cryptography. When you use Kerberos, Amazon EMR configures Kerberos
for the applications, components, and subsystems that it installs on the cluster
so that they are authenticated with each other. To access a cluster with
Kerberos configured, a kerberos principal must be present in the Kerberos Domain
Controller (KDC). For more information, see [enabling support for
Kerberos with Amazon EMR](emr-kerberos.md "emr-kerberos.md").

### Single-tenant and multi-tenant clusters

A cluster is by default configured for a single tenancy with the EC2 Instance
profile as the IAM identity. In a single-tenant cluster, every job has full and
complete access to the cluster and access to all AWS services and resources is
done on the basis of the EC2 instance profile. In a multi-tenant cluster, tenants
are isolated from each other and the tenants don't have full and complete access to
the clusters and EC2 Instances of the cluster. The identity on multi-tenant clusters
is either the runtime roles or the workforce identifies. In a multi-tenant cluster,
you can also enable support for fine-grained access control (FGAC) via AWS Lake Formation or
Apache Ranger. A cluster that has runtime roles or FGAC enabled, access to the EC2
Instance profile is also disable via iptables.

###### Important

Any users who have access to a single-tenant cluster can install any software
on the Linux operating system (OS), change or remove software components
installed by Amazon EMR and impact the EC2 Instances that are part of the cluster. If
you want to ensure that users can't install or change configurations of an Amazon EMR
cluster, we recommend that you enable multi-tenancy for the cluster. You can
enable multi-tenancy on a cluster by enabling support for runtime role, AWS
IAM identity center, Kerberos, or LDAP.

## Data protection

With AWS, you control your data by using AWS services and tools to determine how
the data is secured and who has access to it. Services such as AWS Identity and Access Management (IAM) let you
securely manage access to AWS services and resources. AWS CloudTrail enables detection and
auditing. Amazon EMR makes it easy for you to encrypt data at rest in Amazon S3 by using keys
either managed by AWS or fully managed by you. Amazon EMR also support enabling encryption
for data in transit. For more information, see [encrypt data at rest and
in transit](emr-data-encryption.md "emr-data-encryption.md").

### Data Access Control

With data access control, you can control what data an IAM identity or a
workforce identity can access. Amazon EMR supports the following access controls:

- **IAM identity-based policies** –
  manage permissions for IAM roles that you use with Amazon EMR. IAM policies
  can be combined with tagging to control access on a cluster-by-cluster
  basis. For more information, see [AWS Identity and Access Management for
  Amazon EMR](emr-plan-access-iam.md "emr-plan-access-iam.md").
- **AWS Lake Formation** centralizes permissions
  management of your data and makes it easier to share across your
  organization and externally. You can use Lake Formation to enable fine-grained,
  column-level access to databases and tables in the AWS Glue Data Catalog. For more
  information, see [Using AWS Lake Formation
  with Amazon EMR](emr-lake-formation.md "emr-lake-formation.md").
- **Amazon S3 access grants** map identities map
  identities in directories such as Active Directory, or AWS Identity and Access Management (IAM)
  principals, to datasets in S3. Additionally, S3 access grants log end-user
  identity and the application used to access S3 data in AWS CloudTrail. For more
  information, see [Using Amazon S3
  access grants with Amazon EMR](emr-access-grants.md "emr-access-grants.md").
- **Apache Ranger** is a framework to enable,
  monitor and manage comprehensive data security across the Hadoop platform.
  Amazon EMR supports Apache Ranger based fine-grained access control for Apache
  Hive Metastore and Amazon S3. For more information see [Integrate Apache Ranger with Amazon EMR](emr-ranger.md "emr-ranger.md").
