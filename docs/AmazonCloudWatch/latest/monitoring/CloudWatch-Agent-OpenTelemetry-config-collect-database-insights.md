

# Collect CloudWatch Database Insights metrics

The `database_insights` source collects metrics and logs from self-managed databases for CloudWatch Database Insights. This source can contain a `postgresql` array. Each entry in the array can include the following fields:
+ `endpoint` – Required. The host and port that the agent connects to, for example `localhost:5432`.
+ `instance_name` – Required. The display name of the instance in Database Insights.
+ `username` – Required. The database user that the agent uses for monitoring.
+ `password_file` – Required. The path to a libpq pgpass file that contains the monitoring user's password.
+ `ca_file` – Optional. The path to a CA certificate file for TLS connections to the database.
+ `per_resource_collection_interval` – Optional. How often, in seconds, to collect per-table and per-index metrics. The default is 60.
+ `logs` – Optional. Specifies the database log files to collect, with a `file_path` field.

In the monitored PostgreSQL database, create a monitoring role that the agent uses, grant it the `pg_monitor` role, and enable the `pg_stat_statements` extension. Store the monitoring role's password in a libpq pgpass file and point `password_file` at it. For the complete setup procedure, including how to create the monitoring user, the pgpass file, and the full agent configuration, see [Monitoring Self-Managed PostgreSQL](Database-Insights-Self-Managed-PostgreSQL.md).

The following example `opentelemetry` section collects Database Insights metrics from a self-managed PostgreSQL database that runs on the same host as the agent.

```json
{
  "opentelemetry": {
    "collect": {
      "database_insights": {
        "postgresql": [
          {
            "endpoint": "localhost:5432",
            "instance_name": "example-postgres",
            "username": "cwagent",
            "password_file": "/opt/aws/amazon-cloudwatch-agent/etc/cwagent-pgpass",
            "per_resource_collection_interval": 60
          }
        ]
      }
    }
  }
}
```

The agent publishes these as OpenTelemetry metrics to the CloudWatch OTLP endpoint, which you view in CloudWatch Database Insights and query with PromQL.