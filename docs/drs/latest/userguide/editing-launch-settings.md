# Editing the default AWS DRS launch

settings

The default launch settings are applied to every newly launched source server
in AWS Elastic Disaster Recovery (AWS DRS). You can change these settings for a single or multiple
servers whenever you choose.

To edit these settings, follow these steps:

1. Select **Default launch** from the
   left-hand navigation menu (under **Settings**).
2. select **Edit** in the **Default DRS launch settings** section.
3. Change the settings according to your preferences.
4. select **Save**.

## Launch settings

parameters

AWS Elastic Disaster Recovery (AWS DRS) launch settings include:

- **Instance type right sizing –**
  Allow the service to automatically update the instance type on the
  EC2 launch template, based on the CPU and RAM of the source server.
  If this setting is active (default), any modification you make to
  the instance type in the EC2 launch template are overwritten by the
  service.
- **Start instance upon launch –**
  Configure how the EC2 recovery instance should be launched – running
  or in a stopped state.
- **Copy private IP –** Define whether
  the private IP should be copied from the source server’s primary
  network interface to EC2 launch template. If this setting is on,
  make sure that the subnet defined in the EC2 launch template
  includes that IP in its range.
- **Transfer server tags –** Define if
  the launched EC2 instance should have the same tags as the source
  server resource.
- **Launch into source instance -**
  Define whether DRS automatically assigns the ID of the source
  instances to the **Launch into instance
  ID** field in the Launch Settings of newly added source
  servers in this region. A source instance is the EC2 instance in
  this region that was the source of the data before replication was
  reversed to this region or availability zone. The EC2 instance to
  launch into must have a tag with key _AWSDRS_ and value _AllowLaunchingIntoThisInstance_, and it must be
  stopped before launching into it. If **Launch
  into instance ID** is automatically set for a source
  server, the **Transfer server tags**,
  and **Copy private IP** settings need
  to be deactivated for that server, as they cannot apply to an
  already launched instance.

###### Note

Note that for the instance to appear as a recovery instance
in DRS, it needs to have an instance profile that includes the
policy **AWSElasticDisasterRecoveryRecoveryInstancePolicy**.
The role **AWSElasticDisasterRecoveryRecoveryInstanceRole**,
which is added to an account when initializing the service,
contains this policy and can be used as an instance profile.

[Learn more about Launch into source instance](default-drs-launch-into-source-instance.md "default-drs-launch-into-source-instance.md").

- **OS**
  **licensing –** Choose the launched
  instance’s license type for Windows Servers – License-included or
  Bring Your Own License (BYOL). Linux servers and Windows Home are
  automatically launched as BYOL. If you launch a Windows Server or
  Windows Home as BYOL, you must select Dedicated host for the Tenancy
  setting in the advance settings of the EC2 launch template.
