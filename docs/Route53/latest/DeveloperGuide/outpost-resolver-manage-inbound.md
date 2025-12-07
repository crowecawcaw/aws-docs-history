# Managing inbound endpoints on

Resolver on Outpost

To manage inbound endpoints on Resolver on Outpost, perform the applicable procedure.

###### Topics

- [Viewing and editing inbound endpoints](#resolver-forwarding-inbound-queries-managing-viewing-outpost "#resolver-forwarding-inbound-queries-managing-viewing-outpost")
- [Viewing the status for inbound endpoints](#resolver-forwarding-inbound-queries-managing-viewing-status-outpost "#resolver-forwarding-inbound-queries-managing-viewing-status-outpost")
- [Deleting inbound endpoints](#resolver-forwarding-inbound-queries-managing-deleting-outpost "#resolver-forwarding-inbound-queries-managing-deleting-outpost")

## Viewing and editing inbound endpoints

To view and edit settings for an inbound endpoint, perform the following
procedure.

###### To view and edit settings for an inbound endpoint

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the left navigation pane, expand **Resolver**, and
   then navigate to **Outposts**.
3. On the navigation bar, choose the Region where your AWS Outposts is
   located.
4. Select the check box next to the VPC Resolver that is in operational state and
   choose **View details**.
5. In the **Inbound endpoints** list, choose the option for
   the endpoint that you want to view settings for or want to edit.
6. Choose **View details** or
   **Edit**.

For information about the values for inbound endpoints, see [Values that you specify when you create or edit outbound endpoints in an
AWS Outposts](outpost-resolver-add-outbound-endpoints.md#resolver-forwarding-outbound-queries-endpoint-values-outpost "outpost-resolver-add-outbound-endpoints.md#resolver-forwarding-outbound-queries-endpoint-values-outpost"). 7. If you chose **Edit**, enter the applicable values, and
choose **Save**.

## Viewing the status for inbound endpoints

To view the status for an inbound endpoint, perform the following
procedure.

###### To view the status for an inbound endpoint

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the left navigation pane, expand **Resolver**, and
   then navigate to **Outposts**.
3. On the navigation bar, choose the Region where your AWS Outposts is
   located.
4. Select the check box next to the VPC Resolver that is in operation state and
   choose **View details**.
5. The **Status** column of the **inbound
   endpoints** list contains one of the following values:

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
delete the IP address that isn't available. An endpoint must
always include at least two IP addresses. A status of
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

## Deleting inbound endpoints

To delete an inbound endpoint, perform the following procedure.

###### Important

If you delete an inbound endpoint, DNS queries from your network are no longer
forwarded to VPC Resolver in the VPC that you specified in the endpoint.

###### To delete an inbound endpoint

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the left navigation pane, expand **Resolver**, and
   then navigate to **Outposts**.
3. On the navigation bar, choose the Region where your AWS Outposts is
   located.
4. Select the check box next to the VPC Resolver that is in operation state and
   choose **View details**.
5. Choose the check box next to the endpoint that you want to delete.
6. Choose **Delete**.
7. To confirm that you want to delete the endpoint, enter the name of the
   endpoint and choose **Submit**.
