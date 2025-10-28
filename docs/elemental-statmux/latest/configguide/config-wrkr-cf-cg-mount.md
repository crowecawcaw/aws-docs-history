This is version 2.20 of the AWS Elemental Statmux documentation.
This is the latest version. For prior versions, see the
_Previous Versions_ section of [AWS Elemental Statmux
and AWS Elemental Live Documentation](../../../elemental-live.md "../../../elemental-live.md").

# Add Mount Points to AWS Elemental Statmux Nodes

To make remote assets, such as scripts, image files, or video source files, available to
your AWS Elemental Statmux nodes, create mount points as described in this section. When you mount a
remote folder to a local folder on the node, all of the contents of the remote folder appear as
if they are actually in the local mount folder. In this way, you can view the remote folder and
verify that the backup files are created. You can also copy or delete a file from the remote
folder by copying or deleting it from this mount folder.

The mount folder becomes a mount share. It's mounted to
`/data/mnt/`folder``.

###### To create a mount

1. On the AWS Elemental Statmux web interface, go to the **Settings** page and
   choose **Mount Points**.
2. On the **Mount Points** page, complete the mount point fields as described in the following table and choose **Save**:

| Field            | Description                                                                                                                                                                                                                        |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **Type**         | Choose the type of remote server: <br>• **CIFS**: Choose this for a Windows CIF server or for a Windows, Linux, or Mac SMB server. <br>• **NFS**: Choose this for a Linux server. <br>• **DAVFS**: Choose this for a DavFS server. |
| **Server Share** | The address of the folder on the remote computer that you want to make available on this node.                                                                                                                                     |
| **Mount Folder** | The folder on the node where the remote folder is mounted. As shown, this folder must be under `/data/mnt`. You can specify a sub-subfolder; if that folder does not already exist, Statmux automatically creates it.              |
| **Username**     | If the remote server folder is protected with a username/password, enter the username here.                                                                                                                                        |
| **Password**     | If the remote server folder is protected with a username/password, enter the password here.                                                                                                                                        | The newly mounted folder appears on the node after a few minutes. |
