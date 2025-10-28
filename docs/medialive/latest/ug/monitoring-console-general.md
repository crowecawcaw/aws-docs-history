# Monitoring using the

MediaLive console

You can monitor the state and health of channels and
multiplexes.

###### Topics

- [Monitoring a channel using
  the console](#monitoring-console "#monitoring-console")
- [Monitoring a
  multiplex using the Console](#monitoring-multiplex-console "#monitoring-multiplex-console")

## Monitoring a channel using

the console

You can monitor a channel using the AWS Elemental MediaLive console to view
its activity and its current state.

###### To monitor activity on a channel and its current state

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/ "https://console.aws.amazon.com/medialive/").
2. In the navigation pane, choose
   **Channels**. (For information
   about the buttons on the page, see [Editing a channel](editing-deleting-channel.md#editing-a-channel "editing-deleting-channel.md#editing-a-channel"), [Starting, stopping, and pausing a channel](starting-stopping-deleting-a-channel.md "starting-stopping-deleting-a-channel.md"),
   and [Creating a channel by
   cloning](creating-channel-clone.md "creating-channel-clone.md").)
3. The **Channels** page shows a list of
   your channels. Each line in the list provides basic
   information about the channel, including its state. For
   information about states, see [States for channels and
   multiplexes](monitor-activity-types-channel.md "monitor-activity-types-channel.md").
4. To view more details about a channel, choose the name
   of that channel. The **Channel
   details** page appears.

###### Topics

- [Status tab –
  Viewing status information](#view-status-info "#view-status-info")
- [Alerts tab – Viewing
  alerts](#view-alerts "#view-alerts")
- [Handling alerts](#handle-alerts "#handle-alerts")
- [Destinations
  pane](#view-status-details "#view-status-details")

### Status tab –

Viewing status information

For basic status information, look at the
**Status** pane.

For information about the inputs in the channel, choose
the **Details** tab.

For detailed information about the status, choose the
**Health** tab. This tab provides
information for the pipelines in the channel:

- Pipeline 0 and pipeline 1, if the channel is set
  up as a standard channel and therefore has two
  pipelines
- Pipeline 0, if the channel is set up as a
  single-pipeline channel

You can specify the period of time for the health
information.

### Alerts tab – Viewing

alerts

MediaLive generates alerts for a channel when an issue or
potential issue occurs in either pipeline in a channel.
These alerts are displayed in two ways:

- On the right side of the
  **Status** pane, there is a
  count of active alerts for each pipeline.
- On the **Alerts** tab, details
  about each alert are displayed.

If the alert is still active, the
**Cleared** column is blank. If
the alert has cleared, the column shows the
timestamp for when it cleared.

For a list of MediaLive alerts, see [List of alerts for channels](monitor-activity-types-alerts-channels.md "monitor-activity-types-alerts-channels.md").

### Handling alerts

When an alert occurs, look at the
**Alerts** tab to determine possible
causes of the issue. Take steps to resolve the issue.

After you resolve the issue, MediaLive automatically clears
the alert.

If you stop a channel, alerts always automatically
clear.

### Destinations

pane

This pane has three panes:

- **Egress endpoints** – This
  pane shows one line for each pipeline. The
  **Source IP** is the channel
  endpoint for this pipeline. The channel endpoint is
  the egress from the pipeline. From this point, the
  content goes to the output destinations for each of
  the output groups in the channel.

In a regular channel, this endpoint is in a
location that MediaLive manages.

In a channel set up for [delivery via your
VPC](delivery-out-vpc.md "delivery-out-vpc.md"), this endpoint is in your VPC. You
are responsible for ensuring that this endpoint is
always available to accept the content from the
channel pipeline.

- **Destinations** – This
  pane shows one line for each destination.

Each output group has one destination line. Each
line shows the address of the output in the one or
two pipelines in the channel.

- **MediaPackage destinations**
  – This pane shows the channel ID that is the
  destination for each MediaPackage output group. The
  channel in MediaPackage has one or two pipelines, mapped to
  the one or two pipelines in MediaLive.

## Monitoring a

multiplex using the Console

You can view the activity of your multiplex and its current
state.

###### To monitor activity on a multiplex (MediaLive

console)

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/ "https://console.aws.amazon.com/medialive/").
2. In the navigation pane, choose
   **Multiplexes**.
3. The **Multiplexes** page shows a list
   of your multiplexes. Each line in the list provides
   basic information about the multiplex, including its
   state. For information about states, see [States for channels and
   multiplexes](monitor-activity-types-channel.md "monitor-activity-types-channel.md").
4. To view more details about a multiplex, choose the
   name of that multiplex. The **Multiplex
   details** page appears.

###### Topics

- [Viewing status
  information](#view-status-info "#view-status-info")

### Viewing status

information

The **Multiplex details** page is divided
into two panes. The second pane is divided into tabs.

#### Details

tab

The **Details** tab shows the fields
that you set when you created the multiplex.

It also shows this information that MediaLive
assigns:

- The ARN of the multiplex.
- The ARNs of the two entitlements that MediaLive
  automatically creates when you create the
  multiplex. For more information about these
  entitlements, see [Starting the multiplex](start-multiplex.md "start-multiplex.md").

#### Programs

tab

The **Programs** tab lists the tabs
that are in the multiplex. For information about
programs, see [Overview of multiplex and MPTS](mpts-general.md "mpts-general.md").

#### Bandwidth

monitoring tab

The **Bandwidth monitoring** tab
shows information about the bandwidth allocation for the
multiplex.

###### To display the information as a bar chart

1. Choose **Bar chart**.
2. Choose to show the multiplex (all the programs
   in the multiplex) or a specific program.
3. Choose which pipeline to show.

The chart always shows the data for the most recent
minute. The chart refreshes every minute.

###### To display the information as an area chart

1. Choose **Area chart**.
2. Set the time window. This window sets the size
   of the x-axis. The window always shows 60 data
   points. Therefore, a window of 1 hour shows a
   data point every minute, for example. A window
   of 1 day shows a data point every 24
   minutes.
3. Choose to show the multiplex (all the programs
   in the multiplex) or a specific program.
4. Choose which pipeline to show.

#### Alerts

tab

MediaLive generates alerts for a multiplex when an issue
or potential issue occurs in either pipeline in a
multiplex. These alerts are displayed in two
ways:

- On the right side of the
  **Status** pane, there is a
  count of active alerts for each pipeline.
- On the **Alerts** tab,
  details about each alert are displayed.

If an alert is still active, the
**Cleared** column is blank. If an
alert has cleared, the column shows the timestamp for
when it cleared.

###### To handle an alert

1. When an alert occurs, look at the
   **Alerts** tab to determine
   possible causes of the issue. Take steps to resolve
   the issue.

After you resolve the issue, MediaLive automatically
clears the alert. The **Cleared**
column shows the timestamp for when it
cleared. 2. If you stop a channel, alerts always automatically
clear.

#### Tags Tab

For information about tags, see [Tagging resources](tagging.md "tagging.md").
