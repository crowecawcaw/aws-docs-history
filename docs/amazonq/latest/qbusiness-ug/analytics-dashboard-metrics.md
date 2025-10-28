# Amazon Q Business Analytics dashboard

metrics

The Amazon Q Business dashboard provides a comprehensive view of key metrics to help admins
understand the performance and usage of every Amazon Q application environment from the Amazon Q Business
console.

The following analytics are available in the dashboard for the specified time
period.

- **Average daily active users**

This tile gives the average number of unique daily users for the application
environment that participated in at least one chat session for the chosen period.

###### Note

This metric is calculated using the _Maximum_ statistic. For more
information, see [CloudWatch
statistics definitions](../../../AmazonCloudWatch/latest/monitoring/Statistics-definitions.md "../../../AmazonCloudWatch/latest/monitoring/Statistics-definitions.md").

- **Total users**

All the users of this application environment.

- **Weekly active users**

This tile gives the total number of unique users for the application environment who
participated in at least one chat session for the week in the chosen period.

- **Monthly active users**

This tile gives the total number of unique users for the application environment who
participated in at least one chat session for the month in the chosen period.

- **Total conversations**

This tile gives the total number of chat conversations that have occurred in this
application environment. Conversations are different from individual chat queries and represent a
collection of related queries and responses over a relevant session or subject.

- **Total queries**

This tile gives the total number of chat message queries received by this
application environment.

- **Average queries per user**

This tile gives the average of daily chat queries for divided by the daily active
unique users for that application environment for the chosen period.

- **Average queries per conversation**

This tile gives the average of total chat queries to an application environment divided by the
total individual conversations in the application environment. Conversations refer to new chat
threads, which are listed on the left navigation pane of the web experience for the
application environment.

- **Total plugins**

This tile shows the total number of plug-ins currently used by this
application environment.

- **Most frequently used plugin**

This tile shows the plug-in most frequently used by this application environment.

- The **Overview** trend

This line chart displays two trend lines - one showing the daily active users for each
day for the application environment, and another showing the total daily individual chat queries
received by the application environment.

- The **Customer feedback** trend

This line chart displays three trend lines for the application environment.

    + The number of thumbs up feedback.
    + The number of thumbs down feedback.
    + The number of chat message responses that did not receive any feedback thumbs up
     or thumbs down).

- The **Thumbs down reasons** chart

This pie chart represents the different feedback reasons that users choose when
providing a thumbs down feedback, along with the count or percentage of times each reason
was selected. You can also filter by feedback reasons to further see the top queries that
resulted in the feedback or choose **view details to resolve issues** to
see all the queries for further evaluation.

    + The **Thumbs-down feedback queries**



    This page shows the list of queries that resulted in an unsuccessful response for
     further evaluation. You can choose any query to view details and see
     **Recommendations** on how to possibly resolve the issue.


    ###### Note



    	- A maximum of *5000* query responses will be loaded
    	 initially for evaluation. You can always search for specific queries.
    	- The empty columns in some rows indicate that you need to update the
    	 **Vended log deliveries** configuration in
    	 **Admin-controls-guardrails page**.

- The **Unsuccessful query responses** chart

This pie chart represents the breakdown between unsuccessful query responses because
the answer was not found or the answer was blocked due to your guardrails settings. You
can also filter by response type further to see the top queries that resulted in the
response or choose **view details to resolve** issues to see all the
queries for further evaluation.

    + The **Unsuccessful response queries**



    This page shows the list of queries that resulted in an unsuccessful response for
     further evaluation. You can choose any query to view details and see
     **Recommendations** on how to possibly resolve the issue.


    ###### Note



    	- A maximum of *5000* query responses will be loaded
    	 initially for evaluation. You can always search for specific queries.
    	- The empty columns in some rows indicate that you need to update the
    	 **Vended log deliveries** configuration in
    	 **Admin-controls-guardrails page**.

- The **Queries** trend

This chart displays three trend lines.

    + The number of chat queries that included a file upload.
    + The number of instances where the chat queries was blocked by the guardrails
     set.
    + The number of instances where the application environment was unable to find a relevant
     answer to the user's query.

- The **Plugins** chart

This bar chart shows the number of times users have selected each of the available
plugins per day. For example, _ServiceNow_,
_Salesforce_, _JIRA_,
_Zendesk_, _Custom_, etc. when sending a query to
the application environment.

- The **Conversations** chart

This bar chart shows the total number of conversations per day for the specified date
range. Conversations are different from individual chat queries, and represent a
collection of related queries and responses over a relevant session.

- The **Average queries per conversation** trend

This bar chart calculates the average number of queries per conversation by dividing
the total number of daily queries by the total number of conversations per day for the
application environment. Conversations are listed on the left navigation pane of the web experience,
and each conversation represents a collection of related chat messages. The chart
indicates the average length of conversations, as measured by the total number of chat
messages from the first to the last message in a given conversation thread.
