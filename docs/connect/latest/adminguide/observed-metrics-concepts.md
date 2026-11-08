

# Observed metrics
<a name="observed-metrics-concepts"></a>

Observed metrics are state-based metrics. They report on the states a contact passes through while it is still active, not only after it ends. The model maps each state to a segment, which makes that state measurable across a reporting interval. Because a segment exists as soon as a state begins, a contact that is in a given state during the interval is counted, without waiting for the contact to disconnect.

The states are the stages a contact passes through, such as initiated, queued, connected to an agent, and paused.

Observed metrics are additive. The contact record-driven historical metrics and their calculations do not change, and a caller that does not request observed metrics sees no difference in behavior.

## States and segments
<a name="observed-metrics-segments"></a>

A segment is one state a contact passes through, with a start time and an end time. Each state the contact passes through, such as initiated, queued, connected to an agent, or paused, becomes its own segment. A segment opens the moment the state begins. The segment takes an end time when the state ends, and a segment that has no end time is still running and still counts. When one segment closes, the next segment opens at that same instant, so segments do not overlap and do not leave gaps.

Each segment carries the dimensions of its contact, such as queue, channel, agent, and routing profile. A segment has the values its contact has so far. For example, a contact that is still waiting in queue has no agent. When a segment ends, it takes the values of its contact at that time, so a queued segment that ends when an agent answers carries that agent. When you group results, a segment that has no value for any of the requested groupings is left out of the results. A segment that has a value for at least one requested grouping is kept, and its missing groupings are returned empty.

The following diagram shows one contact on a time axis as a row of consecutive boxes for its states: initiated, queued, connected to an agent, and paused. Each earlier box is closed and carries a start time and an end time. The last box is open, has no end time, and extends to a current-time marker. The end time of one box is the start time of the next, so the boxes touch without overlapping or leaving a gap.

![A contact's states shown as consecutive segments on a time axis, the last one open to now.](https://docs.aws.amazon.com/connect/latest/adminguide/images/observed-metrics-segment-timeline.png)


The diagram shows one contact on a horizontal time axis as four consecutive boxes, one per state:
+ Initiated: a closed box labeled with a start time and an end time.
+ Queued: a closed box that starts at the end time of the initiated box and is labeled with its own start time and end time.
+ Connected to an agent: a closed box that starts at the end time of the queued box and is labeled with its own start time and end time.
+ Paused: an open box that starts at the end time of the connected box, has no end time, and extends to a current-time marker.

The end time of each box is the start time of the next box, so the boxes touch without overlapping or leaving a gap.

## Interval retrieval and overlap attribution
<a name="observed-metrics-interval"></a>

An interval request returns a metric across a reporting window. You set `StartTime` and `EndTime`, and optionally an `IntervalPeriod` to divide the window into equal periods. A segment belongs to every interval that its time overlaps, whether the segment started before the interval, ended after it, or sat entirely within it. A segment that is still open counts up to the current time. For contacts, this makes long-running work, such as a task or an email that stays open for days, visible in each interval it spanned rather than collapsing into the single interval where the contact ended.

Count metrics count a segment in each interval it overlaps. Average duration metrics clip each segment to the interval boundaries before averaging, so a segment that carries into or out of an interval contributes only the portion of its duration that falls within that interval, never its full length. A segment that does not overlap the interval contributes nothing. The duration each segment contributes to an interval is `max(0, min(endTime, requestEndTime) - max(startTime, requestStartTime))`. In this formula, `requestStartTime` and `requestEndTime` are the start and end of each period when you set an `IntervalPeriod`, and the `StartTime` and `EndTime` of the request when you do not. For a segment that is still open, `endTime` is the current time.

The following diagram shows one requested interval window and several segments beneath it. A segment drawn fully inside the window contributes its whole duration. A segment that started before the window carries in and contributes only from the window start, and a segment that ends after the window carries out and contributes only up to the window end. A segment that spans the whole window contributes the window length. A still-open segment extends to the current time at the window edge and counts while it runs. A segment that falls outside the window contributes nothing.

![Segments shaded to show the portion of each clipped to the requested interval window.](https://docs.aws.amazon.com/connect/latest/adminguide/images/observed-metrics-interval-clipping.png)


The diagram shows the requested interval window as a bar from `StartTime` to `EndTime`, with six segments drawn beneath it. Each segment contributes to a duration metric as follows:
+ Fully inside: the segment starts after the window start and ends before the window end, so it contributes its whole duration.
+ Carry-in: the segment starts before the window and ends inside it, so it contributes only from the window start to its end time.
+ Carry-out: the segment starts inside the window and ends after it, so it contributes only from its start time to the window end.
+ Full span: the segment starts before the window and ends after it, so it contributes the whole window length.
+ Still open: the segment has no end time and extends to the current time at the window edge, so it contributes from its start time to the window end while it runs.
+ No overlap: the segment ends before the window starts or begins after the window ends, so it contributes nothing.

## Observed metrics and units
<a name="observed-metrics-metric-list"></a>

The following observed metrics are available. The count metrics report a count of segments, and the average duration metrics report seconds. For a description of each metric, see [Metric definitions in Connect Customer](metrics-definitions.md). For the segment primitives these metrics are composed from, see [Custom metric primitives](metric-primitive-definitions.md).


| Metric | Unit | 
| --- | --- | 
| CONTACTS\_INITIATED\_OBSERVED | Count | 
| CONTACTS\_IN\_QUEUE\_OBSERVED | Count | 
| CONTACTS\_CONNECTED\_TO\_AGENT\_OBSERVED | Count | 
| CONTACTS\_ON\_PAUSE\_OBSERVED (tasks only) | Count | 
| AVG\_QUEUE\_TIME\_OBSERVED | Seconds | 
| AVG\_CONNECTED\_TO\_AGENT\_TIME\_OBSERVED | Seconds | 
| AVG\_PAUSE\_TIME\_OBSERVED (tasks only) | Seconds | 
| CONTACTS\_DEFERRED\_SERVICE\_LEVEL\_OBSERVED | Percent | 

## Availability and retention
<a name="observed-metrics-availability"></a>

Observed metrics are available through the [GetMetricDataV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricDataV2.html) API. You can group and filter them by queue, channel, subtype, routing profile, and agent. The observed metrics do not support metric-level filters. To apply metric-level filters, such as segment type or initiation method, create a custom metric from the Contact segment count or Contact segment time primitive. For more information, see [Creating Custom Metric from Primitives](metric-primitive-definitions.md#create-custom-metric-from-primitives). `CONTACTS_DEFERRED_SERVICE_LEVEL_OBSERVED` takes a threshold in seconds, the same as `SERVICE_LEVEL`.

The `StartTime` of a request can be up to 30 days in the past. A request with an older `StartTime` returns an error. Segments are removed only after their contact disconnects, so a contact that is still active stays available however long it runs. A request within the 30-day limit can therefore include a segment that started more than 30 days before the `StartTime` of the request.

**Note**  
Observed metrics are recorded from 00:00 UTC on October 17, 2026. Data for contacts that were already active at that time can be missing or incomplete.