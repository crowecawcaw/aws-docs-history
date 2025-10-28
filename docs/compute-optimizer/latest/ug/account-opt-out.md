# Opting out of Compute Optimizer

Use the following procedure to opt your account out of Compute Optimizer using the AWS CLI. This
procedure also deletes your account's recommendations and related metrics data from Compute Optimizer. For
more information, see [update-enrollment-status](../../../cli/latest/reference/compute-optimizer/update-enrollment-status.md "../../../cli/latest/reference/compute-optimizer/update-enrollment-status.md") in the _AWS CLI Command Reference_.

###### Note

You can't opt out using the Compute Optimizer console.

## Procedure

###### To opt an account out of Compute Optimizer

1. Open a terminal or command prompt window.

If you haven't already, install the AWS CLI and configure it to work with Compute Optimizer. For more
information, see [Installing the
AWS CLI](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md") and [Quickly Configuring
the AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md#cli-quick-configuration "../../../cli/latest/userguide/cli-chap-configure.md#cli-quick-configuration") in the _AWS Command Line Interface User Guide_. 2. Enter the following command.

```
`aws compute-optimizer update-enrollment-status --status Inactive`
```

###### Note

You can't specify the `--include-member-accounts` parameter when opting
out with the `update-enrollment-status` command. If you specify this
parameter when opting out with this command, an error occurs.

Your account is opted out of Compute Optimizer after running the previous command. At the same time,
your account's recommendations and related metrics data are deleted from Compute Optimizer. If you access
the Compute Optimizer console, the option to opt in again should be displayed.
