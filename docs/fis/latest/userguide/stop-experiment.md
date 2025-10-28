# Stop an experiment

You can stop a running experiment at any time. When you stop an experiment, any
post actions that have not been completed for an action are completed before the
experiment stops. You cannot resume a stopped experiment.

###### To stop an experiment using the console

1. Open the AWS FIS console at [https://console.aws.amazon.com/fis/](https://console.aws.amazon.com/fis/ "https://console.aws.amazon.com/fis/").
2. In the navigation pane, choose **Experiments**.
3. Select the experiment, and choose **Stop
   experiment**.
4. In the confirmation dialog box, choose **Stop
   experiment**.

###### To stop an experiment using the CLI

Use the [stop-experiment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/stop-experiment.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/stop-experiment.html")
command.
