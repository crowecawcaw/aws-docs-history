

# Create, modify, and delete a network function attachment of type Gateway Load Balancer

Create and manage a network function attachment of type Gateway Load Balancer on your transit gateway. Only the transit gateway owner can create, modify, or delete this attachment. The attachment connects the transit gateway to the Gateway Load Balancer VPC endpoint service that fronts the firewall deployment. In Amazon VPC Console, the attachment appears with a type of **Network function**.

**Topics**
+ [Prerequisites](#prereq-nf-attachment-gwlb)
+ [Create the attachment](#create-nf-attachment-gwlb)
+ [Modify the attachment](#modify-nf-attachment-gwlb)
+ [Delete the attachment](#delete-nf-attachment-gwlb)

## Prerequisites
<a name="prereq-nf-attachment-gwlb"></a>

Before you create the attachment, you must have a Gateway Load Balancer with healthy appliance targets and a VPC endpoint service that fronts the security appliance deployment.

If the transit gateway and endpoint service are in different AWS accounts, the endpoint service owner must allow the transit gateway owner's account to connect. Use the `modify-vpc-endpoint-service-permissions` command with the `transit-gateway-attachment` permission type. This permission type supports only an AWS account principal, specified using its root ARN. For more information, see [Manage permissions](https://docs.aws.amazon.com/vpc/latest/privatelink/configure-endpoint-service.html#add-remove-permissions) in the *AWS PrivateLink Guide*.

```bash
aws ec2 modify-vpc-endpoint-service-permissions \
  --service-id <vpce-svc-id> \
  --permission-type transit-gateway-attachment \
  --add-allowed-principals arn:aws:iam::<account-id>:root
```

The following additional requirements apply:
+ Encryption Support must be disabled on the transit gateway. If the transit gateway encryption state is `enabled`, `enabling`, or `disabling`, the create request is rejected. For more information, see [Encryption Support](tgw-encryption-support.md).
+ The principal that creates the attachment must have permission to call `ec2:DescribeVpcEndpointServices`. The create operation uses this permission to validate access to the endpoint service.
+ The Availability Zone `use1-az3` is not supported. Specify a supported Availability Zone instead.
+ There is no separate quota for network function attachments of type Gateway Load Balancer. They count toward the quota for transit gateway attachments.

## Create a network function attachment of type Gateway Load Balancer
<a name="create-nf-attachment-gwlb"></a>

Create the attachment by specifying the transit gateway, Gateway Load Balancer VPC endpoint service, and up to 16 Availability Zones. Transit Gateway creates one Gateway Load Balancer endpoint in each Availability Zone you select.

**To create the attachment using the console**

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc/home#TransitGatewayAttachments).

1. In the navigation pane, choose **Transit Gateways**.

1. Choose **Transit gateway attachments**.

1. Choose **Create transit gateway attachment**.

1. For **Transit gateway ID**, choose the transit gateway for the attachment.

1. For **Attachment type**, choose **Network function**.

1. For **Service name**, choose the Gateway Load Balancer VPC endpoint service.

1. Select one or more Availability Zones.

1. Choose **Create transit gateway attachment**.

1. Wait until the attachment reaches the `available` state. If the endpoint service requires acceptance, the attachment remains in `pendingAcceptance` until the endpoint service owner accepts the connection.

**To create the attachment using the AWS CLI or API**  
Use `create-transit-gateway-network-function-attachment`. Specify Availability Zones by name with `--availability-zones`, by ID with `--availability-zone-ids`, or by using both options. The following example uses Availability Zone IDs.

```bash
aws ec2 create-transit-gateway-network-function-attachment \
  --transit-gateway-id tgw-0123456789abcdef0 \
  --service-name <gwlb-endpoint-service-name> \
  --availability-zone-ids <az-id-1> <az-id-2>
```

To specify the Availability Zones by name, use `--availability-zones`.

```bash
aws ec2 create-transit-gateway-network-function-attachment \
  --transit-gateway-id tgw-0123456789abcdef0 \
  --service-name <gwlb-endpoint-service-name> \
  --availability-zones <az-name-1> <az-name-2>
```

**Note**  
Each Availability Zone must be supported by both the transit gateway and endpoint service. The create request is rejected if the endpoint service is not accessible or an Availability Zone is not supported.

If the endpoint service requires acceptance, the endpoint service owner must accept the endpoint connection before the attachment becomes active. For more information, see [Accept or reject a transit gateway network function attachment](accept-reject-firewall-attachment.md).

## Modify a network function attachment of type Gateway Load Balancer
<a name="modify-nf-attachment-gwlb"></a>

Add or remove Availability Zones while the attachment is in the `available` state. Specify at least one Availability Zone to add or remove, and keep at least one Availability Zone in the attachment. You can't add and remove the same Availability Zone in one request. Each Availability Zone you add must be supported by both the transit gateway and endpoint service.

When you add an Availability Zone, Transit Gateway creates a Gateway Load Balancer endpoint in that Availability Zone. When you remove an Availability Zone, Transit Gateway removes the endpoint that it created there.

**To modify the attachment using the console**

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc/home#TransitGatewayAttachments).

1. In the navigation pane, choose **Transit Gateways**.

1. Choose **Transit gateway attachments**.

1. Select the network function attachment that you want to modify. The attachment has a type of **Network function**.

1. Choose **Actions**, and then choose **Modify transit gateway attachment**.

1. For **Availability Zones**, add or remove Availability Zones. To remove an Availability Zone, choose **Remove Availability Zone**.

1. Choose **Modify transit gateway attachment**.

1. Wait until the attachment returns to the `available` state.

**To modify the attachment using the AWS CLI or API**  
Use `modify-transit-gateway-network-function-attachment`. To add Availability Zones, use `--add-availability-zones` or `--add-availability-zone-ids`. To remove Availability Zones, use `--remove-availability-zones` or `--remove-availability-zone-ids`.

```bash
aws ec2 modify-transit-gateway-network-function-attachment \
  --transit-gateway-attachment-id tgw-attach-0123456789abcdef0 \
  --add-availability-zone-ids <az-id-1> \
  --remove-availability-zone-ids <az-id-2>
```

**Note**  
If the endpoint service does not accept connection requests automatically, the endpoint service owner must accept the new endpoint connection created for each Availability Zone that you add. For more information, see [Accept or reject a transit gateway network function attachment](accept-reject-firewall-attachment.md).

While the attachment is being modified, it is in the `modifying` state. If an Availability Zone is not supported, the attachment enters the `rollingBack` state, restores its previous configuration, and returns to `available`.

## Delete a network function attachment of type Gateway Load Balancer
<a name="delete-nf-attachment-gwlb"></a>

Delete an attachment that is in the `available` or `pendingAcceptance` state. Traffic no longer passes through the Gateway Load Balancer and its firewall appliances for inspection. Transit Gateway removes the Gateway Load Balancer endpoints that it created for the attachment.

Before deleting the attachment, remove or replace transit gateway routes that target it. If the routes remain, they enter the `blackhole` state and matching traffic is dropped.

**Note**  
For an AWS Network Firewall attachment, don't delete the attachment from the transit gateway. Delete the firewall in AWS Network Firewall, which removes the attachment.

**To delete the attachment using the console**

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc/home#TransitGatewayAttachments).

1. In the navigation pane, choose **Transit Gateways**.

1. Choose **Transit gateway attachments**.

1. Select the network function attachment that you want to delete. The attachment has a type of **Network function**.

1. Choose **Actions**, and then choose **Delete transit gateway attachment**.

1. When prompted for confirmation, enter **delete** and choose **Delete**.

**To delete the attachment using the AWS CLI or API**  
Use `delete-transit-gateway-network-function-attachment`.

```bash
aws ec2 delete-transit-gateway-network-function-attachment \
  --transit-gateway-attachment-id <attachment-id>
```