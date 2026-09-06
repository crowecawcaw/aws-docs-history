

# Create the nodes
<a name="emla-setup-cl-nodes-create"></a>

Create all the nodes for one cluster. Create them after you've created the cluster, and after you've finalized the cluster and network configurations. 

**Important**  
You won't be able to modify the network after you've added nodes to any cluster associated with the network.

To create a node, you create a node registration script then run the script on each node hardware unit. You then run the script on each hardware unit. 

## Prepare the node hardware
<a name="emla-setup-cl-nodes-hardware"></a>

You should have already obtained the hardware for the MediaLive Anywhere nodes. 

Install the RHEL 9.5 operating system on each node. RHEL 9.5 is the only supported version.

## Create the node registration script
<a name="emla-setup-cl-nodes-add"></a>

1. In the navigation bar, choose MediaLive Anywhere, then choose **Clusters**. In the list of clusters, select the name of the cluster where you want to add the nodes. The **Details** page appears.

1. Scroll down and select the **Nodes** tab. Choose **Create node**. 

1. In the **Create node** page, complete the following fields. The script uses the values that you enter here.
   + **Name**: The name that you want to permanently assign to this node. 
   + **Node role**: Choose **Active** or **Backup**. You should have identified these roles when you [designed the cluster](emla-deploy-design-cluster.md#emla-deploy-design-organize-cluster).
   + **Node interface mappings**: Create the mappings that you identified in [Designing mappings for node interfaces](emla-design-mappings.md).

1. Choose **Create**.

1. Scroll to the top of the page on the Console. If the request to add the node has succeeded, the banner displays a message and the contents of the registration script. 

1. Choose **Copy script** to copy the script to the clipboard on the computer where you are using the Console. Then go to the next step to run the script.

## Activate the node
<a name="emla-setup-cl-nodes-activate"></a>

You must run the node registration script within 24 hours of the script's creation. You must run each script on only one node because the script includes data such as a node name that must be unique in the cluster of nodes.

1. Start an SSH session on the node.

1. At the prompt, paste the node registration script for this node and press **Enter**. The script performs the following actions:
   + It binds the node identity (that you specified when you created the node) to this node hardware. 
   + It then activates the node hardware for use with MediaLive Anywhere. This activation takes approximately 1 minute.

## Verify the node state
<a name="emla-setup-cl-nodes-verify"></a>

1. On the MediaLive console, in the navigation bar, choose **Nodes**. (Don't choose **Cluster**.)

1. In the **Nodes** list, verify that the node state is **Registering**. After a short time, the state changes to **Active**. 