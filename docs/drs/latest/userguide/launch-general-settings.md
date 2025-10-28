# DRS launch settings

The **DRS launch settings** section allows you to
control server-specific settings.

To edit these settings for a single server, take the following steps:

1. Go to the **Source servers** page.
2. Select a source server to update.
3. Under the **Actions** menu, select
   **Edit DRS launch settings** and you will be
   navigated to the **Edit DRS launch template** page
   within the AWS DRS console.
4. Change the settings according to your preferences.
5. Click **Save settings**.
   Alternatively:

- Go to the **Source servers** page.
- Select a specific source server.
- Go to the **Launch settings** tab.
- Click **Edit** in the DRS launch settings
  section.

## DRS launch settings parameters

The DRS launch settings include the following parameters:

- **Instance type right-sizing –** choose whether
  to allow AWS Elastic Disaster Recovery to launch a drill, recovery, or failback instance type
  that best matches the hardware configuration of the source server. If you
  activate this feature, any modification you make to the instance type in the
  EC2 launch template will be overwritten by the service.
- - If you select the **Active (basic)**
    option, AWS Elastic Disaster Recovery will launch an AWS instance type that best
    matches the OS, CPU, and RAM of your source server. AWS Elastic Disaster Recovery will
    launch a new instance type after every change of configuration on
    the source server (for example, added/removed disks, added/removed
    RAM). Instance types are only chosen from the C5 family.
  - If you select the **Active (in-aws)** option,
    AWS Elastic Disaster Recovery will periodically update the EC2 launch template based on the hardware
    configuration of the EC2 instance source server.
  - If you select **Inactive**, AWS Elastic Disaster Recovery will
    launch the AWS instance type as configured in your EC2 launch template.
    Select this option if you want to determine the instance type that will be
    launched in AWS for all your drill or recovery servers.

###### Important

    + The AWS instance type selected by AWS Elastic Disaster Recovery when this feature
     is activated will overwrite the instance type defined in your
     EC2 launch template.
    + Hardware changes and the resulting AWS instance type change
     may take up to 90 minutes to be processed by AWS Elastic Disaster Recovery.

The right-sizing instance type selected by AWS Elastic Disaster Recovery will be featured on
the **Server details** tab.

- **Start instance upon launching –** Choose
  whether you want to start your drill and recovery instances automatically
  upon launch or whether you want to launch them in a stopped state.

If you choose **No**, you will have
to start the drill or recovery AWS instance manually from the EC2
Console.

- **Copy Private IP –** Choose whether you want
  AWS Elastic Disaster Recovery to ensure that the private IP used by the drill or recovery
  instance matches the private IP used by the source server. AWS Elastic Disaster Recovery will
  monitor the source server on an hourly basis to identify the private IP and
  will use the private IP of the primary network interface.

The **No** option is chosen by default.
Choose **No** if you do not want the private IP
of the drill or recovery instance to match that of the source
machine.

Choose **Yes** if you want to use a
private IP. The IP will be shown in brackets next to the option.

    + If you choose **Yes**, ensure
     that the IP range of the subnet you set in the EC2 launch
     template includes the private IP address.
    + If the both the source server and the drill or recovery instance
     share the same subnet though a VPN, then the source private IP is
     already in use, and the **Copy private IP** option should not be used.
    + Removing a private IP from a specific server's settings does not remove it from the launch template.

**Copy private IP** will be deactivated if you set a value for
**Launch into instance ID**, as this setting cannot affect an
already launched instance.

- **Transfer server tags –** Choose
  whether you want AWS Elastic Disaster Recovery to transfer any user-configured custom tags from
  your source servers onto your drill or recovery instance. These tags are
  attached to all source servers, all launched drill and recovery instances,
  and all of the ephemeral resources that are created on your AWS Account
  during the normal operation of AWS Elastic Disaster Recovery. Transfer server tags only copies
  tags associated with the source servers in the AWS Elastic Disaster Recovery console, and does
  not copy the EC2 source server tags (in case of AWS to AWS disaster recovery
  implementation).

These resources include:

    + EC2 instances
    + Conversion groups
    + Security groups
    + EBS volumes
    + Snapshots

###### Note

    + AWS Elastic Disaster Recovery automatically adds system tags to all
     resources.
    + Tags that are added on the EC2 launch template will take
     precedence over tags that are transferred directly from the
     source server.

You can always add tags from the Amazon EC2 console as described in
[this Amazon EC2 article](../../../AWSEC2/latest/UserGuide/Using_Tags.md#tag-resources)%5C "../../../AWSEC2/latest/UserGuide/Using_Tags.md#tag-resources)%5C").

**Transfer server tags** is deactivated if you set a value for
**Launch into instance ID**, because this setting cannot affect an
already launched instance.

- **Launch into instance ID** - Configure an existing instance ID to launch into,
  instead of creating a new instance.
  This field allows to select an EC2 instance from the list of EC2 instances available in this region.
  The EC2 instance to launch into must have a tag with key _AWSDRS_ and value
  _AllowLaunchingIntoThisInstance_ to appear in the list, and it must be stopped
  prior to launching into it. When this value is set, the **Transfer server tags** and
  **Copy private IP** settings will be deactivated, as they cannot apply to an already
  launched instance.

###### Note

For the instance to appear and perform as a recovery instance in DRS and allow to run post-launch actions on it, it needs to
have an instance profile that includes the policies **AWSElasticDisasterRecoveryRecoveryInstancePolicy**
and **AmazonSSMManagedInstanceCore**.
The role **AWSElasticDisasterRecoveryRecoveryInstanceWithLaunchActionsRole**, installed from the
Default post-launch actions settings page if not already present, contains these policies and can be used as an instance profile.

The launch into an instance will fail if the following pre-requisites
are not met:

    1. The instance to launch into must have the required tag with key
     *AWSDRS* and value *AllowLaunchingIntoThisInstance*.
    2. The instance to launch into has been stopped.
    3. The instance to launch into must have the same operating systems
     platform (Linux or Windows) as that of the server it is protecting.
    4. If the instance to launch into is a Linux it must have the BIOS
     boot mode, and if Windows it must have the same boot mode as that of
     the server it is protecting.
    5. The instance to launch into must have the x86\_64 architecture, HVM
     virtualization and an EBS root device.
    6. **OS licensing** can only be **Bring Your Own License (BYOL)** if the
     instance’s platform is Linux or if the instance’s **tenancy** is **dedicated host**.
    7. **Transfer server tags** and **Copy private IP** must be deactivated (this
     is done automatically when **Launch into
     instance ID** is set via the console).

- **OS licensing –** Choose whether you want to
  Bring Your Own Licenses (BYOL) from the source server into the drill or
  recovery instance.

The **Use default** option will use the default licensing
mechanism for your operating system.

Choose **BYOL** if:

    + You are migrating a Linux server. All Linux licenses are BYOL by
     default. Any RHEL, SUSE, or Debian licenses will be transferred in
     their current form to the recovered instance. Make sure that the
     terms of your licenses allow this license transfer.
    + You want to BYOL your Windows licenses. This will set up a
     dedicated host through which all the licenses from the Windows
     source server will be automatically transferred to the drill or
     recovery instance.

###### Important

If you activate BYOL licensing for Windows, you have to change the
**Placement.tenancy** type in the EC2
launch template to **Host**. Otherwise,
instance launch will fail.

###### Note

    + Windows Desktop Editions require BYOL – [note
     the specific restrictions for AWS Provided
     Licenses](https://aws.amazon.com/windows/faq/#buy-win-cl "https://aws.amazon.com/windows/faq/#buy-win-cl").
    + If you are using Windows Servers datacenter: Azure addition,
     [note the specified restrictions for BYOL](https://www.microsoft.com/licensing/terms/productoffering/WindowsServerStandardDatacenterEssentials/EAEAS#UseRights "https://www.microsoft.com/licensing/terms/productoffering/WindowsServerStandardDatacenterEssentials/EAEAS#UseRights").
