NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Review source server alerts

The source server **Alerts** migration metric
presents an aggregated overview of the application associated servers alerts.
You can look up an individual source server **Alerts** status at the **Source
servers** table at the bottom of the page.

![Pie chart showing server status: 2 healthy servers (66.7%) and 1 launched server (33.3%).](images/app-7.png)

- A healthy server for which a test or cutover instance has not been
  launched will display a **Healthy** status.
- A healthy server for which a test of cutover instance has been
  launched will display a **Healthy** status.
- A server that is experiencing a temporary issue such as lag or backlog
  will display a **Lagging** status.
- A server that is experiencing significant issues, such as a stall,
  will display a **Stalled** status.
