# Costs for Insights events

###### Note

Insights events on data events are only supported on trails.

When you enable Insights events on an existing trail or event data store, CloudTrail
analyzes the past 28 days of management and data events collected by the trail or event data
store to establish a baseline of normal activity. After the initial baseline is created,
the baseline is recalculated every day on the past 28 days of data.
There are no CloudTrail charges for the baseline analysis.

After the baseline analysis, you incur CloudTrail charges for any future management and data events
analyzed by CloudTrail. You incur charges based on the number of management and data events analyzed
for the enabled Insights types.

If you choose to log both API call rate and API error rate Insights types for management events for a trail or event data store that logs
`read` and `write` management events, the total number of
events analyzed will be greater than the total number of recorded management events.
This is because CloudTrail will analyze the write-only management events twice, once for
calculating the API call rate and again for determining the API error rate. The
read-only management events will be analyzed once to calculate the API error
rate.

Similarly, if you choose to log both API call rate and API error rate Insights types for data events for a trail that logs
`read` and `write` data events, the total number of
events analyzed will be greater than the total number of recorded data events.
This is because CloudTrail will analyze all data events twice, once for
calculating the API call rate and again for determining the API error rate.

You can identify the charges for Insights for management and data events on your bill by looking for the
`InsightsEvents` and `DataInsightsEvents` usage type respectively. For more information, see [Viewing your CloudTrail cost and usage with AWS Cost Explorer](cloudtrail-costs.md "cloudtrail-costs.md").

You will incur separate Insights charges for both trails and event data stores, and separate data events Insights for trails.
For more information about pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

**Example 1 – Enable Insights on management events for API call rate and API
error rate on a trail**

In this first example, you enable Insights on a trail logging management events and choose to collect both Insights types. The trail in this example is
logging both `read` and `write` management events.

- CloudTrail analyzes the management events logged in the past 28 days to form a
  baseline. There are no CloudTrail charges for the analysis.
- After the baseline is created, the trail logs 300,000 management
  events, of which 270,000 are `read` management events and 30,000 are
  `write` management events.

      + The `write` management events are analyzed twice, once for the API
       call rate and once for the API error rate (30,000 \* 2=60,000).
      + The `read` management events are analyzed once for the API error
       rate (270,000 \*1=270,000).
      + The total management events analyzed is 330,000 (60,000 + 270,000). You will
       incur costs for analyzing 330,000 management events for this trail. You will be
       charged separately if you enable Insights for another trail or an event data
       store.

  **Example 2 – Enable Insights on management events for two trails**

In this next example, you enable Insights on two trails logging management events, trail A and trail B. You choose to
enable API call rate Insights only on trail A and API error rate Insights only on trail B.
Both trails log `read` and `write` management events.

- CloudTrail analyzes the `write` management events logged in the past 28
  days to form a baseline. There are no CloudTrail charges for the analysis.
- After the baseline is created, the trails log 800,000 management events, of
  which 710,000 are `read` events and 90,000 are `write`
  events.

For trail A, the following analysis occurs:

    + The `write` management events are analyzed once for the API call
     rate (90,000 \* 1=90,000).
    + The `read` management events are not analyzed, because CloudTrail only
     analyzes `write` management events for API call rate Insights.
    + The total management events analyzed is 90,000. You will incur costs for
     analyzing 90,000 management events for trail A.

For trail B, the following analysis occurs:

    + The `write` management events are analyzed once for the
     API error rate (90,000 \* 1=90,000).
    + The `read` management events are analyzed once for the API error
     rate (710,000 \*1=710,000).
    + The total management events analyzed is 800,000 (90,000 + 710,000). You will
     incur costs for analyzing 800,000 management events for trail B.

**Example 3 – Enable Insights on management events for API call rate and API
error rate on a trail and an event data store**

In this example, you enable Insights for API call rate and API error rate on both a trail and an event
data store logging management events. Both the trail and event data store are logging `read` and
`write` management events. You will incur charges for CloudTrail Insights
for the trail and event data store separately as you enabled Insights on both.

- CloudTrail analyzes the management events logged in the past 28 days to form a
  baseline. There are no CloudTrail charges for the analysis.
- After the baseline is created, the trail and event data store log 500,000 management events,
  of which 380,000 are `read` management
  events and 120,000 are `write` management events.

For the trail, the following analysis occurs:

    + The `write` management events are analyzed twice for the trail,
     once for the API call rate and once for the API error rate (120,000 \*
     2=240,000).
    + The `read` management events are analyzed once for the trail for
     the API error rate (380,000 \*1=380,000).
    + The total management events analyzed for the trail is 620,000 (240,000 + 380,000). You will
     incur costs for analyzing 620,000 management events for the trail.

For the event data store, the following analysis occurs:

    + The `write` management events are analyzed twice for the event data
     store, once for the API call rate and once for the API error rate (120,000 \*
     2=240,000).
    + The `read` management events are analyzed once for the event data
     store for the API error rate (380,000 \*1=380,000).
    + The total management events analyzed for the event data store is
     620,000 (240,000 + 380,000). You will incur costs for analyzing 620,000
     management events for the event data store.

**Example 4 – Enable management events Insights and data events Insights for API call rate and API error rate on a trail**

In this final example, you enable Insights on management and data events. The trail in this example is logging `read` and `write` management and data events.

- CloudTrail analyzes the management and data events logged in the past 28 days to form a baseline. There are no CloudTrail charges for the analysis.
- After the baseline is created, the trail logs 300,000 management events, of which 270,000 are read management events and 30,000 are write management events.
  The trail also logs 400,000 data events, of which 340,000 are read data events and 60,000 are write data events.
  - The `write` management events are analyzed twice, once for the API call rate and once for the API error rate (30,000 \* 2=60,000).
    The `read` management events are analyzed once for the API error rate (270,000 \*1=270,000). The total management events analyzed is 330,000 (60,000 + 270,000).
  - The `read` and `write` data events are analyzed twice, once for the API call rate and once for the API error rate (400,000 \* 2).
    The total data events analyzed is 800,000.
  - You will incur costs for analyzing 1,130,000 management and data events for this trail.
