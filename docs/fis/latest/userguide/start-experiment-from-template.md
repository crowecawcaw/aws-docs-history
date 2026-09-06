

# Start an experiment from a template
<a name="start-experiment-from-template"></a>

After you have created an experiment template, you can start experiments using that template.

When you start an experiment, we create a snapshot of the specified template and use that snapshot to run the experiment. Therefore, if the experiment template is updated or deleted while the experiment is running, those changes have no impact on the running experiment.

When you start an experiment, AWS FIS creates a service-linked role on your behalf. For more information, see [Use service-linked roles for AWS Fault Injection Service](using-service-linked-roles.md).

After you start the experiment, you can stop it at any time. For more information, see [Stop an experiment](stop-experiment.md).

**To start an experiment using the console**

1. Open the AWS FIS console at [https://console.aws.amazon.com/fis/](https://console.aws.amazon.com/fis/).

1. In the navigation pane, choose **Experiment templates**.

1. Select the experiment template, and choose **Start experiment**.

1. (Optional) To add a tag to your experiment, choose **Add new tag** and enter a tag key and a tag value.

1. Choose **Start experiment**. When prompted for confirmation, enter **start** and choose **Start experiment**.

**To start an experiment using the CLI**  
Use the [start-experiment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/start-experiment.html) command.