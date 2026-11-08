

# Troubleshooting OpenSearch UI applications
<a name="application-troubleshooting"></a>

The following topics cover problems that are specific to OpenSearch UI. The sections in this topic cover problems that you can resolve inside the interface itself.

## Resolving no results in Discover
<a name="application-troubleshooting-no-results"></a>

If Discover reports that no results were found, check the following, in order:

1. **Expand the time range.** The default range is the last 15 minutes. Choose the date picker, and then choose a longer range, such as the last 7 days or the last 30 days.

1. **Check the index pattern.** The data source selector must point to the correct index pattern. If the list is empty, choose **Manage workspace**, choose **Index patterns**, and create one.

1. **Verify the time field.** The index pattern must have a valid time field. If the time field does not match the timestamp field in your data, Discover cannot find results.

## Resolving dashboard panel errors
<a name="application-troubleshooting-panels"></a>

A panel that reports `Expected exactly 1 result for data_source_name "X" but got 0 results` references a data source that does not exist in the current environment. This is common after a migration. Choose **Manage workspace**, choose **Data sources**, and confirm that the data source the visualization references is accessible.

## Resolving an empty data source selector
<a name="application-troubleshooting-empty-selector"></a>

If the data selector shows an empty list, you have not created any index patterns for the workspace. Choose **Manage workspace**, choose **Index patterns**, and create an index pattern before you continue.

## Switching to PPL or SQL in Discover
<a name="application-troubleshooting-query-language"></a>

**To change the query language in Discover**

1. Choose **DQL** next to the search bar.

1. In the language selector, choose **PPL** or **SQL**.

1. For PPL, begin the query with `source = {{index-name}}`.

## Improving slow dashboard loading
<a name="application-troubleshooting-slow"></a>
+ Reduce the time range. A 30-day range is substantially slower than a 7-day range.
+ Reduce the number of panels. Each panel runs a separate query.
+ Avoid wildcard index patterns, which can match more indexes than you need.
+ Check the health of the domain. Slow queries can indicate that the domain needs to be scaled.

**Topics**
+ [Resolving no results in Discover](#application-troubleshooting-no-results)
+ [Resolving dashboard panel errors](#application-troubleshooting-panels)
+ [Resolving an empty data source selector](#application-troubleshooting-empty-selector)
+ [Switching to PPL or SQL in Discover](#application-troubleshooting-query-language)
+ [Improving slow dashboard loading](#application-troubleshooting-slow)
+ [An OpenSearch UI application remains in the Creating state](application-troubleshooting-creating.md)
+ [Resolving sign-in and permission errors in OpenSearch UI](application-troubleshooting-auth.md)
+ [Resolving data source health and access errors in OpenSearch UI](application-troubleshooting-data-sources.md)
+ [Resolving VPC connectivity problems in OpenSearch UI](application-troubleshooting-vpc.md)