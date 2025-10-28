End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# The AWS CLI doesn't recognize `simspaceweaver`

If the AWS CLI gives you errors that suggest that it doesn't know about SimSpace Weaver,
run the following command.

```
aws simspaceweaver help
```

If you get an error that starts with the following lines and lists all available choices
then your AWS CLI might be an older version.

```
usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help

aws: error: argument command: Invalid choice, valid choices are:

```

Run the following command to check the version of your AWS CLI.

```
aws --version
```

If the version number is earlier than 2.9.19 then you
must update your AWS CLI. Note that the current version of the AWS CLI is later
than 2.9.19.

To update your AWS CLI, see [Install or update
the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide for
Version 2_.
