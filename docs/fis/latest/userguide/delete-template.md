# Delete an experiment template

If you no longer need an experiment template, you can delete it. When you delete
an experiment template, any running experiments that use the template are not
affected. The experiment continues to run until completed or stopped. However, experiment templates that are deleted are not available for viewing from the **Experiments** page in the console.

###### To delete an experiment template using the console

1. Open the AWS FIS console at [https://console.aws.amazon.com/fis/](https://console.aws.amazon.com/fis/ "https://console.aws.amazon.com/fis/").
2. In the navigation pane, choose **Experiment
   templates**.
3. Select the experiment template, and choose **Actions**,
   **Delete experiment template**.
4. When prompted for confirmation, enter `delete` and
   choose **Delete experiment template**.

###### To delete an experiment template using the CLI

Use the [delete-experiment-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/delete-experiment-template.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/delete-experiment-template.html") command.
