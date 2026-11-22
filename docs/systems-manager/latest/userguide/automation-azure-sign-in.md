

# Choosing Azure resources with Azure sign-in

Azure sign-in is an optional feature of the Automation console. It lets you pick Microsoft Azure resources from a list instead of typing their IDs. The console uses your sign-in only to list resources and doesn't change anything in Azure. It appears for a Cloud Connector target's **Subscriptions** (only when the connector covers the whole tenant) and **Resource groups**, and for the runbook's Azure resource inputs (such as virtual machines (VMs), scale sets, disks, SQL servers, SQL databases, storage accounts, key vaults, app services, AKS clusters, and container instances, but not blob containers or managed identities) after you choose a connector. It is shown only for an Azure connector whose tenant the console could read. Azure sign-in isn't available for Google Cloud.

**Note**  
Automation runs using the Cloud Connector, not your sign-in. Seeing a resource doesn't mean the connector can manage it.

## Choosing Azure resources with Azure sign-in
<a name="automation-azure-sign-in-procedure"></a>

**To choose Azure resources with Azure sign-in**

1. In the target or input fields, choose an Azure Cloud Connector.

1. Under **Azure sign-in**, choose **Sign in to Azure**.

1. Complete sign-in in the pop-up window. Use an account in the connector's Azure tenant. After you sign in, the console shows **Signed in to Azure as {{account}}**.

1. Turn on **Show interactive VM picker** (for VM inputs) or **Show interactive selector** (for other resources). The toggle is on by default after sign-in and shows the picker.

1. Select the resources you want. With **Parameter Values**, you can choose up to 50 VMs. Entries that the picker can't show stay under **Also included** or **Current value**.

## What the list shows
<a name="automation-azure-sign-in-list"></a>

The list shows the resources that your Azure account can read in the connector's scope. Your account needs read access to those resources, for example the Reader role. If you can't read some subscriptions, the console shows how many it left out, for example **You can't see 2 requested subscriptions. Showing the subscriptions you can access.**

## How your sign-in is used
<a name="automation-azure-sign-in-token"></a>

Your sign-in token stays in memory in the browser tab. It isn't saved, and it isn't sent to AWS. The console asks Azure for the `user_impersonation` scope of Azure Resource Manager (ARM), so the consent screen lists access as you. That scope allows what your own Azure roles allow. The console only reads with it: it lists subscriptions and queries Azure Resource Graph for resources. The session ends when the token expires (60 minutes at most) or when you reload the page. During sign-in and browsing, your browser connects to `login.microsoftonline.com` and `management.azure.com`.

## If you can't sign in
<a name="automation-azure-sign-in-troubleshoot"></a>
+ If your browser blocked the sign-in window, the console shows `Your browser blocked the sign-in window. Allow pop-ups for this site and try again, or enter the IDs yourself.` Allow pop-ups for the site and try again.
+ If sign-in doesn't complete, the console shows `Sign-in didn't finish. Try again, or enter the IDs yourself.` or `Sign-in was declined. Try again, or enter the IDs yourself.`
+ The first time, a tenant might ask an administrator to approve the application that Systems Manager uses for Azure sign-in. An administrator of the Microsoft Entra ID tenant grants consent once. You can also enter the IDs yourself instead of using Azure sign-in.