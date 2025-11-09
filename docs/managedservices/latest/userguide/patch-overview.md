# AMS standard patching

AMS supports existing customers using the AMS standard patching model, but this model is not available
for new customers and is being retired in favor of AMS Patch Orchestrator.

Typical patch contents for AMS standard patching include vendor updates for supported
operating systems and software preinstalled with supported operating systems (for
example, IIS and Apache Server).

During AMS onboarding, you specify patching requirements, policy, frequency, and
preferred patch windows.
These configurations mean you can avoid taking applications offline all at
once for infrastructure patching, so you can control what infrastructure gets patched when.

###### Note

The patching process described in this topic applies only to your stacks. AMS
infrastructure is patched during a separate process. The AWS Managed Services Maintenance Window (or Maintenance Window) performs maintenance activities for AWS Managed Services (AMS) and recurs the second Thursday of every month from
3 PM to 4 PM Pacific Time. AMS may change the maintenance window with 48 hours notice. You configure the
AMS patch window at onboarding, or you approve or reject the monthly patch service notification.

AMS regularly scans managed Amazon EC2 instances for
updates available through the operating system update functionality. We also provide
regular updates to the AMS base Amazon Machine Images (AMIs) supported in our environment.

After they are validated, AMS AMI releases are shared with all AMS accounts. You
can view the available AWS AMI releases by using the
[DescribeImages](../../../AWSEC2/latest/APIReference/API_DescribeImages.md "../../../AWSEC2/latest/APIReference/API_DescribeImages.md")
Amazon EC2 API call or using the Amazon EC2 console. To find available AMS AMIs, see [Find AMI IDs, AMS](find-ami.md "find-ami.md").

AMS performs ad hoc patching schedules only when requested by you.Previously AMS would send a notification;
currently, a notification is not sent.

###### Note

By default, AMS uses Systems Manager to apply patches by having the package
manager (Linux) or System Update service (Windows) query its default repository to
see which new packages are available. If, during the course of your day-to-day
operations, you have installed a package on a Linux host using the default package
manager, that package manager also picks up new packages for that software when
they're available. In such a case, you may want to take a patching action (described
in this section) to opt-out for that instance.

## Supported operating systems

**Supported operating systems (x86-64)**

- Amazon Linux 2023
- Amazon Linux 2 (**expected AMS support end date June 30, 2026**)
- Oracle Linux 9.x, 8.x
- Red Hat Enterprise Linux (RHEL) 9.x, 8.x
- SUSE Linux Enterprise Server 15 SP6
- SUSE Linux Enterprise Server for SAP 15 SP3 and later
- Microsoft Windows Server 2022, 2019, 2016
- Ubuntu 20.04, 22.04, 24.04

**Supported operating systems (ARM64)**

- Amazon Linux 2023
- Amazon Linux 2 (**expected AMS support end date June 30, 2026**)

## Supported patches

AWS Managed Services supports patching primarily at the operating system level. The patches that are installed may differ by operating system.

###### Important

All updates are downloaded from the Systems Manager patch baseline service
remote repositories configured on the instance, and described later in this
topic. The instance must be able to connect to the repositories so the patching can be performed.

To opt-out of the patch baseline service for repositories that deliver
packages that you want to maintain yourself, run the following command to disable the repository:

```
yum-config-manager DASHDASHdisable `REPOSITORY_NAME`
```

Retrieve the list of currently configured repositories with the following
command:

```
yum repolist
```

- **Amazon Linux** preconfigured repositories (usually
  four):

| Repository ID       | Repository name                                   |
| ------------------- | ------------------------------------------------- |
| amzn-main/latest    | amzn-main-Base                                    |
| amzn-updates/latest | amzn-updates-Base                                 |
| epel/x86_64         | Extra Packages for Enterprise Linux 6<br>• x86_64 |
| pbis                | PBIS Packages Updates                             |

- **Red Hat Enterprise Linux** preconfigured repositories
  (five for Red Hat Enterprise Linux 7 and five for Red Hat Enterprise Linux 6):

| Repository ID                                   | Repository name                                            |
| ----------------------------------------------- | ---------------------------------------------------------- |
| rhui-REGION-client-config-server-7/x86_64       | Red Hat Update Infrastructure 2.0 Client Configuration Ser |
| rhui-REGION-rhel-server-releases/7Server/x86_64 | Red Hat Enterprise Linux Server 7                          |
| rhui-REGION-rhel-server-releases/7Server/x86_64 | Red Hat Enterprise Linux Server 7 RH Common(RPMs)          |
| epel/x86_64                                     | Extra Packages for Enterprise Linux 7<br>• x86_64          |
| pbis                                            | PBIS Packages Updates                                      |

| Repository ID                      | Repository name                                    |
| ---------------------------------- | -------------------------------------------------- |
| rhui-REGION-client-config-server-6 | Red Hat Update Infrastructure 2.0                  |
| rhui-REGION-rhel-server-releases   | Red Hat Enterprise Linux Server 6 (RPMs)           |
| rhui-REGION-rhel-server-rh-common  | Red Hat Enterprise Linux Server 6 RH Common (RPMs) |
| epel                               | Extra Packages for Enterprise Linux 6<br>• x86_64  |
| pbis                               | PBIS Packages Updates                              |

- **CentOS 7** preconfigured repositories (usually
  five):

| Repository ID    | Repository Name                                   |
| ---------------- | ------------------------------------------------- |
| base/7/x86_64    | CentOS-7<br>• Base                                |
| updates/7/x86_64 | CentOS-7<br>• Updates                             |
| extras/7/x86_64  | CentOS-7<br>• Extras                              |
| epel/x86_64      | Extra Packages for Enterprise Linux 7<br>• x86_64 |
| pbis             | PBIS Packages Updates                             |

- For **Microsoft Windows Server**, all updates are
  detected and installed using the Windows Update Agent, which is configured
  to use the Windows Update catalog (this doesn't include updates from
  Microsoft Update).

On Microsoft Windows operating systems, Patch Manager uses Microsoft’s cab
file wsusscn2.cab as the source of available operating system security
updates. This file contains information about the security-related updates
that Microsoft publishes. Patch Manager downloads this file regularly from
Microsoft and uses it to update the set of patches available for Windows
instances. The file contains only updates that Microsoft identifies as being
related to security. As the information in the file is processed, Patch
Manager also removes updates that have been replaced by later updates.
Therefore, only the most recent update is displayed and made available for
installation. For example, if KB4012214 replaces KB3135456, only KB4012214
is made available as an update in Patch Manager.

To read more about the wsusscn2.cab file, see the Microsoft article
[Using WUA to Scan for Updates Offline](<https://msdn.microsoft.com/en-us/library/windows/desktop/aa387290(v=vs.85).aspx> "https://msdn.microsoft.com/en-us/library/windows/desktop/aa387290(v=vs.85).aspx").

## Patching and infrastructure design

AMS employs different patching methods depending on your infrastructure design:
mutable or immutable (for detailed definitions, see [AMS key terms](key-terms.md "key-terms.md")).

With mutable infrastructures, patching is done using a traditional in-place
methodology of installing updates directly to the Amazon EC2 instances, individually,
by AMS operations engineers. This patching
method is used for stacks that are not Auto Scaling groups, and contain a single Amazon EC2
instance or a few instances. In this scenario, replacing the AMI that the instance
or stack was based on would destroy all of the changes made to that system since it
was first deployed, so that is not done. Updates are applied to the running system,
and you may experience system downtime (depending on the stack configuration) due to
application or system restarts. This can be mitigated with a Blue/Green update
strategy. For more information, see
[AWS CodeDeploy Introduces Blue/Green Deployments](https://aws.amazon.com/about-aws/whats-new/2017/01/aws-codedeploy-introduces-blue-green-deployments/ "https://aws.amazon.com/about-aws/whats-new/2017/01/aws-codedeploy-introduces-blue-green-deployments/").

With immutable infrastructures, the patching method is AMI replacement. Immutable
instances are updated uniformly using an updated AMI that replaces the AMI specified
in the Auto Scaling group configuration. AMS releases updated (that is, patched)
AMIs every month, usually the week of Patch Tuesday. The following section describes how this works.

## AMS standard patching failures

In case of failed updates, AMS performs an analysis to understand the cause of
failure and communicates the outcome of the analysis to you. If the failure is
attributable to AMS, we retry the updates if it's within the maintenance window.
Otherwise, AMS creates service notifications for the failed instance update and waits
for your instructions.

For failures attributable to your system, you can submit a service request with a new
patch RFC to update the instances.
