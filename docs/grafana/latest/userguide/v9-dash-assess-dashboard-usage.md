# Assessing dashboard usage

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Usage insights enable you to have a better understanding of how your Grafana instance
is used.

The usage insights feature collects a number of aggregated data and stores them in the
database.

- Dashboard views (aggregated and per user)
- Data source errors
- Data source queries
  The aggregated data provides you access to several features, including dashboard and
  data source insights, presence indicator, sorting dashboards by using insights data, and
  visualizing usage insight data in a dashboard.

This feature also generates detailed logs that can be exported to Loki.

## Dashboard and data source insights

For every dashboard and data source, you can access usage information.

**Dashboard insights**

To see dashboard usage information, click **Dashboard
insights** in the top bar.

Dashboard insights show the following information.

- **Stats**: The number of daily queries and
  errors for the past 30 days.
- **Users & activity**: The daily view
  count for the last 30 days; last activities on the dashboard and recent
  users (with a limit of 20).

**Data source insights**

Data source insights provide information about how a data source has been used in
the past 30 days, such as:

- Queries per day
- Errors per day
- Query load time per day (averaged in ms)

To find data source insights:

1. Go to the **Data source** list view.
2. Click on **Data source**.
3. Click the **Insights** tab.

## Presence indicator

When you sign in and look at a dashboard, you can know who is looking at the same
dashboard as you are through a presence indicator, which displays avatars of users
who have recently interacted with the dashboard. The default timeframe is 10
minutes. To see the user’s name, hover over the user’s avatar. The avatars come from
[Gravatar](https://gravatar.com/ "https://gravatar.com/") based on the user’s
email.

When there are more active users on a dashboard than can fit within the presence
indicator, click the **+X** icon. Doing this will open
dashboard insights, which contain more details about recent user activity.

## Sorting dashboards by using insights

data

In the search view, you can use insights data to help you find most-used, broken,
and unused dashboards.

- Errors total
- Errors 30 days
- Views total
- Views 30 days
