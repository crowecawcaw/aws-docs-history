

# Remove the association between a MACsec secret key and a Direct Connect connection
<a name="disassociate-key-connection"></a>

You can remove the association between the connection and the MACsec key using either the Direct Connect console or through the command-line or API.

**To remove an association between a connection and a MACsec key**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. 

1. In the left pane, choose **Connections**.

1. Select a connection, and then choose **View details**.

1. Select the MACsec secret to remove, and then choose **Disassociate key**.

1. In the confirmation dialog box, enter **disassociate**, and then choose **Disassociate**.

**To remove an association between a connection and a MACsec key using the command line or API**
+ [disassociate-mac-sec-key](https://docs.aws.amazon.com/cli/latest/reference/directconnect/disassociate-mac-sec-key.html) (AWS CLI)
+ [DisassociateMacSecKey](https://docs.aws.amazon.com/directconnect/latest/APIReference/API__DisassociateMacSecKey.html) (Direct Connect API)