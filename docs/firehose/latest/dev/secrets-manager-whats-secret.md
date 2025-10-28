# Understand secrets

A secret can be a password, a set of credentials such as a user name and password, an
OAuth token, or other secret information that you store in an encrypted form in Secrets Manager.

For each destination, you must specify the secret key-value pair in the correct JSON
format as shown in the following section. Amazon Data Firehose will fail to connect to your
destination if your secret doesn't have the correct JSON format as per the destination.

**Format of secret for databases such as MySQL and
PostgreSQL**

```
{
    "username":  "<`username`>",
    "password":  "<`password`>"
}
```

**Format of secret for Amazon Redshift Provisioned cluster and Amazon Redshift Serverless
workgroup**

```
{
    "username":  "<`username`>",
    "password":  "<`password`>"
}
```

**Format of secret for Splunk**

```
{
    "hec_token":  "<`hec token`>"
}
```

**Format of secret for Snowflake**

```
{
    "user":  "<`snowflake-username`>",
    "private_key":  "<`snowflake-private-key`>", // without the beginning and ending private key, remove all spaces and newlines
    "key_passphrase":  "<`snowflake-private-key-passphrase`>" // optional
}
```

**Format of secret for HTTP endpoint, Coralogix, Datadog,
Dynatrace, Elastic, Honeycomb, LogicMonitor, Logz.io, MongoDB Cloud, and New
Relic**

```
{
    "api_key":  "<`apikey`>"
}
```
