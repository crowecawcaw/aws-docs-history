

# Monitoring Self-Managed PostgreSQL
<a name="Database-Insights-Self-Managed-PostgreSQL"></a>

The following sections describe how to set up CloudWatch Database Insights monitoring for a self-managed PostgreSQL database. You prepare the database, install the CloudWatch agent on the database host, configure the agent to collect from the database, and verify that telemetry appears in the console.

## Prerequisites
<a name="Database-Insights-Self-Managed-prerequisites"></a>

Before you set up monitoring for a self-managed PostgreSQL database, confirm the following.
+ The database is running PostgreSQL version 14 or later.
+ The CloudWatch agent runs on the same host as the PostgreSQL instance. Monitoring a remote database is not supported.
+ You can create a dedicated, least-privilege database user for the agent to use for monitoring.
+ The Amazon EC2 instance has an IAM role that can publish metrics and logs to CloudWatch. For more information, see [Install the CloudWatch agent](#Database-Insights-Self-Managed-install).

## Prepare your PostgreSQL database
<a name="Database-Insights-Self-Managed-prepare-db"></a>

Self-managed monitoring reads performance data from standard PostgreSQL views, including `pg_stat_activity` and `pg_stat_statements`. Complete the following database-side configuration before you configure the agent.

**To prepare a PostgreSQL database for Database Insights**

1. In `postgresql.conf`, enable the `pg_stat_statements` extension and the server settings that Database Insights depends on. The extension must be loaded at startup through `shared_preload_libraries`, and the server logging settings populate the log files that the agent collects.

   ```
   # Required
   shared_preload_libraries = 'pg_stat_statements'
   track_activities = on
   track_activity_query_size = 4096
   password_encryption = 'scram-sha-256'
   
   # pg_stat_statements tuning
   pg_stat_statements.max = 10000
   pg_stat_statements.track = all
   pg_stat_statements.track_planning = on
   
   # Server logging (required for the slow query log)
   logging_collector = on
   log_directory = 'log'
   log_filename = 'postgresql-%a.log'
   log_rotation_age = 1d
   log_rotation_size = 0
   log_truncate_on_rotation = on
   log_min_duration_statement = 500
   log_line_prefix = '%m [%p] %q%u@%d '
   
   # Recommended (PostgreSQL 14 and later)
   compute_query_id = on
   ```

   The day-of-week `log_filename` pattern (`postgresql-%a.log`), combined with daily rotation and `log_truncate_on_rotation`, caps the log directory at roughly seven files and reuses them each week. This keeps the query log from growing without bound and filling the volume on a long-running host. The `postgresql-*.log` glob that you configure for the agent later still matches these file names.

1. Restart PostgreSQL. A restart, rather than a reload, is required because `shared_preload_libraries` is read only at startup.

   ```
   sudo systemctl restart postgresql
   ```

1. Create the `pg_stat_statements` extension in the `postgres` database. The agent connects to the `postgres` database and reads cluster-wide statistics from it, so the extension must exist there.

   ```
   \c postgres
   CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
   ```

1. Create a dedicated monitoring user and grant it the `pg_monitor` role. We don't recommend using an admin account. The `pg_monitor` role grants read access to `pg_stat_activity`, `pg_stat_statements`, and other monitoring views without superuser privileges.

   ```
   CREATE ROLE cw_monitor WITH LOGIN PASSWORD '{{your-password}}';
   GRANT pg_monitor TO cw_monitor;
   ```

1. To capture query execution plans, grant the monitoring user read access to the schemas that hold the tables your queries run against. Database Insights captures plans by running `EXPLAIN` as the monitoring user, and `EXPLAIN` requires access to the referenced tables. Run the grants in each database whose queries you want plans for, and repeat for any additional schemas.

   ```
   GRANT USAGE ON SCHEMA public TO cw_monitor;
   GRANT SELECT ON ALL TABLES IN SCHEMA public TO cw_monitor;
   ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO cw_monitor;
   ```
**Note**  
The `ALTER DEFAULT PRIVILEGES` statement grants `SELECT` only on tables created later by the same role that runs the statement. If tables are created by a different role, run `ALTER DEFAULT PRIVILEGES FOR ROLE` {{owner}} for that role as well.

1. In `pg_hba.conf`, allow the monitoring user to connect over `localhost`. Add lines for both the IPv4 and IPv6 loopback addresses, because `localhost` can resolve to either one.

   ```
   # TYPE  DATABASE  USER         ADDRESS         METHOD
   host    all       cw_monitor   127.0.0.1/32    scram-sha-256
   host    all       cw_monitor   ::1/128         scram-sha-256
   ```

   Then reload PostgreSQL to apply the change.

   ```
   sudo systemctl reload postgresql
   ```

1. Verify that the monitoring user can connect over `localhost` and read the monitoring views.

   ```
   psql -h localhost -U cw_monitor -d postgres -c "SELECT count(*) FROM pg_stat_activity;"
   psql -h localhost -U cw_monitor -d postgres -c "SELECT count(*) FROM pg_stat_statements;"
   ```

## Install the CloudWatch agent
<a name="Database-Insights-Self-Managed-install"></a>

Self-managed monitoring uses the CloudWatch agent to collect telemetry from your database. Install the agent on the same host as the PostgreSQL instance. There are several methods for installing the agent, so choose the one that best supports your operational practices. For full instructions on downloading, installing, and setting up permissions for the agent, see [Collect metrics, logs, and traces using the CloudWatch agent](Install-CloudWatch-Agent.md).

The IAM role that the Amazon EC2 instance uses must have the `CloudWatchAgentServerPolicy` AWS managed policy attached. This policy grants the permissions the agent needs to publish metrics and logs to CloudWatch.

## Configure the CloudWatch agent
<a name="Database-Insights-Self-Managed-configure"></a>

After the agent is installed, add a `database_insights` section to the agent configuration that defines the PostgreSQL instance to monitor.

**To configure the agent for a PostgreSQL database**

1. Create a password file in PostgreSQL libpq pgpass format so that the monitoring user's password is kept out of the main agent configuration. Create `/opt/aws/amazon-cloudwatch-agent/etc/pgpass` with a single line.

   ```
   # hostname:port:database:username:password
   localhost:5432:*:cw_monitor:{{your-password}}
   ```

   Restrict the file so that only the agent user can read it.

   ```
   sudo chmod 600 /opt/aws/amazon-cloudwatch-agent/etc/pgpass
   sudo chown cwagent:cwagent /opt/aws/amazon-cloudwatch-agent/etc/pgpass
   ```

1. Add the `database_insights` section to the agent configuration file at `/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json`.

   ```
   {
     "agent": {
       "region": "{{your-region}}"
     },
     "opentelemetry": {
       "collect": {
         "database_insights": {
           "postgresql": [
             {
               "endpoint": "localhost:5432",
               "instance_name": "{{your-instance-name}}",
               "username": "cw_monitor",
               "password_file": "/opt/aws/amazon-cloudwatch-agent/etc/pgpass",
               "logs": {
                 "file_path": "/var/lib/pgsql/data/log/postgresql-*.log"
               }
             }
           ]
         }
       }
     }
   }
   ```

   The following table describes the key parameters.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Database-Insights-Self-Managed-PostgreSQL.html)

1. Start the agent with the configuration. On an Amazon EC2 instance, use `-m ec2`.

   ```
   sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl \
       -a fetch-config \
       -m ec2 \
       -s \
       -c file:/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json
   ```

1. Confirm that the agent is running.

   ```
   sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a status
   ```

## Verify monitoring in the console
<a name="Database-Insights-Self-Managed-verify"></a>

After the agent starts, open the CloudWatch console and choose **Database Insights**. Within a few minutes, your self-managed PostgreSQL instance appears in the fleet view with a non-zero **DB Load** metric. Choose the instance to open its dashboard, and confirm that the following panels show data.
+ **DB Load** – active sessions broken down by wait event type, collected from `pg_stat_activity`.
+ **Top SQL** – query statistics from `pg_stat_statements`.
+ **Wait Events** – a breakdown by wait event type.
+ **Host Metrics** – CPU, memory, and disk I/O collected by the agent.

If the fleet view shows the instance but the detailed panels are empty, allow a few more minutes for `pg_stat_statements` data to accumulate.