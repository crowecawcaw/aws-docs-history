# EUCCOST08-BP02 Monitor your Amazon AppStream 2.0 fleet utilization, and optimize scaling policies and buffer capacity

Use [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/?nc1=h_ls "https://aws.amazon.com/cloudwatch/?nc1=h_ls") to observe and
monitor your Amazon AppStream 2.0 resources. Amazon AppStream 2.0 publishes several [AppStream 2.0
Metrics and Dimensions](../../../appstream2/latest/developerguide/monitoring-with-cloudwatch.md "../../../appstream2/latest/developerguide/monitoring-with-cloudwatch.md") to Amazon CloudWatch that you can visualize and use to check if you
are overprovisioning buffer capacity or if you are running into capacity shortages at times.
Use these metrics to adjust your AppStream 2.0 Fleet capacity and scaling policies to minimize idle
capacity and reduce insufficient capacity errors where possible. 

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Create your own customized CloudWatch dashboards to visualize key AppStream 2.0 metrics for your
AppStream 2.0 fleets. These dashboards can contain several widgets that display a view of
selected metrics of a specific AppStream 2.0 fleet or across multiple AppStream 2.0 fleets. Review these
dashboards on a regular basis.

Additionally, use the EUC Toolkit to review Amazon CloudWatch and OS-level metrics. This
Toolkit also helps you manage large WorkSpaces and AppStream 2.0 deployments at scale. After review of
the metrics, determine whether changes to the fleet capacity or scaling policies are
required, and plan for how to implement those changes. For more information, see [Use the EUC
Toolkit to manage Amazon AppStream 2.0 and Amazon WorkSpaces](https://aws.amazon.com/blogs/desktop-and-application-streaming/euc-toolkit/ "https://aws.amazon.com/blogs/desktop-and-application-streaming/euc-toolkit/")
