

# Create an AWS Site-to-Site VPN Concentrator
<a name="create-vpn-concentrator"></a>

Create a Concentrator using either the Amazon VPC Console, the APIs, or the AWS CLI. Before you create a Concentrator, you must first have created a transit gateway to associate with the Concentrator. For more information about creating transit gateways, see [Create a transit gateway](https://docs.aws.amazon.com/vpc/latest/tgw/create-tgw.html) in the *Amazon VPC AWS Transit Gateway Guide*.

## Create a Site-to-Site VPN Concentrator using the console
<a name="create-Concentrator-console"></a>

To create a Site-to-Site VPN Concentrator using the AWS Management Console, follow these steps:

**To create a Site-to-Site VPN Concentrator using the console**

1. Open the Amazon VPC Console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Site-to-Site VPN Concentrators**.

1. Choose **Create Site-to-Site VPN Concentrator**.

1. (Optional) For **Name tag**, enter a name for your Site-to-Site VPN Concentrator.

1. For **Transit gateway**, select an existing transit gateway.

1. (Optional) Add tags to help identify and organize your Site-to-Site VPN Concentrator.

   1. Choose **Add new tag**.

   1. For **Key**, enter a tag key (for example, **Name**).

   1. For **Value**, enter a tag value (for example, **Production-VPN-Concentrator**).

   1. Repeat the previous steps to add additional tags as needed.

1. Choose **Create Site-to-Site VPN Concentrator**.

After creation, the Site-to-Site VPN Concentrator will be in a `pending` state while it is being provisioned. Once ready, the state will change to `available` and you can begin creating VPN connections that use the Site-to-Site VPN Concentrator.

## Create a Site-to-Site VPN Concentrator using the CLI
<a name="create-Concentrator-cli"></a>

Before creating a Site-to-Site VPN Concentrator using the CLI, ensure you have the following:
+ An existing Transit Gateway in your AWS account
+ Appropriate IAM permissions to create Site-to-Site VPN Concentrators
+ The ID of the Transit Gateway you want to attach the Concentrator to

The following example creates a Site-to-Site VPN Concentrator for the specified transit gateway:

```
aws ec2 create-vpn-concentrator --transit-gateway-id tgw-123456789
```

The following shows a successful response:

```
{
    "VpnConcentrator": {
        "VpnConcentratorId": "vcn-0123456789abcdef0",
        "State": "pending",
        "TransitGatewayId": "tgw-123456789",
        "CreationTime": "2025-09-29T17:26:31.000Z",
        "Tags": []
    }
}
```

## Create a Site-to-Site VPN Concentrator using the API
<a name="create-Concentrator-api"></a>

You can create a Site-to-Site VPN Concentrator using the CreateVpnConcentrators API.

The API accepts the following key parameters:

`TransitGatewayId`  
The ID of the Transit Gateway to attach the Site-to-Site VPN Concentrator to.

`TagSpecification`  
Tags to assign to the Site-to-Site VPN Concentrator for resource organization and billing.

The following example shows how to create a Site-to-Site VPN Concentrator attached to a Transit Gateway:

```
POST / HTTP/1.1
Host: ec2.us-east-1.amazonaws.com
Content-Type: application/x-www-form-urlencoded
Authorization: AWS4-HMAC-SHA256 Credential=...

Action=CreateVpnConcentrator
&Version=2016-11-15
&TransitGatewayId=tgw-0123456789abcdef0
&TagSpecification.1.ResourceType=vpn-concentrator
&TagSpecification.1.Tag.1.Key=Name
&TagSpecification.1.Tag.1.Value=MyVpnConcentrator
```

Upon successful creation, the API returns details about the newly created Site-to-Site VPN Concentrator:

```
<?xml version="1.0" encoding="UTF-8"?>
<CreateVpnConcentratorResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>12345678-1234-1234-1234-123456789012</requestId>
    <vpnConcentrator>
        <vpnConcentratorId>vcn-0123456789abcdef0</vpnConcentratorId>
        <state>pending</state>
        <transitGatewayId>tgw-0123456789abcdef0</transitGatewayId>
        <creationTime>2024-01-15T10:30:00.000Z</creationTime>
        <tagSet>
            <item>
                <key>Name</key>
                <value>MyVpnConcentrator</value>
            </item>
        </tagSet>
    </vpnConcentrator>
</CreateVpnConcentratorResponse>
```