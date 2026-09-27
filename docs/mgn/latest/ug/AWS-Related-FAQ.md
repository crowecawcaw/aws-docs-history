

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Launch questions
<a name="AWS-Related-FAQ"></a>

This section contains answers to questions about launching test and cutover instances with AWS Transform MGN.

**Topics**
+ [What does the AWS Transform MGN Machine Conversion Server do?](#What-Conversion-Server-Do)
+ [What boot modes are supported by the AWS Transform MGN?](#Supported-boot-mode)
+ [What impacts the conversion and boot time of test and cutover instances?](#What-Impacts-Conversion-Boot-Time-Target)
+ [How long does it take to copy a disk from the AWS Transform MGN staging area to production?](#How-Long-Copy-Disk-Staging)
+ [Which AWS services are automatically installed when launching a test or cutover instance?](#Which-AWS-Services-Automatically-Installed-Target)
+ [Why are my Windows server disks read-only after launching the test or cutover instance?](#Why-Windows-Server-Disks-Read-Only)
+ [How do I change the server AMI on AWS after Migration?](#How-Change-Server-AMI)
+ [Can I prevent AWS Transform MGN from cleaning up test instance resources in AWS?](#Can-Prevent-Clean-Up-Target-Resources)
+ [Why do I observe EBS volume performance issues while using test or cutover instances?](#EBS-performance-hit-after-instance-launch)
+ [Which Amazon EBS attributes can I use to optimize EBS volume hydration when launching instances?](#EBS-Volume-Hydration-Attributes)
+ [What are the Amazon EBS volume limits for AWS Transform MGN?](#ebs-limits-faq)
+ [How is the AWS Licensing Model Tenancy chosen for AWS Transform MGN?](#How-Licensing-Model-Tenancy)

## What does the AWS Transform MGN Machine Conversion Server do?
<a name="What-Conversion-Server-Do"></a>

The machine conversion server converts the disks to boot and run on AWS. 

Specifically, the machine conversion server makes bootloader changes, injects hypervisor drivers and installs cloud tools.

## What boot modes are supported by the AWS Transform MGN?
<a name="Supported-boot-mode"></a>

The agent supports systems that use either BIOS (Basic Input/Output System) or UEFI (Unified Extensible Firmware Interface) boot modes. BIOS is the traditional boot mode that initializes hardware and starts the operating system. UEFI is a more modern boot firmware that provides additional boot configurations and security features. You can install the agent on servers that use either UEFI or legacy BIOS firmware.

## What impacts the conversion and boot time of test and cutover instances?
<a name="What-Impacts-Conversion-Boot-Time-Target"></a>

Before launching the test or cutover instance, AWS Transform MGN runs a machine conversion server process on the boot volume. This conversion process is quick.

The time to boot the test or cutover instance varies depending on many factors unrelated to AWS Transform MGN processes. Some of these factors are within your control and should be considered when recovery or cutover times are important.
+ Operating system – The amount of time required to boot the operating system is dependent on the OS itself. Although Linux servers typically boot quickly, Windows servers might take additional time, because of the nature of the Windows OS. If opportunity permits, test the boot time of the source server. If Linux OS takes a long time to boot ensure to check that dhclient (Dynamic Host Configuration Protocol Client) is installed and running on the system so it can pull an IP.
+ Scheduled Windows Updates – If the Windows server has pending patches, ensure those are installed before launching the test or cutover instance. If pending patches remain, the boot time in the cloud might be severely impacted because the patch process might start upon the initial boot.
+ Boot volume type – Depending on services/applications, boot time might be impacted by disk performance. It is recommended that boot volumes be tested with a higher performance SSD and even by provisioning IOPs to ensure throughput. This might be more critical during the first initial boot of the server in the cloud, because all initial settings are applied. In many cases, the boot volume type might be scaled back after the initial boot and should be tested.

**Note**  
The first boot of Windows machines on AWS might take up to 45 minutes because of Windows adjusting to the AWS virtual hardware.

## How long does it take to copy a disk from the AWS Transform MGN staging area to production?
<a name="How-Long-Copy-Disk-Staging"></a>

AWS Transform MGN uses internal cloud provider snapshots. This process typically takes less than a minute and the size of the volume does not impact the time.

## Which AWS services are automatically installed when launching a test or cutover instance?
<a name="Which-AWS-Services-Automatically-Installed-Target"></a>

AWS Transform MGN automatically installs EC2Config. After installation, EC2Config automatically installs the SSM EC2 Configuration Service.

CloudWatch, AWS PowerShell or CLI are not automatically installed. This can be done by combining the AWS Transform MGN APIs and the AWS APIs – you can use the AWS Transform MGN APIs to determine the EC2 instance IDs of the machines and then use AWS API/CLI to turn on the detailed monitoring. An alternative approach would be to do it by using the AWS API only based on the tags you associate with the machine. A third approach would be to do so from the post-launch script.

AWS Transform MGN installs EC2Launch (Windows 2016 only). You need to configure EC2Launch based on [these specific requirements](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2launch.html#ec2launch-config). This configuration step needs to be performed post Migration using the wizard in C:\\ProgramData\\Amazon\\EC2-Windows\\Launch\\Settings\\Ec2LaunchSettings.exe on the test or cutover instance.

## Why are my Windows server disks read-only after launching the test or cutover instance?
<a name="Why-Windows-Server-Disks-Read-Only"></a>

When launching test or cutover instances Windows Server may boot with all the disks as read-only.

This is a common issue that occurs when detaching and attaching data disks. This issue can be resolved using steps in [this Microsoft TechNet article](https://blogs.technet.microsoft.com/askcore/2011/06/02/my-disk-is-read-only-help/).

## How do I change the server AMI on AWS after Migration?
<a name="How-Change-Server-AMI"></a>

After AWS Transform MGN launches the machine, you can switch the AMI. Launch a new machine from the required AMI, stop that machine, detach all of its disks (including the root disk), and then attach the disks from the test or cutover instance that MGN created.

## Can I prevent AWS Transform MGN from cleaning up test instance resources in AWS?
<a name="Can-Prevent-Clean-Up-Target-Resources"></a>

By default, AWS Transform MGN removes any resources created during the test process either when requested by the user or when a new Test instance is launched.

To prevent this in AWS, you can [activate Termination Protection](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination) for the test or cutover instance, and the resources are not removed upon a new instance launch.

## Why do I observe EBS volume performance issues while using test or cutover instances?
<a name="EBS-performance-hit-after-instance-launch"></a>

**Note**  
This applies only when using Amazon EBS as the target storage type.

The EBS volumes attached to the test or cutover instances are created from snapshots of converted volumes. For any volume type that was created from snapshots, the storage blocks are pulled down from Amazon S3 and written to the volume before you access them. This process might take significant time and varies based on the EBS volume type. For additional details and EBS initialization options, refer to [Initialize Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-initialize.html)

## Which Amazon EBS attributes can I use to optimize EBS volume hydration when launching instances?
<a name="EBS-Volume-Hydration-Attributes"></a>

AWS Transform MGN supports the Amazon EBS Provisioned Rate for Volume Initialization (volume initialization rate). When launching an instance, it creates Amazon EBS volumes from snapshots, and this attribute downloads the snapshot blocks at a rate you specify (100 to 300 MiB/s), so volumes reach full performance in a predictable amount of time.

AWS Transform MGN does not support Amazon EBS fast snapshot restore (FSR), as it is not well suited to migration. FSR must be enabled in advance per snapshot and Availability Zone and is billed while enabled, which better suits steady-state workloads that repeatedly create volumes from the same snapshot and require full volume performance immediately at creation.

For more information, see [Initialize Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-initialize.html) and [Amazon EBS fast snapshot restore](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-fast-snapshot-restore.html) in the *Amazon EBS User Guide*.

## What are the Amazon EBS volume limits for AWS Transform MGN?
<a name="ebs-limits-faq"></a>

AWS Transform MGN does not impose its own limits on Amazon EBS volume size or the number of Amazon EBS volumes per instance. The limits for maximum volume size, number of volumes per instance, and other Amazon EBS constraints are governed by Amazon EBS itself. For current limits, see [Amazon EBS service quotas](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-resource-quotas.html) and [Instance volume limits](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/volume_limits.html).

## How is the AWS Licensing Model Tenancy chosen for AWS Transform MGN?
<a name="How-Licensing-Model-Tenancy"></a>

AWS Transform MGN conforms to the [Microsoft Licensing on AWS](https://aws.amazon.com/windows/resources/licensing/) guidelines. 