# Monitor your global network using EventBridge

Amazon EventBridge delivers a near-real-time stream of system events that describe changes in your
resources. Using simple rules that you can quickly set up, you can match events and
route them to one or more target functions or streams. For more information, see the
_[Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md")_.

AWS Global Networks for Transit Gateways sends the following types of events to EventBridge:

- [Topology change events](#network-topology-events "#network-topology-events")
- [Routing update events](#routing-changes-events "#routing-changes-events")
- [Status update events](#network-status-events "#network-status-events")

## Get started

Before you can view events for your global network, you must onboard to CloudWatch Logs
Insights. In the global networks console, choose the ID of your global network. In the
**Network events summary** section, choose **Onboard to
CloudWatch Log Insights**.

An IAM principal in your account, such as an IAM user, must have sufficient
permissions to onboard to CloudWatch Logs Insights. Ensure that the IAM policy contains the
following permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "events:PutTargets",
 "events:DescribeRule",
 "logs:PutResourcePolicy",
 "logs:DescribeLogGroups",
 "logs:DescribeResourcePolicies",
 "events:PutRule",
 "logs:CreateLogGroup"
 ],
 "Resource": "*"
 }
 ]
}`

```

The preceding policy does not grant permission to create, modify, or delete Network Manager
resources. For more information about IAM policies for working with Network Manager, see [Identity and access management for AWS Global Networks for Transit Gateways](nm-security-iam.md "nm-security-iam.md").

When you onboard to CloudWatch Logs Insights, the following occurs:

- A CloudWatch event rule with the name
  `DON_NOT_DELETE_networkmanager_rule` is created in the
  US West (Oregon) Region.
- A CloudWatch Logs log group with the name
  `/aws/events/networkmanagerloggroup` is created in the
  US West (Oregon) Region.
- The CloudWatch event rule is configured with the CloudWatch Logs log group as a
  target.
- A CloudWatch resource policy with the name
  `DO_NOT_DELETE_networkmanager_TrustEventsToStoreLogEvents` is
  created in the US West (Oregon) Region. To view this policy, use the
  following AWS CLI command: `aws logs describe-resource-policies --region
us-west-2`

### View transit gateway events using the AWS Transit Gateway

console

You can view events for your global network or view a specific transit gateway using the
global networks console.

###### To view global network events

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, choose **Transit gateway network**.
5. Choose **Events**.

On this page you can view events for your transit gateway network. For
more information about this page, see [Events](nm-visualize-tgw.md#tgw-visualize-events "nm-visualize-tgw.md#tgw-visualize-events").

###### To view events for a specific transit gateway

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, choose **Transit gateways**.
5. Choose the **Transit gateway ID**.
6. Choose **Events**.

On this page you can view events for your transit gateway network. For
more information about this page, see [Events](nm-visualize-tgw.md#tgw-visualize-events "nm-visualize-tgw.md#tgw-visualize-events").

## Topology change events

Topology change events occur when there have been changes to the resources in your
global network. These include the following:

###### Events

- [A transit gateway in the global network was
  deleted (TGW-DELETED)](#tgw-delete "#tgw-delete")
- [A VPN connection was created for a transit
  gateway (VPN-CONNECTION-CREATED)](#vpn-tgw-create "#vpn-tgw-create")
- [A VPN connection was deleted on a transit
  gateway (VPN-CONNECTION-DELETED)](#vpn-tgw-delete "#vpn-tgw-delete")
- [The customer gateway for a VPN connection
  was changed (VPN-CONNECTION-CUSTOMER-GATEWAY-MODIFIED)](#vpn-gateway-changed "#vpn-gateway-changed")
- [The target gateway for a VPN
  connection was changed (VPN-CONNECTION-TARGET-GATEWAY-MODIFIED)](#vpn-target-gateway-changed "#vpn-target-gateway-changed")
- [A VPC was attached to a transit gateway
  (VPC-ATTACHMENT-CREATED)](#vpc-tgw-attach "#vpc-tgw-attach")
- [A VPC attachment was deleted from a
  transit gateway (VPC-ATTACHMENT-DELETED)](#vpc-attach-tgw-delete "#vpc-attach-tgw-delete")
- [An AWS Direct Connect gateway was attached to a
  transit gateway (DXGW-ATTACHMENT-CREATED)](#dx-gateway-attach "#dx-gateway-attach")
- [An AWS Direct Connect gateway was detached from a
  transit gateway (DXGW-ATTACHMENT-DELETED)](#dx-gateway-detach "#dx-gateway-detach")
- [A transit gateway peering connection
  attachment was created (TGW_PEERING_CREATED)](#tgw-peering-attach "#tgw-peering-attach")
- [A transit gateway peering connection was deleted
  (TGW-PEERING-DELETED)](#tgw-peering-delete "#tgw-peering-delete")
- [A transit gateway
  Connect attachment was created for a transit gateway
  (CONNECT_ATTACHMENT_CREATED)](#connect-attachment-create "#connect-attachment-create")
- [A transit gateway
  Connect attachment was deleted for a transit gateway
  (CONNECT_ATTACHMENT_DELETED)](#connect-attachment-delete "#connect-attachment-delete")
- [A transit gateway Connect peer was created in
  a Connect attachment (TGW-CONNECT-PEER-CREATED)](#tgw-connect-peer-created "#tgw-connect-peer-created")
- [A transit gateway Connect peer was deleted in
  a Connect attachment (CONNECT_PEER_DELETED)](#tgw-connect-peer-deleted "#tgw-connect-peer-deleted")
- [A Network Firewall attachment was created (NETWORK-FIREWALL-ATTACHMENT-CREATED)](#vpc-firewall-attach "#vpc-firewall-attach")
- [A Network Firewall attachment was deleted (NETWORK-FIREWALL-ATTACHMENT-DELETED)](#vpc-firewall-delete "#vpc-firewall-delete")

### A transit gateway in the global network was

deleted (TGW-DELETED)

```
{"version":"0",
"id":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
"detail-type":"Network Manager Topology Change",
"source":"aws.networkmanager",
"account":"123456789012",
"time":"2023-01-18T22:18:44Z",
"region":"us-west-2",
"resources":[
    "arn:aws:networkmanager::123456789012:global-network/global-network-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:123456789012:transit-gateway/tgw-1234567890abcdef0"
],
"detail":{
    "changeType":"TGW-DELETED",
    "changeDescription":"A Transit Gateway in the global network has been deleted.",
    "region":"us-east-1",
    "transitGatewayArn":"arn:aws:ec2:us-east-1:123456789012:transit-gateway/tgw-1234567890abcdef0"}}

```

### A VPN connection was created for a transit

gateway (VPN-CONNECTION-CREATED)

```
{
"version":"0",
"id":"7636f496-ba9f-b1cc-22a6-8c90bbca8540",
"detail-type":"Network Manager Topology Change",
"source":"aws.networkmanager",
"account":"123456789012",
"time":"2023-01-18T19:52:42Z",
"region":"us-west-2",
"resources":[
    "arn:aws:networkmanager::123456789012:global-network/global-network-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:123456789012:vpn-connection/vpn-01c3c3738ab9f83c5"
],
"detail":{
    "changeType":"VPN-CONNECTION-CREATED",
    "changeDescription":"A Site-to-Site VPN connection has been created.",
    "region":"us-east-1",
    "transitGatewayAttachmentArn":"arn:aws:ec2:us-east-1:123456789012:transit-gateway-attachment/tgw-attach-1234567890abcdef0",
    "vpnConnectionArn":"arn:aws:ec2:us-east-1:123456789012:vpn-connection/vpn-1234567890abcdef0",
    "customerGatewayArn":"arn:aws:ec2:us-east-1:123456789012:customer-gateway/cgw-1234567890abcdef0",
    "outsideIpAddresses":["54.166.146.158","3.93.214.172"],
    "routing":"dynamic_route",
    "accelerated":false,
    "isPrivateVpn":false,
    "transitGatewayArn":"arn:aws:ec2:us-east-1:123456789012:transit-gateway/tgw-1234567890abcdef0"
    }
}
```

### A VPN connection was deleted on a transit

gateway (VPN-CONNECTION-DELETED)

```
{
"version":"0",
"id":"877fe5fd-4c95-1553-84ef-cfa271121081",
"detail-type":"Network Manager Topology Change",
"source":"aws.networkmanager",
"account":"123456789012",
"time":"2023-01-19T19:43:12Z",
"region":"us-west-2",
"resources":[
    "arn:aws:networkmanager::123456789012:global-network/global-network-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:123456789012:vpn-connection/vpn-1234567890abcdef0"
    ],
"detail":{
    "changeType":"VPN-CONNECTION-DELETED",
    "changeDescription":"A Site-to-Site VPN connection has been deleted.",
    "region":"us-east-1",
    "transitGatewayAttachmentArn":"arn:aws:ec2:us-east-1:123456789012:transit-gateway-attachment/tgw-attach-1234567890abcdef0",
    "vpnConnectionArn":"arn:aws:ec2:us-east-1:123456789012:vpn-connection/vpn-1234567890abcdef0",
    "customerGatewayArn":"arn:aws:ec2:us-east-1:123456789012:customer-gateway/cgw-1234567890abcdef0",
    "isPrivateVpn":false,
    "transitGatewayArn":"arn:aws:ec2:us-east-1:123456789012:transit-gateway/tgw-1234567890abcdef0"
    }
}
```

### The customer gateway for a VPN connection

was changed (VPN-CONNECTION-CUSTOMER-GATEWAY-MODIFIED)

```
{"version":"0",
"id":"76594f68-2b9f-7885-895e-58ece42ac48a",
"detail-type":"Network Manager Topology Change",
"source":"aws.networkmanager",
"account":"123456789012","time":"2023-06-28T19:25:12Z",
"region":"us-west-2",
"resources":[
    "arn:aws:networkmanager::123456789012:global-network/global-network-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:123456789012:vpn-connection/vpn-0822025a9ea3dde43"
],
"detail":{
    "changeType":"VPN-CONNECTION-CUSTOMER-GATEWAY-MODIFIED",
    "changeDescription":"The customer gateway of a Site-to-Site VPN connection has been modified",
    "region":"us-east-1",
    "vpnConnectionArn":"arn:aws:ec2:us-east-1:123456789012:vpn-connection/vpn-1234567890abcdef0",
    "previousCustomerGatewayArn":"arn:aws:ec2:us-east-1:123456789012:customer-gateway/cgw-1234567890abcdef0",
    "currentCustomerGatewayArn":"arn:aws:ec2:us-east-1:123456789012:customer-gateway/cgw-1234567890abcdef0",
    "transitGatewayArn":"arn:aws:ec2:us-east-1:123456789012:transit-gateway/tgw-1234567890abcdef0"
    }
}
```

### The target gateway for a VPN

connection was changed (VPN-CONNECTION-TARGET-GATEWAY-MODIFIED)

```

{"version":"0",
"id":"668a4e46-a757-3663-dc32-308c5ac5d87f",
"detail-type":"Network Manager Topology Change",
"source":"aws.networkmanager",
"account":"503089527312",
"time":"2023-06-27T18:27:24Z",
"region":"us-west-2",
"resources":[
    "arn:aws:networkmanager::123456789012:global-network/global-network-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:123456789012:vpn-connection/vpn-1234567890abcdef0"
],
"detail":{
    "changeType":"VPN-CONNECTION-TARGET-GATEWAY-MODIFIED",
    "changeDescription":"The target gateway of a Site-to-Site VPN connection has been modified",
    "region":"us-east-1",
    "vpnConnectionArn":"arn:aws:ec2:us-east-1:123456789012:vpn-connection/vpn-1234567890abcdef0",
    "previousTargetGatewayArn":"arn:aws:ec2:us-east-1:123456789012:transit-gateway/tgw-1234567890abcdef0",
    "currentTargetGatewayArn":"arn:aws:ec2:us-east-1:123456789012:transit-gateway/tgw-1234567890abcdef0",
    "transitGatewayArn":"arn:aws:ec2:us-east-1:123456789012:transit-gateway/tgw-1234567890abcdef0"
    }
}
```

### A VPC was attached to a transit gateway

(VPC-ATTACHMENT-CREATED)

```
{
"version":"0",
"id":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
"detail-type":"Network Manager Topology Change",
"source":"aws.networkmanager",
"account":"123456789012",
"time":"2023-01-18T19:52:52Z",
"region":"us-west-2",
"resources": [
    "arn:aws:networkmanager::123456789012:global-network/global-network-1234567890abcdef0",
    "arn:aws:networkmanager::123456789012:core-network/core-network-1234567890abcdef0"
],
"detail":{
    "changeType":"VPC-ATTACHMENT-CREATED",
    "changeDescription":"A VPC attachment has been created for a Core Network.",
    "edgeLocation":"us-east-2",
    "attachmentArn":"arn:aws:networkmanager::123456789012:attachment/attachment-1234567890abcdef0",
    "vpcArn":"arn:aws:ec2:us-east-2:123456789012:vpc/vpc-1234567890abcdef0",
    "coreNetworkArn":"arn:aws:networkmanager::123456789012:core-network/core-network-1234567890abcdef0"
    }
}
```

### A VPC attachment was deleted from a

transit gateway (VPC-ATTACHMENT-DELETED)

```
{
  "account": "123456789012",
  "region": "us-west-2",
  "detail-type": "Network Manager Topology Change",
  "source": "aws.networkmanager",
  "version": "0",
  "time": "2019-06-30T23:18:50Z",
  "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "resources": [
     "arn:aws:networkmanager::123456789012:global-network/global-network-1234567890abcdef0",
     "arn:aws:ec2:us-east-1:123456789012:transit-gateway/tgw-1234567890abcdef0"
  ],
  "detail": {
     "changeType": "VPC-ATTACHMENT-DELETED",
     "changeDescription": "A VPC attachment has been deleted.",
     "region": "us-east-1",
     "transit-gateway-arn": "arn:aws:ec2:us-east-1:123456789012:transit-gateway/tgw-11111111111122222",
     "transit-gateway-attachment-arn": "arn:aws:ec2:us-east-1:123456789012:transit-gateway-attachment/tgw-attach-1234567890abcdef0",
     "vpc-arn": "arn:aws:ec2:us-east-1:123456789012:vpc/vpc-1234567890abcdef0"
  }
}
```

### An AWS Direct Connect gateway was attached to a

transit gateway (DXGW-ATTACHMENT-CREATED)

```
{
"version":"0",
"id":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
"detail-type":"Network Manager Topology Change",
"source":"aws.networkmanager",
"account":"123456789012",
"time":"2023-01-19T18:57:29Z",
"region":"us-west-2",
"resources":[
    "arn:aws:networkmanager::123456789012:global-network/global-network-1234567890abcdef0",
    "arn:aws:ec2:us-west-1:123456789012:transit-gateway/tgw-1234567890abcdef0"],
    "detail":{
        "changeType":"DXGW-ATTACHMENT-CREATED",
        "changeDescription":"A Direct Connect Gateway attachment has been created.",
        "region":"us-west-1",
        "transitGatewayAttachmentArn":"arn:aws:ec2:us-west-1:123456789012:transit-gateway-attachment/tgw-attach-1234567890abcdef0",
        "directConnectGatewayArn":"arn:aws:directconnect::123456789012:dx-gateway/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "transitGatewayArn":"arn:aws:ec2:us-west-1:123456789012:transit-gateway/tgw-1234567890abcdef0"
    }
}
```

### An AWS Direct Connect gateway was detached from a

transit gateway (DXGW-ATTACHMENT-DELETED)

```
{
"version":"0",
"id":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
"detail-type":"Network Manager Topology Change",
"source":"aws.networkmanager",
"account":"123456789012",
"time":"2023-01-19T19:16:23Z",
"region":"us-west-2",
"resources":[
    "arn:aws:networkmanager::123456789012:global-network/global-network-1234567890abcdef0",
    "arn:aws:ec2:us-west-1:123456789012:transit-gateway/tgw-1234567890abcdef0"
],
"detail":{
    "changeType":"DXGW-ATTACHMENT-DELETED",
    "changeDescription":"A Direct Connect Gateway attachment has been deleted.",
    "region":"us-west-1",
    "transitGatewayAttachmentArn":"arn:aws:ec2:us-west-1:123456789012:transit-gateway-attachment/tgw-attach-1234567890abcdef0",
    "directConnectGatewayArn":"arn:aws:directconnect::123456789012:dx-gateway/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "transitGatewayArn":"arn:aws:ec2:us-west-1:123456789012:transit-gateway/tgw-1234567890abcdef0"
    }
}
```

### A transit gateway peering connection

attachment was created (TGW_PEERING_CREATED)

```
{
"version":"0",
"id":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
"detail-type":"Network Manager Topology Change",
"source":"aws.networkmanager",
"account":"123456789012",
"time":"2023-01-18T22:28:51Z",
"region":"us-west-2",
"resources":[
    "arn:aws:networkmanager::123456789012:global-network/global-network-1234567890abcdef0",
    "arn:aws:networkmanager::123456789012:core-network/core-network-1234567890abcdef0"
],
"detail":{
    "changeType":"TGW_PEERING_CREATED",
    "changeDescription":"A Transit Gateway peering has been created for a Core Network.",
    "edgeLocation":"us-east-1",
    "peeringArn":"arn:aws:networkmanager::123456789012:peering/peering-1234567890abcdef0",
    "transitGatewayArn":"arn:aws:ec2:us-east-1:123456789012:transit-gateway/tgw-1234567890abcdef0",
    "coreNetworkArn":"arn:aws:networkmanager::123456789012:core-network/core-network-1234567890abcdef0"
    }
}
```

### A transit gateway peering connection was deleted

(TGW-PEERING-DELETED)

```
{
"version":"0",
"id":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
"detail-type":"Network Manager Topology Change",
"source":"aws.networkmanager",
"account":"503089527312",
"time":"2023-06-27T19:55:59Z",
"region":"us-west-2",
"resources":[
    "arn:aws:networkmanager::123456789012:global-network/global-network-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:111122223333:transit-gateway/tgw-1234567890abcdef0"
],
"detail":{
    "changeType":"TGW-PEERING-DELETED",
    "changeDescription":"A Transit Gateway peering attachment has been deleted.",
    "region":"us-east-1",
    "transitGatewayAttachmentArn":"arn:aws:ec2:us-east-1:111122223333:transit-gateway-attachment/tgw-attach-1234567890abcdef0",
    "peeredTransitGatewayArn":"arn:aws:ec2:us-east-1:111122223333:transit-gateway/tgw-1234567890abcdef0",
    "transitGatewayArn":"arn:aws:ec2:us-east-1:111122223333:transit-gateway/tgw-1234567890abcdef0"
    }
}
```

### A transit gateway

Connect attachment was created for a transit gateway
(CONNECT_ATTACHMENT_CREATED)

```
{
"version":"0",
"id":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
"detail-type":"Network Manager Topology Change",
"source":"aws.networkmanager",
"account":"123456789012",
"time":"2022-11-21T23:23:46Z",
"region":"us-west-2",
"resources":[
    "arn:aws:networkmanager::123456789012:global-network/global-network-1234567890abcdef0",
    "arn:aws:networkmanager::123456789012:core-network/core-network-1234567890abcdef0"
    ],
"detail":{
    "changeType":"CONNECT_ATTACHMENT_CREATED",
    "changeDescription":"A Connect attachment has been created for a Core Network.",
    "edgeLocation":"us-east-1",
    "attachmentArn":"arn:aws:networkmanager::123456789012:attachment/attachment-1234567890abcdef0",
    "transportAttachmentArn":"arn:aws:networkmanager::123456789012:attachment/attachment-1234567890abcdef0",
    "protocol":"GRE",
    "coreNetworkArn":"arn:aws:networkmanager::123456789012:core-network/core-network-1234567890abcdef0"
    }
}
```

### A transit gateway

Connect attachment was deleted for a transit gateway
(CONNECT_ATTACHMENT_DELETED)

```
{
"version":"0",
"id":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
"detail-type":"Network Manager Topology Change",
"source":"aws.networkmanager",
"account":"123456789012",
"time":"2023-01-19T19:26:26Z",
"region":"us-west-2","resources":[
    "arn:aws:networkmanager::123456789012:global-network/global-network-1234567890abcdef0",
    "arn:aws:networkmanager::123456789012:core-network/core-network-1234567890abcdef0"
    ],
"detail":{
    "changeType":"CONNECT_ATTACHMENT_DELETED",
    "changeDescription":"A Connect attachment has been deleted for a Core Network.",
    "edgeLocation":"us-east-1",
    "attachmentArn":"arn:aws:networkmanager::123456789012:attachment/attachment-1234567890abcdef0",
    "transportAttachmentArn":"arn:aws:networkmanager::123456789012:attachment/attachment-1234567890abcdef0",
    "coreNetworkArn":"arn:aws:networkmanager::123456789012:core-network/core-network-1234567890abcdef0"
    }
}
```

### A transit gateway Connect peer was created in

a Connect attachment (TGW-CONNECT-PEER-CREATED)

```
{
"version": "0",
"id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
"detail-type": "Network Manager Topology Change",
"source": "aws.networkmanager",
"account": "123456789012",
"time": "2023-06-27T17:22:45Z",
"region": "us-west-2",
"resources": [
    "arn:aws:networkmanager::123456789012:global-network/global-network-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:111122223333:transit-gateway/tgw-1234567890abcdef0"
],
"detail": {
    "changeType": "TGW-CONNECT-PEER-CREATED",
    "changeDescription": "A TGW Connect Peer has been created in a Connect attachment.",
    "region": "us-east-1",
    "transitGatewayAttachmentArn": "arn:aws:ec2:us-east-1:111122223333:transit-gateway-attachment/tgw-attach-1234567890abcdef0",
    "connectPeerArn": "arn:aws:ec2:us-east-1:111122223333:transit-gateway-connect-peer/tgw-connect-peer-1234567890abcdef0",
    "peerAddress": "10.1.2.3",
    "transitGatewayAddress": "10.0.0.1", 111122223333
    "transitGatewayArn": "arn:aws:ec2:us-east-1:111122223333:transit-gateway/tgw-1234567890abcdef0"
    }
}
```

### A transit gateway Connect peer was deleted in

a Connect attachment (CONNECT_PEER_DELETED)

```
{
    "version": "0",
    "id": "437f664b-cc6c-ccb8-b322-2c185ebe0c10",
    "detail-type": "Network Manager Topology Change",
    "source": "aws.networkmanager",
    "account": "738040852526",
    "time": "2023-11-13T20:49:34Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:networkmanager::738040852526:global-network/global-network-02e49afd6fa01d0c3",
        "arn:aws:networkmanager::738040852526:core-network/core-network-0d6ee69cdc931f7b5"
    ],
    "detail": {
        "changeType": "CONNECT_PEER_DELETED",
        "changeDescription": "A Connect peer has been deleted in a Connect attachment.",
        "edgeLocation": "eu-west-2",
        "attachmentArn": "arn:aws:networkmanager::738040852526:attachment/attachment-05e447f0df042a011",
        "connectPeerArn": "arn:aws:networkmanager::738040852526:connect-peer/connect-peer-024b3172d38112df5",
        "coreNetworkArn": "arn:aws:networkmanager::738040852526:core-network/core-network-0d6ee69cdc931f7b5"
    }
}
```

### A Network Firewall attachment was created (NETWORK-FIREWALL-ATTACHMENT-CREATED)

```
{
    "version": "0",
    "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "detail-type": "Network Manager Topology Change",
    "source": "aws.networkmanager",
    "account": "123456789012",
    "time": "2023-01-19T18:57:29Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:networkmanager::123456789012:global-network/global-network-1234567890abcdef0",
        "arn:aws:ec2:us-east-1:123456789012:transit-gateway/tgw-1234567890abcdef0"
    ],
    "detail": {
        "changeType": "  ",
        "changeDescription": "A Network Firewall attachment has been created.",
        "region": "us-east-1",
        "transitGatewayAttachmentArn": "arn:aws:ec2:us-east-1:123456789012:transit-gateway-attachment/tgw-attach-1234567890abcdef0",
        "resourceArns":[
            "arn:aws:network-firewall:us-east-1:123456789012:firewall/arn:aws:network-firewall:us-east-1:123456789012:firewall/firewall-network-manager-event-example"
            ],
        "transitGatewayArn": "arn:aws:ec2:us-east-1:123456789012:transit-gateway/tgw-1234567890abcdef0"
    }
}
```

### A Network Firewall attachment was deleted (NETWORK-FIREWALL-ATTACHMENT-DELETED)

```
{
    "version": "0",
    "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "detail-type": "Network Manager Topology Change",
    "source": "aws.networkmanager",
    "account": "123456789012",
    "time": "2023-01-19T19:16:23Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:networkmanager::123456789012:global-network/global-network-1234567890abcdef0",
        "arn:aws:ec2:us-east-1:123456789012:transit-gateway/tgw-1234567890abcdef0"
    ],
    "detail": {
        "changeType": "NETWORK-FIREWALL-ATTACHMENT-DELETED",
        "changeDescription": "A Network Firewall attachment has been deleted.",
        "region": "us-east-1",
        "transitGatewayAttachmentArn": "arn:aws:ec2:us-east-1:123456789012:transit-gateway-attachment/tgw-attach-1234567890abcdef0",
                "resourceArns":[
            "arn:aws:network-firewall:us-east-1:123456789012:firewall/arn:aws:network-firewall:us-east-1:123456789012:firewall/firewall-network-manager-event-example"
            ],
        "transitGatewayArn": "arn:aws:ec2:us-east-1:123456789012:transit-gateway/tgw-1234567890abcdef0"
    }
}
```

## Routing update events

Routing update events occur when there have been changes to the transit gateway route
tables in your global network. These include the following:

###### Events

- [A transit gateway attachment's route
  table changed (CONNECT_PEER_DELETED)](#tgw-route-changed "#tgw-route-changed")
- [A route was created in a transit gateway
  route table (TGW-ROUTE-INSTALLED)](#tgw-route-created "#tgw-route-created")
- [A route was deleted in a
  transit gateway route table gateway (TGW-ROUTE-UNINSTALLED)](#tgw-route-uninstall "#tgw-route-uninstall")

### A transit gateway attachment's route

table changed (CONNECT_PEER_DELETED)

```
{
    "version": "0",
    "id": "437f664b-cc6c-ccb8-b322-2c185ebe0c10",
    "detail-type": "Network Manager Topology Change",
    "source": "aws.networkmanager",
    "account": "738040852526",
    "time": "2023-11-13T20:49:34Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:networkmanager::738040852526:global-network/global-network-02e49afd6fa01d0c3",
        "arn:aws:networkmanager::738040852526:core-network/core-network-0d6ee69cdc931f7b5"
    ],
    "detail": {
        "changeType": "CONNECT_PEER_DELETED",
        "changeDescription": "A Connect peer has been deleted in a Connect attachment.",
        "edgeLocation": "eu-west-2",
        "attachmentArn": "arn:aws:networkmanager::738040852526:attachment/attachment-05e447f0df042a011",
        "connectPeerArn": "arn:aws:networkmanager::738040852526:connect-peer/connect-peer-024b3172d38112df5",
        "coreNetworkArn": "arn:aws:networkmanager::738040852526:core-network/core-network-0d6ee69cdc931f7b5"
    }
}
```

### A route was created in a transit gateway

route table (TGW-ROUTE-INSTALLED)

```
{
"version": "0",
"id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
"detail-type": "Network Manager Routing Update",
"source": "aws.networkmanager",
"account": "123456789012",
"time": "2023-06-27T15:24:32Z",
"region": "us-west-2",
"resources": [
    "arn:aws:networkmanager::123456789012:global-network/global-network-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:111122223333:transit-gateway/tgw-1234567890abcdef0"
],
"detail": {
    "changeType": "TGW-ROUTE-INSTALLED",
    "changeDescription": "Routes in one or more Transit Gateway route tables have been installed.",
    "region": "us-east-1",
    "transitGatewayRouteTableArns": [
        "arn:aws:ec2:us-east-1:111122223333:transit-gateway-route-table/tgw-rtb-1234567890abcdef0"
    ],
    "sequenceNumber": 1687879467281,
    "routes": [{
        "destinationCidrBlock": "11.0.0.0/16",
        "attachments": [
            { "tgwAttachmentId": "tgw-attach-1234567890abcdef0",
              "resourceId": "vpc-1234567890abcdef0",
              "attachmentType": "vpc"
            }
            ],
        "routeType":
            "route_propagated",
            "routeState": "active",
            "propagatedRouteFamily":
                "connected" }
            ],
   "transitGatewayArn": "arn:aws:ec2:us-east-1:111122223333:transit-gateway/tgw-1234567890abcdef0"
}
```

### A route was deleted in a

transit gateway route table gateway (TGW-ROUTE-UNINSTALLED)

```
{
  "version": "0",
  "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "detail-type": "Network Manager Routing Update",
  "source": "aws.networkmanager",
  "account": "123456789012",
  "time": "2022-02-30T23:18:50Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws-us-east-1:networkmanager::123456789012:global-network/global-network-1234567890abcdef0",
    "arn:aws-us-east-1:ec2:us-east-1:111122223333:transit-gateway/tgw-1234567890abcdef0"
  ],
  "detail": {
    "changeType": "TGW-ROUTE-UNINSTALLED",
    "changeDescription": "Routes in one or more Transit Gateway route tables have been uninstalled.",
    "region": "us-east-1",
    "transitGatewayRouteTableArns": [
      "arn:aws-us-east-1:ec2:us-east-1:111122223333:transit-gateway-route-table/tgw-rtb-1234567890abcdef0"
    ],
    "sequenceNumber": 1648147298451,
    "routes": [{
      "destinationCidrBlock": "10.10.10.0/16",
      "attachments": [],
      "routeType": "route_static",
      "routeState": "blackhole"
    }
    ],
    "transitGatewayArn": "arn:aws-us-east-1:ec2:us-east-1:111122223333:transit-gateway/tgw-1234567890abcdef0"
  }
}
```

## Status update events

Status update events occur when there have been changes to the status of the
connectivity of your VPN connections in the global network. These include the
following:

###### Events

- [A VPN tunnel's IPsec session
  went down (VPN-CONNECTION-IPSEC-DOWN)](#vpn-connection-ipsec-down "#vpn-connection-ipsec-down")
- [A VPN tunnel's IPsec session went up
  (after being down) (VPN-CONNECTION-IPSEC-UP)](#vpn-connection-ipsec-up "#vpn-connection-ipsec-up")
- [A VPN tunnel's BGP session went down
  (VPN-CONNECTION-BGP-DOWN)](#vpn-connection-bgp-down "#vpn-connection-bgp-down")
- [A VPN tunnel's BGP session went
  up (after being down) (VPN-CONNECTION-BGP-ESTABLISH)](#vpn-connection-bgp-establish "#vpn-connection-bgp-establish")
- [A Connect peer (GRE tunnel) BGP
  session went down (CONNECT_PEER_BGP_DOWN)](#tgw-connect-peer-bgp-down "#tgw-connect-peer-bgp-down")
- [A Connect peer (GRE tunnel) BGP
  session went up after being down) (CONNECT_PEER_BGP_UP)](#tgw-connect-peer-bgp-up "#tgw-connect-peer-bgp-up")

### A VPN tunnel's IPsec session

went down (VPN-CONNECTION-IPSEC-DOWN)

```
{
    "version": "0",
    "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "detail-type": "Network Manager Status Update",
    "source": "aws.networkmanager",
    "account": "123456789012",
    "time": "2023-01-31T19:48:05Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:networkmanager::123456789012:global-network/global-network-1234567890abcdef0",
        "arn:aws:ec2:us-west-2:111122223333:vpn-connection/vpn-1234567890abcdef0"
     ],
    "detail": {
        "changeType": "VPN-CONNECTION-IPSEC-DOWN",
        "changeDescription": "IPsec for a VPN connection has gone down.",
        "region": "us-west-2",
        "transitGatewayAttachmentArn": "arn:aws:ec2:us-west-2:111122223333:transit-gateway-attachment/tgw-attach-1234567890abcdef0",
        "vpnConnectionArn": "arn:aws:ec2:us-west-2:111122223333:vpn-connection/vpn-1234567890abcdef0",
        "outsideIpAddress": "35.84.102.207",
        "transitGatewayArn": "arn:aws:ec2:us-west-2:111122223333:transit-gateway/tgw-1234567890abcdef0"
    }
}
```

### A VPN tunnel's IPsec session went up

(after being down) (VPN-CONNECTION-IPSEC-UP)

```
{
    "version": "0",
    "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "detail-type": "Network Manager Status Update",
    "source": "aws.networkmanager",
    "account": "123456789012",
    "time": "2023-01-31T19:34:54Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:networkmanager::123456789012:global-network/global-network-1234567890abcdef0",
        "arn:aws:ec2:us-west-2:111122223333:vpn-connection/vpn-1234567890abcdef0"
    ],
    "detail": {
        "changeType": "VPN-CONNECTION-IPSEC-UP",
        "changeDescription": "IPsec for a VPN connection has come up.",
        "region": "us-west-2",
        "transitGatewayAttachmentArn": "arn:aws:ec2:us-west-2:111122223333:transit-gateway-attachment/tgw-attach-1234567890abcdef0",
        "vpnConnectionArn": "arn:aws:ec2:us-west-2:111122223333:vpn-connection/vpn-1234567890abcdef0",
        "outsideIpAddress": "52.37.214.193",
        "transitGatewayArn": "arn:aws:ec2:us-west-2:111122223333:transit-gateway/tgw-1234567890abcdef0"
    }
}
```

### A VPN tunnel's BGP session went down

(VPN-CONNECTION-BGP-DOWN)

```
{
    "version": "0",
    "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "detail-type": "Network Manager Status Update",
    "source": "aws.networkmanager",
    "account": "123456789012",
    "time": "2023-01-31T19:48:23Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:networkmanager::123456789012:global-network/global-network-0c243052669618f74",
        "arn:aws:ec2:us-west-2:111122223333:vpn-connection/vpn-0fdb136628eff65a8"
    ],
    "detail": {
        "changeType": "VPN-CONNECTION-BGP-DOWN",
        "changeDescription": "BGP for a VPN connection has gone down.",
        "region": "us-west-2",
        "transitGatewayAttachmentArn": "arn:aws:ec2:us-west-2:111122223333:transit-gateway-attachment/tgw-attach-1234567890abcdef0",
        "vpnConnectionArn": "arn:aws:ec2:us-west-2:111122223333:vpn-connection/vpn-1234567890abcdef0",
        "outsideIpAddress": "54.190.210.71",
        "peerAsn": "65001",
        "transitGatewayArn": "arn:aws:ec2:us-west-2:111122223333:transit-gateway/tgw-1234567890abcdef0"
    }
}
```

### A VPN tunnel's BGP session went

up (after being down) (VPN-CONNECTION-BGP-ESTABLISH)

```
{
    "version": "0",
    "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "detail-type": "Network Manager Status Update",
    "source": "aws.networkmanager",
    "account": "123456789012",
    "time": "2023-01-31T19:34:40Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:networkmanager::123456789012:global-network/global-network-1234567890abcdef0",
        "arn:aws:ec2:us-west-2:111122223333:vpn-connection/vpn-1234567890abcdef0"
    ],
    "detail": {
        "changeType": "VPN-CONNECTION-BGP-ESTABLISH",
        "changeDescription": "BGP for a VPN connection has been established.",
        "region": "us-west-2",
        "transitGatewayAttachmentArn": "arn:aws:ec2:us-west-2:111122223333:transit-gateway-attachment/tgw-attach-1234567890abcdef0",
        "vpnConnectionArn": "arn:aws:ec2:us-west-2:111122223333:vpn-connection/vpn-1234567890abcdef0",
        "outsideIpAddress": "52.37.214.193",
        "peerAsn": "65001",
        "transitGatewayArn": "arn:aws:ec2:us-west-2:111122223333:transit-gateway/tgw-1234567890abcdef0"
    }
}
```

### A Connect peer (GRE tunnel) BGP

session went down (CONNECT_PEER_BGP_DOWN)

```
{
    "version": "0",
    "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "detail-type": "Network Manager Status Update",
    "source": "aws.networkmanager",
    "account": "123456789012",
    "time": "2023-03-01T19:57:34Z",
    "region": "us-west-2",
    "resources": ["arn:aws:networkmanager::123456789012:global-network/global-network-07a82dd610af0cc57", "arn:aws:networkmanager::123456789012:core-network/core-network-1234567890abcdef0"],
    "detail": {
        "changeType": "CONNECT_PEER_BGP_DOWN",
        "changeDescription": "BGP for a Connect peer has gone down.",
        "edgeLocation": "ap-southeast-1",
        "attachmentArn": "arn:aws:networkmanager::123456789012:attachment/attachment-1234567890abcdef0",
        "connectPeerArn": "arn:aws:networkmanager::123456789012:connect-peer/connect-peer-1234567890abcdef0",
        "peerAsn": "65011",
        "coreNetworkAddress": "192.0.2.0",
        "coreNetworkArn": "arn:aws:networkmanager::123456789012:core-network/core-network-1234567890abcdef0"
    }
}
```

### A Connect peer (GRE tunnel) BGP

session went up after being down) (CONNECT_PEER_BGP_UP)

```
{
    "version": "0",
    "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "detail-type": "Network Manager Status Update",
    "source": "aws.networkmanager",
    "account": "123456789012",
    "time": "2023-03-01T19:57:49Z",
    "region": "us-west-2",
    "resources": ["arn:aws:networkmanager::123456789012:global-network/global-network-07a82dd610af0cc57", "arn:aws:networkmanager::123456789012:core-network/core-network-1234567890abcdef0"],
    "detail": {
        "changeType": "CONNECT_PEER_BGP_UP",
        "changeDescription": "BGP for a Connect peer has been established.",
        "edgeLocation": "ap-southeast-1",
        "attachmentArn": "arn:aws:networkmanager::123456789012:attachment/attachment-1234567890abcdef0",
        "connectPeerArn": "arn:aws:networkmanager::123456789012:connect-peer/connect-peer-1234567890abcdef0",
        "peerAsn": "65011",
        "coreNetworkAddress": "192.0.2.0",
        "coreNetworkArn": "arn:aws:networkmanager::123456789012:core-network/core-network-1234567890abcdef0"
    }
}
```
