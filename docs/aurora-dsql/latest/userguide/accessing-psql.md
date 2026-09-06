

# Use the PostgreSQL interactive terminal (psql) to access Aurora DSQL
<a name="accessing-psql"></a>

## Use AWS CloudShell to access Aurora DSQL with the PostgreSQL interactive terminal (psql)
<a name="accessing-sql-clients-psql"></a>

Use the following procedure to access Aurora DSQL with the PostgreSQL interactive terminal from AWS CloudShell. For more information, see [What is AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html).

**To connect using AWS CloudShell**

1. Sign in to the [Aurora DSQL console](https://console.aws.amazon.com/dsql).

1. Choose the cluster for which you would like to open in CloudShell. If you haven't yet created a cluster, follow the steps in [Step 1: Create an Aurora DSQL single-Region cluster](getting-started.md#getting-started-create-cluster) or [Create a multi-Region cluster](getting-started.md#getting-started-multi-region).

1. Choose **Connect with Query Editor** and then choose **Connect with CloudShell**.

1. Choose whether you want to connect as an admin or with a [custom database role](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/authentication-authorization.html#authentication-authorization-iam-role-connect).

1. Choose **Launch in CloudShell** and choose **Run** in the following CloudShell dialog.

## Use the local CLI to access Aurora DSQL with the PostgreSQL interactive terminal (psql)
<a name="accessing-sql-clients-psql-local"></a>

Use `psql`, a terminal-based front-end to PostgreSQL utility, to interactively enter in queries, issue them to PostgreSQL, and view the query results.

**Note**  
To improve query response times, use the PostgreSQL version 17 client. If you use the CLI in a different environment, make sure you manually set up Python version 3.8\+ and psql version 14\+.

Download your operating system's installer from the [PostgreSQL Downloads](https://www.postgresql.org/download/) page. For more information about `psql`, see [PostgreSQL Client Applications](https://www.postgresql.org/docs/current/app-psql.htm) on the *PostgreSQL* website.

If you already have the AWS CLI installed, use the following example to connect to your cluster.

```
# Aurora DSQL requires a valid IAM token as the password when connecting.
# Aurora DSQL provides tools for this and here we're using Python.
export PGPASSWORD=$(aws dsql generate-db-connect-admin-auth-token \
  --region {{us-east-1}} \
  --expires-in 3600 \
  --hostname {{your_cluster_endpoint}})

# Aurora DSQL requires SSL and will reject your connection without it.
export PGSSLMODE=require

# Connect with psql, which automatically uses the values set in PGPASSWORD and PGSSLMODE.
# Quiet mode suppresses unnecessary warnings and chatty responses but still outputs errors.
psql --quiet \
  --username admin \
  --dbname postgres \
  --host {{your_cluster_endpoint}}
```