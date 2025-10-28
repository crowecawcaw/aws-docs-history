# Use Automation runbooks to

remediate application issues

You can remediate issues with AWS resources from Application Manager, a tool in AWS Systems Manager,
by using Automation runbooks. An Automation runbook defines the actions that Systems Manager
performs on your managed instances and other AWS resources when an automation
runs. Automation is a tool in AWS Systems Manager. A runbook contains one or more steps that
run in sequential order. Each step is built around a single action. Output from one
step can be used as input in a later step.

When you choose **Start runbook** from an Application Manager application
or cluster, the system displays a filtered list of available runbooks based on the
type of resources in your application or cluster. When you choose the runbook you
want to start, Systems Manager opens the **Execute automation document**
page.

Application Manager includes the following enhancements for working with runbooks.

- If you choose the name of a resource in Application Manager and then choose
  **Execute runbook**, the system displays a filtered
  list of runbooks for that resource type.
- You can initiate an automation on all resources of the same type by
  choosing a runbook in the list and then choosing **Run for resources
  of same type**.

###### Before you begin

Before you start a runbook from Application Manager, do the following:

- Verify that you have the correct permissions for starting runbooks. For
  more information, see [Setting up Automation](automation-setup.md "automation-setup.md").
- Review the Automation procedure documentation about starting runbooks. For
  more information, see [Run an automated operation powered by Systems Manager
  Automation](running-simple-automations.md "running-simple-automations.md").

###### To start a runbook from Application Manager

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Application Manager**.
3. In the **Applications** section, choose a category. If
   you want to open an application you created manually in Application Manager, choose
   **Custom applications**.
4. Choose the application in the list. Application Manager opens the
   **Overview** tab.
5. Choose **Start runbook**. Application Manager opens the
   **Automation widget** pop up. For information about the
   options in the **Automation widget**, see [Run an automated operation powered by Systems Manager
   Automation](running-simple-automations.md "running-simple-automations.md").
