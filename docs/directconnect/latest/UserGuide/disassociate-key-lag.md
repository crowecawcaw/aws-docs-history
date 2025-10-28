# Remove the association between a MACsec secret key and an AWS Direct Connect endpoint

LAG

You can remove the association between the LAG and the MACsec key using either the AWS Direct Connect console or using the command line or API.

###### To remove an association between a LAG and a MACsec key

1. Open the **AWS Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2. In the navigation pane, choose **LAGs**.
3. Select the LAG and choose **View
   details**.
4. Select the MACsec secret to remove, and then choose
   **Disassociate key**.
5. In the confirmation dialog box, enter
   **disassociate**, and then choose
   **Disassociate**.

###### To remove an association between a LAG and a MACsec key using the command line or API

- [disassociate-mac-sec-key](../../../cli/latest/reference/directconnect/disassociate-mac-sec-key.md "../../../cli/latest/reference/directconnect/disassociate-mac-sec-key.md") (AWS CLI)
- [DisassociateMacSecKey](../APIReference/API__DisassociateMacSecKey.md "../APIReference/API__DisassociateMacSecKey.md") (AWS Direct Connect API)
