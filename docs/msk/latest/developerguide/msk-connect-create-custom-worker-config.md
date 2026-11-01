

# Create a custom worker configuration
<a name="msk-connect-create-custom-worker-config"></a>

This procedure describes how to create a custom worker configuration using the AWS Management Console.

**Creating a custom worker configuration using the AWS Management Console**

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/](https://console.aws.amazon.com/msk/).

1. In the left pane, under **MSK Connect**, choose **Worker configurations**.

1. Choose **Create worker configuration**.

1. Enter a name and an optional description, then add the properties and values that you want to set them to.

1. Choose **Create worker configuration**.

To use the MSK Connect API to create a worker configuration, see [CreateWorkerConfiguration](https://docs.aws.amazon.com/MSKC/latest/mskc/API_CreateWorkerConfiguration.html).

To change the worker configuration that an existing connector uses, or to return a connector to the default worker configuration, update the connector's worker settings. For more information about updating worker settings, see [Update worker settings](mkc-update-connector.md#mkc-update-connector-worker-settings).