

# Add a device to an AWS Cloud WAN global network
<a name="cloudwan-devices-add"></a>

Add a device to your Cloud WAN global network. Devices can then be associated to sites using links. 

**To add a device**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Devices**.

1. Choose **Create Device**.

1. For Name and Description, enter a name and description for the device.

1. For **Model**, enter the device model number.

1. For **Serial number**, enter the serial number for the device. 

1. For **Type**, enter the device type.

1. For **Vendor**, enter the name of the vendor, for example, **Cisco**. 

1. For **Location type**, specify whether the device is located in a remote location (**On-premises, Data center/ Other Cloud Provider**) or in the **AWS Cloud**.

   If you choose **AWS Cloud**, specify the location of the device within AWS: 
   +  For the **Zone**, specify the name of an **Availability Zone**,**Local Zone**, **Wavelength Zone**, or an **Outpost**. 
   + For the **Subnet**, specify the Amazon Resource Name (ARN) of the subnet (for example, `arn:aws:ec2:useast-1:111111111111:subnet/subnet-abcd1234`).

1. For **Address**, enter the physical location of the site (for example **New York, NY 10004**).

1. For **Latitude**, enter the latitude coordinates for the site (for example, **40.7128**). 

1. For **Longitude**, enter the longitude coordinates for the site (for example, **-74.0060**).