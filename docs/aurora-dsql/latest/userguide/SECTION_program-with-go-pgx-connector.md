

# Aurora DSQL Connector for Go pgx
<a name="SECTION_program-with-go-pgx-connector"></a>

The [Aurora DSQL Connector for Go](https://github.com/awslabs/aurora-dsql-connectors/tree/main/go/pgx) wraps [pgx](https://github.com/jackc/pgx) with automatic IAM authentication. The connector handles token generation, SSL configuration, and connection management so you can focus on your application logic.

## About the connector
<a name="SECTION_program-with-go-pgx-connector-about"></a>

Aurora DSQL requires IAM-based authentication with time-limited tokens that existing Go PostgreSQL drivers do not natively support. The Aurora DSQL Connector for Go adds an authentication layer on top of the pgx driver that handles IAM token generation, allowing you to connect to Aurora DSQL without changing your existing pgx workflows.

### What is Aurora DSQL Authentication?
<a name="SECTION_program-with-go-pgx-connector-authentication"></a>

In Aurora DSQL, **authentication** involves:
+ **IAM Authentication**: All connections use IAM-based authentication with time-limited tokens
+ **Token Generation**: The connector generates authentication tokens using AWS credentials, and these tokens have configurable lifetimes

The Aurora DSQL Connector for Go is designed to understand these requirements and automatically generate IAM authentication tokens when establishing connections.

### Benefits of the Aurora DSQL Connector for Go
<a name="SECTION_program-with-go-pgx-connector-benefits"></a>

The Aurora DSQL Connector for Go allows you to continue using your existing pgx workflows while enabling IAM authentication through:
+ **Automatic Token Generation**: The connector generates IAM tokens automatically for each connection
+ **Connection Pooling**: Built-in support for `pgxpool` with automatic token generation per connection
+ **Flexible Configuration**: Support for full endpoints or cluster IDs with region auto-detection
+ **AWS Credentials Support**: Supports AWS profiles and custom credentials providers

## Key features
<a name="SECTION_program-with-go-pgx-connector-features"></a>

Automatic Token Management  
The connector generates IAM tokens automatically for each new connection using pre-resolved credentials.

Connection Pooling  
Connection pooling via `pgxpool` with automatic token generation per connection.

Flexible Host Configuration  
Supports both full cluster endpoints and cluster IDs with automatic region detection.

SSL Security  
SSL is always enabled with verify-full mode and direct TLS negotiation.

## Prerequisites
<a name="SECTION_program-with-go-pgx-connector-prerequisites"></a>
+ Go 1.24 or later
+ AWS credentials configured
+ An Aurora DSQL cluster

The connector uses the [AWS SDK for Go v2 default credential chain](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/configure-gosdk.html#specifying-credentials), which resolves credentials in the following order:

1. Environment variables (AWS\_ACCESS\_KEY\_ID, AWS\_SECRET\_ACCESS\_KEY)

1. Shared credentials file (\~/.aws/credentials)

1. Shared config file (\~/.aws/config)

1. IAM role for Amazon EC2/ECS/Lambda

## Installation
<a name="SECTION_program-with-go-pgx-connector-installation"></a>

Install the connector using Go modules:

```
go get github.com/awslabs/aurora-dsql-connectors/go/pgx/dsql
```

## Quick start
<a name="SECTION_program-with-go-pgx-connector-quick-start"></a>

The following example shows how to create a connection pool and execute a query:

```
package main

import (
    "context"
    "log"

    "github.com/awslabs/aurora-dsql-connectors/go/pgx/dsql"
)

func main() {
    ctx := context.Background()

    // Create a connection pool
    pool, err := dsql.NewPool(ctx, dsql.Config{
        Host: "your-cluster.dsql.us-east-1.on.aws",
    })
    if err != nil {
        log.Fatal(err)
    }
    defer pool.Close()

    // Execute a query
    var greeting string
    err = pool.QueryRow(ctx, "SELECT 'Hello, DSQL!'").Scan(&greeting)
    if err != nil {
        log.Fatal(err)
    }
    log.Println(greeting)
}
```

## Configuration options
<a name="SECTION_program-with-go-pgx-connector-configuration"></a>

The connector supports the following configuration options:


| Field | Type | Default | Description | 
| --- | --- | --- | --- | 
| Host | string | (required) | Cluster endpoint or cluster ID | 
| Region | string | (auto-detected) | AWS region; required if Host is a cluster ID | 
| User | string | "admin" | Database user | 
| Database | string | "postgres" | Database name | 
| Port | int | 5432 | Database port | 
| Profile | string | "" | AWS profile name for credentials | 
| TokenDurationSecs | int | 900 (15 min) | Token validity duration in seconds (max allowed: 1 week, default: 15 min) | 
| MaxConns | int32 | 0 | Maximum pool connections (0 = pgxpool default) | 
| MinConns | int32 | 0 | Minimum pool connections (0 = pgxpool default) | 
| MaxConnLifetime | time.Duration | 55 minutes | Maximum connection lifetime | 

## Connection string format
<a name="SECTION_program-with-go-pgx-connector-connection-string"></a>

The connector supports PostgreSQL and DSQL connection string formats:

```
postgres://[user@]host[:port]/[database][?param=value&...]
dsql://[user@]host[:port]/[database][?param=value&...]
```

Supported query parameters:
+ `region` - AWS region
+ `profile` - AWS profile name
+ `tokenDurationSecs` - Token validity duration in seconds

Examples:

```
// Full endpoint (region auto-detected)
pool, _ := dsql.NewPool(ctx, "postgres://admin@cluster.dsql.us-east-1.on.aws/postgres")

// Using dsql:// scheme (also supported)
pool, _ := dsql.NewPool(ctx, "dsql://admin@cluster.dsql.us-east-1.on.aws/postgres")

// With explicit region
pool, _ := dsql.NewPool(ctx, "postgres://admin@cluster.dsql.us-east-1.on.aws/mydb?region=us-east-1")

// With AWS profile
pool, _ := dsql.NewPool(ctx, "postgres://admin@cluster.dsql.us-east-1.on.aws/postgres?profile=dev")
```

## Advanced usage
<a name="SECTION_program-with-go-pgx-connector-advanced"></a>

### Host configuration
<a name="SECTION_program-with-go-pgx-connector-host-config"></a>

The connector supports two host formats:

**Full endpoint** (region auto-detected):

```
pool, _ := dsql.NewPool(ctx, dsql.Config{
    Host: "your-cluster.dsql.us-east-1.on.aws",
})
```

**Cluster ID** (region required):

```
pool, _ := dsql.NewPool(ctx, dsql.Config{
    Host:   "your-cluster-id",
    Region: "us-east-1",
})
```

### Pool configuration tuning
<a name="SECTION_program-with-go-pgx-connector-pool-tuning"></a>

Configure the connection pool for your workload:

```
pool, err := dsql.NewPool(ctx, dsql.Config{
    Host:              "your-cluster.dsql.us-east-1.on.aws",
    MaxConns:          20,
    MinConns:          5,
    MaxConnLifetime:   time.Hour,
    MaxConnIdleTime:   30 * time.Minute,
    HealthCheckPeriod: time.Minute,
})
```

### Single connection usage
<a name="SECTION_program-with-go-pgx-connector-single-connection"></a>

For simple scripts or when connection pooling is not needed:

```
conn, err := dsql.Connect(ctx, dsql.Config{
    Host: "your-cluster.dsql.us-east-1.on.aws",
})
if err != nil {
    log.Fatal(err)
}
defer conn.Close(ctx)

// Use the connection
rows, err := conn.Query(ctx, "SELECT * FROM users")
```

### Using AWS profiles
<a name="SECTION_program-with-go-pgx-connector-aws-profiles"></a>

Specify an AWS profile for credentials:

```
pool, err := dsql.NewPool(ctx, dsql.Config{
    Host:    "your-cluster.dsql.us-east-1.on.aws",
    Profile: "production",
})
```

## OCC retry
<a name="SECTION_program-with-go-pgx-connector-occ-retry"></a>

Aurora DSQL uses optimistic concurrency control (OCC). When two transactions modify the same data, the first to commit wins and the second receives an OCC error.

The `occretry` package provides helpers for automatic retry with exponential backoff and jitter. Install it with:

```
go get github.com/awslabs/aurora-dsql-connectors/go/pgx/occretry
```

Use `WithRetry` for transactional writes:

```
err := occretry.WithRetry(ctx, pool, occretry.DefaultConfig(), func(tx pgx.Tx) error {
    _, err := tx.Exec(ctx, "UPDATE accounts SET balance = balance - $1 WHERE id = $2", 100, fromID)
    if err != nil {
        return err
    }
    _, err = tx.Exec(ctx, "UPDATE accounts SET balance = balance + $1 WHERE id = $2", 100, toID)
    return err
})
```

For DDL or single statements, use `ExecWithRetry`:

```
err := occretry.ExecWithRetry(ctx, pool, occretry.DefaultConfig(),
    "CREATE TABLE IF NOT EXISTS users (id UUID PRIMARY KEY, name TEXT)")
```

**Important**  
`WithRetry` manages `BEGIN`/`COMMIT`/`ROLLBACK` internally. Your callback receives a transaction and should contain only database operations and be safe to retry.

## Examples
<a name="SECTION_program-with-go-pgx-connector-examples"></a>

For more comprehensive examples and use cases, refer to the [Aurora DSQL Connector for Go examples](https://github.com/awslabs/aurora-dsql-connectors/tree/main/go/pgx/example).


| Example | Description | 
| --- | --- | 
|  [example\_preferred](https://github.com/awslabs/aurora-dsql-connectors/tree/main/go/pgx/example/src/example_preferred.go)  | Recommended: Connection pool with concurrent queries | 
|  [transaction](https://github.com/awslabs/aurora-dsql-connectors/tree/main/go/pgx/example/src/transaction)  | Transaction handling with BEGIN/COMMIT/ROLLBACK | 
|  [occ\_retry](https://github.com/awslabs/aurora-dsql-connectors/tree/main/go/pgx/example/src/occ_retry)  | Handling OCC conflicts with exponential backoff | 
|  [connection\_string](https://github.com/awslabs/aurora-dsql-connectors/tree/main/go/pgx/example/src/connection_string)  | Using connection strings for configuration | 