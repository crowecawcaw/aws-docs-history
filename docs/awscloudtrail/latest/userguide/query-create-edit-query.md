# Create or edit a query with the CloudTrail console

In this walkthrough, we open one of the sample queries, edit it to find actions taken by a specific user named `Alice`, and save it as a new query. You can also edit a saved
query on the **Saved queries** tab, if you have saved queries. To help control costs, we recommend that you constrain queries by adding starting and
ending `eventTime` time stamps to queries.

1. Sign in to the AWS Management Console and open the CloudTrail console at
   [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. From the navigation pane, under **Lake**, choose **Query**.
3. On the **Query** page, choose the **Sample
   queries** tab.
4. Open a sample query by choosing the **Query name**. This
   opens the query in the **Editor** tab. In this example, we'll
   select the query named **Investigate user actions** and edit
   the query to find the actions for a specific user named
   `Alice`.
5. In the **Editor** tab, edit the `WHERE` line to specify the user that you want to investigate and
   update the `eventTime` values as needed. The value of `FROM` is the ID portion of the event data
   store's ARN and is automatically populated by CloudTrail when you choose the event data store.

```
SELECT
    eventID, eventName, eventSource, eventTime, userIdentity.arn AS user
FROM
    `event-data-store-id`
WHERE
    userIdentity.arn LIKE '%`Alice`%'
    AND eventTime > '2023-06-23 00:00:00' AND eventTime < '2023-06-26 00:00:00'
```

6. You can run a query before you save it, to verify that the query works. To run
   a query, choose an event data store from the **Event data
   store** drop-down list, and then choose **Run**.
   View the **Status** column of the **Command
   output** tab for the active query to verify that a query ran
   successfully.
7. When you have updated the sample query, choose
   **Save**.
8. In **Save query**, enter a name and description for the
   query. Choose **Save query** to save your changes as the new
   query. To discard changes to a query, choose **Cancel**, or
   close the **Save query** window.

![Saving a changed query](images/query-save.png)

###### Note

Saved queries are tied to your browser; if you use a different browser or
a different device to access the CloudTrail console, the saved queries are not
available. 9. Open the **Saved queries** tab to see the new query in the
table.

![Saved queries tab showing the new saved query](images/query-saved-table.png)
