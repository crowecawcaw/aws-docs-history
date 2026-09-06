

# sam local generate-event
<a name="sam-cli-command-reference-sam-local-generate-event"></a>

This page provides reference information for the AWS Serverless Application Model Command Line Interface (AWS SAM CLI) `sam local generate-event` subcommand.
+ For an introduction to the AWS SAM CLI, see [What is the AWS SAM CLI?](what-is-sam-overview.md#what-is-sam-cli)
+ For documentation on using the AWS SAM CLI `sam local generate-event` command, see [Introduction to testing with sam local generate-event](using-sam-cli-local-generate-event.md).

The `sam local generate-event` subcommand generates event payload samples for supported AWS services.

## Usage
<a name="ref-sam-cli-local-generate-event-usage"></a>

```
$ sam local generate-event {{<options> <service> <event> <event-options>}}
```

## Options
<a name="ref-sam-cli-local-generate-event-options"></a>

`--config-env TEXT`  <a name="ref-sam-cli-local-generate-event-options-config-env"></a>
The environment name specifying the default parameter values in the configuration file to use. The default value is "default". For more information about configuration files, see [AWS SAM CLI configuration file](serverless-sam-cli-config.md).

`--config-file {{PATH}}`  <a name="ref-sam-cli-local-generate-event-options-config-file"></a>
The path and file name of the configuration file containing default parameter values to use. The default value is `samconfig.toml` in the root of the project directory. For more information about configuration files, see [AWS SAM CLI configuration file](serverless-sam-cli-config.md).

`--help`  <a name="ref-sam-cli-local-generate-event-options-help"></a>
Shows this message and exits.

## Service
<a name="ref-sam-cli-local-generate-event-service"></a>

To see a list of supported services, run the following:

```
$ sam local generate-event
```

## Event
<a name="ref-sam-cli-local-generate-event-event"></a>

To see a list of supported events that can be generated for each service, run the following:

```
$ sam local generate-event {{<service>}}
```

## Event options
<a name="ref-sam-cli-local-generate-event-event-options"></a>

To see a list of supported event options that you can modify, run the following:

```
$ sam local generate-event {{<service> <event>}} --help
```

## Examples
<a name="sam-cli-command-reference-sam-local-generate-event-examples"></a>

For examples on using the `sam local generate-event` subcommand, refer to [Generate sample events](using-sam-cli-local-generate-event.md#using-sam-cli-local-generate-event-generate).