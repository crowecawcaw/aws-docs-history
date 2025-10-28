AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Viewing strategy recommendations in

Strategy Recommendations

This section describes how to use Strategy Recommendations in the AWS Migration Hub console to view migration
strategy recommendations.

###### To view strategy recommendations

1. Using the AWS account that you created in [Setting up Strategy Recommendations](setting-up.md "setting-up.md"), sign in to the AWS Management Console and open the Migration Hub
   console at [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/ "https://console.aws.amazon.com/migrationhub/").
2. In the Migration Hub console navigation pane, choose **Strategy** and
   then choose **Recommendations**.
3. On the **Recommendations** page, you can view and export summary
   recommendations of your portfolio and detailed migration "R" strategy
   recommendations. You can also view migration and modernization tools and
   destinations, and anti-patterns for your servers and application components.

Anti-patterns are a list of known issues found in your portfolio that are
categorized by severity. High severity anti-patterns represent incompatibilities
that need to be resolved, medium severity anti-patterns represent warnings, and low
severity anti-patterns represent informational issues. For information about the "R"
strategy, see [Migration terms - 7 Rs](../../../prescriptive-guidance/latest/migration-retiring-applications/apg-gloss.md#apg.migration.terms "../../../prescriptive-guidance/latest/migration-retiring-applications/apg-gloss.md#apg.migration.terms") in the _AWS Prescriptive
Guidance_ glossary.

    1. If a change occurs in your data center or if you update your preferences,
     we recommend reanalyzing your data. To reanalyze your data to get new
     recommendations, choose **Reanalyze data**.


    Until the reanalyze process completes, your recommendation data results
     can be a mix of prior data and new data.


    To download a report file with the recommendations, Choose
     **Export recommendations**.

4. On the **Application components** tab, you can view the
   recommendations for application components in your migration portfolio. For more
   information, see [Strategy Recommendations application component
   recommendations](recommendations-app-components.md "recommendations-app-components.md").
5. On the **Servers** tab, you can view the recommendations for the
   servers in your migration portfolio. For more information, see [Strategy Recommendations server recommendations](recommendations-servers.md "recommendations-servers.md").
6. On the **Preferences** tab, you can edit the preferences you
   specified in [Step 5: Get
   recommendations](getting-started-get-recommendations.md "getting-started-get-recommendations.md"). For information about
   editing your preferences, see [Strategy Recommendations preferences](recommendations-preferences.md "recommendations-preferences.md").
