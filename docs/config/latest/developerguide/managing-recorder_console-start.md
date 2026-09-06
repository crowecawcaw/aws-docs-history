

# Starting the customer managed configuration recorder
<a name="managing-recorder_console-start"></a>

You can use the AWS Config console or the AWS CLI start the customer managed configuration recorder.

------
#### [ To start the customer managed configuration recorder (Console) ]

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home).

1. Choose **Settings** in the navigation pane.

1. On the **Customer managed recorder** tab, choose **Start recording**. When prompted, choose **Confirm**.

------
#### [ To start the customer managed configuration recorder (CLI) ]

Use the [`start-configuration-recorder`](http://docs.aws.amazon.com/cli/latest/reference/configservice/start-configuration-recorder.html) command:

```
$ aws configservice start-configuration-recorder --configuration-recorder-name {{configRecorderName}}
```

------