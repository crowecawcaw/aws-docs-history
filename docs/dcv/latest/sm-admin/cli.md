# Broker CLI reference

The Amazon DCV Session Manager broker is a command-line interface (CLI) tool that provides administrative control over the Session Manager.
This reference covers the complete set of CLI commands available for managing sessions, users, resources, and
other aspects of the Session Manager. Administrators can automate routine management tasks, troubleshoot issues, and optimize
the performance of their Amazon DCV infrastructure.

Use the following commands if you use an external authentication server to generate OAuth 2.0 access tokens:

- [register-auth-server](register-auth-server.md "register-auth-server.md")
- [list-auth-servers](list-auth-servers.md "list-auth-servers.md")
- [unregister-auth-server](unregister-auth-server.md "unregister-auth-server.md")
  Use the following commands if you use the Session Manager broker as the OAuth 2.0 authentication server.

- [register-api-client](register-api-client.md "register-api-client.md")
- [describe-api-clients](describe-api-clients.md "describe-api-clients.md")
- [unregister-api-client](unregister-api-client.md "unregister-api-client.md")
- [renew-auth-server-api-key](renew-auth-server-api-key.md "renew-auth-server-api-key.md")
  Use the following commands to manage the Session Manager agent.

- [generate-software-statement](generate-software-statement.md "generate-software-statement.md")
- [describe-software-statements](describe-software-statements.md "describe-software-statements.md")
- [deactivate-software-statement](deactivate-software-statement.md "deactivate-software-statement.md")
- [describe-agent-clients](describe-agent-clients.md "describe-agent-clients.md")
- [unregister-agent-client](unregister-agent-client.md "unregister-agent-client.md")
  Use the following commands to manage the DCV server - DNS names mapping file.

- [register-server-dns-mappings](register-server-dns-mappings.md "register-server-dns-mappings.md")
- [describe-server-dns-mappings](describe-server-dns-mappings.md "describe-server-dns-mappings.md")
