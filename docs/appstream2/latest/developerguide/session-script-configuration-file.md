# Session Scripts Configuration File

To locate the session scripts configuration file in a Windows instance, navigate
to C:\AppStream\SessionScripts\config.json. On a Linux instance, navigate to
/opt/appstream/SessionScripts/config.json. The file is formatted as follows.

###### Note

The configuration file is in .json format. Verify that any text you type in
this file is in valid .json format.

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
see [Using Windows PowerShell Files](using-powershell-files-with-session-scripts.md "using-powershell-files-with-session-scripts.md").

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
