# AWS Secrets Manager Get Secret task

## Synopsis

Stores the value of a secret in AWS Secrets Manager into a secret build variable.

## Description

Use this task to retrieve the value of a secret stored in AWS Secrets Manager and store it
locally in an Azure DevOps build variable. The build variable will be automatically set to
'secret' mode to automatically mask the value when logged or otherwise displayed.

## Parameters

You can set the following parameters for the task. Required
parameters
are noted by an asterisk (\*). Other parameters are optional.

### Display name\*

The default name of the task instance, which can be modified: Secrets Manager Get Secret

### AWS Credentials

Specifies the AWS credentials to be used by the task in the build agent environment.

You can specify credentials using a service endpoint (of type AWS) in the task configuration or you can leave unspecified. If
unspecified the task will attempt to obtain credentials from the following sources in order:

- From task variables named _AWS.AccessKeyID_, _AWS.SecretAccessKey_ and optionally _AWS.SessionToken_.
- From credentials set in environment variables in the build agent process. When using environment variables in the
  build agent process you may use the standard AWS environment variables: _AWS_ACCESS_KEY_ID_, _AWS_SECRET_ACCESS_KEY_ and
  optionally _AWS_SESSION_TOKEN_.
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

**Note:** The Regions listed in the picker are those known
at the time this software was released. New Regions that are not listed may still be
used by entering the _region code_ of the Region (for example,
_us_west_2_).

### Secret ID/Name

Specifies the secret containing the version that you want to retrieve. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.

### Version ID

Specifies the unique identifier of the version of the secret that you want to retrieve. If you specify this parameter then don't specify _Version Stage_. If you don't specify either a _Version Stage_ or _Version ID_ then the default is to perform the operation on the version with the version stage value of _AWSCURRENT_.

### Version Stage

Specifies the version of the secret that you want to retrieve using the staging label attached to the version.

Staging labels are used to keep track of different versions during the rotation process. If you use this parameter then don't specify _Version ID_. If you don't specify either a _Version Stage_ or _Version ID_, then the default is to perform the operation on the version with the version stage value of _AWSCURRENT_.

## Task Permissions

This task requires permissions to call the following AWS service APIs (depending on selected task options, not all APIs may be used):

- secretsmanager:GetSecretValue
