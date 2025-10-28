# Troubleshoot no metrics or too few rows in a

queues report in Amazon Connect

It's possible to run a manually configured queues report and have no metrics
returned, or fewer rows than expected.

This is because a queues report only includes data for a maximum of 500 queues,
using one row per queue. If a queue doesn't have any activity\* during the time range
for the report, it's excluded from the report rather than included with null values.
This means that if you create a report, and there is no activity for any of the
queues included in the report, your report will not include any data.

This applies to the `GetCurrentMetricsData` API as well. This means
that if a queue is not considered active, if you query for its metrics using the API
you won't get any data.

###### Tip

\*Here's how we define whether a queue is active: there's at least one contact
in queue or there's at least one online agent for that queue. Otherwise, it's
considered inactive.

Real-time metrics reports do not include agents who have been inactive for
approximately the past 5 minutes. For example, after the agent changes their CCP
status to **Offline**, their username continues to appear in
the Real-time metrics report for another approximately 5 minutes. At the 5
minute point, the agent no longer appears in the report.

In the following situations, you could end up with no metrics or fewer rows than
expected:

1. You're attempting to run a report with no filters or groupings, and have
   more than 500 queues in your instance. The report pulls metrics for the
   first 500 queues, and then displays only those that are active.
2. You're attempting to run a report with filters and groupings, but it still
   has more than 500 queues matching that criteria. To process this request,
   Amazon Connect applies all the specified filters and groupings. This
   pulls the first 500 queues matching that criteria. Then out of those queues,
   it displays only the active ones.

For example, let's say you have 600 queues in your instance. Of these, 200
match your criteria; 100 are active and by coincidence all happen to be
Queues #500-#600. When you run the report, you'd get just 1 row (Queue #500)
since the other 499 queues that were returned (Queues #1-#499) were
considered inactive and were not displayed. 3. You're running a report with fewer than 500 queues. While you may expect
to see metrics for all filtered queues, only active queues are shown on the
real-time metrics report page. Try changing the settings for the report,
such as changing the time range. 4. If you as a user don't have any tags assigned to you
(in other words, you have access to every queue in your Amazon Connect instance),
then the metrics page randomly selects 100 queues from your Amazon Connect instance
and any filters/groupings are applied to those 100 queues only.
The same applies for other resources that can be tagged.
This is done to limit the amount of data so dashboard performance is optimized.
