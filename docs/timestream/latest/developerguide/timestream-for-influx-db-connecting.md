For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Connecting to an Amazon Timestream for InfluxDB DB instance

Before you can connect to a DB instance, you must create the DB instance. For information, see
[Creating a DB instance](timestream-for-influx-configuring.md#timestream-for-influx-configuring-create-db "timestream-for-influx-configuring.md#timestream-for-influx-configuring-create-db"). After Amazon
Timestream provisions your DB instance, use the InfluxDB API, influx CLI, or any compatible client or utility for InfluxDB to connect to the DB instance.

###### Topics

- [Finding the connection information for an Amazon Timestream for InfluxDB DB instance](#timestream-for-influx-db-connecting-finding-connection-info "#timestream-for-influx-db-connecting-finding-connection-info")
- [Database authentication options](#timestream-for-influx-db-connecting-authentication-options "#timestream-for-influx-db-connecting-authentication-options")
- [Working with parameter groups](#timestream-for-influx-parameter-groups "#timestream-for-influx-parameter-groups")

## Finding the connection information for an Amazon Timestream for InfluxDB DB instance

The connection information for a DB instance includes its endpoint, port,
username, password, and a valid access token, such as the operator or all-access token. For example, for a Timestream for InfluxDB DB instance, suppose that the endpoint value is `c5vasdqn0b-3ksj4dla5nfjhi.timestream-influxdb.us-east-1.on.aws`. In this case, the port value is 8086, and the database user is _admin_. Given this information, to access the instance you will use:

- The endpoint of your instance, `c5vasdqn0b-3ksj4dla5nfjhi.timestream-influxdb.us-east-1.on.aws:8086`.
- Either the username and password supplied when creating the instance or valid access token.

Instances created before December 9, 2024 will have an endpoint that contains the
instance name instead of the instance ID. For example: `influxdb1-123456789.us-east-1.timestream-influxdb.amazonaws.com`.

###### Important

As part of the DB instance response object, you will receive a
`influxAuthParametersSecretArn`. This will hold an ARN to a Secrets Manager
secret in your account. t will only be populated after your InfluxDB DB
instances are available. The secret contains Influx authentication parameters
provided during the `CreateDbInstance` process. This is a **read-only** copy as any updates/modifications/deletions
to this secret doesn't impact the created DB instance. If you delete this
secret, our API response will still refer to the deleted secret ARN.

The endpoint is unique for each DB instance, and the values of the port and user can vary.
To connect to a DB instance, you can use the influx CLI, InfluxDB API, or any client compatible with InfluxDB.

To find the connection information for a DB instance, use the AWS Management
Console. You can also use the AWS Command Line Interface (AWS CLI)
`describe-db-instances` command or the Timestream for InfluxDB API `GetDBInstance` operation.

###### Using the AWS Management Console

1. Sign in to the AWS Management Console and open the [Amazon Timestream console](https://console.aws.amazon.com/timestream/ "https://console.aws.amazon.com/timestream/").
2. In the navigation pane, choose **InfluxDB Databases**
   to display a list of your DB instances.
3. Choose the name of the DB instance to display its details.
4. In the **Summary** section, copy the endpoint.
   Also, note the port number. You will need both the endpoint and the port number to connect to the
   DB instance.

If you need to find the username and password information, choose the **Configuration Details** tab and choose the `influxAuthParametersSecretArn`
to access your Secrets Manager.

###### Using the CLI

- To find the connection information for a InfluxDB DB instance by using
  the AWS CLI, call the `get-db-instance` command. In the call, query
  for the DB instance ID, endpoint, port, and influxAuthParametersSecretArn.

For Linux, macOS, or Unix:

```
aws timestream-influxdb get-db-instance --identifier id \
 --query "[name,endpoint,influxAuthParametersSecretArn]"
```

For Windows:

```
aws timestream-influxdb get-db-instance --identifier id ^
 --query "[name,endpoint,influxAuthParametersSecretArn]"
```

Your output should be similar to the following. To access the username
information, you will need to check the `InfluxAuthParameterSecret`.

```
[
    [
        "mydb",
        "mydbid-123456789012.timestream-influxdb.us-east-1.on.aws",
        8086,
    ]
]
```

### Creating access tokens

With this information, you are going to be able to connect to your instance to retrieve or create your access tokens. There are several ways to achieve this:

###### Using the CLI

1. If you haven’t already, download, install, and configure the [influx CLI](https://docs.influxdata.com/influxdb/v2/tools/influx-cli/ "https://docs.influxdata.com/influxdb/v2/tools/influx-cli/").
2. When configuring your influx CLI config, use `--username-password` to authenticate.

```
influx config create --config-name YOUR_CONFIG_NAME --host-url "https://yourinstanceid-accountidentifier.timestream-influxdb.us-east-1.on.aws:8086" --org yourorg --username-password admin --active
```

3. Use the [influx auth create](https://docs.influxdata.com/influxdb/v2/reference/cli/influx/auth/create/ "https://docs.influxdata.com/influxdb/v2/reference/cli/influx/auth/create/") command to re-create your operator token. Take into account that this process will invalidate the old operator token.

```
influx auth create --org kronos --operator
```

4. Once you have the operator token, you can use the [influx auth list](https://docs.influxdata.com/influxdb/v2/reference/cli/influx/auth/list "https://docs.influxdata.com/influxdb/v2/reference/cli/influx/auth/list") command to
   view all your tokens. You can use the [influx auth create](https://docs.influxdata.com/influxdb/v2/reference/cli/influx/auth/create/ "https://docs.influxdata.com/influxdb/v2/reference/cli/influx/auth/create/") command
   to create an all-access token.

###### Important

You will need to perform this step to obtain your operator token
first. Then you will be able to create new tokens using the InfluxDB API or CLI.

###### Using the InfluxDB UI

1. Browse to your Timestream for InfluxDB instance using the created endpoint to log in and access the InfluxDB UI. You will need to use the username and password
   used to create your InfluxDB DB instance. You can retrieve this information from the
   `influxAuthParametersSecretArn` that was specified in the response object of the
   `CreateDbInstance`.

Alternatively you can open the InfluxDB UI from the Amazon Timestream for InfluxDB console:

    1. Sign in to the AWS Management Console and open the Timestream for InfluxDB console at [https://console.aws.amazon.com/timestream/.](https://console.aws.amazon.com/timestream/ "https://console.aws.amazon.com/timestream/")
    2. In the upper-right corner of the Amazon Timestream for InfluxDB console, choose the
     AWS Region in which you created the DB instance.
    3. In the **Databases** list, choose the name of your
     InfluxDB instance to show its details. In the upper right corner,
     choose **InfluxDB UI**.

2. Once logged in to your InfluxDB UI, navigate to **Load Data** and then **API Tokens**
   using the left navigation bar.
3. Choose **Generate API Token** and select **All Access API Token**.
4. Enter a description for the API token and choose **SAVE**.
5. Copy the generated token and store it for safe keeping.

###### Important

When creating tokens from the InfluxDB UI, the newly created tokens
are only going to be shown once. Make sure you copy these. Otherwise, you will need to re-create them.

###### Using the InfluxDB API

- Send a request to the InfluxDB API `/api/v2/authorizations` endpoint using the POST request method.

Include the following with your request:

    1. Headers:


    	1. Authorization: Token <INFLUX\_OPERATOR\_TOKEN>
    	2. Content-Type: application/json
    2. Request body: JSON body with the following properties:


    	1. status: "active"
    	2. description: API token description
    	3. orgID: InfluxDB organization ID
    	4. permissions: Array of objects where each object represents permissions for an InfluxDB resource type or a specific resource. Each permission contains the following properties:


    		1. action: “read” or “write”
    		2. resource: JSON object that represents the InfluxDB resource to grant permission to. Each resource
    		 contains at least the following property: orgID: InfluxDB organization ID
    		3. type: Resource type. For information about what InfluxDB resource types exist, use the /api/v2/resources endpoint.

The following example uses `curl` and the InfluxDB API to generate
an all-access token:

```
export INFLUX_HOST=https://instanceid-123456789.timestream-influxdb.us-east-1.on.aws
export INFLUX_ORG_ID=<YOUR_INFLUXDB_ORG_ID>
export INFLUX_TOKEN=<YOUR_INFLUXDB_OPERATOR_TOKEN>

curl --request POST \
"$INFLUX_HOST/api/v2/authorizations" \
  --header "Authorization: Token $INFLUX_TOKEN" \
  --header "Content-Type: text/plain; charset=utf-8" \
  --data '{
    "status": "active",
    "description": "All access token for get started tutorial",
    "orgID": "'"$INFLUX_ORG_ID"'",
    "permissions": [
      {"action": "read", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "authorizations"}},
      {"action": "write", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "authorizations"}},
      {"action": "read", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "buckets"}},
      {"action": "write", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "buckets"}},
      {"action": "read", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "dashboards"}},
      {"action": "write", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "dashboards"}},
      {"action": "read", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "orgs"}},
      {"action": "write", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "orgs"}},
      {"action": "read", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "sources"}},
      {"action": "write", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "sources"}},
      {"action": "read", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "tasks"}},
      {"action": "write", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "tasks"}},
      {"action": "read", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "telegrafs"}},
      {"action": "write", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "telegrafs"}},
      {"action": "read", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "users"}},
      {"action": "write", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "users"}},
      {"action": "read", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "variables"}},
      {"action": "write", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "variables"}},
      {"action": "read", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "scrapers"}},
      {"action": "write", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "scrapers"}},
      {"action": "read", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "secrets"}},
      {"action": "write", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "secrets"}},
      {"action": "read", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "labels"}},
      {"action": "write", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "labels"}},
      {"action": "read", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "views"}},
      {"action": "write", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "views"}},
      {"action": "read", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "documents"}},
      {"action": "write", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "documents"}},
      {"action": "read", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "notificationRules"}},
      {"action": "write", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "notificationRules"}},
      {"action": "read", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "notificationEndpoints"}},
      {"action": "write", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "notificationEndpoints"}},
      {"action": "read", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "checks"}},
      {"action": "write", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "checks"}},
      {"action": "read", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "dbrp"}},
      {"action": "write", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "dbrp"}},
      {"action": "read", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "notebooks"}},
      {"action": "write", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "notebooks"}},
      {"action": "read", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "annotations"}},
      {"action": "write", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "annotations"}},
      {"action": "read", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "remotes"}},
      {"action": "write", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "remotes"}},
      {"action": "read", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "replications"}},
      {"action": "write", "resource": {"orgID": "'"$INFLUX_ORG_ID"'", "type": "replications"}}
    ]
  }
'
```

## Database authentication options

Amazon Timestream for InfluxDB supports the following ways to authenticate database users:

- **Password authentication** –
  Your DB instance performs all administration of user accounts.
  You create users, specify passwords, and administer tokens using the
  InfluxDB UI, influx CLI, or InfluxDB API.
- **Token authentication** –
  Your DB instance performs all administration of user accounts. You can create
  users, specify passwords, and administer tokens using your operator token via
  the influx CLI and InfluxDB API.

### Encrypted connections

You can use Secure Socket Layer (SSL) or Transport Layer Security (TLS) from your application to encrypt a connection to a DB instance.
The certificates needed for the TLS handshake between InfluxDB and the applications created and managed by the Kronos service. When the certificate is renewed, the instance is automatically updated with the latest version without requiring any user intervention.

## Working with parameter groups

Database parameters specify how the database is configured. For example, database parameters can specify the amount of resources, such as memory, to allocate to a database.

You manage your database configuration by associating your DB instances with parameter groups. Amazon Timestream for InfluxDB defines parameter groups with default settings. You can also define your own parameter groups with customized settings.

### Overview of parameter groups

A DB parameter group acts as a container for engine configuration values that are applied to one or more DB instances.

###### Topics

- [Default and custom parameter groups](#timestream-for-influx-parameter-groups-overview-default-custom-parameter-groups "#timestream-for-influx-parameter-groups-overview-default-custom-parameter-groups")
- [Creating a DB parameter group](#timestream-for-influx-parameter-groups-creating "#timestream-for-influx-parameter-groups-creating")
- [Static and dynamic DB instance parameters](#timestream-for-influx-parameter-groups-static-dynamic-parameters "#timestream-for-influx-parameter-groups-static-dynamic-parameters")
- [Supported parameters and parameter values](#timestream-for-influx-parameter-groups-overview-supported-parameters "#timestream-for-influx-parameter-groups-overview-supported-parameters")

#### Default and custom parameter groups

DB instances use DB parameter groups. The following sections describe configuring and managing DB instance parameter groups.

#### Creating a DB parameter group

You can create a new DB parameter group using the AWS Management Console, the AWS Command Line Interface, or the Timestream API.

The following limitations apply to the DB parameter group name:

- The name must be 1 to 255 letters, numbers, or hyphens.
- Default parameter group names can include a period, such as `default.InfluxDB.2.7`. However, custom parameter group names can't include a period.
- The first character must be a letter.
- The name cannot start with “dbpg-”
- The name can't end with a hyphen or contain two consecutive hyphens.
- If you create a DB instance without specifying a DB
  parameter group, the DB instance uses the InfluxDB engine defaults.

You can't modify the parameter settings of a default parameter group. Instead, you can do the following:

1. Create a new parameter group.
2. Change the settings of your desired parameters. Not all DB engine parameters in a parameter group are eligible to be modified.
3. Update your DB instance to use the custom parameter group.
   For information about updating a DB instance, see [Updating DB instances](timestream-for-influx-managing-modifying-db.md "timestream-for-influx-managing-modifying-db.md").

###### Note

If you have modified your DB instance to use a custom parameter group, and you start the DB instance, Amazon Timestream for InfluxDB automatically reboots the DB instance as part of the startup process.

Currently, you won’t be able to modify custom parameter groups once they have been created. If you need to change a parameter, it is required that you create a new custom parameter group and assign it to the instances that require this configuration change. If you update an existing DB instance to assign a new parameter group, it will always be applied immediately and reboot your instance.

#### Static and dynamic DB instance parameters

InfluxDB DB instance parameters are always static. They behave as follows:

When you change a static parameter, save the DB parameter group, and assign it to an instance, the parameter change takes effect automatically after the instance is rebooted.

When you associate a new DB parameter group with a DB instance, Timestream applies the modified static parameters only after the DB instance is rebooted. Currently the only option is apply immediately.

For more information about changing the DB parameter group, see [Updating DB instances](timestream-for-influx-managing-modifying-db.md "timestream-for-influx-managing-modifying-db.md").

#### Supported parameters and parameter values

To determine the supported parameters for your DB instance, view the
parameters in the DB parameter group used by the DB instance. For more
information, see [Viewing parameter values for a DB parameter group](#timestream-for-influx-working-with-parameter-groups-viewing "#timestream-for-influx-working-with-parameter-groups-viewing").

For more information about all parameters supported by the open-source
version of InfluxDB, see [InfluxDB configuration options](https://docs.influxdata.com/influxdb/v2/reference/config-options/?t=JSON "https://docs.influxdata.com/influxdb/v2/reference/config-options/?t=JSON"). Currently you will only be
able to modify the following InfluxDB parameters:

| Parameter                                                                                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Default value | Value                                                                                                               | Valid range                                                                                                                                                                          | Note                                                                                                                                                                                 |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [flux-log-enabled](https://docs.influxdata.com/influxdb/v2/reference/config-options/?t=JSON "https://docs.influxdata.com/influxdb/v2/reference/config-options/?t=JSON")                                                                                                                                          | Include option to show detailed logs for Flux<br>queries                                                                                                                                                                                                                                                                                                                                                                                                                                     | FALSE         | Boolean                                                                                                             | N/A                                                                                                                                                                                  |                                                                                                                                                                                      |
| [log-level](https://docs.influxdata.com/influxdb/v2/reference/config-options/#log-level "https://docs.influxdata.com/influxdb/v2/reference/config-options/#log-level")                                                                                                                                           | Log output level. InfluxDB outputs log entries with<br>severity levels greater than or equal to the level<br>specified.                                                                                                                                                                                                                                                                                                                                                                      | info          | debug, info, error                                                                                                  | N/A                                                                                                                                                                                  |                                                                                                                                                                                      |
| [no-tasks](https://docs.influxdata.com/influxdb/v2/reference/config-options/#no-tasks "https://docs.influxdata.com/influxdb/v2/reference/config-options/#no-tasks")                                                                                                                                              | Disable the task scheduler. If problematic tasks<br>prevent InfluxDB from starting, use this option to start<br>InfluxDB without scheduling or executing tasks.                                                                                                                                                                                                                                                                                                                              | FALSE         | Boolean                                                                                                             | N/A                                                                                                                                                                                  |                                                                                                                                                                                      |
| [query-concurrency](https://docs.influxdata.com/influxdb/v2/reference/config-options/#query-concurrency "https://docs.influxdata.com/influxdb/v2/reference/config-options/#query-concurrency")                                                                                                                   | Number of queries allowed to execute concurrently.<br>Setting to 0 allows an unlimited number of concurrent<br>queries.                                                                                                                                                                                                                                                                                                                                                                      | 0             |                                                                                                                     | 0 to 256                                                                                                                                                                             |                                                                                                                                                                                      |
| [query-queue-size](https://docs.influxdata.com/influxdb/v2/reference/config-options/#query-queue-size "https://docs.influxdata.com/influxdb/v2/reference/config-options/#query-queue-size")                                                                                                                      | Maximum number of queries allowed in execution queue.<br>When queue limit is reached, new queries are rejected.<br>Setting to 0 allows an unlimited number of queries in<br>the queue.                                                                                                                                                                                                                                                                                                       | 1,024         |                                                                                                                     | N/A                                                                                                                                                                                  |                                                                                                                                                                                      |
| [tracing-type](https://docs.influxdata.com/influxdb/v2/reference/config-options/#tracing-type "https://docs.influxdata.com/influxdb/v2/reference/config-options/#tracing-type")                                                                                                                                  | Enable tracing in InfluxDB and specifies the tracing<br>type. Tracing is disabled by default.                                                                                                                                                                                                                                                                                                                                                                                                | ""            | log, jaeger                                                                                                         | N/A                                                                                                                                                                                  |                                                                                                                                                                                      |
| [metrics-disabled](https://docs.influxdata.com/influxdb/v2/reference/config-options/#metrics-disabled "https://docs.influxdata.com/influxdb/v2/reference/config-options/#metrics-disabled")                                                                                                                      | Disable the HTTP /metrics endpoint which exposes<br>[internal InfluxDB metrics](https://docs.influxdata.com/influxdb/v2/reference/internals/metrics/ "https://docs.influxdata.com/influxdb/v2/reference/internals/metrics/").                                                                                                                                                                                                                                                                | FALSE         |                                                                                                                     | N/A                                                                                                                                                                                  |                                                                                                                                                                                      |
| [http-idle-timeout](https://docs.influxdata.com/influxdb/v2/reference/config-options/#http-idle-timeout "https://docs.influxdata.com/influxdb/v2/reference/config-options/#http-idle-timeout")                                                                                                                   | Maximum duration the server should keep<br>established connections alive while waiting for new<br>requests. Set to `0` for no<br>timeout.                                                                                                                                                                                                                                                                                                                                                    | 3m0s          | Duration with unit `hours`,<br>`minutes`, `seconds`,<br>`milliseconds`. Example:<br>`durationType=minutes,value=10` | Hours:-Minimum: 0-Maximum:<br>256,205Minutes:-Minimum:<br>0-Maximum:<br>15,372,286Seconds:-Minimum:<br>0-Maximum:<br>922,337,203Milliseconds:-Minimum:<br>0-Maximum: 922,337,203,685 |                                                                                                                                                                                      |
| [http-read-header-timeout](https://docs.influxdata.com/influxdb/v2/reference/config-options/#http-read-header-timeout "https://docs.influxdata.com/influxdb/v2/reference/config-options/#http-read-header-timeout")                                                                                              | Maximum duration the server should try to read<br>HTTP headers for new requests. Set to `0`<br>for no timeout.                                                                                                                                                                                                                                                                                                                                                                               | 10s           | Duration with unit `hours`,<br>`minutes`, `seconds`,<br>`milliseconds`. Example:<br>`durationType=minutes,value=10` | Hours:-Minimum: 0-Maximum:<br>256,205Minutes:-Minimum:<br>0-Maximum:<br>15,372,286Seconds:-Minimum:<br>0-Maximum:<br>922,337,203Milliseconds:-Minimum:<br>0-Maximum: 922,337,203,685 |                                                                                                                                                                                      |
| [http-read-timeout](https://docs.influxdata.com/influxdb/v2/reference/config-options/#http-read-timeout "https://docs.influxdata.com/influxdb/v2/reference/config-options/#http-read-timeout")                                                                                                                   | Maximum duration the server should try to read<br>the entirety of new requests. Set to `0`<br>for no timeout.                                                                                                                                                                                                                                                                                                                                                                                | 0             | Duration with unit `hours`,<br>`minutes`, `seconds`,<br>`milliseconds`. Example:<br>`durationType=minutes,value=10` | Hours:-Minimum: 0-Maximum:<br>256,205Minutes:-Minimum:<br>0-Maximum:<br>15,372,286Seconds:-Minimum:<br>0-Maximum:<br>922,337,203Milliseconds:-Minimum:<br>0-Maximum: 922,337,203,685 |                                                                                                                                                                                      |
| [http-write-timeout](https://docs.influxdata.com/influxdb/v2/reference/config-options/#http-write-timeout "https://docs.influxdata.com/influxdb/v2/reference/config-options/#http-write-timeout")                                                                                                                | Maximum duration the server should spend<br>processing and responding to write requests. Set to<br>`0` for no timeout.                                                                                                                                                                                                                                                                                                                                                                       | 0             | Duration with unit `hours`,<br>`minutes`, `seconds`,<br>`milliseconds`. Example:<br>`durationType=minutes,value=10` | Hours:-Minimum: 0-Maximum:<br>256,205Minutes:-Minimum:<br>0-Maximum:<br>15,372,286Seconds:-Minimum:<br>0-Maximum:<br>922,337,203Milliseconds:-Minimum:<br>0-Maximum: 922,337,203,685 |                                                                                                                                                                                      |
| [influxql-max-select-buckets](https://docs.influxdata.com/influxdb/v2/reference/config-options/#influxql-max-select-buckets "https://docs.influxdata.com/influxdb/v2/reference/config-options/#influxql-max-select-buckets")                                                                                     | Maximum number of group by time buckets a<br>`SELECT` statement can create.<br>`0` allows an unlimited number of<br>buckets.                                                                                                                                                                                                                                                                                                                                                                 | 0             | Long                                                                                                                | Minimum: 0<br>Maximum: 9,223,372,036,854,775,807                                                                                                                                     |                                                                                                                                                                                      |
| [influxql-max-select-point](https://docs.influxdata.com/influxdb/v2/reference/config-options/#influxql-max-select-point "https://docs.influxdata.com/influxdb/v2/reference/config-options/#influxql-max-select-point")                                                                                           | Maximum number of points a `SELECT`<br>statement can process. `0` allows an<br>unlimited number of points. InfluxDB checks the<br>point count every second (so queries exceeding the<br>maximum aren’t immediately aborted).                                                                                                                                                                                                                                                                 | 0             | Long                                                                                                                | Minimum: 0<br>Maximum: 9,223,372,036,854,775,807                                                                                                                                     |                                                                                                                                                                                      |
| [influxql-max-select-series](https://docs.influxdata.com/influxdb/v2/reference/config-options/#influxql-max-select-series "https://docs.influxdata.com/influxdb/v2/reference/config-options/#influxql-max-select-series")                                                                                        | Maximum number of series a `SELECT`<br>statement can return. `0` allows an<br>unlimited number of series.                                                                                                                                                                                                                                                                                                                                                                                    | 0             | Long                                                                                                                | Minimum: 0<br>Maximum: 9,223,372,036,854,775,807                                                                                                                                     |                                                                                                                                                                                      |
| [pprof-disabled](https://docs.influxdata.com/influxdb/v2/reference/config-options/#pprof-disabled "https://docs.influxdata.com/influxdb/v2/reference/config-options/#pprof-disabled")                                                                                                                            | Disable the `/debug/pprof` HTTP<br>endpoint. This endpoint provides runtime profiling<br>data and can be helpful when<br>debugging.                                                                                                                                                                                                                                                                                                                                                          | TRUE          | Boolean                                                                                                             | N/A                                                                                                                                                                                  | While InfluxDB sets pprof-disabled as<br>`false` by default, AWS sets it as<br>`true` by default.                                                                                    |
| [query-initial-memory-bytes](https://docs.influxdata.com/influxdb/v2/reference/config-options/#query-initial-memory-bytes "https://docs.influxdata.com/influxdb/v2/reference/config-options/#query-initial-memory-bytes")                                                                                        | Initial bytes of memory allocated for a<br>query.                                                                                                                                                                                                                                                                                                                                                                                                                                            | 0             | Long                                                                                                                | Minimum: 0Maximum:<br>query-memory-bytes                                                                                                                                             |                                                                                                                                                                                      |
| [query-max-memory-bytes](https://docs.influxdata.com/influxdb/v2/reference/config-options/#influxql-max-select-series "https://docs.influxdata.com/influxdb/v2/reference/config-options/#influxql-max-select-series")                                                                                            | Maximum total bytes of memory allowed for<br>queries.                                                                                                                                                                                                                                                                                                                                                                                                                                        | 0             | Long                                                                                                                | Minimum: 0Maximum:<br>9,223,372,036,854,775,807                                                                                                                                      |                                                                                                                                                                                      |
| [query-memory-bytes](https://docs.influxdata.com/influxdb/v2/reference/config-options/#query-memory-bytes "https://docs.influxdata.com/influxdb/v2/reference/config-options/#query-memory-bytes")                                                                                                                | Specifies the Time to Live (TTL) in minutes for<br>newly created user sessions.                                                                                                                                                                                                                                                                                                                                                                                                              | 0             | Long                                                                                                                | Minimum: 0Maximum:<br>2,147,483,647                                                                                                                                                  | Must be greater than or equal to query-initial-memory-bytes.                                                                                                                         |
| [session-length](https://docs.influxdata.com/influxdb/v2/reference/config-options/#session-length "https://docs.influxdata.com/influxdb/v2/reference/config-options/#session-length")                                                                                                                            | Specifies the Time to Live (TTL) in minutes for<br>newly created user sessions.                                                                                                                                                                                                                                                                                                                                                                                                              | 60            | Integer                                                                                                             | Minimum: 0Maximum:<br>2,880                                                                                                                                                          |                                                                                                                                                                                      |
| [session-renew-disabled](https://docs.influxdata.com/influxdb/v2/reference/config-options/#session-renew-disabled "https://docs.influxdata.com/influxdb/v2/reference/config-options/#session-renew-disabled")                                                                                                    | Disables automatically extending a user’s<br>session TTL on each request. By default, every<br>request sets the session’s expiration time to 5<br>minutes from now. When disabled, sessions expire<br>after the specified [session length](https://docs.influxdata.com/influxdb/v2/reference/config-options/#session-length "https://docs.influxdata.com/influxdb/v2/reference/config-options/#session-length") and the user is redirected<br>to the login page, even if recently<br>active. | FALSE         | Boolean                                                                                                             | N/A                                                                                                                                                                                  |                                                                                                                                                                                      |
| [storage-cache-max-memory-size](https://docs.influxdata.com/influxdb/v2/reference/config-options/#storage-cache-max-memory-size "https://docs.influxdata.com/influxdb/v2/reference/config-options/#storage-cache-max-memory-size")                                                                               | Maximum size (in bytes) a shard’s cache can<br>reach before it starts rejecting<br>writes.                                                                                                                                                                                                                                                                                                                                                                                                   | 1,073,741,824 | Long                                                                                                                | Minimum: 0Maximum:<br>549,755,813,888                                                                                                                                                | Must be lower than instance's total memory<br>capacity.We recommend setting it to<br>below 15 percent of the total memory<br>capacity.                                               |
| [storage-cache-snapshot-memory-size](https://docs.influxdata.com/influxdb/v2/reference/config-options/#storage-cache-snapshot-memory-size "https://docs.influxdata.com/influxdb/v2/reference/config-options/#storage-cache-snapshot-memory-size")                                                                | Size (in bytes) at which the storage engine<br>will snapshot the cache and write it to a TSM file<br>to make more memory available.                                                                                                                                                                                                                                                                                                                                                          | 26,214,400    | Long                                                                                                                | Minimum: 0Maximum:<br>549,755,813,888                                                                                                                                                | Must be lower than<br>storage-cache-max-memory-size.                                                                                                                                 |
| [storage-cache-snapshot-write-cold-duration](https://docs.influxdata.com/influxdb/v2/reference/config-options/#storage-cache-snapshot-write-cold-duration "https://docs.influxdata.com/influxdb/v2/reference/config-options/#storage-cache-snapshot-write-cold-duration")                                        | Duration at which the storage engine will<br>snapshot the cache and write it to a new TSM file if<br>the shard hasn’t received writes or<br>deletes.                                                                                                                                                                                                                                                                                                                                         | 10m0s         | Duration with unit `hours`,<br>`minutes`, `seconds`,<br>`milliseconds`. Example:<br>`durationType=minutes,value=10` | Hours:-Minimum: 0-Maximum:<br>256,205Minutes:-Minimum:<br>0-Maximum:<br>15,372,286Seconds:-Minimum:<br>0-Maximum:<br>922,337,203Milliseconds:-Minimum:<br>0-Maximum: 922,337,203,685 |                                                                                                                                                                                      |
| [storage-compact-full-write-cold-duration](https://docs.influxdata.com/influxdb/v2/reference/config-options/#storage-compact-full-write-cold-duration "https://docs.influxdata.com/influxdb/v2/reference/config-options/#storage-compact-full-write-cold-duration")                                              | Duration at which the storage engine will<br>compact all TSM files in a shard if it hasn’t<br>received writes or deletes.                                                                                                                                                                                                                                                                                                                                                                    | 4h0m0s        | Duration with unit `hours`,<br>`minutes`, `seconds`,<br>`milliseconds`. Example:<br>`durationType=minutes,value=10` | Hours:-Minimum: 0-Maximum:<br>256,205Minutes:-Minimum:<br>0-Maximum:<br>15,372,286Seconds:-Minimum:<br>0-Maximum:<br>922,337,203Milliseconds:-Minimum:<br>0-Maximum: 922,337,203,685 |                                                                                                                                                                                      |
| [storage-compact-throughput-burst](https://docs.influxdata.com/influxdb/v2/reference/config-options/#storage-compact-throughput-burst "https://docs.influxdata.com/influxdb/v2/reference/config-options/#storage-compact-throughput-burst")                                                                      | Rate limit (in bytes per second) that TSM<br>compactions can write to disk.                                                                                                                                                                                                                                                                                                                                                                                                                  | 50,331,648    | Long                                                                                                                | Minimum: 0Maximum:<br>9,223,372,036,854,775,807                                                                                                                                      |                                                                                                                                                                                      |
| [storage-max-concurrent-compactions](https://docs.influxdata.com/influxdb/v2/reference/config-options/#storage-max-concurrent-compactions "https://docs.influxdata.com/influxdb/v2/reference/config-options/#storage-max-concurrent-compactions")                                                                | Maximum number of full and level compactions<br>that can run concurrently. A value of `0`<br>results in 50 percent of `runtime.GOMAXPROCS(0)`<br>used at runtime. Any number greater than zero limits<br>compactions to that value. This setting does not<br>apply to cache snapshotting.                                                                                                                                                                                                    | 0             | Integer                                                                                                             | Minimum: 0Maximum:<br>64                                                                                                                                                             |                                                                                                                                                                                      |
| [storage-max-index-log-file-size](https://docs.influxdata.com/influxdb/v2/reference/config-options/#storage-max-index-log-file-size "https://docs.influxdata.com/influxdb/v2/reference/config-options/#storage-max-index-log-file-size")                                                                         | Size (in bytes) at which an index write-ahead<br>log (WAL) file will compact into an index file.<br>Lower sizes will cause log files to be compacted<br>more quickly and result in lower heap usage at the<br>expense of write throughput.                                                                                                                                                                                                                                                   | 1,048,576     | Long                                                                                                                | Minimum: 0Maximum:<br>9,223,372,036,854,775,807                                                                                                                                      |                                                                                                                                                                                      |
| [storage-no-validate-field-size](https://docs.influxdata.com/influxdb/v2/reference/config-options/#storage-no-validate-field-size "https://docs.influxdata.com/influxdb/v2/reference/config-options/#storage-no-validate-field-size")                                                                            | Skip field size validation on incoming write<br>requests.                                                                                                                                                                                                                                                                                                                                                                                                                                    | FALSE         | Boolean                                                                                                             | N/A                                                                                                                                                                                  |                                                                                                                                                                                      |
| [storage-retention-check-interval](https://docs.influxdata.com/influxdb/v2/reference/config-options/#storage-retention-check-interval "https://docs.influxdata.com/influxdb/v2/reference/config-options/#storage-retention-check-interval")                                                                      | Interval of retention policy enforcement<br>checks.                                                                                                                                                                                                                                                                                                                                                                                                                                          | 30m0s         | Duration with unit `hours`,<br>`minutes`, `seconds`,<br>`milliseconds`. Example:<br>`durationType=minutes,value=10` | N/A                                                                                                                                                                                  | Hours:-Minimum: 0-Maximum:<br>256,205Minutes:-Minimum:<br>0-Maximum:<br>15,372,286Seconds:-Minimum:<br>0-Maximum:<br>922,337,203Milliseconds:-Minimum:<br>0-Maximum: 922,337,203,685 |
| [storage-series-file-max-concurrent-snapshot-compactions](https://docs.influxdata.com/influxdb/v2/reference/config-options/#storage-series-file-max-concurrent-snapshot-compactions "https://docs.influxdata.com/influxdb/v2/reference/config-options/#storage-series-file-max-concurrent-snapshot-compactions") | Maximum number of snapshot compactions that can<br>run concurrently across all series partitions in a<br>database.                                                                                                                                                                                                                                                                                                                                                                           | 0             | Integer                                                                                                             | Minimum: 0Maximum: 64                                                                                                                                                                |                                                                                                                                                                                      |
| [storage-series-id-set-cache-size](https://docs.influxdata.com/influxdb/v2/reference/config-options/#storage-series-id-set-cache-size "https://docs.influxdata.com/influxdb/v2/reference/config-options/#storage-series-id-set-cache-size")                                                                      | Size of the internal cache used in the TSI<br>index to store previously calculated series results.<br>Cached results are returned quickly rather than<br>needing to be recalculated when a subsequent query<br>with the same tag key/value predicate is executed.<br>Setting this value to `0` will disable<br>the cache and may decrease query<br>performance.                                                                                                                              | 100           | Long                                                                                                                | Minimum: 0Maximum:<br>9,223,372,036,854,775,807                                                                                                                                      |                                                                                                                                                                                      |
| [storage-wal-max-concurrent-writes](https://docs.influxdata.com/influxdb/v2/reference/config-options/#storage-wal-max-concurrent-writes "https://docs.influxdata.com/influxdb/v2/reference/config-options/#storage-wal-max-concurrent-writes")                                                                   | Maximum number writes to the WAL directory to<br>attempt at the same time.                                                                                                                                                                                                                                                                                                                                                                                                                   | 0             | Integer                                                                                                             | Minimum: 0Maximum: 256                                                                                                                                                               |                                                                                                                                                                                      |
| [storage-wal-max-write-delay](https://docs.influxdata.com/influxdb/v2/reference/config-options/#storage-wal-max-write-delay "https://docs.influxdata.com/influxdb/v2/reference/config-options/#storage-wal-max-write-delay")                                                                                     | Maximum amount of time a write request to the<br>WAL directory will wait when the the maximum number<br>of concurrent active writes to the WAL directory has<br>been met. Set to `0` to disable the<br>timeout.                                                                                                                                                                                                                                                                              | 10m           | Duration with unit `hours`,<br>`minutes`, `seconds`,<br>`milliseconds`. Example:<br>`durationType=minutes,value=10` | Hours:-Minimum: 0-Maximum:<br>256205Minutes:-Minimum:<br>0-Maximum:<br>15,372,286Seconds:-Minimum:<br>0-Maximum:<br>922,337,203Milliseconds:-Minimum:<br>0-Maximum: 922,337,203,685  |                                                                                                                                                                                      |
| [ui-disabled](https://docs.influxdata.com/influxdb/v2/reference/config-options/#ui-disabled "https://docs.influxdata.com/influxdb/v2/reference/config-options/#ui-disabled")                                                                                                                                     | Disable the InfluxDB user interface (UI). The<br>UI is enabled by default.                                                                                                                                                                                                                                                                                                                                                                                                                   | FALSE         | Boolean                                                                                                             | N/A                                                                                                                                                                                  |                                                                                                                                                                                      |

Improperly setting parameters in a parameter group can have unintended
adverse effects, including degraded performance and system instability.
Always be cautious when modifying database parameters. Test parameter
group setting changes on a test DB instance before applying those
parameter group changes to a production DB instance.

### Working with DB parameter groups

DB instances use DB parameter groups. The following sections describe configuring and managing DB instance parameter groups.

###### Topics

- [Creating a DB parameter group](#timestream-for-influx-working-with-parameter-groups-creating "#timestream-for-influx-working-with-parameter-groups-creating")
- [Associating a DB parameter group with a DB instance](#timestream-for-influx-working-with-parameter-groups-associating "#timestream-for-influx-working-with-parameter-groups-associating")
- [Listing DB parameter groups](#timestream-for-influx-working-with-parameter-groups-listing "#timestream-for-influx-working-with-parameter-groups-listing")
- [Viewing parameter values for a DB parameter group](#timestream-for-influx-working-with-parameter-groups-viewing "#timestream-for-influx-working-with-parameter-groups-viewing")

#### Creating a DB parameter group

###### Using the AWS Management Console

1. Sign in to the AWS Management Console and open the [Amazon Timestream for InfluxDB console](https://console.aws.amazon.com/timestream/ "https://console.aws.amazon.com/timestream/").
2. In the navigation pane, choose **Parameter groups**.
3. Choose **Create parameter group**.
4. In the **Parameter group name** box, enter the name of the new DB parameter group.
5. In the **Description** box, enter a description for the new DB parameter group.
6. Choose the parameters to modify and apply the desired values. For more information on supported parameters, see
   [Supported parameters and parameter values](#timestream-for-influx-parameter-groups-overview-supported-parameters "#timestream-for-influx-parameter-groups-overview-supported-parameters").
7. Choose **Create parameter group**.

###### Using the AWS Command Line Interface

- To create a DB parameter group by using the AWS CLI, call the
  `create-db-parameter-group` command with the following parameters:

```
--db-parameter-group-name <value>
--description <value>
--endpoint_url <value>
--region <value>
--parameters (list) (string)

```

###### Example

For information about each setting, see [Settings for DB instances](timestream-for-influx-configuring.md#timestream-for-influx-configuring-create-db-settings "timestream-for-influx-configuring.md#timestream-for-influx-configuring-create-db-settings").
This example uses default engine configs.

```
aws timestream-influxdb create-db-parameter-group
    --db-parameter-group-name YOUR_PARAM_GROUP_NAME \
    --endpoint-url YOUR_ENDPOINT \
    --region YOUR_REGION \
    --parameters "InfluxDBv2={logLevel=debug,queryConcurrency=10,metricsDisabled=true}" \" \
    --debug
```

#### Associating a DB parameter group with a DB instance

You can create your own DB parameter groups with customized settings. You can associate a DB parameter group with a DB instance using the AWS Management Console, the AWS Command Line Interface, or the
Timestream for InfluxDB API. You can do so when you create or modify a DB instance.

For information about creating a DB parameter group, see [Creating a DB parameter group](#timestream-for-influx-working-with-parameter-groups-creating "#timestream-for-influx-working-with-parameter-groups-creating").
For information about creating a DB instance,
see [Creating a DB instance](timestream-for-influx-configuring.md#timestream-for-influx-configuring-create-db "timestream-for-influx-configuring.md#timestream-for-influx-configuring-create-db").
For information about modifying a DB instance, see [Updating DB instances](timestream-for-influx-managing-modifying-db.md "timestream-for-influx-managing-modifying-db.md").

###### Note

When you associate a new DB parameter group with a DB instance, the modified static parameters are applied only after the DB instance is rebooted. Currently, only apply immediately is supported. Timestream for InfluxDB only support static parameters.

###### Using the AWS Management Console

1. Sign in to the AWS Management Console and open the [Amazon Timestream for InfluxDB console](https://console.aws.amazon.com/timestream/ "https://console.aws.amazon.com/timestream/").
2. In the navigation pane, choose **InfluxDB Databases**, and then choose the DB instance that you want to modify.
3. Choose **Update**. The **Update DB instance** page appears.
4. Change the **DB parameter group** setting.
5. Choose **Continue** and check the summary of modifications.
6. Currently only **Apply immediately** is supported.
   This option can cause an outage in some cases since it will reboot your DB instance.
7. On the confirmation page, review your changes. If they are correct, choose
   **Update DB instance** to save your changes and apply them.
   Or choose **Back** to edit your changes or **Cancel** to cancel your changes.

**Using the AWS Command Line Interface**

For Linux, macOS, or Unix:

```
aws timestream-influxdb update-db-instance
--identifier YOUR_DB_INSTANCE_ID \
--region YOUR_REGION \
--db-parameter-group-identifier YOUR_PARAM_GROUP_ID \
--log-delivery-configuration "{\"s3Configuration\": {\"bucketName\": \"${LOGGING_BUCKET}\", \"enabled\": false }}"
```

For Windows:

```
aws timestream-influxdb update-db-instance
--identifier YOUR_DB_INSTANCE_ID ^
--region YOUR_REGION ^
--db-parameter-group-identifier YOUR_PARAM_GROUP_ID ^
--log-delivery-configuration "{\"s3Configuration\": {\"bucketName\": \"${LOGGING_BUCKET}\", \"enabled\": false }}"


```

#### Listing DB parameter groups

You can list the DB parameter groups you've created for your AWS account.

###### Using the AWS Management Console

1. Sign in to the AWS Management Console and open the [Amazon Timestream for InfluxDB console](https://console.aws.amazon.com/timestream/ "https://console.aws.amazon.com/timestream/").
2. In the navigation pane, choose **Parameter groups**.
3. The DB parameter groups appear in a list.

**Using the AWS Command Line Interface**

To list all DB parameter groups for an AWS account, use the AWS Command Line Interface
`list-db-parameter-groups` command.

```
aws timestream-influxdb list-db-parameter-groups --region `region`
```

To return a specific DB parameter groups for an AWS account, use the AWS Command Line Interface
`get-db-parameter-group` command.

```
aws timestream-influxdb get-db-parameter-group --region `region` --identifier `identifier`
```

#### Viewing parameter values for a DB parameter group

You can get a list of all parameters in a DB parameter group and their values.

###### Using the AWS Management Console

1. Sign in to the AWS Management Console and open the [Amazon Timestream for InfluxDB console](https://console.aws.amazon.com/timestream/ "https://console.aws.amazon.com/timestream/").
2. In the navigation pane, choose **Parameter groups**.
3. The DB parameter groups appear in a list.
4. Choose the name of the parameter group to see its list of parameters.

**Using the AWS Command Line Interface**

To view the parameter values for a DB parameter group, use the AWS Command Line Interface `get-db-parameter-group` command. Replace `parameter-group-identifier` with your own information.

```
get-db-parameter-group --identifier `parameter-group-identifier`
```

**Using the API**

To view the parameter values for a DB parameter group, use the Timestream API
`GetDbParameterGroup` command. Replace `parameter-group-identifier` with your own information.

```
GetDbParameterGroup `parameter-group-identifier`
```
