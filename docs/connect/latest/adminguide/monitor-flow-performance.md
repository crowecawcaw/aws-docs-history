

# Monitor flow performance with metrics in flow designer analytics mode
<a name="monitor-flow-performance"></a>

You can view near real-time and historical performance data directly in the flow designer to identify bottlenecks and optimize your published flows and modules. You can see aggregate traffic through each completed and in-progress blocks in the flow. This helps you identify behavioral patterns of your customers or pinpoint where errors are being encountered.

Following are a couple example use cases for this functionality:
+ In an IVR experience, you can determine how often customers select specific options from a menu, where a menu configuration might be causing an error, or identify at which point in the flow customers are abandoning the experience.
+ For step-by-step guides, you can track which guides customers and agents use most frequently and optimize their navigation paths.

**Topics**
+ [Requirements](#flow-performance-requirements)
+ [How flow designer analytics mode works](#how-it-works)
+ [Display metrics for a flow](#show-metrics-for-a-flow)
+ [View metrics in the flow designer](#metrics-display)
+ [Block Metrics table](#block-metrics-table)
+ [Metrics with flow versions](#metrics-with-flow-versions)

## Requirements
<a name="flow-performance-requirements"></a>

To use flow designer analytics mode: 
+ You must enable [Next Generation Connect Customer](enable-nextgeneration-amazonconnect.md) for your instance.
+ Your flows and modules must be published so metrics can be collected.
+ You must have the following permissions in your security profile: **Analytics and Optimization** - **Access metrics** - **Access**.

## How flow designer analytics mode works
<a name="how-it-works"></a>

Flows designer analytics displays metrics in three places:
+ At the entry point of each block.
+ On the block's branches (for example, Success: 94%, Error: 4%).
+ A floating metrics table on the flows designer provides detailed performance data for all blocks. You can move the table as needed.

The following GIF shows how analytics mode works:

![Analytics mode in the flow designer.](http://docs.aws.amazon.com/connect/latest/adminguide/images/metrics-button.gif)


## Display metrics for a flow
<a name="show-metrics-for-a-flow"></a>

Complete the following steps to display metrics for a flow.

1. On the Connect Customer admin website, on the left navigation menu, choose **Routing**, **Flows**.

1. Choose a flow to open the flows designer.

1. On the toolbar, choose **Show Metrics**.

1. Choose the **Show Metrics** dropdown arrow to open the **Metric Controls** panel. The following image shows an example panel.  
![The Metric Controls panel with sample settings.](http://docs.aws.amazon.com/connect/latest/adminguide/images/metric-controls.png)

1. In the **Metric Controls** panel, you can configure the following settings:
   + **Date range**: You can set the following types of date ranges:
     + **Relative range**: Displays flow metrics that are captured X hours, minutes, weeks, or months from the current time.
     + **Absolute range**: Displays flow metrics that are captured between a date range.
**Important**  
Historical data is retained and available for the last 30 days from the current date.  
![The options for choosing relative or absolute range.](http://docs.aws.amazon.com/connect/latest/adminguide/images/flow-metrics-date-range.png)
   + **Visual options**
     + **Highlight incompletes**: Displays **Incomplete: X%** on the affected blocks.
     + **Highlight errors**: Adds amber color highlight (1-4% errors) or red color highlight (≥5% errors) indicators to density of error branches.
     + **Highlight traffic**: Highlights the relative traffic volume with thickness of the block connecting line.
   + **Data presentation**
     + **Show as a percentage of all traffic**: Change the metric to use percentage (%) to represent each block traffic as percentage of total flow traffic.
     + **Show as a percentage of incoming block(s)**: Change the metric to use percentage (%) to represent each block traffic as percentage relative to the previous connecting block's traffic.
     + **Show interaction count**: Change the metric to show absolute number of traffic going through the flow.

## View metrics in the flow designer
<a name="metrics-display"></a>

Flows metrics appear directly on block branches and at the entry point of each block. Choose any entry point metric to toggle all flow metrics between the visual option **Show percentage of traffic** and **Show interaction count**.

The following GIF shows an example of choosing the entry point and the metrics displaying.

![Metrics for blocks on the flow designer.](http://docs.aws.amazon.com/connect/latest/adminguide/images/metrics-choose-badge.gif)


## Block Metrics table
<a name="block-metrics-table"></a>

When you enable metrics, a floating block metrics palette appears that you can drag anywhere on the canvas. To open the **Block Metrics** table, choose the arrow on the right side as shown in the following image.

![The Block Metrics table on the flow designer.](http://docs.aws.amazon.com/connect/latest/adminguide/images/block-metrics.png)


The following image shows an example of metrics on the **Block Metrics** table:

![An example Block Metrics table for a flow.](http://docs.aws.amazon.com/connect/latest/adminguide/images/block-metrics-table.png)


The following information is displayed on the table:
+ **Block name**: Shows the block name. Choose the name to navigate to that block in the canvas.
+ **Type**: The block type.
+ **Status**: An alert indicator for issues.
+ **Ingress**: The contact traffic that has entered the block.
+ **Success**: The contact traffic that has successfully completed the block.
+ **Incomplete**: The contact traffic that entered but did not exit through any block branch. This occurs when customers are disconnected, timeouts expired, transfers failed, or error handling is missing.

  The following image shows an example of an **Incomplete** metric on the **Play prompt** block.  
![An example Incomplete metric.](http://docs.aws.amazon.com/connect/latest/adminguide/images/incomplete-metrics.png)

To work with the palette, you can:
+ Drag it using the handle (⋮⋮) in the header.
+ Resize the **Block Metrics** table after it is opened. Use the right bottom corner to resize it.
+ Expand and collapse the **Block Metrics** table by choosing the right side of the arrow icon.

## Metrics with flow versions
<a name="metrics-with-flow-versions"></a>

When viewing metrics for previous flow versions:
+ Metrics are version-specific: Each published flow generates its own data while active.
+ Publishing a replacement version closes the previous data and opens a new one.
+ Only published versions collect metrics. Drafts are excluded from analytics.