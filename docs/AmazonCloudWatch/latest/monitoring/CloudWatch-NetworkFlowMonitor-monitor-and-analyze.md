# Monitor and analyze network

flows with a Network Flow Monitor monitor

Network Flow Monitor data and graphs help you to visualize and track network issues. You can create
monitors to see detailed information about specific network segments for your AWS workloads, including a
view of the network path for individual network flows. After you create one or more monitors in Network Flow Monitor, you can
observe performance and metrics, and explore historical data, to find anomalies.

To see the information provided by a monitor, on the **Monitors** tab, choose a monitor in the
**Monitors** table. Then, choose one of the following tabs for more information:
**Overview**, **Historical explorer**, or **Monitor details**.

**Overview tab**

On the **Overview** tab, you can review the following, for time periods that
you specify. To see a broader or narrower range of historical
information, including the NHI and traffic summary data, adjust the time period selection
at the top of the page.

- **Network health indicator (NHI):** NHI alerts you to whether there
  there were AWS network issues for one or more of the network flows tracked by your monitor,
  during the time frame that you've selected for viewing performance metrics. NHI is a binary value,
  that is, 1 or 0, which is shown in the console as **Degraded** or **Healthy**.

      + NHI is shown as **Degraded** if there were issues with the portion of the
       AWS network that any network flow in the monitor traversed, at any time during the time frame
       that you select.
      + Otherwise, NHI is shown as **Healthy**.

  If the NHI is **Degraded**, you can view the
  **Network health indicator** bar graph for more information. The graph
  shows you when, during the selected time frame, there were AWS network issues for the
  network flows tracked by your monitor.

- **Traffic summary:** Observe overall metrics for the flows tracked by this
  monitor, for the time period that you've selected. You can see average round-trip time, sums (totals)
  of transmission timeouts and retransmissions, and the average amount of data transferred for the flows
  in the monitor. Be aware that RTT data can be sparse because RTT is not always calculated.

**Historical explorer tab**
On the **Historical explorer** tab, you can dive deep into information about
specific flows. You can review metrics and network paths for top contributor network flows for specified time
frames. In the tables of metrics, you can filter the data by different categories of
flows, such as flows between Availability Zones (`INTER_AZ`).

- **Metrics:** View detailed information for the top contributors
  for each metric type that Network Flow Monitor aggregates data for. Separate tables of top contributors are
  provided for retransmission timeouts, retransmissions, round-trip time, and data transferred.
- **Network paths:** To get an idea about where anomalies are occurring,
  you can view the network path of a network flow. When you choose a
  specific metric in a metrics table, the network path for that flow is displayed below the table.

**Monitor details tab**

On the **Monitor details** tab, you can see details about the monitor, including
the monitor state, the ARN, when it was created and last updated, and the flows that are included.

You can choose to edit or delete a monitor from any page on the **Monitors** tab.

As part of your regular use of Network Flow Monitor, we recommend that you periodically review the data on the
**Workload insights** page to determine if there are new flows that show metrics anomalies
that you want to track more closely over time. When you see a set of flows on the
**Workload insights** page that you want to see details about, select the flows and
create a monitor for them.
