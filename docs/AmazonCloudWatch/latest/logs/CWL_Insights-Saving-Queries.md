# Save and re-run CloudWatch Logs Insights queries

After you create a query, you can save it, and run it again later. Queries are saved
in a folder structure, so you can organize them. You can save as many as 1000 queries
per region and per account.

Queries are saved on a Region-specific level, not a user-specific level. If you create
and save a query, other users with access to CloudWatch Logs in the same Region can see all saved
queries and their folder structures in the Region.

To save a query, you must be logged into a role that has the permission
`logs:PutQueryDefinition`. To see a list of your saved queries, you must
be logged into a role that has the
permission`logs:DescribeQueryDefinitions`.

###### To save a query

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Logs**, and then choose
   **Logs Insights**.
3. In the query editor, create a query.
4. Choose **Save**.

If you don't see a **Save** button, you need to change to the
new design for the CloudWatch Logs console. To do so:

    1. In the navigation pane, choose **Log groups**.
    2. Choose **Try the new design**.
    3. In the navigation pane, choose **Insights** and
     return to step 3 of this procedure.

5. Enter a name for the query.
6. (Optional) Choose a folder where you want to save the query. Select
   **Create new** to create a folder. If you create a new
   folder, you can use slash (/) characters in the folder name to define a folder
   structure. For example, naming a new folder
   `folder-level-1/folder-level-2` creates a top-level
   folder called `folder-level-1`, with another folder called
   `folder-level-2` inside that folder. The query is saved
   in `folder-level-2`.
7. (Optional) Change the query's log groups or query text.
8. Choose **Save**.

###### Tip

You can create a folder for saved queries with `PutQueryDefinition`.
To create a folder for your saved queries, use a forward slash (/) to prefix your
desired query name with your desired folder name:
`<`folder-name`>/<`query-name`>`.
For more information about this action, see [PutQueryDefinition](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutQueryDefinition.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutQueryDefinition.md").

###### To run a saved query

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Logs**, and then choose
   **Logs Insights**.
3. On the right, choose **Queries**.
4. Select your query from **Saved queries** list. It appears in
   the query editor.
5. Choose **Run**.

###### To save a new version of a saved query

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Logs**, and then choose
   **Logs Insights**.
3. On the right, choose **Queries**.
4. Select your query from **Saved queries** list. It appears in
   the query editor.
5. Modify the query. If you need to run it to check your work, choose
   **Run query**.
6. When you are ready to save the new version, choose
   **Actions**, **Save as**.
7. Enter a name for the query.
8. (Optional) Choose a folder where you want to save the query. Select
   **Create new** to create a folder. If you create a new
   folder, you can use slash (/) characters in the folder name to define a folder
   structure. For example, naming a new folder
   `folder-level-1/folder-level-2` creates a top-level
   folder called `folder-level-1`, with another folder called
   `folder-level-2` inside that folder. The query is saved
   in `folder-level-2`.
9. (Optional) Change the query's log groups or query text.
10. Choose **Save**.
    To delete a query, you must be logged in to a role that has the
    `logs:DeleteQueryDefinition` permission.

###### To edit or delete a saved query

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Logs**, and then choose
   **Logs Insights**.
3. On the right, choose **Queries**.
4. Select your query from **Saved queries** list. It appears in
   the query editor.
5. Choose **Actions**, **Edit** or
   **Actions**, **Delete**.
