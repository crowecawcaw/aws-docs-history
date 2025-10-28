# Importing dashboards

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

You can import preconfigured dashboards into your Amazon Managed Grafana workspace.

###### To import a dashboard

1. Sign into your Amazon Managed Grafana workspace.
2. Select **Dashboards** from the left menu.
3. Select **New** and choose **Import**
   in the drop down menu.
4. Next you need to choose the dashboard JSON definition to import. You
   have three choices for how to import JSON:
   - Upload a file containing dashboard JSON.
   - Directly copy JSON text into the text area.
   - Paste a Grafana Labs dashboard URL or ID into the field. For
     more information on grafana.com dashboard URLs, see the next
     section.
   - (Optional) Change any dashboard details that you wish to
     change.
   - Select a data source, if required.
   - Choose **Import**.
   - Save the dashboard.

## Finding dashboards on

grafana.com

The [Dashboards](https://grafana.com/grafana/dashboards/ "https://grafana.com/grafana/dashboards/")
page on grafana.com provides you with dashboards for common server
applications. Browse a library of official and community-built dashboards and
import them to quickly get up and running.

###### Note

To import dashboards from grafana.com, your Amazon Managed Grafana workspace must
have access to the internet.
