# Using AWS CloudShell to work with AWS Security Incident Response

AWS CloudShell is a browser-based, pre-authenticated shell that you can launch directly from the
AWS Management Console. You can run AWS CLI commands against AWS services (including AWS Security Incident Response) using
your preferred shell (Bash, PowerShell or Z shell). And you can do this without needing to
download or install command line tools.

You [launch AWS CloudShell from the AWS Management Console](../../../cloudshell/latest/userguide/working-with-cloudshell.md#launch-options "../../../cloudshell/latest/userguide/working-with-cloudshell.md#launch-options"), and the AWS credentials you used to sign in to
the console are automatically available in a new shell session. This pre-authentication of
AWS CloudShell users allows you to skip configuring credentials when interacting with AWS services
such as Security Incident Response using AWS CLI version 2 (pre-installed on the shell's compute
environment).

###### Contents

- [Obtaining IAM permissions for AWS CloudShell](cloudshell-permissions.md "cloudshell-permissions.md")
- [Interacting with Security Incident Response using AWS CloudShell](cshell-examples.md "cshell-examples.md")
