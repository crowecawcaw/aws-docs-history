NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Review overall application status

The **Overview** dashboard provides an overview of
the overall application status, including:

- **Description** – The description of the
  application.
- **State** – The state of the application.
  **State** can be in one of two states:
  **Active** or **Archived**.
- **Last status update** – Time stamp of when
  application status was updated (update occurs every five minutes).
- **Wave name** – Name of the wave that the
  application is associated with.
- **Migration status** – The application
  migration status.

Application **Migration status** can have
one of the following values:

**Not started** – If none of its servers has
started replication yet.

**Completed** – If all of its servers completed
migration (have been cutover).

**In progress** – At least one of its servers
has started replication and not all of its servers completed migration.

- **Alerts** – The application alert.

An application that has at least one server that is experiencing
significant issues, such as a stall, will display a **Stalled** status.

An application that has at least one server that is experiencing a
temporary issue such as lag or backlog will display a **Lagging** status.

A healthy active application will display a **Healthy** status.

An archived application will not display a status.
