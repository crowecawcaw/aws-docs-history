# Route traffic through an AWS Transit Gateway network

function attachment

After creating a network function attachment, you need to update your transit gateway route
tables to send traffic through the firewall for inspection using either the Amazon VPC Console or by
using the CLI. For the steps to update a transit gateway route table association, see [Associate a transit gateway route table](associate-tgw-route-table.md "associate-tgw-route-table.md").

## Route traffic through a firewall

attachment using the console

Use the Amazon VPC Console console to route traffic through a transit gateway network function
attachment.

###### To route traffic through a network function attachment using the console

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Transit Gateways**.
3. Choose **Transit gateway route tables**.
4. Select the route table you want to modify.
5. Choose **Actions**, and then choose **Create static route**.
6. For **CIDR**, enter the destination CIDR block for the route.
7. For **Attachment**, select the network function attachment. For example,
   this might be an AWS Network Firewall attachment.
8. Choose **Create static route**.

###### Note

Only static routes are supported.

Traffic matching the CIDR block in your route table will now be sent to the firewall attachment for inspection before being forwarded to its final destination.

## Route traffic through a network function attachment using

the CLI or API

Use the command line or API to route a transit gateway network function attachment.

###### To route traffic through a network function attachment using the command line or API

- Use [`create-transit-gateway-route`](../../../cli/latest/reference/create-transit-gateway-route/create-transit-gateway-route.md "../../../cli/latest/reference/create-transit-gateway-route/create-transit-gateway-route.md").

For example, the request might be to route a network firewall attachment:

```
aws ec2 create-transit-gateway-route \
  --transit-gateway-route-table-id tgw-rtb-0123456789abcdef0 \
  --destination-cidr-block 0.0.0.0/0 \
  --transit-gateway-attachment-id tgw-attach-0123456789abcdef0
```

The output then returns:

```
{
  "Route": {
    "DestinationCidrBlock": "0.0.0.0/0",
    "TransitGatewayAttachments": [
      {
        "ResourceId": "network-firewall",
        "TransitGatewayAttachmentId": "tgw-attach-0123456789abcdef0",
        "ResourceType": "network-function"
      }
    ],
    "Type": "static",
    "State": "active"
  }
}
```

Traffic matching the CIDR block in your route table will now be sent to the firewall
attachment for inspection before being forwarded to its final destination.
