

# Add mount points to Elemental Live Nodes
<a name="config-wrkr-cf-cg-mount"></a>

To make remote assets, such as scripts, image files, or video source files, available to your AWS Elemental Live nodes, create mount points as described in this section. When you mount a remote folder to a local folder on the node, all of the contents of the remote folder appear as if they are actually in the local mount folder. In this way, you can view the remote folder and verify that the backup files are created. You can also copy or delete a file from the remote folder by copying or deleting it from this mount folder.

The mount folder becomes a mount share. It's mounted to `/data/mnt/{{folder}}`.

**To create a mount**

1. On the primary Elemental Live web interface, go to the **Settings** page and choose **Mount Points**.

1. On the **Mount Points** page, complete the mount point fields as described in the following table and choose **Save**:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-live/latest/configguide/config-wrkr-cf-cg-mount.html)

The newly mounted folder appears on the node after a few minutes.