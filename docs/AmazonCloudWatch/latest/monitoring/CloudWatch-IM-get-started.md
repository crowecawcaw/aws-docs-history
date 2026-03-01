# Getting started with Internet Monitor using the console

To help you get started with Internet Monitor, this chapter provides the steps for creating and configuring a _monitor_. You create
a monitor in Internet Monitor for your application by naming it, and then adding AWS resources that your application uses.

You create a monitor in Internet Monitor for your application by adding AWS resources that it uses, and then setting several configuration options.
The resources that you add, Amazon Virtual Private Cloud VPCs, Network Load Balancers (NLBs), CloudFront distributions, or WorkSpaces directories,
provide the information for Internet Monitor to map internet traffic information for your application. After you create your monitor, wait 15-30
minutes to generate the traffic profile specific to where your application is used.

Then, use the Internet Monitor dashboard, or other tools, to visualize and explore performance and availability about your client usage.
These tools provide insights for you using your application traffic's measurements gathered for you by the monitor.

The steps here walk you through setting up your monitor by using the console. To see examples
of using the AWS Command Line Interface with the Internet Monitor API actions, to create a monitor, view events, and so on, see
[Examples of using the CLI with Internet Monitor](CloudWatch-IM-get-started-CLI.md "CloudWatch-IM-get-started-CLI.md").

**Tasks**

- [Step 1: Create a monitor](#CloudWatch-IM-get-started.create "#CloudWatch-IM-get-started.create")
- [Step 2: Configure the monitor](#CloudWatch-IM-get-started.configure "#CloudWatch-IM-get-started.configure")
- [Step 3: View metrics and explore history](#CloudWatch-IM-get-started.explore "#CloudWatch-IM-get-started.explore")
- [Step 4: Get suggestions to improve latency](#CloudWatch-IM-get-started.suggestions "#CloudWatch-IM-get-started.suggestions")
- [Step 5 (Optional): Delete the monitor](#CloudWatch-IM-get-started.delete "#CloudWatch-IM-get-started.delete")

## Step 1: Create a monitor

###### To create a monitor using the console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, under **Network Monitoring**, choose **Internet monitors**.
3. Choose **Create monitor**.
4. For **Monitor name**, enter the name you want to use for this monitor in
   Internet Monitor.
5. Choose **Add resources**, and then select the resources to set the monitoring boundaries
   for Internet Monitor to use for this monitor.

###### Note

Be aware of the following:

    * To generate meaningful output with Internet Monitor, VPCs that you add must be connected to the internet by having
     an Internet Gateway configured.
    * You can add only one type of resource to a single monitor. For example, VPCs or CloudFront distributions or WorkSpaces directories,
     but not a combination of different types.

6. Leave the default percentage of traffic as 100%, or choose another percentage of your internet traffic to monitor.
7. Choose **Create monitor**.

## Step 2: Configure the monitor

After you create a monitor, you can edit the monitor at any time, for example, to change the application traffic percentage, update
the maximum city-networks limit or add or remove resources. To make updates in the Internet Monitor console,
follow the procedure in this section. Note that you can’t change the name of a monitor.

For more information about configuring a monitor, see [Edit a monitor in Internet Monitor](CloudWatch-IM-get-started.md "CloudWatch-IM-get-started.md").

###### To configure a monitor using the console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, under **Network Monitoring**, choose **Internet monitors**.
3. Choose your monitor, and then choose the **Action** menu.
4. Choose **Update monitor**.
5. Make the desired updates. For example, to change the percentage of traffic to monitor, under **Application traffic
   to monitor**, select or enter a percentage.
6. Choose **Update**.

## Step 3: View metrics and explore history

Visualize data about your internet traffic, from an overview perspective or by drilling down into details.

###### To visualize data and get insights for application traffic using the console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, under **Network Monitoring**, choose **Internet monitors**.
3. Choose a monitor to work with.
4. Choose from the following tabs:
   - **Overview** — Review a general summary
     of your monitor and your application traffic performance.
   - **Health events** — View current and historical health events that currently impact,
     or previously impacted, locations where clients access your application.
   - **Analyze** — See information about top monitored traffic in client
     locations (by traffic volume), summarized in several customizable ways. Visualize metrics and historical
     trends for health scores and metrics.

In the next section, learn about how Internet Monitor provides suggestions for improving latency for your application traffic.

## Step 4: Get suggestions to improve latency

Get suggestions for how to optimize latency, so that your clients experience the best internet performance for your application.

Internet Monitor evaluates your monitored application traffic, and then makes suggestion about whether you can reduce latency, for
example, by changing the AWS Regions that you've configured for your application.

For more information, see [Get suggestions to optimize application performance in Internet Monitor (Optimize page)](CloudWatch-IM-insights.md "CloudWatch-IM-insights.md").

###### To get suggestions for improving application latency using the console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, under **Network Monitoring**, choose **Internet monitors**.
3. Choose a monitor to work with.
4. Choose **Optimize**, and then view the top suggestions.

## Step 5 (Optional): Delete the monitor

If you created a monitor as a test or if you're no longer using a monitor, you can delete it. Before you can delete
a monitor, you must disable it.

###### To delete a monitor

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, under **Network Monitoring**, choose **Internet monitors**.
3. Choose your monitor, and then choose the **Action** menu.
4. Choose **Disable**.
5. Choose the **Action** menu again, and then choose **Delete**.
6. Follow the guidance in the modal dialog to confirm deleting the monitor.
