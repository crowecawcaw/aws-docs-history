# Visualizing your Storage Lens groups data

You can visualize your Storage Lens groups data by [attaching the group to your Amazon S3 Storage Lens dashboard](storage-lens-groups-dashboard-console.md#storage-lens-groups-attach-dashboard-console "storage-lens-groups-dashboard-console.md#storage-lens-groups-attach-dashboard-console"). After you've included
the Storage Lens group in the Storage Lens group aggregation in your dashboard
configuration, it can take up to 48 hours for the Storage Lens group data to display in
your dashboard.

After the dashboard configuration has been updated, any newly attached Storage Lens groups
appear in the list of available resources under the **Storage Lens groups**
tab. You can also further analyze storage usage in your **Overview** tab by
slicing the data by another dimension. For example, you can choose one of the items listed
under the **Top 3** categories and choose **Analyze by**
to slice the data by another dimension. You can't apply the same dimension as the filter
itself.

###### Note

You can't apply a Storage Lens group filter along with a prefix filter, or the
reverse. You also can't further analyze a Storage Lens group by using a prefix
filter.

You can use the **Storage Lens groups** tab in the Amazon S3 Storage Lens
dashboard to customize the data visualization for the Storage Lens groups that are
attached to your dashboard. You can either visualize the data for some Storage Lens
groups that are attached to your dashboard, or all of them.

When visualizing Storage Lens group data in your S3 Storage Lens dashboard, be aware of the
following:

- S3 Storage Lens aggregates usage metrics for an object under all matching Storage
  Lens groups. Therefore, if an object matches the filter conditions for two or
  more Storage Lens groups, you will see repeated counts for the same object
  across your storage usage.
- Objects must match the filters that you include in your Storage Lens groups.
  If no objects match the filters that you include in your Storage Lens group,
  then no metrics are generated. To determine if there are any unassigned objects,
  check your total object count in the dashboard at the account level and bucket
  level.
