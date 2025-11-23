# Disassociate a connection from a LAG at an Direct Connect endpoint

Convert a connection to standalone by disassociating it from a LAG using either the Direct Connect console or using the command line or API. You can't disassociate a
connection if it causes the LAG to fall below its threshold for the minimum number of
operational connections.

Disassociating a connection from a LAG does not automatically disassociate any virtual
interfaces.

###### Important

Your connection to AWS is broken off during disassociation.

###### To disassociate a connection from a LAG

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2. In the left pane, choose **LAGs**.
3. Select the LAG, and then choose **View details**.
4. Under **Connections**, select the connection from the list of available
   connections and choose **Disassociate**.
5. In the confirmation dialog box, choose **Disassociate**.

###### To disassociate a connection using the command line or API

- [disassociate-connection-from-lag](../../../cli/latest/reference/directconnect/disassociate-connection-from-lag.md "../../../cli/latest/reference/directconnect/disassociate-connection-from-lag.md") (AWS CLI)
- [DisassociateConnectionFromLag](../APIReference/API_DisassociateConnectionFromLag.md "../APIReference/API_DisassociateConnectionFromLag.md") (Direct Connect API)
