AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Strategy Recommendations server recommendations

This section describes how to use Migration Hub Strategy Recommendations in the Migration Hub console to view migration
strategy recommendations for the servers in your migration portfolio.

###### To view recommendations for servers

1. Using the AWS account that you created in [Setting up Strategy Recommendations](setting-up.md "setting-up.md"), sign in to the AWS Management Console and open the Migration Hub
   console at [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/ "https://console.aws.amazon.com/migrationhub/").
2. In the Migration Hub console navigation pane, choose **Strategy** and
   then choose **Recommendations**.
3. On the **Recommendations** page, choose the
   **Servers** tab.
   1. Under **Server summary**, you view an overview of the
      various types of servers that you are running in your portfolio.
   2. Under **Servers**, you view server and operating system
      details and migration "R" strategy recommendations. You can also view the
      migration destination and the number of anti-patterns identified on your
      servers, which are based on the recommendations. For information about the
      "R" strategy, see [Migration terms - 7 Rs](../../../prescriptive-guidance/latest/migration-retiring-applications/apg-gloss.md#apg.migration.terms "../../../prescriptive-guidance/latest/migration-retiring-applications/apg-gloss.md#apg.migration.terms") in the _AWS Prescriptive
      Guidance_ glossary.

4. To view in-depth recommendation details for a server, select the server from the
   list, and then choose **View details**. You can view the metadata
   collected for the server, along with in-depth analysis and recommendations for it,
   which are based on the application components found running on the server.
5. On the server details page (the page with the server's name as the heading),
   under **Recommendation summary**, you can see an overview of
   **Strategy recommendations** for the server. You can also view
   identified **Anti-patterns**. Anti-patterns are a list of known
   issues found in your portfolio that are categorized by severity.
6. Choose the **Strategy options** tab to view the migration
   recommendation for the server. You can override the recommended strategy by
   selecting a different strategy and then choosing **Set
   preferred**.
7. Choose the **Application components** tab to view the list of
   application components associated with the server.
8. To view details about the application component, select the component from the
   list and then choose **View details.** For more information about
   application components, see [Working with application
   components](recommendations-view-app-components.md "recommendations-view-app-components.md").
