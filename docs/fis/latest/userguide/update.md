# Update a target account configuration

You can update an existing target account configuration if you want to change the role ARN or description for the the account.
When you update a target account configuration, the changes do not affect any running experiments that use the template.

###### To update a target account configuration using the AWS Management Console

1. Open the AWS FIS console at [https://console.aws.amazon.com/fis/](https://console.aws.amazon.com/fis/ "https://console.aws.amazon.com/fis/").
2. In the navigation pane, choose **Experiment templates**
3. Select the experiment template, and choose **Actions**,
   **Update experiment template**.
4. In the side panel, choose **Step 3, Configure service access**.
5. Modify the **target account configurations**, and choose **Update experiment template**.
6. Select **Step 5, Review and create**.

###### To update a target account configuration using the CLI

Run the [update-target-account-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/update-target-account-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/update-target-account-configuration.html") command to
command, replacing the placeholder values in `italics` with your own values. The `--role-arn` and `--description` parameters are optional, and will not be updated if not included.

```
aws fis update-target-account-configuration --experiment-template-id `EXTxxxxxxxxx` --account-id `111122223333` --role-arn arn:aws:iam::`111122223333`:role/`role-name` --description `"my description"`
```
