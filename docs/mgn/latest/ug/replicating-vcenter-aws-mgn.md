NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Replicating servers from vCenter to AWS

Once you have successfully installed the AWS vCenter client, all of your vCenter VMs are added to Application Migration Service in the DISCOVERED state. The DISCOVERED state means that the VM has not been
replicated to AWS.

###### Note

VMware only sends data for up to 50 servers in parallel. Replicating more than 50 servers
at once causes the rest to be queued and results in a longer wait.

By default, the Application Migration Service console only shows active servers. You can tell which servers are being
shown by looking at the filtering box under the main **Source
servers** title.

To see your discovered non-replicating servers that have been added from vCenter, open the
filtering menu and choose **Discovered source servers**.

You now see all of your non-replicating DISCOVERED VMs.

To replicate one or more VMs into AWS, select the box to the left of each VM name, choose
the **Replication** menu, and then choose **Start data replication**.

Choose **Start** on the **Start data
replication for x servers** dialog.

The Application Migration Service console indicates that data replication has started.

To view the data replication progress, open the filtering menu and return to the default
**Active source servers** view.

You now only see your replicating source servers. You can follow the launch process on
the main **Source servers** view.

Once the VM has reached the **Ready for testing** state under
**Migration lifecycle**, you can continue to [launch test and cutover instances](launching-test-servers.md "launching-test-servers.md") and perform all other
regular Application Migration Service operations on the server.
