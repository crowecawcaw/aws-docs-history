# Joining instances to an Active Directory domain

With AWS Elastic Beanstalk, the Windows Server instances in your environment can automatically join an Active Directory domain. You manage the directory
with [AWS Directory Service](../../../directoryservice/latest/admin-guide/what_is.md "../../../directoryservice/latest/admin-guide/what_is.md"), and you turn on the join with
configuration options in the `aws:elasticbeanstalk:windows:activedirectory` namespace. Each instance then joins the domain when it launches,
before Elastic Beanstalk deploys your application to it. You don't write any custom join logic or manage the join yourself.

You can join instances to an AWS Managed Microsoft AD directory or a Simple AD directory, or to your self-managed Active Directory through AD
Connector.

###### Note

Active Directory domain join is available on Windows Server platform versions released on or after [August 18, 2026](../relnotes/release-2026-08-18-windows.md "../relnotes/release-2026-08-18-windows.md"). Earlier platform versions don't support the
`aws:elasticbeanstalk:windows:activedirectory` namespace and reject its options during validation. To upgrade your environment, see [Updating your Elastic Beanstalk environment's platform version](using-features.platform.upgrade.md "using-features.platform.upgrade.md").

## How the domain join works

When an instance in an environment with Active Directory options launches, it does the following before Elastic Beanstalk deploys your application:

1. Creates a computer object for itself in the directory. The instance calls the AWS Directory Service [CreateComputer](../../../directoryservice/latest/devguide/API_CreateComputer.md "../../../directoryservice/latest/devguide/API_CreateComputer.md") API operation with the credentials
   of the environment's instance profile. If you set the `DirectoryOU` option, the instance creates the computer object in
   that organizational unit (OU). Otherwise, it creates the object in the directory's default container.
2. Renames itself to `EC2-`XXXXXXXX`, where `XXXXXXXX`` is the last eight
   characters of the instance ID in uppercase.
3. Joins the domain, and then reboots to complete the join. This is the same one-time reboot that every Windows Server instance in an Elastic Beanstalk
   environment performs during provisioning to apply its hostname, so the domain join doesn't add an extra reboot.

Without Active Directory options, Elastic Beanstalk derives each Windows instance's hostname from its private IPv4 address (for example,
`IP-0A010203`). IP addresses can be reused, so these names can collide with stale computer objects in a directory. This can happen in
disaster recovery topologies that reuse IP ranges across Regions, or in long-lived environments. When Active Directory options are set, the hostname
derives from the instance ID instead. Because each instance ID is globally unique, the chance of a name collision with a stale computer object is negligible. The
instance-ID-derived hostname applies only to environments with Active Directory options.

## Prerequisites

Before you configure Active Directory domain join, verify that the following prerequisites are met:

- **An AWS Directory Service directory** – AWS Managed Microsoft AD, Simple AD, or AD
  Connector. To create one, see [Setting up AWS
  Directory Service](../../../directoryservice/latest/admin-guide/getting_started.md "../../../directoryservice/latest/admin-guide/getting_started.md") in the _AWS Directory Service Administration Guide_.
- **Network connectivity and DNS resolution** – Your environment must run in a VPC from which the directory is
  reachable, and the instances in your environment must resolve the directory's DNS name. The join process discovers domain controllers through DNS SRV
  records. This typically means associating your VPC with a DHCP options set that points to the directory's DNS servers. This is the standard
  AWS Directory Service configuration. For more information, see [Create or change a DHCP options set](../../../directoryservice/latest/admin-guide/dhcp_options_set.md "../../../directoryservice/latest/admin-guide/dhcp_options_set.md") in the
  _AWS Directory Service Administration Guide_. Missing DNS resolution is a common cause of failed domain joins.
- **Instance profile permissions** – The environment's [instance
  profile](iam-instanceprofile.md "iam-instanceprofile.md") (for example, `aws-elasticbeanstalk-ec2-role`) must have permission to call `ds:CreateComputer` on the
  directory. To follow the principle of least privilege, add a policy scoped to your directory:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "ds:CreateComputer",
      "Resource": "arn:aws:ds:`us-east-2`:`123456789012`:directory/`d-1234567890`"
    }
  ]
}
```

Alternatively, you can attach the [AmazonSSMDirectoryServiceAccess](../../../aws-managed-policy/latest/reference/AmazonSSMDirectoryServiceAccess.md "../../../aws-managed-policy/latest/reference/AmazonSSMDirectoryServiceAccess.md") managed policy, which
includes the `ds:CreateComputer` permission for all directories in your account.

- **A supported platform version** – Your environment must run a Windows Server platform version released on or
  after [August 18, 2026](../relnotes/release-2026-08-18-windows.md "../relnotes/release-2026-08-18-windows.md").
- **An existing OU (if you set `DirectoryOU`)** – Elastic Beanstalk doesn't create organizational units.
  If you set the `DirectoryOU` option, the OU must already exist in the directory, or the join fails.

## Configuring Active Directory domain join

To turn on Active Directory domain join, set the following configuration options in the `aws:elasticbeanstalk:windows:activedirectory`
namespace. You can set them in a [configuration file](ebextensions.md "ebextensions.md"), with the AWS CLI, or with any other method for setting [configuration options](command-options.md "command-options.md"). For details about each option, see [aws:elasticbeanstalk:windows:activedirectory](command-options-general.md#command-options-general-elasticbeanstalkwindowsactivedirectory "command-options-general.md#command-options-general-elasticbeanstalkwindowsactivedirectory").

- `DirectoryId` – The ID of the directory to join (for example, `d-1234567890`). Setting this option turns on the
  feature. If you don't set it, your environment's behavior doesn't change.
- `DirectoryName` – The fully qualified DNS name of the directory (for example, `corp.example.com`). Required when
  `DirectoryId` is set.
- (Optional) `DirectoryOU` – The distinguished name of the organizational unit to create computer objects in (for example,
  `OU=WebServers,DC=corp,DC=example,DC=com`). The OU must already exist. If you don't set this option, computer objects are created in the
  directory's default container.

The following AWS CLI example configures Active Directory domain join on a running environment. The example uses the JSON syntax for the
`--option-settings` parameter, because `DirectoryOU` values contain commas, which the shorthand syntax interprets as
separators.

###### Example AWS CLI - Configure Active Directory domain join

```
aws elasticbeanstalk update-environment \
    --environment-name `my-env` \
    --option-settings '[
      {"Namespace": "aws:elasticbeanstalk:windows:activedirectory", "OptionName": "DirectoryId", "Value": "`d-1234567890`"},
      {"Namespace": "aws:elasticbeanstalk:windows:activedirectory", "OptionName": "DirectoryName", "Value": "`corp.example.com`"},
      {"Namespace": "aws:elasticbeanstalk:windows:activedirectory", "OptionName": "DirectoryOU", "Value": "`OU=WebServers,DC=corp,DC=example,DC=com`"}
    ]'
```

###### Important

When you add, change, or remove any option in this namespace, Elastic Beanstalk reprovisions the Amazon EC2 instances in your environment. This triggers a [rolling update](using-features.rollingupdates.md "using-features.rollingupdates.md").

If you change the environment's configuration to point to a different directory, the replacement instances join the new directory. If you remove the
options, the replacement instances launch without joining a domain and use the standard IP-address-derived hostnames. In both cases, the computer objects
that the previous instances created remain in the directory. For more information, see [Managing computer objects in your directory](#dotnet-activedirectory-cleanup "#dotnet-activedirectory-cleanup").

## Confirming the domain join

To confirm that an instance joined the domain, do either of the following:

- Verify that a computer object named `EC2-`XXXXXXXX`` (the instance's hostname) exists in your directory,
  under the OU you specified or the default container.
- Review the instance's deployment log for the line `Active Directory: joined to `directory-name``. For more
  information, see [Viewing deployment logs for an Elastic Beanstalk environment](environments-deployment-logs.md "environments-deployment-logs.md").

When your environment scales out, Auto Scaling adds instances that also join the domain. To review the deployment log for one of these instances, retrieve
it from Amazon S3. For more information, see [Deployment log files on instances](environments-deployment-logs.md#environments-deployment-logs.instance "environments-deployment-logs.md#environments-deployment-logs.instance").

## Failed domain joins

A failed domain join doesn't block the deployment. If an instance can't join the domain for any reason, it falls back to the standard
IP-address-derived hostname (`IP-`XXXXXXXX``), the deployment continues, and the environment can still reach the
_Ready_ state and report healthy.

To make the failure visible, Elastic Beanstalk compares the instance's actual domain membership against the configured directory and emits an
`ERROR` [event](using-features.events.md "using-features.events.md") when they don't match:

```
Active Directory domain join did not complete: instance is not joined to '`corp.example.com`' (PartOfDomain=False, Domain=`WORKGROUP`). See the deployment log for the join output.
```

The instance writes the output of the join process to `C:\cfn\log\eb-ad-join.log`. When a join fails, Elastic Beanstalk also copies this log
into the instance's deployment log, so you can retrieve the cause without connecting to the instance. For more information, see [Viewing deployment logs for an Elastic Beanstalk environment](environments-deployment-logs.md "environments-deployment-logs.md").

## Troubleshooting

If your instances don't join the domain, check the following:

- **Join log** – Read the join output in the instance's deployment log (see [Viewing deployment logs for an Elastic Beanstalk environment](environments-deployment-logs.md "environments-deployment-logs.md")), or in `C:\cfn\log\eb-ad-join.log` on
  the instance. The log records the specific error that made the join fail.
- **DNS resolution** – From an instance in the environment's VPC, verify that the directory's DNS name (the
  `DirectoryName` value) resolves. If it doesn't, associate the VPC with a DHCP options set that points to the directory's DNS
  servers.
- **IAM permissions** – Verify that the environment's instance profile allows `ds:CreateComputer`
  on the directory. Without it, the join fails when it tries to create the computer object.
- **Organizational unit** – If you set `DirectoryOU`, verify that the OU exists in the directory and
  that its distinguished name matches the option value exactly. A join into a nonexistent OU fails.
- **Instance configuration** – The file `C:\cfn\eb-ad.json` on each instance records the
  `DirectoryId` and `DirectoryName` that the instance launched with. Use it to confirm which directory configuration the
  instance received.

## Managing computer objects in your directory

Elastic Beanstalk doesn't delete an instance's computer object from your directory when the instance or the environment is terminated. Every joined instance
leaves its `EC2-`XXXXXXXX`` computer object behind, and scaling activity creates an object for each new instance.
You are responsible for periodically removing stale computer objects from your directory, using your organization's usual directory management
tools.

Because each new instance's hostname derives from its own globally unique instance ID, the chance of a name collision with a stale computer object
is negligible.
