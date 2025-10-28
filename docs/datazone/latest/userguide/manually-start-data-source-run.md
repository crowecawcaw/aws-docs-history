# Manually start a data source run in

Amazon DataZone

When you run a data source, Amazon DataZone pulls all any new or modified metadata from the
source and updates the associated assets in the inventory. When you add a data source to
Amazon DataZone, you specify the source's run preference, which defines whether the source
runs on a schedule or on demand. If your source runs on demand, you must initiate a data
source run manually.

Even if your source runs on a schedule, you can still run it manually at any time.
After adding business metadata to the assets, you can select assets and publish them to
the Amazon DataZone catalog in order for these assets to be discoverable by all domain users.
Only published assets are searchable by other domain users.

###### To run a data source manually

1. Navigate to the Amazon DataZone data portal URL and sign in using single sign-on
   (SSO) or your AWS credentials. If you’re an Amazon DataZone administrator, you can
   navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with the
   AWS account where the domain was created, then choose **Open data
   portal**.
2. Choose **Select project** from the top navigation pane and
   select the project to which the data source belongs.
3. Navigate to the **Data** tab for the project.
4. Choose **Data sources** from the left navigation pane, then
   locate and choose the data source that you want to run. This opens the data
   source details page.
5. Choose **Run on demand**.

The data source status changes to `Running` as Amazon DataZone updates
the asset metadata with the most recent data from the source. You can monitor
the status of the run on the **Data source runs** tab.
