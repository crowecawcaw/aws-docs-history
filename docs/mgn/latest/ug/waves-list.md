NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Manage migration waves

The **Waves** page lists all the waves that have been added to
AWS Application Migration Service (AWS MGN). The **Waves** page allows you to manage your
waves and perform a variety of commands for one or more waves (such as controlling replication
and launching test and cutover instances).

## Interacting with the Waves page

The **Waves** page shows a list of waves. Each row on the list
represents a single wave.

The **Waves** page provides key information for each wave
under each of the columns on the page.

The columns include:

- **Selector column** – This blank checkbox selector column allows
  you to select one or more waves. When a wave is selected, you can interact with the wave
  through the **Actions** menu, **Edit**, and **Delete** buttons. Selected waves are
  highlighted.
- **Wave name** – This column shows the unique wave name for each
  wave.
- **Migration status** – This column shows the migration status for
  each wave.
  - **Not started** – If none of the wave's associated servers has
    started replication yet.
  - **In progress** – At least one of the wave's associated
    applications has started replication and not all of its applications completed migration.
  - **Completed** – If all the wave associated applications
    completed migration (have been cutover).

- **Alerts** – This column shows whether any alerts exist for the
  wave.

A wave that has at least one application that is experiencing significant issues, such as
a stall, will display a **Stalled** status.

An wave that has at least one application that is experiencing a temporary issue such as
lag or backlog will display a **Lagging** status.

A healthy active wave will display a **Healthy** status.

Archived waves do not display any alerts.

- **Number of applications** – This column shows the total number
  of applications associated with each wave.

###### Topics

- [Add wave](add-wave.md "add-wave.md")
- [Edit wave](edit-wave.md "edit-wave.md")
- [Delete wave](delete-wave.md "delete-wave.md")
- [Manage selected waves](wave-actions-menu.md "wave-actions-menu.md")
- [Filtering migration waves](waves-filtering.md "waves-filtering.md")
