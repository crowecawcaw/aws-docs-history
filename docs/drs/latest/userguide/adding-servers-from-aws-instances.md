# Adding instances from the Amazon EC2

Console

You can now add EC2 instances as source servers in DRS, starting from the EC2 console.
New or existing instances can be added by selecting the appropriate action on the EC2 console,
sending you to the AWS focused page allowing to install the AWS replication agent used by DRS on the selected instances.

## Add instances

You can protect your EC2 instances using AWS Elastic Disaster Recovery (DRS) in the chosen AWS Region, by adding to them to AWS DRS as source servers.
Utilize AWS Systems Manager (SSM) if present on your instance to install the AWS replication agent,
a step needed to start replicating data from your instance to AWS.
Only instances managed by AWS Systems Manager would be able to have the AWS replication agent installed on them.

###### Note

You need an instance profile with the policies listed below in order to have
your instances managed by SSM and for installing the AWS replication agent:

1. [AmazonSSMManagedInstanceCore](../../../aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.md "../../../aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.md")
2. [AWSElasticDisasterRecoveryEC2InstancePolicy](security-iam-awsmanpol-AWSElasticDisasterRecoveryEc2InstancePolicy.md "security-iam-awsmanpol-AWSElasticDisasterRecoveryEc2InstancePolicy.md")

Successfully installing the AWS replication agent adds the instance to AWS DRS (as a **source server**) in the chosen target region.

## Supported EC2 instances

###### Note

Any additional EBS volumes added during the EC2 Instance creation that are
offline, unmounted, or unformatted are not replicated. Any volume that is later placed
online or mounted with a valid file system is automatically replicated if [Automatically replicate new disks](volumes-drs.md#auto-replicate "volumes-drs.md#auto-replicate") is enabled.

This section lists all the instances that were selected to be protected by AWS DRS.
The list shows which instances are currently managed by SSM and which instances are currently not managed.
Only instances managed by SSM can have the AWS replication agent installed on them using this page.
You can also install the agent using the installer as defined in [Installing the AWS Replication Agent](agent-installation.md "agent-installation.md"),
without requiring the SSM agent to be present and active on the server to be protected.

To have an instance managed by SSM, requires the SSM agent to be installed on a
compatible operating system ([or preinstalled in the AMI](../../../systems-manager/latest/userguide/ami-preinstalled-agent.md "../../../systems-manager/latest/userguide/ami-preinstalled-agent.md")), and the instance to have the correct permissions
(as defined in the [AmazonSSMManagedInstanceCore](../../../aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.md "../../../aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.md") and the [AWSElasticDisasterRecoveryEC2InstancePolicy](security-iam-awsmanpol-AWSElasticDisasterRecoveryEc2InstancePolicy.md "security-iam-awsmanpol-AWSElasticDisasterRecoveryEc2InstancePolicy.md") policies). To update the instance
profiles, the **Instance profile role installation** section
allows you to create the default instance profile (with the two policies mentioned above)
if needed. The **Instance profiles** section allow you to
assign instance profiles to instances, and automatically assigns the default instance
profile to all instances that do not have any instance profile attached to them. Use the
**Attach profiles to all instances** button to attach the
assigned instance profiles to the instances in case the default profile was created and
automatically assigned to them or if you changed the assigned instance profile.

## Target disaster recovery region

On this section, you can define the target disaster recovery region. This can be
the same region where the instances are present in, or it can be a different region, for
cross-region protection. AWS DRS must be initialized in the target region in order to
protect the instances onto that region. The indicator next to the region’s name shows if
AWS DRS is already initialized in the target region, or not. If the region is not
initialized, a button labelled Initialize and configure AWS Elastic Disaster Recovery is
visible and active. Choosing this button opens the AWS DRS initialization wizard for AWS
DRS in the target region on another browser tab.

## Instance profile role installation - optional

This section provides you with the option to create the default IAM role with the
required permissions as an instance profile. The role **AWSElasticDisasterRecoveryAutomatedAgentInstallRole** includes the permissions
defined in the policies [AmazonSSMManagedInstanceCore](../../../aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.md "../../../aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.md") and [AWSElasticDisasterRecoveryEC2InstancePolicy](security-iam-awsmanpol-AWSElasticDisasterRecoveryEc2InstancePolicy.md "security-iam-awsmanpol-AWSElasticDisasterRecoveryEc2InstancePolicy.md"). These permissions are required to
allow the SSM agent to operate and to install the AWS replication agent, respectively.
Clicking the **Install default IAM role** installs this role.
This needs to be done only once per account. If the role was already installed in the
account, this button is inactive. The default instance profile role is automatically
assigned to instances without an instance profile in the **Instance
profiles** section. If you click the **Attach profiles to
all instances** button, this role is attached to all instances it was assigned
to in the **Instance profiles** section. If this default IAM
role is not installed, you need to make sure you have an instance profile with the [AmazonSSMManagedInstanceCore](../../../aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.md "../../../aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.md") and [AWSElasticDisasterRecoveryEC2InstancePolicy](security-iam-awsmanpol-AWSElasticDisasterRecoveryEc2InstancePolicy.md "security-iam-awsmanpol-AWSElasticDisasterRecoveryEc2InstancePolicy.md") policies (or the combined set of
permissions within both of these policies).

## Instance profiles

This section lists all the instances that were selected to be protected by adding
them as source servers to AWS DRS and their current instance profiles. Instances without
any instance profile have the **AWSElasticDisasterRecoveryAutomatedAgentInstallRole** instance profile and IAM
role assigned to them if it exists on this account. Using the default profile is not
mandatory, as any instance profile in the account can be assigned to any instance, but
care must be taken to verify each instance has an instance profile with the permissions
defined in the [AmazonSSMManagedInstanceCore](../../../aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.md "../../../aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.md") and [AWSElasticDisasterRecoveryEC2InstancePolicy](security-iam-awsmanpol-AWSElasticDisasterRecoveryEc2InstancePolicy.md "security-iam-awsmanpol-AWSElasticDisasterRecoveryEc2InstancePolicy.md") policies.

###### Note

AWS DRS does not validate the instance profile has the required permissions to support
working with the SSM agent or installing the AWS replication agent for DRS.

###### Note

Attaching an instance profile with the needed permissions is a mandatory step if you want to install AWS DRS on instances
that have the SSM agent installed on them (manually, or preinstalled on AMI) but are not managed on SSM due to missing an instance profile with the
[AmazonSSMManagedInstanceCore](../../../aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.md "../../../aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.md") policy.

Click the button labelled **Attach profiles to all instances** to
attach the assigned instance profiles to their instances.

After attaching such a profile, allow AWS DRS a few minutes to identify the
instance as managed by SSM. If SSM is present on the instance, and an instance profile
with the needed permissions was attached to the instance, then within a few minutes, the
marker near the instance ID changes to show that the instance is currently managed by SSM.

## Attach profiles to all instances

Clicking this button attaches the instance profiles assigned in the **Instance profiles**
section to their instances.
After attaching appropriate instance profiles to instances, allow a few minutes for DRS to
detect if these instances are managed by SSM.

## Add instances

Click this button to install the AWS replication agent on all instances that are
currently managed by SSM. If there are such instances, AWS DRS lists those instances and
the progress of installing the AWS replication agent on them. Successfully installing the
AWS replication agent on these instances adds them as source servers to AWS DRS. If there
are no instances that are currently managed by SSM, try installing the SSM agent on these
instances, then attach an appropriate instance profile to them.

## Add instances result page

On this page you can view the result of adding instances to AWS DRS by installing the AWS replication agent on them.
The page shows the progress of this process if currently running, or the summary of the last run.
In addition, for each instance that is currently managed by SSM, there is a table listing the following:

**Instance ID** - The ID of the instance.
This also links to the instance on the EC2 console page (opens in a different browser tab).

**Status** - The current status of the installation, possible values include
**Success**, **In Progress**,
**Pending** and **Error**.

**Details** - holds a link to the source servers page on the target region for
successful installations, or a link to the run log on the SSM console (opens in a new browser tab) for runs
that have failed, are pending or are in progress.
