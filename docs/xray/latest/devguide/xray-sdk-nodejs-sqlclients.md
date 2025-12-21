# Tracing SQL queries with the X-Ray SDK for Node.js

###### Note

X-Ray SDK/Daemon Maintenance Notice – On February 25th, 2026, the AWS X-Ray SDKs/Daemon will enter maintenance mode, where AWS will limit X-Ray SDK and Daemon releases to address security issues only. For more information on the support timeline, see
[X-Ray SDK and Daemon Support timeline](xray-sdk-daemon-timeline.md "xray-sdk-daemon-timeline.md"). We recommend to migrate to OpenTelemetry. For more information on migrating to OpenTelemetry, see [Migrating from X-Ray instrumentation to OpenTelemetry instrumentation](xray-sdk-migration.md "xray-sdk-migration.md") .

Instrument SQL database queries by wrapping your SQL client in the corresponding X-Ray SDK for Node.js client
method.

- **PostgreSQL** – `AWSXRay.capturePostgres()`

```
var AWSXRay = require('aws-xray-sdk');
`var pg = AWSXRay.capturePostgres(`require('pg')`)`;
var client = new pg.Client();
```

- **MySQL** – `AWSXRay.captureMySQL()`

```
var AWSXRay = require('aws-xray-sdk');
`var mysql = AWSXRay.captureMySQL(`require('mysql')`)`;
...
var connection = mysql.createConnection(config);
```

When you use an instrumented client to make SQL queries, the X-Ray SDK for Node.js records information about the
connection and query in a subsegment.

## Including additional data in SQL subsegments

You can add additional information to subsegments generated for SQL queries, as long as it's mapped to an
allow-listed SQL field. For example, to record the sanitized SQL query string in a subsegment, you can add it directly
to the subsegment's SQL object.

###### Example Assign SQL to subsegment

```
    const queryString = 'SELECT * FROM `MyTable`';
connection.query(queryString, ...);

// Retrieve the most recently created subsegment
const subs = AWSXRay.getSegment().subsegments;

if (subs & & subs.length > 0) {
  var sqlSub = subs[subs.length - 1];
  sqlSub.sql.sanitized_query = queryString;
}

```

For a full list of allow-listed SQL fields, see [SQL Queries](xray-api-segmentdocuments.md#api-segmentdocuments-sql "xray-api-segmentdocuments.md#api-segmentdocuments-sql") in the
_AWS X-Ray Developer Guide_.
