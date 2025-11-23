# Edit a self-managed license in

License Manager

You can edit values for the following fields in a self-managed license:

- Self-managed license name
- Description
- Expiry Date
- Number of <option>
- Enforce license type limit

###### To edit a self-managed license

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the left navigation pane, choose **self-managed licenses**.
3. Select the self-managed license.
4. Choose **Actions**, **Edit**.
5. Edit the details as needed and then choose **Update**.

###### Note

Once the License Expiry Date is set, License Manager can send notifications on 120 days, 90 days, 60 days, 30 days, 0 day to the Amazon SNS topic that's configured in [Managed license settings in License Manager](settings-managed-licenses.md "settings-managed-licenses.md").

###### To edit a self-managed license using the command line

- [update-license-configuration](../../../cli/latest/reference/license-manager/update-license-configuration.md "../../../cli/latest/reference/license-manager/update-license-configuration.md") (AWS CLI)
- [Update-LICMLicenseConfiguration](../../../powershell/latest/reference/items/Update-LICMLicenseConfiguration.md "../../../powershell/latest/reference/items/Update-LICMLicenseConfiguration.md") (AWS Tools for PowerShell)
