# Connect to an InfluxDB data source

Grafana ships with a feature-rich data source plugin for InfluxDB. The plugin
includes a custom query editor and supports annotations and query templates.

## Adding the data source

1. Open the side menu by choosing the Grafana icon in the top header.
2. In the side menu under the link,**Dashboards** you
   should find a link named **Data Sources**.
3. Choose the **+ Add data source** button in the top
   header.
4. Select **InfluxDB** from the
   **Type** dropdown list.
5. Select **InfluxQL** or **Flux**
   from the **Query Language** list.

###### Note

If you don't see the **Data Sources** link in your side
menu, it means that your current user does not have the `Admin`
role.
