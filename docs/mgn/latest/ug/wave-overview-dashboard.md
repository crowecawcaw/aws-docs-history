NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Review overall wave status

The **Overview** dashboard provides an overview of the overall
wave status, including:

- **Description** – The description of the wave.
- **State** – The state of the wave. **State** can be in one of two states: **Active** or
  **Archived**
- **Last status update** – Time stamp of when wave status was
  updated (update occurs every five minutes).
- **Wave start time** – Time stamp of when the earliest replication
  started for a server associated with this wave.
- **Current duration** – Duration of replication time since
  **Wave start time**. If wave is archived, duration is until the
  moment the wave was archived.
- **Migration status** – The wave migration status.

Wave **Migration status** can have one of the following
values:

    + **Not started** – If none of its applications has started
     replication yet.
    + **Completed** – If all of its applications completed
     migration (have been cutover).
    + **In progress** – At least one of its applications has
     started replication and not all of its applications completed migration.

- **Alerts** – The wave alert.
  - A wave that has at least one application that is experiencing significant issues, such
    as a stall, will display a **Stalled** status.
  - A wave that has at least one application that is experiencing a temporary issue such as
    lag or backlog will display a **Lagging** status.
  - A healthy active wave will display a **Healthy**
    status.
  - An archived wave will not display a status.
