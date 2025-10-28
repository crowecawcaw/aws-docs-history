# AWS SSM Set Parameter Task

(AWS Systems Manager Set Parameter Task)

## Synopsis

Creates or updates a parameter in Systems Manager Parameter Store.

## Description

Use this task to creates or updates a parameter in Systems Manager Parameter Store.

## Parameters

You can set the following parameters for the task. Required
parameters
are noted by an asterisk (\*). Other parameters are optional.

### Display name\*

The default name of the task instance, which can be modified: Systems Manager Set Parameter

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

The AWS region code (for example, us-east-1, us-west-2) of the Region containing the
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

### Parameter Name

The name identifying a single parameter to be created or updated in the store.

### Parameter Type

The type of parameter to be written Choose from -

- String: the parameter is assigned a single string value
- String list: the parameter value is a comma-separated list of strings
- Secure string: the parameter value is encrypted at rest using either a service- or customer-provided KMS key

**Note:** If the parameter exists and is a secure string, this field is ignored and the secure string status of the parameter is retained.

### Parameter Value

The value for the parameter.

### KMS Key ID

If the parameter type is set to _Secure string_, identifies the customer-provided KMS key used to encrypt the parameter value at
rest. If a secure string type is specified but no key provided a service-provided KMS key is used to encrypt the parameter value.

## Task Permissions

This task requires permissions to call the following AWS service APIs (depending on selected task options, not all APIs may be used):

- ssm:GetParameter
- ssm:PutParameter
