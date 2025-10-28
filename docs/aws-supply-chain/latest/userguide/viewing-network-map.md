# Viewing the network map

After ingesting the required datasets for Insights, the network map displays the current and projected inventory for products and locations
in a map view for quick understanding of your inventory health and projected health. Locations appear in clusters, and the total number of locations appear under each cluster. You can zoom in on each cluster to see individual locations. Each icon represents
a location type. The colored ring shows the inventory health for each location or cluster for the selected time interval on the scroll bar at the bottom left. Inventory health status depends on the inventory policy, that is, _min_safety_stock_ and _max_safety_stock_ in your ingested data.

The ring colors are defined as follows:

###### Note

The color code definitions remain the same throughout Insights.

- **Red** – Products in this location are stocked out or are at risk of a stock out for future dates.
- **Green** – Products in this location are well within your safety stock levels.
- **Purple** – Products in this location have excess stock or are at risk of a holding more stock than your safety stock levels for this product and site.
  To view the network map, perform the following procedure.

1. In the left navigation pane on the AWS Supply Chain dashboard, choose
   **Network Map**.

The **Network Map** page appears.

![Viewing the network map](images/insights_network_map.png) 2. Select a ring and zoom in on a location that you need. You can view the details of the
current and projected inventory for one or more particular items. 3. Use the timeslider on the bottom left of the page to view the projected inventory for the
current map view. The slider defaults to current date representing current inventory health. 4. Click the **+/-** symbol to zoom in and out of a particular location in
the network map. 5. Click the **Filter** icon to filter by **Locations**
and **Products**. Your permissions determine your level of access.
When you click on a cluster of sites, you will see a pop-up on the right side of the page, which displays the current inventory levels, safety stock levels for this product, and projected inventory graph.
