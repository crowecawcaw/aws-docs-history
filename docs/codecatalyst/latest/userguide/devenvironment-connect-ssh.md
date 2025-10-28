Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Connecting to a Dev Environment using SSH

You can connect to your Dev Environment using SSH to perform actions without limitations, such as port forwarding, uploading and downloading files, and using other IDEs.

###### Note

If you want to continue using SSH for an extended time after closing the IDE tab or window, make sure to set a high timeout for your Dev Environment so that it
doesn't stop due to inactivity in the IDE.

###### Prerequisites

- You need one of the following operating systems:
  - Windows 10 or newer and OpenSSH enabled
  - macOS and Bash version 3 or higher
  - Linux with `yum`, `dpkg` or `rpm` package managers and Bash version 3 or higher

- You also need AWS CLI version 2.9.4 or higher.

###### To connect to a Dev Environment using SSH

1.  Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2.  Navigate to the project where you want to connect to a Dev Environment using SSH.
3.  In the navigation pane, choose **Code**.
4.  Choose **Dev Environments**.
5.  Choose a running Dev Environment you want to connect to using SSH.
6.  Choose **Connect via SSH**, choose your desired operating system, and do the following:
    - If you haven't done so already, paste and execute the first command in your specified terminal. The command
      downloads a script and executes the following modifications in your local environment
      so that you can connect to your Dev Environment using SSH:
      - Installs the [Session Manager plugin for the AWS CLI](../../../systems-manager/latest/userguide/session-manager-working-with-install-plugin.md "../../../systems-manager/latest/userguide/session-manager-working-with-install-plugin.md")
      - Modifies your local AWS Config and adds a CodeCatalyst profile so that you're able to perform the SSO login.
        For more information, see [Setting up to use the AWS CLI with CodeCatalyst](set-up-cli.md "set-up-cli.md").
      - Modifies your local SSH config and adds the required configuration for connecting to your Dev Environment using SSH.
      - Adds a script in the `~/.aws/codecatalyst-dev-env` directory that is used by the SSH client to connect to your Dev Environment.
        This script calls the [CodeCatalyst StartDevEnvironmentSession API](../APIReference/API_StartDevEnvironmentSession.md "../APIReference/API_StartDevEnvironmentSession.md")
        and uses AWS Systems Manager Session Manager plugin to establish an AWS Systems Manager session with your Dev Environment which is used by the local SSH client to securely connect to the remote Dev Environment.

    - Sign-in to Amazon CodeCatalyst using AWS SSO using the second command. This command requests and retrieves credentials so that the script in the
      `~/.aws/codecatalyst-dev-env` directory can call [CodeCatalyst StartDevEnvironmentSession API](../APIReference/API_StartDevEnvironmentSession.md "../APIReference/API_StartDevEnvironmentSession.md").
      This command should be executed every time your credentials expire. When you execute the last command in the modal(
      ssh <destination>) you will get an error if your credentials are expired or you haven’t performed the SSO login as instructed in this step.
    - Connect to your specified Dev Environment using SSH using the third command. This command has the following structure:

    ```
    ssh codecatalyst-dev-env=`<space-name>`=`<project-name>`=`<dev-environment-id>`
    ```

    You can also use this command to perform other actions allowed by the SSH client, such as port forwarding or uploading and downloading files:

        + Port forwarding:



        ```
        ssh -L `<local-port>`:127.0.0.1:`<remote-port>` codecatalyst-dev-env=`<space-name>`=`<project-name>`=`<dev-environment-id>`
        ```
        + Uploading a file to the home directory in your Dev Environment:



        ```
        scp -O `</path-to-local-file>` codecatalyst-dev-env=`<space-name>`=`<project-name>`=`<dev-environment-id>`:`</path-to-remote-file-or-directory>`
        ```
