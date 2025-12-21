# AWS X-Ray SDK for Python

###### Note

X-Ray SDK/Daemon Maintenance Notice – On February 25th, 2026, the AWS X-Ray SDKs/Daemon will enter maintenance mode, where AWS will limit X-Ray SDK and Daemon releases to address security issues only. For more information on the support timeline, see
[X-Ray SDK and Daemon Support timeline](xray-sdk-daemon-timeline.md "xray-sdk-daemon-timeline.md"). We recommend to migrate to OpenTelemetry. For more information on migrating to OpenTelemetry, see [Migrating from X-Ray instrumentation to OpenTelemetry instrumentation](xray-sdk-migration.md "xray-sdk-migration.md") .

The X-Ray SDK for Python is a library for Python web applications that provides classes and
methods for generating and sending trace data to the X-Ray daemon. Trace data includes
information about incoming HTTP requests served by the application, and calls that the
application makes to downstream services using the AWS SDK, HTTP clients, or an SQL database
connector. You can also create segments manually and add debug information in annotations and
metadata.

You can download the SDK with `pip`.

```
$ `pip install aws-xray-sdk`
```

###### Note

The X-Ray SDK for Python is an open source project. You can follow the project and submit
issues and pull requests on GitHub: [github.com/aws/aws-xray-sdk-python](https://github.com/aws/aws-xray-sdk-python "https://github.com/aws/aws-xray-sdk-python")

If you use Django or Flask, start by [adding the
SDK middleware to your application](xray-sdk-python-middleware.md "xray-sdk-python-middleware.md") to trace incoming requests. The middleware creates a
[segment](xray-concepts.md#xray-concepts-segments "xray-concepts.md#xray-concepts-segments") for each traced request, and completes
the segment when the response is sent. While the segment is open, you can use the SDK client's
methods to add information to the segment and create subsegments to trace downstream calls. The
SDK also automatically records exceptions that your application throws while the segment is
open. For other applications, you can [create
segments manually](xray-sdk-python-middleware.md#xray-sdk-python-middleware-manual "xray-sdk-python-middleware.md#xray-sdk-python-middleware-manual").

For Lambda functions called by an instrumented application or service, Lambda
reads the [tracing header](xray-concepts.md#xray-concepts-tracingheader "xray-concepts.md#xray-concepts-tracingheader") and traces sampled
requests automatically. For other functions, you can [configure Lambda](xray-services-lambda.md "xray-services-lambda.md") to sample and trace incoming requests. In either case, Lambda creates
the segment and provides it to the X-Ray SDK.

###### Note

On Lambda, the X-Ray SDK is optional. If you don't use it in your function,
your service map will still include a node for the Lambda service, and one for each Lambda function.
By adding the SDK, you can instrument your function code to add subsegments to the function
segment recorded by Lambda. See [AWS Lambda and AWS X-Ray](xray-services-lambda.md "xray-services-lambda.md")
for more information.

See [Worker](scorekeep-lambda.md#scorekeep-lambda-worker "scorekeep-lambda.md#scorekeep-lambda-worker") for a example Python function instrumented in
Lambda.

Next, use the X-Ray SDK for Python to instrument downstream calls by [patching your application's libraries](xray-sdk-python-patching.md "xray-sdk-python-patching.md"). The SDK
supports the following libraries.

###### Supported Libraries

- `botocore`,
  `boto3` –
  Instrument AWS SDK for Python (Boto) clients.
- `pynamodb` –
  Instrument PynamoDB's version of the Amazon DynamoDB client.
- `aiobotocore`,
  `aioboto3` –
  Instrument [asyncio](https://docs.python.org/3/library/asyncio.html "https://docs.python.org/3/library/asyncio.html")-integrated versions of SDK for Python clients.
- `requests`,
  `aiohttp` –
  Instrument high-level HTTP clients.
- `httplib`,
  [`http.client`](https://docs.python.org/3/library/http.client.html "https://docs.python.org/3/library/http.client.html") – Instrument low-level HTTP clients and the higher
  level libraries that use them.
- `sqlite3`
  – Instrument SQLite clients.
- `mysql-connector-python` – Instrument MySQL clients.
- `pg8000` – Instrument Pure-Python PostgreSQL interface.
- `psycopg2` – Instrument PostgreSQL database adapter.
- `pymongo` – Instrument MongoDB clients.
- `pymysql` – Instrument PyMySQL based clients for MySQL and MariaDB.
  Whenever your application makes calls to AWS, an SQL database, or other HTTP services, the
  SDK records information about the call in a subsegment. AWS services and the resources that
  you access within the services appear as downstream nodes on the trace map to help you
  identify errors and throttling issues on individual connections.

After you start using the SDK, customize its behavior by [configuring the recorder and middleware](xray-sdk-python-configuration.md "xray-sdk-python-configuration.md"). You can add plugins to record data about the compute resources
running your application, customize sampling behavior by defining sampling rules, and set the log level to see more
or less information from the SDK in your application logs.

Record additional information about requests and the work that your application does in
[annotations and metadata](xray-sdk-python-segment.md "xray-sdk-python-segment.md"). Annotations are
simple key-value pairs that are indexed for use with [filter
expressions](xray-console-filters.md "xray-console-filters.md"), so that you can search for traces that contain specific data. Metadata
entries are less restrictive and can record entire objects and arrays — anything that can
be serialized into JSON.

###### Annotations and Metadata

Annotations and metadata are arbitrary text that you add to segments with the X-Ray SDK.
Annotations are indexed for use with filter expressions. Metadata are not indexed, but can be
viewed in the raw segment with the X-Ray console or API. Anyone that you grant read access to
X-Ray can view this data.

When you have a lot of instrumented clients in your code, a single request segment can
contain a large number of subsegments, one for each call made with an instrumented client. You
can organize and group subsegments by wrapping client calls in [custom subsegments](xray-sdk-python-subsegments.md "xray-sdk-python-subsegments.md"). You can create a custom
subsegment for an entire function or any section of code. You can then you can record metadata
and annotations on the subsegment instead of writing everything on the parent segment.

For reference documentation for the SDK's classes and methods, see the [AWS X-Ray SDK for Python API
Reference](../../../xray-sdk-for-python/latest/reference.md "../../../xray-sdk-for-python/latest/reference.md").

## Requirements

The X-Ray SDK for Python supports the following language and library versions.

- **Python** – 2.7, 3.4, and newer
- **Django** – 1.10 and newer
- **Flask** – 0.10 and newer
- **aiohttp** – 2.3.0 and newer
- **AWS SDK for Python (Boto)** – 1.4.0 and newer
- **botocore** – 1.5.0 and newer
- **enum** – 0.4.7 and newer, for Python versions 3.4.0 and older
- **jsonpickle** – 1.0.0 and newer
- **setuptools** – 40.6.3 and newer
- **wrapt** – 1.11.0 and newer

## Dependency management

The X-Ray SDK for Python is available from `pip`.

- **Package** – `aws-xray-sdk`

Add the SDK as a dependency in your `requirements.txt` file.

###### Example requirements.txt

```
`aws-xray-sdk==2.4.2`
boto3==1.4.4
botocore==1.5.55
Django==1.11.3
```

If you use Elastic Beanstalk to deploy your application, Elastic Beanstalk installs all of the packages in
`requirements.txt` automatically.
