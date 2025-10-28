# Delete a data source in Amazon SageMaker Unified Studio

When you no longer need an Amazon DataZone data source, you can remove it permanently.
After you delete a data source, all assets that originated from that data source are
still available in the catalog, and users can still subscribe to them. However, the
assets will stop receiving updates from the source. We recommend that you first move the
dependent assets to a different data source before you delete it.

###### To delete a data source in the project catalog

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Choose **Select project** from the top navigation pane and
   select the project that contains the data source that you want to edit.
3. Choose **Data sources** from the left navigation pane under
   **Project catalog**.
4. Choose the data source that you want to delete.
5. Expand the **Actions** menu, then choose **Delete
   data source**.
6. To confirm deletion, type `delete` in the text entry field. Then
   choose **Delete**.
