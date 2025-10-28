# Managing dashboard version

history

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Whenever you save a version of your dashboard, a copy of that version is saved so
that previous versions of your dashboard are never lost. A list of these versions is
available by entering the dashboard settings and then selecting **Versions** in the left side menu.

The dashboard version history feature lets you compare and restore to previously
saved dashboard versions.

**Comparing two dashboard versions**

To compare two dashboard versions, select the two versions from the list that you
wish to compare. Click **Compare versions** to view the
diff between the two versions.

Upon clicking the button, you’ll be brought to the diff view. By default, you’ll
see a textual summary of the changes.

If you want to view the diff of the raw JSON that represents your dashboard, you
can do that as well by clicking the **View JSON Diff**
button at the bottom.

If you want to restore to the version you are diffing against, you can do so by
clicking the **Restore to version <x>** button in
the top right.

**Restoring to a previously saved dashboard
version**

If you need to restore to a previously saved dashboard version, you can either
click the **Restore** button on the right of a row in
the dashboard version list, or click the **Restore to version
<x>** button appearing in the diff view. Clicking the button will
bring up the following pop-up prompting you to confirm the restoration.

After restoring to a previous version, a new version will be created containing
the same exact data as the previous version, only with a different version number.
This is indicated in the **Notes column** for the row
in the new dashboard version. This is done simply to ensure your previous dashboard
versions are not affected by the change.
