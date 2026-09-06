

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# Viewing strategy recommendations in Strategy Recommendations
<a name="viewing-recommendations"></a>

This section describes how to use Strategy Recommendations in the AWS Migration Hub console to view migration strategy recommendations.

**To view strategy recommendations**

1. Using the AWS account that you created in [Setting up Strategy Recommendations](setting-up.md), sign in to the AWS Management Console and open the Migration Hub console at [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/).

1. In the Migration Hub console navigation pane, choose **Strategy** and then choose **Recommendations**.

1. On the **Recommendations** page, you can view and export summary recommendations of your portfolio and detailed migration "R" strategy recommendations. You can also view migration and modernization tools and destinations, and anti-patterns for your servers and application components. 

   Anti-patterns are a list of known issues found in your portfolio that are categorized by severity. High severity anti-patterns represent incompatibilities that need to be resolved, medium severity anti-patterns represent warnings, and low severity anti-patterns represent informational issues. For information about the "R" strategy, see [Migration terms - 7 Rs](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-retiring-applications/apg-gloss.html#apg.migration.terms) in the *AWS Prescriptive Guidance* glossary.

   1. If a change occurs in your data center or if you update your preferences, we recommend reanalyzing your data. To reanalyze your data to get new recommendations, choose **Reanalyze data**. 

     Until the reanalyze process completes, your recommendation data results can be a mix of prior data and new data.

     To download a report file with the recommendations, Choose **Export recommendations**.

1. On the **Application components** tab, you can view the recommendations for application components in your migration portfolio. For more information, see [Strategy Recommendations application component recommendations](recommendations-app-components.md).

1.  On the **Servers** tab, you can view the recommendations for the servers in your migration portfolio. For more information, see [Strategy Recommendations server recommendations](recommendations-servers.md).

1.  On the **Preferences** tab, you can edit the preferences you specified in [Step 5: Get recommendations](getting-started-get-recommendations.md). For information about editing your preferences, see [Strategy Recommendations preferences](recommendations-preferences.md). 