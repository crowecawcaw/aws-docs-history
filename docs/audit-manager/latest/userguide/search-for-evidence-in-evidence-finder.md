# Searching for evidence in evidence

finder

You can use evidence finder to perform targeted searches and quickly surface relevant
evidence for review.

On this page, you'll learn how to filter your searches by criteria like assessment, date
range, resource compliance status, and additional attributes. Applying these filters narrows your
search scope to just the evidence you need. You can also group your results by certain fields to
better analyze patterns.

## Prerequisites

Make sure that you completed the steps to enable evidence finder in your Audit Manager settings. For
instructions, see [Enabling evidence finder](evidence-finder-settings-enable.md "evidence-finder-settings-enable.md").

In addition, make sure that you have permissions to perform search queries in evidence
finder. For an example permission policy that you can use, see [Allow users to run search queries in
evidence finder](security_iam_id-based-policy-examples.md#evidence-finder-query-access "security_iam_id-based-policy-examples.md#evidence-finder-query-access").

## Procedure

Follow these steps to search for evidence in the Audit Manager console.

1. [Perform a search query](search-for-evidence-in-evidence-finder.md#performing-a-search "search-for-evidence-in-evidence-finder.md#performing-a-search")
2. [Stop an in-progress search query (optional)](search-for-evidence-in-evidence-finder.md#stopping-a-search "search-for-evidence-in-evidence-finder.md#stopping-a-search")
3. [Edit the filters for your search query (optional)](search-for-evidence-in-evidence-finder.md#editing-a-search "search-for-evidence-in-evidence-finder.md#editing-a-search")

###### Note

You can also use the CloudTrail API to query your evidence data. For more information, see
[StartQuery](../../../awscloudtrail/latest/APIReference/API_StartQuery.md "../../../awscloudtrail/latest/APIReference/API_StartQuery.md") in the _AWS CloudTrail API Reference_. If you
prefer to use the AWS CLI, see [Start a
query](../../../awscloudtrail/latest/userguide/query-lake-cli.md#lake-cli-start-query "../../../awscloudtrail/latest/userguide/query-lake-cli.md#lake-cli-start-query") in the _AWS CloudTrail User Guide_.

### Performing a search query

Follow these steps to perform a search query in evidence finder.

###### To search for evidence

1.  Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2.  In the navigation pane, choose **Evidence finder**.
3.  Next, apply filters to narrow the scope of your search.

        1. For **Assessment**, choose an assessment.
        2. For **Date range**, select a range.
        3. For **Resource compliance**, select an evaluation status.

    ![The required assessment, date range, and resource compliance filters in evidence finder.](images/evidence-finder-required_filters-console.png)

4.  (Optional) Choose **Additional filters - optional** to narrow the search even
    further.

        1. Choose **Add criteria**, select a criteria, and then select one or more
         values for that criteria.
        2. Continue to build more filters in the same way.
        3. To remove an unwanted filter, choose **Remove**.

    ![An additional filter for a specific control in evidence finder.](images/evidence-finder-additional_filters-console.png)

5.  Under **Grouping**, specify whether you want to group the search
    results.

        1. If you want to group the results, select a value to group the results by.
        2. If you don’t want to group the results, proceed to step 6.

    ![The group results option selected, with a chosen group by value.](images/evidence-finder-grouping-console.png)

6.  Choose **Search**.

![The search button to start a search query in evidence finder.](images/evidence-finder-search-console.png)

Your search might take a few minutes, depending on the amount of evidence data that you
have. Feel free to navigate away from evidence finder while the search is in progress. A flash
bar notifies you when the search results are ready.

### Stopping a search query

If you want to stop a search query for any reason, follow these steps.

###### Note

Stopping a search query can still result in charges. You're charged for the amount of
evidence data that was scanned before you stopped the search query. After it's stopped, you can
view the partial results that were returned.

###### To stop an in-progress search query

1. In the blue progress flash bar at the top of the screen, choose **Stop
   search**.

![The blue flash bar that indicates when a search query is in progress.](images/in_progress_search-evidence-finder-console.png) 2. (Optional) Review the partial results that were returned before you stopped the search
query.

    1. If you're on the evidence finder page, the partial results are displayed on the screen.
    2. If you navigated away from evidence finder, choose **View partial
     results** in the green confirmation flash bar.

![The green flash bar that indicates when a search was stopped.](images/stopped_search-evidence-finder-console.png)

### Editing search filters

Follow these steps to return to your most recent search query and adjust the filters as
needed.

###### Note

When you edit your filters and choose **Search**, this starts a new search
query.

###### To edit a recent search query

1. From the **View results** page, choose **Evidence finder**
   from the breadcrumb navigation menu.

![The breadcrumb navigation menu on the console with evidence finder highlighted.](images/breadcrumb_menu-evidence-finder-console.png) 2. Choose **Filters and grouping** to expand the filter selection.

![The expandable Filters and grouping section of evidence finder.](images/expand_filters-evidence-finder-console.png) 3. Next, edit your filters or start a new search.

    1. To edit filters, adjust or remove the current filters and grouping selection.
    2. To start over, choose **Clear filters** and apply the filters and grouping
     selection of your choice.

![The clear filters button that you can use to start over with a new search query.](images/evidence-finder-clear_filters-console.png) 4. When you’re done, choose **Search**.

![The search button to start a new search query in evidence finder.](images/evidence-finder-search-console.png)

## Next steps

After your search is finished, you can view the results that matched your search criteria.
For instructions, see [Viewing results in evidence
finder](viewing-search-results-in-evidence-finder.md "viewing-search-results-in-evidence-finder.md").

## Additional resources

- [Filter and grouping options for evidence
  finder](evidence-finder-filters-and-groups.md "evidence-finder-filters-and-groups.md")
- [Example use cases for evidence
  finder](example-use-cases-for-evidence-finder.md "example-use-cases-for-evidence-finder.md")
- [Troubleshooting evidence finder issues](evidence-finder-issues.md "evidence-finder-issues.md")
