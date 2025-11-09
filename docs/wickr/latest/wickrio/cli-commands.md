This guide provides documentation for Wickr IO Integrations. If you're
using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Wickr IO Command Line Interface (CLI)

The Wickr IO command line interface commands are used to perform operations on the Wickr
IO clients and the integrations you associate with them. The commands are described as
follows:

Many commands require a client number parameter shown as `[<#>]`. To obtain
the client number for a specific Wickr IO client, use the `list` command, which
displays all configured clients with their corresponding numbers in the first column (e.g., 0, 1,
2). Use this number when executing commands that require the `[<#>]`
parameter.

###### Topics

- [General Commands](#general-commands "#general-commands")
- [Client Management Commands](#client-commands "#client-commands")
- [Integration Management Commands](#integration-commands "#integration-commands")

## General Commands

The following are the general Wickr IO command line interface commands:

| Command          | Description                                                          |
| ---------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `help [command]` | Display the list of commands or help for the specified command.      |
| `version`        | Displays the current version number of the running Wickr IO Gateway. |
| `welcome [on     | off]`                                                                | Displays the welcome message or changes whether the welcome message is displayed when<br>you enter the command line interface. |

## Client Management Commands

The following are the Wickr IO command line interface client commands:

| Command              | Description                                                                                                                                                                                                                                                 |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `add`                | Adds a Wickr bot client to the Wickr IO Gateway. The Wickr bot client will be<br>associated with a Wickr user account and any associated integration.                                                                                                       |
| `avatar [<#>]`       | This command will change the avatar associated with a Wickr IO client. The avatar<br>file must be accessible to the software running on the Wickr IO docker image.                                                                                          |
| `config [<#>]`       | Re-runs the configuration of the specified Wickr IO Client. Can only be done on<br>paused clients.                                                                                                                                                          |
| `delete [<#>]`       | Deletes an existing client from the Wickr IO Gateway. The Wickr bot client will no<br>longer be associated with the Wickr IO Gateway system after the delete is<br>completed.                                                                               |
| `events [<#>]`       | Displays the list of events associated with the specified client. These events are<br>indications of when the client was started or stopped.                                                                                                                |
| `list [integration]` | Display a list of Wickr clients that have been added to the Wickr IO Gateway. If<br>the integration option is used, then a list of available integrations will be displayed. The<br>integration commands are described in the integration's commands below. |
| `modify [<#>]`       | Modify the settings of a client. You will be prompted for the settings that can be<br>changed. You can change the password, the integration associated with the client, and/or<br>change the settings.                                                      |
| `pause [<#>]`        | Pause a running Wickr IO client.                                                                                                                                                                                                                            |
| `restart [<#>]`      | Performs a stop and start of the Wickr IO client.                                                                                                                                                                                                           |
| `start [<#>]`        | Starts a Wickr IO client. If this is the first time the client has been started, you<br>will be prompted for the password associated with the Wickr user account.                                                                                           |

## Integration Management Commands

The following are the integration commands:

| Command              | Description                                                                                                                                                                                  |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `export [<#>]`       | Export the integration software associated with the specified Wickr IO client. This<br>will create a tar file that can be used with other Wickr IO clients.                                  |
| `import`             | Import custom integration software. The integration software has to adhere to specific<br>requirements, which are described later.                                                           |
| `list [integration]` | The list command with the 'integration' option will display a list of integrations that<br>are available for use with Wickr IO clients. This command may take up to a minute to<br>complete. |
| `rename [<#>]`       | Rename the integration of the specified Wickr IO client. This is useful when you want<br>to create a new integration using an existing integration as the base for the new<br>integration.   |
| `upgrade [<#>]`      | Update integration software for a Wickr IO client. This command will check to see if<br>there is a newer version of the integration software available and upgrade to that<br>version.       |
