NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Actions during migration

Once the AWS Replication Agent is installed and data replication is active, you can
perform the following actions on your source servers. These actions allow you to monitor
replication health, manage the replication process, and progress through the migration
lifecycle.

## Start data replication

Data replication begins automatically after the AWS Replication Agent is installed.
However, if replication has been paused or stopped, you can restart it manually.

To start data replication:

1. Open the AWS Transform MGN console and navigate to the **Source
   servers** page.
2. Select the checkbox next to one or more source servers.
3. Choose **Replication**, then choose **Start data replication**.

## Pause data replication

You can pause data replication for a source server. When replication is paused, the
replication server in the staging area is stopped, which reduces costs. Data changes on the
source server are not replicated while replication is paused.

To pause data replication:

1. Open the AWS Transform MGN console and navigate to the **Source
   servers** page.
2. Select the checkbox next to one or more source servers.
3. Choose **Replication**, then choose **Pause data replication**.

###### Important

Pausing replication will cause lag to accumulate on the source server. When replication
is resumed, a resync will be required to bring the target up to date. This may extend the time
needed before the server is ready for cutover.

## Resume data replication

After pausing replication, you can resume it at any time. AWS Transform MGN will perform a resync
to replicate any data changes that occurred while replication was paused.

To resume data replication:

1. Open the AWS Transform MGN console and navigate to the **Source
   servers** page.
2. Select the checkbox next to one or more source servers.
3. Choose **Replication**, then choose **Resume data replication**.

## Launch test instance

Once the initial sync is complete and the server reaches the **Ready
for testing** state, you can launch a test instance. A test instance is a non-disruptive
launch that allows you to validate the migrated server in AWS without affecting the source
server or the ongoing replication.

To launch a test instance:

1. Open the AWS Transform MGN console and navigate to the **Source
   servers** page.
2. Select the checkbox next to one or more source servers in the **Ready
   for testing** state.
3. Choose **Test and cutover**, then choose **Launch test instances**.
4. Review the launch summary and choose **Launch**.

###### Note

Launching a test instance does not stop replication. Data continues to replicate from the
source server while the test instance is running.

## Finalize test and mark as ready for cutover

After validating the test instance, finalize the test to mark the server as ready for
cutover. This action terminates the test instance and advances the server's migration lifecycle
state.

To finalize a test:

1. Open the AWS Transform MGN console and navigate to the **Source
   servers** page.
2. Select the checkbox next to one or more source servers.
3. Choose **Test and cutover**, then choose **Finalize test**.
4. Confirm the action by choosing **Finalize test** in the
   dialog.

## Launch cutover instance

When you are ready to perform the final migration, launch a cutover instance. Before
launching a cutover instance, stop all services on the source server to ensure that no new data
changes occur and that the replication lag is zero.

To launch a cutover instance:

1. Confirm that the data replication lag is zero on the source server.
2. Stop all operational services on the source server.
3. Open the AWS Transform MGN console and navigate to the **Source
   servers** page.
4. Select the checkbox next to one or more source servers in the **Ready
   for cutover** state.
5. Choose **Test and cutover**, then choose **Launch cutover instances**.
6. Review the launch summary and choose **Launch**.

###### Important

Launching a cutover instance is a significant step in the migration process. Ensure that
you have completed all acceptance testing and that your team is prepared for the cutover window
before proceeding.

## Monitor replication health

You can monitor the replication health and progress of each source server from the
AWS Transform MGN console. The **Source servers** page displays the
current data replication state and migration lifecycle state for each server.

To view detailed replication information for a source server:

1. Open the AWS Transform MGN console and navigate to the **Source
   servers** page.
2. Choose the source server name to open the **Server details**
   view.
3. Review the **Migration dashboard** section to see the
   current lifecycle state, data replication status, and any alerts or errors.

The following data replication states may be displayed:

- **Initial sync** – The agent is performing the first full
  replication of the source server's data to AWS.
- **Healthy** – Replication is active and up to date with no
  lag.
- **Lagging** – Replication is active but behind the source
  server. This is typically a temporary state.
- **Stalled** – Replication has stopped due to an error.
  Review the alerts and take corrective action.
- **Paused** – Replication has been manually paused.
- **Disconnected** – The agent on the source server has lost
  connectivity to AWS Transform MGN.
