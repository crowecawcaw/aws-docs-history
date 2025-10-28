# AWS Shell Script task

## Synopsis

Run a shell script using Bash with AWS credentials.

## Description

Runs a shell script in Bash, setting AWS credentials and Region information into the
shell environment using the standard environment keys
_AWS_ACCESS_KEY_ID_, _AWS_SECRET_ACCESS_KEY_,
_AWS_SESSION_TOKEN_ and _AWS_REGION_.

## Parameters

You can set the following parameters for the task. Required parameters are noted by an
asterisk (\*). Other parameters are optional.

### Display name\*

The default name of the task instance, which can be modified: AWS Shell Script

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

The AWS Region code (us-east-1, us-west-2 etc.) of the Region containing the AWS
resources the task will use or create. For more information, see [Regions and endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in
the _Amazon Web Services General Reference_.

If a Region is not specified in the task configuration, the task will attempt to
obtain the Region to be used using the standard AWS environment variable
_AWS_REGION_ in the build agent process's environment. Tasks
running in build agents hosted on Amazon EC2 instances (Windows or Linux) will also
attempt to obtain the Region using the instance metadata associated with the EC2
instance if no Region is configured on the task or set in the environment
variable.

**Note:** The Regions listed in the picker are those known
at the time this software was released. New Regions that are not listed can still be
used by entering the _Region code_ of the Region (for example,
_us_west_2_).

### Arguments

The arguments to be passed to the shell script.

### Script Source

The source of the script to run in the shell. Choose _Script file_
to enter the file path to the script to be run or _Inline script_ to
specify the source code for the script in the task configuration.

### Script Path

When _Script Source_ is set to _Script file_,
specifies the file path to the script to execute. This must be a fully qualified path or
a path relative to the $(System.DefaultWorkingDirectory) location. The script file must
exist.

### Inline Script

The source code of the script to run when _Script Source_ is set
to _Inline script_. A maximum of 5000 characters is allowed.

### Specify Working Directory

If selected a custom working directory, which must exist, can be specified for the
script. The default behavior when unchecked is to set the working directory for the
shell to be the script file location.

### Working Directory

If _Specify Working Directory_ is checked, contains the custom
working directory for the script.

#### Fail on Standard Error

If this option is selected, the task will fail if any errors are written to the
standard error stream.

## Task Permissions

Permissions for this task to call AWS service APIs depend on the activities in the
supplied script.
