

# Stopping the customer managed configuration recorder
<a name="managing-recorder_console-stop"></a>

**Note**  
**Service-linked configuration recorders are always recording**  
You cannot stop a service-linked configuration recorder because service-linked configuration recorders are always recording. To stop recording, you must delete the service-linked configuration recorder. For more information, see [Deleting the Configuration Recorder](https://docs.aws.amazon.com/config/latest/developerguide/managing-recorder_console-delete.html).

You can use the AWS Config console or the AWS CLI stop the customer managed configuration recorder.

------
#### [ To stop the customer managed configuration recorder (Console) ]

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home).

1. Choose **Settings** in the navigation pane.

1. On the **Customer managed recorder** tab, choose **Stop recording**. When prompted, choose **Confirm**.

------
#### [ To stop the customer managed configuration recorder (CLI) ]

Use the [`stop-configuration-recorder`](http://docs.aws.amazon.com/cli/latest/reference/configservice/stop-configuration-recorder.html) command:

```
$ aws configservice stop-configuration-recorder --configuration-recorder-name {{configRecorderName}}
```

------