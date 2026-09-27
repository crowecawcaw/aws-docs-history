

# Dashboards
<a name="omni-dashboards"></a>

A dashboard is a saved arrangement of panels (charts, tables, maps, and text) that shows your team one agreed view of a system. Most panels are backed by a query against your space's telemetry. Build one per audience: a service's health for its on-call, an agent fleet's quality trends for its owners, a cross-signal view for an operations review.

**Note**  
Omni dashboards are separate from the dashboards in the CloudWatch console. Your existing CloudWatch dashboards keep working unchanged (see [CloudWatch Omni](cloudwatch-omni.md)).

**Every dashboard is shared**

Every dashboard belongs to your space, and every member of the space can see it. Name dashboards so others can find them.

**Pages and dashboards**

You build and edit on a **page**, the live working surface on a canvas with a shared time range where you arrange related panels. Saving a page makes it a dashboard. Opening a saved dashboard gives you a working copy on a fresh page: you can rearrange and experiment without changing what the rest of the team sees. When you save, you choose whether to update the original — this is how you edit a shared dashboard — or keep your version as a new dashboard. Omni saves your editing progress as you work, so if you are signed out you can resume in your most recent thread.

**What goes on a dashboard**

Any view you work with in the Omni web UI is a panel, and application and agent telemetry mix on the same dashboard: a service's request charts next to its agent's quality trends. Panels include query visualizations from Explore, the application map and service views, trace and session views, alert status, agent fleet and evaluation views, and text panels for notes. For the query languages behind query-backed panels, see [Explore and query your telemetry](omni-explore-and-query-your-telemetry.md).

**Create a dashboard**

You can create a dashboard in three ways, depending on where you start:
+ **Save the view you are in.** From any page, choose **Save** in the toolbar. An Explore query or an investigation's working view becomes a shared dashboard.
+ **Start in the Dashboards page.** Choose **Create dashboard**, then start from an empty canvas or a starter template, and add panels.
+ **Describe it.** Ask the Omni agent to build a dashboard from a plain-language description, or to turn a finished investigation into one, then refine and save the result. See [Ask the Omni agent](omni-ask-the-omni-agent.md).

**Manage your dashboards**

The **Dashboards** page lists every dashboard in the space. From it you can open or delete a dashboard, and search the list. Note the following behavior:
+ **Deleting is permanent, and removes the dashboard for everyone in the space.**