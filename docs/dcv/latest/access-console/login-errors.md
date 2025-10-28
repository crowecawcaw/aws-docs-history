# I'm having problems logging in

During login, the Web Client uses OAuth 2.0 with the Authentication Server to receive an access token that is used to obtain user information
and other information from the Handler. If you experience errors logging in, it could be due to either an error contacting the Handler, or
invalid PAM credentials if you configured your Console to use PAM.

## Error contacting the Handler

If you see an “Error contacting the handler” message, this means that the Web Client is unable to contact the Handler.

1. Check the [status of the handler](managing-component-process.md#checking-status-components "managing-component-process.md#checking-status-components") and the [handler components logs](using-component-log-files.md "using-component-log-files.md") to diagnose the problem.
2. Check that the web browser is able to connect to the host running the Handler. You could do this by using telnet to test connectivity to the port.

```
telnet handler-host 443
Trying *handler-host ip address*...
Connected to handler-host.
Escape character is '^]'.
^]
telnet> ^C
```

## Invalid PAM credentials

When the Authentication Server is setup to use PAM authentication, it validates the
username and the password using the PAM method of the operating system on the host
running the authentication server.

###### Verify PAM authentication configuration

1. Connect to the host on which you are running the Authentication Server.
2. Navigate to `/etc/dcv-access-console-auth-server/access-console-auth-server.properties` .
3. Verify that `pam-service-name` is set to `system-auth` for Red Hat based
   systems or `common-auth` for Ubuntu/Debian.
4. Restart the [Authentication Server](managing-component-process.md#restarting-components "managing-component-process.md#restarting-components").

###### Gather more detailed information.

1. Connect to the host on which you are running the Authentication Server.
2. Navigate to
   `/etc/dcv-access-console-auth-server/access-console-auth-server.properties`.
3. Enable `pam-normalize-userid-enabled` to true.
4. Enable [debug logs](using-component-log-files.md#changing-log-verbosity "using-component-log-files.md#changing-log-verbosity") for the `com.amazon.dcv.sm.ui.handler.authorization` class.
5. Restart the [Authentication Server](managing-component-process.md#restarting-components "managing-component-process.md#restarting-components").

###### Note

Enabling “Debug” logging prints the access and refreshes tokens in the logs. It is recommended you change the verbosity back to “Info” after debugging.
