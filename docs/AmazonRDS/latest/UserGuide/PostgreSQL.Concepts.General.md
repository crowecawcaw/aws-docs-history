# Using SSL with a PostgreSQL DB

instance

Amazon RDS supports Secure Socket Layer (SSL) encryption for PostgreSQL DB instances.
Using SSL, you can encrypt a PostgreSQL connection between your applications and
your PostgreSQL DB instances. By default, RDS for PostgreSQL uses and expects all clients
to connect using SSL/TLS, but you can also require it. RDS for PostgreSQL supports
Transport Layer Security (TLS) versions 1.1, 1.2, and 1.3.

For general information about SSL support and PostgreSQL databases, see [SSL support](https://www.postgresql.org/docs/11/libpq-ssl.html "https://www.postgresql.org/docs/11/libpq-ssl.html") in
the PostgreSQL documentation. For information about using an SSL connection over
JDBC, see [Configuring
the client](https://jdbc.postgresql.org/documentation/head/ssl-client.html "https://jdbc.postgresql.org/documentation/head/ssl-client.html") in the PostgreSQL documentation.

SSL support is available in all AWS Regions for PostgreSQL. Amazon RDS creates an SSL
certificate for your PostgreSQL DB instance when the instance is created. If you
enable SSL certificate verification, then the SSL certificate includes the DB
instance endpoint as the Common Name (CN) for the SSL certificate to guard against
spoofing attacks.

###### Topics

- [Connecting to a
  PostgreSQL DB instance over SSL](#PostgreSQL.Concepts.General.SSL.Connecting "#PostgreSQL.Concepts.General.SSL.Connecting")
- [Requiring an SSL
  connection to a PostgreSQL DB instance](#PostgreSQL.Concepts.General.SSL.Requiring "#PostgreSQL.Concepts.General.SSL.Requiring")
- [Determining the SSL
  connection status](#PostgreSQL.Concepts.General.SSL.Status "#PostgreSQL.Concepts.General.SSL.Status")
- [SSL cipher suites in
  RDS for PostgreSQL](#PostgreSQL.Concepts.General.SSL.Ciphers "#PostgreSQL.Concepts.General.SSL.Ciphers")

## Connecting to a

PostgreSQL DB instance over SSL

###### To connect to a PostgreSQL DB instance over SSL

1. Download the certificate.

For information about downloading certificates, see [Using SSL/TLS to encrypt a connection to a DB
instance or cluster](UsingWithRDS.md "UsingWithRDS.md"). 2. Connect to your PostgreSQL DB instance over SSL.

When you connect using SSL, your client can choose whether to verify
the certificate chain. If your connection parameters specify
`sslmode=verify-ca` or `sslmode=verify-full`,
then your client requires the RDS CA certificates to be in their trust
store or referenced in the connection URL. This requirement is to verify
the certificate chain that signs your database certificate.

When a client, such as psql or JDBC, is configured with SSL support,
the client first tries to connect to the database with SSL by default.
If the client can't connect with SSL, it reverts to connecting
without SSL. The default `sslmode` mode used is different
between libpq-based clients (such as psql) and JDBC. The libpq-based and
JDBC clients default to `prefer`.

Use the `sslrootcert` parameter to reference the
certificate, for example
`sslrootcert=rds-ssl-ca-cert.pem`.

The following is an example of using `psql` to connect to a
PostgreSQL DB instance using SSL with certificate verification.

```
`$` `psql "host=`db-name.555555555555.ap-southeast-1.rds.amazonaws.com`
 port=5432 dbname=`testDB` user=`testuser` sslrootcert=`rds-ca-rsa2048-g1.pem` sslmode=verify-full"`
```

## Requiring an SSL

connection to a PostgreSQL DB instance

You can require that connections to your PostgreSQL DB instance use SSL by using the
`rds.force_ssl` parameter. The `rds.force_ssl`
parameter default value is 1 (on) for RDS for PostgreSQL version 15 and later. For
all other RDS for PostgreSQL major versions 14 and older, the default value of this
parameter is 0 (off). You can set the `rds.force_ssl` parameter to 1
(on) to require SSL/TLS for connections to your DB cluster. You can set the
`rds.force_ssl` parameter to 1 (on) to require SSL for
connections to your DB instance.

To change the value of this parameter, you need to create a custom DB
parameter group. You then change the value for `rds.force_ssl` in
your custom DB parameter group to `1` to turn on this feature. If you
prepare the custom DB parameter group before creating your RDS for PostgreSQL DB
instance you can choose it (instead of a default parameter group) during the
creation process. If you do this after your RDS for PostgreSQL DB instance is already
running, you need to reboot the instance so that your instance uses the custom
parameter group. For more information, see [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

When the `rds.force_ssl` feature is active on your DB instance,
connection attempts that aren't using SSL are rejected with the following
message:

```
`$` psql -h db-name.555555555555.ap-southeast-1.rds.amazonaws.com port=5432 dbname=testDB user=testuser
psql: error: FATAL: no pg_hba.conf entry for host "w.x.y.z", user "testuser", database "testDB", SSL off
```

## Determining the SSL

connection status

The encrypted status of your connection is shown in the logon banner when you
connect to the DB instance:

```
`Password for user master:
psql (10.3)
SSL connection (cipher: DHE-RSA-AES256-SHA, bits: 256)
Type "help" for help.`
`postgres=>`
```

You can also load the `sslinfo` extension and then call the
`ssl_is_used()` function to determine if SSL is being used. The
function returns `t` if the connection is using SSL, otherwise it
returns `f`.

```
`postgres=>` `CREATE EXTENSION sslinfo;`
`CREATE EXTENSION`
`postgres=>` `SELECT ssl_is_used();`
`ssl_is_used
---------
t
(1 row)`
```

For more detailed information, you can use the following query to get
information from `pg_settings`:

```
`SELECT name as "Parameter name", setting as value, short_desc FROM pg_settings WHERE name LIKE '%ssl%';`
 `Parameter name | value | short_desc
----------------------------------------+-----------------------------------------+-------------------------------------------------------
 ssl | on | Enables SSL connections.
 ssl_ca_file | /rdsdbdata/rds-metadata/ca-cert.pem | Location of the SSL certificate authority file.
 ssl_cert_file | /rdsdbdata/rds-metadata/server-cert.pem | Location of the SSL server certificate file.
 ssl_ciphers | HIGH:!aNULL:!3DES | Sets the list of allowed SSL ciphers.
 ssl_crl_file | | Location of the SSL certificate revocation list file.
 ssl_dh_params_file | | Location of the SSL DH parameters file.
 ssl_ecdh_curve | prime256v1 | Sets the curve to use for ECDH.
 ssl_key_file | /rdsdbdata/rds-metadata/server-key.pem | Location of the SSL server private key file.
 ssl_library | OpenSSL | Name of the SSL library.
 ssl_max_protocol_version | | Sets the maximum SSL/TLS protocol version to use.
 ssl_min_protocol_version | TLSv1.2 | Sets the minimum SSL/TLS protocol version to use.
 ssl_passphrase_command | | Command to obtain passphrases for SSL.
 ssl_passphrase_command_supports_reload | off | Also use ssl_passphrase_command during server reload.
 ssl_prefer_server_ciphers | on | Give priority to server ciphersuite order.
(14 rows)`

```

You can also collect all the information about your RDS for PostgreSQL DB
instance's SSL usage by process, client, and application by using the
following query:

````
`SELECT datname as "Database name", usename as "User name", ssl, client_addr, application_name, backend_type
 FROM pg_stat_ssl
 JOIN pg_stat_activity
 ON pg_stat_ssl.pid = pg_stat_activity.pid
 ORDER BY ssl;`
 `Database name | User name | ssl | client_addr | application_name | backend_type
---------------+-----------+-----+----------------+------------------------+------------------------------
| | f | | | autovacuum launcher
| rdsadmin | f | | | logical replication launcher
| | f | | | background writer
| | f | | | checkpointer
| | f | | | walwriter rdsadmin | rdsadmin | t | 127.0.0.1 | | client backend rdsadmin | rdsadmin | t | 127.0.0.1 | PostgreSQL JDBC Driver | client backend postgres | postgres | t | 204.246.162.36 | psql | client backend (8 rows)` ``` To identify the cipher used for your SSL connection, you can query as follows: ``` `postgres=>` `SELECT ssl_cipher();` `ssl_cipher -------------------- DHE-RSA-AES256-SHA (1 row)` ``` To learn more about the `sslmode` option, see [Database connection control functions](https://www.postgresql.org/docs/11/libpq-connect.html#LIBPQ-CONNECT-SSLMODE "https://www.postgresql.org/docs/11/libpq-connect.html#LIBPQ-CONNECT-SSLMODE") in the *PostgreSQL documentation*. ## SSL cipher suites in RDS for PostgreSQL The PostgreSQL configuration parameter [ssl\_ciphers](https://www.postgresql.org/docs/current/runtime-config-connection.html#RUNTIME-CONFIG-CONNECTION-SSL "https://www.postgresql.org/docs/current/runtime-config-connection.html#RUNTIME-CONFIG-CONNECTION-SSL") specifies the categories of cipher suites that are allowed for SSL connections to the database when using TLS 1.2 and lower. In RDS for PostgreSQL 16 and later, you can modify the `ssl_ciphers` parameter to use specific values from the allowlisted cipher suites. This is a dynamic parameter that doesn't require a database instance reboot. To view the allowlisted cipher suites, use either the Amazon RDS console or the following AWS CLI command: ``` aws rds describe-db-parameters --db-parameter-group-name `<your-parameter-group>` --region `<region>` --endpoint-url `<endpoint-url>` --output json | jq '.Parameters[] | select(.ParameterName == "ssl_ciphers")' ``` The following table lists both the default cipher suites and the allowed cipher suites for versions that support custom configurations.
| PostgreSQL engine version | Default ssl\_cipher suite values | Allowlisted custom ssl\_cipher suite values | | --- | --- | --- |
| 17 | `HIGH:!aNULL:!3DES` | `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384` `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256` `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256` `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384` `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256` | | 16 | `HIGH:!aNULL:!3DES` | `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384` `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256` `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256` `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384` `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256` |
| 15 | `HIGH:!aNULL:!3DES` | Custom ssl\_ciphers isn't supported | | 14 | `HIGH:!aNULL:!3DES` | Custom ssl\_ciphers isn't supported |
| 13 | `HIGH:!aNULL:!3DES` | Custom ssl\_ciphers isn't supported | | 12 | `HIGH:!aNULL:!3DES` | Custom ssl\_ciphers isn't supported |
| 11.4 and higher minor versions | `HIGH:MEDIUM:+3DES:!aNULL:!RC4` | Custom ssl\_ciphers isn't supported | | 11.1, 11.2 | `HIGH:MEDIUM:+3DES:!aNULL` | Custom ssl\_ciphers isn't supported |
| 10.9 and higher minor versions | `HIGH:MEDIUM:+3DES:!aNULL:!RC4` | Custom ssl\_ciphers isn't supported | | 10.7 and lower minor versions | `HIGH:MEDIUM:+3DES:!aNULL` | Custom ssl\_ciphers isn't supported | To configure all instance connections to use the `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384` cipher suite, modify your parameter group as shown in the following example: ``` aws rds modify-db-parameter-group --db-parameter-group-name `<your-parameter-group>` --parameters "ParameterName='ssl_ciphers',ParameterValue='TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384',ApplyMethod=immediate" ``` This example uses an ECDSA cipher, which requires your instance to use a certificate authority with elliptic curve cryptography (ECC) to establish a connection. For information about certificate authorities provided by Amazon RDS, see [Certificate authorities](singWithRDS.md#UsingWithRDS.SSL.RegionCertificateAuthorities "singWithRDS.md#UsingWithRDS.SSL.RegionCertificateAuthorities"). You can verify the ciphers in use through the methods described in [Determining the SSL connection status](PostgreSQL.Concepts.General.md#PostgreSQL.Concepts.General.SSL.Status "PostgreSQL.Concepts.General.md#PostgreSQL.Concepts.General.SSL.Status"). Ciphers may have different names depending on the context: <br>• The allowlisted ciphers that you can configure in your parameter group are referred to with their IANA names. <br>• The `sslinfo` and `psql` logon banner refer to ciphers using their OpenSSL names. By default, the value of `ssl_max_protocol_version` in RDS for PostgreSQL 16 and later is TLS v1.3. You must set the value of this parameter to TLS v1.2 as TLS v1.3 doesn't use the cipher configurations specified in the `ssl_ciphers` parameter. When you set the value as TLS v1.2, connections use only the ciphers that you define in `ssl_ciphers`. ``` aws rds modify-db-parameter-group --db-parameter-group-name `<your-parameter-group>` --parameters "ParameterName='ssl_max_protocol_version',ParameterValue='TLSv1.2',ApplyMethod=immediate" ``` To ensure database connections use SSL, set the `rds.force_ssl parameter` to 1 in your parameter group. For more information about parameters and parameter groups, see [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").
````
