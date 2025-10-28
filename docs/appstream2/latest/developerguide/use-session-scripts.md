# Use Session Scripts to Manage Your Amazon AppStream 2.0 Users'

Streaming Experience

AppStream 2.0 provides on-instance session scripts. You can use these scripts to run your own
custom scripts when specific events occur in users' streaming sessions. For example, you
can use custom scripts to prepare your AppStream 2.0 environment before your users' streaming
sessions begin. You can also use custom scripts to clean up streaming instances after
users complete their streaming sessions.

Session scripts are specified within an AppStream 2.0 image. These scripts are run within the
user context or the system context. If your session scripts use the standard out to
write information, error, or debugging messaging, these can be optionally saved to an
Amazon S3 bucket within your Amazon Web Services account.

###### Contents

- [Run Scripts Before
  Streaming Sessions Begin](run-scripts-before-streaming-sessions-begin.md "run-scripts-before-streaming-sessions-begin.md")
- [Run Scripts After
  Streaming Sessions End](run-scripts-after-streaming-sessions-end.md "run-scripts-after-streaming-sessions-end.md")
- [Create and Specify Session
  Scripts](create-specify-session-scripts.md "create-specify-session-scripts.md")
- [Session Scripts Configuration
  File](session-script-configuration-file.md "session-script-configuration-file.md")
- [Using Windows
  PowerShell Files](using-powershell-files-with-session-scripts.md "using-powershell-files-with-session-scripts.md")
- [Logging Session Script Output](logging-session-output.md "logging-session-output.md")
- [Use Storage Connectors
  with Session Scripts](use-storage-connectors-with-session-scripts.md "use-storage-connectors-with-session-scripts.md")
- [Enable Amazon S3 Bucket
  Storage for Session Script Logs](enable-S3-bucket-storage-session-script-logs.md "enable-S3-bucket-storage-session-script-logs.md")
- [Use Session Scripts on Multi-Session Fleets](session-scripts-multi-session-fleets.md "session-scripts-multi-session-fleets.md")
