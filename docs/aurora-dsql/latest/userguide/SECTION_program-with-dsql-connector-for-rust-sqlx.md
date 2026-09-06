

# Aurora DSQL Connector for Rust SQLx
<a name="SECTION_program-with-dsql-connector-for-rust-sqlx"></a>

The [Aurora DSQL Connector for Rust](https://github.com/awslabs/aurora-dsql-connectors/tree/main/rust/sqlx) is a Rust connector built on [SQLx](https://github.com/launchbadge/sqlx) that integrates IAM authentication for connecting Rust applications to Amazon Aurora DSQL clusters.

The connector handles token generation, SSL configuration, and connection management so you can focus on your application logic.

## About the connector
<a name="SECTION_program-with-dsql-connector-for-rust-sqlx-about"></a>

The Aurora DSQL Connector for Rust adds an authentication layer on top of SQLx that handles IAM token generation, allowing you to connect to Aurora DSQL without changing your existing SQLx workflows.

### What is Aurora DSQL authentication?
<a name="SECTION_program-with-dsql-connector-for-rust-sqlx-authentication"></a>

In Aurora DSQL, **authentication** involves:
+ **IAM Authentication**: All connections use IAM-based authentication with time-limited tokens
+ **Token Generation**: The connector generates authentication tokens using AWS credentials, and these tokens have configurable lifetimes

The Aurora DSQL Connector for Rust understands these requirements and automatically generates IAM authentication tokens when establishing connections.

### Features
<a name="SECTION_program-with-dsql-connector-for-rust-sqlx-features"></a>
+ **Automatic IAM authentication** - Handles Aurora DSQL token generation and refresh
+ **Built on SQLx** - Wraps the popular async PostgreSQL driver for Rust
+ **Seamless integration** - Works with existing SQLx workflows
+ **Connection pooling** - Opt-in pool support with background token refresh via the `pool` feature
+ **Region auto-detection** - Extracts AWS region from Aurora DSQL cluster hostname
+ **AWS credentials support** - Supports AWS profiles and the default credential chain
+ **OCC retry** - Opt-in optimistic concurrency control retry with exponential backoff and jitter

## Example application
<a name="SECTION_program-with-dsql-connector-for-rust-sqlx-example-application"></a>

For a complete example, see the [example application](https://github.com/awslabs/aurora-dsql-connectors/tree/main/rust/sqlx/example) on GitHub.

## Quick start guide
<a name="SECTION_program-with-dsql-connector-for-rust-sqlx-quick-start"></a>

### Requirements
<a name="SECTION_program-with-dsql-connector-for-rust-sqlx-requirements"></a>
+ Rust 1.80 or later
+ [Getting started with Aurora DSQL](getting-started.md)
+ AWS credentials configured (via AWS CLI, environment variables, or IAM roles)

## Installation
<a name="SECTION_program-with-dsql-connector-for-rust-sqlx-installation"></a>

Add to your `Cargo.toml`:

```
[dependencies]
aurora-dsql-sqlx-connector = "0.1.2"
```

For most applications, enable both the `pool` and `occ` features:

```
[dependencies]
aurora-dsql-sqlx-connector = { version = "0.1.2", features = ["pool", "occ"] }
```

### Feature flags
<a name="SECTION_program-with-dsql-connector-for-rust-sqlx-feature-flags"></a>


| Feature | Default | Description | 
| --- | --- | --- | 
| pool | No | SQLx pool helper with background token refresh | 
| occ | No | OCC retry helpers (retry\_on\_occ, is\_occ\_error) | 

## Usage
<a name="SECTION_program-with-dsql-connector-for-rust-sqlx-usage"></a>

### Pool connection
<a name="SECTION_program-with-dsql-connector-for-rust-sqlx-pool-connection"></a>

```
use sqlx::Row;

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    let pool = aurora_dsql_sqlx_connector::pool::connect(
        "postgres://admin@your-cluster.dsql.us-east-1.on.aws/postgres"
    ).await?;

    // Read
    let row = sqlx::query("SELECT 'Hello, DSQL!' as greeting")
        .fetch_one(&pool)
        .await?;
    let greeting: &str = row.get("greeting");
    println!("{}", greeting);

    // Write — you must wrap writes in a transaction
    let mut tx = pool.begin().await?;
    sqlx::query("INSERT INTO users (id, name) VALUES (gen_random_uuid(), $1)")
        .bind("Alice")
        .execute(&mut *tx)
        .await?;
    tx.commit().await?;

    pool.close().await;
    Ok(())
}
```

### Single connection
<a name="SECTION_program-with-dsql-connector-for-rust-sqlx-single-connection"></a>

For simple scripts or when you don't need connection pooling:

```
use sqlx::Row;

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    let mut conn = aurora_dsql_sqlx_connector::connection::connect(
        "postgres://admin@your-cluster.dsql.us-east-1.on.aws/postgres"
    ).await?;

    let row = sqlx::query("SELECT 1 as value")
        .fetch_one(&mut conn)
        .await?;
    let value: i32 = row.get("value");
    println!("Result: {}", value);

    Ok(())
}
```

Each call to `connection::connect()` generates a fresh IAM token. For operations longer than the token duration, create a new connection.

### Advanced usage
<a name="SECTION_program-with-dsql-connector-for-rust-sqlx-advanced"></a>

**Host configuration**

The connector supports both full cluster endpoints (region auto-detected) and cluster IDs (region required):

```
// Full endpoint (region auto-detected)
let opts = DsqlConnectOptions::from_connection_string(
    "postgres://admin@your-cluster.dsql.us-east-1.on.aws/postgres"
)?;

// Cluster ID (region required)
let opts = DsqlConnectOptions::from_connection_string(
    "postgres://admin@your-cluster-id/postgres?region=us-east-1"
)?;
```

**AWS profiles**

Specify an AWS profile for credentials:

```
let pool = aurora_dsql_sqlx_connector::pool::connect(
    "postgres://admin@your-cluster.dsql.us-east-1.on.aws/postgres?profile=production"
).await?;
```

**Connection string format**

The connector supports PostgreSQL connection string formats:

```
postgres://[user@]host[:port]/[database][?param=value&...]
postgresql://[user@]host[:port]/[database][?param=value&...]
```

Supported query parameters: `region`, `profile`, `tokenDurationSecs`, `ormPrefix`.

**Pool configuration**

For custom pool settings, pass `PgPoolOptions` to `connect_with()`:

```
use aurora_dsql_sqlx_connector::DsqlConnectOptions;
use sqlx::postgres::PgPoolOptions;

let config = DsqlConnectOptions::from_connection_string(
    "postgres://admin@your-cluster.dsql.us-east-1.on.aws/postgres"
)?;

let pool = aurora_dsql_sqlx_connector::pool::connect_with(
    &config,
    PgPoolOptions::new().max_connections(20),
).await?;
```

**Programmatic configuration**

Use `DsqlConnectOptionsBuilder` for programmatic configuration:

```
use aurora_dsql_sqlx_connector::{DsqlConnectOptionsBuilder, Region};
use sqlx::postgres::PgConnectOptions;

let pg = PgConnectOptions::new()
    .host("your-cluster.dsql.us-east-1.on.aws")
    .username("admin")
    .database("postgres");

let opts = DsqlConnectOptionsBuilder::default()
    .pg_connect_options(pg)
    .region(Some(Region::new("us-east-1")))
    .build()?;

let mut conn = aurora_dsql_sqlx_connector::connection::connect_with(&opts).await?;
```

**OCC retry**

Aurora DSQL uses optimistic concurrency control (OCC). When two transactions modify the same data, the first to commit wins and the second receives an OCC error.

OCC retry is opt-in. Enable the `occ` feature and use `retry_on_occ` to enable automatic retry with exponential backoff and jitter:

```
use aurora_dsql_sqlx_connector::{retry_on_occ, OCCRetryConfig};

let config = OCCRetryConfig::default(); // max_attempts: 3, exponential backoff

retry_on_occ(&config, || async {
    let mut tx = pool.begin().await?;

    sqlx::query("UPDATE accounts SET balance = balance - 100 WHERE id = $1")
        .bind(account_id)
        .execute(&mut *tx)
        .await?;

    tx.commit().await?;
    Ok(())
}).await?;
```

**Warning**  
`retry_on_occ` re-executes the entire closure on OCC conflict, so the closure should contain only database operations and be safe to retry.

## Configuration options
<a name="SECTION_program-with-dsql-connector-for-rust-sqlx-configuration"></a>


| Field | Type | Default | Description | 
| --- | --- | --- | --- | 
| host | String | (required) | Cluster endpoint or cluster ID | 
| region | Option<Region> | (auto-detected) | AWS region; required if host is a cluster ID | 
| user | String | "admin" | Database user | 
| database | String | "postgres" | Database name | 
| port | u16 | 5432 | Database port | 
| profile | Option<String> | None | AWS profile name for credentials | 
| tokenDurationSecs | u64 | 900 (15 min) | Token validity duration in seconds | 
| ormPrefix | Option<String> | None | ORM prefix for application\_name (for example, "diesel" produces "diesel:aurora-dsql-rust-sqlx/{version}") | 

## Authentication
<a name="SECTION_program-with-dsql-connector-for-rust-sqlx-auth"></a>

The connector automatically handles Aurora DSQL authentication by generating tokens using AWS credentials. If you don't provide the AWS region, the connector parses it from the hostname.

For more information on authentication in Aurora DSQL, see [Authentication and authorization for Aurora DSQL](authentication-authorization.md).

### Token generation
<a name="SECTION_program-with-dsql-connector-for-rust-sqlx-token-generation"></a>
+ **Connection pools**: A background task refreshes the token at 80% of the token duration. Call `pool.close().await` to stop the refresh task and release pool resources.
+ **Single connections**: The connector generates a fresh token at connection time.
+ **Token generation** is a local SigV4 presigning operation with negligible cost.

### Admin vs regular users
<a name="SECTION_program-with-dsql-connector-for-rust-sqlx-admin-vs-regular"></a>
+ Users named "admin" automatically use admin authentication tokens
+ All other users use regular authentication tokens
+ The connector generates tokens dynamically for each connection