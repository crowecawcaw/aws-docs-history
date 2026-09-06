

# Viewing Fleet Usage Using the Console
<a name="monitoring-console"></a>

You can monitor your Amazon WorkSpaces Applications fleet usage using the WorkSpaces Applications or CloudWatch console.

**To view fleet usage in the WorkSpaces Applications console**

1. Open the WorkSpaces Applications console at [https://console.aws.amazon.com/appstream2/home](https://console.aws.amazon.com/appstream2/home).

1. In the left pane, choose **Fleets**.

1. Select a fleet and choose its **Fleet Usage** tab.

1. By default, the graph displays the following metrics: 
   + `ActualCapacity`, `InUseCapacity`, `DesiredCapacity`, `AvailableCapacity`, `PendingCapacity`, and `CapacityUtilization` for single-session fleets.
   + `ActualUserSessionCapacity`, `ActiveUserSessionCapacity`, `AvailableUserSessionCapacity`, `DesiredUserSessionCapacity`, `PendingUserSessionCapacity`, `CapacityUtilization`, `DrainingCapacity`, `DrainModeActiveUserSessionCapacity`, and `DrainModeUnusedUserSessionCapacity` for multi-session fleets.

**To view fleet usage in the CloudWatch console**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the left pane, choose **Metrics**.

1. Choose the **AppStream** namespace and then choose **Fleet Metrics**.

1. Select the metrics to graph.