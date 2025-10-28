# Associate a MACsec CKN/CAK with an AWS Direct Connect

connection

After you create the connection that supports MACsec, you can associate a CKN/CAK with the
connection. You can create the association using either the AWS Direct Connect console or through the
command-line or API.

###### Note

You cannot modify a MACsec secret key after you associate it with a connection. If
you need to modify the key, disassociate the key from the connection, and then
associate a new key with the connection. For information about removing an
association, see [Remove the association between a MACsec secret key
and a connection](disassociate-key-connection.md "disassociate-key-connection.md").

###### To associate a MACsec key with a connection

1. Open the **AWS Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2. In the left pane, choose **Connections**.
3. Select a connection, and then choose **View
   details**.
4. Choose **Associate key**.
5. Enter the MACsec key.

[Use the CAK/CKN pair] Choose **Key Pair**, and then do the
following:

    * For **Connectivity Association Key
     (CAK)**, enter the CAK.
    * For **Connectivity Association Key Name
     (CKN)**, enter the CKN.

[Use the secret] Choose **Existing Secret Manager secret**, and then
for **Secret**, select the MACsec secret
key. 6. Choose **Associate key**.

###### To associate a MACsec key with a connection using the command line or

API

- [associate-mac-sec-key](../../../cli/latest/reference/directconnect/associate-mac-sec-key.md "../../../cli/latest/reference/directconnect/associate-mac-sec-key.md") (AWS CLI)
- [AssociateMacSecKey](../APIReference/API_AssociateMacSecKey.md "../APIReference/API_AssociateMacSecKey.md") (AWS Direct Connect API)
