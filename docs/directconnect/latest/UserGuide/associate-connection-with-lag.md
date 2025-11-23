# Associate a connection with a LAG at an Direct Connect endpoint

You can associate an existing connection with a LAG using either the Direct Connect console or using the command line or API. The connection can be standalone, or it
can be part of another LAG. The connection must be on the same AWS device and must use
the same bandwidth as the LAG. If the connection is already associated with another LAG,
you cannot re-associate it if removing the connection causes the original LAG to fall
below its threshold for the minimum number of operational connections.

Associating a connection to a LAG automatically re-associates its virtual interfaces to the
LAG.

###### Important

Connectivity to AWS over the connection is interrupted during association.

###### To associate a connection with a LAG

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2. In the navigation pane, choose **LAGs**.
3. Select the LAG, and then choose **View details**.
4. Under **Connections**, choose **Associate
   connection**.
5. For **Connection**, choose the Direct Connect connection to use for the
   LAG.
6. Choose **Associate
   Connection**.

###### To associate a connection using the command line or API

- [associate-connection-with-lag](../../../cli/latest/reference/directconnect/associate-connection-with-lag.md "../../../cli/latest/reference/directconnect/associate-connection-with-lag.md") (AWS CLI)
- [AssociateConnectionWithLag](../APIReference/API_AssociateConnectionWithLag.md "../APIReference/API_AssociateConnectionWithLag.md") (Direct Connect API)
