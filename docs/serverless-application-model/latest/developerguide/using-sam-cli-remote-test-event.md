# Introduction to cloud testing with sam remote test-event

Use the AWS Serverless Application Model Command Line Interface (AWS SAM CLI) `sam remote test-event` command to access and manage shareable test events for your
AWS Lambda functions.

To learn more about shareable test events, see [Shareable test events](../../../lambda/latest/dg/testing-functions.md#creating-shareable-events "../../../lambda/latest/dg/testing-functions.md#creating-shareable-events") in the _AWS Lambda Developer Guide_.

###### Topics

- [Set up the AWS SAM CLI to use sam remote test-event](#using-sam-cli-remote-test-event-setup "#using-sam-cli-remote-test-event-setup")
- [Using the sam remote test-event command](#using-sam-cli-remote-test-event-use "#using-sam-cli-remote-test-event-use")
- [Using shareable test events](#using-sam-cli-remote-test-event-invoke "#using-sam-cli-remote-test-event-invoke")
- [Managing shareable test events](#using-sam-cli-remote-test-event-manage "#using-sam-cli-remote-test-event-manage")
  To use `sam remote test-event`, install the AWS SAM CLI by completing the
  following:

- [AWS SAM prerequisites](prerequisites.md "prerequisites.md").
- [Install the AWS SAM CLI](install-sam-cli.md "install-sam-cli.md").
  If you already have the AWS SAM CLI installed, we recommend upgrading to the latest version of the AWS SAM CLI version. To learn more, see
  [Upgrading the AWS SAM CLI](manage-sam-cli-versions.md#manage-sam-cli-versions-upgrade "manage-sam-cli-versions.md#manage-sam-cli-versions-upgrade").

Before using `sam remote test-event`, we recommend a basic understanding of the
following:

- [Configuring the AWS SAM CLI](using-sam-cli-configure.md "using-sam-cli-configure.md").
- [Create your application in AWS SAM](using-sam-cli-init.md "using-sam-cli-init.md").
- [Introduction to building with AWS SAM](using-sam-cli-build.md "using-sam-cli-build.md").
- [Introduction to deploying with AWS SAM](using-sam-cli-deploy.md "using-sam-cli-deploy.md").
- [Introduction to using sam sync to sync to AWS Cloud](using-sam-cli-sync.md "using-sam-cli-sync.md").

## Set up the AWS SAM CLI to use sam remote test-event

Complete the following set up steps to use the AWS SAM CLI `sam remote test-event` command:

1. **Configure the AWS SAM CLI to use your AWS account** – Shareable test events for Lambda can be accessed and managed by
   users within the same AWS account. To configure the AWS SAM CLI to use your AWS account, see [Configuring the AWS SAM CLI](using-sam-cli-configure.md "using-sam-cli-configure.md").
2. **Configure permissions for shareable test events** – To access and manage shareable test events, you must have the proper permissions.
   To learn more, see [Shareable test events](../../../lambda/latest/dg/testing-functions.md#creating-shareable-events "../../../lambda/latest/dg/testing-functions.md#creating-shareable-events") in the _AWS Lambda Developer Guide_.

## Using the sam remote test-event command

The AWS SAM CLI `sam remote test-event` command provides the following subcommands that you can use to access and manage your shareable test
events:

- `delete` – Delete a shareable test event from the Amazon EventBridge schema registry.
- `get` – Get a shareable test event from the EventBridge schema registry.
- `list` – List the existing shareable test events for a function from the EventBridge schema registry.
- `put` – Save an event from a local file to the EventBridge schema registry.

To list these subcommands using the AWS SAM CLI, run the following:

```
`$` `sam remote test-event --help`
```

### Deleting shareable test events

You can delete a shareable test event by using the `delete` subcommand along with the following:

- Provide the name of the shareable test event to delete.
- Provide an acceptable ID of the Lambda function associated with the event.
- If you are providing the Lambda function logical ID, you must also provide the AWS CloudFormation stack name associated with the Lambda function.

The following is an example:

```
`$` `sam remote test-event delete `HelloWorldFunction` --stack-name `sam-app` --name `demo-event``
```

For a list of options to use with the `delete` subcommand, see [sam remote test-event delete](sam-cli-command-reference-remote-test-event-delete.md "sam-cli-command-reference-remote-test-event-delete.md"). You can also run the following from the AWS SAM CLI:

```
`$` `sam remote test-event delete --help`
```

### Getting shareable test events

You can get a shareable test event from the EventBridge schema registry by using the `get` subcommand along with the following:

- Provide the name of the shareable test event to get.
- Provide an acceptable ID of the Lambda function associated with the event.
- If you are providing the Lambda function logical ID, you must also provide the AWS CloudFormation stack name associated with the Lambda function.

The following is an example that gets a shareable test event named `demo-event` that is associated with the `HelloWorldFunction` Lambda function of
the `sam-app` stack. This command will print the event to your console.

```
`$` `sam remote test-event get `HelloWorldFunction` --stack-name `sam-app` --name `demo-event``
```

To get a shareable test event and save it to your local machine, use the `--output-file` option and provide a file path and name. The following is an example that
saves `demo-event` as `demo-event.json` in the current working directory:

```
`$` `sam remote test-event get `HelloWorldFunction` --stack-name `sam-app` --name `demo-event` --output-file `demo-event.json``
```

For a list of options to use with the `get` subcommand, see [sam remote test-event get](sam-cli-command-reference-remote-test-event-get.md "sam-cli-command-reference-remote-test-event-get.md"). You can also run the following from the AWS SAM CLI:

```
`$` `sam remote test-event get --help`
```

### Listing shareable test events

You can list all shareable test events for a particular Lambda function from the schema registry. Use the `list` subcommand along with the following:

- Provide an acceptable ID of the Lambda function associated with the events.
- If you are providing the Lambda function logical ID, you must also provide the AWS CloudFormation stack name associated with the Lambda function.

The following is an example that obtains a list of all shareable test events associated with the `HelloWorldFunction` Lambda function of the
`sam-app` stack:

```
`$` `sam remote test-event list `HelloWorldFunction` --stack-name `sam-app``
```

For a list of options to use with the `list` subcommand, see [sam remote test-event list](sam-cli-command-reference-remote-test-event-list.md "sam-cli-command-reference-remote-test-event-list.md"). You can also run the following from the AWS SAM CLI:

```
`$` `sam remote test-event list --help`
```

### Saving shareable test events

You can save shareable test events to the EventBridge schema registry. Use the `put` subcommand along with the following:

- Provide an acceptable ID of the Lambda function associated with the shareable test event.
- Provide a name for the shareable test event.
- Provide the file path and name to the local event to upload.

The following is an example that saves the local `demo-event.json` event as `demo-event` and associates it with the
`HelloWorldFunction` Lambda function of the `sam-app` stack:

```
`$` `sam remote test-event put `HelloWorldFunction` --stack-name `sam-app` --name `demo-event` --file `demo-event.json``
```

If a shareable test event with the same name exists in the EventBridge schema registry, the AWS SAM CLI will not overwrite it. To overwrite, add the
`--force` option to your command.

For a list of options to use with the `put` subcommand, see [sam remote test-event put](sam-cli-command-reference-remote-test-event-put.md "sam-cli-command-reference-remote-test-event-put.md"). You can also run the following from the AWS SAM CLI:

```
`$` `sam remote test-event put --help`
```

## Using shareable test events

Use shareable test events to test your Lambda functions in the AWS Cloud with the `sam remote invoke` command. To learn more, see
[Pass shareable test events to a Lambda function in the cloud](using-sam-cli-remote-invoke.md#using-sam-cli-remote-invoke-shareable "using-sam-cli-remote-invoke.md#using-sam-cli-remote-invoke-shareable").

## Managing shareable test events

This topic contains examples on how you can manage and use shareable test events.

### Get a shareable test event, modify it, and use it

You can get a shareable test event from the EventBridge schema registry, modify it locally, and use the local test event with your Lambda function in the AWS Cloud. The following is
an example:

1. **Retrieve the shareable test event** – Use the `sam remote test-event get` subcommand to retrieve a shareable test event for a
   specific Lambda function and save it locally:

```
`$` `sam remote test-event get `HelloWorldFunction` --stack-name `sam-app` --name `demo-event` --output-file `demo-event.json``
```

2. **Modify the shareable test event** – Use a text editor of your choice to modify the shareable test event.
3. **Use the shareable test event** – Use the `sam remote invoke` command and provide the file path and name of the event with
   `--event-file`:

```
`$` `sam remote invoke `HelloWorldFunction` --stack-name `sam-app` --event-file `demo-event.json``
```

### Get a shareable test event, modify it, upload it, and use it

You can get a shareable test event from the EventBridge schema registry, modify it locally, and upload it. Then, you can pass the shareable test event directly to your Lambda
function in the AWS Cloud. The following is an example:

1. **Retrieve the shareable test event** – Use the `sam remote test-event get` subcommand to retrieve a shareable test event for a
   specific Lambda function and save it locally:

```
`$` `sam remote test-event get `HelloWorldFunction` --stack-name `sam-app` --name `demo-event` --output-file `demo-event.json``
```

2. **Modify the shareable test event** – Use a text editor of your choice to modify the shareable test event.
3. **Upload the shareable test event** – Use the `sam remote test-event put` subcommand to upload and save the shareable test
   event to the EventBridge schema registry. In this example, we use the `--force` option to overwrite an older version of our shareable test:

```
`$` `sam remote test-event put `HelloWorldFunction` --stack-name `sam-app` --name `demo-event` --file `demo-event.json` --force`
```

4. **Pass the shareable test event to your Lambda function** – Use the `sam remote invoke` command to pass the shareable test event
   directly to your Lambda function in the AWS Cloud:

```
`$` `sam remote invoke `HelloWorldFunction` --stack-name `sam-app` --test-event-name `demo-event``
```
