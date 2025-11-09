This is version 2.18 of the AWS Elemental Conductor File documentation. This is the
latest version. For prior versions, see the _Archive_ section of
[AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Add Mount Points to AWS Elemental Conductor File Nodes

You might want to specify files as the input sources for jobs. You might also have assets such as scripts and image files that you want to use in jobs that are stored in a folder on a remote server.

For Conductor or a worker node to access remote files, you must mount the remote server
folder onto the node. The folder will become a “remote share”. The remote share is mounted to:
`/data/mnt/`folder``

where `folder` is a folder name that you specify and
that is then created on the node.

###### To add mount points

1. On the AWS Elemental Conductor File node, click **Nodes** in the main menu.
2. On the **Nodes** screen, choose **Edit** (wrench icon) beside the primary Conductor node.
3. On the **Node Configuration** screen, choose **Mount Points**.
4. On the **Mount Points** screen, complete the screen according to the
   following table and choose **Save**.

| Field            | Description                                                                                                                                                                                                                        |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**         | Choose the type of remote server:<br>• **CIFS**: Choose this for a Windows CIF server or for a Windows, Linux, or Mac SMB server.<br>• **NFS**: Choose this for a Linux server.<br>• **DAVFS**: Choose this for a DavFS server.    |
| **Server Share** | The address of the folder on the remote computer that you want to make<br>available on this node.                                                                                                                                  |
| **Mount Folder** | The folder on the node where the remote folder is mounted. As shown,<br>this folder must be under `/data/mnt`. You can specify a sub-subfolder;<br>if that folder does not already exist, Conductor File automatically creates it. |
| **Username**     | If the remote server folder is protected with a username/password, enter the<br>username here.                                                                                                                                     |
| **Password**     | If the remote server folder is protected with a username/password, enter the<br>password here.                                                                                                                                     |

5. Wait a few minutes. The newly mounted folder appears on the screen.
6. If you have a secondary Conductor node, switch to the web interface for that node and repeat these steps.
   The folder on the remote server is now mounted on the Conductor nodes.
