# sam traces

This page provides reference information for the AWS Serverless Application Model Command Line Interface (AWS SAM CLI)
`sam traces` command.

For an introduction to the AWS SAM CLI, see [What is the AWS SAM CLI?](what-is-sam-overview.md#what-is-sam-cli "what-is-sam-overview.md#what-is-sam-cli")

The `sam traces` command fetches AWS X-Ray traces in your AWS account in the AWS Region.

## Usage

```
`$` `sam traces `<options>``
```

## Options

`--config-env `TEXT``

The environment name specifying the default parameter values in the configuration
file to use. The default value is "default". For more information about configuration
files, see [AWS SAM CLI configuration file](serverless-sam-cli-config.md "serverless-sam-cli-config.md").

`--config-file `PATH``

The path and file name of the configuration file containing default parameter
values to use. The default value is "`samconfig.toml`" in the root of
the project directory. For more information about configuration files, see [AWS SAM CLI configuration file](serverless-sam-cli-config.md "serverless-sam-cli-config.md").

`--end-time `TEXT``

Fetches traces up to this time. The time can be relative values like '5mins ago', 'tomorrow', or a formatted timestamp like '2018-01-01 10:10:10'.

`--output `TEXT``

Specifies the output format for logs. To print formatted logs, specify `text`. To print the logs as JSON, specify `json`.

`--save-params`

Save the parameters that you provide at the command line to the AWS SAM configuration file.

`--start-time `TEXT``

Fetches traces starting at this time. The time can be relative values like '5mins ago', 'yesterday', or a formatted timestamp like '2018-01-01 10:10:10'.
It defaults to '10mins ago'.

`--tail`

Tails the trace output. This ignores the end time argument and continues to display traces as they become available.

`--trace-id `TEXT``

The unique identifier for an X-Ray trace.

## Examples

Run the following command to fetch X-Ray traces by ID.

```
`$` `sam traces --trace-id `tracing-id-1` --trace-id `tracing-id-2``
```

Run the following command to tail X-Ray traces as they become available.

```
`$` `sam traces --tail`
```
