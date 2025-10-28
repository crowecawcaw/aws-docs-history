This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Client configuration

Config file or deeplinks created on the Client Configuration screen are the second most
important thing an end user needs to successfully register and use Wickr Enterprise.

###### Note

Deeplink passwords are optional.

It displays currently active files or deeplinks, and will allow the administrator to expire
an active token, as well as download it again.

###### Note

It is not possible to download configuration files created before version 5.70.

The files and links are only used for the initial connection to Enterprise config files and
must be password protected, as the information within is encrypted. This allows the client to
establish a connection to the Enterprise service, but a user must still have a valid username and
password to complete the Registration or Sign In process.

After creating the configuration file, a deeplink URL and a deeplink landing page URL will
also be created.

The deeplink is a URL that will launch the app directly (on desktop, iOS, and Android) but
may not be directly usable on a mobile client. For security reasons many mobile mechanisms for
rendering that link will block it. In general, deeplink should work on desktop devices.

###### Note

Deeplink is not supported on Linux.

The deeplink landing page is a URL that any user can access from any normal mechanism. This
is the URL that should be distributed if the company is not hosting their own internal website for
the config file.

## Configuration naming

Administrators can enter custom names to identify the Wickr Enterprise configurations they
generate for client setup.
