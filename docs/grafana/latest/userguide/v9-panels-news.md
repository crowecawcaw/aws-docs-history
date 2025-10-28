# News panel

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

This panel displays an RSS feed. By default, it displays articles from the Grafana
Labs blog.

Enter the URL of an RSS in the **Display** section. This panel type
does not accept any other queries.

###### Note

RSS feeds are loaded by the Grafana front end without a proxy. As a result, only
RSS feeds that are configured with the appropriate [CORS
headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS "https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS") will load. If the RSS feed you're trying to display fails to
load, consider re-hosting the RSS feed or creating your own proxy.
