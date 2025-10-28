# Using AWS CloudShell to access Amazon Keyspaces

AWS CloudShell is a browser-based, pre-authenticated shell that you can launch directly from the
AWS Management Console. You can run AWS CLI commands against AWS services using your preferred shell (Bash,
PowerShell or Z shell). To work with Amazon Keyspaces using `cqlsh`, you must install the `cqlsh-expansion`.
For `cqlsh-expansion` installation instructions, see [Using the cqlsh-expansion to connect
to Amazon Keyspaces](programmatic.md#using_cqlsh "programmatic.md#using_cqlsh").

You [launch AWS CloudShell from the AWS Management Console](../../../cloudshell/latest/userguide/working-with-cloudshell.md#launch-options "../../../cloudshell/latest/userguide/working-with-cloudshell.md#launch-options"), and the AWS credentials you used to sign in to
the console are automatically available in a new shell session. This pre-authentication of
AWS CloudShell users allows you to skip configuring credentials when interacting with AWS services
such as Amazon Keyspaces using `cqlsh` or AWS CLI version 2 (pre-installed on the shell's compute
environment).

## Obtaining IAM permissions for AWS CloudShell

Using the access management resources provided by AWS Identity and Access Management, administrators can grant
permissions to IAM users so they can access AWS CloudShell and use the environment's
features.

The quickest way for an administrator to grant access to users is through an AWS managed
policy. An [AWS managed
policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") is a standalone policy that's created and administered by AWS. The
following AWS managed policy for CloudShell can be attached to IAM identities:

- `AWSCloudShellFullAccess`: Grants permission to use AWS CloudShell with full
  access to all features.

If you want to limit the scope of actions that an IAM user can perform with AWS CloudShell,
you can create a custom policy that uses the `AWSCloudShellFullAccess` managed
policy as a template. For more information about limiting the actions that are available to
users in CloudShell, see [Managing AWS CloudShell access and usage with IAM policies](../../../cloudshell/latest/userguide/sec-auth-with-identities.md "../../../cloudshell/latest/userguide/sec-auth-with-identities.md") in the
_AWS CloudShell User Guide_.

###### Note

Your IAM identity also requires a policy that grants permission to make calls to
Amazon Keyspaces.

You can use an AWS managed policy to give your IAM identity access you Amazon Keyspaces, or start with the
managed policy as a template and remove the permissions that you don't need. You can also limit access to
specific keyspaces and tables to create a custom policy. The following managed policy for Amazon Keyspaces can be
attached to IAM identities:

- [AmazonKeyspacesFullAccess](../../../aws-managed-policy/latest/reference/AmazonKeyspacesFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonKeyspacesFullAccess.md") – This policy grants permission to use Amazon Keyspaces with full
  access to all features.

For a detailed explanation of the actions defined in the managed policy, see [AWS managed policies for Amazon Keyspaces](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

For more information about how to restrict actions or limit access to specific
resources in Amazon Keyspaces, see [How Amazon Keyspaces works with
IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md").

## Interacting with Amazon Keyspaces using AWS CloudShell

After you launch AWS CloudShell from the AWS Management Console, you can immediately start to interact with
Amazon Keyspaces using `cqlsh` or the command line interface. If you haven't already
installed the `cqlsh-expansion`, see [Using the cqlsh-expansion to connect
to Amazon Keyspaces](programmatic.md#using_cqlsh "programmatic.md#using_cqlsh") for detailed
steps.

###### Note

When using the `cqlsh-expansion` in AWS CloudShell, you don't need
to configure credentials before making calls, because you're already authenticated within the shell.

###### Connect to Amazon Keyspaces and create a new keyspace. Then read from a system table to confirm

that the keyspace was created using AWS CloudShell

1. From the AWS Management Console, you can launch CloudShell by choosing the following options
   available on the navigation bar:
   - Choose the CloudShell icon.
   - Start typing "cloudshell" in Search box and then choose the CloudShell
     option.

2. You can establish a connection to Amazon Keyspaces using the following command. Make sure to replace `cassandra.`us-east-1`.amazonaws.com`
   with the correct endpoint for your Region.

```
`cqlsh-expansion cassandra.`us-east-1`.amazonaws.com 9142 --ssl`
```

If the connection is successful, you should see output similar to the following example.

```
`Connected to Amazon Keyspaces at cassandra.us-east-1.amazonaws.com:9142
[cqlsh 6.1.0 | Cassandra 3.11.2 | CQL spec 3.4.4 | Native protocol v4]
Use HELP for help.
cqlsh current consistency level is ONE.
cqlsh>`
```

3. Create a new keyspace with the name `mykeyspace`. You can use the following
   command to do that.

```
CREATE KEYSPACE mykeyspace WITH REPLICATION = {'class': 'SingleRegionStrategy'};
```

4. To confirm that the keyspace was created, you can read from a system table using the following command.

```
SELECT * FROM system_schema_mcs.keyspaces WHERE keyspace_name = 'mykeyspace';
```

If the call is successful, the command line displays a response from the service
similar to the following output:

```
 keyspace_name  | durable_writes | replication
----------------+----------------+-------------------------------------------------------------------------------------
 mykeyspace     |           True | {'class': 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '3'}

(1 rows)
```
