# Delete a data source in Amazon DataZone

After you create an Amazon DataZone data source, you can modify it at any time to change
the source details or the data selection criteria.

To complete these steps, you must have the
**AmazonDataZoneFullAccess** AWS managed policy attached. For
more information, see [AWS managed policies for Amazon DataZone](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

When you no longer need an Amazon DataZone data source, you can remove it permenantly.
After you delete a data source, all assets that originated from that data source are
still available in the catalog, and users can still subscribe to them. However, the
assets will stop receiving updates from the source. We recommend that you first move the
dependent assets to a different data source before you delete it.

###### Note

You must remove all fulfillments on the data source before you can delete it. For
more information, see [Amazon DataZone data discovery, subscription,
and consumption](discover-subscribe-consume-data.md "discover-subscribe-consume-data.md").

###### To delete a data source

1. On the **Data** tab for the project, choose **Data
   sources** from the left navigation pane.
2. Choose the data source that you want to delete.
3. Choose **Actions**, **Delete data source**
   and confirm deletion.
