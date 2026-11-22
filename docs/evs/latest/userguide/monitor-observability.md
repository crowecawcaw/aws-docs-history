

# Monitor hosts and VCF

You monitor an Amazon Elastic VMware Service environment at two layers. Amazon CloudWatch and the EC2 status checks report on the EC2 instances that run your hosts. VMware Cloud Foundation (VCF) tools, such as VCF Operations, report on VCF components and workloads. You’re responsible for monitoring host health in both deployment modes, so we recommend that you set up both layers.

## What each tool monitors
<a name="monitor-observability-compare"></a>

The following table shows what you monitor, the tool that reports it, and where to read more.


| What you monitor | Tool | More information | 
| --- | --- | --- | 
| Hardware and software problems of the EC2 instance that runs a host | EC2 status checks |  [Monitor host instances with EC2 status checks and CloudWatch](#monitor-observability-ec2)  | 
| Alarms when a status check fails on a host | Amazon CloudWatch |  [Monitor host instances with EC2 status checks and CloudWatch](#monitor-observability-ec2)  | 
| Usage of Amazon EVS resources that have quotas (environments and hosts) | Amazon CloudWatch |  [Service quotas for Amazon EVS](service-quotas-evs.md)  | 
| Scheduled maintenance and retirement of host instances |  AWS Health |  [Get notified about host events](monitor-notifications.md)  | 
| Amazon EVS environment status and connector health | Amazon EVS console or AWS CLI  |  [Monitor environment status](evs-env-status-check.md)  | 
| VCF components, such as vCenter Server, NSX, and vSAN, and the workloads that run on them | VCF Operations and the VCF management tools |  [Monitor VCF components and workloads with VCF tools](#monitor-observability-vcf)  | 
| User activity inside VCF, such as changes in vSphere or NSX Manager | VCF logs and VCF Operations |  [Log API calls with CloudTrail](logging-using-cloudtrail.md)  | 

## Monitor host instances with EC2 status checks and CloudWatch
<a name="monitor-observability-ec2"></a>

Amazon EC2 runs automated checks on every running EC2 instance to identify hardware and software issues. You can view the results of these status checks in the EC2 console or with the AWS CLI to identify specific and detectable problems. For more information, see [View status checks for Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_status.html) in the *Amazon EC2 User Guide* and [describe-instance-status](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-status.html) in the * AWS CLI Command Reference*.

To find the EC2 instance of a host, run `aws evs list-environment-hosts` and read the `ec2InstanceId` value of the host.

You can create a CloudWatch alarm that warns you when status checks fail on a specific instance. For more information, see [Create CloudWatch alarms for Amazon EC2 instances that fail status checks](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating_status_check_alarms.html) in the *Amazon EC2 User Guide*.

**Important**  
Use the alarm only to notify you, and don’t add an alarm action that stops, reboots, terminates, or recovers the instance.

Don’t use the Amazon EC2 console to stop, start, or terminate Amazon EVS hosts. On hosts with local storage, these actions cause the loss of the vSAN data on the instance store volumes. For why EC2 automatic recovery doesn’t apply to Amazon EVS hosts, see [Why EC2 automatic recovery doesn’t apply](evs-host-maintenance.md#evs-host-auto-recovery).

Amazon CloudWatch also collects AWS usage metrics for Amazon EVS resources that have quotas. For more information, see [CloudWatch usage metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Usage-Metrics.html) in the *Amazon CloudWatch User Guide*.

## Monitor VCF components and workloads with VCF tools
<a name="monitor-observability-vcf"></a>

Amazon EVS doesn’t monitor the VCF components inside your environment. You can keep using the VCF management and monitoring tools that you already use, such as VCF Operations, for monitoring and for centralized VCF logging.

The VCF tools that you use differ by deployment mode.
+ In Self-deployed environments that run VCF 9.x, VCF Operations is a separate appliance that you deploy with VCF. For more information, see the [Broadcom documentation for VCF](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1.html).
+ In EVS-deployed environments (VCF 5.2.x), you monitor VCF components in SDDC Manager. For more information, see [Getting started with SDDC Manager](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/getting-started-with-sddc-manager-admin.html) in the Broadcom documentation.

On diskless hosts (VCF 9.x only), your datastores are on external storage, such as Amazon FSx. You monitor the capacity and health of that storage with the tools of the storage service. For more information, see [External storage options for diskless hosts](external-storage-diskless.md). For the VCF versions and instance types that each mode supports, see [Supported VCF versions and instance types](versions-provided.md).

## Where to get help
<a name="monitor-observability-support"></a>

For problems with the Amazon EVS service, the EC2 instances, or the AWS network, contact AWS Support. For VCF configuration guidance, you can also use the Broadcom documentation and your Broadcom support entitlement. For who to contact for which problem, see [Get help from AWS Support and Broadcom](get-help.md).