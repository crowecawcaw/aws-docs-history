

# Stop an experiment
<a name="stop-experiment"></a>

You can stop a running experiment at any time. When you stop an experiment, any post actions that have not been completed for an action are completed before the experiment stops. You cannot resume a stopped experiment.

**To stop an experiment using the console**

1. Open the AWS FIS console at [https://console.aws.amazon.com/fis/](https://console.aws.amazon.com/fis/).

1. In the navigation pane, choose **Experiments**.

1. Select the experiment, and choose **Stop experiment**.

1. In the confirmation dialog box, choose **Stop experiment**.

**To stop an experiment using the CLI**  
Use the [stop-experiment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/stop-experiment.html) command.