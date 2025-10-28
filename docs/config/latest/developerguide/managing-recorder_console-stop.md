# Stopping the customer managed configuration

recorder

###### Note

**Service-linked configuration recorders are always
recording**

You cannot stop a service-linked configuration recorder because service-linked
configuration recorders are always recording. To stop recording, you must delete the
service-linked configuration recorder. For more information, see [Deleting the Configuration
Recorder](managing-recorder_console-delete.md "managing-recorder_console-delete.md").

You can use the AWS Config console or the AWS CLI stop the customer managed configuration
recorder.

To stop the customer managed configuration recorder (Console)

1. Sign in to the AWS Management Console and open the AWS Config console at
   [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home "https://console.aws.amazon.com/config/home").
2. Choose **Settings** in the navigation pane.
3. On the **Customer managed recorder** tab, choose **Stop
   recording**. When prompted, choose **Confirm**.

To stop the customer managed configuration recorder (CLI)
Use the [`stop-configuration-recorder`](../../../cli/latest/reference/configservice/stop-configuration-recorder.md "../../../cli/latest/reference/configservice/stop-configuration-recorder.md") command:

```
$ **aws configservice stop-configuration-recorder --configuration-recorder-name `configRecorderName`**
```
