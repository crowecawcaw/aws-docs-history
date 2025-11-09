# Configuring the AWS SAM CLI

One of the benefits of AWS SAM is that it optimizes a developer's time by removing repetitive
tasks. AWS SAM CLI includes a configuration file named
`samconfig` for this purpose. By default, no configuration to the
AWS SAM CLI is needed, but you can update your configuration file to
allow you to run commands with fewer parameters by allowing AWS SAM to instead reference your
customized parameters in your configuration file. The examples in the following table show
how you can optimize your commands:

| Original                                                               | Optimized with `samconfig` |
| ---------------------------------------------------------------------- | -------------------------- |
| **sam build --cached --parallel --use-containers**                     | **sam build**              |
| **sam local invoke --env-vars locals.json**                            | **sam local invoke**       |
| **sam local start-api --env-vars locals.json --warm-containers EAGER** | **sam local start-api**    |

The AWS SAM CLI provides a set of commands to help developers create,
develop, and deploy serverless applications. Each of these commands is configurable with optional flags based on the preferences of the application and developer. For more information, see
the [AWS SAM CLI content in GitHub](https://github.com/aws/aws-sam-cli "https://github.com/aws/aws-sam-cli")

The topics in this section show you how to create your [AWS SAM CLI configuration file](serverless-sam-cli-config.md "serverless-sam-cli-config.md")
and customize its default settings to optimize development time for your serverless application.

###### Topics

- [How to create your configuration file (the samconfig file)](#using-sam-cli-configure-create "#using-sam-cli-configure-create")
- [Configure project settings](#using-sam-cli-configure-project "#using-sam-cli-configure-project")
- [Configure credentials and basic
  settings](#using-sam-cli-configure-basic "#using-sam-cli-configure-basic")

## How to create your configuration file (the `samconfig` file)

The AWS SAM CLI configuration file (filename `samconfig`) is a text file that typically uses the TOML structure, but can also be in YAML.
When using an AWS Quick Start Template, this file is created when you run the **sam init** command.
You can update this file when you deploy an application using the **sam deploy -\-guided** command.

After the deployment is complete, the `samconfig` file contains a profile named `default` if you used the default values.
When you rerun the **deploy** command, AWS SAM applies the stored configuration settings from this profile.

The benefit of the `samconfig` file is that AWS SAM stores configuration settings for any other commands available in addition to the deploy command.
Beyond these values created at a new deploy, there are a number of attributes that you can set in the `samconfig` file that can simplify other
aspects of the developer workflow with AWS SAM CLI.

## Configure project settings

You can specify project-specific settings, such as AWS SAM CLI command parameter values, in a configuration file to
use with the AWS SAM CLI. For more information about this configuration file, see [AWS SAM CLI configuration file](serverless-sam-cli-config.md "serverless-sam-cli-config.md").

### Using configuration files

Configuration files are structured by environment, command, and parameter value. For more information, see
[Configuration file basics](serverless-sam-cli-config.md#serverless-sam-cli-config-basics "serverless-sam-cli-config.md#serverless-sam-cli-config-basics").

###### To configure a new environment

1. Specify your new environment in your configuration file.

The following is an example of specifying a new `prod` environment:

TOML

```
[prod.global.parameters]
```

YAML

```
prod:
  global:
    parameters:
```

2. Specify parameter values as key-value pairs in the parameters section of the configuration file.

The following is an example of specifying your application’s stack name for the `prod`
environment.

TOML

```
[prod.global.parameters]
stack_name = "prod-app"
```

YAML

```
prod:
  global:
    parameters:
      stack_name: prod-app
```

3. Use the `--config-env` option to specify the environment to use.

The following is an example:

```
`$` `sam deploy --config-env "prod"`
```

###### To configure parameter values

1. Specify the AWS SAM CLI command that you’d like to configure parameter values for. To configure parameter
   values for all AWS SAM CLI commands, use the `global` identifier.

The following is an example of specifying parameter values for the `default` environment’s
`sam deploy` command:

TOML

```
[default.deploy.parameters]
confirm_changeset = true
```

YAML

```
default:
  deploy:
    parameters:
      confirm_changeset: true
```

The following is an example of specifying parameter values for all AWS SAM CLI commands in the
`default` environment:

TOML

```
[default.global.parameters]
stack_name = "sam-app"
```

YAML

```
default:
  global:
    parameters:
      stack_name: sam-app
```

2. You can also specify parameter values and modify your configuration file through the AWS SAM CLI interactive
   flow.

The following is an example of the `sam deploy --guided` interactive flow:

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

For more information, see [Creating and modifying configuration files](serverless-sam-cli-config.md#serverless-sam-cli-config-using "serverless-sam-cli-config.md#serverless-sam-cli-config-using").

### Examples

#### Basic TOML example

The following is an example of a `samconfig.toml` configuration file:

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

#### Basic YAML example

The following is an example of a `samconfig.yaml` configuration file:

```
version 0.1
default:
  global:
    parameters:
      stack_name: sam-app
  build:
    parameters:
      cached: true
      parallel: true
  deploy:
    parameters:
      capabilities: CAPABILITY_IAM
      confirm_changeset: true
      resolve_s3: true
  sync:
    parameters:
      watch: true
  local_start_api:
    parameters:
      warm_containers: EAGER
prod:
  sync:
    parameters:
      watch: false
```

## Configure credentials and basic

settings

Use the AWS Command Line Interface (AWS CLI) to configure basic settings such as AWS credentials, default
region name, and default output format. Once configured, you can use these settings with the
AWS SAM CLI. To learn more, see the following from the
_AWS Command Line Interface User Guide_:

- [Configuration basics](../../../cli/latest/userguide/cli-configure-quickstart.md "../../../cli/latest/userguide/cli-configure-quickstart.md")
- [Configuration and credential file settings](../../../cli/latest/userguide/cli-configure-files.md "../../../cli/latest/userguide/cli-configure-files.md")
- [Named profiles for the AWS CLI](../../../cli/latest/userguide/cli-configure-profiles.md "../../../cli/latest/userguide/cli-configure-profiles.md")
- [Using an
  IAM Identity Center enabled named profile](../../../cli/latest/userguide/sso-using-profile.md "../../../cli/latest/userguide/sso-using-profile.md")

For quick setup instructions, see [Step 5: Use the AWS CLI to configure AWS credentials](prerequisites.md#prerequisites-configure-credentials "prerequisites.md#prerequisites-configure-credentials").
