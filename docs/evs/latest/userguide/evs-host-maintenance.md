# Amazon EVS host maintenance

Because Amazon EVS is a self-managed service, you are responsible for maintenance of the VMware Cloud Foundation (VCF) software that runs on the host, monitoring host health, and remediating host issues, including host replacement in the event of host failure.
For more information about managing ESX hosts in VMware Cloud Foundation (VCF), see [Host Management](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin.html "https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin.html") in the VMware Cloud Foundation documentation.

## Checking health of the underlying EC2 instance

Amazon EC2 performs automated checks on every running EC2 instance to identify hardware and software issues.
You can view the results of these status checks in the EC2 console or AWS CLI to identify specific and detectable problems.
For more information, see [View status checks for Amazon EC2 instance](../../../AWSEC2/latest/UserGuide/viewing_status.md "../../../AWSEC2/latest/UserGuide/viewing_status.md") in the _Amazon EC2 User Guide_ and [describe-instance-status](../../../cli/latest/reference/ec2/describe-instance-status.md "../../../cli/latest/reference/ec2/describe-instance-status.md") in the _AWS CLI Command Line Reference_.

You can create a CloudWatch alarm to warn you if status checks fail on a specific instance.
For more information, see [Create CloudWatch alarms for Amazon EC2 instances that fail status checks](../../../AWSEC2/latest/UserGuide/creating_status_check_alarms.md "../../../AWSEC2/latest/UserGuide/creating_status_check_alarms.md") om tje _Amazon EC2 User Guide_.

## About AWS scheduled maintenance for EC2 instances

AWS performs scheduled maintenance on the underlying EC2 instances to ensure reliability, availability, and performance.
EC2 bare metal instances are subject to the same types of scheduled events as other EC2 instances.
AWS can schedule events to reboot, stop, and retire your instances due to underlying hardware issues or scheduled maintenance.
These events do not occur frequently.
For more information, see [Types of scheduled events](../../../AWSEC2/latest/UserGuide/monitoring-instances-status-check_sched.md#types-of-scheduled-events "../../../AWSEC2/latest/UserGuide/monitoring-instances-status-check_sched.md#types-of-scheduled-events") in the _Amazon EC2 User Guide_.

###### Note

You should place your hosts in maintenance mode in the vSphere Client before any scheduled reboot event.

If one of your instances will be affected by a scheduled event, AWS notifies you in advance by email, using the email address that’s associated with your AWS account.
AWS also sends an AWS Health event, which you can monitor and manage by using Amazon EventBridge.
For more information, see [Monitoring events in AWS Health with Amazon EventBridge](../../../health/latest/ug/cloudwatch-events-health.md "../../../health/latest/ug/cloudwatch-events-health.md") and [Scheduled events for Amazon EC2 instances](../../../AWSEC2/latest/UserGuide/monitoring-instances-status-check_sched.md "../../../AWSEC2/latest/UserGuide/monitoring-instances-status-check_sched.md") in the _Amazon EC2 User Guide_.

At any time, you can reschedule the event so that it occurs at a specific date and time that suits you.
The event can be rescheduled up to the event deadline date.
For more information, see [Reschedule a scheduled event for an EC2 instance](../../../AWSEC2/latest/UserGuide/reschedule-event.md "../../../AWSEC2/latest/UserGuide/reschedule-event.md") in the _Amazon EC2 User Guide_.

## Using EC2 On-Demand Capacity Reservations

You can use EC2 On-Demand Capacity Reservations to ensure that your cluster has sufficient capacity during maintenance periods.
You can reserve capacity in a specific Availabilty Zones for any duration.
For more information, see [Reserve compute capacity with EC2 On-Demand Capacity Reservations](../../../AWSEC2/latest/UserGuide/ec2-capacity-reservations.md "../../../AWSEC2/latest/UserGuide/ec2-capacity-reservations.md") in the _Amazon EC2 User Guide_.

For steps to create a Capacity Reservation, see [Create a Capacity Reservation](../../../AWSEC2/latest/UserGuide/capacity-reservations-create.md "../../../AWSEC2/latest/UserGuide/capacity-reservations-create.md") in the _Amazon EC2 User Guide_.

###### Note

If you use EC2 On-Demand Capacity Reservations or EC2 Dedicated Hosts, we recommend that you retain a spare host for mission-critical workloads.
While Capacity Reservations ensure you have access to a specific amount of EC2 instance capacity in a given Availability Zone, having a spare host provides an additional layer of redundancy that is crucial for mission-critical workloads.
For Dedicated Hosts, having a spare host ensures that you maintain the environment for mission-critical workloads, even if a primary host requires maintenance or experiences an issue.

## Preparing for AWS scheduled `system-maintenance` and `instance-retirement` events

AWS schedules two types of `system-maintenance` events: network maintenance and power maintenance.

- During network maintenance, scheduled instances lose network connectivity for a brief period of time.
  Normal network connectivity to your instance is restored after maintenance is complete.
- During power maintenance, scheduled instances are taken offline for a brief period, and then rebooted.
  When a reboot is performed on EC2 bare metal instances, instance store volume data is not preserved.

AWS schedules EC2 `instance-retirement` events when degradation of the underlying hardware hosting your EC2 instances is detected.

To remediate `system-maintenance` and `instance-retirement` events, replace the failed host with a new host using the Amazon EVS console or AWS CLI and SDDC Manager before the maintenance event occurs.
If you wait for the maintenance event to occur and an EC2 instance reboot is required, you will lose your vSAN data that is stored on the instance store volume.
For detailed steps, see [Replace an Amazon EVS host](#evs-replace-host "#evs-replace-host").

###### Important

The EC2 console should not be used to manage the state of your Amazon EVS hosts, including, stop, start, and termination.
Do not attempt to start, stop, or terminate the EC2 instances that Amazon EVS deploys.
This action results in vSAN data loss.

### Replace an Amazon EVS host

Follow this procedure to a replace an Amazon EVS host.

###### Warning

Amazon EVS hosts use a custom vendor add-on to provide important host functionality.
When you add a host to your environment, it will have the latest available version of the Amazon EVS custom add-on.
If your environment uses hosts with an older add-on version, adding host to your vSphere cluster will cause cluster image remediation to fail.
For steps to troubleshoot this issue, see [Troubleshoot add host failure due to incompatible cluster image](evs-env-ami-maintenance.md#troubleshoot-add-host-failure-cluster-image "evs-env-ami-maintenance.md#troubleshoot-add-host-failure-cluster-image").

###### Warning

If you have updated your ESX version post-deployment, SDDC manager may fail
during VCF host validation in the commission hosts step.
For steps to troubleshoot this issue, see [SDDC Manager fails VCF host validation during host commissioning](troubleshooting.md#troubleshoot-sddc-failure-host-commission "troubleshooting.md#troubleshoot-sddc-failure-host-commission").

###### Note

Ensure that your Amazon EVS host count per EVS environment quota is correctly set to ensure successfully host creation.
Host creation fails if this quota value is less than the number of hosts that you are attempting to provision within a single Amazon EVS environment.
You may need to request a quota increase for maintenance operations that require host replacement.
For more information, see [Amazon EVS service quotas](service-quotas-evs.md "service-quotas-evs.md").

Amazon EVS console and SDDC Managuer UI

1. Go to the [Amazon EVS console](https://console.aws.amazon.com/evs "https://console.aws.amazon.com/evs").
2. In the navigation pane, choose **Environment**.
3. Select the environment that contains the host to be replaced.
4. Select the **Hosts** tab.
5. Choose **Create host**.
6. Specify host details and choose **Create host**.
7. To verify completion, check that the **Host state** has changed to **Created**.
8. Retrieve the credentials for the ESX root password from AWS Secrets Manager.
   For more information about retrieving secrets, see [Get secrets from AWS Secrets Manager](../../../secretsmanager/latest/userguide/retrieving-secrets.md "../../../secretsmanager/latest/userguide/retrieving-secrets.md") in the _AWS Secrets Manager User Guide_.
9. Go to SDDC Manager.
10. Commission the new host in SDDC Manager, using the ESX root credentials that you retrieved in a previous step.
    For more information, see [Commission Hosts](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin/commission-hosts-admin.html "https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin/commission-hosts-admin.html") in the VMware Cloud Foundation documentation.
11. Add the new host to the cluster.
    For more information, see [How to Add an ESX
    Host to Your vSphere Cluster by Using the Quickstart Workflow](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/use-quickstart-to-add---host-to-a-cluster.html "https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/use-quickstart-to-add---host-to-a-cluster.html") in the vSphere documentation.
12. Decommission the old host in SDDC Manager that you want to remove from SDDC Manager.
    For more information, see [Decommission Hosts](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin/decommission-hosts-admin.html "https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin/decommission-hosts-admin.html") in the VMware Cloud Foundation documentation.
13. Return to the Amazon EVS console.
14. Under the **Hosts** tab, select the failed host and choose **Delete** > **Delete host**.

AWS CLI and SDDC Manager UI

1. Open a new terminal session.
2. Create a new host.
   See example command below for reference.

```
aws evs create-environment-host \
    --environment-id "env-abcde12345" \
    --host '{ \
        "hostName": "esxi-host-05", \
        "keyName": "your-ec2-keypair-name", \
        "instanceType": "i4i.metal" \
        "esxVersion": "ESXi-8.0U3g-24859861"\
    }'
```

3. Retrieve the credentials for the ESX root password from AWS Secrets Manager.
   For more information about retrieving secrets, see [Get secrets from AWS Secrets Manager](../../../secretsmanager/latest/userguide/retrieving-secrets.md "../../../secretsmanager/latest/userguide/retrieving-secrets.md") in the _AWS Secrets Manager User Guide_.
4. Go to SDDC Manager.
5. Commission the new host in SDDC Manager, using the ESX root credentials that you retrieved in a previous step.
   For more information, see [Commission Hosts](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin/commission-hosts-admin.html "https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin/commission-hosts-admin.html") in the VMware Cloud Foundation documentation.
6. Add the new host to the cluster that contains the impaired host.
7. Decommission the impaired host in SDDC Manager.
   For more information, see [Decommission Hosts](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin/decommission-hosts-admin.html "https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin/decommission-hosts-admin.html") in the VMware Cloud Foundation documentation.
8. Return to the terminal.
9. Delete the failed host.
   See example command below for reference.

```
aws evs delete-environment-host --environment-id "env-abcde12345" --host-name "esxi-host-05"
```

### Troubleshooting

For troubleshooting guidance, see [Troubleshooting](troubleshooting.md "troubleshooting.md").
If you continue to experience issues after reviewing the troubleshooting guidance, contact AWS Support for further assistance.
