

# Accepting or declining a link request
<a name="accepting-declining-link-request"></a>

When another RTB Fabric user sends you a link request, you can accept or reject it from your gateway's **Associated links** tab. Link requests allow other RTB Fabric users to connect and send bid requests to your gateway.

**To accept or reject a link request**

1. Sign in to the AWS Management Console and open the RTB Fabric console at [https://console.aws.amazon.com/rtbfabric](https://console.aws.amazon.com/rtbfabric).

1. Choose either **Requester Gateways** or **Responder Gateways** depending on which gateway received the link request.

1. Choose the gateway that received the link request.

1. Choose the **Associated links** tab to view pending link requests.

1. In the **Links** section, locate the link request you want to respond to in the links table. The table displays the following information:
   + **Link ID** – Unique identifier for the link.
   + **Link status** – Current status of the link request.
   + **Link creation date (UTC)** – When the request was created.
   + **Responder Gateway ID** – Target gateway ID.
   + **Actions** – Available actions for the link.

1. In the **Actions** column for the link request, choose one of the following:
   + **To accept the link request:**

     1. Choose **Accept**.

     1. In the confirmation dialog, choose **Accept** to confirm.

     1. The link status changes to **Active** and bid requests can now flow between the gateways.
   + **To reject the link request:**

     1. Choose **Reject**.

     1. In the confirmation dialog, choose **Reject** to confirm.

     1. The link status changes to **Rejected** and the connection request is rejected.

Once you accept a link request, the requesting gateway can send bid requests to your gateway. You can view link metrics and manage the connection from the **Associated links** tab.

**Note**  
You can also choose **View details** to see more information about the link request before making your decision. The links table also includes action buttons for **Accept**, **Reject**, and **Delete** operations.

**Important**  
Links that are not accepted within 7 days of requesting will time out, and will need to be re-initiated. 

## AWS CLI
<a name="accept-reject-link-cli"></a>

Use the following commands to accept or reject link requests using the AWS Command Line Interface (AWS CLI).

**Accept a link request**

```
$ aws rtbfabric accept-link \
--gateway-id {{"rtb-gw-target456"}} \
--link-id {{"link-sedf903ujiose"}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```

**Reject a link request**

```
$ aws rtbfabric reject-link \
--gateway-id {{"rtb-gw-target456"}} \
--link-id {{"link-sedf903ujiose"}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```