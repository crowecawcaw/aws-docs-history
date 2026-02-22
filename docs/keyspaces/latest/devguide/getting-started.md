# Tutorial prerequisites and considerations

Before you can get started with Amazon Keyspaces, follow the AWS setup instructions in [Accessing Amazon Keyspaces (for Apache Cassandra)](accessing.md "accessing.md"). These steps include signing up for AWS
and creating an AWS Identity and Access Management (IAM) user with access to Amazon Keyspaces.

To complete all the steps of the tutorial, you need to install `cqlsh`. You
can follow the setup instructions at [Using cqlsh to connect to
Amazon Keyspaces](programmatic.md "programmatic.md").

To access Amazon Keyspaces using `cqlsh` or the AWS CLI, we recommend using AWS CloudShell. CloudShell
is a browser-based, pre-authenticated shell that you can launch directly from the
AWS Management Console. You can run AWS Command Line Interface (AWS CLI) commands against Amazon Keyspaces using your preferred shell (Bash,
PowerShell or Z shell). To use `cqlsh`, you must install the
`cqlsh-expansion`. For `cqlsh-expansion` installation
instructions, see [Using the cqlsh-expansion to connect
to Amazon Keyspaces](programmatic.md#using_cqlsh "programmatic.md#using_cqlsh"). For more information about CloudShell see
[Using AWS CloudShell to access Amazon Keyspaces](using-aws-with-cloudshell.md "using-aws-with-cloudshell.md").

To use the AWS CLI to create, view, and delete resources in Amazon Keyspaces, follow the setup instructions
at [Downloading and Configuring the
AWS CLI](access.md#access.cli.installcli "access.md#access.cli.installcli").

After completing the
prerequisite steps, proceed to [Create a keyspace in Amazon Keyspaces](getting-started.md "getting-started.md").
