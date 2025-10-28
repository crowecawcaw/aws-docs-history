# Configure ENA Express settings for your EC2

instance

You can configure ENA Express for supported EC2 instance types without needing to
install any additional software. For more information, see [Supported instance types for ENA
Express](ena-express.md#ena-express-supported-instance-types "ena-express.md#ena-express-supported-instance-types").

Console

###### To manage ENA Express for a network interface

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the left navigation pane, choose **Network
   interfaces**.
3. Select a network interface that is attached to an instance. You
   can choose the **Network interface ID** link to
   open the detail page, or you can select the checkbox on the left side of the list.
4. Choose **Manage ENA Express** from the
   **Action** menu at the top right side of the
   page. This opens the **Manage ENA Express** dialog,
   with the selected network interface ID and current settings
   displayed.

If the network interface you selected is not attached to an
instance, this action does not appear in the menu. 5. To use **ENA Express**, select the
**Enable** checkbox. 6. When ENA Express is enabled, you can configure UDP settings. To
use **ENA Express UDP**, select the
**Enable** checkbox. 7. To save your settings, choose **Save**.

###### To manage ENA Express for an instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the left navigation pane, choose
   **Instances**.
3. Select the instance that you want to manage. You can choose the
   **Instance ID** to open the detail page,
   or you can select the checkbox on the left side of the list.
4. Select the **Network interface** to configure for
   your instance.
5. Choose **Manage ENA Express** from the
   **Action** menu at the top right side of the
   page.
6. To configure ENA Express for a network interface that's attached
   to your instance, select it from the **Network
   interface** list.
7. To use **ENA Express** for the selected network
   interface attachment, select the **Enable**
   checkbox.
8. When ENA Express is enabled, you can configure UDP settings. To
   use **ENA Express UDP**, select the
   **Enable** checkbox.
9. To save your settings, choose **Save**.

###### To configure ENA Express when you attach a network interface

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the left navigation pane, choose **Network
   interfaces**.
3. Select a network interface that is not attached to an instance
   (**Status** is **Available**).
   You can choose the **Network interface ID** link to
   open the detail page, or you can select the checkbox on the left side of the list.
4. Select the **Instance** that you'll attach
   to.
5. To use **ENA Express** after you attach the
   network interface to the instance, select the
   **Enable** checkbox.
6. When ENA Express is enabled, you can configure UDP settings. To
   use **ENA Express UDP**, select the
   **Enable** checkbox.
7. To attach the network interface to the instance and save your ENA
   Express settings, choose **Attach**.

AWS CLI

###### To configure ENA Express when you attach a network interface

Use the [attach-network-interface](../../../cli/latest/reference.md "../../../cli/latest/reference.md") command, as
shown in the following examples.

###### Example 1: Use ENA Express for TCP traffic, but not UDP

traffic

This example configures `EnaSrdEnabled` as
`true`, and allows `EnaSrdUdpEnabled` to
default to `false`.

```
aws ec2 attach-network-interface \
    --network-interface-id `eni-1234567890abcdef0` \
    --instance-id `i-1234567890abcdef0` \
    --device-index 1 \
    --ena-srd-specification 'EnaSrdEnabled=true'
```

###### Example 2: Use ENA Express for both TCP traffic and UDP

traffic

This example configures both `EnaSrdEnabled` and
`EnaSrdUdpEnabled` as `true`.

```
aws ec2 attach-network-interface \
    --network-interface-id `eni-1234567890abcdef0` \
    --instance-id `i-1234567890abcdef0` \
    --device-index 1 \
    --ena-srd-specification 'EnaSrdEnabled=true,EnaSrdUdpSpecification={EnaSrdUdpEnabled=true}'
```

###### To update ENA Express settings for a network interface

attachment

Use the [modify-network-interface-attribute](../../../cli/latest/reference/modify-network-interface-attribute.md "../../../cli/latest/reference/modify-network-interface-attribute.md")
command as shown in the following examples.

###### Example 1: Use ENA Express for TCP traffic, but not UDP

traffic

This example configures `EnaSrdEnabled` as
`true`, and allows `EnaSrdUdpEnabled` to
default to `false` if it has never been set
previously.

```
aws ec2 modify-network-interface-attribute \
    --network-interface-id `eni-1234567890abcdef0` \
    --ena-srd-specification 'EnaSrdEnabled=true'
```

###### Example 2: Use ENA Express for both TCP traffic and UDP

traffic

This example configures both `EnaSrdEnabled` and
`EnaSrdUdpEnabled` as `true`.

```
aws ec2 modify-network-interface-attribute \
    --network-interface-id `eni-1234567890abcdef0` \
    --ena-srd-specification 'EnaSrdEnabled=true,EnaSrdUdpSpecification={EnaSrdUdpEnabled=true}'
```

###### Example 3: Stop using ENA Express for UDP traffic

This example configures `EnaSrdUdpEnabled` as
`false`.

```
aws ec2 modify-network-interface-attribute \
    --network-interface-id `eni-1234567890abcdef0` \
    --ena-srd-specification 'EnaSrdUdpSpecification={EnaSrdUdpEnabled=false}'
```

PowerShell

###### To configure ENA Express when you attach a network interface

Use the [Add-EC2NetworkInterface](../../../powershell/latest/reference/items/Add-EC2NetworkInterface.md "../../../powershell/latest/reference/items/Add-EC2NetworkInterface.md") cmdlet as shown
in the following examples.

###### Example 1: Use ENA Express for TCP traffic, but not UDP

traffic

This example configures `EnaSrdEnabled` as
`true`, and allows `EnaSrdUdpEnabled` to
default to `false`.

```
Add-EC2NetworkInterface `
    -NetworkInterfaceId `eni-1234567890abcdef0` `
    -InstanceId `i-1234567890abcdef0` `
    -DeviceIndex `1` `
    -EnaSrdSpecification_EnaSrdEnabled $true
```

###### Example 2: Use ENA Express for both TCP traffic and UDP

traffic

This example configures both `EnaSrdEnabled` and
`EnaSrdUdpEnabled` as `true`.

```
Add-EC2NetworkInterface `
    -NetworkInterfaceId `eni-1234567890abcdef0` `
    -InstanceId `i-1234567890abcdef0` `
    -DeviceIndex `1` `
    -EnaSrdSpecification_EnaSrdEnabled $true `
    -EnaSrdUdpSpecification_EnaSrdUdpEnabled $true
```

###### To configure ENA Express settings for your network interface

attachment

Use the [Edit-EC2NetworkInterfaceAttribute](../../../powershell/latest/reference/items/Edit-EC2NetworkInterfaceAttribute.md "../../../powershell/latest/reference/items/Edit-EC2NetworkInterfaceAttribute.md") cmdlet
as shown in the following examples.

###### Example 1: Use ENA Express for TCP traffic, but not UDP

traffic

This example configures `EnaSrdEnabled` as
`true`, and allows `EnaSrdUdpEnabled` to
default to `false` if it has never been set
previously.

```
Edit-EC2NetworkInterfaceAttribute `
    -NetworkInterfaceId `eni-1234567890abcdef0` `
    -EnaSrdSpecification_EnaSrdEnabled $true ;
Get-EC2NetworkInterface -NetworkInterfaceId eni-`0123f4567890a1b23` | `
Select-Object `
    NetworkInterfaceId,
    @{Name = 'EnaSrdEnabled'; Expression = { $_.Attachment.EnaSrdSpecification.EnaSrdEnabled }},
    @{Name = 'EnaSrdUdpEnabled'; Expression = { $_.Attachment.EnaSrdSpecification.EnaSrdUdpSpecification.EnaSrdUdpEnabled }} | `
Format-List
```

###### Example 2: Use ENA Express for both TCP traffic and UDP

traffic

This example configures both `EnaSrdEnabled` and
`EnaSrdUdpEnabled` as `true`.

```
Edit-EC2NetworkInterfaceAttribute `
    -NetworkInterfaceId `eni-1234567890abcdef0` `
    -EnaSrdSpecification_EnaSrdEnabled $true `
    -EnaSrdSpecification_EnaSrdUdpSpecification_EnaSrdUdpEnabled $true ;
Get-EC2NetworkInterface -NetworkInterfaceId `eni-1234567890abcdef0` | `
Select-Object `
    NetworkInterfaceId,
    @{Name = 'EnaSrdEnabled'; Expression = { $_.Attachment.EnaSrdSpecification.EnaSrdEnabled }},
    @{Name = 'EnaSrdUdpEnabled'; Expression = { $_.Attachment.EnaSrdSpecification.EnaSrdUdpSpecification.EnaSrdUdpEnabled }} | `
Format-List
```

###### Example 3: Stop using ENA Express for UDP traffic

This example configures `EnaSrdUdpEnabled` as
`false`.

```
Edit-EC2NetworkInterfaceAttribute `
    -NetworkInterfaceId eni-`0123f4567890a1b23` `
    -EnaSrdSpecification_EnaSrdUdpSpecification_EnaSrdUdpEnabled $false ;
Get-EC2NetworkInterface -NetworkInterfaceId eni-`0123f4567890a1b23` | `
Select-Object `
    NetworkInterfaceId,
    @{Name = 'EnaSrdEnabled'; Expression = { $_.Attachment.EnaSrdSpecification.EnaSrdEnabled }},
    @{Name = 'EnaSrdUdpEnabled'; Expression = { $_.Attachment.EnaSrdSpecification.EnaSrdUdpSpecification.EnaSrdUdpEnabled }} | `
Format-List
```

## Configure ENA Express at

launch

You can use one of the following methods to configure ENA Express directly when
you launch an instance. The specified links refer you to the AWS Management Console instructions
for these methods.

- **Launch instance wizard** – You can
  configure ENA Express at launch with the launch instance wizard. For more
  information, see **Advanced network
  configuration** in the [Network settings](ec2-instance-launch-parameters.md#liw-network-settings "ec2-instance-launch-parameters.md#liw-network-settings") for the launch instance
  wizard.
- **Launch template** – You can configure
  ENA Express at launch when you use a launch template. For more information,
  see the [Create an Amazon EC2 launch template](create-launch-template.md "create-launch-template.md") page, then expand the **Network settings** section and review the **Advanced network configuration**.
