

# Deleting links
<a name="deleting-rtb-links"></a>

When you no longer need a link, you can delete it from either the requester or responder gateway. This action permanently removes the connection and stops all communication between the linked gateways.

**Warning**  
Deleting a link is irreversible and will immediately stop all bid request processing between the connected gateways. Ensure that you no longer need the link before proceeding.

**To delete a link**

1. Navigate to RTB Fabric console and choose either **Requester Gateways** or **Responder Gateways** depending on which resource owns the link you want to delete.

1. Access the link details using one of these methods:
   + On the gateways page, select the radio button next to the desired gateway. In the **Links associated with this gateway** section at the bottom of the page, choose the **Link ID** you want to delete.
   + Choose the **gateway ID** to open the gateway details page. Choose the **Associated links** tab and choose the **Link ID** you want to delete.

1. On the link details page, review the link information including:
   + **Link ID** – Unique identifier for the link.
   + **Link status** – Current status (Requested, Active, etc.).
   + **gateway ID** – Source gateway.
   + **Peer gateway ID** – Target gateway.
   + **Link created on** and **Link updated on** – Timestamps.

1. Choose **Delete link** from the action buttons at the top of the page.

1. In the confirmation dialog, verify that you want to delete the selected link.

1. Choose **Delete** to confirm the deletion.

The link is immediately removed from both gateways and will no longer facilitate communication between them. Any ongoing bid requests using this link will be terminated.

## AWS CLI
<a name="delete-link-cli"></a>

Use the following command to delete a link between gateways using the AWS Command Line Interface (AWS CLI).

**Delete a link from a gateway**

```
$ aws rtbfabric delete-link \
--gateway-id {{"rtb-gw-source123"}} \
--link-id {{"link-sedf903ujiose"}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```