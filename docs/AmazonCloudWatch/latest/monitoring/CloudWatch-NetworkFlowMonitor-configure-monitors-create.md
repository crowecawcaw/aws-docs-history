# Create a monitor in Network Flow Monitor

As you review top contributors in the **Workload insights** tab,
if you see one or several network flows that you want to follow over time, or that you want more details
about, you can create a monitor directly from **Workload insights**. This simplifies
the process for creating a monitor for specific network flows.

Or, if you know specific network flows that you want to track with a monitor, such as looking
at performance information for all network flows to another AWS Region, you can use the **Create monitor** wizard to create a monitor from scratch. When you create a monitor
this way, you specify all of the local and remote
resources that define the network flows that you want to monitor.

For specific procedures, see the following sections:

- [Create a monitor
  by specifying network flows](#CloudWatch-NetworkFlowMonitor-configure-monitors-create-workload-insights "#CloudWatch-NetworkFlowMonitor-configure-monitors-create-workload-insights")
- [Create a monitor
  by specifying local and remote resources](#CloudWatch-NetworkFlowMonitor-configure-monitors-create-standalone "#CloudWatch-NetworkFlowMonitor-configure-monitors-create-standalone")

## Create a monitor

by specifying network flows

To create a monitor by selecting network flows, start on the **Workload insights** tab.
Select one or more network flows in one of the tables, in a single Region, and then, choose to create a
monitor with those flows.

When you create a monitor in this way, the **Create monitor**
wizard pre-populates local and remote resources for you and displays them in a modal dialog. You
can choose to create a monitor with those resources, or edit the selection of local
or remote resources to add or remove resources to include.

By reviewing the top contributors on **Workload insights** on an ongoing
basis, you can regularly evaluate if you have the monitors that you need, or if
creating new monitors would be helpful.

###### Important

These steps are designed to be completed all at once. You won't be able to save any in-process work to continue later.

###### To create a monitor from **Workload insights**

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, under **Network Monitoring**,
   choose **Flow monitors**.
3. Choose **Workload insights**.
4. In one of the **Top contributors** tables, select one or more network flows
   and then choose **Create monitor**.
5. In the modal window that opens, you can edit the resources that define the network flows
   that you chose, or choose **Create monitor**.

## Create a monitor

by specifying local and remote resources

You can create a monitor at any time for specific local and remote resources that define network
flows that you want to see details for.

For example, you might want to create a monitor for
one of the following scenarios:

- A monitor that includes network flows for a specific VPC in a local Region
  to another VPC in the same Region. (Note that you can't select a specific resource,
  such as a VPC, as a network flow endpoint - that is, the remote resource - in another Region.)
  - For local resource, choose **Specific resources
    in _Region_**. Then, choose **VPC and
    subnets**, and then, in the table, select a specific VPC.
  - For remote resource, do the same: choose **Specific resources
    in _Region_**, then, choose **VPC and
    subnets**, and finally, select a specific VPC.

- A monitor that includes all network flows from your
  workload in a local Region to a specific Availability Zone.
  - For local resource, choose **Everywhere in _Region_**
  - For remote resource, choose **Availability Zone**,
    and then choose a specific AZ

- A monitor that includes all network flows for your
  workload within a local Region.
  - For local resource, choose **Everywhere in
    _Region_**
  - For remote resource, choose **Everywhere in
    _Region_**

- A monitor that includes all network flows for your
  workload from a local Region to the edge of another Region.
  - For local resource, choose **Everywhere in
    _Region_**
  - For remote resource, choose **Another Region**,
    and then choose the remote Region

###### Important

These steps are designed to be completed all at once. You won't be able to save any in-process work to continue later.

###### To create a monitor using the console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, under **Network Monitoring**,
   choose **Flow monitors**.
3. From the Network Flow Monitor page, select the **Monitors** tab, and then choose **Create monitor**.
4. For **Monitor name**, enter the name that you want to use for the monitor.
   You can't change this name later.
5. Choose **Next**.
6. Select the local resources (one or more) for the network flows that you want to monitor.
   - To monitor network flows from all resources in your Region, choose **Everywhere
     in _Region_**.
   - To choose specific local resources to monitor flows from, choose **Specific resources
     in _Region_**. Then, under **Add resources**,
     choose **Availability Zones**, **EKS clusters**, or **VPCs and subnets**,
     and then choose resources to add.

7. Choose **Next**.
8. Select the remote resources (one or more) for the network flows that you want to monitor.
   - To monitor network flows to all resources in your Region, choose **Everywhere
     in _Region_**.
   - To monitor flows from specific remote resources, choose **Specific resources
     in _Region_**. Under **Add resources**,
     select **VPCs and subnets**, **Availability Zones**,
     or **AWS services**, and then choose the resources to add.
   - To monitor network flows to the edge of another Region, choose **Another Region**.

9. Choose **Next**.
10. Review your choices to confirm the network flows to monitor, or edit the options to
    make changes.
11. Choose **Create monitor**.

After you create a monitor, you can edit or delete the monitor at any time to add or
remove network flows. Select a monitor, and then choose
**Edit** or **Delete**. Note that you can't change the name of a monitor.

###### To view the Network Flow Monitor dashboard

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Network monitoring**, then
   **Flow monitors**.

The **Monitors** tab displays a list of the monitors that you have created.

To see more information about a specific monitor, choose a monitor.
