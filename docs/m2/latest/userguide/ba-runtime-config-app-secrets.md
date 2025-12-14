AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# AWS Blu Age Runtime secrets

Some of the resource configurations that contain credentials can be further secured by using
AWS secrets. The idea is to store critical data in an AWS secret and have a reference to the
secret in the YAML configuration so the secret content is picked up on the fly at Apache Tomcat
startup.

## Secrets for Aurora

Aurora database configuration (for JICS, Blusam, customer db, and so on) will use the
built-in [database secret](../../../secretsmanager/latest/userguide/create_database_secret.md "../../../secretsmanager/latest/userguide/create_database_secret.md"),
which will populate all the relevant fields automatically from the corresponding
database.

###### Note

The `dbname` key is optional, depending on your database configuration, it
will get into the secret or not. You can add it there manually, or by supplying the name to
the YAML file.

## Other secrets

Other secrets are for resources that have a single password (notably password-protected
redis caches). In this case the [other type of secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") must
be used.

### YAML references to secrets

The `application-main.yml` can reference the secret ARN for various
resources:

### JICS database

JICS database credentials with `spring.aws.jics.db.secret`

```
spring:
   aws:
     jics:
       db:
         dbname: jics
         secret: arn:aws:secretsmanager:XXXX
```

Supported JICS database secret keys:

| Secret key            | Secret key description                                           |
| --------------------- | ---------------------------------------------------------------- |
| host                  | The host name                                                    |
| port                  | The port                                                         |
| dbname                | The name of the database                                         |
| username              | The username                                                     |
| password              | The password                                                     |
| engine                | Database engine: Postgres, Oracle, Db2, Microsoft SQL Server     |
| currentSchema         | Specific schema to use (Db2 support only)                        |
| sslConnection         | Whether to use SSL connection (Db2 support only)                 |
| sslTrustStoreLocation | The location of the truststore on the client (Db2 support only)  |
| sslTrustStorePassword | The password for the truststore on the client (Db2 support only) |

###### Note

The name of the database is either supplied in the secret or in the yaml reference
`spring.aws.jics.db.dbname`.

### Blusam database

Blusam database credentials with `spring.aws.client.bluesam.db.secret`

```
spring:
   aws:
     client:
       bluesam:
         db:
           dbname: bluesam
           secret: arn:aws:secretsmanager:XXXX
```

Supported Blusam database secret keys:

| Secret key | Secret key description    |
| ---------- | ------------------------- |
| host       | The host name             |
| port       | The port                  |
| dbname     | The name of the database  |
| username   | The username              |
| password   | The password              |
| engine     | Database engine: Postgres |

###### Note

The name of the database is either supplied in the secret or in the yaml reference
`spring.aws.client.bluesam.db.dbname`.

### Client database

The client `application-profile.yml` can reference the secret ARN for the
client database. This requires an additional property to list the datasource names
`spring.aws.client.datasources.names`. For each datasource name
`ds_name` specify the secret ARN in the following property:
`spring.aws.client.datasources.ds_name.secret`. Example:

```
spring:
   aws:
     client:
       datasources:
         names: primary,host
         primary:
           secret: arn:aws:secretsmanager:XXXX
         host:
           dbname: hostdb
           secret: arn:aws:secretsmanager:XXXX
```

_names: primary,host_:

An example with two client datasources named primary and host, each with their database
and credentials.

_dbname: hostdb_:

In this example, the name of the "host" database is not in the secret and is supplied
here instead, while for the "primary" database it is in the secret.

Supported client database secret keys:

| Secret key            | Secret key description                                           |
| --------------------- | ---------------------------------------------------------------- |
| host                  | The host name                                                    |
| port                  | The port                                                         |
| dbname                | The name of the database                                         |
| username              | The username                                                     |
| password              | The password                                                     |
| engine                | Database engine: Postgres, Oracle, Db2, Microsoft SQL Server     |
| currentSchema         | Specific schema to use (Db2 support only)                        |
| sslConnection         | Whether to use SSL connection (Db2 support only)                 |
| sslTrustStoreLocation | The location of the truststore on the client (Db2 support only)  |
| sslTrustStorePassword | The password for the truststore on the client (Db2 support only) |

### PGM utility database

The `application-utility-pgm.yml` can reference the secret ARN for various
resources.

- `spring.aws.client.datasources.primary`
  - `secret`

  Secret ARN for the application database.

Type: string

- `type`

Fully qualified name of the connection pool implementation to use.

Type: string

Default: `com.zaxxer.hikari.HikariDataSource`

- `spring.aws.client.utility.pgm.datasources`
  - `names`

List of data source names.

Type: string

- `dsname`
  - `dbname`

Name of the host.

Type: string

- `secret`

Secret ARN of the host database.

Type: string

- `type`

Fully qualified name of the connection pool implementation to use.

Type: string

Default: `com.zaxxer.hikari.HikariDataSource`

For a multi-datasources secret:

```
spring:
   aws:
     client:
       primary:
         secret: arn:aws:secretsmanager:XXXX
         type: dataSourceType
       utility:
         pgm:
           datasources:
             names: dsname1,dsname2,dsname3
               dsname1:
                 dbname: dbname1
                 secret: arn:aws:secretsmanager:XXXX
                 type: dataSourceType
               dsname2:
                 dbname: dbname2
                 secret: arn:aws:secretsmanager:XXXX
                 type: dataSourceType
               dsname3:
                 dbname: dbname3
                 secret: arn:aws:secretsmanager:XXXX
                 type: dataSourceType
```

### No XA supported secret keys

- engine (postgres/oracle/db2/mssql)
- port
- dbname
- currentSchema
- username
- password
- url
- sslConnection
- sslTrustStoreLocation
- sslTrustStorePassword

For `postgres` only the `sslMode` secret key value
(`disable/allow/prefer/require/verify-ca/verify-full`) and the
`spring.aws.rds.ssl.cert-path` YAML property make it possible to connect with
SSL.

### XA supported secret keys

If the client database is using XA, the sub xa-properties are supported through secret
values.

- host
- port
- dbname
- currentSchema
- username
- password
- url
- sslConnection (true/false)
- sslTrustStoreLocation
- sslTrustStorePassword

However, for other xa-properties ( for example `maxPoolSize` or
`driverType`), the regular YAML key
`spring.jta.atomikos.datasource.XXXX.unique-resource-name` must still be
supplied.

The secret value overrides the YAML properties.

### Default Super Admin BAC and JAC

You can also configure application-main.yml to retrieve the username and the password of
the default super admin user in the secret from AWS Secrets Manager by specifying the ARN.
The following example shows how to declare this secret in a YAML file.

```
spring:
   aws:
     client:
       defaultSuperAdmin:
         secret: arn:aws:secretsmanager:XXXX
```

Supported default super admin database secret keys:

| Secret key | Secret key description |
| ---------- | ---------------------- |
| username   | The username.          |
| password   | The password.          |

### OAuth2

You can also configure `application-main.yml` to retrieve the OAuth2 client secret from
AWS Secrets Manager by specifying the provider and ARN. The default value for the provider property is
Amazon Cognito. The following is an example configuration for the OAuth2 provider
Keycloak:

```
spring:
   aws:
     client:
       provider: keycloak
       keycloak:
         secret: arn:aws:secretsmanager:XXXX
```

In this example, the client-secret for the OAuth2 provider Keycloak is retrieved from
the specified ARN in AWS Secrets Manager. This configuration supports multiple providers by
dynamically resolving the provider name and corresponding secret ARN.

Supported OAuth2 secret keys:

| Secret key    | Secret key description                                                                              |
| ------------- | --------------------------------------------------------------------------------------------------- |
| client-secret | The secret generated by the authorization server during the process of<br>application registration. |

### Secret manager for Redis

caches

The `application-main.yml` file can reference the secret ARN for
Redis caches. The supported one are:

- Gapwalk Redis credentials with
  `spring.aws.client.gapwalk.redis.secret`
- Bluesam Redis credentials with
  `spring.aws.client.bluesam.redis.secret`
- Bluesam locks Redis credentials with
  `spring.aws.client.bluesam.locks.redis.secret`
- Dataset catalog Redis credentials with
  `spring.aws.client.dataset.catalog.redis.secret`
- JICS Redis credentials with
  `spring.aws.client.jics.redis.secret`
- Session Redis credentials with
  `spring.aws.client.jics.redis.secret`
- Session tracker Redis credentials with
  `spring.aws.client.session.tracker.redis.secret`
- JICS TS Queues Redis credentials with
  `spring.aws.client.jics.queues.ts.redis.secret`
- JCL checkpoint Redis credentials with
  `spring.aws.client.jcl.checkpoint.redis.secret`
- Gapwalk files locks Redis credentials with
  `spring.aws.client.gapwalk.files.locks.redis.secret`
- Blu4IV locks Redis credentials with
  `spring.aws.client.blu4iv.locks.redis.secret`

The following example shows how to declare these secrets in a YAML file.

```
spring:
   aws:
     client:
       gapwalk:
         redis:
           secret: arn:aws:secretsmanager:XXXX
       bluesam:
         locks:
           redis:
             secret: arn:aws:secretsmanager:XXXX
         redis:
           secret: arn:aws:secretsmanager:XXXX
       dataset:
         catalog:
           redis:
             secret: arn:aws:secretsmanager:XXXX
       jics:
         redis:
           secret: arn:aws:secretsmanager:XXXX
       session:
         tracker:
           redis:
             secret: arn:aws:secretsmanager:XXXX
       jics:
         queues:
           ts:
             redis:
               secret: arn:aws:secretsmanager:XXXX
       jcl:
         checkpoint:
           redis:
             secret: arn:aws:secretsmanager:XXXX
       gapwalk:
         files:
           locks:
             redis:
               secret: arn:aws:secretsmanager:XXXX
       blu4iv:
         locks:
           redis:
             secret: arn:aws:secretsmanager:XXXX
```

Supported Redis secret keys:

| Secret key | Secret key description     |
| ---------- | -------------------------- |
| hostname   | The Redis server hostname. |
| port       | The Redis server port.     |
| username   | The username.              |
| password   | The password.              |

### Secret manager for SSL password

settings

The `application-main.yml` file can reference the secret ARN for SSL
password settings. The following is supported.

- Gapwalk SSL credentials with `spring.aws.client.ssl.secret`

The following example shows how to declare these secrets in a YAML file.

```
spring:
   aws:
     client:
       ssl:
         secret: arn:aws:secretsmanager:XXXX
```

| Secret key         | Secret key description   |
| ------------------ | ------------------------ |
| trustStorePassword | The truststore password. |
| keyStorePassword   | The keystore password.   |

### Secret manager for IBM MQ password

settings

The `application-main.yml` file can reference the secret ARN for IBM MQ
settings. The following is supported.

- IBM MQ connections are defined as a list, and so are the credentials:

`mq.queues.jmsMQQueueManagers[N].secret:`

N starts at 0 for the first connection.

The following example shows how to declare these secrets in a YAML file.

```
mq.queues.jmsMQQueueManagers[0].secret: `Secret-0-ARN`
mq.queues.jmsMQQueueManagers[1].secret: `Secret-1-ARN`
```

For information about secret ARNs, see [What's in a Secrets Manager secret?](../../../secretsmanager/latest/userguide/whats-in-a-secret.md "../../../secretsmanager/latest/userguide/whats-in-a-secret.md")

Properties defined in the secret will override their corresponding values in the
`jmsMQ` YAML configuration.

If `queueManager` is set in the secret, it will override
the `mq.queues.jmsMQQueueManagers[N].jmsMQQueueManager` value
in the YAML file.

| Secret key   | Secret key description         |
| ------------ | ------------------------------ |
| queueManager | The IBM MQ queue manager name. |
| appName      | The IBM MQ application name.   |
| channel      | The IBM MQ channel name.       |
| host         | The IBM MQ hostname.           |
| port         | The IBM MQ port.               |
| userId       | The IBM MQ user name.          |
| password     | The IBM MQ user password.      |
| maxPoolSize  | The IBM MQ maximum pool size.  |
| sslCipherKey | The IBM MQ SSL cipher suite.   |

### JHDB database

The client `application-jhdb.yml` file can reference the secret ARNs for JHDB metadata databases.
Each database connection requires a unique name and corresponding secret ARN containing the connection credentials.
Database names are defined in a comma-separated list, with individual secret ARNs mapped to each database name.

```
spring:
   aws:
     jhdb:
       cnxs:
         datasources:
           names: DBD1,DBD2
           DBD1:
             secret: arn:aws:secretsmanager:XXXX
           DBD2:
             secret: arn:aws:secretsmanager:XXXX
```

Supported client database secret keys:

| Secret key    | Secret key description                                |
| ------------- | ----------------------------------------------------- |
| host          | The host name.                                        |
| port          | The port.                                             |
| dbname        | The name of the database.                             |
| username      | The username.                                         |
| password      | The password.                                         |
| engine        | Database engine: Postgres(now support Postgres only). |
| currentSchema | Specific schema to use.                               |
