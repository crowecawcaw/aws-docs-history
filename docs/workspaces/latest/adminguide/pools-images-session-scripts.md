# Use session scripts to manage your

users' streaming experience

WorkSpaces Pool provides on-instance session scripts. You can use these scripts to run your
own custom scripts when specific events occur in users' streaming sessions. For example,
you can use custom scripts to prepare your WorkSpaces Pools environment before your users'
streaming sessions begin. You can also use custom scripts to clean up streaming
instances after users complete their streaming sessions.

Session scripts are specified within a WorkSpace image. These scripts are run within
the user context or the system context. If your session scripts use the standard out to
write information, error, or debugging messaging, these can be optionally saved to an
Amazon S3 bucket within your Amazon Web Services account.

###### Contents

- [Run Scripts Before
  Streaming Sessions Begin](#run-scripts-before-streaming-sessions-begin "#run-scripts-before-streaming-sessions-begin")
- [Run Scripts After
  Streaming Sessions End](#run-scripts-after-streaming-sessions-end "#run-scripts-after-streaming-sessions-end")
- [Create and Specify Session
  Scripts](#create-specify-session-scripts "#create-specify-session-scripts")
- [Session Scripts Configuration
  File](#session-script-configuration-file "#session-script-configuration-file")
- [Using Windows
  PowerShell Files](#using-powershell-files-with-session-scripts "#using-powershell-files-with-session-scripts")
- [Logging Session Script Output](#logging-session-output "#logging-session-output")
- [Use persistent storage
  with session scripts](#use-storage-connectors-with-session-scripts "#use-storage-connectors-with-session-scripts")
- [Enable Amazon S3 Bucket
  Storage for Session Script Logs](#enable-S3-bucket-storage-session-script-logs "#enable-S3-bucket-storage-session-script-logs")

## Run Scripts Before

Streaming Sessions Begin

You can configure your scripts to run for a maximum of 60 seconds before your
users' applications launch and their streaming sessions begin. Doing so enables you
to customize the WorkSpaces Pools environment before users start streaming their
applications. When the session scripts run, a loading spinner displays for your
users. When your scripts complete successfully or the maximum waiting time elapses,
your users' streaming session will begin. If your scripts don't complete
successfully, an error message displays for your users. However, your users are not
prevented from using their streaming session.

When you specify a file name on a Windows instance, you must use a double
backslash. For example:

```
C:\\Scripts\\Myscript.bat
```

If you don't use a double backslash, an error displays to notify you that the
`.json` file is incorrectly formatted.

###### Note

When your scripts complete successfully, they must return a value of 0. If
your scripts return a value other than 0, WorkSpaces displays the error message to
the user.

When you run scripts before streaming sessions begin, the following process
occurs:

1. Your users connect to a WorkSpace in a WorkSpaces Pool that is not
   domain-joined. They connect by using SAML 2.0.
2. One of the following occurs:
   - If application settings persistence is enabled for your users, the
     application settings Virtual Hard Disk (VHD) file that stores your
     users' customizations and Windows settings is downloaded and
     mounted. Windows user login is required in this case.

   For information about application settings persistence, see [Enable application settings persistence for your
   WorkSpaces Pools users](app-settings-persistence.md "app-settings-persistence.md").
   - If application settings persistence is not enabled, the Windows
     user is already logged in.

3. Your session scripts start. If persistent storage is enabled for your
   users, storage connector mounting also starts. For information about
   persistent storage, see [Enable and Administer Persistent Storage for
   WorkSpaces Pools](persistent-storage.md "persistent-storage.md").

###### Note

The storage connector mount doesn't need to complete for the streaming
session to start. If the session scripts complete before the storage
connector mount completes, the streaming session starts.

For information about monitoring the mount status of storage
connectors, see [Use persistent storage
with session scripts](#use-storage-connectors-with-session-scripts "#use-storage-connectors-with-session-scripts"). 4. Your session scripts complete or time out. 5. The users' streaming session starts.

## Run Scripts After

Streaming Sessions End

You can also configure your scripts to run after users' streaming sessions end.
For example, you can run a script when users select **End Session**
from the WorkSpaces client toolbar, or when they reach the maximum allowed duration for
the session. You can also use these session scripts to clean up your WorkSpaces
environment before a streaming instance is terminated. For example, you can use
scripts to release file locks or upload log files. When you run scripts after
streaming sessions end, the following process occurs:

1. Your users' WorkSpaces streaming session ends.
2. Your session termination scripts start.
3. The session termination scripts complete or time out.
4. Windows user logout occurs.
5. One or both of the following occur in parallel, if applicable:
   - If application settings persistence is enabled for your users, the
     application settings VHD file that stores your users' customizations
     and Windows settings is unmounted and uploaded to an Amazon S3 bucket in
     your account.
   - If persistent storage is enabled for your users, the storage
     connector completes a final synchronization and is unmounted.

6. The WorkSpace is terminated.

## Create and Specify Session

Scripts

Complete the following procedure to create and specify session scripts for your
WorkSpaces in a WorkSpaces Pool.

1. Connect to the Windows WorkSpaces from which you are creating a custom
   image.
2. Create the directory `/AWSEUC/SessionScripts` if it does not
   already exist.
3. Create a configuration file
   `/AWSEUC/SessionScripts/config.json` if it does not already
   exist, using the [Session Script Configuration template](pools-images-session-scripts.md#session-script-configuration-file "pools-images-session-scripts.md#session-script-configuration-file").
4. Navigate to `C:\AWSEUC\SessionScripts`, and open the
   `config.json` configuration file.

For information about session script parameters, see [Session Scripts Configuration
File](#session-script-configuration-file "#session-script-configuration-file"). 5. After you finish making your changes, save and close the
`config.json` file. 6. Complete the steps to create an image from the WorkSpace. For more
information, see [Create a custom image and bundle for
WorkSpaces Pools](pools-images-custom-image.md "pools-images-custom-image.md").

## Session Scripts Configuration

File

To locate the session scripts configuration file in a Windows instance, navigate
to `C:\AWSEUC\SessionScripts\config.json`. The file is formatted as
follows.

###### Note

The configuration file is in JSON format. Verify that any text you type in
this file is in valid JSON format.

```
{
  "SessionStart": {
    "executables": [
      {
        "context": "system",
        "filename": "",
        "arguments": "",
        "s3LogEnabled": true
      },
      {
        "context": "user",
        "filename": "",
        "arguments": "",
        "s3LogEnabled": true
      }
    ],
    "waitingTime": 30
  },
  "SessionTermination": {
    "executables": [
      {
        "context": "system",
        "filename": "",
        "arguments": "",
        "s3LogEnabled": true
      },
      {
        "context": "user",
        "filename": "",
        "arguments": "",
        "s3LogEnabled": true
      }
    ],
    "waitingTime": 30
  }
}
```

You can use the following parameters in the session scripts configuration
file.

**`SessionStart/SessionTermination`**

The session scripts to run in the appropriate session event based on
the name of the object.

**Type**: String

**Required**: No

**Allowed values:**
`SessionStart`,
`SessionTermination`

**`WaitingTime`**

The maximum duration of the session scripts in seconds.

**Type**: Integer

**Required**: No

**Constraints:** The maximum duration is
60 seconds. If the session scripts don't complete within this duration,
they will be stopped. If you require a script to continue running,
launch it as a separate process.

**`Executables`**

The details for the session scripts to run.

**Type**: String

**Required**: Yes

**Constraints:** The maximum number of
scripts that can run per session event is 2 (one for the user context,
one for the system context).

**`Context`**

The context in which to run the session script.

**Type**: String

**Required**: Yes

**Allowed values:**
`user`, `system`

**`Filename`**

The full path to the session script to run. If this parameter is not
specified, the session script is not run.

**Type**: String

**Required**: No

**Constraints:** The maximum length for
the file name and full path is 1,000 characters.

**Allowed values:**
`.bat`, `.exe`,
`.sh`

###### Note

You can also use Windows PowerShell files. For more information,
see [Using Windows
PowerShell Files](#using-powershell-files-with-session-scripts "#using-powershell-files-with-session-scripts").

**`Arguments`**

The arguments for your session script or executable file.

**Type**: String

**Required**: No

**Length constraints:** The maximum
length is 1,000 characters.

**`S3LogEnabled`**

When the value for this parameter is set to
`True`, an S3 bucket is created within your
Amazon Web Services account to store the logs created by the session script. By
default, this value is set to `True`. For more
information, see the _Logging Session Script Output_
section later in this topic.

**Type**: Boolean

**Required**: No

**Allowed values:**
`True`, `False`

## Using Windows

PowerShell Files

To use Windows PowerShell files, specify the full path to the PowerShell file in
the `filename` parameter:

```
"filename":
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
```

Then specify your session script in the `arguments`
parameter:

```
"arguments": "-File \"C:\\path\\to\\session\\script.ps1\"",
```

Finally, verify that the PowerShell Execution Policy allows your PowerShell file
to run.

## Logging Session Script Output

When this option is enabled in the configuration file, WorkSpaces Pool automatically
captures the output from the session script that is written to the standard out.
This output is uploaded to an Amazon S3 bucket in your account. You can review the log
files for troubleshooting or debugging purposes.

###### Note

The log files are uploaded when the session script returns a value, or the
value set in `WaitingTime` has elapsed, whichever comes
first.

## Use persistent storage

with session scripts

When WorkSpaces persistent storage is enabled, the storage begins mounting when the
session start scripts run. If your script relies on persistent storage being
mounted, you can wait for the connectors to be available. WorkSpaces maintains the mount
status of the storage connectors in the Windows registry on Windows WorkSpaces, at the
following key:

```
HKEY_LOCAL_MACHINE\SOFTWARE\Amazon\AWSEUC\Storage\<provided user
                name>\<Storage connector>
```

The registry key values are as follows:

- Provided user name — The user ID provided through the access mode.
  The access modes and value for each mode are as follows:
  - User Pool — The email address for the user
  - Streaming URL — The UserID
  - SAML — The NameID. If the user name includes a slash (for
    example, a domain user’s SAMAccountName), the slash is replaced by a
    "-" character.

- Storage connector — The connector for the persistent storage option
  that is enabled for the user. The storage connector values are as
  follows:
  - HomeFolder

Each storage connector registry key contains a **MountStatus**
DWORD value. The following table lists the possible values for
**MountStatus**.

###### Note

To view these registry keys, you must have Microsoft .NET Framework version
4.7.2 or later installed on your image.

| Value | Description                                                |
| ----- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0     | Storage connector not be enabled for this user             |
| 1     | Storage connector mounting is in progress                  |
| 2     | Storage connector mounted successfully                     |
| 3     | Storage connector mounting failed                          |
| 4     | Storage connector mounting is enabled, but not mounted yet | ## Enable Amazon S3 Bucket Storage for Session Script Logs When you enable Amazon S3 logging in your session script configuration, WorkSpaces Pool captures standard output from your session script. The output is periodically uploaded to an S3 bucket within your Amazon Web Services account. For every AWS Region, WorkSpaces Pool creates a bucket in your account that is unique to your account and the Region. You do not need to perform any configuration tasks to manage these S3 buckets. They are fully managed by the WorkSpaces service. The log files that are stored in each bucket are encrypted in transit using Amazon S3's SSL endpoints and at rest using Amazon S3-managed encryption keys. The buckets are named in a specific format as follows: `` wspool-logs-`<region-code>`-`<account-id-without-hyphens>`-`random-identifier` `` **`<region-code>`** This is the AWS Region code in which the WorkSpaces Pool is created with Amazon S3 bucket storage enabled for session script logs. **`<account-id-without-hyphens>`** Your Amazon Web Services account identifier. The random ID ensures that there is no conflict with other buckets in that Region. The first part of the bucket name, `wspool-logs`, does not change across accounts or Regions. For example, if you specify session scripts in an image in the US West (Oregon) Region (`us-west-2`) on account number `123456789012`, WorkSpaces Pool creates an Amazon S3 bucket within your account in that Region with the name shown. Only an administrator with sufficient permissions can delete this bucket. `wspool-logs-us-west-2-1234567890123-abcdefg` Disabling session scripts does not delete log files stored in the S3 bucket. To permanently delete log files, you or another administrator with adequate permissions must do so by using the Amazon S3 console or API. WorkSpaces Pools adds a bucket policy that prevents accidental deletion of the bucket. When session scripts are enabled, a unique folder is created for each streaming session that is started. The path for the folder where the log files are stored in the S3 bucket in your account uses the following structure: `` `<bucket-name>`/`<stack-name>`/`<fleet-name>`/`<access-mode>`/`<user-id-SHA-256-hash>`/`<session-id>`/SessionScriptsLogs/`<session-event>` `` **`<bucket-name>`** The name of the S3 bucket in which the session scripts are stored. The name format is described earlier in this section. **`<stack-name>`** The name of the stack the session came from. **`<fleet-name>`** The name of the WorkSpaces Pool the session script is running on. **`<access-mode>`** The identity method of the user: `custom` for the WorkSpaces API or CLI, `federated` for SAML, and `userpool` for users in the user pool. **`<user-id-SHA-256-hash>`** The user-specific folder name. This name is created using a lowercase SHA-256 hash hexadecimal string generated from the user identifier. **`<session-id>`** The identifier of the user's streaming session. Each user streaming session generates a unique ID. **`<session-event>`** The event that generated the session script log. The event values are: `SessionStart` and `SessionTermination`. The following example folder structure applies to a streaming session started from the test-stack and test-fleet. The session uses the API of user ID `testuser@mydomain.com`, from an AWS account ID of `123456789012`, and the settings group `test-stack` in the US West (Oregon) Region (`us-west-2`): `wspool-logs-us-west-2-1234567890123-abcdefg/test-stack/test-fleet/custom/a0bcb1da11f480d9b5b3e90f91243143eac04cfccfbdc777e740fab628a1cd13/05yd1391-4805-3da6-f498-76f5x6746016/SessionScriptsLogs/SessionStart/` This example folder structure contains one log file for a user context session start script, and one log file for a system context session start script, if applicable. |
