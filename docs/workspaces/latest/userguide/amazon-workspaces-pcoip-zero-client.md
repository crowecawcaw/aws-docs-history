

# WorkSpaces PCoIP zero client
<a name="amazon-workspaces-pcoip-zero-client"></a>

You can set up and use a PCoIP zero client device with WorkSpaces. 

## Requirements
<a name="zero_client_reqs"></a>

To use a PCoIP zero client with WorkSpaces, you need the following:
+ PCoIP zero clients are compatible only with WorkSpaces that are using the PCoIP protocol.
+ Your Tera2 zero client device must have firmware version 6.0.0 or later. If your Tera2 zero client device has a firmware version between 4.6.0 and 6.0.0, your WorkSpaces administrator must upgrade your device firmware through a Desktop Access subscription at [https://www.teradici.com/products/zero-clients\#buy](https://www.teradici.com/products/zero-clients#buy).
+ WorkSpaces multi-factor authentication (MFA) requires a Tera2 zero client device with firmware version 6.0.0 or later.
+ Your WorkSpaces administrator might need to enable your zero client device to use USB printers and other USB peripheral devices. If you're having trouble using a USB printer or other USB peripheral devices, contact your WorkSpaces administrator for assistance. For more information, see [ USB printers and other USB peripherals aren't working for PCoIP zero clients](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-troubleshooting.html#pcoip_zero_client_usb) in the *Amazon WorkSpaces Administration Guide*.

For a list of approved PCoIP zero client devices, see [PCoIP Zero Clients](https://www.teradici.com/resource-center/product-service-finder/pcoip-zero-clients) on the Teradici website.

## Connect to your WorkSpace
<a name="zero_client_connect"></a>

If your zero client device has firmware version 6.0.0 or later, you can connect to your WorkSpace. If your zero client device has a firmware version between 4.6.0 and 6.0.0, your WorkSpaces administrator must upgrade your device firmware through a Desktop Access subscription at [https://www.teradici.com/desktop-access](https://www.teradici.com/desktop-access).

**To connect to your WorkSpace**

1. From the PCoIP zero client device, choose **Options**, **Configuration**, **Session**, and choose the **OSD: WorkSpaces Session Settings** connection type.

1. Enter the registration code from your welcome email.

1. Enter a name for this registered WorkSpace.

1. Choose **Connect**.

## Disconnect from the zero client
<a name="zero_client_disconnect"></a>

To disconnect the zero client from your WorkSpace, you can press Ctrl\+Alt\+F12. Alternatively, you can log off of the WorkSpace, which disconnects the client.

## IPv6 network settings
<a name="zero_client_ipv6_settings"></a>

The WorkSpaces PCoIP zero client application supports connecting to your WorkSpace via IPv4, IPv6, or dual-stack (both IPv4 and IPv6).

You can refer to the PCoIP Zero Client documentation to [configure IPv6 settings](https://anyware.hp.com/web-help/pcoip_zero_client/tera2/23.06/configuring_ipv6_settings/).

**Note**  
IPv6 connections are supported on the Zero Client firmware version `25.10` or later.
When IPv6 is enabled for a Zero client application, the system will exclusively use IPv6 networking and will not automatically switch to IPv4 if an IPv6 connection is unavailable.