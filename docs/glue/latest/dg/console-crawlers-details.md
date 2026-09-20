

# Viewing crawler results and details
<a name="console-crawlers-details"></a>

 After the crawler runs successfully, it creates table definitions in the Data Catalog. Choose **Tables** in the navigation pane to see the tables that were created by your crawler in the database that you specified. 

 You can view information related to the crawler itself as follows:
+ The **Crawlers** page on the AWS Glue console displays the following properties for a crawler:


<table>
<thead>
  <tr><th>Property</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><b>Name</b></td><td>When you create a crawler, you must give it a unique name.</td></tr>
  <tr><td><b>Status</b></td><td>A crawler can be ready, starting, stopping, scheduled, or schedule paused. A running crawler progresses from starting to stopping. You can resume or pause a schedule attached to a crawler.</td></tr>
  <tr><td><b>Schedule</b></td><td>You can choose to run your crawler on demand or choose a frequency with a schedule. For more information about scheduling a crawler, see <a href="schedule-crawler.md">Scheduling a crawler</a>.</td></tr>
  <tr><td><b>Last run</b></td><td> The date and time of the last time the crawler was run. </td></tr>
  <tr><td><b>Log</b></td><td>Links to any available logs from the last run of the crawler. </td></tr>
  <tr><td><b>Tables changes from last run</b></td><td>The number of tables in the AWS Glue Data Catalog that were updated by the latest run of the crawler.</td></tr>
</tbody>
</table>

+  To view the history of a crawler, choose **Crawlers** in the navigation pane to see the crawlers you created. Choose a crawler from the list of available crawlers. You can view the crawler properties and view the crawler history in the **Crawler runs** tab. 

   The Crawler runs tab displays information about each time the crawler ran, including ** Start time (UTC),** **End time (UTC)**, **Duration**, **Status**, **DPU hours**, and **Table changes**. 

  The Crawler runs tab displays only the crawls that have occurred since the launch date of the crawler history feature, and only retains up to 12 months of crawls. Older crawls will not be returned.
+ To see additional information, choose a tab in the crawler details page. Each tab will display information related to the crawler. 
  +  **Schedule**: Any schedules created for the crawler will be visible here. 
  +  **Data sources**: All data sources scanned by the crawler will be visible here. 
  +  **Classifiers**: All classifiers assigned to the crawler will be visible here. 
  +  **Tags**: Any tags created and assigned to an AWS resource will be visible here. 