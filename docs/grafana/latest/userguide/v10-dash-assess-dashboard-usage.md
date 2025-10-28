# Assessing dashboard usage

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

For every dashboard and data source, you can access usage information.

**Dashboard insights**

To see dashboard usage information, select **Dashboard
insights** in the top bar.

Dashboard insights show the following information.

- **Stats** – The number of daily queries and
  errors for the past 30 days.
- **Users & activity** – The daily view
  count for the last 30 days; last activities on the dashboard and recent
  users (with a limit of 20).
  **Data source insights**

Data source insights provide information about how a data source has been used in
the past 30 days, such as:

- Queries per day
- Errors per day
- Query load time per day (averaged in ms)

###### To find data source insights

1. Select **Connections** in the main navigation of your
   workspace.
2. Select **Data sources**.
3. Choose a data source.
4. Select the **Insights** tab.

## Presence indicator

When you are signed in and look at a dashboard, you can know who is looking at
the same dashboard as you are through a presence indicator, which displays
avatars of users who have recently interacted with the dashboard. The default
timeframe is 10 minutes. To see the user’s name, hover over the user’s avatar.
The avatars come from [Gravatar](https://gravatar.com/ "https://gravatar.com/") based
on the user’s email.

When there are more active users on a dashboard than can fit within the presence
indicator, click the **+X** icon. Doing this will open
dashboard insights, which contain more details about recent user activity.

## Sorting dashboards by using insights

data

In the search view, you can use insights data to help you find most-used, broken,
and unused dashboards. You can sort dashboards by the following.

- Views
- Errors
- Views
- Created time
- Updated time
