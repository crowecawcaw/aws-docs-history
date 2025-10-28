# Remove Dedicated Hosts from a host resource group in License Manager

When you remove a host from the host resource group, the instance running on the host remains on the
host. The instances attached to the host resource group remain associated with the group, and instances
directly attached to the host through affinity maintain the same property. If you share the
host resource group with other AWS accounts, License Manager automatically removes the shared host and consumers
receive an eviction notice to move their instances from the host in 15 days. To work with a
Dedicated Host that has been removed from a host resource group, see [Work with Dedicated Hosts](../../../AWSEC2/latest/UserGuide/how-dedicated-hosts-work.md "../../../AWSEC2/latest/UserGuide/how-dedicated-hosts-work.md") in the
_Amazon EC2 User Guide_.

Use the following steps to remove a Dedicated Host to a host resource group:

1. Log into the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. Choose **Host resource groups**.
3. Click on the name of the host resource that you want to remove a Dedicated Host.
4. Choose **Dedicated Hosts**.
5. Choose the Dedicated Host to delete from the host resource group. Or, you can search
   for a Dedicated Host by host ID, host type, host state, or availability zone.
6. Choose **Remove**.
7. Choose **Remove** again to confirm.
