# Turn on event capture for an existing Amazon ECS cluster

You can enable event capture on an existing Amazon ECS cluster to store Amazon ECS-generated events in Amazon CloudWatch Logs through EventBridge. This feature helps you monitor and troubleshoot task failures, service deployments, and other cluster activities.

After you enable event capture, Amazon ECS creates the following resources:

- A Amazon CloudWatch Logs log group named `/aws/events/ecs/containerinsights/${clusterName}/performance`
- An EventBridge rule that captures all events from the `aws.ecs` source
  A **History** tab displays in the cluster view,
  allowing you to query task lifecycle events and service actions. Event capture begins
  immediately and stores all Amazon ECS-generated events according to your specified retention
  period.

## Prerequisites

- An existing Amazon ECS cluster
- Appropriate IAM permissions to modify cluster settings and create Amazon CloudWatch Logs resources

## Turn on event capture using the console

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Clusters**.
3. Select the cluster where you want to enable event capture.

The cluster details page displays. 4. Choose **Configuration**. 5. In the **ECS events** section, choose **Turn on event capture**.

The **Turn on event capture** dialog box
displays. 6. For **Expire event**, choose the retention period
for the Amazon CloudWatch Logs log group. The default is 7 days. 7. Choose **Turn on**.
