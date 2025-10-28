# Elastic Disaster Recovery quick start guide

This section guides you through your initial Elastic Disaster Recovery setup, including:

###### Topics

- [First time setup](#first-time-setup-gs "#first-time-setup-gs")
- [Adding source servers](#adding-servers-gs "#adding-servers-gs")
- [Configuring launch settings](#configuring-target-gs "#configuring-target-gs")
- [Launching a drill instance](#launching-test-gs "#launching-test-gs")
- [Launching a recovery instance](#launch-recovery-gs "#launch-recovery-gs")
- [Performing a failback](#failback-gs "#failback-gs")

## First time setup

In order to use AWS Elastic Disaster Recovery (AWS DRS), you first need to set it up in each AWS Region in
which you want to use it (the Region into which you will be replicating, and where
you will launch Recovery instances). Setting up the service consists of defining
default replication settings and creating the roles and permissions required for the
service to operate.

###### Note

You need to be the admin user of the AWS account, or have a role with the
AWSElasticDisasterRecoveryConsoleFullAccess permission in order to set up the service

The first setup step for AWS DRS is setting the default replication settings. Choose
**Set default replication settings** on the AWS
Elastic Disaster Recovery landing page. You are guided through the steps of setting
up your default replication settings, default launch settings, and EC2 template.
These default settings are applied to every source server that is added to
AWS Elastic Disaster Recovery. You can change both the default settings and individual source server
settings for one or more source servers at any time. Learn more about editing [your replication settings](default-replication-settings.md "default-replication-settings.md") and
[launch settings](launch-settings-overview.md "launch-settings-overview.md"). To learn more
about each setting, select the **Info** links next to
each section.

###### Important

Before configuring your default settings, ensure that you meet the
[Network requirements for running
AWS Elastic Disaster Recovery](preparing-environments.md "preparing-environments.md")

On the first page of the wizard, you are asked to **Set up replication
servers**. Replication servers are lightweight Amazon EC2 instances that are
used to replicate data between your source servers and AWS. Replication servers
are automatically launched and terminated as needed. You can start using AWS Elastic Disaster Recovery
with the default replication server settings or you can configure your own settings.
[Learn more about replication server
settings.](individual-replication-settings.md#replication-server-settings "individual-replication-settings.md#replication-server-settings")

- Configurable replication server settings include:
  - The subnet within which the replication server will be launched
  - Replication server instance type

During this step you can review the service linked role and additional
policies created during Elastic Disaster Recovery initialization. Choose **View
details** to learn more. the service linked role and additional
policies created during Elastic Disaster Recovery initialization

On the second page of the wizard you are asked to **Specify volumes and
security groups**. For each disk on an added source server there is an
identically-sized EBS volume attached to a replication server, and each replication
server can handle replication of disks from multiple source servers. [Learn more about volumes.](volumes-drs.md "volumes-drs.md")

A security group acts as a virtual firewall, which controls the inbound and outbound
traffic of the staging area. The best practice is to have AWS Elastic Disaster Recovery automatically
attach to and monitor the default AWS Elastic Disaster Recovery security group. This group opens inbound
TCP Port 1500 for receiving the transferred replicated data. [Learn more about security groups.](drs-security-group.md "drs-security-group.md")

Configurable volumes and security groups settings include:

- EBS volume type
- EBS encryption
- Always use AWS Elastic Disaster Recovery security group

On the third page of the wizard you can **Configure
additional replication settings**. These include **Data routing and throttling**, **Point in time
(PIT) policy**, and **Tags**.

- **Data routing and throttling** controls how
  data flows from the external server to the replication servers. If you
  choose not to use a private IP, your replication servers are automatically
  assigned a public IP and data flows over the public internet. [Learn more about data routing and
  throttling.](data-routing.md "data-routing.md")
- Point in Time (PIT) is a disaster recovery feature which allows launching an instance from a
  snapshot captured at a specific point in time. As source servers are
  replicated, snapshots are taken over time. The **Point
  in time (PIT) policy** section allows to configure a retention
  policy that determines which snapshots are not required after a defined
  duration.
- The **Tags** section allows you to add custom tags to
  resources created by AWS Elastic Disaster Recovery in your AWS account.

Additional configurable settings include:

- Use private IP for data replication
- Create public IP
- Throttle network bandwidth
- Snapshot retention
- Tags

On the fourth page of the wizard you can**Set default DRS launch
settings**.

Default launch settings define how drill or recovery instances are launched in AWS. You
can start using AWS Elastic Disaster Recovery with the default launch settings or configure your own.
[Learn more about default DRS launch
settings.](default-drs-launch-settings.md "default-drs-launch-settings.md")

Configurable options include:

- Instance type right sizing
- Start instance upon launch
- Copy private IP
- Transfer server tags
- OS licensing

The fifth page of the wizard: **Set default EC2 launch
settings** is where you configure the default Amazon EC2 launch template which
defines how instances are launched in AWS. Changes you make to the template only
affect new servers, but you can edit the template for multiple servers according to
your preferences. [Learn more about
default EC2 launch template.](default-ec2-launch-template.md "default-ec2-launch-template.md") The EC2 launch template includes basic and
advanced settings.

Basic configurable options include:

- Subnet
- Security groups
- Instance type
- EBS volume type

You only need to change advance configurable options in specific operational scenarios.
They include:

- IAM instance profile
- Tenancy

The sixth page is where you**Review and initialize**.

Review the settings you configured. To change a specific setting select **Edit**, which redirects you to the page in the wizard on
which the setting appears. Go through the remaining pages to return to the **Review and create** page.

Once you have reviewed all of the settings you chose, select **Configure and initialize**. The default template is created and you
return to the AWS Elastic Disaster Recovery console.

###### Note

You can always edit the default replication or launch settings by choosing the appropriate item from the **Settings** page, which you can open from the left-hand navigation menu. Remember that
changes you make are only applied to newly added servers and not to
existing servers.

## Adding source servers

Add source servers to AWS Elastic Disaster Recovery by installing the AWS Replication Agent
(also referred to as "the Agent") on them. The Agent can be installed on both Linux and Windows
servers.
[Learn more about adding source servers.](adding-servers.md "adding-servers.md")

Prior to adding your source servers, ensure that you meet all of the [Network requirements](preparing-environments.md "preparing-environments.md").

###### Note

DRS agents can only be installed on instances that are in AWS Regions that are supported by Elastic Disaster Recovery.

## Configuring launch settings

After you have added your source servers to the AWS Elastic Disaster Recovery console, you need to configure
the launch settings for each server. The launch settings are a set of instructions
that determine how a recovery instance is launched for each source server on AWS.
You must configure the launch settings prior to launching test or recovery
instances. You can use the default settings or configure the settings to fit your
requirements.

###### Note

You can change the launch settings after a drill or recovery instance has been launched.
You need to launch a new Drill or Recovery instance for the new settings to take
effect.

You can access the launch settings by selecting the hostname of a source server on the
**Source servers** page.

Within the individual server view, navigate to the **Launch
settings** tab.

Here you can see your **General launch settings** and your
**EC2 launch template**. Select **Edit** to edit your launch settings or your EC2 launch
template.

Launch settings include:

- **Instance type right-sizing** – The Instance
  type right-sizing feature allows AWS Elastic Disaster Recovery to launch a drill or recovery
  instance type that best matches the hardware configuration of the source
  server. When activated, this feature overrides the instance type selected in
  the EC2 launch template.
- **Start instance upon launch** – Choose whether you want to
  start your Initiate recovery job instances automatically upon launch or
  whether you want to start them manually through the Amazon EC2 Console.
- **Copy private IP** – Choose whether you want
  AWS Elastic Disaster Recovery to verify that the private IP used by the drill or recovery
  instance matches the private IP used by the source server.
- **Transfer server tags** – Choose whether you
  want AWS Elastic Disaster Recovery to transfer any user-configured custom tags from your source
  servers to your drill or recovery instance.

AWS Elastic Disaster Recovery automatically creates an **EC2 launch
template** for each new source server. AWS Elastic Disaster Recovery bases the majority of
the instance launch settings on this template. You can edit this template to fit
your needs.

[Learn more about Launch settings.](launching-target-servers.md "launching-target-servers.md")

## Launching a drill instance

After you have added all of your source servers and configured their launch settings, you
are ready to launch a drill instance. It is crucial to drill the recovery of your
source servers to AWS prior to initiating a recovery in order to verify that your
source servers function properly within the AWS environment.

###### Important

- When launching a drill, recovery, or an in-AWS failback, you can
  launch up to 100 source servers in a single operation. Additional source
  servers can be launched in subsequent operations.
- It is a best practice to perform drills regularly. After launching
  drill instances, use either SSH (Linux) or RDP (Windows) to connect to
  your instance and ensure that everything is working correctly.

You can drill one source server at a time, or simultaneously drill multiple source servers.
For each source server, you are informed of the success or failure of the drill. You
can drill your source server as many times as you want. Each new drill first deletes
any previously launched drill or recovery instance and dependent resources. Then, a
new Drill instance is launched, which reflects the chosen Point-in-time state of the
source server. After the drill, data replication continues as before. The new and
modified data on the source server is transferred to the Staging Area Subnet and not
to the Recovery instances that were launched during the test.

###### Note

- Windows source servers need to have at least 2 GB of free space to
  successfully launch a recovery instance.
- Take into consideration that once a drill instance is launched, actual resources are
  used in your AWS account and you will be billed for these resources. You
  can terminate the operation of launched Recovery instances once you
  verify that they are working properly without impact in order to data
  replication.

[Learn more about launching drill instances
as part of the overall failover and failback framework.](preparing-failover.md#recovery-drill-overview "preparing-failover.md#recovery-drill-overview")

## Launching a recovery instance

Once you have finalized the testing of all of your source servers, you are ready for
recovery. You should perform the recovery at a set date and time. The recovery
migrates your source servers to the recovery instances on AWS.

You can recover one source server at a time, or simultaneously recover multiple source
servers. For each source server you are informed of the success or failure of the
Recovery. For each new recovery, AWS Elastic Disaster Recovery first deletes any previously launched
recovery instance and dependent resources. Then, it launches a new Recovery instance
which reflects the most up-to-date state of the source server. After the Recovery,
data replication continues as before. The new and modified data on the source server
is transferred to the Staging Area Subnet, and not to the recovery instances that
were launched during the recovery.

[Learn more about launching Recovery
instances as part of the overall failover and failback framework.](failback-preparing-failover.md#failback-launching-instances "failback-preparing-failover.md#failback-launching-instances")

## Performing a failback

Once the disaster is over, you can perform a failback to your original source server or to
any other AWS Elastic Disaster Recovery Failback Client on the server. In order to use the Failback
Client, you need to generate Elastic Disaster Recovery-specific credentials. Once
the failback is complete, you can opt to either terminate, delete, or disconnect the
Recovery instance.

[Learn more about performing a failback.](failback-performing.md "failback-performing.md")
