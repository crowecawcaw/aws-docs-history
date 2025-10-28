# Enable open monitoring on

existing MSK Provisioned cluster

To enable open monitoring, make sure that the MSK Provisioned cluster is in the
`ACTIVE` state.

###### Using the AWS Management Console

1. Sign in to the AWS Management Console, and open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/ "https://console.aws.amazon.com/msk/home?region=us-east-1#/home/").
2. Choose the name of the cluster that you want to update. This takes you to
   a page the contains details for the cluster.
3. On the **Properties** tab, scroll down to find the
   **Monitoring** section.
4. Choose **Edit**.
5. Select the check box next to **Enable open monitoring with
   Prometheus**.
6. Choose **Save changes**.

###### Using the AWS CLI

- Invoke the [update-monitoring](../../../cli/latest/reference/kafka/update-monitoring.md "../../../cli/latest/reference/kafka/update-monitoring.md") command and specify its
  `open-monitoring` option. Enable the
  `JmxExporter`, the `NodeExporter`, or both. If you
  specify `open-monitoring`, the two exporters can't be disabled at
  the same time.

###### Using the API

- Invoke the [UpdateMonitoring](../../1.0/apireference/clusters-clusterarn-monitoring.md#UpdateMonitoring "../../1.0/apireference/clusters-clusterarn-monitoring.md#UpdateMonitoring") operation and specify
  `OpenMonitoring`. Enable the `jmxExporter`, the
  `nodeExporter`, or both. If you specify
  `OpenMonitoring`, the two exporters can't be disabled at the
  same time.
