This is version 2.18 of the AWS Elemental Conductor File documentation. This is the
latest version. For prior versions, see the _Archive_ section of
[AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Add AWS Elemental Server Nodes to the Cluster

Add all of the worker nodes to the cluster so that they can be controlled by the Conductor node.

###### Important

If this is your first time adding worker nodes to a cluster you must add worker nodes to the Conductor File cluster via the CLI. Using the Conductor File web interface to discover the worker node and add to the cluster causes the worker node to go into a failed state.

###### To add worker nodes to the cluster via the CLI

1. On the worker node, enter the following command to change the directory:

`cd /opt/elemental_se` 2. Enter the following command to start the configurations script on the worker node:

`sudo ./configure` 3. After being prompted to add the worker node to the Conductor File cluster, you are asked to trust the public key from the conductor node(s). You must accept this for the Conductor File node to control the worker node. 4. After trusting the public key, continue through the configuration prompts as normal.

###### Note

After you run the configuration script on the worker node, you can add or remove any future nodes using the Conductor File web interface. EXCEPTION: If you kickstart the worker node after you added it to the Conductor File cluster, you must add it back into the cluster via the CLI again.

###### To add worker nodes to the cluster

1. On the primary Conductor web interface, choose **Nodes**.
2. On the **Nodes** screen, scroll down to the list of nodes.
3. Choose **All Nodes** to display a list of all the Conductor and worker nodes in the network. If a given node does not appear in the list, you must force discovery, as described in the next section.
4. Select the nodes to add to the cluster or use the checkbox to select all nodes, and choose **Add to Cluster** (+ icon).
5. Wait a few minutes and then select the **Cluster** tab to view all of the nodes in the cluster.
