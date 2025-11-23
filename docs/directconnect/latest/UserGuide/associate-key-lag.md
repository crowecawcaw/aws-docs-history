# Associate a MACsec CKN/CAK with an Direct Connect endpoint LAG

After you create the LAG that supports MACsec, you can associate a CKN/CAK with the
connection using either the Direct Connect console or using the command line or API.

###### Note

You cannot modify a MACsec secret key after you associate it with a LAG. If you need to
modify the key, disassociate the key from the connection, and then associate a new
key with the connection. For information about removing an association, see [Remove the association between a MACsec secret key and an Direct Connect endpoint
LAG](disassociate-key-lag.md "disassociate-key-lag.md").

###### To associate a MACsec key with a LAG

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2. In the navigation pane, choose **LAGs**.
3. Select the LAG and choose **View
   details**.
4. Choose **Associate key**.
5. Enter the MACsec key.

[Use the CAK/CKN pair] Choose **Key Pair**, and
then do the following:

    * For **Connectivity Association Key
     (CAK)**, enter the CAK.
    * For **Connectivity Association Key Name
     (CKN)**, enter the CKN.

[Use the secret] Choose **Existing Secret Manager
secret**, and then for **Secret**,
select the MACsec secret key. 6. Choose **Associate key**.

###### To associate a MACsec key with a LAG using the command line or API

- [associate-mac-sec-key](../../../cli/latest/reference/directconnect/associate-mac-sec-key.md "../../../cli/latest/reference/directconnect/associate-mac-sec-key.md") (AWS CLI)
- [AssociateMacSecKey](../APIReference/API_AssociateMacSecKey.md "../APIReference/API_AssociateMacSecKey.md") (Direct Connect API)
