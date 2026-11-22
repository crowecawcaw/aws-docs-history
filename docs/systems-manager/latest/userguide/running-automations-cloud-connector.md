

# Run automations on multicloud resources

With AWS Systems Manager Automation, you can run a runbook on Microsoft Azure and Google Cloud resources through a Systems Manager Cloud Connector. The connector and its federation role are the identity that Automation uses to reach your resources, so Automation doesn't need any Azure or Google Cloud credentials from you.

You can run an automation on the resources that a Cloud Connector reaches in the following ways.

Rate control with a Cloud Connector target  
You choose a Cloud Connector and optional filters. Automation finds the resources that match and runs the runbook once for each one. By default, the target finds the running virtual machines (VMs) in every subscription or project that the connector covers. Use this method to run a runbook on many VMs.

Rate control with **Parameter Values**  
You enter the IDs of up to 50 VMs. For more than 50 VMs, use a Cloud Connector target.

Simple execution or Manual execution  
For a runbook that has a Cloud Connector input, you choose the connector and enter the IDs of the resources in the runbook's inputs. The automation runs once, on those resources.

Multi-account and Region  
This execution mode supports AWS targets only. For more information, see [Running automations in multiple AWS Regions and accounts](running-automations-multiple-accounts-regions.md).

Before you run an automation through a Cloud Connector, complete the following prerequisites.
+ Create a Cloud Connector. For Azure, see [Set up a Cloud Connector for Microsoft Azure in Systems Manager](systems-manager-cloud-connector.md). For Google Cloud, see [Set up a Cloud Connector for Google Cloud Platform in Systems Manager](systems-manager-cloud-connector-gcp.md).
+ Make sure that your AWS account has an automation assume role for the connector. Systems Manager creates this role when you enable node management for the connector and keep the default **Automation execution role**. If you didn't, create the role as described in [Create the automation assume role](automation-cloud-connector-permissions.md#automation-cloud-connector-permissions-create-role). You can also use a role that you chose under **Additional trusted roles** when you created the connector. For more information, see [Use another role](automation-cloud-connector-permissions.md#automation-cloud-connector-permissions-other-role).
+ Use a runbook that has an input for the resource ID. With a Cloud Connector target, Automation passes each resource's ID in that input. To check a runbook, open it on the **Documents** page of the Systems Manager console, choose the **Content** tab, and look in `parameters` for one of the following inputs:
  + An input whose type is a resource type, such as `microsoft.Compute/VirtualMachines` or `compute.googleapis.com/Instance`. For the types, see [Parameter types for Azure and Google Cloud resources](automation-multicloud-parameter-types.md).
  + A `String` input whose `allowedPattern` accepts the resource IDs. Automation passes Azure resource IDs in lowercase, so the pattern must accept lowercase letters.

  On the **Execute automation** page, the **Parameter** list shows the inputs that match.
+ To filter resources by managed node status, make sure that SSM Agent is installed on the VMs.

**Note**  
A Cloud Connector belongs to the AWS Region where you create it. Start the automation in that Region. For example, to use a connector that you created in the US East (N. Virginia) Region, start the automation in US East (N. Virginia). In another Region, Automation can't read the connector. For that error, see [An error occurred reading the provided CloudConnector](automation-cloud-connector-troubleshooting.md#automation-cloud-connector-troubleshooting-reading). You can use a Cloud Connector target in every AWS Region where you can create a Cloud Connector.

**Where to see results**

Automation runs the runbook for each resource in a separate automation, called a child automation. The automation that you start has one step for each resource, and the step's execution ID is the ID of that resource's child automation. To see the child automations, choose **Show child automations** on the **Automation** page of the Systems Manager console. For more information, see the console and command line procedures that follow.

**Topics**
+ [Run an automation on Azure or Google Cloud resources (console)](running-automations-cloud-connector-console.md)
+ [Run an automation on Azure or Google Cloud resources (command line)](running-automations-cloud-connector-cli.md)
+ [Cloud Connector target reference](automation-cloud-connector-target.md)
+ [Permissions for automations that use a Cloud Connector](automation-cloud-connector-permissions.md)
+ [Choosing Azure resources with Azure sign-in](automation-azure-sign-in.md)
+ [Troubleshooting automations that use a Cloud Connector](automation-cloud-connector-troubleshooting.md)