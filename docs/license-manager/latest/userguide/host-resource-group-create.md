# Create a host resource group in License Manager

Configure a host resource group to enable License Manager to manage your Dedicated Hosts. To best
utilize your most expensive licenses, you can associate one or more core- or socket-based
self-managed licenses with your host resource group. To best optimize host utilization, you
can allow all core- or socket-based self-managed licenses with your host resource group.

###### To create a host resource group

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the left navigation pane, choose **Host resource groups**.
3. Choose **Create host resource group**.
4. For **Host resource group details**, specify a name and description
   for the host resource group.
5. For **EC2 Dedicated Host management settings**, enable or disable the
   following settings as needed:
   - **Allocate hosts automatically**
   - **Release hosts automatically**
   - **Recover hosts automatically**

6. (Optional) For **Additional settings**, select the instance families
   that you can launch in the host resource group.
7. For **self-managed licenses**, select one or more core- or
   socket-based self-managed licenses.
8. (Optional) For **Tags**, add one or more tags.
9. Choose **Create**.
