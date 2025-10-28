# Examples using LDAP with Amazon EMR

Once you [provision an EMR cluster that uses
LDAP](ldap-setup-launch.md "ldap-setup-launch.md") integration, you can provide your LDAP credentials to any [supported application](ldap-considerations.md#ldap-considerations-apps "ldap-considerations.md#ldap-considerations-apps") through its built-in
username and password authentication mechanism. This page shows some examples.

## Using LDAP authentication with Apache

Hive

###### Example - Apache Hive

The following example command starts an Apache Hive session through
HiveServer2 and Beeline:

```
beeline -u "jdbc:hive2://`$HOSTNAME`:10000/default;ssl=true;sslTrustStore=$`TRUSTSTORE_PATH`;trustStorePassword=$`TRUSTSTORE_PASS`"  -n `LDAP_USERNAME` -p `LDAP_PASSWORD`
```

## Using LDAP authentication with Apache

Livy

###### Example - Apache Livy

The following example command starts a Livy session through cURL. Replace
`ENCODED-KEYPAIR` with a
Base64-encoded string for `username:password`.

```
curl -X POST --data '{"proxyUser":"`LDAP_USERNAME`","kind": "pyspark"}' -H "Content-Type: application/json" -H "Authorization: Basic `ENCODED-KEYPAIR`" `DNS_OF_PRIMARY_NODE`:8998/sessions

```

## Using LDAP authentication with Presto

###### Example - Presto

The following example command starts a Presto session through the Presto
CLI:

```
presto-cli --user "`LDAP_USERNAME`" --password --catalog hive
```

After you run this command, enter the LDAP password at the prompt.

## Using LDAP authentication with Trino

###### Example - Trino

The following example command starts a Trino session through the Trino
CLI:

```
trino-cli --user "`LDAP_USERNAME`" --password --catalog hive
```

After you run this command, enter the LDAP password at the prompt.

## Using LDAP authentication with Hue

You can access Hue UI through an SSH tunnel that you create on the cluster, or you
can set a proxy server to publicly broadcast the connection to Hue. Because Hue
doesn't run in HTTPS mode by default, we recommend that you use an additional
encryption layer to ensure that communication between clients and the Hue UI is
encrypted with HTTPS. This reduces the chance that you might accidentally expose
user credentials in plain text.

To use the Hue UI, open the Hue UI in your browser and enter your LDAP username
password to log in. If the credentials are correct, Hue logs you in and uses your
identity to authenticate you with all supported applications.

## Using SSH for password authentication and

Kerberos tickets for other applications

###### Important

We don't recommend that you use password authentication to SSH into an
EMR cluster.

You can use your LDAP credentials to SSH to an EMR cluster. To do this, set the
`EnableSSHLogin` configuration to `true` in the Amazon EMR
security configuration that you use to start the cluster. Then, use the following
command to SSH to the cluster once its been launched:

```
ssh `username`@`EMR_PRIMARY_DNS_NAME`
```

After you run this command, enter the LDAP password at the prompt.

Amazon EMR includes an on-cluster script that allows users to generate a Kerberos
keytab file and ticket to use with supported applications that don't accept LDAP
credentials directly. Some of these applications include `spark-submit`,
Spark SQL, and PySpark.

Run `ldap-kinit` and follow the prompts. If the authentication
succeeds, the Kerberos keytab file appears in your home directory with a valid
Kerberos ticket. Use the Kerberos ticket to run applications as you would on any
Kerberized environment.
