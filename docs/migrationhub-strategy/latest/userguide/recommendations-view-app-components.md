AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Working with application components in

Strategy Recommendations

This section describes how to use Migration Hub Strategy Recommendations in the Migration Hub console to view and configure
migration and modernization strategy recommendations.

###### Topics

- [Viewing
  recommendations](#recommendations-view-app-components-details "#recommendations-view-app-components-details")
- [Configure source code
  analysis](#recommendations-source-code-config "#recommendations-source-code-config")
- [Configure database
  analysis](#recommendations-database-config "#recommendations-database-config")

## Viewing application

component recommendations

This section describes how to use Strategy Recommendations in the Migration Hub console to view migration
strategy recommendations for application components.

###### To view recommendations details for application components

1. Using the AWS account that you created in [Setting up Strategy Recommendations](setting-up.md "setting-up.md"), sign in to the AWS Management Console and open the Migration Hub
   console at [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/ "https://console.aws.amazon.com/migrationhub/").
2. In the Migration Hub console navigation pane, choose **Strategy** and
   then choose **Recommendations**.
3. On the **Recommendations** page, choose the
   **Application components** tab.
   1. Under **Application components summary**, is an
      overview of the various types of application components that you are
      running in your server portfolio.
   2. Under **Application components**, you view component
      name, component type, and migration "R" strategy recommendations. You
      can also view the migration destination, and the migration and
      modernization tools to use for various application components that are
      running in your server portfolio. For information about the "R"
      strategy, see [Migration terms - 7 Rs](../../../prescriptive-guidance/latest/migration-retiring-applications/apg-gloss.md#apg.migration.terms "../../../prescriptive-guidance/latest/migration-retiring-applications/apg-gloss.md#apg.migration.terms") in the _AWS Prescriptive
      Guidance_ glossary.

4. To view the details for an application component, select an application
   component and then choose **View details**.
5. On the application component details page (the page with the component's name
   as the heading) under **Recommendation summary**, you can view
   **Recommendations** for the application component. You can
   also view identified **Anti-patterns**. Anti-patterns are a
   list of known issues found in your portfolio that are categorized by severity.
6. Choose the **Strategy options** tab to view the migration
   recommendation for the application component. You can override the recommended
   strategy by selecting a different strategy and then choosing **Set
   preferred**.
7. Depending on which type of application component you are viewing, there is a
   **Source configuration** or a **Database
   configuration** tab. For information about **Source
   configuration**, see [Configure source code analysis for
   an application component](#recommendations-source-code-config "#recommendations-source-code-config"). For information about
   **Database configuration**, see [Configure database analysis for an
   application component](#recommendations-database-config "#recommendations-database-config").

## Configure source code analysis for

an application component

This section describes how to use Strategy Recommendations in the Migration Hub console to configure source
code analysis for an application component.

###### To configure source code analysis for an application component

1. In the Migration Hub console navigation pane, choose **Strategy** and
   then choose **Recommendations**.
2. On the **Recommendations** page, choose the
   **Application components** tab.
3. From the list of components under **Application components**,
   select an application component with a component type of
   **java**, **dotnetframework**, or
   **IIS**, and then choose **View
   details**.
4. On the application component details page (the page with the component's name
   as the heading), choose the **Source code configuration** tab.
5. Under **Source code configuration details**, choose
   **Analyze source code**.
6. On the **Analyze source code** page, provide the repository
   name, branch name, and project name (if applicable) that stores the source code for the application component.
   Select the type of GitHub source code version control that you want to use, and
   then choose **Analyze**.

After the analysis is complete, you can view the updated recommendations on
the application component details page.

For more information about source code analysis, see [Strategy Recommendations source code analysis](source-code-analysis.md "source-code-analysis.md").

## Configure database analysis for an

application component

This section describes how to use Strategy Recommendations in the Migration Hub console to configure database
analysis for an application component.

###### To configure database analysis for an application component

1. In the Migration Hub console navigation pane, choose **Strategy** and
   then choose **Recommendations**.
2. On the **Recommendations** page, choose the
   **Application components** tab.
3. From the list of components under **Application components**,
   select an application component with component type
   **SQLServer** and then choose **View
   details**.
4. On the application component details page (the page with the component's name
   as the heading), choose the **Database configuration**
   tab.
5. Under **Database configuration details**, choose
   **Analyze database details**.
6. Choose a secret name from the dropdown menu that you created in AWS
   Secrets Manager to use for database credentials, and then choose
   **Analyze**.

After the analysis is complete, you can view the updated recommendations on
the application component details page.

For more information about database analysis and setting up a secret name, see [Strategy Recommendations database analysis](database-analysis.md "database-analysis.md").
