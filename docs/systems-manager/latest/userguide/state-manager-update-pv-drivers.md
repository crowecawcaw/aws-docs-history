AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Walkthrough: Automatically update PV

drivers on EC2 instances for Windows Server

Amazon Windows Server Amazon Machine Images (AMIs) contain a set of drivers to permit access to
virtualized hardware. These drivers are used by Amazon Elastic Compute Cloud (Amazon EC2) to map instance store
and Amazon Elastic Block Store (Amazon EBS) volumes to their devices. We recommend that you install the latest
drivers to improve stability and performance of your EC2 instances for Windows Server. For
more information about PV drivers, see [AWS PV
Drivers](../../../AWSEC2/latest/WindowsGuide/xen-drivers-overview.md#xen-driver-awspv "../../../AWSEC2/latest/WindowsGuide/xen-drivers-overview.md#xen-driver-awspv").

The following walkthrough shows you how to configure a State Manager association to
automatically download and install new AWS PV drivers when the drivers become
available. State Manager is a tool in AWS Systems Manager.

###### Before you begin

Before you complete the following procedure, verify that you have at least one
Amazon EC2 instance for Windows Server running that is configured for Systems Manager. For more
information, see [Setting up managed nodes for
AWS Systems Manager](systems-manager-setting-up-nodes.md "systems-manager-setting-up-nodes.md").

###### To create a State Manager association that automatically updates PV drivers

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **State Manager**.
3. Choose **Create association**.
4. In the **Name** field, enter a descriptive name for the
   association.
5. In the **Document** list, choose
   `AWS-ConfigureAWSPackage`.
6. In the **Parameters** area, do the following:
   - For **Action**, choose
     **Install**.
   - For **Installation type**, choose **Uninstall
     and reinstall**.

   ###### Note

   In-place upgrades are not supported for this package. It must be
   uninstalled and reinstalled.
   - For **Name**, enter
     `AWSPVDriver`.

   You don't need to enter anything for **Version** and
   **Additional Arguments**.

7. In the **Targets** section, choose the managed nodes on which you want to
   run this operation by specifying tags, selecting instances or edge devices manually, or
   specifying a resource group.

###### Tip

If a managed node you expect to see isn't listed, see [Troubleshooting managed
node availability](fleet-manager-troubleshooting-managed-nodes.md "fleet-manager-troubleshooting-managed-nodes.md") for troubleshooting
tips.

###### Note

If you choose to target instances by using tags, and you specify tags that
map to Linux instances, the association succeeds on the Windows Server instance
but fails on the Linux instances. The overall status of the association
shows **Failed**. 8. In the **Specify schedule** area, choose whether to run the
association on a schedule that you configure, or just once. Updated PV drivers
are released a several times a year, so you can schedule the association to run
once a month, if you want. 9. In the **Advanced options** area, for **Compliance
severity**, choose a severity level for the association. Compliance
reporting indicates whether the association state is compliant or noncompliant,
along with the severity level you indicate here. For more information, see [About State Manager association
compliance](compliance-about.md#compliance-about-association "compliance-about.md#compliance-about-association"). 10. For **Rate control**:

    * For **Concurrency**, specify either a number or a percentage of
     managed nodes on which to run the command at the same time.


    ###### Note

    If you selected targets by specifying tags applied to managed nodes or by
     specifying AWS resource groups, and you aren't certain how many managed
     nodes are targeted, then restrict the number of targets that can run the
     document at the same time by specifying a percentage.
    * For **Error threshold**, specify when to stop running the command
     on other managed nodes after it fails on either a number or a percentage of nodes.
     For example, if you specify three errors, then Systems Manager stops sending the command when
     the fourth error is received. Managed nodes still processing the command might also
     send errors.

11. (Optional) For **Output options**, to save the command output to a file,
    select the **Enable writing output to S3** box. Enter the bucket and prefix
    (folder) names in the boxes.

###### Note

The S3 permissions that grant the ability to write the data to an S3 bucket are those
of the instance profile assigned to the managed node, not those of the IAM user
performing this task. For more information, see [Configure instance permissions required for Systems Manager](setup-instance-permissions.md "setup-instance-permissions.md")
or [Create an IAM service role for a
hybrid environment](hybrid-multicloud-service-role.md "hybrid-multicloud-service-role.md"). In addition, if the specified S3 bucket is in a different
AWS account, verify that the instance profile or IAM service role associated with
the managed node has the necessary permissions to write to that bucket. 12. (Optional) In the **CloudWatch alarm** section, for **Alarm
name**, choose a CloudWatch alarm to apply to your association for
monitoring.

###### Note

Note the following information about this step.

    * The alarms list displays a maximum of 100 alarms. If you don't see
     your alarm in the list, use the AWS Command Line Interface to create the association.
     For more information, see [Create an
     association (command line)](state-manager-associations-creating.md#create-state-manager-association-commandline "state-manager-associations-creating.md#create-state-manager-association-commandline").
    * To attach a CloudWatch alarm to your command, the IAM principal that
     creates the association must have permission for the
     `iam:createServiceLinkedRole` action. For more
     information about CloudWatch alarms, see [Using Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md").
    * If your alarm activates, any pending command invocations or
     automations do not run.

13. Choose **Create association**, and then choose
    **Close**. The system attempts to create the association on
    the instances and immediately apply the state.

If you created the association on one or more Amazon EC2 instances for Windows Server,
the status changes to **Success**. If your instances aren't
configured for Systems Manager, or if you inadvertently targeted Linux instances, the
status shows **Failed**.

If the status is **Failed**, choose the association ID,
choose the **Resources** tab, and then verify that the
association was successfully created on your EC2 instances for Windows Server. If EC2
instances for Windows Server show a status of **Failed**, verify that
the SSM Agent is running on the instance, and verify that the instance is
configured with an AWS Identity and Access Management (IAM) role for Systems Manager. For more information, see
[Setting up Systems Manager unified console
for an organization](systems-manager-setting-up-organizations.md "systems-manager-setting-up-organizations.md").
