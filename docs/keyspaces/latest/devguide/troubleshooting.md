# Troubleshooting connection errors in Amazon Keyspaces

Having trouble connecting? Here are some common issues and how to resolve them.

## Errors connecting to

an Amazon Keyspaces endpoint

Failed connections and connection errors can result in different error messages. The
following section covers the most common scenarios.

###### Topics

- [I can't connect to Amazon Keyspaces with
  cqlsh](#troubleshooting.connection.cqlsh "#troubleshooting.connection.cqlsh")
- [I can't connect to Amazon Keyspaces using a Cassandra client driver](#troubleshooting.connection.driver "#troubleshooting.connection.driver")

### I can't connect to Amazon Keyspaces with

cqlsh

**You're trying to connect to an Amazon Keyspaces endpoint using cqlsh and
the connection fails with a `Connection error`.**

If you try to connect to an Amazon Keyspaces table and cqlsh hasn't been configured properly, the
connection fails. The following section provides examples of the most common configuration issues that result in connection errors when
you're trying to establish a connection using cqlsh.

###### Note

If you're trying to connect to Amazon Keyspaces from a VPC, additional permissions are required. To
successfully configure a connection using VPC endpoints, follow the steps in the
[Tutorial: Connect to Amazon Keyspaces using an interface VPC
endpoint](vpc-endpoints-tutorial.md "vpc-endpoints-tutorial.md").

**You're trying to connect to Amazon Keyspaces using cqlsh, but you get a
connection `timed out` error.**

This might be the case if you didn't supply the correct port, which results in the following error.

```
`# cqlsh cassandra.us-east-1.amazonaws.com `9140` -u "USERNAME" -p "PASSWORD" --ssl
Connection error: ('Unable to connect to any servers', {'3.234.248.199': error(None, "Tried connecting to [('3.234.248.199', 9140)]. Last error: timed out")})`
```

To resolve this issue, verify that you're using port 9142 for the connection.

**You're trying to connect to Amazon Keyspaces using cqlsh, but you get a `Name or service not known` error.**

This might be the case if you used an endpoint that is misspelled or doesn't exist. In
the following example, the name of the endpoint is misspelled.

```
`# cqlsh `cassandra.us-east-1.amazon.com` 9142 -u "USERNAME" -p "PASSWORD" --ssl
Traceback (most recent call last):
 File "/usr/bin/cqlsh.py", line 2458, in >module>
 main(*read_options(sys.argv[1:], os.environ))
 File "/usr/bin/cqlsh.py", line 2436, in main
 encoding=options.encoding)
 File "/usr/bin/cqlsh.py", line 484, in __init__
 load_balancing_policy=WhiteListRoundRobinPolicy([self.hostname]),
 File "/usr/share/cassandra/lib/cassandra-driver-internal-only-3.11.0-bb96859b.zip/cassandra-driver-3.11.0-bb96859b/cassandra/policies.py", line 417, in __init__
socket.gaierror: [Errno -2] Name or service not known`
```

To resolve this issue when you're using public endpoints to connect, select an
available endpoint from [Service endpoints for Amazon Keyspaces](programmatic.md "programmatic.md"), and verify that the
name of the endpoint doesn't have any errors. If you're using VPC endpoints to connect,
verify that the VPC endpoint information is correct in your cqlsh configuration.

**You're trying to connect to Amazon Keyspaces using cqlsh, but you receive
an `OperationTimedOut` error.**

Amazon Keyspaces requires that SSL is enabled for connections to ensure strong security. The SSL parameter might be missing if you receive the following error.

```
`# cqlsh cassandra.us-east-1.amazonaws.com -u "USERNAME" -p "PASSWORD"
Connection error: ('Unable to connect to any servers', {'3.234.248.192': OperationTimedOut('errors=Timed out creating connection (5 seconds), last_host=None',)})
#`
```

To resolve this issue, add the following flag to the cqlsh connection command.

```
--ssl
```

**You're trying to connect to Amazon Keyspaces using cqlsh, and you receive a `SSL transport factory requires a valid certfile to be specified` error.**

In this case, the path to the SSL/TLS certificate is missing, which results in the following error.

```
`# cat .cassandra/cqlshrc
[connection]
port = 9142
factory = cqlshlib.ssl.ssl_transport_factory
#


# cqlsh cassandra.us-east-1.amazonaws.com -u "USERNAME" -p "PASSWORD" --ssl
Validation is enabled; SSL transport factory requires a valid certfile to be specified. Please provide path to the certfile in [ssl] section as 'certfile' option in /root/.cassandra/cqlshrc (or use [certfiles] section) or set SSL_CERTFILE environment variable.
#`
```

To resolve this issue, add the path to the certfile on your computer. For more
information, see [How to manually configure
cqlsh connections for TLS](programmatic.md#encrypt_using_tls "programmatic.md#encrypt_using_tls").

```
certfile =  `path_to_file`/`keyspaces-bundle.pem`
```

**You're trying to connect to Amazon Keyspaces using cqlsh, but you receive a `No such file or directory` error.**

This might be the case if the path to the certificate file on your computer is wrong, which results in the following error.

```
`# cat .cassandra/cqlshrc
[connection]
port = 9142
factory = cqlshlib.ssl.ssl_transport_factory

[ssl]
validate = true
certfile = /root/`wrong_path`/`keyspaces-bundle.pem`
#



# cqlsh cassandra.us-east-1.amazonaws.com -u "USERNAME" -p "PASSWORD" --ssl
Connection error: ('Unable to connect to any servers', {'3.234.248.192': IOError(2, 'No such file or directory')})
#`
```

To resolve this issue, verify that the path to the certfile on your computer is correct. For more
information, see [How to manually configure
cqlsh connections for TLS](programmatic.md#encrypt_using_tls "programmatic.md#encrypt_using_tls").

**You're trying to connect to Amazon Keyspaces using cqlsh, but you receive a `[X509] PEM lib` error.**

This might be the case if the SSL/TLS
certificate `pem` file is not
valid, which results in the following error.

```
`# cqlsh cassandra.us-east-1.amazonaws.com -u "USERNAME" -p "PASSWORD" --ssl
Connection error: ('Unable to connect to any servers', {'3.234.248.241': error(185090057, u"Tried connecting to [('3.234.248.241', 9142)]. Last error: [X509] PEM lib (_ssl.c:3063)")})
#`
```

To resolve this issue make sure that you downloaded the required digital certificates.
For more
information, see [How to manually configure
cqlsh connections for TLS](programmatic.md#encrypt_using_tls "programmatic.md#encrypt_using_tls").

**You're trying to connect to Amazon Keyspaces using cqlsh, but you receive
an `unknown` SSL error.**

This might be the case if the SSL/TLS
certificate `pem` file is empty, which results in the following error.

```
`# cqlsh cassandra.us-east-1.amazonaws.com -u "USERNAME" -p "PASSWORD" --ssl
Connection error: ('Unable to connect to any servers', {'3.234.248.220': error(0, u"Tried connecting to [('3.234.248.220', 9142)]. Last error: unknown error (_ssl.c:3063)")})
#`
```

To resolve this issue make sure that you downloaded the required digital certificates.

You can confirm this using the steps in the following topic [How to manually configure
cqlsh connections for TLS](programmatic.md#encrypt_using_tls "programmatic.md#encrypt_using_tls").

**You're trying to connect to Amazon Keyspaces using cqlsh, but you receive a `SSL: CERTIFICATE_VERIFY_FAILED` error.**

This might be the case if the SSL/TLS
certificate file could not be verified, which results in the following error.

```
`Connection error: ('Unable to connect to any servers', {'3.234.248.223': error(1, u"Tried connecting to [('3.234.248.223', 9142)]. Last error: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:727)")})`
```

To resolve this issue make sure that you downloaded the required digital certificates.

You can confirm this using the steps in the following topic [How to manually configure
cqlsh connections for TLS](programmatic.md#encrypt_using_tls "programmatic.md#encrypt_using_tls").

**You're trying to connect to Amazon Keyspaces using cqlsh, but you're receiving a `Last error: timed out` error.**

This might be the case if you didn't
configure an outbound rule for Amazon Keyspaces in your Amazon EC2 security group, which results in the following error.

```
`# cqlsh cassandra.us-east-1.amazonaws.com 9142 -u "USERNAME" -p "PASSWORD" --ssl
Connection error: ('Unable to connect to any servers', {'3.234.248.206': error(None, "Tried connecting to [('3.234.248.206', 9142)]. Last error: timed out")})
#`
```

To confirm that this issue is caused by the configuration of the Amazon EC2 instance and not `cqlsh`,
you can try to connect to your keyspace using
the AWS CLI, for example with the following command.

```
aws keyspaces list-tables --keyspace-name '`my_keyspace`'
```

If this command also times out, the Amazon EC2 instance is not correctly configured.

To confirm that you have sufficient permissions to access Amazon Keyspaces, you can use the AWS CloudShell to connect with `cqlsh`. If that
connections gets established, you need to configure the Amazon EC2 instance.

To resolve this issue, confirm that your Amazon EC2 instance has an outbound rule that allows traffic to Amazon Keyspaces. If that is not the case, you need
to create a new security group for the EC2 instance, and add a rule that allows outbound
traffic to Amazon Keyspaces resources. To update the outbound rule to allow traffic to Amazon Keyspaces, choose **CQLSH/CASSANDRA**
from the **Type** drop-down menu.

After creating the new security group with the outbound traffic rule, you need to add it to the instance.
Select the instance and then choose **Actions**, then **Security**, and then **Change
security groups**. Add the new security group with the outbound rule, but make sure that the default group also remains available.

For more information about how to view and edit EC2 outbound rules, see [Add
rules to a security group in the Amazon EC2 User Guide](../../../AWSEC2/latest/UserGuide/working-with-security-groups.md#adding-security-group-rule "../../../AWSEC2/latest/UserGuide/working-with-security-groups.md#adding-security-group-rule").

**You're trying to connect to Amazon Keyspaces using cqlsh, but you receive
an `Unauthorized` error.**

This might be the case if you're
missing Amazon Keyspaces permissions in the IAM user policy, which results in the following error.

```
`# cqlsh cassandra.us-east-1.amazonaws.com 9142 -u "testuser-at-12345678910" -p "PASSWORD" --ssl
Connection error: ('Unable to connect to any servers', {'3.234.248.241': AuthenticationFailed('Failed to authenticate to 3.234.248.241: Error from server: code=2100 [Unauthorized] message="User arn:aws:iam::12345678910:user/testuser has no permissions."',)})
#`
```

To resolve this issue, ensure that the IAM user `testuser-at-12345678910` has
permissions to access Amazon Keyspaces. For examples of IAM policies that grant access to Amazon Keyspaces,
see [Amazon Keyspaces identity-based
policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

For troubleshooting guidance that's specific to IAM access, see [Troubleshooting Amazon Keyspaces identity
and access](security_iam_troubleshoot.md "security_iam_troubleshoot.md").

**You're trying to connect to Amazon Keyspaces using cqlsh, but you receive a `Bad credentials` error.**

This might be the case if the user name
or password is wrong, which results in the following error.

```
`# cqlsh cassandra.us-east-1.amazonaws.com 9142 -u `"USERNAME"` -p `"PASSWORD"` --ssl
Connection error: ('Unable to connect to any servers', {'3.234.248.248': AuthenticationFailed('Failed to authenticate to 3.234.248.248: Error from server: code=0100 [Bad credentials] message="Provided username USERNAME and/or password are incorrect"',)})
#`
```

To resolve this issue, verify that the `USERNAME` and
`PASSWORD` in your code match the user name and password
you obtained when you generated [service-specific
credentials](programmatic.credentials.md "programmatic.credentials.md").

###### Important

If you continue to see errors when trying to connect with cqlsh, rerun the command
with the `--debug` option and include the detailed output when contacting
Support.

###

I can't connect to Amazon Keyspaces using a Cassandra client driver

The following sections shows the most common errors when connecting with a Cassandra client driver.

**You're trying to connect to an Amazon Keyspaces table using the DataStax Java driver, but
you receive an `NodeUnavailableException` error.**

If the connection on which the request is attempted is broken, it results in the following error.

```
`[com.datastax.oss.driver.api.core.NodeUnavailableException: No connection was available to Node(endPoint=vpce-22ff22f2f22222fff-aa1bb234.cassandra.us-west-2.vpce.amazonaws.com/11.1.1111.222:9142, hostId=1a23456b-c77d-8888-9d99-146cb22d6ef6, hashCode=123ca4567)]`
```

To resolve this issue, find the heartbeat value and lower it to 30 seconds if it's higher.

```
advanced.heartbeat.interval = 30 seconds
```

Then look for the associated time out and ensure the value is set to at least 5 seconds.

```
advanced.connection.init-query-timeout = 5 seconds
```

**You're trying to connect to an Amazon Keyspaces table using a driver and the SigV4 plugin, but
you receive an `AttributeError` error.**

If the credentials are not correctly configured, it results in the following error.

```
`cassandra.cluster.NoHostAvailable: (‘Unable to connect to any servers’,
 {‘44.234.22.154:9142’: AttributeError(“‘NoneType’ object has no attribute ‘access_key’“)})`
```

To resolve this issue, verify that you're passing the credentials associated with your
IAM user or role when using the SigV4 plugin. The SigV4 plugin requires the
following credentials.

- `AWS_ACCESS_KEY_ID` – Specifies an AWS access key associated with an IAM user or role.
- `AWS_SECRET_ACCESS_KEY`– Specifies the secret key associated with the access key. This is
  essentially the "password" for the access key.

To learn more about access keys and the SigV4 plugin, see [Create and configure AWS credentials for Amazon Keyspaces](access.md "access.md").

**You're trying to connect to an Amazon Keyspaces table using a driver, but
you receive a `PartialCredentialsError` error.**

If the `AWS_SECRET_ACCESS_KEY` is missing, it can result in the following error.

```
`cassandra.cluster.NoHostAvailable: (‘Unable to connect to any servers’, {‘44.234.22.153:9142’:
 PartialCredentialsError(‘Partial credentials found in config-file, missing: aws_secret_access_key’)})`
```

To resolve this issue, verify that you're passing both the `AWS_ACCESS_KEY_ID` and the `AWS_SECRET_ACCESS_KEY` when using the SigV4 plugin.
To learn more about access keys and the SigV4 plugin, see [Create and configure AWS credentials for Amazon Keyspaces](access.md "access.md").

**You're trying to connect to an Amazon Keyspaces table using a driver, but
you receive an `Invalid signature` error.**

This might be the case if any of the components required for the signature are wrong or not correctly defined for the session.

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_DEFAULT_REGION`

The following error is an examples of invalid access keys.

```
`cassandra.cluster.NoHostAvailable: (‘Unable to connect to any servers’, {‘11.234.11.234:9142’:
 AuthenticationFailed(‘Failed to authenticate to 11.234.11.234:9142: Error from server: code=0100
 [Bad credentials] message=“Authentication failure: Invalid signature”’)})`
```

To resolve this issue, verify that the access keys and the AWS Region have been correctly configured for the SigV4 plugin to access Amazon Keyspaces.
To learn more about access keys and the SigV4 plugin, see [Create and configure AWS credentials for Amazon Keyspaces](access.md "access.md").

#### My VPC endpoint connection doesn't work properly

**You're trying to connect to Amazon Keyspaces using VPC endpoints, but
you're receiving token map errors or you are experiencing low throughput.**

This might be the case if the VPC endpoint connection isn't correctly configured.

To resolve these issues, verify the following configuration details. To follow a
step-by-step tutorial to learn how to configure a connection over interface VPC
endpoints for Amazon Keyspaces see [Tutorial: Connect to Amazon Keyspaces using an interface VPC
endpoint](vpc-endpoints-tutorial.md "vpc-endpoints-tutorial.md").

1. Confirm that the IAM entity used to connect to Amazon Keyspaces has read/write access to the user table
   and read access to the system tables as shown in the following example.

```
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Effect":"Allow",
         "Action":[
            "cassandra:Select",
            "cassandra:Modify"
         ],
         "Resource":[
            "arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/mykeyspace/table/mytable",
            "arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/system*"
         ]
      }
   ]
}
```

2. Confirm that the IAM entity used to connect to Amazon Keyspaces has the required read permissions to
   access the VPC endpoint information on your Amazon EC2 instance as shown in the following example.

```
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Sid":"ListVPCEndpoints",
         "Effect":"Allow",
         "Action":[
            "ec2:DescribeNetworkInterfaces",
            "ec2:DescribeVpcEndpoints"
         ],
         "Resource":"*"
      }
   ]
}
```

###### Note

The managed policies `AmazonKeyspacesReadOnlyAccess_v2` and
`AmazonKeyspacesFullAccess` include the required permissions to let Amazon Keyspaces
access the Amazon EC2 instance to read information about available interface VPC endpoints.

For more information about VPC endpoints, see [Using interface VPC endpoints for
Amazon Keyspaces](vpc-endpoints.md#using-interface-vpc-endpoints "vpc-endpoints.md#using-interface-vpc-endpoints") 3. Confirm that the SSL configuration of the Java driver sets hostname validation to false as shown
in this example.

```
hostname-validation = false
```

For more information about driver configuration, see [Step 2: Configure the
driver](using_java_driver.md#java_tutorial.driverconfiguration "using_java_driver.md#java_tutorial.driverconfiguration"). 4. To confirm that the VPC endpoint has been configured correctly, you can run
the following statement from _within_ your VPC.

###### Note

You can't use your local developer environment or the Amazon Keyspaces CQL editor to confirm this configuration, because they use the public endpoint.

```
SELECT peer FROM system.peers;
```

The output should look similar to this example and return between 2 to 6 nodes with private IPv4 addresses when connecting
from an IPv4 network, depending on your VPC setup and AWS Region.

```
`peer
---------------
 192.0.2.0.15
 192.0.2.0.24
 192.0.2.0.13
 192.0.2.0.7
 192.0.2.0.8

(5 rows)`
```

#### I can't connect using `cassandra-stress`

**You're trying to connect to Amazon Keyspaces using the
`cassandra-stress` command, but you're receiving an `SSL
 context` error.**

This happens if you try to connect to Amazon Keyspaces, but you don't have the trustStore setup correctly. Amazon Keyspaces requires the use of Transport Layer Security (TLS) to help secure connections with clients.

In this case, you see the following error.

```
`Error creating the initializing the SSL Context`
```

To resolve this issue, follow the instructions to set up a trustStore as shown in this topic [Before you
begin](using_java_driver.md#using_java_driver.BeforeYouBegin "using_java_driver.md#using_java_driver.BeforeYouBegin").

Once the trustStore is setup, you should be able to connect with the following command.

```
./cassandra-stress user profile=./profile.yaml n=100 "ops(insert=1,select=1)" cl=LOCAL_QUORUM -node "`cassandra.eu-north-1.amazonaws.com`" -port native=9142 -transport ssl-alg="PKIX" truststore="./cassandra_truststore.jks" truststore-password="`trustStore_pw`" -mode native cql3 user="`user_name`" password="`password`"
```

#### I can't connect using IAM

identities

**You're trying to connect to an Amazon Keyspaces table using an IAM
identity, but you're receiving an `Unauthorized` error.**

This happens if you try to connect to an Amazon Keyspaces table using an IAM identity (for example, an IAM
user) without implementing the policy and giving the user the required permissions first.

In this case, you see the following error.

```
`Connection error: ('Unable to connect to any servers', {'3.234.248.202': AuthenticationFailed('Failed to authenticate to 3.234.248.202:
Error from server: code=2100 [Unauthorized] message="User arn:aws:iam::1234567890123:user/testuser has no permissions."',)})`
```

To resolve this issue, verify the permissions of the IAM user. To connect with a standard driver, a user must have at least `SELECT`
access to the system tables, because most drivers read the system keyspaces/tables when they establish the connection.

For example IAM policies that grant access to Amazon Keyspaces system and user tables, see
[Accessing
Amazon Keyspaces tables](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-access-one-table "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-access-one-table").

To review the troubleshooting section specific to IAM, see [Troubleshooting Amazon Keyspaces identity
and access](security_iam_troubleshoot.md "security_iam_troubleshoot.md").

#### I'm trying to import data with cqlsh and the

connection to my Amazon Keyspaces table is lost

**You're trying to upload data to Amazon Keyspaces with cqlsh, but you're
receiving connection errors.**

The connection to Amazon Keyspaces fails after the cqlsh client receives three consecutive errors of any type from the server.
The cqlsh client fails with the following message.

```
`Failed to import 1 rows: NoHostAvailable - , will retry later, attempt 3 of 100`
```

To resolve this error, you need to make sure that the data to be imported matches the
table schema in Amazon Keyspaces. Review the import file for parsing errors. You can try using a
single row of data by using an INSERT statement to isolate the error.

The client automatically attempts to reestablish the connection.
