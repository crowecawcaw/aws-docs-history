This is version 2.18 of the AWS Elemental Conductor File documentation. This is the
latest version. For prior versions, see the _Archive_ section of
[AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Add Mount Points to AWS Elemental Server Nodes

If you have mounted remote shares on the Conductor node or nodes, we strongly recommend that you mount the same shares on all worker nodes.

###### To add mount points

1. On the Conductor web interface, hover over **Configuration** (cog icon) on the main menu and choose **Mount Point** from the dropdown menu.

The **Conductor Configuration** screen appears showing the **Cluster Mount Point Settings** tab.

###### Important

This screen has the same fields as the Mount Points screen (where you mounted remote shares for the Conductor nodes). But it is not the same screen! 2. Complete the screen with the same information as you entered on the Mount Points screen.
The folder on the remote server will now be mounted on the worker nodes.
