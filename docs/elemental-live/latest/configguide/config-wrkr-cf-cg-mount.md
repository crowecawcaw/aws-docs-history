

# Add mount points to Elemental Live Nodes
<a name="config-wrkr-cf-cg-mount"></a>

To make remote assets, such as scripts, image files, or video source files, available to your AWS Elemental Live nodes, create mount points as described in this section. When you mount a remote folder to a local folder on the node, all of the contents of the remote folder appear as if they are actually in the local mount folder. In this way, you can view the remote folder and verify that the backup files are created. You can also copy or delete a file from the remote folder by copying or deleting it from this mount folder.

The mount folder becomes a mount share. It's mounted to `/data/mnt/{{folder}}`.

**To create a mount**

1. On the primary Elemental Live web interface, go to the **Settings** page and choose **Mount Points**.

1. On the **Mount Points** page, complete the mount point fields as described in the following table and choose **Save**:



<table>
<thead>
  <tr><th>Field</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><b>Type</b></td><td>Choose the type of remote server:<ul><li><b>CIFS</b>: Choose this for a Windows CIF server or for a Windows, Linux, or Mac SMB server.</li><li><b>NFS</b>: Choose this for a Linux server.</li><li><b>DAVFS</b>: Choose this for a DavFS server.</li></ul></td></tr>
  <tr><td><b>Server Share</b></td><td>The address of the folder on the remote computer that you want to make available on this node.</td></tr>
  <tr><td><b>Mount Folder</b></td><td>The folder on the node where the remote folder is mounted. As shown, this folder must be under <code>/data/mnt</code>. You can specify a sub-subfolder; if that folder does not already exist, Elemental Live automatically creates it.</td></tr>
  <tr><td><b>Username</b></td><td>If the remote server folder is protected with a username/password, enter the username here.</td></tr>
  <tr><td><b>Password</b></td><td>If the remote server folder is protected with a username/password, enter the password here.</td></tr>
</tbody>
</table>


The newly mounted folder appears on the node after a few minutes.