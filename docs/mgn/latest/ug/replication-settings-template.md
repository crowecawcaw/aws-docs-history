NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Replication settings

Replication settings determine how data will be replicated from your source servers to
AWS. Configure the replication settings in the replication template before adding source servers to AWS Application Migration Service. You can modify the
template at any time. Templaate settings are transferred to each newly added server.

You can also edit the replication settings for a particular server or group of servers after you add them to AWS Application Migration Service. You can also control other source server settings through the
**Settings** section in the menu on the left of the console.

###### Topics

- [Understanding template settings and server-specific
  settings](#template-vs-server "#template-vs-server")
- [Edit your replication settings
  template](#edit-replication-template "#edit-replication-template")
- [Edit replication settings for a
  server](#edit-replication-settings "#edit-replication-settings")
- [Replication server settings
  reference](replication-server-settings.md "replication-server-settings.md")

## Understanding template settings and server-specific

settings

The replication template settings determine how data replication works for each new
server you add to AWS Application Migration Service. These settings are
applied to each source server you add. You are prompted to configure your
replication template upon your first use of AWS Application Migration Service.

You can change the replication settings for individual
source servers or for a group of source servers. These changes do not affect the replication settings
template. [Learn more about configuring your
initial replication template](first-time-setup-gs.md "first-time-setup-gs.md").

## Edit your replication settings

template

To edit the replication settings template:

- Choose **Replication template**, under
  **Settings** on the left-hand console
  menu.
- This openw the **Replication template**
  view. Choose **Edit** to edit your account-wide
  replication settings. These settings changes will be applied to each server you add to your account but do not affect servers that you already added to
  AWS Application Migration Service.

## Edit replication settings for a

server

To edit the settings for an individual server or group of servers:

- Select servers on the **Source servers** page.
- Open the **Replication** menu and choose
  **Edit replication settings**.

The names of the servers you are editing appear under the **Selected
servers** dropdown.

- Edit individual replication settings under the **Replication settings** category.
- To change the settings, choose the preferred option from the drop-down
  menu under each setting category.

Any setting that you don't change is labeled **Do not change** option

- Choose **Save replication settings**.

The replication settings categories are explained in the following
sections.
