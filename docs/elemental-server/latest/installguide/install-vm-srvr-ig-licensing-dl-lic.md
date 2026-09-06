

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Step c: Download Licenses from the AWS Elemental User Community
<a name="install-vm-srvr-ig-licensing-dl-lic"></a>

1. Follow the instructions in [Downloading AWS Elemental Server Software](detailed-dl-srvr-ig.md) to get to the **Order Detail** page on the [AWS Elemental Support Center Activations](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations).

1. Hover over the three-bar icon on the right of the screen to bring up a small menu. Choose **License(s)**.  
![](http://docs.aws.amazon.com/elemental-server/latest/installguide/images/install-licorderdetail-shared-png.png)

1. On the **License Information** page, choose **Generate**.  
![](http://docs.aws.amazon.com/elemental-server/latest/installguide/images/install-licinfo-shared-png.png)

1. On the **Generate Licenses** page, select **Choose File** to browse to and select your `.key` file.

1. This returns you to the **Generate Licenses** page, with your `.key` file selected. Choose **Upload License Key**.  
![](http://docs.aws.amazon.com/elemental-server/latest/installguide/images/install-genlic-shared-png.png)

1. This takes you to the **View Licenses** page, where you can download a `.tgz` file. This is a compressed, aggregated file that contains all the license files that you need for this system.  
![](http://docs.aws.amazon.com/elemental-server/latest/installguide/images/install-viewlic-shared-png.png)

1. Save the `.tgz` file to a place accessible to the AWS Elemental system that will be using this license, for example, a directory on your workstation called “licenses”. Make a note of the path. 

   The files are named `lic-download-<hostname>.tgz`.

1. Repeat these steps for each virtual machine that will have AWS Elemental software.