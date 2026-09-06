

This is version 2.18 of the AWS Elemental Conductor File documentation. This is the latest version. For prior versions, see the *Archive* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server).

# Step d: Install the License Files
<a name="install-cf-ig-licensing-lic-files"></a>

Now that you have a `.tgz` compressed license file for each instance of the software you are running, you must point the software to it.

From your workstation, perform the following steps for each newly installed AWS Elemental system.

1. Navigate to the directory where you saved the `.tgz` file and unpack it.

1. Bring up the web interface for the AWS Elemental Conductor File system. From the main menu, select **Settings** > **Licenses**. The Licenses screen appears.

1. Select **Choose File** and navigate to the directory where you placed the license files. Select the file name with the hostname portion matching the hostname of this node.  
![License management interface showing options to upload or update license files.](http://docs.aws.amazon.com/elemental-cf2/latest/installguide/images/install-installlic-shared-png.png)

1. Back on the Licenses screen, choose **Update**. The license file is installed. 

1. Repeat steps 1 through 4 on each node.

   Ignore the message about the license pools. You are setting a node-locked deployment, so you don't need a license pool (`pool.lic`).