• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Working with

runbooks for clusters

You can remediate issues with AWS resources from Application Manager, a tool in
AWS Systems Manager, by using Systems Manager Automation runbooks. When you choose **Start
runbook** from an Application Manager cluster, the system displays a filtered
list of runbooks based on the type of resources in your cluster. When you choose
the runbook you want to start, Systems Manager opens the **Execute automation
document** page.

###### Before you begin

Before you start a runbook from Application Manager, do the following:

- Verify that you have the correct permissions for starting runbooks.
  For more information, see [Setting up Automation](automation-setup.md "automation-setup.md").
- Review the Automation procedure documentation about starting runbooks.
  For more information, see [Run an automated operation powered by Systems Manager
  Automation](running-simple-automations.md "running-simple-automations.md").
- If you intend to start runbooks on multiple resources at one time,
  review the documentation about using targets and rate controls. For more
  information, see [Run automated operations at scale](running-automations-scale.md "running-automations-scale.md").

###### To start a runbook for clusters from Application Manager

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Application Manager**.
3. In the **Container clusters** section, choose a
   container type.
4. Choose the cluster in the list. Application Manager opens the
   **Overview** tab.
5. On the **Runbooks** tab, choose **Start
   runbook**. Application Manager opens the **Execute automation
   document** page in a new tab. For information about the
   options in the **Execute automation document** page,
   see [Run an automated operation powered by Systems Manager
   Automation](running-simple-automations.md "running-simple-automations.md").
