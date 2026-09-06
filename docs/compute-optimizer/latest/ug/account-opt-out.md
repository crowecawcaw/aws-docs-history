

# Opting out of Compute Optimizer
<a name="account-opt-out"></a>

Use the following procedure to opt your account out of Compute Optimizer using the AWS CLI. This procedure also deletes your account's recommendations and related metrics data from Compute Optimizer. For more information, see [update-enrollment-status](https://docs.aws.amazon.com/cli/latest/reference/compute-optimizer/update-enrollment-status.html) in the *AWS CLI Command Reference*. 

**Note**  
You can't opt out using the Compute Optimizer console.

## Procedure
<a name="opt-in-procedure"></a>

**To opt an account out of Compute Optimizer**

1. Open a terminal or command prompt window.

   If you haven't already, install the AWS CLI and configure it to work with Compute Optimizer. For more information, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) and [Quickly Configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html#cli-quick-configuration) in the *AWS Command Line Interface User Guide*.

1. Enter the following command.

   ```
   aws compute-optimizer update-enrollment-status --status Inactive
   ```
**Note**  
You can't specify the `--include-member-accounts` parameter when opting out with the `update-enrollment-status` command. If you specify this parameter when opting out with this command, an error occurs.

Your account is opted out of Compute Optimizer after running the previous command. At the same time, your account's recommendations and related metrics data are deleted from Compute Optimizer. If you access the Compute Optimizer console, the option to opt in again should be displayed.