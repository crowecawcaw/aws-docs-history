# Adding mount points to worker

nodes

Create mount points if you need to make remote assets available on the
Conductor Live cluster. Remote assets include scripts, image files, and video source
files.

The mount folder becomes a mount share. It's mounted to
`/data/mnt/`folder``.

**Where to perform the configuration**

Make sure you perform the configuration on the correct nodes.

| Node                          | Work on this node? |
| ----------------------------- | ------------------ |
| Primary Conductor Live node   | Yes                |
| Secondary Conductor Live node | No                 |
| Each worker node              | Typically no.      |

**How mount points work**

When you mount a remote folder to a local folder on the node, all of the
contents of the remote folder appear as if they are actually in the local
mount folder. In this way, you can view the remote folder and verify that
the backup files are created. You can also copy or delete a file from the
remote folder by copying or deleting it from this mount folder.

**About synchronization**

Mount points on the primary Conductor node automatically synchronize to
the secondary Conductor Live node and worker nodes. The sync occurs within one hour
for nodes that are already part of the cluster when the mount is created.
For nodes added to a cluster with existing mount points, the sync occurs
within three minutes.

**Creating mount points on a worker
node**

Generally, there is no need to create mount points on a worker node.
Create them here if you want only one worker node to work with the folder,
perhaps for security reasons.

To create the mount point, you must use the CLI. Mount points you create
using the worker web interface are overwritten the next time that the
primary Conductor Live synchronizes data on all the nodes.

###### To create a mount

1. On the web interface of the primary Conductor Live node, go to the
   **Settings** page and choose **Mount
   Points**.
2. On the **Mount Points** page, choose **Add
   Mount Point**, complete the mount point fields as described
   in the following table, and choose **Create**.

| Field            | Description                                                                                                                                                                                                                              |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**         | Choose the type of remote server:<br>• **CIFS**: Choose this for a Windows CIF<br>server or for a Windows, Linux, or Mac SMB server.<br>• **NFS**: Choose this for a Linux<br>server.<br>• **DAVFS**: Choose this for a DavFS<br>server. |
| **Server Share** | The address of the folder that you want to make available on<br>this node. This is an address on the remote computer.                                                                                                                    |
| **Mount Folder** | The folder on the node where the remote folder is mounted. As<br>shown, this folder must be under `/data/mnt`. You can<br>specify a sub-subfolder; if that folder does not already exist,<br>Conductor Live automatically creates it.    |
| **User name**    | If the remote server folder is protected with user<br>credentials, enter the username here.                                                                                                                                              |
| **Password**     | If the remote server folder is protected with a user<br>credentials, enter the password here.                                                                                                                                            |

After a few minutes, the newly mounted folder appears on the web
interface.
