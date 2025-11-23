# AWS related

## What does the Elastic Disaster Recovery

machine conversion server do?

The machine conversion server converts the disks to boot and run on AWS.

Specifically, it makes bootloader changes, injects hypervisor drivers, and
installs cloud tools.

## How do I change the server AMI on AWS after

recovery?

After the machine has been launched by AWS Elastic Disaster Recovery, switching the AMI can be
done by launching a vanilla machine from the required AMI, stopping that machine, detaching
all the disks (including the root) and then attaching the disks from the drill or recovery
instance created by Elastic Disaster Recovery.

## Which AWS services are

automatically installed when launching a drill or recovery instance?

AWS Elastic Disaster Recovery (AWS DRS) automatically installs EC2Config. After installation, EC2Config
automatically installs the SSM EC2 Configuration Service.

CloudWatch, AWS Powershell or CLI are not automatically installed. This can be done by
combining the AWS DRS APIs and the AWS APIs - you can use the AWS DRS APIs to determine the
EC2 instance IDs of the machines and then use AWS API/CLI to turn on the detailed monitoring.
An alternative approach would be to do it via AWS API only based on the tags you associate with the machine.
A third approach would be to do so from the post-launch script.

AWS DRS installs EC2Launch (Windows 2016 only). Customers need to
configure EC2Launch based on the specific requirements explained [here](../../../AWSEC2/latest/WindowsGuide/ec2launch.md#ec2launch-config "../../../AWSEC2/latest/WindowsGuide/ec2launch.md#ec2launch-config"). This configuration step needs to be performed post Recovery using the
wizard in C:\Program Data\Amazon\EC2-Windows\Launch\Settings\Ec2LaunchSettings.exe on the
drill or recovery instance.

## How long does it take to copy a disk

from the AWS Elastic Disaster Recovery staging area to production?

AWS Elastic Disaster Recovery uses internal cloud provider snapshots. This process typically
takes less than a minute and the size of the volume does not impact the time.

## What are

the differences between conversion servers and replication servers?

Replication servers run on Linux and conversion servers (for Windows machines) run
on Windows.

The conversion is done by AWS Elastic Disaster Recovery automatically bringing up a
vanilla Windows conversion server machines in the same subnet with the replication
servers as part of the launch job.

Both conversion and replication servers have Public IPs

The conversion servers will use the same security groups as the replication
server.

The conversion servers must be able to access the AWS Elastic Disaster Recovery
Service Manager.

The conversion servers machines, just like the Replication servers are managed
automatically by Elastic Disaster Recovery. Any attempt to disrupt their automated
functionality will result in failed conversions.

## Can I prevent Elastic Disaster Recovery

from cleaning up drill instance resources in AWS?

AWS Elastic Disaster Recovery will, by default, remove any resources created during the drill
process either when requested by the user or when a new drill instance is launched.

To prevent this in AWS, you can [Activate Termination Protection](../../../AWSEC2/latest/UserGuide/terminating-instances.md#Using_ChangingDisableAPITermination "../../../AWSEC2/latest/UserGuide/terminating-instances.md#Using_ChangingDisableAPITermination") for the drill or recovery instance, and the
resources will not be removed upon a new instance launch.

## Why are my Windows Server disks read-only

after launching the drill or recovery instance?

When launching drill or recovery instances Windows Server may boot with all the disks as
read-only.

This is a common issue that occurs when detaching and attaching data disks. It can be
resolved by following the steps in [this
Microsoft TechNet article](https://blogs.technet.microsoft.com/askcore/2011/06/02/my-disk-is-read-only-help/ "https://blogs.technet.microsoft.com/askcore/2011/06/02/my-disk-is-read-only-help/").

## What impacts the conversion and boot

time of drill and recovery instances?

Prior to launching the drill or recovery instance, AWS Elastic Disaster Recovery goes
through a machine conversion server process on the boot volume. The conversion
process is fairly quick.

While the actual conversion process itself is quick, the time to boot the drill or recovery
instance varies depending on many factors unrelated to any Elastic Disaster Recovery
processes. Some of these are controllable and should be taken into account when drill or
recovery times are of importance.

- Operating system - The amount of time required to boot the operating
  system is dependent on the OS itself. While Linux servers typically boot
  quickly, Windows servers may take additional time, due to the nature of the
  Windows OS. If opportunity permits, drill the boot time of the source
  server. If Linux OS takes a long time to boot ensure to check that dhclient
  (Dynamic Host Configuration Protocol Client) is installed and the system so
  it can pull an IP.
- Scheduled Windows Updates - If the Windows server has pending patches, ensure those are
  installed prior to launching the drill or recovery instance. If pending patches remain,
  the boot time in the cloud may be severely impacted as the patch process may commence
  upon the initial boot.
- Boot volume type - Depending on services/applications, boot time may be impacted by disk
  performance. It is recommended that boot volumes be drilled with a higher performance
  SSD and even by provisioning IOPs to ensure throughput. This may be more critical during
  the first initial boot of the server in the cloud, as all initial settings are applied.
  In many cases, the boot volume type may be scaled back after the initial boot and should
  be drilled.

###### Note

The first boot of Windows machines on AWS may take up to 45 minutes due to Windows
adjusting to the AWS virtual hardware.

## How is the AWS Licensing Model Tenancy chosen for

Elastic Disaster Recovery?

Elastic Disaster Recovery conforms to the [Microsoft Licensing on
AWS](https://aws.amazon.com/windows/resources/licensing/ "https://aws.amazon.com/windows/resources/licensing/") guidelines.

## How does Elastic Disaster Recovery interact with interface VPC

endpoints?

If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you
can establish a private connection between your Amazon VPC and AWS Elastic Disaster Recovery.
You can use this connection to allow AWS Elastic Disaster Recovery to communicate with
your resources on your VPC without going through the public internet.

Amazon VPC is an AWS service that you can use to launch AWS resources in a virtual
network that you define. With a VPC, you have control over your network settings, such the
IP address range, subnets, route tables, and network gateways. With VPC endpoints, the
routing between the Amazon VPC and AWS services is handled by the AWS network, and you can use IAM
policies to control access to service resources.

To connect your VPC to Elastic Disaster Recovery, you define an _interface VPC endpoint_ for Elastic Disaster Recovery. An interface endpoint is
an elastic network interface with a private IP address that serves as an entry point for
traffic destined to a supported AWS service. The endpoint provides reliable, scalable
connectivity to Elastic Disaster Recovery without requiring an internet gateway, network
address translation (NAT) instance, or VPN connection. For more information, see [What is Amazon VPC](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md") in the
_Amazon VPC User Guide_.

Interface VPC endpoints are powered by AWS PrivateLink, an AWS technology that facilitates
private communication between AWS services using an elastic network interface with private
IP addresses. For more information, see [AWS
PrivateLink](https://aws.amazon.com/privatelink/ "https://aws.amazon.com/privatelink/").

For more information, see [Getting
Started](../../../vpc/latest/userguide/GetStarted.md "../../../vpc/latest/userguide/GetStarted.md") in the _Amazon VPC User Guide_.

If the AWS replication agents are installed with a principal using
[AWSElasticDisasterRecoveryAgentInstallationPolicy](security-iam-awsmanpol-AWSElasticDisasterRecoveryAgentInstallationPolicy.md#security-iam-awsmanpol-AWSElasticDisasterRecoveryAgentInstallationPolicy.title "security-iam-awsmanpol-AWSElasticDisasterRecoveryAgentInstallationPolicy.md#security-iam-awsmanpol-AWSElasticDisasterRecoveryAgentInstallationPolicy.title") and a VPCE policy is used (to scope down access), add the following statement to your policy:

```
`{
 "Effect": "Allow",
 "Principal": "*",
 "Action": "execute-api:Invoke",
 "Resource": "arn:aws:execute-api:<region>:*.*/POST/CreateSessionForDrs"
 }`
```

## Will AWS Elastic Disaster Recovery reserve EC2 capacity for

recovery?

AWS Elastic Disaster Recovery relies on Amazon EC2 On-Demand pools by default. If a specific Amazon EC2 instance type is
unavailable to support your recovery, DRS will automatically attempt scale up the
instance repeatedly until an available instance type is found, but in extreme
circumstances, instances may not always be available. To ensure the availability of
the required instance types you need for your most critical applications, you may
purchase [EC2
Capacity Reservations](../../../AWSEC2/latest/UserGuide/ec2-capacity-reservations.md "../../../AWSEC2/latest/UserGuide/ec2-capacity-reservations.md"). You can specifically designate which applications
you want to use the EC2 Capacity Reservations for by using launch templates.
