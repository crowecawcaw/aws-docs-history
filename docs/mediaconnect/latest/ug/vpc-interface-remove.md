# Removing a VPC interface from a MediaConnect flow

You can remove a VPC interface from your flow if it isn't used as a source for the
flow.

## Prerequisites

- The flow must be in **Standby**.
- If the flow has an error, you must resolve the error before you complete
  the following procedure.

## Procedure

###### To remove a VPC interface from a flow (console)

1. On the **Flows** page, choose the name of the flow that is
   associated with the VPC interface that you want to remove.
2. Choose **Stop**.

The status of the flow changes to **Standby**. The flow stops
immediately and is no longer viewable to customers who are accessing the output
directly from your flow or through an entitlement. 3. Choose the **VPC interfaces** tab. 4. Choose the VPC interface that you want to remove, and then choose
**Remove**.
