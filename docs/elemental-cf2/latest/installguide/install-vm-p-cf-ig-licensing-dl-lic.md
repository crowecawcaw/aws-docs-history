This is version 2.18 of the AWS Elemental Conductor File documentation. This is the
latest version. For prior versions, see the _Archive_ section of
[AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Step c: Download Licenses from the AWS Elemental User Community

###### Important

You must perform these steps for the system that will act as the primary
AWS Elemental Conductor File node first and then for the secondary.

1. Follow the instructions in [Downloading AWS Elemental Conductor File Software](detailed-dl-cf-ig.md "detailed-dl-cf-ig.md") to get to the **Order Detail** page on the
   [AWS Elemental Support Center Activations](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations "https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations").
2. Hover over the three-bar icon on the right of the screen to bring up a small menu. Choose **License(s)**.

![Three-bar icon with dropdown menu showing "License(s)" and "Download" options.](/images/elemental-cf2/latest/installguide/images/install-licorderdetail-shared-png.png) 3. On the **License Information** page, choose **Generate**.

![Generate button highlighted on a License Information page interface.](images/install-licinfo-shared-png.png) 4. On the **Generate Licenses** page, select **Choose File** to browse to and select your `.key` file. 5. This returns you to the **Generate Licenses** page,
with your `.key` file selected. Choose **Upload License Key**.

![File upload interface with "Choose File" button and "UPLOAD LICENSE KEY" option highlighted.](images/install-genlic-shared-png.png) 6. This takes you to the **View Licenses** page, where you can download a `.tgz` file. This is a compressed, aggregated file that contains all the license files that you need for this system.

![View Licenses page showing license details and download options.](images/install-viewlic-shared-png.png) 7. Save the `.tgz` file to a place accessible to the AWS Elemental system that will be using this license, for example, a directory on your workstation called “licenses”. Make a note of the path.

The files are named `lic-download-<hostname>-primary.tgz` and `lic-download-<hostname>-secondary.tgz`. 8. Download the license files for the secondary AWS Elemental Conductor File node using
these same steps.
