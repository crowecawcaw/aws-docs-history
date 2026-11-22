

# Connecting a procurement system

To route approval requests to Coupa or SAP Ariba, connect your procurement system on the **External system** tab of the **Approvers and routing** page. Your organization can connect one procurement system. For more information, see [Integrating AWS Marketplace with procurement systems](procurement-system-integration.md).

**To connect a procurement system**

1. Open [Approvers and routing](https://console.aws.amazon.com/marketplace/buying-policies/approvers-and-routing?tab=external-system) in the AWS Marketplace console. It's under **Buying policies** in the left navigation pane.

1. On the **External system** tab, choose **Connect external system**.

1. Do one of the following:
   + If you already have portal connections, review them under **Portal connections**. Only connections with AWS Marketplace PunchOut enabled are used to route requests. To enable it for a connection, select the connection and choose **Enable AWS Marketplace PunchOut for this connection**.
   + To create a new connection, choose **Coupa** or **SAP Ariba** under **External system**, and then enter the connection details. For Coupa, enter the **Buyer ID**, **Shared secret**, and **Supplier ID** from your procurement system's cXML configuration. For SAP Ariba, enter the **Buyer ANID** and choose the **Supplier ANID**.

1. Choose **Connect system**.

When you connect a procurement system, AWS Marketplace automatically creates a single-level approval chain for it. To route purchases to the system, create a rule with the **External system** routing. To update connection identity values or Sellers of Record, use the Billing console. You can't remove a procurement system after you connect it. To remove a connected system, contact AWS Marketplace customer support.