# Viewing details about resources in Security Hub

The **Resources** page tracks common resources across your account and organization.
You can access the **Resources** page in the Security Hub console by choosing **Resources** in the navigation pane.
The benefit of the **Resources** page is that it helps you monitor your security posture, organize your resources, and review details about your resources.
When you choose a resource type, you can review all of the resources associated with the resource type.
You can review any findings associated with a resource.
The resource types available in the **Resources** page include any resources in your accounts covered by AWS security services contributing findings to Security Hub.

###### Note

The delegated administrator can view all resources associated with member accounts.
If you configured a home AWS Region, you can view all of your resources in your home AWS Region from linked AWS Regions.

If you choose a resource, you can review details for that resource.
These details include the resource name, ID, ARN, type, and category.
You can review the account ID associated with the resource, when the resource was created (timestamp), and where the resource was created (AWS Region).
You also can review additional configuration details about the resource.
These details can be found in a JSON snippet that you can copy.

If you switch from the **Overview** tab to the **Findings** tab, you can review any findings associated with the resource.
The **Findings** tab shows the name of each finding, type of each finding, and severity of each finding.
You can group findings by different fields and search for findings using filters.
If you choose a finding, you can review an overview of the finding, which includes information about compliance and how to remediate issues associated with the finding.
The **Traits** tab shows each trait that has been identified about the resource.
You can view contributing traits that were used to create an exposure finding for the resource.
You can also see contextual traits, which are other security items identified for the resource but did not directly contribute to any exposure findings.
If you go back to the resource, you can choose **Open resource** to review the resource in the console for its resource type.
For example, if the resource is an IAM resource, you can open the resource in the IAM console.

The resources page provides you with different ways to organize and search for resources.
You can group resources by type.
For example, you can group resources by account ID, finding type, AWS Region, resource category, resource name, and resource type.
Quick filters help you review resources by category, accounts, and finding types.
