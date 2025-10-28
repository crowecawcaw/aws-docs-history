# Manually start a data source run in

Amazon SageMaker Unified Studio

When you run a data source, Amazon SageMaker Unified Studio pulls all any new or modified metadata from the
source and updates the associated assets in the inventory. When you add a data source to
Amazon SageMaker Unified Studio, you specify the source's run preference, which defines whether the source
runs on a schedule or on demand. If your source runs on demand, you must initiate a data
source run manually.

Even if your source runs on a schedule, you can still run it manually at any time.
After adding business metadata to the assets, you can select assets and publish them to
the Amazon SageMaker Catalog in order for these assets to be discoverable by all domain users.
Only published assets are searchable by other domain users.

###### To run a data source manually

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Choose **Select project** from the top navigation pane and
   select the project to which the data source belongs.
3. Choose **Data sources** from the left navigation pane under
   **Project catalog**.
4. Choose the data source that you want to run. This opens the data source
   details page.
5. Choose **Run**.

The data source status changes as Amazon SageMaker Unified Studio updates the asset metadata with
the most recent data from the source. You can monitor the status of the run on
the **Data source runs** tab.
