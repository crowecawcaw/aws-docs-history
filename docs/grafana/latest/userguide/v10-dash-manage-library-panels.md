# Managing library panels

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

A library panel is a reusable panel that you can use in any dashboard. When you
change a library panel, the change propagates to all instances of where the panel is
used. Library panels streamline reuse of panels across multiple dashboards.

You can save a library panel in a folder alongside saved dashboards.

**Creating a library panel**

When you create a library panel, the panel on the source dashboard is converted to
a library panel as well. You need to save the original dashboard after a panel is
converted.

###### To create a library panel

1. Open the panel you want to convert to a library panel in edit
   mode.
2. In the panel display options, click the down arrow option to start changes
   to the visualization.
3. Select **Library panels**, and then
   **+ Create library panel**. This opens the create
   dialog.
4. In **Library panel name**, enter the
   name you want for the panel.
5. In **Save in folder**, select the folder to
   save the library panel.
6. Select **Create library panel** to save your changes
   to the library.
7. Save the dashboard.
   After a library panel is created, you can modify the panel using any dashboard on
   which it appears. After you save the changes, all instances of the library panel
   reflect these modifications.

You can also create a library panel directly from the edit menu of any panel,
by selecting **More...** then **Create library
panel**.

**Adding a library panel to a dashboard**

Add a Grafana library panel to a dashboard when you want to provide visualizations
to other dashboard users.

###### To add a library panel to a dashboard

1. Select **Dashboards** on the left menu.
2. Select **New**, and then choose **New
   dashboard** from the drop down.
3. On the empty dashboard, select **+ Import library panel**.
   You will see a list of your library panels.
4. Filter the list or search to find the panel you want to add.
5. Click a panel to add it to the dashboard.
   **Unlinking a library panel**

Unlink a library panel when you want to make a change to the panel and not affect
other instances of the library panel.

###### To unlink a library panel

1. Select **Dashboards** on the left menu.
2. Select **Library panels**.
3. Select a library panel that is being used in different dashboards.
4. Select the panel that you want to unlink.
5. Select the panel title (or hover the pointer anywhere over the panel),
   to display the actions menu on the top right corner of the panel.
6. Select **Edit**. The panel will open in edit
   mode.
7. Select **Unlink** on the top right
   corner of the page.
8. Choose **Yes, unlink**.
   **Viewing a list of library panels**

You can view a list of available library panels and search for a library
panel.

###### To view a list of library panels

1. Select **Dashboards** on the left menu.
2. Select **Library panels**. You
   can see a list of previously defined library panels.
3. Search for a specific library panel if you know its name. You can also
   filter the panels by folder or type.
   **Deleting a library panel**

Delete a library panel when you no longer need it.

###### To delete a library panel

1. Select **Dashboards** on the left menu.
2. Select **Library panels**.
3. Select the delete icon next to the library panel name for the panel
   you wish to delete.
