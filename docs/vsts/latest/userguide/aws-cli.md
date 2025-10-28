# AWS CLI task

## Synopsis

Runs a command using the AWS CLI. Note that you must have the AWS CLI installed to use this
task. For more information, see [Installing the AWS Command
Line Interface](../../../cli/latest/userguide/installing.md "../../../cli/latest/userguide/installing.md").

## Description

The AWS CLI uses a multipart structure on the command line. It starts with the base call
to AWS. The next part specifies a top-level command, which often represents an AWS service
that the AWS CLI supports. Each AWS service has additional subcommands that specify the
operation to perform. You can specify the general AWS CLI options, or the specific parameters
for an operation, in any order on the command line. If you specify an exclusive parameter
multiple times, only the last value applies.

```
<command> <subcommand> [options and parameters]
```

Parameters can take various types of input values such as numbers, strings, lists, maps,
and JSON structures.

## Parameters

You can set the following parameters for the task. Required parameters are noted by an
asterisk (\*). Other parameters are optional.

### Display name\*

The default name of the task instance, which can be modified: AWS CLI

### AWS Credentials

Specifies the AWS credentials to be used by the task in the build agent
environment.

You can specify credentials using a service endpoint (of type AWS) in the task
configuration or you can leave unspecified. If unspecified the task will attempt to
obtain credentials from the following sources in order:

- From task variables named _AWS.AccessKeyID_,
  _AWS.SecretAccessKey_ and optionally
  _AWS.SessionToken_.
- From credentials set in environment variables in the build agent process. When
  using environment variables in the build agent process you may use the standard
  AWS environment variables: _AWS_ACCESS_KEY_ID_,
  _AWS_SECRET_ACCESS_KEY_ and optionally
  _AWS_SESSION_TOKEN_.
- If the build agent is running on an Amazon EC2 instance, from the instance
  metadata associated with the EC2 instance. For credentials to be available from
  EC2 instance metadata the instance must have been started with an instance profile
  referencing a role granting permissions to the task to make calls to AWS on your
  behalf. For more information, see [Using an IAM role to grant permissions to applications running on Amazon EC2
  instances](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md").

### AWS Region

The AWS Region code (for example, us-east-1, us-west-2) of the Region containing the
AWS resources the task will use or create. For more information, see [Regions and endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in
the _Amazon Web Services General Reference_.

If a Region is not specified in the task configuration the task will attempt to
obtain the Region to be used using the standard AWS environment variable
_AWS_REGION_ in the build agent process's environment. Tasks
running in build agents hosted on Amazon EC2 instances (Windows or Linux) will also
attempt to obtain the Region using the instance metadata associated with the EC2
instance if no Region is configured on the task or set in the environment
variable.

###### Note

The Regions listed in the picker are those known at the time this software was
released. New Regions that are not listed may still be used by entering the
_region code_ of the Region (for example,
_us_west_2_).

### Command\*

The AWS CLI command to run. Run `aws help` in the AWS Command Line Interface to get a
complete list of commands, or see [CommandStructure](../../../cli/latest/userguide/command-structure.md "../../../cli/latest/userguide/command-structure.md") in the AWS Command Line Interface.

### Subcommand

The AWS CLI subcommand to run. Run `aws help` in the AWS Command Line Interface to get a
complete list of commands, or see [CommandStructure](../../../cli/latest/userguide/command-structure.md "../../../cli/latest/userguide/command-structure.md") in the AWS Command Line Interface.

### Options and Parameters

The arguments to pass to the AWS CLI command. Run `aws <command>
 --help` in the AWS Command Line Interface to get the complete list of arguments supported by the
command.

### Advanced

#### Fail on Standard Error

If true, this task fails if any errors are written to the StandardError
stream.

## Task Permissions

Permissions for this task to call AWS service APIs depend on the configured
command.
