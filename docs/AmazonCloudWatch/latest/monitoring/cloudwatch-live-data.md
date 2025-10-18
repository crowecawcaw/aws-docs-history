# Using live data in CloudWatch dashboards

You can choose whether your metric widgets display *live data*. Live data
 is data published within the last minute that has not been fully aggregated.


* If live data is turned **off**, only data points with an aggregation period
 of at least one minute in the past are shown. For example, when using 5-minute periods, 
 the data point for 12:35 would be aggregated from 12:35 to 12:40, and displayed at 12:41.
* If live data is turned **on**, the most recent
 data point is shown as soon as any data is published in the corresponding aggregation interval. 
 Each time you refresh the display, the most recent data point may change as new data within that 
 aggregation period is published. If you use a cumulative statistic such as **Sum**
 or **Sample Count**, using live data may result in a dip at the end of your graph.
You can choose to enable live data for a whole dashboard, or for individual widgets on the dashboard.
