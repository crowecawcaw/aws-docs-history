# Step F: Rebuild the cluster

1. Restore the database on primary conductor file node.
2. If you have a secondary conductor in the cluster, you need to restore the
   database on secondary conductor file node.
3. If you have a secondary conductor in the cluster, you need to add the
   secondary conductor to the cluster.
   1. From the Linux prompt, log in to the secondary conductor node with the
      _elemental_ user
      credentials.
   2. Run the following commands:

   ```
   [elemental@hostname ~]$ cd /opt/elemental_se
   [elemental@hostname ~]$ sudo ./configure -s -c -t -n -z -xeula
   ```

   3. You will see the following prompts:

   ```
   [elemental@hostname ~]$ Configure this node as a secondary Elemental Conductor in an existing cluster? [N]
   Y
   [elemental@hostname ~]$ What is the hostname or IP address of the cluster management node?
   <hostname of primary conductor>
   ...
   [elemental@hostname ~]$ Are you sure you want to continue connecting (yes/no/[fingerprint])?
   yes
   [elemental@hostname ~]$ elemental@<hostname> password:
   <hostname of primary conductor>
   ...
   [elemental@hostname ~]$ Trust this public key? [Y]
   Y
   ```

4. If HA mode is enabled before, you need to re-enable it again.
5. Restore the database on all the worker nodes.
6. Add all the worker nodes back to the cluster
   1. From the Linux prompt, log in to the worker node with the _elemental_ user credentials.
   2. Run the following commands:

   ```
   [elemental@hostname ~]$ cd /opt/elemental_se
   [elemental@hostname ~]$ sudo ./configure -s -c -t -n -z -xeula
   ```

   3. After being prompted to add the worker node to the Conductor File
      cluster, you are asked to trust the public key from the conductor
      node(s). You must accept this for the Conductor File node to control the
      worker node.
   4. After trusting the public key, continue through the configuration
      prompts as normal.

7. Use the configure script to add worker nodes to the cluster.

###### Important

If this is your first time adding worker nodes to a cluster you must add
worker nodes to the Conductor File cluster via the CLI. Using the Conductor
File web interface to discover the worker node and add to the cluster causes
the worker node to go into a failed state.

    1. On the worker node, enter the following command to change the
     directory:



    ```
    cd /opt/elemental_se
    ```
    2. Enter the following command to start the configurations script on the
     worker node:



    ```
    sudo ./configure
    ```
    3. After being prompted to add the worker node to the Conductor File
     cluster, you are asked to trust the public key from the conductor
     node(s). You must accept this for the Conductor File node to control the
     worker node.
    4. After trusting the public key, continue through the configuration
     prompts as normal.
