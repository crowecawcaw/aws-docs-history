NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Source server migration metrics

The source server migration metrics present an aggregated overview of your source servers,
focused on three topics: **Alerts**, **Data
replication status**, and **Migration status**.

## Understand source server alerts

The source server **Alerts** migration metric presents an
aggregated overview of the application associated servers alerts. You can look up an individual
source server's **Alerts** in the **Source
servers** table at the bottom of the page.

- A healthy server for which a test or cutover instance has not been launched displays
  a **Healthy** status.
- A healthy server for which a test of cutover instance has been launched displays a
  **Healthy** status.
- A server that is experiencing a temporary issue such as lag or backlog displays a
  **Lagging** status.
- A server that is experiencing significant issues, such as a stall, displays a
  **Stalled** status.

## Understand data replication status

The source server **Data replication status** migration
metric presents an aggregated overview of the your source servers' data replication status. You
can look up an individual source server's **Data replication
status** status in the **Source servers** table at the
bottom of the page.

Source server **Data replication status** can have one of these values:

- **Transferring snapshot**
- **Initial sync**
- **Finalizing sync**
- **Lagging**
- **Healthy**
- **Stalled**
- **Rescanning**
- **Not started**
- **Initiating**
- **Creating snapshot**
- **Paused**
- **Disconnected**

## Understand the migration lifecycle

metric

The source server **Migration lifecycle** metric shows an
aggregated overview of your source servers' migration lifecycle. You can look up an individual
source server's **Migration lifecycle** status in the **Source servers** table at the bottom of the page.

Source server **Migration lifecycle** can have one of these values:

- **Stopped**
- **Not ready**
- **Ready for testing**
- **Test in progress**
- **Ready for cutover**
- **Cutover in progress**
- **Cutover complete**
- **Disconnected**
- **Discovered**
