# Get started using MACsec on a dedicated Direct Connect

connection

The following task gets you started setting up MACsec to use on a Direct Connect dedicated
connection

## Step 1: Create a connection

To start using MACsec, you must turn the feature on when you create a dedicated
connection.

## (Optional) Step 2: Create a link aggregation

group (LAG)

If you use multiple connections for redundancy, you can create a LAG that supports
MACsec. For more information, see [MACsec considerations](lags.md#lag-macsec-considerations "lags.md#lag-macsec-considerations") and [Create a LAG](create-lag.md "create-lag.md").

## Step 3: Associate the CKN/CAK with the connection

or LAG

After you create the connection or LAG that supports MACsec, you need to associate a
CKN/CAK with the connection. For more information, see one of the following:

- [Associate a MACsec CKN/CAK with a
  connection](associate-key-connection.md "associate-key-connection.md")
- [Associate a MACsec CKN/CAK with a LAG](associate-key-lag.md "associate-key-lag.md")

## Step 4: Configure your on-premises router

Update your on-premises router with the MACsec secret key. The MACsec secret key on
the on-premises router and in the Direct Connect location must match. For more information,
see [Download the router configuration file](vif-router-config.md "vif-router-config.md").

## Step 5: (Optional) Remove the association

between the CKN/CAK and the connection or LAG

You can optionally remove the association between the CKN/CAK and the connection or LAG. f you need to remove the association, see one of the following:

- [Remove the association between a MACsec secret key
  and a connection](disassociate-key-connection.md "disassociate-key-connection.md")
- [Remove the association between a MACsec secret key and a
  LAG](disassociate-key-lag.md "disassociate-key-lag.md")
