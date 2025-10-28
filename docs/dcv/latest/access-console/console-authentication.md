# Authentication methods

The Authentication Server for the Amazon DCV Access Console can be setup to use either
Pluggable Authentication Modules (PAM) or HTTP Header authentication. Utilizing PAM
authentication allows you to inherit your existing Linux authentication model. HTTP
Header authentication provides a customizable authentication mechanism to perform
additional validation before the end user reaches the authentication server.

## PAM authentication

The authentication server can be setup to use PAM authentication, it validates the
username and the password using the PAM method of the operating system on the host
running the authentication server.

###### Enabling PAM authentication

1. Connect to the host that is running the authentication server.
2. Open
   `/etc/dcv-access-console-auth-server/access-console-auth-server.properties`
   with your preferred editor.
3. Comment out or remove the `authentication-header-name` property
   to disable header based authentication if it is present.
4. Set the `pam-helper-path to the full path of the dcvpamhelper` that is
   installed as part of the authentication server. By default this is
   `/usr/share/dcv-access-console-auth-server/dcvpamhelper`.
5. Set the `pam-service-name` to the name of the file in
   `/etc/pam.d` that should be used to authenticate
   users.
   - To use the host’s authentication for Redhat based operating
     systems, set the `pam-service-name` property to
     `system-auth`.
   - To use the host’s authentication for Ubuntu/Debian based operating
     systems, set the `pam-service-name` to
     `common-auth`.

6. If the host uses different format of the username that are mapped to the
   same user in the operating system with the same uid and gid, set the
   `pam-normalize-userid-enabled` to true in order to normalize
   the username.

The userid is normalized using the command specified in
`pam-normalize-userid-command`, by default it runs `id
 -u -nr` for each username and uses the output of the command as
the userid. 7. Restart the authentication server.

```
sudo systemctl restart dcv-access-console-auth-server
```

## HTTP Header

authentication

The Amazon DCV Access Console can be setup to use the HTTP header in the request to the
Authentication Server to authenticate a user. The Authentication Server checks for
the configured header name in the request and uses the value of the header as the
user id.

This method is useful when there is an intermediary identity provider between the
Web Client and the Authentication Server. The intermediary solution authenticates
the user and forwards the request with the configured HTTP header. For example, the
authentication server can be setup behind a load balancer which uses an Amazon
Incognito user pool to validate the user.

###### Note

It is important that the intermediary solution removes the configured header
name from the requests from the web browser so that users cannot bypass the
authentication solution.

###### Configuring HTTP header authentication

1. Connect to the host that is running the authentication server.
2. Open
   `/etc/dcv-session-manager-ui-auth-server/session-manager-auth-server.properties`
   with your preferred editor.
3. Disable PAM based authentication if it is present, by commenting out or
   removing the `pam-helper-path` property.
4. Set the `authentication-header-name` to the header name in the
   request and use the value of the header as the userid.
5. Restart the authentication server.

```
sudo systemctl restart dcv-access-console-auth-server
```
