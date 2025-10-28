NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Using the AWS Application Migration Service console

AWS Application Migration Service is AWS Region-specific. Ensure that you select the correct Region from the
**Select a Region** menu when using AWS Application Migration Service, just like you would
with other AWS Region-specific services such as Amazon EC2.

AWS Application Migration Service is divided into several primary pages. Each page contains additional tabs and
actions. The default view for the AWS Application Migration Service console is the **Source
servers** page. This page automatically opens every time you open AWS Application Migration Service.

You can navigate to other AWS Application Migration Service pages through the left-hand **AWS Application Migration Service** navigation menu. You can also access the AWS Migration Hub and the
AWS Application Migration Service documentation through this menu.

Each AWS Application Migration Service page will open in the right-hand main view. Here, you can interact with the
various tabs, actions, and settings on the page.

## Source servers page

The **Source servers** page lists all of the source servers
you added to AWS Application Migration Service and allows you to interact with your servers and perform a variety of
actions. [Learn more about the source servers page.](source-servers.md "source-servers.md")

- To control your source servers within the AWS Application Migration Service console, use the **Actions, Replication**, and **Test and
  cutover** menus. The commands within those menus influence the specific source
  servers you have selected. You can select a single source server or multiple source servers
  for any command by checking the box to the left of the server name.
- To review the progress of all commands, use the **Launch
  history** tab. [Learn more about Launch history.](jobs.md "jobs.md")
- Use the **Filter source servers...** box to filter servers
  based on a variety of parameters.

AWS Application Migration Service color codes the state of each source server. Use the **Alerts** column to easily determine the state of your server.

A clock icon with gray text indicates that the server is experiencing temporary issues. The
nature of the issue will be identified (for example, "Lagging").

A red x and text indicates that the server is experiencing significant issues that need to
be addressed before replication can resume. The nature of the issue will be indicated (for
example, "Stalled")

When various commands are initiated, AWS Application Migration Service will display information messages at the top
of the **Source Servers** page. Application Migration Service color
codes these messages for clarity.

- A green message indicates that a command was completed successfully.
- A red message means that a command was not completed successfully.

Each message shows details and links to supplemental information.

AWS Application Migration Service allows you to interact with and manage each server. Choose the source server name
to be redirected to the Server details view.

The **Server details** tab shows specific details for an
individual server. From here, you can review the server's migration lifecycle and health, view
various technical details, manage tags, manage disks, edit the server's replication settings,
and edit the server's launch settings through the various tabs. [Learn more about the Server details view](server-details.md "server-details.md").

Certain AWS Application Migration Service commands, such as **Edit replication
settings**, allow you to interact with multiple source servers at once. When multiple
source servers are selected by checking the box to the left of the server name and the **Replication > Edit replication settings** option is chosen, AWS Application Migration Service will
indicate which servers are being edited.

For your changes to take effect, click **Save** at the bottom
of each settings page.
