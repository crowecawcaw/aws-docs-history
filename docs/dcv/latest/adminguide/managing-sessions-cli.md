# Using the Command Line Tool to Manage Sessions

The Amazon DCV server includes a command line tool that can be used to start, stop, and view Amazon DCV sessions.

## Using the command line tool on a Windows Amazon DCV Server

To use the command line tool on a Windows Amazon DCV server, run the commands from the Amazon DCV installation directory or add the Amazon DCV
directory to the PATH environment variable. If you add the Amazon DCV directory to the PATH environment variable, you can use the commands
from any directory.

###### To use the command line tool from the Amazon DCV installation directory

Navigate to the folder where the `dcv.exe` file is located, `C:\Program Files\NICE\DCV\Server\bin\` by
default, and open a command prompt window.

Or you can specify the full path when running a command from a different directory.

```
"`C:\>` Program Files\NICE\DCV\Server\bin\dcv.exe" list-sessions
```

###### To add the Amazon DCV directory to the PATH environment variable

1. In File Explorer, right-click **This PC** and choose **Properties**.
2. Choose **Advanced system settings**.
3. On the **Advanced** tab, choose **Environment Variables**.
4. In the **System variables** section, select the **Path** variable and choose
   **Edit**.
5. Choose **New** and specify the full path to the `bin` folder in the Amazon DCV installation directory
   (for example, `C:\Program Files\NICE\DCV\Server\bin\`).
6. Choose **OK** and close the Environment Variables window.

## Using the command line on a Linux Amazon DCV Server

On Linux Amazon DCV servers, the command line tool is automatically configured in the `$PATH` environment variable. You can
use the tool from any folder. Open a terminal window and enter the command to run.

## Command line tool usage

The following table covers the available command line tool options. This list can be retrieved by using `--help` when calling `dcv`.
For more information on how to use each command, pass in `--help` after the command you would like usage information for.
For example: `dcv create-session --help`.

| Command              | Description                                               |
| -------------------- | --------------------------------------------------------- |
| `create-session`     | Create a new DCV session                                  |
| `close-session`      | Close an active DCV session                               |
| `describe-session`   | Describe a DCV session                                    |
| `list-sessions`      | List the active DCV sessions                              |
| `list-connections`   | List the client connections for a DCV session             |
| `close-connection`   | Close an active client connection                         |
| `get-screenshot`     | Get a screenshot of the DCV console                       |
| `set-display-layout` | Set display layout of an active DCV session               |
| `set-name`           | Set name for a DCV session                                |
| `set-permissions`    | Set permissions of an active DCV session                  |
| `set-storage-root`   | Set storage root of an active DCV session                 |
| `reload-licenses`    | Force reloading the licenses for all the running sessions |
| `get-config`         | Get server configuration                                  |
| `list-endpoints`     | List the DCV endpoints                                    |
| `set-config`         | Set server configuration                                  |
| `version`            | Show the version of DCV                                   |
| `help`               | Show help                                                 |
