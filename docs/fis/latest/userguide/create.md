# Create a multi-account experiment template

###### To learn how to create an experiment template via the AWS Management Console

See [Create an experiment template](create-template.md "create-template.md").

###### To create an experiment template using the CLI

1. Open the AWS Command Line Interface
2. To create an experiment from a saved JSON file with the account targeting experiment option set to `"multi-account"` (for example, `my-template.json`),
   replace the placeholder values in `italics` with your own values, and then run the following
   [create-experiment-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/create-experiment-template.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/create-experiment-template.html") command.

```
aws fis create-experiment-template --cli-input-json file://`my-template`.json
```

This will return the experiment template in the response. Copy the `id` from the response, which is the ID of the experiment template. 3. Run the [create-target-account-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/create-target-account-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/create-target-account-configuration.html") command to add a target account configuration
to the experiment template. Replace the placeholder values in `italics` with your own values,
using the `id` from step 2 as the value for the `--experiment-template-id` parameter, and then run the following.
The `--description` parameter is optional. Repeat this step for each target account.

```
aws fis create-target-account-configuration --experiment-template-id `EXTxxxxxxxxx` --account-id `111122223333` --role-arn arn:aws:iam::`111122223333`:role/`role-name` --description `"my description"`
```

4. Run the [get-target-account-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/get-target-account-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/get-target-account-configuration.html") command to retrieve the details for a specific target account configuration.

```
aws fis get-target-account-configuration --experiment-template-id `EXTxxxxxxxxx` --account-id `111122223333`
```

5. Once you have added all your target account configurations, you can run the [list-target-account-configurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/list-target-account-configurations.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/list-target-account-configurations.html") command
   command to see that your target account configurations have been created.

```
aws fis list-target-account-configurations --experiment-template-id `EXTxxxxxxxxx`
```

You can also verify that you have added target account configurations by running the [get-experiment-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/get-experiment-template.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/get-experiment-template.html") command.
The template will return a read-only field `targetAccountConfigurationsCount` that is a count of all the target account configurations on the experiment template. 6. When you are ready, you can run the experiment template using the [start-experiment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/start-experiment.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/start-experiment.html") command.

```
aws fis start-experiment --experiment-template-id `EXTxxxxxxxxx`
```
