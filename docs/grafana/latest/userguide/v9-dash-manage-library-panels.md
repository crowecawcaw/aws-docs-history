# Adding a library panel to your

dashboard

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

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

1. Open a panel in edit mode.
2. In the panel display options, click the down arrow option to bring changes
   to the visualization.
3. To open the **Create** dialog box, click the
   **Library panels** option, and then click
   **Create library panel**.
4. In **Library panel name**, enter the
   name.
5. In **Save in folder**, select the folder to
   save the library panel.
6. To save your changes, click **Create library
   panel**.
7. To save the dashboard, click **Save**.
   After a library panel is created, you can modify the panel using any dashboard on
   which it appears. After you save the changes, all instances of the library panel
   reflect these modifications.

**Adding a library panel to a dashboard**

Add a Grafana library panel to a dashboard when you want to provide visualizations
to other dashboard users.

1. Hover over the **Dashboards** option on the
   left menu, then select **New dashboard** from
   the dropdown options. The **Add panel** dialog
   box will open.
2. Click the **Add a panel** from the panel
   library option. You will see a list of your library panels.
3. Filter the list or search to find the panel you want to add.
4. Click a panel to add it to the dashboard.
   **Unlinking a library panel**

Unlink a library panel when you want to make a change to the panel and not affect
other instances of the library panel.

1. Hover over **Dashboard** on the left menu,
   and then click **Library panels**.
2. Select a library panel that is being used in different dashboards.
3. Select the panel that you want to unlink.
4. Click the title of the panel and then click **Edit**. The panel will open in edit mode.
5. Click the **Unlink** option on the top right
   corner of the page.
   **Viewing a list of library panels**

Unlink a library panel when you want to make a change to the panel and not affect
other instances of the library panel.

1. Hover over the **Dashboard** option on the
   left menu, then click **Library panels**. You
   can see a list of previously defined library panels.
2. Search for a specific library panel if you know its name. You can also
   filter the panels by folder or type.
   **Deleting a library panel**

Delete a library panel when you no longer need it.

1. Hover over **Dashboard** on the left menu,
   and select **Library panels**.
2. Select the panel that you want to delete.
3. Click the delete icon next to the library name.
