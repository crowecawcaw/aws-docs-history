# Log group selection options when creating a query

This section explains the various ways that you can select log groups to include
in a query.

###### To select log groups for a query in the console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Logs**, **Logs
   Insights**.
3. Select the query language you want to use for this query. You can choose
   either: **Logs Insights QL**, **OpenSearch
   PPL**, or **OpenSearch SQL**.
4. There are three ways to select log groups for the query:
   - Use the **Log group name** box. This is the
     default selection method. You can enter as many as 50 log group
     names with this method. If this is a monitoring account in CloudWatch
     cross-account observability, you can select log groups in the source
     accounts as well as the monitoring account. A single query can query
     logs from different accounts at once.
   - Use the **Log group criteria** section. In this
     section, you can choose log groups based on the prefix of the log
     group names. You can include as many as five prefixes in one query.
     Log groups having these prefixes in their names will be selected.
     Alternatively, the **All log groups** option
     selects all the log groups from the account.
   - If this is a monitoring account in CloudWatch cross-account
     observability, you can select **All accounts** in
     the account dropdown menu to select the log groups from all linked
     accounts. Alternatively, you can individually select which accounts
     should be included for this query.If your choices match more than 10,000 log groups, you'll see an error
     that prompts you to narrow your selection.

5. The default log class for a query is **Standard**. You
   can use **Log class** to change it to **Infrequent
   access**.
   **Using the AWS CLI**

To make these types of selections when you start a query from the command line,
you can use the `source` command in your query. For more information and
examples, see [SOURCE](CWL_QuerySyntax-Source.md "CWL_QuerySyntax-Source.md").
