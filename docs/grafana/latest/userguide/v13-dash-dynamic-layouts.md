

# Organizing dashboards with tabs, rows, and flexible layouts
<a name="v13-dash-dynamic-layouts"></a>

****  
This documentation topic is designed for Grafana workspaces that support **Grafana version 13.x**.  
For Grafana workspaces that support Grafana version 12.x, see [Working in Grafana version 12](using-grafana-v12.md).  
For Grafana workspaces that support Grafana version 10.x, see [Working in Grafana version 10](using-grafana-v10.md).  
For Grafana workspaces that support Grafana version 9.x, see [Working in Grafana version 9](using-grafana-v9.md).

Rows let you group panels vertically. Previously, if you needed to separate concerns further (for example, between your API gateway and your database), you had to either create a single dashboard with a long scroll, or split it across multiple dashboards.

Dynamic dashboards add *tabs* as a first-class layout option, alongside rows. Tabs let you organize a dashboard horizontally, so that different teams or services can each have their own section in one place. You can nest tabs inside rows and rows inside tabs, up to three levels deep.

Each section can have its own independent variable filters by using section-level variables, so changing a filter in one tab or row does not affect the others.