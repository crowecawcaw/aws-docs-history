# News

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

The news visualization displays an RSS feed. By default, it displays articles from
the Grafana Labs blog, and users can change this by entering a different RSS feed
URL.

Enter the URL of an RSS in the **Display** section. This
visualization type does not accept any other queries, and users should not expect to
be able to ilter or query the RSS feed data in any way using this visualization.

###### Note

RSS feeds are loaded by the Grafana front end without a proxy. As a result, only
RSS feeds that are configured with the appropriate [CORS
headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS "https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS") will load. If the RSS feed you're trying to display fails to
load, consider re-hosting the RSS feed or creating your own proxy.
