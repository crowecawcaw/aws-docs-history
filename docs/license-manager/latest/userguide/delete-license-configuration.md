# Delete a self-managed license in

License Manager

Before you can delete a self-managed license, you must disassociate any resources. You can
delete a self-managed license if you need to start over with new licensing rules. If the
licensing terms from your software vendors change, you can disassociate existing resources,
delete the self-managed license, create a new self-managed license to reflect the updated terms
and associate it with the existing resources.

###### To delete a self-managed license using the console

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the left navigation pane, choose **Self-managed licenses**.
3. Choose the name of the self-managed license to open the license details page.
4. Select each resource (individually or in bulk) and choose **Disassociate resource**.
   Repeat until the list is empty.
5. Choose **Actions**, **Delete**. When prompted for confirmation,
   choose **Delete**.

###### To delete a self-managed license using the command line

- [delete-license-configuration](../../../cli/latest/reference/license-manager/delete-license-configuration.md "../../../cli/latest/reference/license-manager/delete-license-configuration.md") (AWS CLI)
- [Remove-LICMLicenseConfiguration](../../../powershell/latest/reference/items/Remove-LICMLicenseConfiguration.md "../../../powershell/latest/reference/items/Remove-LICMLicenseConfiguration.md") (AWS Tools for PowerShell)
