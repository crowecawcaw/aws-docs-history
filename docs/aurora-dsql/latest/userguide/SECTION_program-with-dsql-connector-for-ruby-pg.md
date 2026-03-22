# Connecting to Aurora DSQL clusters with a Ruby connector

The [Aurora DSQL Connector for Ruby](https://github.com/awslabs/aurora-dsql-connectors/tree/main/ruby/pg "https://github.com/awslabs/aurora-dsql-connectors/tree/main/ruby/pg") is a Ruby connector built on [pg](https://github.com/ged/ruby-pg "https://github.com/ged/ruby-pg") that integrates IAM authentication for connecting Ruby applications to Amazon Aurora DSQL clusters.

The connector handles token generation, SSL configuration, and connection pooling so you can focus on your application logic.

## About the connector

Amazon Aurora DSQL requires IAM authentication with time-limited tokens that existing Ruby PostgreSQL drivers do not natively support. The Aurora DSQL Connector for Ruby adds an authentication layer on top of the pg gem that handles IAM token generation, allowing you to connect to Aurora DSQL without changing your existing pg workflows.

### What is Aurora DSQL authentication?

In Aurora DSQL, **authentication** involves:

- **IAM Authentication**: All connections use IAM-based authentication with time-limited tokens
- **Token Generation**: The connector generates authentication tokens using AWS credentials, and these tokens have configurable lifetimes

The Aurora DSQL Connector for Ruby understands these requirements and automatically generates IAM authentication tokens when establishing connections.

### Features

- **Automatic IAM authentication** - Handles Aurora DSQL token generation and refresh
- **Built on pg** - Wraps the popular PostgreSQL gem for Ruby
- **Seamless integration** - Works with existing pg gem workflows
- **Connection pooling** - Built-in support via the `connection_pool` gem with max_lifetime enforcement
- **Region auto-detection** - Extracts AWS region from Aurora DSQL cluster hostname
- **AWS credentials support** - Supports AWS profiles and custom credentials providers
- **OCC retry** - Opt-in optimistic concurrency control retry with exponential backoff

## Example application

For a complete example, see the [example application](https://github.com/awslabs/aurora-dsql-connectors/tree/main/ruby/pg/example "https://github.com/awslabs/aurora-dsql-connectors/tree/main/ruby/pg/example") on GitHub.

## Quick start guide

### Requirements

- Ruby 3.1 or later
- [Access to an Aurora DSQL cluster](getting-started.md "getting-started.md")
- AWS credentials configured (via AWS CLI, environment variables, or IAM roles)

## Installation

Add to your Gemfile:

```
gem "aurora-dsql-ruby-pg"
```

Or install directly:

```
gem install aurora-dsql-ruby-pg
```

## Usage

### Pool connection

```
require "aurora_dsql_pg"

# Create a connection pool with OCC retry enabled
pool = AuroraDsql::Pg.create_pool(
  host: "your-cluster.dsql.us-east-1.on.aws",
  occ_max_retries: 3
)

# Read
pool.with do |conn|
  result = conn.exec("SELECT 'Hello, DSQL!'")
  puts result[0]["?column?"]
end

# Write — you must wrap writes in a transaction
pool.with do |conn|
  conn.transaction do
    conn.exec_params("INSERT INTO users (id, name) VALUES (gen_random_uuid(), $1)", ["Alice"])
  end
end

pool.shutdown
```

### Single connection

For simple scripts or when connection pooling is not needed:

```
conn = AuroraDsql::Pg.connect(host: "your-cluster.dsql.us-east-1.on.aws")
conn.exec("SELECT 1")
conn.close
```

### Advanced usage

**Host configuration**

The connector supports both full cluster endpoints (region auto-detected) and cluster IDs (region required):

```
# Full endpoint (region auto-detected)
pool = AuroraDsql::Pg.create_pool(
  host: "your-cluster.dsql.us-east-1.on.aws"
)

# Cluster ID (region required)
pool = AuroraDsql::Pg.create_pool(
  host: "your-cluster-id",
  region: "us-east-1"
)
```

**AWS profiles**

Specify an AWS profile for credentials:

```
pool = AuroraDsql::Pg.create_pool(
  host: "your-cluster.dsql.us-east-1.on.aws",
  profile: "production"
)
```

**Connection string format**

The connector supports PostgreSQL connection string formats:

```
postgres://[user@]host[:port]/[database][?param=value&...]
postgresql://[user@]host[:port]/[database][?param=value&...]
```

Supported query parameters: `region`, `profile`, `tokenDurationSecs`.

```
# Full endpoint with profile
pool = AuroraDsql::Pg.create_pool(
  "postgres://admin@cluster.dsql.us-east-1.on.aws/postgres?profile=dev"
)
```

**OCC retry**

Aurora DSQL uses optimistic concurrency control (OCC). When two transactions modify the same data, the first to commit wins and the second receives an OCC error.

OCC retry is opt-in. Set `occ_max_retries` when creating the pool to enable automatic retry with exponential backoff and jitter on `pool.with`:

```
pool = AuroraDsql::Pg.create_pool(
  host: "your-cluster.dsql.us-east-1.on.aws",
  occ_max_retries: 3
)

pool.with do |conn|
  conn.transaction do
    conn.exec_params("UPDATE accounts SET balance = balance - $1 WHERE id = $2", [100, from_id])
    conn.exec_params("UPDATE accounts SET balance = balance + $1 WHERE id = $2", [100, to_id])
  end
end
```

###### Warning

`pool.with` does NOT automatically wrap your block in a transaction. You must call `conn.transaction` yourself for write operations. On OCC conflict the connector re-executes the entire block, so it should contain only database operations and be safe to retry.

To skip retry on individual calls, pass `retry_occ: false`:

```
pool.with(retry_occ: false) do |conn|
  conn.exec("SELECT 1")
end
```

## Configuration options

| Field                | Type             | Default         | Description                                                               |
| -------------------- | ---------------- | --------------- | ------------------------------------------------------------------------- |
| host                 | String           | (required)      | Cluster endpoint or cluster ID                                            |
| region               | String           | (auto-detected) | AWS region; required if host is a cluster ID                              |
| user                 | String           | "admin"         | Database user                                                             |
| database             | String           | "postgres"      | Database name                                                             |
| port                 | Integer          | 5432            | Database port                                                             |
| profile              | String           | nil             | AWS profile name for credentials                                          |
| token_duration       | Integer          | 900 (15 min)    | Token validity duration in seconds (max allowed: 1 week, default: 15 min) |
| credentials_provider | Aws::Credentials | nil             | Custom credentials provider                                               |
| pool_size            | Integer          | 5               | Connection pool size                                                      |
| checkout_timeout     | Integer          | 5               | Seconds to wait for a pool connection                                     |
| max_lifetime         | Integer          | 3300 (55 min)   | Maximum connection lifetime in seconds                                    |
| application_name     | String           | nil             | ORM prefix for application_name                                           |
| logger               | Logger           | nil             | Logger for OCC retry warnings                                             |
| occ_max_retries      | Integer          | nil (disabled)  | Max OCC retries on `pool.with`; enables retry when set                    |

## Authentication

The connector automatically handles Aurora DSQL authentication by generating tokens using AWS credentials. If you do not provide the AWS region, the connector parses it from the hostname.

For more information on authentication in Aurora DSQL, see [Authentication and authorization for Aurora DSQL](authentication-authorization.md "authentication-authorization.md").

### Admin vs regular users

- Users named "admin" automatically use admin authentication tokens
- All other users use regular authentication tokens
- The connector generates tokens dynamically for each connection
