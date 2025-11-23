# Best practices for Simple AD

Here are some suggestions and guidelines you should consider to avoid problems and get the
most out of Simple AD.

## Setting up: Prerequisites

Consider these guidelines before creating your directory.

### Verify you have the right directory type

Directory Service provides multiple ways to use Microsoft Active Directory with other AWS
services. You can choose the directory service with the features you need at a cost
that fits your budget:

- **AWS Directory Service for Microsoft Active Directory** is a feature-rich managed
  Microsoft Active Directory hosted on the AWS cloud. AWS Managed Microsoft AD is your best choice
  if you have more than 5,000 users and need a trust relationship set up between an AWS
  hosted directory and your on-premises directories.
- **AD Connector** simply connects your
  existing on-premises Active Directory to AWS. AD Connector is your best
  choice when you want to use your existing on-premises directory with AWS
  services.
- **Simple AD** is a low-scale, low-cost directory
  with basic Active Directory compatibility. It supports 5,000 or fewer users, Samba
  4–compatible applications, and LDAP compatibility for LDAP-aware applications.

For a more detailed comparison of Directory Service options, see [Which to choose](what_is.md#choosing_an_option "what_is.md#choosing_an_option").

### Ensure your VPCs and instances are configured

correctly

In order to connect to, manage, and use your directories, you must properly
configure the VPCs that the directories are associated with. See either [Prerequisites for creating a
AWS Managed Microsoft AD](ms_ad_getting_started.md#ms_ad_getting_started_prereqs "ms_ad_getting_started.md#ms_ad_getting_started_prereqs"), [AD Connector prerequisites](ad_connector_getting_started.md#prereq_connector "ad_connector_getting_started.md#prereq_connector"), or [Simple AD prerequisites](simple_ad_getting_started.md#prereq_simple "simple_ad_getting_started.md#prereq_simple") for information about the
VPC security and networking requirements.

If you are adding an instance to your domain, ensure that you have connectivity
and remote access to your instance as described in [Ways to join an Amazon EC2 instance to your
AWS Managed Microsoft AD](ms_ad_join_instance.md "ms_ad_join_instance.md").

### Be aware of your limits

Learn about the various limits for your specific directory type. The available storage and the aggregate size of your objects are the only limitations on the number of objects you may store in your directory. See either [AWS Managed Microsoft AD quotas](ms_ad_limits.md "ms_ad_limits.md"), [AD Connector quotas](ad_connector_limits.md "ad_connector_limits.md"), or [Simple AD quotas](simple_ad_limits.md "simple_ad_limits.md") for details about your chosen directory.

### Understand your directory's AWS security group configuration and use

AWS creates a [security group](../../../AWSEC2/latest/UserGuide/using-network-security.md#adding-security-group-rule "../../../AWSEC2/latest/UserGuide/using-network-security.md#adding-security-group-rule") and attaches it to your directory's domain controller [elastic network
interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md"). AWS configures the security group to block unnecessary traffic to the
directory and allows necessary traffic.

#### Modifying the directory security group

You can modify security groups for your directories, but only do so if you fully understand security group filtering. For more information, see [Amazon EC2 security groups for Linux instances](../../../AWSEC2/latest/UserGuide/using-network-security.md "../../../AWSEC2/latest/UserGuide/using-network-security.md") in the _Amazon EC2 User Guide_. Improper changes may disrupt communications with intended computers and instances. AWS recommends against opening additional ports to your directory as this reduces security. Review the [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") before making changes.

###### Warning

It is technically possible for you to associate the directory's security group with
other EC2 instances that you create. However, AWS recommends against this practice. AWS
may have reasons to modify the security group without notice to address functional or
security needs of the managed directory. Such changes affect any instances with which
you associate the directory security group and may disrupt operation of the associated
instances. Furthermore, associating the directory security group with your EC2 instances
may create a potential security risk for your EC2 instances.

### Use AWS Managed Microsoft AD if trusts are required

Simple AD does not support trust relationships. If you need to establish a trust
between your Directory Service directory and another directory, you should use
AWS Directory Service for Microsoft Active Directory.

## Setting up: Creating your directory

Here are some suggestions to consider as you create your directory.

### Remember your administrator ID and password

When you set up your directory, you provide a password for the administrator account.
That account ID is _Administrator_ for Simple AD. Remember the password
that you create for this account; otherwise you will not be able to add objects to your
directory.

### Understand username restrictions for AWS applications

Directory Service provides support for most character formats that can be used in the construction
of usernames. However, there are character restrictions that are enforced on usernames that
will be used for signing in to AWS applications, such as WorkSpaces, WorkDocs, Amazon WorkMail, or Quick Suite. These
restrictions require that the following characters not be used:

- Spaces
- Multibyte characters
- !"#$%&'()\*+,/:;<=>?@[\]^`{|}~

###### Note

The @ symbol is allowed as long as it precedes a UPN suffix.

## Programming your applications

Before you program your applications, consider the following:

### Use the Windows DC locator service

When developing applications, use the Windows DC locator service or use the Dynamic DNS (DDNS) service of your AWS Managed Microsoft AD to locate domain controllers (DCs). Do not hard code applications with the address of a DC. The DC locator service helps ensure directory load is distributed and enables you to take advantage of horizontal scaling by adding domain controllers to your deployment. If you bind your application to a fixed DC and the DC undergoes patching or recovery, your application will lose access to the DC instead of using one of the remaining DCs. Furthermore, hard coding of the DC can result in hot spotting on a single DC. In severe cases, hot spotting may cause your DC to become unresponsive. Such cases may also cause AWS directory automation to flag the directory as impaired and may trigger recovery processes that replace the unresponsive DC.

### Load test before rolling out to production

Be sure to do lab testing with objects and requests that are representative of your
production workload to confirm that the directory scales to the load of your application.
Should you require additional capacity, you should use Directory Service for Microsoft
Active Directory, which enables you to add domain controllers for high performance. For more
information, see [Deploying additional domain controllers for your
AWS Managed Microsoft AD](ms_ad_deploy_additional_dcs.md "ms_ad_deploy_additional_dcs.md").

### Use efficient LDAP queries

Broad LDAP queries to a domain controller across thousands of objects can consume
significant CPU cycles in a single DC, resulting in hot spotting. This may affect
applications that share the same DC during the query.
