# Step C: Tear down

an
AWS Elemental Conductor File cluster

Before you can install RHEL 9 and the new software version, you must remove all the
nodes from the cluster.

1. Remove every worker node from the cluster. You perform this action from the
   primary Conductor node.
   1. On the primary Conductor web interface, choose **Nodes**.
   2. On the **Nodes** screen, scroll down to
      the list of nodes.
   3. Choose **View All Nodes** to display a
      list of all the conductor and worker nodes in the network.
   4. Select the nodes to remove and choose **Remove
      from Cluster**.

2. If you have a secondary conductor in the cluster, you need to remove the
   secondary conductor node from the cluster.
   1. If HA mode is enabled, you need to disable HA mode on the **secondary** conductor.
   2. Remove the secondary conductor node from the cluster
      1. From the Linux prompt, log in to the conductor node with the
         _elemental_ user
         credentials.
      2. Run the following commands:

      ```
      [elemental@hostname ~]$ cd /opt/elemental_se
      [elemental@hostname ~]$ sudo ./configure -s -c -t -n -z -xeula
      ```

      3. You will see the following prompts:

      ```
      Remove this node from the Conductor system? [N]
      Y
      Configure this node as a secondary Elemental Conductor in an existing cluster? [N]
      N
      ```

3. If HA mode is enabled, you need to disable HA mode on the **primary** conductor.
   After you remove the last worker node, the cluster still exists but it doesn't contain
   any worker nodes or a secondary Conductor. The single Conductor exists, but it isn't
   controlling any worker nodes.
