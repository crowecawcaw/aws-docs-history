

# Database authentication options for Amazon RDS
<a name="database-auth"></a>

Authentication determines how users and applications connect to your Amazon RDS database. This section provides an overview of the available authentication options in Amazon RDS and guidance for selecting the right method for your use case. 

This topic provides an overview of the available authentication options. For comprehensive documentation, see [Database authentication with Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/database-authentication.html) in the *Amazon RDS User Guide*.

**Note**  
By default, the **Easy create** option configures your database for password authentication. This means that you must specify a master username and password during creation, which are required when you connect to your DB instance. This is the simplest authentication option and requires no further configuration. If you need advanced authentication mechanisms, consider using the **Standard create** option.

**Topics**
+ [Password authentication](#password-auth)
+ [IAM database authentication](#password-iam-auth)
+ [Kerberos authentication](#password-kerberose-auth)
+ [Next steps](#database-auth-next-steps)

## Password authentication
<a name="password-auth"></a>

Password authentication is the default mechanism for databases. This method requires users to connect by providing a database username and password.
+ **Use case**: Simple and widely supported, suitable for basic database configurations and scenarios where external authentication systems are unnecessary.
+ **Considerations**: Ensure strong password policies and secure storage of credentials.

## IAM database authentication
<a name="password-iam-auth"></a>

IAM database authentication allows users and applications to connect to your database using AWS Identity and Access Management (IAM) users and roles in addition to the database password.
+ **Use case**: Enhances security by leveraging IAM for access control and avoids storing credentials directly in your application.
+ **Considerations**: Ensure strong password policies and secure storage of credentials.

## Kerberos authentication
<a name="password-kerberose-auth"></a>

Kerberos authentication integrates with an existing Active Directory to authenticate users connecting to your DB instance.
+ **Use case**: Enhances security by leveraging IAM for access control and avoids storing credentials directly in your application.
+ **Considerations**: Requires IAM policies and roles to be correctly configured. Best suited for environments that already use IAM for identity management.

## Next steps
<a name="database-auth-next-steps"></a>

Now that your DB instance is secure, the next step is to connect to it.

**Next step: **[Connecting to your Amazon RDS DB instance](connecting.md)