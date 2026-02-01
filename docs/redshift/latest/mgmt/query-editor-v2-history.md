Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Viewing query and tab history

You can view your query history with query editor v2. Only queries that you ran using query editor v2
appear in the query history. Both queries that ran from using an
**Editor** tab or **Notebook** tab are shown. You
can filter the list displayed by a time period, such as `This week`, where a
week is defined as Monday–Sunday. The list of queries fetches 25 rows of queries
that match your filter at a time. Choose **Load more** to see the next
set. Choose a query and from the **Actions** menu. The actions
available depend on whether the chosen query has been saved. You can choose the
following operations:

- **View query details** – Displays a query details page
  with more information about the query that ran.
- **Open query in a new tab** – Opens a new editor tab
  and primes it with the chosen query. If still connected, the cluster or
  workgroup and database are automatically selected. To run the query, first
  confirm that the correct cluster or workgroup and database are chosen.
- **Open source tab** – If it is still open, navigates
  to the editor or notebook tab that contained the query when it ran. The contents
  of the editor or notebook might have changed after the query ran.
- **Open saved query** – Navigates to the editor or
  notebook tab and opens the query.
  You can also view the history of queries run in an **Editor** tab or
  the history of queries run in a **Notebook** tab. To see a history of
  queries in a tab, choose **Tab history**. Within the tab history, you
  can do the following operations:

- **Copy query** – Copies the query version SQL content
  to the clipboard.
- **Open query in a new tab** – Opens a new editor tab
  and primes it with the chosen query. To run the query, you must choose the
  cluster or workgroup and database.
- **View query details** – Displays a query details page
  with more information about the query that ran.
