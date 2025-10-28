# Delete a target account configuration

If you no longer need a target account configuration, you can delete it.
When you delete a target account configuration, any running experiments that use the
template are not affected. The experiment continues to run until completed or stopped.

###### To delete a target account configuration using the AWS Management Console

1. Open the AWS FIS console at [https://console.aws.amazon.com/fis/](https://console.aws.amazon.com/fis/ "https://console.aws.amazon.com/fis/").
2. In the navigation pane, choose **Experiment
   templates**.
3. Select the experiment template, and choose **Actions**,
   **Update**.
4. In the side panel, choose **Step 3, Configure service access**.
5. Under **Target account configurations**, select **Remove** for the target account Role ARN you want to delete.
6. Select **Step 5, Review and create**.
7. Review the template and choose **Update experiment template**.
   When prompted for confirmation, enter `update` and choose **Update experiment template**.

###### To delete a target account configuration using the CLI

Run the [delete-target-account-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/delete-target-account-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/delete-target-account-configuration.html")
command, replacing the placeholder values in `italics` with your own values.

```
aws fis update-target-account-configuration --experiment-template-id `EXTxxxxxxxxx` --account-id `111122223333`
```
