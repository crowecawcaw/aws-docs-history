NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Manage data replication

You can manage data replication for the source server through these actions on the
**Replication** drop-down menu:

- **Start data replication** – Restarts data replication for
  a source server on which data replication has been stopped. If you are using agent-based
  replication you don't necessarily have to reinstall the agent.
- **Stop data replication** – Stops data replication for a
  source server. Stopping the replication stops billing, deletes existing snapshots and
  EBS volumes, and terminates replication servers. Configuration is retained, and if you
  are using agent-based replication the agent is not uninstalled.
- **Pause data replication** – Pauses data replication for a
  source server. Pausing the replication does not stop billing or delete existing
  snapshots or EBS volumes. Replication servers are not terminated and if you are using
  agent-based replication the agent is not uninstalled from the source server.
- **Resume data replication** – Resume data replication for a
  paused source server. This syncs any changes since the last synchronization and
  completes the data replication flow.
  Choose **Edit** in the **Replication
  settings** section to access the **Edit Replication Settings** page, where you can edit the settings for the selected source
  server. [Learn more about editing replication
  settings.](replication-settings-template.md "replication-settings-template.md")
