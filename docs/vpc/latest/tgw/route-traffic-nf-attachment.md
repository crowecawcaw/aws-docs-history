

# Route traffic through an AWS Transit Gateway network function attachment

After creating a network function attachment, associate it with a transit gateway route table and create static routes that send traffic to the attachment for inspection. Route propagation from a network function attachment is not supported. For information about route table associations, see [Associate a transit gateway route table](associate-tgw-route-table.md).

## Route traffic through a network function attachment using the console
<a name="route-nf-attachment-console"></a>

Use Amazon VPC Console to route traffic through a transit gateway network function attachment.

**To route traffic through a network function attachment using the console**

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc/home#TransitGatewayRouteTables).

1. In the navigation pane, choose **Transit Gateways**.

1. Choose **Transit gateway route tables**.

1. Select the route table you want to modify.

1. Choose **Actions**, and then choose **Create static route**.

1. For **CIDR**, enter the destination CIDR block for the route.

1. For **Attachment**, select the network function attachment. For example, this might be an AWS Network Firewall attachment.

1. Choose **Create static route**.
**Note**  
Only static routes are supported.

Traffic matching the CIDR block is sent to the network function attachment for inspection.

## Route traffic through a network function attachment using the CLI or API
<a name="route-nf-attachment-cli-steps"></a>

Use the AWS CLI or API to route traffic through a transit gateway network function attachment.

**To route traffic through a network function attachment using the command line or API**
+ Use [`create-transit-gateway-route`](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-transit-gateway-route.html).

  The following example routes traffic to a network function attachment of type AWS Network Firewall:

  ```bash
  aws ec2 create-transit-gateway-route \
    --transit-gateway-route-table-id tgw-rtb-0123456789abcdef0 \
    --destination-cidr-block 0.0.0.0/0 \
    --transit-gateway-attachment-id tgw-attach-0123456789abcdef0
  ```

  The output then returns:

  ```json
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

Traffic matching the CIDR block is sent to the network function attachment for inspection.