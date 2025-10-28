# Viewing Fleet Usage Using the Console

You can monitor your Amazon AppStream 2.0 fleet usage using the AppStream 2.0 or CloudWatch console.

###### To view fleet usage in the AppStream 2.0 console

1. Open the AppStream 2.0 console at
   [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2. In the left pane, choose **Fleets**.
3. Select a fleet and choose its **Fleet Usage** tab.
4. By default, the graph displays the following metrics:
   - `ActualCapacity`, `InUseCapacity`,
     `DesiredCapacity`, `AvailableCapacity`,
     `PendingCapacity`, and `CapacityUtilization`
     for single-session fleets.
   - `ActualUserSessionCapacity`,
     `ActiveUserSessionCapacity`,
     `AvailableUserSessionCapacity`,
     `DesiredUserSessionCapacity`,
     `PendingUserSessionCapacity`, and
     `CapacityUtilization` for multi-session fleets.

###### To view fleet usage in the CloudWatch console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left pane, choose **Metrics**.
3. Choose the **AppStream** namespace and then choose
   **Fleet Metrics**.
4. Select the metrics to graph.
