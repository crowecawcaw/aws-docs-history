

# Adding mount points to worker nodes
<a name="config-wrkr-cf-config-mount"></a>

Create mount points if you need to make remote assets available on the Conductor Live cluster. Remote assets include scripts, image files, and video source files. 

The mount folder becomes a mount share. It's mounted to `/data/mnt/{{folder}}`.

**Where to perform the configuration**

Make sure you perform the configuration on the correct nodes.



| Node | Work on this node? | 
| --- | --- | 
| Primary Conductor Live node | Yes | 
| Secondary Conductor Live node | No | 
| Each worker node | Typically no.  | 

**How mount points work**

When you mount a remote folder to a local folder on the node, all of the contents of the remote folder appear as if they are actually in the local mount folder. In this way, you can view the remote folder and verify that the backup files are created. You can also copy or delete a file from the remote folder by copying or deleting it from this mount folder.

**About synchronization**

Mount points on the primary Conductor node automatically synchronize to the secondary Conductor Live node and worker nodes. The sync occurs within one hour for nodes that are already part of the cluster when the mount is created. For nodes added to a cluster with existing mount points, the sync occurs within three minutes.

**Creating mount points on a worker node**

Generally, there is no need to create mount points on a worker node. Create them here if you want only one worker node to work with the folder, perhaps for security reasons. 

To create the mount point, you must use the CLI. Mount points you create using the worker web interface are overwritten the next time that the primary Conductor Live synchronizes data on all the nodes.

**To create a mount**

1. On the web interface of the primary Conductor Live node, go to the **Settings** page and choose **Mount Points**.

1. On the **Mount Points** page, choose **Add Mount Point**, complete the mount point fields as described in the following table, and choose **Create**.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-wrkr-cf-config-mount.html)

After a few minutes, the newly mounted folder appears on the web interface.