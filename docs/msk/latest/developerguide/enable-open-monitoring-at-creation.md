# Enable open monitoring on new

MSK Provisioned clusters

This procedure describes how to enable open monitoring on a new
MSK cluster using the AWS Management Console, the AWS CLI, or the Amazon MSK
API.

###### Using the AWS Management Console

1. Sign in to the AWS Management Console, and open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/ "https://console.aws.amazon.com/msk/home?region=us-east-1#/home/").
2. In the **Monitoring** section, select the check box next
   to **Enable open monitoring with Prometheus**.
3. Provide the required information in all the sections of the page, and
   review all the available options.
4. Choose **Create cluster**.

###### Using the AWS CLI

- Invoke the [create-cluster](../../../cli/latest/reference/kafka/create-cluster.md "../../../cli/latest/reference/kafka/create-cluster.md") command and specify its
  `open-monitoring` option. Enable the
  `JmxExporter`, the `NodeExporter`, or both. If you
  specify `open-monitoring`, the two exporters can't be disabled at
  the same time.

###### Using the API

- Invoke the [CreateCluster](../../1.0/apireference/clusters.md#CreateCluster "../../1.0/apireference/clusters.md#CreateCluster") operation and specify
  `OpenMonitoring`. Enable the `jmxExporter`, the
  `nodeExporter`, or both. If you specify
  `OpenMonitoring`, the two exporters can't be disabled at the
  same time.
