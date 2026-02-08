# Connecting to Aurora DSQL clusters with a Go connector

The [Aurora DSQL Connector for Go](https://github.com/awslabs/aurora-dsql-connectors/tree/main/go/pgx "https://github.com/awslabs/aurora-dsql-connectors/tree/main/go/pgx") wraps [pgx](https://github.com/jackc/pgx "https://github.com/jackc/pgx") with automatic IAM authentication. The connector handles token generation, SSL configuration, and connection management so you can focus on your application logic.

## About the connector

Aurora DSQL requires IAM-based authentication with time-limited tokens that existing Go PostgreSQL drivers do not natively support. The Aurora DSQL Connector for Go adds an authentication layer on top of the pgx driver that handles IAM token generation, allowing you to connect to Aurora DSQL without changing your existing pgx workflows.

### What is Aurora DSQL Authentication?

In Aurora DSQL, **authentication** involves:

- **IAM Authentication**: All connections use IAM-based authentication with time-limited tokens
- **Token Generation**: Authentication tokens are generated using AWS credentials and have configurable lifetimes

The Aurora DSQL Connector for Go is designed to understand these requirements and automatically generate IAM authentication tokens when establishing connections.

### Benefits of the Aurora DSQL Connector for Go

The Aurora DSQL Connector for Go allows you to continue using your existing pgx workflows while enabling IAM authentication through:

- **Automatic Token Generation**: IAM tokens are generated automatically with smart caching (refreshes at 80% of token lifetime)
- **Connection Pooling**: Built-in support for pgxpool with token caching for efficient connection creation
- **Flexible Configuration**: Support for full endpoints or cluster IDs with region auto-detection
- **AWS Credentials Support**: Supports AWS profiles and custom credentials providers

## Key features

Automatic Token Management

IAM tokens are generated and cached automatically. Tokens are refreshed at 80% of their lifetime to ensure they remain valid.

Connection Pooling

Connection pooling via pgxpool with token caching for efficient connection creation.

Flexible Host Configuration

Supports both full cluster endpoints and cluster IDs with automatic region detection.

SSL Security

SSL is always enabled with verify-full mode and direct TLS negotiation.

## Prerequisites

- Go 1.24 or later
- AWS credentials configured
- An Aurora DSQL cluster

The connector uses the [AWS SDK for Go v2 default credential chain](https://aws.github.io/aws-sdk-go-v2/docs/configuring-sdk/#specifying-credentials "https://aws.github.io/aws-sdk-go-v2/docs/configuring-sdk/#specifying-credentials"), which resolves credentials in the following order:

1. Environment variables (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
2. Shared credentials file (~/.aws/credentials)
3. Shared config file (~/.aws/config)
4. IAM role for Amazon EC2/ECS/Lambda

## Installation

Install the connector using Go modules:

```
go get github.com/awslabs/aurora-dsql-connectors/go/pgx/dsql
```

## Quick start

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

The connector supports the following configuration options:

| Field             | Type          | Default         | Description                                                               |
| ----------------- | ------------- | --------------- | ------------------------------------------------------------------------- |
| Host              | string        | (required)      | Cluster endpoint or cluster ID                                            |
| Region            | string        | (auto-detected) | AWS region; required if Host is a cluster ID                              |
| User              | string        | "admin"         | Database user                                                             |
| Database          | string        | "postgres"      | Database name                                                             |
| Port              | int           | 5432            | Database port                                                             |
| Profile           | string        | ""              | AWS profile name for credentials                                          |
| TokenDurationSecs | int           | 900 (15 min)    | Token validity duration in seconds (max allowed: 1 week, default: 15 min) |
| MaxConns          | int32         | 0               | Maximum pool connections (0 = pgxpool default)                            |
| MinConns          | int32         | 0               | Minimum pool connections (0 = pgxpool default)                            |
| MaxConnLifetime   | time.Duration | 55 minutes      | Maximum connection lifetime                                               |

## Connection string format

The connector supports PostgreSQL and DSQL connection string formats:

```
postgres://[user@]host[:port]/[database][?param=value&...]
dsql://[user@]host[:port]/[database][?param=value&...]
```

Supported query parameters:

- `region` - AWS region
- `profile` - AWS profile name
- `tokenDurationSecs` - Token validity duration in seconds

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

### Host configuration

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

Specify an AWS profile for credentials:

```
pool, err := dsql.NewPool(ctx, dsql.Config{
    Host:    "your-cluster.dsql.us-east-1.on.aws",
    Profile: "production",
})
```

## Token generation and caching

The connector automatically generates and caches IAM authentication tokens for optimal performance:

- **Connection pools**: Tokens are cached and reused across connections. The BeforeConnect hook retrieves tokens from the cache, generating new ones only when the cached token has used 80% of its lifetime.
- **Single connections**: A token is generated at connection time using pre-resolved credentials.
- **Credentials resolution**: AWS credentials are resolved once when the pool/connection is created and reused for all token generations.

Token duration defaults to 15 minutes (the maximum allowed by Aurora DSQL).

## Examples

For more comprehensive examples and use cases, refer to the [Aurora DSQL Connector for Go examples](https://github.com/awslabs/aurora-dsql-connectors/tree/main/go/pgx/example "https://github.com/awslabs/aurora-dsql-connectors/tree/main/go/pgx/example").

| Example                                                                                                                                                                                                                        | Description                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------- |
| [example_preferred](https://github.com/awslabs/aurora-dsql-connectors/tree/main/go/pgx/example/src/example_preferred.go "https://github.com/awslabs/aurora-dsql-connectors/tree/main/go/pgx/example/src/example_preferred.go") | Recommended: Connection pool with concurrent queries |
| [transaction](https://github.com/awslabs/aurora-dsql-connectors/tree/main/go/pgx/example/src/transaction "https://github.com/awslabs/aurora-dsql-connectors/tree/main/go/pgx/example/src/transaction")                         | Transaction handling with BEGIN/COMMIT/ROLLBACK      |
| [occ_retry](https://github.com/awslabs/aurora-dsql-connectors/tree/main/go/pgx/example/src/occ_retry "https://github.com/awslabs/aurora-dsql-connectors/tree/main/go/pgx/example/src/occ_retry")                               | Handling OCC conflicts with exponential backoff      |
| [connection_string](https://github.com/awslabs/aurora-dsql-connectors/tree/main/go/pgx/example/src/connection_string "https://github.com/awslabs/aurora-dsql-connectors/tree/main/go/pgx/example/src/connection_string")       | Using connection strings for configuration           |
