NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# AWS related

This section contains answers to questions about AWS and AWS Application Migration Service.

###### Topics

- [What does the AWS Application Migration Service Machine
  Conversion Server do?](#What-Conversion-Server-Do "#What-Conversion-Server-Do")
- [What boot modes are supported by the AWS Application Migration Service?](#Supported-boot-mode "#Supported-boot-mode")
- [How can we encrypt an unencrypted AWS Application Migration Service base snapshot?](#encrypt-base-snapshot "#encrypt-base-snapshot")
- [How do I change the server AMI on AWS after
  Migration?](#How-Change-Server-AMI "#How-Change-Server-AMI")
- [Which AWS services are
  automatically installed when launching a test or cutover instance?](#Which-AWS-Services-Automatically-Installed-Target "#Which-AWS-Services-Automatically-Installed-Target")
- [How long does it take to copy a disk from the
  AWS Application Migration Service staging area to production?](#How-Long-Copy-Disk-Staging "#How-Long-Copy-Disk-Staging")
- [What are the
  differences between conversion servers and replication servers?](#What-differences-Conversion-Servers-Replication-Servers "#What-differences-Conversion-Servers-Replication-Servers")
- [Can I prevent AWS Application Migration Service from cleaning up test instance resources in AWS?](#Can-Prevent-Clean-Up-Target-Resources "#Can-Prevent-Clean-Up-Target-Resources")
- [Why are my Windows server disks read-only
  after launching the test or cutover instance?](#Why-Windows-Server-Disks-Read-Only "#Why-Windows-Server-Disks-Read-Only")
- [What impacts the conversion and boot
  time of test and cutover instances?](#What-Impacts-Conversion-Boot-Time-Target "#What-Impacts-Conversion-Boot-Time-Target")
- [Why do I observe EBS volume performance issues while using test or cutover instances?](#EBS-performance-hit-after-instance-launch "#EBS-performance-hit-after-instance-launch")
- [How is the AWS Licensing Model Tenancy chosen for
  AWS Application Migration Service?](#How-Licensing-Model-Tenancy "#How-Licensing-Model-Tenancy")
- [How does AWS Application Migration Service interact with Interface VPC
  Endpoints?](#mgn-and-vpc "#mgn-and-vpc")
- [How do I use MGN with CloudWatch and EventBridge
  dashboards?](#mgn-and-monitoring "#mgn-and-monitoring")

## What does the AWS Application Migration Service Machine

Conversion Server do?

The machine conversion server converts the disks to boot and run on AWS.

Specifically, the machine conversion server makes bootloader changes, injects hypervisor
drivers and installs cloud tools.

## What boot modes are supported by the AWS Application Migration Service?

The agent supports systems using either BIOS (Basic Input/Output System) or UEFI (Unified Extensible Firmware Interface) boot modes.
BIOS is the traditional boot mode that initializes hardware and bootstraps the operating system. UEFI is a more modern boot firmware that provides additional boot configurations and security features over BIOS.
Both boot modes are fully supported by the agent, giving users flexibility to choose the mode that best fits their systems and requirements. Users can install the agent on servers using either UEFI or legacy BIOS firmware.

## How can we encrypt an unencrypted AWS Application Migration Service base snapshot?

The encryption status of AWS Application Migration Service base snapshots is determined by the default EBS (Elastic Block Store) encryption setting for the respective AWS region.
Encryption Scenarios:

- Default EBS Encryption Enabled:

If the default EBS encryption is enabled for the region, the base snapshots created by MGN will be encrypted.

- Default EBS Encryption Disabled:

If the default EBS encryption is not enabled, the base snapshots will be unencrypted.

- Encrypting Existing Unencrypted Base Snapshots -

To encrypt an existing unencrypted base snapshot, follow these steps:

    1. Delete the unencrypted base snapshot from the snapshots console.
    2. Enable default EBS encryption for the AWS region where the MGN source environment is located.
    3. Initiate a new test or cutover migration in MGN. During this process, MGN will create a new encrypted base snapshot based on the default EBS encryption setting for the region.

###### Note

Enabling default EBS encryption at the region level will encrypt all newly created EBS volumes and snapshots in that region.

## How do I change the server AMI on AWS after

Migration?

After the machine has been launched by AWS Application Migration Service switching the AMI can
be done by launching a vanilla machine from the required AMI, stopping that machine, detaching
all the disks (including the root) and then attaching the disks from the test or cutover
instance created by AWS Application Migration Service.

## Which AWS services are

automatically installed when launching a test or cutover instance?

AWS Application Migration Service automatically installs EC2Config. After installation,
EC2Config automatically installs the SSM EC2 Configuration Service.

CloudWatch, AWS Powershell or CLI are not automatically installed. This can be done by the
combining the AWS Application Migration Service APIs and the AWS APIs – you can use the
AWS Application Migration Service APIs to determine the EC2 instance IDs of the machines and
then use AWS API/CLI to turn on the detailed monitoring. An alternative approach would be to
do it via AWS API only based on the tags you associate with the machine. A third approach
would be to do so from the post-launch script.

AWS Application Migration Service installs EC2Launch (Windows 2016 only). You will need to
configure EC2Launch based on [these specific requirements](../../../AWSEC2/latest/WindowsGuide/ec2launch.md#ec2launch-config "../../../AWSEC2/latest/WindowsGuide/ec2launch.md#ec2launch-config"). This configuration step needs to be performed post
Migration using the wizard in C:\Program
Data\Amazon\EC2-Windows\Launch\Settings\Ec2LaunchSettings.exe on the test or cutover
instance.

## How long does it take to copy a disk from the

AWS Application Migration Service staging area to production?

AWS Application Migration Service uses internal cloud provider snapshots. This process
typically takes less than a minute and the size of the volume does not impact the time.

## What are the

differences between conversion servers and replication servers?

Replication servers run on Linux and conversion servers (for Windows machines) run on
Windows.

The conversion is done by AWS Application Migration Service (AWS MGN) automatically bringing up a vanilla
Windows conversion server machines in the same subnet with the replication servers as part
of the launch job.

Both conversion and replication servers have public IPs.

The conversion servers will use the same security groups as the Replication Server.

The conversion server must be able to access the AWS MGN's service manager.

The conversion server machines, just like the Replication servers are managed automatically
by AWS Application Migration Service. Any attempt to disrupt their automated functionality will
result in failed conversions.

## Can I prevent AWS Application Migration Service from cleaning up test instance resources in AWS?

AWS Application Migration Service will, by default, removes any resources created during the
test process either when requested by the user or when a new Test instance is launched.

To prevent this in AWS, you can [activate Termination Protection](../../../AWSEC2/latest/UserGuide/terminating-instances.md#Using_ChangingDisableAPITermination "../../../AWSEC2/latest/UserGuide/terminating-instances.md#Using_ChangingDisableAPITermination") for the test or cutover instance, and the resources
will not be removed upon a new instance launch.

## Why are my Windows server disks read-only

after launching the test or cutover instance?

When launching test or cutover instances Windows Server may boot with all the disks as
read-only.

This a common issue that occurs when detaching and attaching data disks. This issue can be
resolved using steps in [this
Microsoft TechNet article](https://blogs.technet.microsoft.com/askcore/2011/06/02/my-disk-is-read-only-help/ "https://blogs.technet.microsoft.com/askcore/2011/06/02/my-disk-is-read-only-help/").

## What impacts the conversion and boot

time of test and cutover instances?

Prior to launching the test or cutover instance, AWS Application Migration Service goes through
a machine conversion server process on the boot volume. The conversion process is fairly
quick.

While the actual conversion process itself is quick, the time to boot the test or cutover
instance varies depending on many factors unrelated to any AWS Application Migration Service
processes. Some of these are controllable and should be taken into account when recovery or
cutover times are of importance.

- Operating system – The amount of time required to boot the operating system is dependent
  on the OS itself. While Linux servers typically boot quickly, Windows servers may take
  additional time, due to the nature of the Windows OS. If opportunity permits, test the
  boot time of the source server. If Linux OS takes a long time to boot ensure to check
  that dhclient (Dynamic Host Configuration Protocol Client) is installed and the system
  so it can pull an IP.
- Scheduled Windows Updates – If the Windows server has pending patches, ensure those are
  installed prior to launching the test or cutover instance. If pending patches remain,
  the boot time in the cloud may be severely impacted as the patch process may commence
  upon the initial boot.
- Boot volume type – Depending on services/applications, boot time may be impacted by disk
  performance. It is recommended that boot volumes be tested with a higher performance SSD
  and even by provisioning IOPs to ensure throughput. This may be more critical during the
  first initial boot of the server in the cloud, as all initial settings are applied. In
  many cases, the boot volume type may be scaled back after the initial boot and should be
  tested.

###### Note

The first boot of Windows machines on AWS may take up to 45 minutes due to Windows
adjusting to the AWS virtual hardware.

## Why do I observe EBS volume performance issues while using test or cutover instances?

The EBS volumes attached to the test or cutover instances are created from snapshots of convertered volumes. For any volume type that were created from snapshots, the storage blocks are pulled down from Amazon S3 and written to the volume before accessed by you. This process may take significant time and varies based on the EBS volume type. For additional details and EBS initialization options, refer to [Initialize Amazon EBS volumes](../../../ebs/latest/userguide/ebs-initialize.md "../../../ebs/latest/userguide/ebs-initialize.md")

## How is the AWS Licensing Model Tenancy chosen for

AWS Application Migration Service?

AWS Application Migration Service conforms to the [Microsoft Licensing on
AWS](https://aws.amazon.com/windows/resources/licensing/ "https://aws.amazon.com/windows/resources/licensing/") guidelines.

## How does AWS Application Migration Service interact with Interface VPC

Endpoints?

If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can
establish a private connection between your VPC and AWS Application Migration Service. You can
use this connection to allow AWS Application Migration Service to communicate with your
resources on your VPC without going through the public internet.

Amazon VPC is an AWS service that you can use to launch AWS resources in a virtual
network that you define. With a VPC, you have control over your network settings, such the
IP address range, subnets, route tables, and network gateways. With VPC endpoints, the
routing between the VPC and AWS services is handled by the AWS network, and you can use IAM
policies to control access to service resources.

To connect your VPC to AWS Application Migration Service, you define an _interface VPC endpoint_ for AWS Application Migration Service. An
interface endpoint is an elastic network interface with a private IP address that serves as
an entry point for traffic destined to a supported AWS service. The endpoint provides
reliable, scalable connectivity to AWS Application Migration Service without requiring an
internet gateway, network address translation (NAT) instance, or VPN connection. For more
information, see [What is
Amazon VPC](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md") in the _Amazon VPC User Guide_.

Interface VPC endpoints are powered by AWS PrivateLink, an AWS technology that allows
private communication between AWS services using an elastic network interface with private
IP addresses. For more information, see [AWS
PrivateLink](https://aws.amazon.com/privatelink/ "https://aws.amazon.com/privatelink/").

For more information, see [Getting
Started](../../../vpc/latest/userguide/GetStarted.md "../../../vpc/latest/userguide/GetStarted.md") in the _Amazon VPC User Guide_.

## How do I use MGN with CloudWatch and EventBridge

dashboards?

You can monitor AWS Application Migration Service using CloudWatch, which collects raw data and
processes it into readable, near real-time metrics. AWS Application Migration Service sends
events to Amazon EventBridge whenever a source server launch has completed, a source server reaches
the READY_FOR_TEST lifecycle state for the first time, and when the data replication state
becomes stalled or when the data replication state is no longer Stalled. You can use EventBridge
and these events to write rules that take actions, such as notifying you, when a relevant
event occurs.

You can see MGN in CloudWatch automatic dashboards:

![CloudWatch cross-service dashboard showing Application Migration Service and EC2 metrics.](images/cw1.png)

![AWS Application Migration Service dashboard showing various performance metrics over a 3-hour period.](images/cw2.png)

MGN events can be selected when defining a rule from the EventBridge console:

![Event pattern form showing AWS services dropdown with MGN options and event JSON input area.](images/EB-cw3.jpg)

[Learn more about monitoring MGN](monitoring-overview.md "monitoring-overview.md").
