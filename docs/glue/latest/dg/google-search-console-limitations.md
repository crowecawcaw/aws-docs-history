

# Google Search Console limitations
<a name="google-search-console-limitations"></a>

The following are limitations or notes for Google Search Console:
+ Google Search Console enforces usage limits on the API. For more information, see [Usage Limits](https://developers.google.com/webmaster-tools/limits).
+ When no filter is passed for the `Search Analytics` entity, the API sums up all the clicks, impressions, CTR, and other data for your entire site within the specified default date range and presents it as a single record.
+ To breakdown the data into smaller segments, you need to introduce dimensions to your query. Dimensions tells the API how you want to segment your data.
  + For example, if you add `filterPredicate: dimensions="country"` you'll get one record for each country where your site received traffic during the specified period.
  + Example to pass multiple dimensions: `filterPredicate: dimensions="country" AND dimensions="device" AND dimensions="page"`. In this case you'll get one row in the response for each unique combination of these three dimensions.
+ Default values are set for the `start_end_date` and `dataState` fields. 


<table>
<thead>
  <tr><th>Field name</th><th>Default filter expression</th><th>Expression to override default values</th></tr>
</thead>
<tbody>
  <tr><td>start_end_date</td><td>start_end_date between &lt;30 days ago from current date&gt; AND &lt;yesterday: that is, 1 day ago from the current date&gt;</td><td>start_end_date between "2024-01-01" AND "2024-05-05"</td></tr>
  <tr><td>dateState</td><td>dataState="all"</td><td>dataState="final"</td></tr>
</tbody>
</table>
