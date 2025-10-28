NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Manage applications

The **Applications** page lists all the applications that
have been added to AWS Application Migration Service. The **Applications** page
allows you to manage your applications and perform a variety of commands for one or more
applications (such as controlling replication and launching test and cutover instances).

## Interacting with the Applications

page

The **Applications** page shows a list of
applications. Each row on the list represents a single application.

The **Applications** page provides key information
for each application under each of the columns on the page.

The columns include:

- **Selector column** – This blank checkbox
  selector column allows you to select one or more applications. When an
  application is selected, you can interact with the application through the
  **Actions** menu, **Edit**, and **Delete** buttons.
  Selected applications are highlighted.
- **Application name** – This column shows the
  unique application name for each application.
- **Wave name** – This column shows the name of
  the wave the application is associated with. An application cannot be
  associated with more than one wave at a time.

This column is hidden by default.

- **Migration status** – This column shows the
  migration status for each application.
  - **Not started** – None of the
    application associated servers has started replication yet.
  - **In progress** – At least one of the
    application associated servers has started replication and not all
    of its servers completed migration.
  - **Completed** – All the application
    associated servers completed migration (have been cut over).

- **Alerts** – This column shows whether any
  alerts exist for the application.

      + **Stalled** – An application that has
       at least one server that is experiencing significant issues, such as
       a stall,.
      + **Lagging** – An application that has
       at least one server that is experiencing a temporary issue such as
       lag or backlog.
      + **Healthy** – A healthy active
       application.

  Archived applications do not display any alerts.

- **Number of servers** – This column shows the
  total number of servers associated with each application.

###### Topics

- [Add application](add-application.md "add-application.md")
- [Edit application](edit-application.md "edit-application.md")
- [Delete application](delete-application.md "delete-application.md")
- [Manage applications](application-actions-menu.md "application-actions-menu.md")
- [Filtering the Applications page](applications-filtering.md "applications-filtering.md")
