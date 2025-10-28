# Populating an existing ID mapping table

When new data is added to an ID namespace, use this workflow. If you have chosen to turn
on incremental processing when you [created the ID mapping table](create-id-mapping-table.md#create-id-mapping-table-rule-based "create-id-mapping-table.md#create-id-mapping-table-rule-based"),
you have the ability to processes only new, updated, or deleted records in either the Source
or Target ID namespace, rather than recreating the entire ID mapping table.

###### To populate an existing ID mapping table

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms/](https://console.aws.amazon.com/cleanrooms/ "https://console.aws.amazon.com/cleanrooms/").
2. In the left navigation pane, choose **Collaborations**.
3. Choose the collaboration.
4. Go to the **Entity resolution** tab.
5. Under the **ID mapping tables** section, select an ID mapping
   table.
6. If you haven't turned on incremental processing for this ID mapping table, choose
   an ID mapping table and then choose **Populate**.
7. If you have turned on incremental processing for this ID mapping table, choose
   **Populate with** and then choose one of the following:
   - **Incremental processing** – Processes only new,
     updated, or deleted records in either the Source or Target ID
     namespace.

   Recommended for frequent updates, daily runs, or real-time data
   synchronization.
   - **Batch processing** – Processes the entire ID
     mapping table.

   Recommended for initial setup, periodic full refreshes, or when
   significant changes occur in both Source and Target ID namespaces.
   - **Delete only processing** – Processes only
     deleted records from the Source ID namespace and updates the Target ID
     namespace accordingly.

   Recommended for quickly synchronizing removals.

8. The ID mapping workflow process begins.

During this process, the ID mapping table is populated with transcoded IDs. The ID
mapping workflow might take a few hours to process.
After the ID mapping table is successfully populated, you can [query the ID
mapping table](query-id-mapping-tables.md "query-id-mapping-tables.md") to join the `sourceId` with the
`targetId`.
