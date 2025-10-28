For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Database authentication with Amazon Timestream for InfluxDB

Amazon Timestream for InfluxDB supports two ways to authenticate database users.

Password and access Token database authentication use different methods of authenticating to the database. Therefore, a specific user can log in to a database using only one authentication method. In both cases InfluxDB performs all administration of user accounts and API tokens.

## Password authentication

During the InfluxDB DB instance creation process, you created an organization, user and password. The user has permissions to manage everything in your Timestream for InfluxDB DB instance. With this username and password combination you will be able to LogIn into your instance using the InfluxUI and
also use the InfluxCLI to generate an operator token.

An operator token is required to create users, delete buckets , organizations etc. For more information, see [Database authentication options](timestream-for-influx-db-connecting.md#timestream-for-influx-db-connecting-authentication-options "timestream-for-influx-db-connecting.md#timestream-for-influx-db-connecting-authentication-options").

## API tokens

InfluxDB API tokens ensure secure interaction between InfluxDB and external tools such as clients or applications. An API token belongs to a specific user and identifies InfluxDB permissions within the user’s organization.

There are three types of API tokens in InfluxDB:

- Operator Token: Grants full read and write access to all organizations and all organization resources in InfluxDB OSS 2.x. Some operations, for example, retrieving the server configuration, require operator permissions. To create an operator token manually with the InfluxDB UI, `api/v2` API, or Influx CLI after the setup process is completed,
  you must use an existing operator token or your username and password. To create a new operator token without using an existing one,
  see the [influxd recovery auth](https://docs.influxdata.com/influxdb/v2/reference/cli/influxd/recovery/auth/ "https://docs.influxdata.com/influxdb/v2/reference/cli/influxd/recovery/auth/") CLI.

###### Important

Because operator tokens have full read and write access to all organizations in the database, we recommend [creating an
All-Access token](https://docs.influxdata.com/influxdb/v2/admin/tokens/create-token/ "https://docs.influxdata.com/influxdb/v2/admin/tokens/create-token/") for each organization and using those to manage InfluxDB.
This helps to prevent accidental interactions across organizations.

- All-Access API Token: Grants full read and write access to all resources in an organization.
- Read/Write Tokens: Grants read access, write access, or both to specific buckets in an organization.

All InfluxDb tokens are long lived tokens with no set expiration date, so it is not recommended to use your
operator or all access tokens to sent monitoring data from your clients or Telegraf agents neither to embed them in your
dashboarding applications. For these applications create read/write tokens with just the necessary permissions to get
the job done. Fo more information on how to create influxDB token, see [Create a
token](https://docs.influxdata.com/influxdb/v2/admin/tokens/create-token/ "https://docs.influxdata.com/influxdb/v2/admin/tokens/create-token/").

## Secrets

InfluxDB operator tokens are generated on instance setup; other kinds of tokens, such as all-access and read/write tokens, can be created using the [Influx CLI](https://docs.influxdata.com/influxdb/v2/tools/influx-cli/ "https://docs.influxdata.com/influxdb/v2/tools/influx-cli/"), Influx v2 API, or the Timestream for InfluxDB Multi-user rotation function. See [Manage API tokens](https://docs.influxdata.com/influxdb/v2/admin/tokens/ "https://docs.influxdata.com/influxdb/v2/admin/tokens/")
for how to generate, view, assign, and delete tokens.

We recommend that you rotate Timestream for InfluxDB tokens often using AWS Secrets Manager and store tokens via environment variables. See [Use Tokens](https://docs.influxdata.com/influxdb/cloud/admin/tokens/use-tokens/#add-a-token-to-a-cli-request "https://docs.influxdata.com/influxdb/cloud/admin/tokens/use-tokens/#add-a-token-to-a-cli-request") for token usage in environment variables and [Rotating the secret](timestream-for-influx-security-db-secrets.md#timestream-for-influx-security-db-secrets-rotation "timestream-for-influx-security-db-secrets.md#timestream-for-influx-security-db-secrets-rotation") for how to rotate Timestream for InfluxDB users and tokens.

**See also:**

- [Infrastructure security in Amazon Timestream for InfluxDB](infrastructure-security-influxdb.md "infrastructure-security-influxdb.md")
- [Security best practices for Timestream for InfluxDB](security-best-practices.md "security-best-practices.md")
