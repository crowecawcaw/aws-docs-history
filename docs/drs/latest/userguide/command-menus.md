# Source servers page command menus

You can perform a variety of actions, control data replication, and manage your drill and
recovery instances for one or more source servers through the command menu buttons. Select one
or more servers on the **Source servers** page and choose the
**Actions**, **Replication**, or
**Initiate recovery job** menu to control your source servers.

###### Topics

- [Actions menu](#server-actions-main "#server-actions-main")
- [Initiate recovery job menu](#server-initiate-recovery-main "#server-initiate-recovery-main")
- [Replication menu](#server-replication-main "#server-replication-main")

## Actions menu

The **Actions** menu allows you to perform the following
actions:

- **Add servers** – Choosing this option redirects you to the
  AWS Replication Agent installation instructions.
- **Create extended source servers** – Choose this to start a wizard to create extended source servers from source servers replicating into staging accounts, in multi-account setups.
- **Edit DRS launch settings** – Choose this option to edit a single or multiple selected source servers for their DRS launch settings.
- **Edit EC2 launch template** – Choose this option to enter edit a single or multiple selected source servers for their EC2 launch template.
- **Edit post-launch action settings** – Choose this option to activate or deactivate post-launch actions for a single or multiple selected source servers.
- **View server details** – Choose this option to enter the
  source server's **Server details view.**
- **Disconnect from AWS** – Choose this option to disconnect
  the selected server from AWS Elastic Disaster Recovery and AWS.

When the **Disconnect X server/s from service** dialog
appears, click **Disconnect**.

###### Important

This uninstalls the AWS Replication Agent from the source server and data replication
will stop for the source server. This action does not affect any Drill or Recovery
instances that have been launched for this source server, but you are no longer able
to identify which source servers your Amazon EC2 instances correspond to.

- **Delete server** - Choose the **Delete
  server** option to permanently delete a source server from AWS Elastic Disaster Recovery. This
  removes all information related to the server from the AWS Elastic Disaster Recovery service. You can only
  delete servers that have been disconnected from AWS. You need to reinstall the AWS
  Replication Agent on a deleted source server to add it back to AWS Elastic Disaster Recovery.

When the **Delete X servers** dialog appears, click
**Permanently delete**. Then, if the servers have associated recovery instances,
you can either:

    + delete them, keeping the EC2 instances intact),
    + terminate them, which deletes the EC2 instances).

## Initiate recovery job menu

The **Initiate recovery job** menu allows you to start
drills and recoveries by launching drill and recovery instances as part of the overall
failback process. You can learn more about the entire failback and failover process with
AWS Elastic Disaster Recovery in the [Performing a failback and
failover with AWS Elastic Disaster Recovery documentation](failback.md "failback.md").

- **Initiate drill** – Choose this option to launch a drill
  instance for this server or group of servers for the purpose of testing your recovery
  solution. You should perform periodic drills in order to ensure that you are ready for
  recovery. [Learn more about launching Drill
  instances in AWS Elastic Disaster Recovery](preparing-failover.md#recovery-drill-overview "preparing-failover.md#recovery-drill-overview").
- **Initiate recovery** – Choose this option to launch a
  Recovery instances for this server or group of servers for the purpose of recovering
  the server in the event of a disaster. [Learn more about launching Recovery instances in AWS Elastic Disaster Recovery](failback-preparing-failover.md#failback-launching-instances "failback-preparing-failover.md#failback-launching-instances").

## Replication menu

The **Replication** menu allows you to perform the
following actions:

- **Stop replication** – You can stop replication
  of a source server at any time. After you stop the replication, you will no longer be
  charged for the ongoing replication and the staging area infrastructure. Changes will
  not be reported by the agent to the replication server, and all saved snapshots will
  be deleted, leaving this instance unprotected. The agent remains installed during this
  process. If you want to replicate this EC2 instance again, simply click the **Start replication** button. This triggers an initial sync.
- **Start replication** – You can start
  replication of a previously stopped source server. After you start the replication,
  the agent replicates the selected instances.
