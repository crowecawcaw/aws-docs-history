# AWS SAM CLI configuration file

The AWS Serverless Application Model Command Line Interface (AWS SAM CLI) supports a project-level configuration file that you can use to
configure AWS SAM CLI command parameter values.

For documentation on creating and using configuration files, see [Configuring the AWS SAM CLI](using-sam-cli-configure.md "using-sam-cli-configure.md").

###### Topics

- [Default configuration file settings](#serverless-sam-cli-config-default "#serverless-sam-cli-config-default")
- [Supported configuration file formats](#serverless-sam-cli-config-formats "#serverless-sam-cli-config-formats")
- [Specify a configuration file](#serverless-sam-cli-config-specify "#serverless-sam-cli-config-specify")
- [Configuration file basics](#serverless-sam-cli-config-basics "#serverless-sam-cli-config-basics")
- [Parameter value rules](#serverless-sam-cli-config-rules "#serverless-sam-cli-config-rules")
- [Configuration precedence](#serverless-sam-cli-config-precedence "#serverless-sam-cli-config-precedence")
- [Creating and modifying configuration files](#serverless-sam-cli-config-using "#serverless-sam-cli-config-using")

## Default configuration file settings

AWS SAM uses the following default configuration file settings:

- **Name** – `samconfig`.
- **Location** – At the root of your project. This is the same location
  as your `template.yaml` file.
- **Format** – `TOML`. To learn more, see [TOML](https://toml.io/en/ "https://toml.io/en/") in the _TOML documentation_.

The following is an example project structure that includes the default configuration file name and location:

```
sam-app
├── README.md
├── __init__.py
├── events
├── hello_world
├── samconfig.toml
├── template.yaml
└── tests
```

The following is an example `samconfig.toml` file:

```
...
version = 0.1

[default]
[default.global]
[default.global.parameters]
stack_name = "sam-app"

[default.build.parameters]
cached = true
parallel = true

[default.deploy.parameters]
capabilities = "CAPABILITY_IAM"
confirm_changeset = true
resolve_s3 = true

[default.sync.parameters]
watch = true

[default.local_start_api.parameters]
warm_containers = "EAGER"

[prod]
[prod.sync]
[prod.sync.parameters]
watch = false
```

## Supported configuration file formats

`TOML` and `[YAML|YML]` formats are supported. See the following basic
syntax:

### TOML

```
version = 0.1
[`environment`]
[`environment`.`command`]
[`environment`.`command`.parameters]
`option` = `parameter value`
```

### YAML

```
version: 0.1
`environment`:
  `command`:
    parameters:
      `option`: `parameter value`
```

## Specify a configuration file

By default, the AWS SAM CLI looks for a configuration file in the following order:

1. **Custom configuration file** – If you use the
   `--config-file` option to specify a file name and location, the AWS SAM CLI looks for this file
   first.
2. **Default `samconfig.toml` file** – This is the
   default configuration file name and format, located at the root of your project. If you don’t specify a
   custom configuration file, the AWS SAM CLI looks for this file next.
3. **`samconfig.[yaml|yml]` file** – If
   the `samconfig.toml` does not exist at the root of your project, the AWS SAM CLI looks for
   this file.

The following is an example of specifying a custom configuration file using the `--config-file`
option:

```
`$` `sam deploy --config-file myconfig.yaml`
```

###### Note

The `--config-file` parameter must be relative to the location of the AWS SAM template file because the AWS SAM CLI needs to determine the context in which the configuration is applied.
The `samconfig.toml` file manages configuration settings for your version of the AWS SAM CLI, and the CLI looks for the `samconfig.toml` file
(or the overriden config file parameter) in the relative the folder of the `template.yaml` file.

## Configuration file basics

### Environment

An **environment** is a named identifier that contains a unique set of
configuration settings. You can have multiple environments in a single AWS SAM application.

The default environment name is `default`.

Use the AWS SAM CLI `--config-env` option to specify the environment to use.

### Command

The **command** is the AWS SAM CLI command to specify parameter values for.

To specify parameter values for all commands, use the `global` identifier.

When referencing an AWS SAM CLI command, replace spaces () and hyphens (`–`)
with underscores (`_`). See the following examples:

- `build`
- `local_invoke`
- `local_start_api`

### Parameters

**Parameters** are specified as key-value pairs.

- The **key** is the AWS SAM CLI command option name.
- The **value** is the value to specify.

When specifying keys, use the long-form command option name and replace hyphens (`–`) with
underscores (`_`). The following are examples:

- `region`
- `stack_name`
- `template_file`

## Parameter value rules

### TOML

- Boolean values can be `true` or `false`. For example,
  `confirm_changeset = true`.
- For string values, use quotation marks (`""`). For example,
  `region = "us-west-2"`.
- For list values, use quotation marks (`""`) and separate each value using a space
  (). For example: `capabilities = "CAPABILITY_IAM CAPABILITY_NAMED_IAM"`.
- For values that contain a list of key-value pairs, the pairs are space-delimited () and
  the value of each pair is surrounded by encoded quotation marks (`\" \"`). For example,
  `tags = "project=\"my-application\" stage=\"production\""`.
- For parameter values that can be specified multiple times, the value is an array of arguments. For
  example: `image_repositories = ["my-function-1=image-repo-1", "my-function-2=image-repo-2"]`.

### YAML

- Boolean values can be `true` or `false`. For example,
  `confirm_changeset: true`.
- For entries that contain a single string value, quotation marks (`""`) are optional. For
  example, `region: us-west-2`. This includes entries that contain multiple key-value pairs
  that are provided as a single string. The following is an example:

```
`$` `sam deploy --tags "foo=bar hello=world"`
```

```
default:
  deploy:
    parameters:
      tags: foo=bar hello=world
```

- For entries that contain a list of values, or entries that can be used multiple times in a single
  command, specify them as a list of strings.

The following is an example:

```
`$` `sam remote invoke --parameter "InvocationType=Event" --parameter "LogType=None"`
```

```
default:
  remote_invoke:
    parameters:
        parameter:
        - InvocationType=Event
        - LogType=None
```

## Configuration precedence

When configuring values, the following precedence takes place:

- Parameter values that you provide at the command line take precedence over corresponding values in the
  configuration file and `Parameters` section of the template file.
- If the `--parameter-overrides` option is used at the command line or in your configuration
  file with the `parameter_overrides` key, its values take precedence over values in the
  `Parameters` section of the template file.
- In your configuration file, entries provided for a specific command take precedence over global entries.
  In the following example, the `sam deploy` command will use the stack name
  `my-app-stack`.

TOML

```
[default.global.parameters]
stack_name = "common-stack"

[default.deploy.parameters]
stack_name = "my-app-stack"
```

YAML

```
default:
  global:
    parameters:
      stack_name: common-stack
  deploy:
    parameters:
      stack_name: my-app-stack
```

## Creating and modifying configuration files

### Creating configuration files

When you create an application using `sam init`, a default `samconfig.toml`
file is created. You can also manually create your configuration file.

### Modifying configuration files

You can manually modify your configuration files. Also, during any AWS SAM CLI interactive flow, configured
values will be displayed in brackets (`[ ]`). If you modify these values, the AWS SAM CLI will
update your configuration file.

The following is an example interactive flow using the `sam deploy --guided` command:

```
`$` `sam deploy --guided`

Configuring SAM deploy
======================

    Looking for config file [samconfig.toml] :  Found
    Reading default arguments  :  Success

    Setting default arguments for 'sam deploy'
    =========================================
    Stack Name [sam-app]: `ENTER`
    AWS Region [us-west-2]: `ENTER`
    #Shows you resources changes to be deployed and require a 'Y' to initiate deploy
    Confirm changes before deploy [Y/n]: `n`
    #SAM needs permission to be able to create roles to connect to the resources in your template
    Allow SAM CLI IAM role creation [Y/n]: `ENTER`
    #Preserves the state of previously provisioned resources when an operation fails
    Disable rollback [y/N]: `ENTER`
    HelloWorldFunction may not have authorization defined, Is this okay? [y/N]: `y`
    Save arguments to configuration file [Y/n]: `ENTER`
    SAM configuration file [samconfig.toml]: `ENTER`
    SAM configuration environment [default]: `ENTER`
```

When modifying your configuration file, the AWS SAM CLI handles global values as follows:

- If the parameter value exists in the `global` section of your configuration file, the
  AWS SAM CLI doesn’t write the value to the specific command section.
- If the parameter value exists in both the `global` and specific command sections, the
  AWS SAM CLI deletes the specific entry in favor of the global value.
