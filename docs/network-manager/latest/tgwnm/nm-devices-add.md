# Add a device using AWS Network Manager

Create a device to represent a physical or virtual appliance.

###### To add a device

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, choose **Devices**. Choose
   **Create device**.
5. For **Name** and **Description**, enter
   a name and description for the device.
6. For **Model**, enter the device model number.
7. For **Serial number**, enter the serial number for the
   device.
8. For **Type**, enter the device type.
9. For **Vendor**, enter the name of the vendor, for
   example, `Cisco`.
10. For **Location type**, specify whether the device is
    located in a remote location (on-premises network, data center, or other
    cloud provider) or in AWS.

If you choose **AWS Cloud**, specify the location of
the device within AWS. For **Zone**, specify the name of
an Availability Zone, Local Zone, Wavelength Zone, or an Outpost. For
**Subnet**, specify the Amazon Resource Name (ARN) of a
subnet (for example, arn:aws:ec2:us-east-1:111111111111:subnet/subnet-abcd1234). 11. For **Address**, enter the physical address of the
site, for example, `New York, NY 10004`. 12. For **Latitude**, enter the latitude coordinates for
the site, for example, `40.7128`. 13. For **Longitude**, enter the longitude coordinates
for the site, for example, `-74.0060`. 14. Choose **Create device**.

###### Creating and viewing a device using the AWS CLI

Use the following commands:

- To create a device: [create-device](../../../cli/latest/reference/networkmanager/create-device.md "../../../cli/latest/reference/networkmanager/create-device.md")
- To view your devices: [get-devices](../../../cli/latest/reference/networkmanager/get-devices.md "../../../cli/latest/reference/networkmanager/get-devices.md")
