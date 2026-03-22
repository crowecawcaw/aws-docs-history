# Change health event thresholds for a monitor

Internet Monitor uses a default threshold to determine when to create a
health event for your monitor. Optionally, you can change that default global threshold, to set another value. You
can also set local threshold. This section describes how global and local thresholds work together, and provides
steps for setting custom thresholds.

You can change the overall threshold that triggers Internet Monitor to create a health event. The default health event threshold,
for both performance scores and availability scores, is 95%. That is, when the overall performance or availability score for your
application falls to 95% or below, Internet Monitor creates a health event. For the overall threshold, the health event can be triggered by a
single large issue, or by the combination of multiple smaller issues.

You can also change the local—that is, city-network—threshold, combined with a percentage of the overall level of
impact, that—in combination—will trigger a health event. By setting a threshold
that creates a health event when a score drops below the threshold for one or more city-networks (locations and ASNs, typically ISPs),
you can get insights into when there are issues in locations with lower traffic, for example.

An additional local threshold option works together with the local threshold for availability or performance scores. The second
factor is the percentage of your overall traffic that must be impacted before Internet Monitor creates a health event based on the local threshold.

By configuring the threshold options for overall traffic and local traffic, you can fine-tune how frequently
health events are created, to align with your application usage and your needs. Be aware that when you set the local threshold to be lower,
typically more health events are created, depending on your application and the other threshold configuration values that you set.

In summary, you can configure health event thresholds—for performance scores, availability scores, or both—in the
following ways:

- Choose different global thresholds for triggering a health event.
- Choose different local thresholds for triggering a health event. With this option, you can also change the percentage
  of impact on your overall application that must be exceeded before Internet Monitor creates an event.
- Choose to turn off triggering a health event based on local thresholds, or enable local threshold options.
  To update health event thresholds for performance scores, availability scores, or both,
  follow these steps.

###### To change threshold configuration options

1. In the AWS Management Console, navigate to CloudWatch, and then, in the left navigation pane, choose Internet Monitor.
2. On the **Configure** page, in the **Health event thresholds** section,
   choose **Update thresholds**.
3. On the **Set health event threshold**page, choose the new values and options that you want for thresholds and other options that
   trigger Internet Monitor to create a health event. You can do any of the following:
   - Choose a new value for **Availability score threshold**,
     **Performance score threshold**, or both.

   The graphs in the sections for each setting display the current threshold setting and the
   actual recent health event scores, for availability or performance, for your application. By viewing the typical values,
   you can get an idea of values that you might want to change a threshold to.

   Tip: To view a larger graph and change the timeframe, choose the expander in the upper right corner of the graph.
   - Choose to turn on or off a local threshold for availability or performance, or both. When an option is enabled,
     you can set the threshold and impact level for when you want Internet Monitor to create a health event.

4. After you configure threshold options, save your updates by choosing **Update health event thresholds**.
   To learn more about how health events work, see [When Internet Monitor creates and resolves health events](CloudWatch-IM-inside-internet-monitor.md#IMHealthEventStartStop "CloudWatch-IM-inside-internet-monitor.md#IMHealthEventStartStop").
