

# Aurora DSQL Connector for PHP `PDO_PGSQL`
<a name="SECTION_program-with-dsql-connector-for-php-pdo-pgsql"></a>

The [Aurora DSQL Connector for PHP](https://github.com/awslabs/aurora-dsql-connectors/tree/main/php/pdo_pgsql) is a PHP connector built on [`PDO_PGSQL`](https://www.php.net/manual/en/ref.pdo-pgsql.php) that integrates IAM authentication for connecting PHP applications to Amazon Aurora DSQL clusters.

The connector handles token generation, SSL configuration, and connection management so you can focus on your application logic.

## About the connector
<a name="SECTION_program-with-dsql-connector-for-php-pdo-pgsql-about"></a>

The Aurora DSQL Connector for PHP adds an authentication layer on top of `PDO_PGSQL` that handles IAM token generation, allowing you to connect to Aurora DSQL using your existing PDO workflows. Amazon Aurora DSQL requires IAM authentication with time-limited tokens, and the connector automatically manages token generation for you.

### What is Aurora DSQL authentication?
<a name="SECTION_program-with-dsql-connector-for-php-pdo-pgsql-authentication"></a>

In Aurora DSQL, **authentication** involves:
+ **IAM Authentication**: All connections use IAM-based authentication with time-limited tokens
+ **Token Generation**: The connector generates authentication tokens using AWS credentials, and these tokens have configurable lifetimes

The Aurora DSQL Connector for PHP understands these requirements and automatically generates IAM authentication tokens when establishing connections.

### Features
<a name="SECTION_program-with-dsql-connector-for-php-pdo-pgsql-features"></a>
+ **Automatic IAM authentication** - Handles Aurora DSQL token generation and refresh
+ **Built on `PDO_PGSQL`** - Wraps the standard PostgreSQL extension for PHP
+ **Seamless integration** - Works with existing PDO workflows
+ **SSL enforcement** - Always uses SSL with `verify-full` mode and direct TLS negotiation
+ **Region auto-detection** - Extracts AWS region from Aurora DSQL cluster hostname
+ **AWS credentials support** - Supports AWS profiles and custom credentials providers
+ **OCC retry** - Opt-in optimistic concurrency control retry with exponential backoff and jitter
+ **PSR-3 logging** - Compatible logging for retry diagnostics

## Example application
<a name="SECTION_program-with-dsql-connector-for-php-pdo-pgsql-example-application"></a>

For a complete example, see the [example application](https://github.com/awslabs/aurora-dsql-connectors/tree/main/php/pdo_pgsql/example) on GitHub.

## Quick start guide
<a name="SECTION_program-with-dsql-connector-for-php-pdo-pgsql-quick-start"></a>

### Requirements
<a name="SECTION_program-with-dsql-connector-for-php-pdo-pgsql-requirements"></a>
+ PHP 8.2 or later
+ `ext-pdo_pgsql` extension
+ [Access to an Aurora DSQL cluster](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/getting-started.html)
+ AWS credentials configured (via AWS CLI, environment variables, or IAM roles)

## Installation
<a name="SECTION_program-with-dsql-connector-for-php-pdo-pgsql-installation"></a>

Add the package to your project:

```
composer require awslabs/aurora-dsql-pdo-pgsql
```

## Usage
<a name="SECTION_program-with-dsql-connector-for-php-pdo-pgsql-usage"></a>

### Configuration-based connection
<a name="SECTION_program-with-dsql-connector-for-php-pdo-pgsql-config-connection"></a>

```
<?php

require_once 'vendor/autoload.php';

use Aws\AuroraDsql\PdoPgsql\AuroraDsql;
use Aws\AuroraDsql\PdoPgsql\DsqlConfig;

$config = new DsqlConfig(
    host: 'your-cluster.dsql.us-east-1.on.aws',
    occMaxRetries: 3
);
$pdo = AuroraDsql::connect($config);

// Read
$stmt = $pdo->query('SELECT 1 AS result');
$row = $stmt->fetch(PDO::FETCH_ASSOC);
echo "Connected: {$row['result']}\n";

// Transactional write with automatic OCC retry
$id = $pdo->transaction(function (PDO $conn): string {
    $stmt = $conn->prepare('INSERT INTO users (name) VALUES (?) RETURNING id');
    $stmt->execute(['Alice']);
    return $stmt->fetchColumn();
});
```

### Connection string format
<a name="SECTION_program-with-dsql-connector-for-php-pdo-pgsql-connection-string"></a>

For simple scripts or when you prefer connection string syntax, the connector supports `postgres://` and `postgresql://` connection strings with Aurora DSQL-specific query parameters:

```
$pdo = AuroraDsql::connectFromDsn(
    'postgres://admin@your-cluster.dsql.us-east-1.on.aws/postgres?region=us-east-1'
);
```

Supported query parameters: `region`, `profile`, `tokenDurationSecs`, `ormPrefix`.

### OCC retry
<a name="SECTION_program-with-dsql-connector-for-php-pdo-pgsql-occ-retry"></a>

Aurora DSQL uses optimistic concurrency control (OCC). When two transactions modify the same data, the first to commit wins and the second receives an OCC error.

OCC retry is opt-in. Set `occMaxRetries` in the config to enable automatic retry with exponential backoff and jitter:

```
$config = new DsqlConfig(
    host: 'your-cluster.dsql.us-east-1.on.aws',
    occMaxRetries: 3
);
$pdo = AuroraDsql::connect($config);

// Single statements are automatically retried via exec()
$pdo->exec("CREATE INDEX ASYNC ON users (email)");

// Multi-statement transactions are retried via transaction()
$pdo->transaction(function (PDO $conn) {
    $conn->exec("UPDATE accounts SET balance = balance - 100 WHERE id = 1");
    $conn->exec("UPDATE accounts SET balance = balance + 100 WHERE id = 2");
});
```

**Important**  
`transaction()` manages `beginTransaction()`/`commit()`/`rollBack()` internally. Your callback should contain only database operations and be safe to retry.

## Configuration options
<a name="SECTION_program-with-dsql-connector-for-php-pdo-pgsql-configuration"></a>

The connector also accepts `postgres://` and `postgresql://` connection strings with query parameters for configuration. Supported query parameters: `region`, `profile`, `tokenDurationSecs`, and `ormPrefix`.


| Field | Type | Default | Description | 
| --- | --- | --- | --- | 
| host | string | (required) | Cluster endpoint or 26-char cluster ID | 
| region | ?string | null (auto-detected) | AWS region; required if host is a cluster ID | 
| user | string | "admin" | Database user | 
| database | string | "postgres" | Database name | 
| port | int | 5432 | Database port | 
| profile | ?string | null | AWS profile name for credentials | 
| credentialsProvider | ?\\Closure | null | Custom AWS credentials provider | 
| tokenDurationSecs | int | 900 (15 min) | Token validity duration in seconds | 
| occMaxRetries | ?int | null (disabled) | Default max OCC retries for exec() and transaction() | 
| ormPrefix | ?string | null | ORM prefix prepended to application\_name | 
| logger | ?LoggerInterface | null | PSR-3 logger for retry warnings and diagnostics | 

## Authentication
<a name="SECTION_program-with-dsql-connector-for-php-pdo-pgsql-auth"></a>

The connector automatically handles Aurora DSQL authentication by generating tokens using AWS credentials. If you don't provide the AWS region, the connector parses it from the hostname.

For more information on authentication in Aurora DSQL, see [Authentication and authorization for Aurora DSQL](authentication-authorization.md).

### Admin vs regular users
<a name="SECTION_program-with-dsql-connector-for-php-pdo-pgsql-admin-vs-regular"></a>
+ Users named "admin" automatically use admin authentication tokens
+ All other users use regular authentication tokens
+ The connector generates tokens dynamically for each connection