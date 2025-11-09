# Getting started with Aurora DSQL

Amazon Aurora DSQL is a serverless, distributed relational database optimized for transactional
workloads. In the following sections, you’ll learn how to create single-Region and multi-Region
Aurora DSQL clusters, connect to them, and create and load a sample schema. You will access clusters
with the AWS Management Console and interact with your database using the `psql` utility. By the
end, you’ll have a working Aurora DSQL cluster set up and ready to use for test or production
workloads.

###### Topics

- [Prerequisites](#getting-started-prereqs "#getting-started-prereqs")
- [Accessing Aurora DSQL](#accessing "#accessing")
- [Step 1: Create an Aurora DSQL single-Region
  cluster](#getting-started-create-cluster "#getting-started-create-cluster")
- [Step 2: Connect to your Aurora DSQL cluster](#connect-dsql-cluster "#connect-dsql-cluster")
- [Step 3: Run sample SQL commands in Aurora DSQL](#getting-started-sql "#getting-started-sql")
- [Step 4: Create a multi-Region cluster](#getting-started-multi-region "#getting-started-multi-region")

## Prerequisites

Before you can begin using Aurora DSQL, make sure you meet the following prerequisites:

- Your IAM identity must have permission to [sign in to the
  AWS Management Console](../../../signin/latest/userguide/console-sign-in-tutorials.md "../../../signin/latest/userguide/console-sign-in-tutorials.md").
- Your IAM identity must meet either of the following criteria:
  - Access to perform any action on any resource in your AWS account
  - The IAM permission `iam:CreateServiceLinkedRole` and the ability to get
    access to the IAM policy action `dsql:*`

- If you use the AWS CLI in a Unix-like environment, make sure that Python version 3.8+ and
  `psql` version 14+ are installed. To check your application versions, run the
  following commands.

```
python3 --version
psql --version
```

If you use the AWS CLI in a different environment, make sure that you manually set up Python
version 3.8+ and `psql` version 14+.

- If you intend to access Aurora DSQL using AWS CloudShell, Python version 3.8+ and `psql`
  version 14+ are provided with no extra setup. For more information about AWS CloudShell, see [What is
  AWS CloudShell?](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md").
- If you intend to access Aurora DSQL using a GUI, use DBeaver or JetBrains DataGrip. For more
  information, see [Accessing Aurora DSQL with DBeaver](#accessing-sql-clients-dbeaver "#accessing-sql-clients-dbeaver") and [Accessing Aurora DSQL with JetBrains
  DataGrip](#accessing-sql-clients-datagrip "#accessing-sql-clients-datagrip").

## Accessing Aurora DSQL

You can access Aurora DSQL through the following techniques. To learn how to use the CLI, APIs,
and SDKs, see [Accessing Aurora DSQL](programming-with.md#accessing-programmatic "programming-with.md#accessing-programmatic").

###### Topics

- [Accessing Aurora DSQL through the AWS Management Console](#accessing-console "#accessing-console")
- [Accessing Aurora DSQL using SQL clients](#accessing-sql-clients "#accessing-sql-clients")
- [Using the PostgreSQL protocol with
  Aurora DSQL](#accessing-postgresql-endpoints "#accessing-postgresql-endpoints")

### Accessing Aurora DSQL through the AWS Management Console

You can access the AWS Management Console for Aurora DSQL at [https://console.aws.amazon.com/dsql](https://console.aws.amazon.com/dsql "https://console.aws.amazon.com/dsql").

### Accessing Aurora DSQL using SQL clients

Aurora DSQL uses the PostgreSQL protocol. Use your preferred interactive client by providing a
signed IAM [authentication
token](SECTION_authentication-token.md "SECTION_authentication-token.md") as the password when connecting to your cluster. An authentication token is a
unique string of characters that Aurora DSQL generates dynamically using AWS Signature Version 4.

Aurora DSQL uses the token only for authentication. The token doesn't affect the connection
after it is established. If you try to reconnect using an expired token, the connection
request is denied. For more information, see [Generating an authentication token in Amazon Aurora DSQL](SECTION_authentication-token.md "SECTION_authentication-token.md").

###### Topics

- [Accessing Aurora DSQL with psql (PostgreSQL
  interactive terminal)](#accessing-sql-clients-psql "#accessing-sql-clients-psql")
- [Accessing Aurora DSQL with DBeaver](#accessing-sql-clients-dbeaver "#accessing-sql-clients-dbeaver")
- [Accessing Aurora DSQL with JetBrains
  DataGrip](#accessing-sql-clients-datagrip "#accessing-sql-clients-datagrip")

#### Accessing Aurora DSQL with psql (PostgreSQL

interactive terminal)

The `psql` utility is a terminal-based front-end to PostgreSQL. It enables you to
type in queries interactively, issue them to PostgreSQL, and see the query results. To improve
query response times, use the PostgreSQL version 17 client.

Download your operating system's installer from the [PostgreSQL Downloads](https://www.postgresql.org/download/ "https://www.postgresql.org/download/") page. For more
information about `psql`, see [https://www.postgresql.org/docs/current/app-psql.htm](https://www.postgresql.org/docs/current/app-psql.htm "https://www.postgresql.org/docs/current/app-psql.htm").

If you already have the AWS CLI installed, use the following example to connect to your
cluster. You can either use AWS CloudShell, which comes with `psql` preinstalled, or
you can install `psql` directly.

```
# Aurora DSQL requires a valid IAM token as the password when connecting.
# Aurora DSQL provides tools for this and here we're using Python.
export PGPASSWORD=$(aws dsql generate-db-connect-admin-auth-token \
  --region `us-east-1` \
  --expires-in 3600 \
  --hostname `your_cluster_endpoint`)

# Aurora DSQL requires SSL and will reject your connection without it.
export PGSSLMODE=require

# Connect with psql, which automatically uses the values set in PGPASSWORD and PGSSLMODE.
# Quiet mode suppresses unnecessary warnings and chatty responses but still outputs errors.
psql --quiet \
  --username admin \
  --dbname postgres \
  --host `your_cluster_endpoint`
```

#### Accessing Aurora DSQL with DBeaver

DBeaver is an open-source, GUI-based database tool. You can use it to connect to and
manage your database. To download DBeaver, see the [download page](https://dbeaver.io/download/ "https://dbeaver.io/download/") on the DBeaver Community website. The following steps explain how
to connect to your cluster using DBeaver.

###### To set up a new Aurora DSQL connection in DBeaver

1. Choose **New Database Connection**.
2. In the **New Database Connection** window, choose
   PostgreSQL.
3. In the **Connection settings/Main** tab, choose **Connect
   by: Host** and enter the following information.
   1. **Host** – Use your cluster endpoint.

   **Database** – Enter `postgres`

   **Authentication** – Choose `Database
 Native`

   **Username** – Enter `admin`

   **Password** – Generate an [authentication token](SECTION_authentication-token.md "SECTION_authentication-token.md"). Copy the generated token and use it as your
   password.

4. Ignore any warnings and paste your authentication token into the **DBeaver
   Password** field.

###### Note

You must set SSL mode in the client connections. Aurora DSQL supports
`SSLMODE=require`. Aurora DSQL enforces SSL communication on the server side
and rejects non-SSL connections. 5. You should be connected to your cluster and can start running SQL statements.

###### Important

The administrative features provided by DBeaver for the PostgreSQL databases (such as
**Session Manager** and **Lock
Manager**) don't apply to a database, due to its unique architecture. While
accessible, these screens don't provide reliable information on the database health or
status.

**Authentication credentials expiry for DBeaver**

Established sessions remain authenticated for a maximum of 1 hour or until DBeaver
disconnects or times out. To establish new connections, provide a valid authentication token
in the **Password** field of **Connection
settings**. Trying to open a new session (for example, to list new tables, or a
new SQL console) forces a new authentication attempt. If the authentication token configured
in the **Connection settings** is no longer valid, the new
session fails, and DBeaver invalidates all previously opened sessions. Keep this in mind
when choosing the duration of your IAM authentication token with the
`expires-in` option.

#### Accessing Aurora DSQL with JetBrains

DataGrip

JetBrains DataGrip is a cross-platform IDE for working with SQL and databases, including
PostgreSQL. DataGrip includes a robust GUI with an intelligent SQL editor. To download
DataGrip, go to the [download
page](https://www.jetbrains.com/datagrip/download "https://www.jetbrains.com/datagrip/download") on the JetBrains website.

###### To set up a new Aurora DSQL connection in JetBrains DataGrip

1. Choose **New Data Source** and choose PostgreSQL.
2. In the Data Sources/General tab, enter the following information:
   1. **Host** – Use your cluster endpoint.

   **Port** – Aurora DSQL uses the PostgreSQL default:
   `5432`

   **Database** – Aurora DSQL uses the PostgreSQL default
   of `postgres`

   **Authentication** – Choose `User &
 Password` .

   **Username** – Enter `admin`.

   **Password** – [Generate a
   token](SECTION_authentication-token.md "SECTION_authentication-token.md") and paste it into this field.

   **URL** – Don't modify this field. It will be
   auto-populated based on the other fields.

3. **Password** – Provide this by generating an authentication
   token. Copy the resulting output of the token generator and paste it into the password
   field.

###### Note

You must set SSL mode in the client connections. Aurora DSQL supports
`PGSSLMODE=require`. Aurora DSQL enforces SSL communication on the server side
and will reject non-SSL connections. 4. You should be connected to your cluster and can start running SQL statements:

###### Important

Some views provided by DataGrip for the PostgreSQL databases (such as Sessions) don't
apply to a database because of its unique architecture. While accessible, these screens
don't provide reliable information on the actual sessions connected to the
database.

**Authentication credentials expiration**

Established sessions remain authenticated for a maximum of 1 hour or until an explicit
disconnect or a client-side timeout takes place. If new connections need to be established,
a new Authentication token must be generated and provided in the **Password** field of the **Data Source Properties**.
Trying to open a new session (for example, to list new tables, or a new SQL console) forces
a new authentication attempt. If the authentication token configured in the **Connection** settings is no longer valid, that new session will fail
and all previously opened sessions will become invalid.

### Using the PostgreSQL protocol with

Aurora DSQL

PostgreSQL uses a message-based protocol for communication between clients and servers.
The protocol is supported over TCP/IP and also over Unix-domain sockets. The following table
shows how Aurora DSQL supports the [PostgreSQL
protocol](https://www.postgresql.org/docs/current/protocol.html "https://www.postgresql.org/docs/current/protocol.html").

| PostgreSQL                                | Aurora DSQL                       | Notes                                                                                                                                                                                                                                                                                                                                                   |
| ----------------------------------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Role (also known as User or Group)        | Database Role                     | Aurora DSQL creates a role for you named `admin`. When you create custom<br>database roles, you must use the `admin` role to associate them with IAM<br>roles for authenticating when connecting to your cluster. For more information, see<br>[Configure<br>custom database roles](using-database-and-iam-roles.md "using-database-and-iam-roles.md"). |
| Host (also known as hostname or hostspec) | Cluster Endpoint                  | Aurora DSQL single-Region clusters provide a single managed endpoint and automatically<br>redirect traffic if there is unavailability within the Region.                                                                                                                                                                                                |
| Port                                      | N/A – use default `5432`          | This is the PostgreSQL default.                                                                                                                                                                                                                                                                                                                         |
| Database (dbname)                         | use `postgres`                    | Aurora DSQL creates this database for you when you create the cluster.                                                                                                                                                                                                                                                                                  |
| SSL Mode                                  | SSL is always enabled server-side | In Aurora DSQL, Aurora DSQL supports the `require` SSL Mode. Connections without<br>SSL are rejected by Aurora DSQL.                                                                                                                                                                                                                                    |
| Password                                  | Authentication Token              | Aurora DSQL requires temporary authentication tokens instead of long-lived passwords.<br>To learn more, see [Generating an authentication token in Amazon Aurora DSQL](SECTION_authentication-token.md "SECTION_authentication-token.md").                                                                                                              |

## Step 1: Create an Aurora DSQL single-Region

cluster

The basic unit of Aurora DSQL is the cluster, which is where you store your data. In this task,
you create a cluster in a single AWS Region.

###### To create a single-Region cluster in Aurora DSQL

1. Sign in to the AWS Management Console and open the Aurora DSQL console at [https://console.aws.amazon.com/dsql](https://console.aws.amazon.com/dsql "https://console.aws.amazon.com/dsql").
2. Choose **Create cluster** and then
   **Single-Region**.
3. (Optional) In **Cluster settings**, select any of the following
   options:
   - Select **Customize encryption settings (advanced)** to choose or
     create an AWS KMS key.
   - Select **Enable deletion protection** to prevent a delete operation
     from removing your cluster. By default, deletion protection is selected.

4. (Optional) In **Tags**, choose or enter a tag for this cluster.
5. Choose **Create cluster**.

## Step 2: Connect to your Aurora DSQL cluster

A _cluster endpoint_ is automatically generated when you create an
Aurora DSQL cluster based on its cluster ID and Region. The naming format is
``clusterid`.dsql.`region`.on.aws`.
A client uses the endpoint to create a network connection to your cluster.

Authentication is managed using IAM so you don't need to store credentials in the
database. An _authentication token_ is a unique string of characters that is
generated dynamically. The token is only used for authentication and doesn't affect the
connection after it is established. Before attempting to connect, make sure that your IAM
identity has the `dsql:DbConnectAdmin` permission, as described in [Prerequisites](#getting-started-prereqs "#getting-started-prereqs").

###### Note

To optimize database connection speed, use the PostgreSQL version 17 client and set
`PGSSLNEGOTIATION` to direct: `PGSSLNEGOTIATION=direct`.

###### To connect to your cluster with an authentication token

1. In the Aurora DSQL console, choose the cluster that you want to connect to.
2. Choose **Connect**.
3. Copy the endpoint from **Endpoint (Host)**.
4. Make sure that you **Connect as admin** is chosen in the
   **Authentication token (Password)** section.
5. Copy the generated authentication token. This token is valid for 15 minutes.
6. On the operating system command line, use the following command to start `psql`
   and connect to your cluster. Replace
   `your_cluster_endpoint` with the cluster endpoint that
   you copied previously.

```
PGSSLMODE=require \
  psql --dbname postgres \
  --username admin \
  --host `your_cluster_endpoint`
```

When prompted for a password, enter the authentication token that you copied previously.
If you try to reconnect using an expired token, the connection request is denied. For more
information, see [Generating an authentication token in Amazon Aurora DSQL](SECTION_authentication-token.md "SECTION_authentication-token.md"). 7. Press **Enter**. You should see a PostgreSQL prompt.

```
postgres=>
```

If you get an access denied error, make sure that your IAM identity has the
`dsql:DbConnectAdmin` permission. If you have the permission and continue to get
access deny errors, see [Troubleshoot IAM](../../../IAM/latest/UserGuide/troubleshoot.md "../../../IAM/latest/UserGuide/troubleshoot.md") and [How can I
troubleshoot access denied or unauthorized operation errors with an IAM policy?](https://repost.aws/knowledge-center/troubleshoot-iam-policy-issues "https://repost.aws/knowledge-center/troubleshoot-iam-policy-issues").

## Step 3: Run sample SQL commands in Aurora DSQL

Test your Aurora DSQL cluster by running SQL statements. The following sample statements require
the data files named `department-insert-multirow.sql` and `invoice.csv`,
which you can download from the [aws-samples/aurora-dsql-samples](https://github.com/aws-samples/aurora-dsql-samples/tree/main/quickstart_data "https://github.com/aws-samples/aurora-dsql-samples/tree/main/quickstart_data") repository on GitHub.

###### To run sample SQL commands in Aurora DSQL

1. Create a schema named `example`.

```
CREATE SCHEMA example;
```

2. Create an invoice table that uses an automatically generated UUID as the primary key.

```
CREATE TABLE example.invoice(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created timestamp,
    purchaser int,
    amount float);
```

3. Create a secondary index that uses the empty table.

```
CREATE INDEX ASYNC invoice_created_idx on example.invoice(created);
```

4. Create a department table.

```
CREATE TABLE example.department(id INT PRIMARY KEY UNIQUE, name text, email text);
```

5. Use the command `psql \include` to load the file named
   `department-insert-multirow.sql` that you downloaded from the [aws-samples/aurora-dsql-samples](https://github.com/aws-samples/aurora-dsql-samples/tree/main/quickstart_data "https://github.com/aws-samples/aurora-dsql-samples/tree/main/quickstart_data") repository on GitHub. Replace
   `my-path` with the path to your local copy.

```
\include `my-path`/department-insert-multirow.sql
```

6. Use the command `psql \copy` to load the file named `invoice.csv`
   that you downloaded from the [aws-samples/aurora-dsql-samples](https://github.com/aws-samples/aurora-dsql-samples/tree/main/quickstart_data "https://github.com/aws-samples/aurora-dsql-samples/tree/main/quickstart_data") repository on GitHub. Replace
   `my-path` with the path to your local copy.

```
\copy example.invoice(created, purchaser, amount) from `my-path`/invoice.csv csv
```

7. Query the departments and sort them by their total sales.

```
SELECT name, sum(amount) AS sum_amount
FROM example.department LEFT JOIN example.invoice ON department.id=invoice.purchaser
GROUP BY name
HAVING sum(amount) > 0
ORDER BY sum_amount DESC;
```

The following sample output shows that Department One has the most sales.

```
           name           |     sum_amount
--------------------------+--------------------
 Example Department One   |  32628.75608634601
 Example Department Three |  32427.43955110429
 Example Department Eight | 32256.810987098102
 Example Department Five  |  31391.14891163639
 Example Department Seven | 31253.236846746757
 Example Department Six   |  29699.06014910414
 Example Department Two   |  29465.58360076501
 Example Department Four  |  28764.19185819191
(8 rows)
```

## Step 4: Create a multi-Region cluster

When you create a multi-Region cluster, you specify the following Regions:

**Remote Region**

This is the Region in which you create a second cluster. You create a second cluster in
this Region and peer it to your initial cluster. Aurora DSQL replicates all writes on the initial
cluster to the remote cluster. You can read and write on any cluster.

**Witness Region**

This Region receives all data that is written to the multi-Region cluster. However,
witness Regions don't host client endpoints and don't provide user data access. A limited
window of the encrypted transaction log is maintained in witness Regions. This log facilitates
recovery and supports transactional quorum if a Region becomes unavailable.

The following example shows how to create an initial cluster, create a second cluster in a
different Region, and then peer the two clusters to create a multi-Region cluster. It also
demonstrates cross-Region write replication and consistent reads from both Regional
endpoints.

###### To create a multi-Region cluster

1. Sign in to the AWS Management Console and open the Aurora DSQL console at [https://console.aws.amazon.com/dsql](https://console.aws.amazon.com/dsql "https://console.aws.amazon.com/dsql").
2. In the navigation pane, choose **Clusters**.
3. Choose **Create cluster** and then
   **Multi-Region**.
4. (Optional) In **Cluster settings**, select any of the following options
   for your initial cluster:
   - Select **Customize encryption settings (advanced)** to choose or
     create an AWS KMS key.
   - Select **Enable deletion protection** to prevent a delete operation
     from removing your cluster. By default, deletion protection is selected.

5. In **Multi-Region settings**, choose the following options for your
   initial cluster:
   - In **Witness Region**, choose a Region. Currently, only US-based
     Regions are supported for witness Regions in multi-Region clusters.
   - (Optional) In **Remote Region cluster ARN**, enter an ARN for an
     existing cluster in another Region. If no cluster exists to serve as the second cluster in
     your multi-Region cluster, complete setup after you create the initial cluster.

6. (Optional) Choose tags for your initial cluster.
7. Choose **Create cluster** to create your initial cluster. If you didn't
   enter an ARN in the previous step, the console shows the **Cluster setup
   pending** notification.
8. In the **Cluster setup pending** notification, choose **Complete
   multi-Region cluster setup**. This action initiates creation of a second cluster in
   another Region.
9. Choose one of the following options for your second cluster:
   - **Add remote Region cluster ARN** – Choose this option if a
     cluster exists, and you want it to be the second cluster in your multi-Region cluster.
   - **Create cluster in another Region** – Choose this option to
     create a second cluster. In **Remote Region**, choose the Region for this
     second cluster.

10. Choose **Create cluster in
    `your-second-region`**, where
    `your-second-region` is the location of your second cluster. The
    console opens in your second Region.
11. (Optional) Choose cluster settings for your second cluster. For example, you can choose an
    AWS KMS key.
12. Choose **Create cluster** to create your second cluster.
13. Choose **Peer in `initial-cluster-region`**,
    where is `initial-cluster-region` is the Region that hosts the first
    cluster that you created.
14. When prompted, choose **Confirm**. This step completes the creation of
    your multi-Region cluster.

###### To connect to your second cluster

1. Open the Aurora DSQL console and choose the Region for your second cluster.
2. Choose **Clusters**.
3. Select the row for the second cluster in your multi-Region cluster.
4. In **Actions**, choose **Open in CloudShell**.
5. Choose **Connect as admin**.
6. Choose **Launch CloudShell**.
7. Choose **Run**.
8. Create a sample schema by following the steps in [Step 3: Run sample SQL commands in Aurora DSQL](#getting-started-sql "#getting-started-sql").

**Example transactions**

```
CREATE SCHEMA example;
CREATE TABLE example.invoice(id UUID PRIMARY KEY DEFAULT gen_random_uuid(), created timestamp, purchaser int, amount float);
CREATE INDEX ASYNC invoice_created_idx on example.invoice(created);
CREATE TABLE example.department(id INT PRIMARY KEY UNIQUE, name text, email text);
```

9. Use `psql`
   `copy` and `include` commands to load sample data. For more information,
   see [Step 3: Run sample SQL commands in Aurora DSQL](#getting-started-sql "#getting-started-sql").

```
\copy example.invoice(created, purchaser, amount) from samples/invoice.csv csv
\include samples/department-insert-multirow.sql
```

###### To query data in the second cluster from the Region hosting your initial cluster

1. In the Aurora DSQL console, choose the Region for your initial cluster.
2. Choose **Clusters**.
3. Select the row for the second cluster in your multi-Region cluster.
4. In **Actions**, choose **Open in CloudShell**.
5. Choose **Connect as admin**.
6. Choose **Launch CloudShell**.
7. Choose **Run**.
8. Query the data that you inserted into the second cluster.

```
SELECT name, sum(amount) AS sum_amount
FROM example.department
LEFT JOIN example.invoice ON department.id=invoice.purchaser
GROUP BY name
HAVING sum(amount) > 0
ORDER BY sum_amount DESC;
```
