

# Get started using MACsec on a dedicated Direct Connect connection
<a name="create-macsec-dedicated"></a>

The following task gets you started setting up MACsec to use on a Direct Connect dedicated connection

## Step 1: Create a connection
<a name="step-create-connection"></a>

 To start using MACsec, you must turn the feature on when you create a dedicated connection. 

## (Optional) Step 2: Create a link aggregation group (LAG)
<a name="step-create-lag"></a>

 If you use multiple connections for redundancy, you can create a LAG that supports MACsec. For more information, see [MACsec considerations](lags.md#lag-macsec-considerations) and [Create a LAG](create-lag.md).

## Step 3: Associate the CKN/CAK with the connection or LAG
<a name="step-associate-key"></a>

After you create the connection or LAG that supports MACsec, you need to associate a CKN/CAK with the connection. For more information, see one of the following:
+ [Associate a MACsec CKN/CAK with a connection](associate-key-connection.md)
+ [Associate a MACsec CKN/CAK with a LAG](associate-key-lag.md)

## Step 4: Configure your on-premises router
<a name="associate-key-router"></a>

Update your on-premises router with the MACsec secret key. The MACsec secret key on the on-premises router and in the Direct Connect location must match. For more information, see [Download the router configuration file](vif-router-config.md).

## Step 5: (Optional) Remove the association between the CKN/CAK and the connection or LAG
<a name="step-disassociate-key"></a>

You can optionally remove the association between the CKN/CAK and the connection or LAG. f you need to remove the association, see one of the following:
+ [Remove the association between a MACsec secret key and a connection](disassociate-key-connection.md)
+ [Remove the association between a MACsec secret key and a LAG](disassociate-key-lag.md)