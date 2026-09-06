

# Amazon EVS host maintenance
<a name="evs-host-maintenance"></a>

Because Amazon EVS is a self-managed service, you are responsible for maintenance of the VMware Cloud Foundation (VCF) software that runs on the host, monitoring host health, and remediating host issues, including host replacement in the event of host failure. For more information about managing ESX hosts in VMware Cloud Foundation (VCF), see [Host Management](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin.html) in the VMware Cloud Foundation documentation.

## Checking health of the underlying EC2 instance
<a name="evs-host-ec2-instance-health"></a>

Amazon EC2 performs automated checks on every running EC2 instance to identify hardware and software issues. You can view the results of these status checks in the EC2 console or AWS CLI to identify specific and detectable problems. For more information, see [View status checks for Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_status.html) in the *Amazon EC2 User Guide* and [describe-instance-status](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-status.html) in the * AWS CLI Command Line Reference*.

You can create a CloudWatch alarm to warn you if status checks fail on a specific instance. For more information, see [Create CloudWatch alarms for Amazon EC2 instances that fail status checks](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating_status_check_alarms.html) om tje *Amazon EC2 User Guide*.

## About AWS scheduled maintenance for EC2 instances
<a name="evs-host-maintenance-about"></a>

 AWS performs scheduled maintenance on the underlying EC2 instances to ensure reliability, availability, and performance. EC2 bare metal instances are subject to the same types of scheduled events as other EC2 instances. AWS can schedule events to reboot, stop, and retire your instances due to underlying hardware issues or scheduled maintenance. These events do not occur frequently. For more information, see [Types of scheduled events](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-instances-status-check_sched.html#types-of-scheduled-events) in the *Amazon EC2 User Guide*.

**Note**  
You should place your hosts in maintenance mode in the vSphere Client before any scheduled reboot event.

If one of your instances will be affected by a scheduled event, AWS notifies you in advance by email, using the email address that’s associated with your AWS account. AWS also sends an AWS Health event, which you can monitor and manage by using Amazon EventBridge. For more information, see [Monitoring events in AWS Health with Amazon EventBridge](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html) and [Scheduled events for Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-instances-status-check_sched.html) in the *Amazon EC2 User Guide*.

At any time, you can reschedule the event so that it occurs at a specific date and time that suits you. The event can be rescheduled up to the event deadline date. For more information, see [Reschedule a scheduled event for an EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/reschedule-event.html) in the *Amazon EC2 User Guide*.

## Using EC2 On-Demand Capacity Reservations
<a name="evs-host-maintenance-odcr"></a>

You can use EC2 On-Demand Capacity Reservations to ensure that your cluster has sufficient capacity during maintenance periods. You can reserve capacity in a specific Availabilty Zones for any duration. For more information, see [Reserve compute capacity with EC2 On-Demand Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html) in the *Amazon EC2 User Guide*.

For steps to create a Capacity Reservation, see [Create a Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-create.html) in the *Amazon EC2 User Guide*.

**Note**  
If you use EC2 On-Demand Capacity Reservations or EC2 Dedicated Hosts, we recommend that you retain a spare host for mission-critical workloads. While Capacity Reservations ensure you have access to a specific amount of EC2 instance capacity in a given Availability Zone, having a spare host provides an additional layer of redundancy that is crucial for mission-critical workloads. For Dedicated Hosts, having a spare host ensures that you maintain the environment for mission-critical workloads, even if a primary host requires maintenance or experiences an issue.

## Preparing for AWS scheduled `system-maintenance` and `instance-retirement` events
<a name="evs-host-preparing-aws-scheduled-maintenance"></a>

 AWS schedules two types of `system-maintenance` events: network maintenance and power maintenance.
+ During network maintenance, scheduled instances lose network connectivity for a brief period of time. Normal network connectivity to your instance is restored after maintenance is complete.
+ During power maintenance, scheduled instances are taken offline for a brief period, and then rebooted. When a reboot is performed on EC2 bare metal instances, instance store volume data is not preserved.

 AWS schedules EC2 `instance-retirement` events when degradation of the underlying hardware hosting your EC2 instances is detected.

To remediate `system-maintenance` and `instance-retirement` events, replace the failed host with a new host using the Amazon EVS console or AWS CLI and SDDC Manager before the maintenance event occurs. If you wait for the maintenance event to occur and an EC2 instance reboot is required, you will lose your vSAN data that is stored on the instance store volume. For detailed steps, see [Replace an Amazon EVS host](#evs-replace-host).

**Important**  
The EC2 console should not be used to manage the state of your Amazon EVS hosts, including, stop, start, and termination. Do not attempt to start, stop, or terminate the EC2 instances that Amazon EVS deploys. This action results in vSAN data loss.

### Replace an Amazon EVS host
<a name="evs-replace-host"></a>

Follow this procedure to a replace an Amazon EVS host.

**Warning**  
Amazon EVS hosts use a custom vendor add-on to provide important host functionality. When you add a host to your environment, it will have the latest available version of the Amazon EVS custom add-on. If your environment uses hosts with an older add-on version, adding host to your vSphere cluster will cause cluster image remediation to fail. For steps to troubleshoot this issue, see [Troubleshoot add host failure due to incompatible cluster image](evs-env-ami-maintenance.md#troubleshoot-add-host-failure-cluster-image).

**Warning**  
If you have updated your ESX version post-deployment, SDDC manager may fail during VCF host validation in the commission hosts step. For steps to troubleshoot this issue, see [SDDC Manager fails VCF host validation during host commissioning](troubleshooting.md#troubleshoot-sddc-failure-host-commission).

**Note**  
Ensure that your Amazon EVS host count per EVS environment quota is correctly set to ensure successfully host creation. Host creation fails if this quota value is less than the number of hosts that you are attempting to provision within a single Amazon EVS environment. You may need to request a quota increase for maintenance operations that require host replacement. For more information, see [Amazon EVS service quotas](service-quotas-evs.md).

**Example**  

1. Go to the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environment**.

1. Select the environment that contains the host to be replaced.

1. Select the **Hosts** tab.

1. Choose **Create host**.

1. Specify host details and choose **Create host**.

1. To verify completion, check that the **Host state** has changed to **Created**.

1. Retrieve the credentials for the ESX root password from AWS Secrets Manager. For more information about retrieving secrets, see [Get secrets from AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets.html) in the * AWS Secrets Manager User Guide*.

1. Go to SDDC Manager.

1. Commission the new host in SDDC Manager, using the ESX root credentials that you retrieved in a previous step. For more information, see [Commission Hosts](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin/commission-hosts-admin.html) in the VMware Cloud Foundation documentation.

1. Add the new host to the cluster. For more information, see [How to Add an ESX Host to Your vSphere Cluster by Using the Quickstart Workflow](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/use-quickstart-to-add---host-to-a-cluster.html) in the vSphere documentation.

1. Decommission the old host in SDDC Manager that you want to remove from SDDC Manager. For more information, see [Decommission Hosts](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin/decommission-hosts-admin.html) in the VMware Cloud Foundation documentation.

1. Return to the Amazon EVS console.

1. Under the **Hosts** tab, select the failed host and choose **Delete** > **Delete host**.

1. Open a new terminal session.

1. Create a new host. See example command below for reference.

   ```
   aws evs create-environment-host \
       --environment-id "env-abcde12345" \
       --esx-version "ESXi-8.0U3g-24859861" \
       --host '{ \
           "hostName": "esxi-host-05", \
           "keyName": "your-ec2-keypair-name", \
           "instanceType": "i4i.metal" \
       }'
   ```

1. Retrieve the credentials for the ESX root password from AWS Secrets Manager. For more information about retrieving secrets, see [Get secrets from AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets.html) in the * AWS Secrets Manager User Guide*.

1. Go to SDDC Manager.

1. Commission the new host in SDDC Manager, using the ESX root credentials that you retrieved in a previous step. For more information, see [Commission Hosts](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin/commission-hosts-admin.html) in the VMware Cloud Foundation documentation.

1. Add the new host to the cluster that contains the impaired host.

1. Decommission the impaired host in SDDC Manager. For more information, see [Decommission Hosts](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin/decommission-hosts-admin.html) in the VMware Cloud Foundation documentation.

1. Return to the terminal.

1. Delete the failed host. See example command below for reference.

   ```
   aws evs delete-environment-host --environment-id "env-abcde12345" --host-name "esxi-host-05"
   ```

### Troubleshooting
<a name="evs-maintenance-troubleshooting"></a>

#### Broadcom and AWS Support guidance
<a name="broadcom_and_shared_aws_support_guidance"></a>

 AWS provides support for Amazon EVS and its associated infrastructure services, including VMware Cloud Foundation (VCF). For VCF-specific configuration guidance, or issues related to other VMware products such as Aria Suite, HCX, or NSX, you can also contact Broadcom directly using your Broadcom support entitlement. For more information, see [Broadcom Support Portal](https://support.broadcom.com/).

For troubleshooting guidance, see [Troubleshooting](troubleshooting.md). If you continue to experience issues after reviewing the troubleshooting guidance, contact AWS Support for further assistance.