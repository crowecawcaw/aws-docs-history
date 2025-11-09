# Automatic and On-Demand Diagnostic Log

Uploads

To help with troubleshooting issues that might occur when your users are using
the WorkSpaces Applications client, you can enable automatic or on-demand diagnostic log uploads,
or let your users do so themselves.

###### Note

Diagnostic logs do not contain sensitive information. You can disable automatic and on-demand diagnostic log uploads on user PCs that you manage, or allow your users to disable these features themselves.

**Automatic diagnostic log uploads**

When you install the client on PCs that you manage, you can configure the
WorkSpaces Applications client to upload diagnostic logs automatically. That way, when a client
issue occurs, the logs are sent to WorkSpaces Applications (AWS) without user interaction. For
more information, see [Configure Additional WorkSpaces Applications Client Settings for Your Users](install-client-configure-settings.md#configure-client "install-client-configure-settings.md#configure-client").

Or, you can let your users choose whether to enable automatic diagnostic
log uploads when they install the WorkSpaces Applications client, or after client installation.
For guidance that you can provide your users to help them perform this task, see
[Setup for Windows](client-application-windows-installation-user.md "client-application-windows-installation-user.md").

**On-demand diagnostic log uploads**

If you require more control over logging, you can disable automatic
logging and enable on-demand diagnostic log uploads. If you let your users
upload diagnostic logs on demand, they can also choose whether to send minidumps
(error reports) to WorkSpaces Applications (AWS) if an exception occurs or the client stops
responding.

For guidance that
you can provide your users to help them perform these tasks, see
[Logging](client-application-windows-how-to-enable-diagnostic-logging-user.md "client-application-windows-how-to-enable-diagnostic-logging-user.md").
