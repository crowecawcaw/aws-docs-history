# Dashboard version history

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

Whenever you save a version of your dashboard, a copy of that version is saved so
that previous versions of your dashboard are not lost. A list of these versions is
available by choosing **Dashboard settings** and then selecting
**Versions** in the left side menu.

The dashboard version history feature lets you compare and restore to previously
saved dashboard versions.

## Comparing two dashboard

versions

To compare two dashboard versions, select the two versions from the list that you
want to compare. After you select two versions, choose **Compare
versions** to open the diff view. By default, you’ll see a textual
summary of the changes, as in the following image.

To view the diff of the raw JSON that represents your dashboard, choose
**View JSON Diff**.

To restore to the earlier version that you are comparing against, choose
**Restore to version <x>**.

## Restoring to a

previously saved dashboard version

If you need to restore to a previously saved dashboard version, you can do so
either by choosing the "Restore" button on the right of a row in the
dashboard version list or by choosing **Restore to version
<x>** appearing in the diff view. After you choose to restore, a
pop-up box will prompt you to confirm the restoration.

After restoring to a previous version, a new version will be created that
containing the same exact data as the previous version, but with a different version
number. This is indicated in the **Notes** column. This helps to
ensure that your previous dashboard versions are not affected by the change.
