

This is version 2.18 of the AWS Elemental Conductor File documentation. This is the latest version. For prior versions, see the *Archive* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server).

# Add Mount Points to AWS Elemental Conductor File Nodes
<a name="config-cond-cf-cg-mount"></a>

You might want to specify files as the input sources for jobs. You might also have assets such as scripts and image files that you want to use in jobs that are stored in a folder on a remote server. 

For Conductor or a worker node to access remote files, you must mount the remote server folder onto the node. The folder will become a “remote share”. The remote share is mounted to: `/data/mnt/{{folder}}`

where `{{folder}}` is a folder name that you specify and that is then created on the node.

**To add mount points**

1. On the AWS Elemental Conductor File node, click **Nodes** in the main menu.

1. On the **Nodes** screen, choose **Edit** (wrench icon) beside the primary Conductor node.

1. On the **Node Configuration** screen, choose **Mount Points**.

1. On the **Mount Points** screen, complete the screen according to the following table and choose **Save**.



<table>
<thead>
  <tr><th>Field</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><b>Type</b></td><td>Choose the type of remote server:<ul><li><b>CIFS</b>: Choose this for a Windows CIF server or for a Windows, Linux, or Mac SMB server.</li><li><b>NFS</b>: Choose this for a Linux server.</li><li><b>DAVFS</b>: Choose this for a DavFS server.</li></ul></td></tr>
  <tr><td><b>Server Share</b></td><td>The address of the folder on the remote computer that you want to make available on this node.</td></tr>
  <tr><td><b>Mount Folder</b></td><td>The folder on the node where the remote folder is mounted. As shown, this folder must be under <code>/data/mnt</code>. You can specify a sub-subfolder; if that folder does not already exist, Conductor File automatically creates it.</td></tr>
  <tr><td><b>Username</b></td><td>If the remote server folder is protected with a username/password, enter the username here.</td></tr>
  <tr><td><b>Password</b></td><td>If the remote server folder is protected with a username/password, enter the password here.</td></tr>
</tbody>
</table>


1. Wait a few minutes. The newly mounted folder appears on the screen.

1. If you have a secondary Conductor node, switch to the web interface for that node and repeat these steps. 

The folder on the remote server is now mounted on the Conductor nodes.