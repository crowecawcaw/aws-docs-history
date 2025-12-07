# Managing outbound endpoints

on Resolver on Outpost

To manage outbound endpoints on Resolver on Outpost, perform the applicable procedure.

###### Topics

- [Viewing and editing outbound endpoints](#resolver-forwarding-outbound-queries-managing-viewing-outpost "#resolver-forwarding-outbound-queries-managing-viewing-outpost")
- [Viewing the status for outbound endpoints](#resolver-forwarding-outbound-queries-managing-viewing-status-outpost "#resolver-forwarding-outbound-queries-managing-viewing-status-outpost")
- [Deleting outbound endpoints](#resolver-forwarding-outbound-queries-managing-deleting-outpost "#resolver-forwarding-outbound-queries-managing-deleting-outpost")

## Viewing and editing outbound endpoints

To view and edit settings for an outbound endpoint, perform the following
procedure.

###### To view and edit settings for an outbound endpoint

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the left navigation pane, expand **Resolver**, and
   then navigate to **Outposts**.
3. On the navigation bar, choose the Region where your AWS Outposts is
   located.
4. Select the check box next to the VPC Resolver that is in operation state and
   choose **View details**.
5. In the **Outbound endpoints** list, choose the check box
   next to the endpoint that you want to view settings for or want to
   edit.
6. Choose **View details** or
   **Edit**.

For information about the values for outbound endpoints, see [Values that you specify when you create or edit outbound endpoints in an
AWS Outposts](outpost-resolver-add-outbound-endpoints.md#resolver-forwarding-outbound-queries-endpoint-values-outpost "outpost-resolver-add-outbound-endpoints.md#resolver-forwarding-outbound-queries-endpoint-values-outpost"). 7. If you chose **Edit**, enter the applicable values, and
then choose **Save**.

## Viewing the status for outbound endpoints

To view the status for an outbound endpoint, perform the following
procedure.

###### To view the status for an outbound endpoint

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the left navigation pane, expand **Resolver**, and
   then navigate to **Outposts**.
3. On the navigation bar, choose the Region where your AWS Outposts is
   located.
4. Select the check box next to the VPC Resolver that is in operation state and
   choose **View details**.
5. In the **Outbound endpoints** list, the
   **Status** column contains one of the following
   values:

**Creating**

VPC Resolver is creating and configuring one or more Amazon VPC
network interfaces for this endpoint.

**Operational**

The Amazon VPC network interfaces for this endpoint are correctly
configured and able to pass inbound or outbound DNS queries
between your network and VPC Resolver.

**Updating**

Resolver is associating or disassociating one or more network
interfaces with this endpoint.

**Auto recovering**

VPC Resolver is trying to recover one or more of the network
interfaces that are associated with this endpoint. During the
recovery process, the endpoint functions with limited capacity
because of the limit on the number of DNS queries per IP address
(per network interface). For the current limit, see [Quotas on Route 53 VPC Resolver](DNSLimitations.md#limits-api-entities-resolver "DNSLimitations.md#limits-api-entities-resolver").

**Action needed**

This endpoint is unhealthy, and VPC Resolver can't automatically
recover it. To resolve the problem, we recommend that you check
each IP address that you associated with the endpoint. For each
IP address that isn't available, add another IP address and then
delete the IP address that isn't available. (An endpoint must
always include at least two IP addresses.) A status of
**Action needed** can have a variety of
causes. Here are two common causes:

    * One or more of the network interfaces that are
     associated with the endpoint were deleted using
     Amazon VPC.
    * The network interface couldn't be created for some
     reason that's outside the control of VPC Resolver.

**Deleting**

Resolver is deleting this endpoint and the associated network
interfaces.

## Deleting outbound endpoints

Before you can delete an endpoint, you must first delete any rules that are
associated to a VPC.

To delete an outbound endpoint, perform the following procedure.

###### Important

If you delete an outbound endpoint, VPC Resolver stops forwarding DNS queries from
your VPC to your network for rules that specify the deleted outbound
endpoint.

###### To delete an outbound endpoint

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the left navigation pane, expand **Resolver**, and
   then navigate to **Outposts**.
3. Select the check box next to the VPC Resolver that is in operation state and
   choose **View details**.
4. In the **Outbound endpoints** list choose the option for
   the endpoint that you want to delete.
5. Choose **Delete**.
6. To confirm that you want to delete the endpoint, enter the name of the
   endpoint, and then choose **Submit**.
