

This is version 2.20 of the AWS Elemental Statmux documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Statmux and AWS Elemental Live Documentation](https://docs.aws.amazon.com/elemental-live).

# Step d: Install the License Files
<a name="install-sm-ig-licensing-lic-files"></a>

Now that you have a `.tgz` compressed license file for each instance of the software you are running, you must point the software to it.

From your workstation, perform the following steps for each newly installed AWS Elemental system.

1. Navigate to the directory where you saved the `.tgz` file and unpack it.

1. Bring up the web interface for the AWS Elemental Statmux system. From the main menu, select **Settings** > **Licenses**. The Licenses screen appears.

1. Select **Choose File** and navigate to the directory where you placed the license files. Select the file name with the hostname portion matching the hostname of this node.  
![Licenses tab showing Choose File button with no license pools currently uploaded.](http://docs.aws.amazon.com/elemental-statmux/latest/upgradeguide/images/install-installlic-shared-png.png)

1. Back on the Licenses screen, choose **Update**. The license file is installed. 

1. Repeat steps 1 through 4 on each node.