

# Aurora DSQL Connector for .NET Npgsql
<a name="SECTION_program-with-dsql-connector-for-dotnet-npgsql"></a>

The [Aurora DSQL Connector for .NET](https://github.com/awslabs/aurora-dsql-connectors/tree/main/dotnet/npgsql) is a .NET connector built on [Npgsql](https://www.npgsql.org/) that integrates IAM authentication for connecting .NET applications to Amazon Aurora DSQL clusters.

The connector handles token generation, SSL configuration, and connection pooling so you can focus on your application logic.

## About the connector
<a name="SECTION_program-with-dsql-connector-for-dotnet-npgsql-about"></a>

Amazon Aurora DSQL requires IAM authentication with time-limited tokens that existing .NET PostgreSQL drivers do not natively support. The Aurora DSQL Connector for .NET adds an authentication layer on top of Npgsql that handles IAM token generation, allowing you to connect to Aurora DSQL without changing your existing Npgsql workflows.

### What is Aurora DSQL authentication?
<a name="SECTION_program-with-dsql-connector-for-dotnet-npgsql-authentication"></a>

In Aurora DSQL, **authentication** involves:
+ **IAM Authentication**: All connections use IAM-based authentication with time-limited tokens
+ **Token Generation**: The connector generates authentication tokens using AWS credentials, and these tokens have configurable lifetimes

The Aurora DSQL Connector for .NET understands these requirements and automatically generates IAM authentication tokens when establishing connections.

### Features
<a name="SECTION_program-with-dsql-connector-for-dotnet-npgsql-features"></a>
+ **Automatic IAM authentication** - Handles Aurora DSQL token generation and refresh
+ **Built on Npgsql** - Wraps the popular PostgreSQL driver for .NET
+ **Seamless integration** - Works with existing Npgsql workflows
+ **Connection pooling** - Built-in support via `NpgsqlDataSource` with max lifetime enforcement
+ **Region auto-detection** - Extracts AWS region from Aurora DSQL cluster hostname
+ **AWS credentials support** - Supports AWS profiles and custom credentials providers
+ **OCC retry** - Opt-in optimistic concurrency control retry with exponential backoff
+ **SSL enforcement** - Always uses SSL with `verify-full` mode and direct TLS negotiation

## Example application
<a name="SECTION_program-with-dsql-connector-for-dotnet-npgsql-example-application"></a>

For a complete example, see the [example application](https://github.com/awslabs/aurora-dsql-connectors/tree/main/dotnet/npgsql/example) on GitHub.

## Quick start guide
<a name="SECTION_program-with-dsql-connector-for-dotnet-npgsql-quick-start"></a>

### Requirements
<a name="SECTION_program-with-dsql-connector-for-dotnet-npgsql-requirements"></a>
+ .NET 8.0 or later
+ [Access to an Aurora DSQL cluster](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/getting-started.html)
+ AWS credentials configured (via AWS CLI, environment variables, or IAM roles)

## Installation
<a name="SECTION_program-with-dsql-connector-for-dotnet-npgsql-installation"></a>

Add the package to your project:

```
dotnet add package Amazon.AuroraDsql.Npgsql
```

## Usage
<a name="SECTION_program-with-dsql-connector-for-dotnet-npgsql-usage"></a>

### Pool connection
<a name="SECTION_program-with-dsql-connector-for-dotnet-npgsql-pool-connection"></a>

```
using Amazon.AuroraDsql.Npgsql;

// Create a connection pool
await using var ds = await AuroraDsql.CreateDataSourceAsync(new DsqlConfig
{
    Host = "your-cluster.dsql.us-east-1.on.aws",
    OccMaxRetries = 3
});

// Read
await using (var conn = await ds.OpenConnectionAsync())
{
    await using var cmd = conn.CreateCommand();
    cmd.CommandText = "SELECT 'Hello, DSQL!'";
    var greeting = await cmd.ExecuteScalarAsync();
    Console.WriteLine(greeting);
}

// Transactional write with OCC retry
await ds.WithTransactionRetryAsync(async conn =>
{
    await using var cmd = conn.CreateCommand();
    cmd.CommandText = "INSERT INTO users (id, name) VALUES (gen_random_uuid(), @name)";
    cmd.Parameters.AddWithValue("name", "Alice");
    await cmd.ExecuteNonQueryAsync();
});
```

### Single connection
<a name="SECTION_program-with-dsql-connector-for-dotnet-npgsql-single-connection"></a>

For simple scripts or when you do not need connection pooling:

```
await using var conn = await AuroraDsql.ConnectAsync(new DsqlConfig
{
    Host = "your-cluster.dsql.us-east-1.on.aws"
});

await using var cmd = conn.CreateCommand("SELECT 1");
await cmd.ExecuteScalarAsync();
```

### OCC retry
<a name="SECTION_program-with-dsql-connector-for-dotnet-npgsql-occ-retry"></a>

Aurora DSQL uses optimistic concurrency control (OCC). When two transactions modify the same data, the first to commit wins and the second receives an OCC error.

OCC retry is opt-in. Set `OccMaxRetries` in the config to enable automatic retry with exponential backoff and jitter. Use `WithTransactionRetryAsync` for transactional writes:

```
await ds.WithTransactionRetryAsync(async conn =>
{
    await using var cmd = conn.CreateCommand();

    cmd.CommandText = "UPDATE accounts SET balance = balance - 100 WHERE id = @from";
    cmd.Parameters.AddWithValue("from", fromId);
    await cmd.ExecuteNonQueryAsync();

    cmd.CommandText = "UPDATE accounts SET balance = balance + 100 WHERE id = @to";
    cmd.Parameters.Clear();
    cmd.Parameters.AddWithValue("to", toId);
    await cmd.ExecuteNonQueryAsync();
});
```

For DDL or single statements, use `ExecWithRetryAsync`:

```
await ds.ExecWithRetryAsync("CREATE TABLE IF NOT EXISTS users (id UUID PRIMARY KEY, name TEXT)");
```

**Important**  
`WithTransactionRetryAsync` manages `BEGIN`/`COMMIT`/`ROLLBACK` internally and opens a fresh connection for each attempt. Your callback should contain only database operations and be safe to retry.

## Configuration options
<a name="SECTION_program-with-dsql-connector-for-dotnet-npgsql-configuration"></a>

The connector also accepts `postgres://` and `postgresql://` connection strings with `region` and `profile` query parameters.


| Field | Type | Default | Description | 
| --- | --- | --- | --- | 
| Host | string | (required) | Cluster endpoint or 26-char cluster ID | 
| Region | string? | (auto-detected) | AWS region; required if Host is a cluster ID | 
| User | string | "admin" | Database user | 
| Database | string | "postgres" | Database name | 
| Port | int | 5432 | Database port | 
| Profile | string? | null | AWS profile name for credentials | 
| CustomCredentialsProvider | AWSCredentials? | null | Custom AWS credentials provider | 
| TokenDurationSecs | int? | null (SDK default, 900s) | Token validity duration in seconds | 
| OccMaxRetries | int? | null (disabled) | Default max OCC retries for retry methods on the data source | 
| OrmPrefix | string? | null | ORM prefix prepended to application\_name | 
| LoggerFactory | ILoggerFactory? | null | Logger factory for retry warnings and diagnostics | 
| ConfigureConnectionString | Action<NpgsqlConnectionStringBuilder>? | null | Callback to override pool settings or set additional Npgsql connection string properties. SSL and Enlist are security invariants and cannot be overridden. | 

## Authentication
<a name="SECTION_program-with-dsql-connector-for-dotnet-npgsql-auth"></a>

The connector automatically handles Aurora DSQL authentication by generating tokens using AWS credentials. If you do not provide the AWS region, the connector parses it from the hostname.

For more information on authentication in Aurora DSQL, see [Authentication and authorization for Aurora DSQL](authentication-authorization.md).

### Admin vs regular users
<a name="SECTION_program-with-dsql-connector-for-dotnet-npgsql-admin-vs-regular"></a>
+ Users named "admin" automatically use admin authentication tokens
+ All other users use regular authentication tokens
+ The connector generates tokens dynamically for each connection