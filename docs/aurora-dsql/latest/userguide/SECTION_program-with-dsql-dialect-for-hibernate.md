

# Aurora DSQL dialect for Hibernate
<a name="SECTION_program-with-dsql-dialect-for-hibernate"></a>

The Amazon Aurora DSQL dialect for Hibernate integrates Hibernate object-relational mapping (ORM) with Aurora DSQL. With the dialect, your Java applications can use the ORM capabilities of Hibernate while taking advantage of the distributed architecture and high availability of Aurora DSQL. For Java Database Connectivity (JDBC), the dialect uses the PostgreSQL JDBC Driver internally, and the Aurora DSQL JDBC Connector for IAM authentication. For more information, see the [Aurora DSQL Dialect for Hibernate](https://github.com/awslabs/aurora-dsql-orms/tree/main/java/hibernate) and the [Aurora DSQL JDBC Connector](https://github.com/awslabs/aurora-dsql-connectors/tree/main/java/jdbc) on the GitHub website, and the [PostgreSQL JDBC Driver website](https://jdbc.postgresql.org/).

The Aurora DSQL Dialect for Hibernate extends and overrides Hibernate's SQL generation to match Aurora DSQL's semantics, including asynchronous index creation, optimistic concurrency control (OCC), universally unique identifier (UUID) primary keys, and OCC-based foreign key enforcement. The dialect layers above the JDBC driver and generates correct SQL for Aurora DSQL.

## About the dialect
<a name="SECTION_program-with-dsql-dialect-for-hibernate-about-the-dialect"></a>

Amazon Aurora DSQL is a serverless, distributed relational database service optimized for transactional workloads. Aurora DSQL has specific requirements, including IAM-based authentication, asynchronous index creation, optimistic concurrency control, and OCC-based foreign key enforcement, where foreign key conflicts raise a serialization error that your application can retry.

With the Aurora DSQL Dialect for Hibernate, you can use the standard Hibernate APIs without manually accounting for the behavioral differences of Aurora DSQL. The dialect addresses these requirements by customizing the Hibernate SQL generation layer.

### What is Aurora DSQL authentication?
<a name="SECTION_program-with-dsql-dialect-for-hibernate-what-is-aurora-dsql-authentication"></a>

In Aurora DSQL, authentication involves:
+ **IAM authentication:** All connections use IAM-based authentication with time-limited tokens.
+ **Token generation:** The connector generates authentication tokens from your AWS credentials. Tokens have configurable lifetimes. Aurora DSQL enforces a maximum connection duration of 3,600 seconds (one hour) regardless of token lifetime; recycle connections before they reach this limit.

The Aurora DSQL JDBC Connector generates tokens automatically, so you can authenticate to Aurora DSQL with the Hibernate dialect without changing your existing Hibernate workflows.

### Features
<a name="SECTION_program-with-dsql-dialect-for-hibernate-features"></a>

The dialect provides the following features:
+ **Aurora DSQL-compatible SQL generation** – Generates SQL that conforms to Aurora DSQL semantics.
+ **Async index creation** – Creates all indexes with `CREATE INDEX ASYNC` and `CREATE UNIQUE INDEX ASYNC`.
+ **Foreign key support** – DDL export includes `FOREIGN KEY` constraints with OCC-based enforcement. Foreign key (FK) conflicts raise a serialization error that your application can retry. For the foreign key options that Aurora DSQL supports, see [Working with foreign key constraints in Aurora DSQL](working-with-foreign-key-constraints.md).
+ **Optimistic concurrency control** – Supports the `NONE` (OCC) and `PESSIMISTIC_WRITE` lock modes.
+ **UUID primary keys** – Registers a UUID JDBC type for correct binding. Use `@ColumnDefault("gen_random_uuid()")` to give the ID column a server-side default.
+ **Sequence and identity support** – Generates correct DDL with the mandatory `CACHE 65536` parameter.
+ **Connection pooling** – Works with HikariCP. To keep connections in the pool after errors that don't affect the connection, add your own `DsqlExceptionOverride` class, as shown in [Keeping healthy connections with `DsqlExceptionOverride`](#SECTION_program-with-dsql-dialect-for-hibernate-handling-retryable-errors-with-dsqlexceptionoverride).

## Quick start guide
<a name="SECTION_program-with-dsql-dialect-for-hibernate-quick-start-guide"></a>

### Requirements
<a name="SECTION_program-with-dsql-dialect-for-hibernate-requirements"></a>

Before you use the dialect, make sure that you have the following:
+ Java 17 or higher
+ Hibernate ORM version 7.2 or higher (Spring Boot 4.x for Spring Boot projects)
+ [Access to an Amazon Aurora DSQL cluster](getting-started.md)
+ Set up appropriate IAM permissions to allow your application to connect to Aurora DSQL.
+ AWS credentials configured (via AWS CLI, environment variables, or IAM roles)
+ PostgreSQL JDBC driver version 42.x or higher

### Installation
<a name="SECTION_program-with-dsql-dialect-for-hibernate-installation"></a>

Add the `aurora-dsql-hibernate-dialect` dependency to your project.

#### Maven
<a name="SECTION_program-with-dsql-dialect-for-hibernate-maven"></a>

Add the following dependency to your `pom.xml` file:

```
<dependency>
    <groupId>software.amazon.dsql</groupId>
    <artifactId>aurora-dsql-hibernate-dialect</artifactId>
    <version>2.2.0</version>
</dependency>
```

#### Gradle
<a name="SECTION_program-with-dsql-dialect-for-hibernate-gradle"></a>

Add the following dependency to your `build.gradle` file:

```
implementation("software.amazon.dsql:aurora-dsql-hibernate-dialect:2.2.0")
```

#### Install the Aurora DSQL JDBC Connector separately
<a name="SECTION_program-with-dsql-dialect-for-hibernate-install-the-aurora-dsql-jdbc-connector-separately"></a>

Add the JDBC connector for IAM authentication as a separate dependency:

**Maven**

```
<dependency>
    <groupId>software.amazon.dsql</groupId>
    <artifactId>aurora-dsql-jdbc-connector</artifactId>
    <version>1.5.0</version>
</dependency>
```

**Gradle**

```
implementation("software.amazon.dsql:aurora-dsql-jdbc-connector:1.5.0")
```

**Note**  
The Aurora DSQL JDBC Connector handles IAM token generation automatically. AWS recommends it for connecting to Aurora DSQL from Java applications, including those using Hibernate.

### Configuring the dialect
<a name="SECTION_program-with-dsql-dialect-for-hibernate-configuring-the-dialect"></a>

Explicitly specify `AuroraDSQLDialect`. Otherwise, Hibernate selects `PostgreSQLDialect` from the database metadata. You can configure the dialect in several ways:

#### `hibernate.properties`
<a name="SECTION_program-with-dsql-dialect-for-hibernate-hibernate-properties"></a>

Add the following line to your `hibernate.properties` file:

```
hibernate.dialect=software.amazon.dsql.hibernate.dialect.AuroraDSQLDialect
```

#### `persistence.xml`
<a name="SECTION_program-with-dsql-dialect-for-hibernate-persistence-xml"></a>

Add the following property to your `persistence.xml` file:

```
<property name="hibernate.dialect" value="software.amazon.dsql.hibernate.dialect.AuroraDSQLDialect"/>
```

#### Spring Boot `application.properties`
<a name="SECTION_program-with-dsql-dialect-for-hibernate-spring-boot-application-properties"></a>

Add the following line to your `application.properties` file:

```
spring.jpa.properties.hibernate.dialect=software.amazon.dsql.hibernate.dialect.AuroraDSQLDialect
```

#### Programmatic configuration
<a name="SECTION_program-with-dsql-dialect-for-hibernate-programmatic-configuration"></a>

Set the dialect when you build the service registry:

```
ServiceRegistry registry = new StandardServiceRegistryBuilder()
    .applySetting("hibernate.dialect", "software.amazon.dsql.hibernate.dialect.AuroraDSQLDialect")
    .build();
```

### Database connection
<a name="SECTION_program-with-dsql-dialect-for-hibernate-database-connection"></a>

Configure your database connection for Aurora DSQL with the Aurora DSQL JDBC Connector and Secure Sockets Layer (SSL) enabled.

**Note**  
The Aurora DSQL JDBC Connector turns on `sslmode=verify-full` and direct SSL negotiation (pgJDBC 42.7.4 or later) by default, so the connection uniform resource locator (URL) needs no SSL parameters.

The following properties configure the database connection. In this example, replace {{cluster-id}} and {{region}} with the values for your cluster.

```
hibernate.connection.url=jdbc:aws-dsql:postgresql://{{cluster-id}}.dsql.{{region}}.on.aws/postgres
hibernate.connection.username=admin
hibernate.connection.driver_class=software.amazon.dsql.jdbc.DSQLConnector
```

### Basic usage
<a name="SECTION_program-with-dsql-dialect-for-hibernate-basic-usage"></a>

The following example creates a Hibernate `SessionFactory` connected to Aurora DSQL and performs a basic read operation.

```
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;

Configuration config = new Configuration()
    .setProperty("hibernate.dialect", "software.amazon.dsql.hibernate.dialect.AuroraDSQLDialect")
    .setProperty("hibernate.connection.url",
        "jdbc:aws-dsql:postgresql://{{cluster-id}}.dsql.{{region}}.on.aws/postgres")
    .setProperty("hibernate.connection.username", "admin")
    .setProperty("hibernate.connection.driver_class", "software.amazon.dsql.jdbc.DSQLConnector")
    .addAnnotatedClass(MyEntity.class);

SessionFactory sessionFactory = config.buildSessionFactory();

try (Session session = sessionFactory.openSession()) {
    Transaction tx = session.beginTransaction();
    try {
        MyEntity result = session.get(MyEntity.class, entityId);
        tx.commit();
    } catch (RuntimeException e) {
        tx.rollback();  // roll back so the session can be reused or closed cleanly
        throw e;
    }
}
```

### Configuration options
<a name="SECTION_program-with-dsql-dialect-for-hibernate-configuration-options"></a>


| Option | Type | Required | Description | 
| --- | --- | --- | --- | 
| hibernate.dialect | string | Yes | Must be software.amazon.dsql.hibernate.dialect.AuroraDSQLDialect | 
| hibernate.connection.url | string | Yes | JDBC URL for the Aurora DSQL cluster endpoint | 
| hibernate.connection.username | string | Yes | Aurora DSQL username | 
| hibernate.connection.driver\_class | string | Yes | Must be software.amazon.dsql.jdbc.DSQLConnector | 
| hibernate.dialect.aurora\_dsql.sequence\_cache\_size | int | No | Cache size for sequences and identity columns. Default: 65536 | 

The dialect also supports all standard Hibernate connection and Jakarta Persistence API (JPA) configuration options.

### Using the Aurora DSQL dialect for Hibernate with connection pooling
<a name="SECTION_program-with-dsql-dialect-for-hibernate-using-the-aurora-dsql-dialect-for-hibernate-with-connection-pooling"></a>

The dialect works with any JDBC connection pool. The recommended pool for production use is [HikariCP](https://github.com/brettwooldridge/HikariCP), which is the default pool in Spring Boot.

Configure HikariCP with the `DsqlExceptionOverride` class so that the pool keeps healthy connections after Aurora DSQL rejects an unsupported statement, instead of evicting them.

```
import com.zaxxer.hikari.HikariDataSource;
import org.springframework.boot.jdbc.autoconfigure.DataSourceProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;
import org.springframework.boot.context.properties.ConfigurationProperties;

@Configuration(proxyBeanMethods = false)
public class DsqlDataSourceConfig {

    @Bean
    @Primary
    public HikariDataSource dataSource(DataSourceProperties properties) {
        HikariDataSource hds = properties.initializeDataSourceBuilder()
            .type(HikariDataSource.class)
            .build();
        hds.setMaxLifetime(3300000); // 55 minutes
        hds.setExceptionOverrideClassName(DsqlExceptionOverride.class.getName());
        return hds;
    }
}
```

**Connection `maxLifetime` configuration**  
Set the `maxLifetime` parameter to less than 3,600,000 milliseconds (one hour), which is the maximum connection duration that Aurora DSQL allows. Setting a lower `maxLifetime` allows the connection pool to proactively recycle connections, which is more efficient than handling connection timeout errors from the database.

#### Keeping healthy connections with `DsqlExceptionOverride`
<a name="SECTION_program-with-dsql-dialect-for-hibernate-handling-retryable-errors-with-dsqlexceptionoverride"></a>

Some Aurora DSQL errors leave the connection healthy, such as OCC conflicts (SQLSTATE `40001`) and unsupported statements (SQLSTATE `0Axxx`). By default, HikariCP evicts connections on `0A000`. Implement `SQLExceptionOverride` and register it with HikariCP so that the pool keeps these connections:

```
import com.zaxxer.hikari.SQLExceptionOverride;
import java.sql.SQLException;

public class DsqlExceptionOverride implements SQLExceptionOverride {

    @java.lang.Override
    public Override adjudicate(SQLException sqlException) {
        String sqlState = sqlException.getSQLState();
        if (sqlState == null) return Override.CONTINUE_EVICT;
        // SQLSTATE 40001 = OCC conflict (OC000/OC001) — application retries the transaction; connection is healthy
        // SQLSTATE 0Axxx = feature_not_supported — Aurora DSQL rejected an unsupported statement (for example, SAVEPOINT),
        //   but the connection itself is healthy; evicting it would force an unnecessary reconnect
        if (sqlState.equals("40001") || sqlState.matches("0A\\d{3}")) {
            return Override.DO_NOT_EVICT;
        }
        return Override.CONTINUE_EVICT;
    }
}
```

## Best practices
<a name="SECTION_program-with-dsql-dialect-for-hibernate-best-practices"></a>

### Primary key generation
<a name="SECTION_program-with-dsql-dialect-for-hibernate-primary-key-generation"></a>

UUID primary keys are the recommended choice in Aurora DSQL because they avoid sequence contention in a distributed environment. With `@GeneratedValue`, Hibernate generates the UUID in the application before the insert. The `@ColumnDefault` annotation adds a `gen_random_uuid()` column default for rows that you insert outside Hibernate. The following Java code example adds a UUID primary key to a base entity class:

```
import jakarta.persistence.*;
import java.util.UUID;
import org.hibernate.annotations.ColumnDefault;

@MappedSuperclass
public class BaseEntity {

    @Id
    @GeneratedValue
    @ColumnDefault("gen_random_uuid()")
    @Column(name = "id", updatable = false, nullable = false)
    private UUID id;
}
```

The dialect also supports sequence and identity-based integer primary keys. The dialect uses a default `CACHE` parameter of `65536` in sequence and identity column definitions. You can override this with the configuration property `hibernate.dialect.aurora_dsql.sequence_cache_size`.

```
@Entity
public class OrderEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE)
    @SequenceGenerator(name = "order_seq", sequenceName = "order_seq",
                       initialValue = 1000, allocationSize = 100)
    private Integer id;
}
```

### Auto-DDL
<a name="SECTION_program-with-dsql-dialect-for-hibernate-auto-ddl"></a>

For production, use explicit DDL scripts instead of automatic schema generation (`hbm2ddl.auto=create` or `update`) to maintain full control over table definitions, index creation, and schema migrations.

### Concurrency control and locking
<a name="SECTION_program-with-dsql-dialect-for-hibernate-concurrency-control-and-locking"></a>

Aurora DSQL uses optimistic concurrency control (OCC). Use only two Hibernate lock modes:
+ **`LockModeType.NONE`** – Uses OCC instead of an explicit database lock. Aurora DSQL checks only the rows that the transaction writes. If a concurrent transaction modifies one of those rows, the transaction that commits second fails with an OCC error (`OC000`, SQLSTATE `40001`).
+ **`LockModeType.PESSIMISTIC_WRITE`** – Adds `SELECT ... FOR UPDATE`, which adds the selected rows to the commit-time conflict check instead of locking them. If another transaction changes those rows, the transaction that commits second fails with SQLSTATE `40001`.

Use only `NONE` and `PESSIMISTIC_WRITE`, the two lock modes that the dialect overrides for Aurora DSQL compatibility. Hibernate core handles other lock modes and can generate clauses such as `SELECT ... FOR SHARE` and `SKIP LOCKED`. For the locking clauses that Aurora DSQL supports, see [`SELECT` command](working-with-postgresql-compatibility-supported-sql-features.md#dsql-select).

#### Handling OCC errors with transaction retry
<a name="SECTION_program-with-dsql-dialect-for-hibernate-handling-occ-errors-with-transaction-retry"></a>

Because OCC errors are retryable, you can retry the transaction. The following Java code example implements a retry aspect around your transactional methods:

```
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.core.Ordered;
import org.springframework.core.annotation.Order;
import org.springframework.dao.CannotAcquireLockException;
import org.springframework.orm.ObjectOptimisticLockingFailureException;
import org.springframework.stereotype.Component;
import org.springframework.transaction.annotation.Propagation;
import org.springframework.transaction.annotation.Transactional;

import java.util.concurrent.ThreadLocalRandom;

@Aspect
@Component
@Order(Ordered.HIGHEST_PRECEDENCE) // run outside the transaction so commit-time OCC errors are retried
public class TransactionRetryAspect {

    private static final int MAX_RETRIES = 3;

    @Around("@annotation(org.springframework.transaction.annotation.Transactional)")
    public Object retryOnOccConflict(ProceedingJoinPoint joinPoint) throws Throwable {
        int attempt = 0;
        while (true) {
            try {
                return joinPoint.proceed();
            } catch (ObjectOptimisticLockingFailureException | CannotAcquireLockException e) {
                if (++attempt >= MAX_RETRIES) throw e;
                Thread.sleep(ThreadLocalRandom.current().nextLong(100L << attempt)); // exponential backoff with jitter
            }
        }
    }
}
```

## Dialect features
<a name="SECTION_program-with-dsql-dialect-for-hibernate-dialect-features"></a>

The following table describes how the dialect handles keys and constraints.


| Feature | Behavior | 
| --- | --- | 
| Foreign keys | Supported — DDL export includes FOREIGN KEY constraints. Aurora DSQL supports NO ACTION, RESTRICT, CASCADE, SET NULL, SET DEFAULT, MATCH SIMPLE, MATCH FULL, and deferrable foreign keys, with SET CONSTRAINTS available for foreign keys only. Enforcement is OCC-based: FK conflicts raise a serialization error (OC000 / SQLSTATE 40001), which you can retry with TransactionRetryAspect. FK constraint violations (for example, referencing a non-existent row) throw DataIntegrityViolationException and aren't retryable. When you add constraints to existing tables with ALTER TABLE ... ADD CONSTRAINT ... NOT VALID, existing rows remain unvalidated. To validate them, run ALTER TABLE ASYNC ... VALIDATE CONSTRAINT, capture its returned job\_id, call sys.wait\_for\_job(job\_id), and check that the returned succeeded value is true. | 
| Check constraints | supportsColumnCheck() returns true in v2.1.0\+. The dialect emits CHECK constraints defined in entity annotations in DDL. | 
| Sequences | Correct DDL including mandatory CACHE parameter (default: 65536). | 
| Identity columns | Uses bigint generated by default as identity (START WITH 1 INCREMENT BY 1 CACHE <size>). | 
| UUID | Custom JDBC type registration ensures UUID columns bind correctly via the PostgreSQL JDBC driver. | 

The following table describes how the dialect handles SQL generation, locking, and data types.


| Feature | Behavior | 
| --- | --- | 
| Index creation | Uses CREATE INDEX ASYNC and CREATE UNIQUE INDEX ASYNC. | 
| Locking | Recommended modes: NONE (OCC) and PESSIMISTIC\_WRITE (SELECT ... FOR UPDATE). Hibernate core handles other modes. The dialect always generates FOR UPDATE, regardless of the lock timeout. | 
| Truncate | Uses DELETE FROM <table> in place of TRUNCATE. | 
| Temporary tables | supportsTemporaryTables() returns false; bulk mutations use the common table expression (CTE) strategies CteMutationStrategy and CteInsertStrategy, which create no physical tables. | 
| Data types | float (6 digits), double (15 digits), numeric (precision 18). varchar max length: 65,535. | 

## Authentication
<a name="SECTION_program-with-dsql-dialect-for-hibernate-authentication"></a>

The Aurora DSQL JDBC Connector automatically handles Aurora DSQL authentication by generating IAM tokens for each new connection. If you don't provide the AWS Region in the connection URL, the connector parses it from the cluster hostname.

For more information about authentication in Aurora DSQL, see [Authentication and authorization](authentication-authorization.md).

### Admin vs regular users
<a name="SECTION_program-with-dsql-dialect-for-hibernate-admin-vs-regular-users"></a>
+ Users named `"admin"` automatically use admin authentication tokens.
+ All other users use non-admin authentication tokens.
+ The JDBC connector generates tokens dynamically for each new connection.

## Examples
<a name="SECTION_program-with-dsql-dialect-for-hibernate-examples"></a>

For full example code, see the [Hibernate pet clinic example application](https://github.com/awslabs/aurora-dsql-orms/tree/main/java/hibernate/examples/pet-clinic-app) on the GitHub website. For instructions on how to run the example, see the [Hibernate pet clinic example README](https://github.com/awslabs/aurora-dsql-orms/blob/main/java/hibernate/examples/pet-clinic-app/README.md) on the GitHub website.

The following table lists the example files and what each one demonstrates.


| Description | Example | 
| --- | --- | 
| Connecting to Aurora DSQL with Hibernate and HikariCP | [DsqlDataSourceConfig.java](https://github.com/awslabs/aurora-dsql-orms/blob/main/java/hibernate/examples/pet-clinic-app/src/main/java/org/springframework/samples/petclinic/config/DsqlDataSourceConfig.java) | 
| Keeping healthy connections after Aurora DSQL errors in HikariCP | [DsqlExceptionOverride.java](https://github.com/awslabs/aurora-dsql-orms/blob/main/java/hibernate/examples/pet-clinic-app/src/main/java/org/springframework/samples/petclinic/config/DsqlExceptionOverride.java) | 
| Retrying transactions on OCC conflicts | [TransactionRetryAspect.java](https://github.com/awslabs/aurora-dsql-orms/blob/main/java/hibernate/examples/pet-clinic-app/src/main/java/org/springframework/samples/petclinic/config/TransactionRetryAspect.java) | 
| UUID primary key entity definition | [BaseEntity.java](https://github.com/awslabs/aurora-dsql-orms/blob/main/java/hibernate/examples/pet-clinic-app/src/main/java/org/springframework/samples/petclinic/model/BaseEntity.java) | 
| OneToMany relationship with OCC-based foreign key enforcement | [Owner.java](https://github.com/awslabs/aurora-dsql-orms/blob/main/java/hibernate/examples/pet-clinic-app/src/main/java/org/springframework/samples/petclinic/owner/Owner.java) | 
| ManyToMany relationship with OCC-based foreign key enforcement | [Vet.java](https://github.com/awslabs/aurora-dsql-orms/blob/main/java/hibernate/examples/pet-clinic-app/src/main/java/org/springframework/samples/petclinic/vet/Vet.java) | 