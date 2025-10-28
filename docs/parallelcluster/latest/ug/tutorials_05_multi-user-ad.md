# Integrating Active Directory

In this tutorial, you create a multiple user environment. This environment includes an AWS ParallelCluster that's integrated with an AWS Managed Microsoft AD
(Active Directory) at `corp.example.com`. You configure an `Admin` user to manage the directory, a `ReadOnly`
user to read the directory, and a `user000` user to log into the cluster. You can use either the automated path or the manual path to
create the networking resources, an Active Directory (AD), and the Amazon EC2 instance that you use to configure the AD. Regardless of the path, the
infrastructure that you create is pre-configured to integrate AWS ParallelCluster using one of the following methods:

- LDAPS with certificate verification (recommended as the most secure option)
- LDAPS without certificate verification
- LDAP
  LDAP by itself _doesn't_ provide encryption. To ensure secure transmission of potentially sensitive information, we strongly recommend
  that you use LDAPS (LDAP over TLS/SSL) for clusters integrated with ADs. For more information, see
  [Enable server-side LDAPS using
  AWS Managed Microsoft AD](../../../directoryservice/latest/admin-guide/ms_ad_ldap_server_side.md "../../../directoryservice/latest/admin-guide/ms_ad_ldap_server_side.md") in the AWS Directory Service _Administration Guide_.

After you create these resources, proceed to configure and create your cluster integrated with your Active Directory (AD). After the cluster
is created, log in as the user you created. For more information about the configuration that you create in this tutorial, see [Multiple user access to clusters](multi-user-v3.md "multi-user-v3.md") and the [DirectoryService](DirectoryService-v3.md "DirectoryService-v3.md") configuration section.

This tutorial covers how to create an environment that supports multiple user access to clusters. This tutorial doesn't cover how you create
and use an AWS Directory Service AD. The steps that you take to set up an AWS Managed Microsoft AD in this tutorial are provided for testing purposes only. They
_aren't_ provided to replace the official documentation and best practices you can find at [AWS Managed Microsoft AD](../../../directoryservice/latest/admin-guide/directory_microsoft_ad.md "../../../directoryservice/latest/admin-guide/directory_microsoft_ad.md") and [Simple AD](../../../directoryservice/latest/admin-guide/directory_simple_ad.md "../../../directoryservice/latest/admin-guide/directory_simple_ad.md") in the _AWS Directory Service Administration
Guide_.

###### Note

Directory user passwords expire according to the directory password policy property definitions. To reset directory
passwords with AWS ParallelCluster, see [How to reset a user password and expired passwords](troubleshooting-v3-multi-user.md#troubleshooting-v3-multi-user-reset-passwd "troubleshooting-v3-multi-user.md#troubleshooting-v3-multi-user-reset-passwd").

###### Note

The directory domain controller IP addresses can change due to domain controller changes and directory maintenance. If you chose the automated
quick create method to create the directory infrastructure, you must manually align the load balancer in front of the directory controllers when the
directory IP addresses change. If you use the quick create method, the directory IP addresses aren't automatically aligned with the load balancers.

When using the AWS ParallelCluster command line interface (CLI) or API, you only pay for
the AWS resources that are created when you create or update AWS ParallelCluster images and clusters. For more information,
see [AWS services used by AWS ParallelCluster](aws-services-v3.md "aws-services-v3.md").

###### Prerequisites

- AWS ParallelCluster [is installed](install-v3-parallelcluster.md "install-v3-parallelcluster.md").
- The AWS CLI [is installed and configured.](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")
- You have an [Amazon EC2 key pair](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md").
- You have an IAM role with the [permissions](iam-roles-in-parallelcluster-v3.md#iam-roles-in-parallelcluster-v3-example-user-policies "iam-roles-in-parallelcluster-v3.md#iam-roles-in-parallelcluster-v3-example-user-policies")
  required to run the [pcluster](pcluster-v3.md "pcluster-v3.md") CLI.
  As you go through the tutorial, replace `inputs highlighted in red`, such as
  `region-id` and `d-abcdef01234567890`, with your own names and IDs.
  Replace `0123456789012` with your AWS account number.
