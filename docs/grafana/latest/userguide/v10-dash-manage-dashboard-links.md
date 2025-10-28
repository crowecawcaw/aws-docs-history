# Managing dashboard links

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

You can use links to navigate between commonly used dashboards or to connect
others to your visualizations. Links let you create shortcuts to other dashboards,
panels, and even external websites.

Grafana supports dashboard links, panel links, and data links. Dashboard links are
displayed at the top of the dashboard. Panel links are accessible by clicking an
icon on the top left corner of the panel.

**Choosing which link to use**

Start by figuring out how you’re currently navigating between dashboards. If
you’re often jumping between a set of dashboards and struggling to find the same
context in each, links can help optimize your workflow.

The next step is to figure out which link type is right for your workflow. Even
though all the link types in Grafana are used to create shortcuts to other
dashboards or external websites, they work in different contexts.

- If the link relates to most if not all of the panels in the dashboard, use
  dashboard links.
- If you want to drill down into specific panels, use panel links.
- If you want to link to an external site, you can use either a dashboard
  link or a panel link.
- If you want to drill down into a specific series, or even a single
  measurement, use data links.
  **Controlling the time range using a URL**

To control the time range of a panel or dashboard, you can provide query
parameters in the dashboard URL:

- `from` defines lower limit of the time range, specified in ms
  epoch.
- `to` defines upper limit of the time range, specified in ms
  epoch.
- `time` and `time.window` defines a time range from
  `time-time.window/2` to `time+time.window/2`. Both
  params should be specified in ms. For example
  `?time=1500000000000&time.window=10000` will result in
  10s time range from 1499999995000 to 1500000005000.
  **Dashboard links**

When you create a dashboard link, you can include the time range and current
template variables to directly jump to the same context in another dashboard. This
way, you don’t have to worry whether the person you send the link to is looking at
the right data. For other types of links, see Data link variables.

Dashboard links can also be used as shortcuts to external systems, such as
submitting a GitHub issue with the current dashboard name.

After adding a dashboard link, it will show up in the upper-right corner of your
dashboard.

**Adding links to dashboards**

Add links to other dashboards at the top of your current dashboard.

###### To add a link to a dashboard

1. While viewing the dashboard you want to link, click the gear at the top of
   the screen to open **Dashboard settings**.
2. Select **Links** and then **Add Dashboard
   Link** or **New**.
3. In **Type**, select **dashboards**.
4. Select link options from the following.
   - **With tags** – Enter tags to limit
     the linked dashboards to only the ones with the tags you enter.
     Otherwise, Grafana includes links to all other dashboards.
   - **As dropdown** – If you are linking
     to many dashboards, By default, Grafana displays them all
     side-by-side across the top of your dashboard. Selecting this
     option and adding an optional title, will display the links in a
     dropdown.
   - **Time range** – Select this
     option to include the dashboard time range in the link. When the
     user clicks the link, the linked dashboard will open with the
     indicated time range already set.
   - **Variable values** – Select this
     option to include template variables currently used as query
     parameters in the link. When the user clicks the link, any matching
     templates in the linked dashboard are set to the values from the
     link. For more information, see [Dashboard URL
     variables](v10-dash-dashboard-url-variables.md "v10-dash-dashboard-url-variables.md").
   - **Open in new tab** – Select this
     option if you want the dashboard link to open in a new tab or
     window.

5. Click **Add**.
   **Adding a URL link to a dashboard**

Add a link to a URL at the top of your current dashboard. You can link to any
available URL, including dashboards, panels, or external sites. You can even control
the time range to ensure the user is zoomed in on the right data in Grafana.

###### To add a URL link to a dashboard

1. While viewing the dashboard you want to link, select the gear at the top of
   the screen to open **Dashboard settings**.
2. Select **Links** and then **Add Dashboard
   Link** or **New**.
3. In **Type**, select **Link**.
4. Select link options from the following.
   - **URL** – Enter the URL you want to
     link to. Depending on the target, you might want to include field
     values.
   - **Title** – Enter the title you want
     the link to display.
   - **Tooltip** – Enter the tooltip you
     want the link to display.
   - **Icon** – Choose the icon that you
     want displayed with the link.
   - **Time range** – Select this option to
     include the dashboard time range in the link. When the user clicks
     the link, the linked dashboard will open with the indicated time
     range set.
     - `from` – Defines lower limit of the time range,
       specified in ms epoch.
     - `to` – Defines upper limit of the time range,
       specified in ms epoch.
     - `time` and `time.window` – Define a
       time range from `time-time.window/2` to
       `time+time.window/2`. Both params should be
       specified in ms. For example
       `?time=1500000000000&time.window=10000`
       will result in 10s time range from 1499999995000 to
     1500000005000.

   - **Variable values** – Select this
     option to include template variables currently used as query
     parameters in the link. When the user clicks the link, any matching
     templates in the linked dashboard are set to the values from the
     link.

   The variable format is as follows:

   ```
   https://${you-domain}/path/to/your/dashboard?var-${template-varable1}=value1&var-{template-variable2}=value2
   ```

   - **Open in a new tab** – Select this
     option if you want the dashboard link to open in a new tab or
     window

5. Select **Add**.
   **Updating a dashboard link**

To change or update an existing dashboard link, follow this procedure.

###### To update a dashboard link

1. In **Dashboard settings,** on the
   **Links** tab, select the existing link that you want
   to edit.
2. Change the settings and then choose **Update**.
   **Duplicating a dashboard link**

To duplicate an existing dashboard link, select the duplicate icon next to the
existing link that you want to duplicate.

**Deleting a dashboard link**

To delete an existing dashboard link, select the trash icon next to the link
that you want to delete.

**Panel links**

Each panel can have its own set of links that are shown in the upper left corner
of the panel. You can link to any available URL, including dashboards, panels, or
external sites. You can even control the time range to ensure the user is zoomed in
on the right data in Grafana.

To see available panel links, select the icon to the right of the panel title.

- **Adding a panel link**: Each panel can have
  its own set of links that are shown in the upper left corner of the panel.
  You can link to any available URL, including dashboards, panels, or external
  sites. You can even control the time range to ensure the user is zoomed in
  on the right data in Grafana. Click the icon on the top left corner of a
  panel to see available panel links.
  1.  Hover your cursor over the panel to which you want to add a link.
  2.  Select the menu, and choose **Edit**, or you
      can use the keyboard shortcut, `e`.
  3.  Expand the **Panel options** section, and scroll
      down to **Panel links**.
  4.  Select **Add link**.
  5.  Enter a **Title**. This is a human-readable
      label for the link that will be displayed in the UI.
  6.  Enter the **URL** you want to link
      to. Press `Ctrl+Space` (or `Cmd+Space`)
      and select the URL field to see available variables. By adding
      template variables to your panel link, the link sends the user to
      the right context, with the relevant variables already set.

  You can also use time variables.

      + `from` defines the lower limit of the time
       range, specified in ms epoch.
      + `to` defines the upper limit of the time range,
       specified in ms epoch.
      + `time` and `time.window` defines a
       time range from `time-time.window/2` to
       `time+time.window/2`. Both parameters should
       be specified in ms. For example
       `?time=1500000000000&time.window=10000`
       results in 10s time range from 1499999995000 to
       1500000005000.

- **Updating a panel link**
  1.  Select a panel (or place the cursor over the panel) to display
      an actions menu at the top right of the panel.
  2.  From the menu, select the **Edit**.

  You can also use the keyboard shortcut, `e`. 3. Expand the **Panel options** section, and
  scroll down to **Panel links**. 4. Find the link that you want to change, and select the
  **Edit** (pencil) icon next to it. 5. Make any necessary changes. 6. Select **Save** to save changes and
  close the window. 7. Save changes to your dashboard by selecting
  **Save** in the upper right.

- **Deleting a panel link**
  1.  Select a panel (or place the cursor over the panel) to display
      an actions menu at the top right of the panel.
  2.  From the menu, select the **Edit**.

  You can also use the keyboard shortcut, `e`. 3. Expand the **Panel options** section, and
  scroll down to **Panel links**. 4. Find the link that you want to delete, and select the
  **X** icon next to it. 5. Select **Save** in the upper right to
  save your changes to the dashboard.
