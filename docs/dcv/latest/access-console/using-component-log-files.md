# Using the component log files

You can use the Amazon DCV Access Console component log files to identify and troubleshoot
problems with the different Amazon DCV Access Console components. The component logs contain
information about requests, responses, and errors regarding the component. The component
access log files contain information about access, throttling, authentication, and
authorization.

The log files can be found in the following locations on the host server that the Amazon DCV components are running on:

- Authentication Server

`/var/log/dcv-access-console-auth-server/DCV-access-console-auth-server.log`

`/var/log/dcv-access-console-auth-server/DCV-access-console-auth-server-access.log`

- Handler

`/var/log/dcv-access-console-handler/DCV-access-console-handler.log`

`/var/log/dcv-access-console-handler/DCV-access-console-handler-access.log`

- Web Client

`/var/log/dcv-access-console-webclient/DCV-access-console-webclient.log`

`/var/log/dcv-access-console-webclient/DCV-access-console-webclient-access.log`

- Ngnix

`/var/log/nginx/error.log`

`/var/log/nginx/access.log`
The Amazon DCV Access Console components enable you to configure the verbosity level of the log files. The following verbosity levels are available:

- `error` – Provides the least detail. Includes errors only.
- `warn` – Includes errors and warnings.
- `info` – The default verbosity level. Includes errors, warnings, and information messages.
- `debug` – Provides the most detail. Provides detailed information that is useful for debugging issues.
  If you need to locate the logs for the session manager broker or session manager agent,
  see [Amazon DCV Session Manager administrator guide](../sm-admin/what-is-sm.md "../sm-admin/what-is-sm.md").

## Changing log file verbosity

To configure the log file verbosity, you must configure the log setting file by updating the `logback.xml` file with
the appropriate class names and then restart the component processes.

###### Changing the Authentication Server log file verbosity

1. Navigate to `/etc/dcv-access-console-auth-server` and open the `logback.xml` file with your preferred text editor.
2. Update the level for `com.amazon.dcv.sm.ui` to the desired level of verbosity.
3. Update the level for `com.amazon.dcv.sm.ui.authserver.throttling` to the desired
   level of verbosity.

###### To change the Handler log file verbosity

1. Navigate to `/etc/dcv-access-console-handler` and open the `logback-spring.xml` file with your preferred text editor.
2. Update the level for `com.amazon.dcv.sm.ui` to the desired level of verbosity.
3. Update the level for `com.amazon.dcv.sm.ui.handler.authorization` to the desired level of verbosity.
4. Update the level for `com.amazon.dcv.sm.ui.authserver.throttling` to the desired level of verbosity.
