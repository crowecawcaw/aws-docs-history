# Delete an AWS Site-to-Site VPN Concentrator

When you no longer need a Site-to-Site VPN Concentrator, you can delete it to stop
incurring charges. Deleting a Site-to-Site VPN Concentrator permanently removes it and all associated
configurations.

## Prerequisites

Before deleting a Site-to-Site VPN Concentrator, ensure the following:

- All VPN connections associated with the Site-to-Site VPN Concentrator are deleted.
- You have the necessary permissions to delete Site-to-Site VPN Concentrators (`ec2:DeleteVpnConcentrator`).

## Delete a Site-to-Site VPN Concentrator using the

console

###### To delete a Site-to-Site VPN Concentrator

1. Open the Amazon VPC Console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Site-to-Site
   Concentrators**.
3. Select the Site-to-Site VPN Concentrator that you want to delete.
4. Choose **Actions**, and then choose **Delete Site-to-Site VPN Concentrator**.
5. In the confirmation dialog, type `delete` to confirm the deletion.
6. Choose **Delete**.

## Delete a Site-to-Site VPN Concentrator using the

CLI

Use the `delete-vpn-concentrator` command to delete a Site-to-Site VPN
Concentrator. You'll need the `vpn-concentrator-id` in order to delete
it.

The following example deletes a Site-to-Site VPN Concentrator:

```
aws ec2 delete-vpn-concentrator --vpn-concentrator-id vcn-0123456789abcdef0
```

The following response is returned:

```
{
    "VpnConcentrator": {
        "VpnConcentratorId": "vcn-0123456789abcdef0",
        "State": "deleting",
        "Message": "The Site-to-Site VPN Concentrator vcn-0123456789abcdef0 is being deleted and will be removed from your account."
    }
}
```

## Delete a Site-to-Site VPN Concentrator using the

API

Use the `DeleteVpnConcentrator` operation to delete a Site-to-Site VPN
Concentrator. You'll need the `VpnConcentratorId` in order to delete
it.

The following example deletes a Site-to-Site VPN Concentrator:

```
POST / HTTP/1.1
Host: ec2.region.amazonaws.com
Content-Type: application/x-www-form-urlencoded

Action=DeleteVpnConcentrator
&VpnConcentratorId=vcn-0123456789abcdef0
&Version=2016-11-15
```

The following response is returned:

```
<?xml version="1.0" encoding="UTF-8"?>
<DeleteVpnConcentratorResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
    <vpnConcentrator>
        <vpnConcentratorId>vcn-0123456789abcdef0</vpnConcentratorId>
        <state>deleting</state>
        <message>The Site-to-Site VPN Concentrator vcn-0123456789abcdef0 is being deleted and will be removed from your account.</message>
    </vpnConcentrator>
</DeleteVpnConcentratorResponse>
```
