This is version 2.18 of the AWS Elemental Conductor File documentation. This is the
latest version. For prior versions, see the _Archive_ section of
[AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Step d: Install the License

Files

Now that you have a `.tgz` compressed license file for each instance of the software you are
running, you must point the software to it.

From your workstation, perform the following steps for each newly installed AWS Elemental system.

1. Navigate to the directory where you saved the `.tgz` file and unpack it.
2. Bring up the web interface for the AWS Elemental Conductor File system. From the main menu, select **Settings**
   > **Licenses**. The Licenses screen appears.
3. Select **Choose File** and navigate to the directory where you placed the license
   files. Select the file name with the hostname portion matching the hostname of this node.

![License management interface showing options to upload or update license files.](/images/elemental-cf2/latest/installguide/images/install-installlic-shared-png.png) 4. Back on the Licenses screen, choose **Update**. The license file is installed. Be sure to install each license file: `conductor.lic` and `ui.lic`. 5. Repeat steps 1 through 4 on each VM guest.

Ignore the message about the license pools.
You are setting a node-locked deployment, so you don't need a license pool (`pool.lic`).
