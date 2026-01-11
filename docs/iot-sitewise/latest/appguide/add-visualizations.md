The SiteWise Monitor feature is not available to new customers. Existing customers can continue to
use the service as normal. For more information, see [SiteWise Monitor availability
change](iotsitewise-monitor-availability-change.md "iotsitewise-monitor-availability-change.md")

# Add visualizations in AWS IoT SiteWise Monitor

In AWS IoT SiteWise Monitor, a dashboard is a group of visualizations. As a project owner, you decide
which asset properties and alarms appear in each dashboard, and how they are best represented.
For more information about the available visualization types, see [Choose visualization types](choose-visualization-types.md "choose-visualization-types.md").

There are three steps to add a visualization to a dashboard:

1. [Edit a dashboard](#editing-dashboards "#editing-dashboards") – Open
   the dashboard for editing.
2. [Drag a property or alarm to a
   dashboard](#dragging-properties-to-dashboards "#dragging-properties-to-dashboards") – Drag a property or alarm to
   the dashboard.
3. [Customize visualizations](customize-visualizations.md "customize-visualizations.md")
   – Customize the visualization by choosing the ideal visualization and setting its
   properties and alarms.

## Edit a dashboard

After you create a dashboard and add your visualizations, you can update your dashboard
to change how it appears.

###### To edit a project's dashboard

1. In the navigation bar, choose the **Projects** icon.

![The "Projects" icon in the navigation bar.](images/portal-navigation-projects-console.png) 2. On the **Projects** page, choose the project whose dashboards you
want to edit.

![The "Projects" page with "Wind Farm 3" highlighted.](images/projects-portal-admin-choose-project-console.png) 3. In the **Dashboards** section, choose a dashboard to edit.

![The dashboards list on the project details page with a dashboard highlighted.](/images/iot-sitewise/latest/appguide/images/project-project-owner-view-dashboard-console.png) 4. In the dashboard, choose **Edit** in the upper right.

You can now rename the dashboard, or add, remove, or modify visualizations. 5. After you finish editing the dashboard, choose **Save dashboard** to
save your changes. The dashboard editor closes. If you try to close a dashboard that has
unsaved changes, you're prompted to save them.

## Drag a property or alarm to a

dashboard

You add visualizations to the dashboard by dragging asset properties and alarms onto the
dashboard. You can drag them onto an empty space to create a visualization or onto an
existing visualization to add that property or alarm to those already in the visualization.
You can add up to five asset properties or alarms to each visualization. Only portal
administrators and project owners can edit dashboards. For more information about how to
open a dashboard to change it, see [Edit a dashboard](#editing-dashboards "#editing-dashboards").

1. Browse the list of project assets on the right side of the dashboard. When you find a
   property or alarm to visualize, drag it to the dashboard.
   - The default visualization type for properties is the [line chart](choose-visualization-types.md#line-charts "choose-visualization-types.md#line-charts").
   - The default visualization type for alarms is the [status grid widget](choose-visualization-types.md#status-grid-chart "choose-visualization-types.md#status-grid-chart").

###### Note

You can drag multiple properties and alarms onto a single visualization.

![The dashboard editor with "Total average power" highlighted.](images/dashboard-add-visualization-console.png) 2. To change how your data displays, choose the visualization type.

![A sample visualization with the visualization type icon highlighted.](images/dashboard-edit-visualization-type-console.png)

For more information about the available visualization types, see [Choose visualization types](choose-visualization-types.md "choose-visualization-types.md"). To
customize details of the visualization, see [Customize visualizations](customize-visualizations.md "customize-visualizations.md"). 3. To add thresholds to your property, choose the visualization configuration icon. If you
add a property that has an alarm, the visualization displays that alarm's threshold. For
more information, see [Configure thresholds](configure-thresholds.md "configure-thresholds.md").

![A sample visualization with the visualization configuration icon highlighted.](images/dashboard-edit-visualization-configuration-console.png) 4. To move or resize your visualization, see [Adjust dashboard layout](adjust-layout.md "adjust-layout.md").
