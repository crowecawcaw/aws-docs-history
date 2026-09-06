

# Adding a new database user when using RDS Proxy
<a name="rds-proxy-new-db-user"></a>

In some cases, you might add a new database user to an RDS DB instance or cluster that's associated with a proxy. Proceed depending on whether you're using standard authentication with Secrets Manager secrets or end-to-end IAM authentication.

If you are using the standard IAM authentication, follow these instructions:

1. Create a new Secrets Manager secret, using the procedure described in [Setting up database credentials for RDS Proxy](rds-proxy-secrets-arns.md). 

1. Update the IAM role to give RDS Proxy access to the new Secrets Manager secret. To do so, update the resources section of the IAM role policy. 

1. Modify the RDS Proxy to add the new Secrets Manager secret under **Secrets Manager secrets**.

1.  If the new user takes the place of an existing one, update the credentials stored in the proxy's Secrets Manager secret for the existing user. 

If you're using end-to-end IAM authentication, you need to create the database user and configure IAM permissions. To do this, run through the following steps:

1. Create a new database user in your database that matches the IAM user or role name you want to use for authentication.

1. Ensure the database user is configured with IAM authentication plugin at the database. See [Creating a database account using IAM authentication](UsingWithRDS.IAMDBAuth.DBAccounts.md).

1. Update the IAM policy to grant the `rds-db:connect` permission to the IAM user or role, as described in [Creating an IAM policy for end-to-end IAM authentication](rds-proxy-iam-setup.md#rds-proxy-iam-setup-e2e-steps).

1. Ensure your proxy is configured to use IAM authentication as the default authentication scheme.

With end-to-end IAM authentication, you don't need to manage database credentials in Secrets Manager secrets, as IAM credentials are used for authentication from the client to the proxy and from the proxy to the database. 

## Adding a new database user to a PostgreSQL database when using RDS Proxy
<a name="rds-proxy-new-db-user-pg"></a>

When adding a new user to your PostgreSQL database, if you have run the following command:

```
REVOKE CONNECT ON DATABASE postgres FROM PUBLIC;
```

Grant the `rdsproxyadmin` user the `CONNECT` privilege so the user can monitor connections on the target database. 

```
GRANT CONNECT ON DATABASE postgres TO rdsproxyadmin;
```

You can also allow other target database users to perform health checks by changing `rdsproxyadmin` to the database user in the command above.

## Changing the password for a database user when using RDS Proxy
<a name="rds-proxy-changing-db-user-password"></a>

In some cases, you might change the password for a database user in an RDS DB instance that's associated with a proxy. If so, update the corresponding Secrets Manager secret with the new password.

If you're using end-to-end IAM authentication, you don't need to update any passwords in Secrets Manager secrets.