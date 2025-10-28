# Understanding the summary

page

The Amazon CodeGuru Profiler summary page displays the status of your profiling group and relevant
metrics gathered during profiling. The metrics shown are for any data gathered in the last 12
hours, up to the beginning of the current UTC hour.

Most information is only displayed while the profiling group is enabled. If a profiling
group is disabled, or becomes inactive, then metrics and reports are not shown. You can view
the following elements in the summary page.

To view the summary page, go to the [CodeGuru Profiler console](https://console.aws.amazon.com/codeguru/profiler/ "https://console.aws.amazon.com/codeguru/profiler/") and choose
**Profiling groups** in the navigation bar. Then select the profiling group
that you want to view.

## Profiling group status

This is the latest general information regarding the status of the profiling
group.

## CPU summary

The **CPU utilization** gives an indication of how much of the
instance’s CPU resources are consumed by the profiled application. For JVM applications,
this gives a percentage of system CPU resources consumed by the JVM. The metric value is an
average across all instances reporting data to this profiling group.

A low value (for example < 10%) indicates your application does not consume a large
amount of the system CPU capacity. This means there could be an opportunity to use smaller
instances or autoscaling to reduce cost, as long as there is nothing else running on the
system. A high value (>90%) indicates your application is consuming a large amount of
system CPU capacity. This means there is likely value in looking at your CPU profiles and
recommendations for areas of optimization. The values are averages over the last full 12
hours.

The **Agent CPU usage** provides an estimate of how much of the system
CPU resources are consumed by the CodeGuru Profiler agent on average across profiled instances. It’s
expected that this value is low (<1%); however, it can be normal for this to be higher
depending on the application being profiled. If the number concerns you, please get in touch
with
AWS
Support, or provide feedback at the bottom of the page.

The **Time spent executing code** is a measure of how frequently your
application’s JVM threads were in the `RUNNABLE` thread state, as a percentage of
all thread states except `IDLE`.

A high percentage (>90%) indicates most of your application’s time is spent executing
operations on the CPU. A very low percentage (<1%) indicates that most of your
application was spent in other thread states (e.g. `BLOCKED` or
`WAITING`) and there may be more value in looking at the
**Latency** visualization, which displays all non-`IDLE`
thread states, instead of the **CPU** visualization.

## Latency summary

The **Time spent blocked** is a measure of how often your threads are
in the `BLOCKED` state, once we exclude all `IDLE` threads. This can happen if
your application makes frequent use of synchronized blocks or monitor locks. The
**Latency** visualization can help you understand what sections of code
are causing threads to block.

**Time spent waiting** is a measure of how much time your application’s
thread spent in the `WAITING` and `TIMED WAITING` thread states, as a
percentage of all thread states except `IDLE`. This is frequently caused by I/O
operations such as network calls or disk operations. The **Latency**
visualization can help you understand which sections of code are causing threads to
wait.

## Heap usage

The **Average heap usage** shows how much of your application’s maximum
heap capacity is consumed by your application on average across all profiled instances. The
percentage shown is the average heap space used compared to the JVM’s maximum heap capacity,
with the absolute value for the average heap space used shown next to it.

A high percentage (>90%) could indicate that your application is close to running out
of memory most of the time. If you wish to optimize this, then the **Heap
summary** visualization shows you the object types consuming the most space on
the heap. A low percentage (<10%) may indicate that your JVM is being provided much more
memory than it actually requires and cost savings may be available by reducing your system
memory size, although you should check the peak usage too.

The **Peak heap usage** metric shows the highest percentage of memory
consumed by your application seen by the CodeGuru Profiler agent. This is based on the same dataset as
seen in the **Heap summary** visualization. A high percentage (>90%)
could indicate that your application has high spikes of memory usage, especially if your
average heap usage is low.

Choose **Visualize heap** to see your application's heap usage over
time. For information on understanding the heap summary, see [Understanding the heap
summary](working-with-visualizations-heap-summary.md "working-with-visualizations-heap-summary.md").

## Anomalies

CodeGuru Profiler discovers anomalies by analyzing trends in your profiling data and detecting
deviations in that data. Any anomalies found are shown here along with details of which time
period is anomalous. Further details can be found in the linked report.

## Recommendations

CodeGuru Profiler makes recommendations that you can use to optimize your applications. Any
recommendations available are shown here along with details of the estimated impact on your
overall application profile. Further details can be found on the linked report.
