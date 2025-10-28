# Database authentication options for Amazon RDS

Authentication determines how users and applications connect to your Amazon RDS database. This
section provides an overview of the available authentication options in Amazon RDS and guidance for
selecting the right method for your use case.

This topic provides an overview of the available authentication options. For comprehensive
documentation, see [Database authentication with
Amazon RDS](../UserGuide/database-authentication.md "../UserGuide/database-authentication.md") in the _Amazon RDS User Guide_.

###### Note

By default, the **Easy create** option configures your database for
password authentication. This means that you must specify a master username and password
during creation, which are required when you connect to your DB instance. This is the
simplest authentication option and requires no further configuration. If you need advanced
authentication mechanisms, consider using the **Standard create**
option.

###### Topics

- [Password authentication](#password-auth "#password-auth")
- [IAM database authentication](#password-iam-auth "#password-iam-auth")
- [Kerberos authentication](#password-kerberose-auth "#password-kerberose-auth")
- [Next steps](#database-auth-next-steps "#database-auth-next-steps")

## Password authentication

Password authentication is the default mechanism for databases. This method requires
users to connect by providing a database username and password.

- **Use case**: Simple and widely supported, suitable for
  basic database configurations and scenarios where external authentication systems are
  unnecessary.
- **Considerations**: Ensure strong password policies and
  secure storage of credentials.

## IAM database authentication

IAM database authentication allows users and applications to connect to your database
using AWS Identity and Access Management (IAM) users and roles in addition to the database password.

- **Use case**: Enhances security by leveraging IAM for
  access control and avoids storing credentials directly in your application.
- **Considerations**: Ensure strong password policies and
  secure storage of credentials.

## Kerberos authentication

Kerberos authentication integrates with an existing Active Directory to authenticate
users connecting to your DB instance.

- **Use case**: Enhances security by leveraging IAM for
  access control and avoids storing credentials directly in your application.
- **Considerations**: Requires IAM policies and roles
  to be correctly configured. Best suited for environments that already use IAM for
  identity management.

## Next steps

Now that your DB instance is secure, the next step is to connect to it.

**Next step:** [Connecting to your Amazon RDS DB instance](connecting.md "connecting.md")
