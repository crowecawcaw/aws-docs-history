# Managing your access to Amazon Managed Grafana

Enterprise plugins

###### To manage your access to Enterprise plugins

1. Open the Amazon Managed Grafana console at
   [https://console.aws.amazon.com/grafana](https://console.aws.amazon.com/grafana "https://console.aws.amazon.com/grafana").
2. In the left navigation pane, choose the menu icon.
3. Choose **All workspaces**.

You can see the list of workspaces. For each workspace, the
**Enterprise license** columns shows the type of
license the workspace has (either no license, or the **Enterprise
plugins** license. 4. Select the name of the workspace whose license you want to manage. This
opens the workspace details page for that workspace. 5. In the summary, under **Enterprise License**, choose
either **Manage** or **Upgrade to Amazon Managed Grafana
Enterprise** (only one option is available, based on
the current status of the Enterprise license).

This opens the **Manage Amazon Managed Grafana Enterprise** page. You
can choose between two options. The active option is marked with
**(current)**.

    * **None** – This is the
     option to remove, or not have an Amazon Managed Grafana Enterprise license. If
     you currently have an Enterprise license, selecting this option
     for your workspace immediately removes access to the Enterprise
     plugins when you save.
    * **Enterprise plugins**
     – This allows you to install any Enterprise plugins to
     your workspace, as well as giving access to [Grafana Labs](https://grafana.com "https://grafana.com") consulting
     and support services. Installing Enterprise plugins in your
     workspace gives you access to additional [data sources](AMG-data-sources-enterprise.md "AMG-data-sources-enterprise.md").


    The first time that you choose this option, you must link
     your AWS account with a token from Grafana Labs, and are prompted
     to do so. For more information, see the next section, [Link your account with
     Grafana Labs](AMG-workspace-register-enterprise.md "AMG-workspace-register-enterprise.md").


    Amazon Managed Grafana Enterprise plugin access includes user fees that are in
     addition to the prices for Amazon Managed Grafana. For detailed fee
     information, see the [Amazon Managed Grafana Pricing page](https://aws.amazon.com/grafana/pricing/ "https://aws.amazon.com/grafana/pricing/").

6. After making your selection, choose **Save** to continue.
