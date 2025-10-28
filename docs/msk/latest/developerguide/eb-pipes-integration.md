# Access Amazon EventBridge Pipes through the Amazon MSK

console

Amazon EventBridge Pipes connects sources to targets. Pipes are intended for point-to-point
integrations between supported sources and targets, with support for advanced transformations and
enrichment. EventBridge Pipes provide a highly scalable way to connect your Amazon MSK cluster to AWS services such as Step Functions, Amazon SQS, and API Gateway, as well as third-party software as a service (SaaS) applications like Salesforce.

To set up a pipe, you choose the source, add optional
filtering, define optional enrichment, and choose the target for the event data.

On the details page for an Amazon MSK cluster, you can view the pipes that use that
cluster as their source. From there, you can also:

- Launch the EventBridge console to view pipe details.
- Launch the EventBridge console to create a new pipe with the cluster as its source.
  For more information on configuring an Amazon MSK cluster as a pipe source, see
  [Amazon Managed Streaming for Apache Kafka cluster as a source](../../../eventbridge/latest/userguide/eb-pipes-msk.md "../../../eventbridge/latest/userguide/eb-pipes-msk.md")

in the _Amazon EventBridge User Guide_. For more information about EventBridge Pipes in general, see
[EventBridge Pipes](../../../eventbridge/latest/userguide/eb-pipes.md "../../../eventbridge/latest/userguide/eb-pipes.md").

###### To access EventBridge pipes for a given Amazon MSK cluster

1. Open the [Amazon MSK console](https://console.aws.amazon.com/msk/ "https://console.aws.amazon.com/msk/") and choose **Clusters** .
2. Select a cluster.
3. On the cluster detail page, choose the **Integration** tab.

The **Integration** tab includes a list of any pipes currently configured to use the selected
cluster as a source, including:

    * pipe name
    * current status
    * pipe target
    * when the pipe was last modified

4. Manage the pipes for your Amazon MSK cluster as desired:

**To access more details about a pipe**

    * Choose the pipe.


    This launches the **Pipe details** page of the EventBridge console.

**To create a new pipe**

    * Choose **Connect Amazon MSK cluster to pipe**.


    This launches the **Create pipe** page of the EventBridge console, with the Amazon MSK cluster
     specified as the pipe source. For more information, see [Creating an EventBridge pipe](../../../eventbridge/latest/userguide/eb-pipes-create.md "../../../eventbridge/latest/userguide/eb-pipes-create.md")
     in the *Amazon EventBridge User Guide*.


    * You can also create a pipe for a cluster from the **Clusters** page. Select
     the cluster, and, from the **Actions** menu, select
     **Create EventBridge Pipe**.
