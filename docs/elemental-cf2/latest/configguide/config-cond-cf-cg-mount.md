

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
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-cond-cf-cg-mount.html)

1. Wait a few minutes. The newly mounted folder appears on the screen.

1. If you have a secondary Conductor node, switch to the web interface for that node and repeat these steps. 

The folder on the remote server is now mounted on the Conductor nodes.