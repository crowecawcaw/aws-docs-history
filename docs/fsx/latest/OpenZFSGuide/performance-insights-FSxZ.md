

# Performance warnings and recommendations
<a name="performance-insights-FSxZ"></a>

FSx for OpenZFS displays a warning for CloudWatch metrics when one of these metrics approaches or crosses a predetermined threshold for multiple consecutive data points. These warnings provide you with actionable recommendations that you can use to optimize your file system's performance.

Warnings are accessible in several areas of the **Monitoring & performance** dashboard on the Amazon FSx console. All active or recent Amazon FSx performance warnings and CloudWatch alarms configured for the file system that are in an alarm state appear in the **Monitoring & performance** panel in the **Summary** section. The warning also appears in the section of the dashboard where the metric graph is displayed.

You can create CloudWatch alarms for any of the Amazon FSx metrics. For more information, see [Creating CloudWatch alarms to monitor metrics](creating_alarms.md).

## Use performance warnings to improve file system performance
<a name="resolve-warnings"></a>

Amazon FSx provides actionable recommendations that you can use to optimize your file system's performance. You can take the recommended action if you expect the issue to continue, or if it's causing an impact to your file system's performance. Depending on which metric has triggered a warning, you can resolve it by increasing the file system's throughput capacity or storage capacity, as described in the following table.


<table>
<thead>
  <tr><th>If there's a warning for this metric</th><th>Do this</th></tr>
</thead>
<tbody>
  <tr><td>Network throughput – utilization</td><td rowspan="6"><a href="managing-throughput-capacity.md#increase-throughput-capacity">Increase throughput capacity</a></td></tr>
  <tr><td>File server &gt; Disk IOPS – utilization</td></tr>
  <tr><td>File server &gt; Disk throughput – utilization</td></tr>
  <tr><td>File server &gt; Disk IOPS – burst balance</td></tr>
  <tr><td>File server &gt; Disk throughput – burst balance</td></tr>
  <tr><td>File server &gt; CPU utilization</td></tr>
  <tr><td>Storage capacity utilization</td><td><a href="managing-storage-capacity.md#increase-storage-capacity">Increase storage capacity</a></td></tr>
  <tr><td>Storage volume &gt; Disk IOPS – utilization (SSD)</td><td><a href="managing-storage-capacity.md#increase-storage-capacity">Increase SSD IOPS</a></td></tr>
</tbody>
</table>


For more information about file system performance, see [Performance for Amazon FSx for OpenZFS](performance.md).