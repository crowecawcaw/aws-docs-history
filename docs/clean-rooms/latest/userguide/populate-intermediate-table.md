# Populating an intermediate table

After you create an intermediate table, you must populate it to materialize data. You can
also repopulate an intermediate table to refresh the data when base tables are updated.

Each populate operation creates a new version of the intermediate table. The previous
version remains available during the refresh. If the refresh fails, the existing data is not
affected.

###### Note

Populating an intermediate table decrements access budgets on all referenced base tables,
including transitive dependencies.

###### Note

Populating an intermediate table starts a query to store the data in the service. This
query counts towards your quotas for concurrent SQL queries per account and concurrent SQL
query vCPU usage per account. For more information, see [AWS Clean Rooms quotas](clean-rooms-quotas.md "clean-rooms-quotas.md").

###### To populate an intermediate table

1. Open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms/](https://console.aws.amazon.com/cleanrooms/ "https://console.aws.amazon.com/cleanrooms/").
2. In the left navigation pane, choose **Collaborations**.
3. Choose the collaboration, and then choose the **Tables** tab.
4. Choose the intermediate table that you want to populate.
5. Choose **Populate**.
6. In the **Populate** dialog, review the stored analysis (SQL query or
   analysis template reference).
7. Configure the following settings:

   - **Query compute payer** – If your collaboration has multiple
     query compute payers, select the one that pays for query compute costs for the populate
     operation.
   - **Worker type** – The instance type for the populate job
     (default: CR.1X).
   - **Number of workers** – The number of instances to use
     (2–128, default: 16).
   - (Optional) **Spark properties** – Custom Spark runtime
     configuration.

8. Choose **Populate**.
   **Tracking progress**

To view the status of a populate operation, choose the **Analysis** tab on
the intermediate table details page. You can view the following information:

- Protected query ID (linked to query details)
- Status
- Worker type
- Number of workers
- Billed CRPU hours
