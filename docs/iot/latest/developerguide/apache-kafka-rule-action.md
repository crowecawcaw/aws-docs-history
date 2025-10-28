# Apache Kafka

The Apache Kafka (Kafka) action sends messages directly to your [Amazon Managed Streaming for Apache Kafka](../../../msk/latest/developerguide/what-is-msk.md "../../../msk/latest/developerguide/what-is-msk.md") (Amazon MSK), Apache Kafka clusters managed by third-party
providers such as [Confluent Cloud](https://www.confluent.io/ "https://www.confluent.io/"), or
self-managed Apache Kafka clusters. With Kafka rule action, you can route your IoT
data to Kafka clusters. This enables you to build high-performance data pipelines
for various purposes, such as streaming analytics, data integration, visualization,
and mission-critical business applications.

###### Note

This topic assumes familiarity with the Apache Kafka platform and related
concepts. For more information about Apache Kafka, see [Apache Kafka](https://kafka.apache.org/ "https://kafka.apache.org/"). [MSK
Serverless](../../../msk/latest/developerguide/serverless.md "../../../msk/latest/developerguide/serverless.md") is not supported. MSK Serverless clusters can only be
done via IAM authentication, which Apache Kafka rule action doesn't
currently support. For more information about how to configure AWS IoT Core with
Confluent, see [Leveraging Confluent and AWS to Solve IoT Device and Data Management
Challenges](https://aws.amazon.com/blogs/apn/leveraging-confluent-and-aws-to-solve-iot-device-and-data-management-challenges/ "https://aws.amazon.com/blogs/apn/leveraging-confluent-and-aws-to-solve-iot-device-and-data-management-challenges/").

## Requirements

This rule action has the following requirements:

- An IAM role that AWS IoT can assume to perform the `ec2:CreateNetworkInterface`,
  `ec2:DescribeNetworkInterfaces`,
  `ec2:CreateNetworkInterfacePermission`,
  `ec2:DeleteNetworkInterface`,
  `ec2:DescribeSubnets`, `ec2:DescribeVpcs`,
  `ec2:DescribeVpcAttribute`, and
  `ec2:DescribeSecurityGroups` operations. This role
  creates and manages elastic network interfaces to your Amazon Virtual Private Cloud to
  reach your Kafka broker. For more information, see [Granting an AWS IoT rule the access it requires](iot-create-role.md "iot-create-role.md").

In the AWS IoT console, you can choose or create a role to allow
AWS IoT Core to perform this rule action.

For more information about network interfaces, see [Elastic network
interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in the _Amazon EC2 User
Guide_.

The policy attached to the role that you specify should look like the
following example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface",
 "ec2:DescribeNetworkInterfaces",
 "ec2:CreateNetworkInterfacePermission",
 "ec2:DeleteNetworkInterface",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs",
 "ec2:DescribeVpcAttribute",
 "ec2:DescribeSecurityGroups"
 ],
 "Resource": "*"
 }
 ]
}`

```

- If you use AWS Secrets Manager to store the credentials required to connect to
  your Kafka broker, you must create an IAM role that AWS IoT Core can
  assume to perform the `secretsmanager:GetSecretValue` and
  `secretsmanager:DescribeSecret` operations.

The policy attached to the role that you specify should look like the
following example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue",
 "secretsmanager:DescribeSecret"
 ],
 "Resource": [
 "arn:aws:secretsmanager:`us-east-1`:`123456789012`:secret:kafka_client_truststore-*",
 "arn:aws:secretsmanager:`us-east-1`:`123456789012`:secret:kafka_keytab-*"
 ]
 }
 ]
}`

```

- You can run your Apache Kafka clusters inside Amazon Virtual Private Cloud (Amazon VPC). You
  must create an Amazon VPC destination and use an NAT gateway in your subnets
  to forward messages from AWS IoT to a public Kafka cluster. The AWS IoT
  rules engine creates a network interface in each of the subnets listed
  in the VPC destination to route traffic directly to the VPC. When you
  create a VPC destination, the AWS IoT rules engine automatically creates a
  VPC rule action. For more information about VPC rule actions, see [Virtual private cloud (VPC)
  destinations](vpc-rule-action.md "vpc-rule-action.md").
- If you use a customer managed AWS KMS key (KMS key) to encrypt
  data at rest, the service must have permission to use the KMS key on
  the caller's behalf. For more information, see [Amazon MSK encryption](../../../msk/latest/developerguide/msk-encryption.md "../../../msk/latest/developerguide/msk-encryption.md") in
  the _Amazon Managed Streaming for Apache Kafka Developer Guide_.

## Parameters

When you create an AWS IoT rule with this action, you must specify the following information:

destinationArn

The Amazon Resource Name (ARN) of the VPC destination. For
information about creating a VPC destination, see [Virtual private cloud (VPC)
destinations](vpc-rule-action.md "vpc-rule-action.md").

topic

The Kafka topic for messages to be sent to the Kafka
broker.

You can substitute this field using a substitution template. For
more information, see [Substitution templates](iot-substitution-templates.md "iot-substitution-templates.md").

key (optional)

The Kafka message key.

You can substitute this field using a substitution template. For
more information, see [Substitution templates](iot-substitution-templates.md "iot-substitution-templates.md").

headers (optional)

The list of Kafka headers that you specify. Each header is a
key-value pair that you can specify when you create a Kafka action.
You can use these headers to route data from IoT clients to
downstream Kafka clusters without modifying your message
payload.

You can substitute this field using a substitution template. To
understand how to pass an inline Rule's function as a substitution
template in Kafka Action's header, see [Examples](#apache-kafka-rule-action-examples "#apache-kafka-rule-action-examples"). For
more information, see [Substitution templates](iot-substitution-templates.md "iot-substitution-templates.md").

###### Note

Headers in binary format are not supported.

partition (optional)

The Kafka message partition.

You can substitute this field using a substitution template. For
more information, see [Substitution templates](iot-substitution-templates.md "iot-substitution-templates.md").

clientProperties

An object that defines the properties of the Apache Kafka
producer client.

acks (optional)

The number of acknowledgments the producer requires
the server to have received before considering a request
complete.

If you specify 0 as the value, the producer won't wait
for any acknowledgment from the server. If the server
doesn't receive the message, the producer won't retry to
send the message.

Valid values: `-1`, `0`,
`1`, `all`. The default value
is `1`.

bootstrap.servers

A list of host and port pairs (for example,
`host1:port1`, `host2:port2`)
used to establish the initial connection to your Kafka
cluster.

compression.type (optional)

The compression type for all data generated by the
producer.

Valid values: `none`, `gzip`,
`snappy`, `lz4`,
`zstd`. The default value is
`none`.

security.protocol

The security protocol used to attach to your Kafka
broker.

Valid values: `SSL`, `SASL_SSL`.
The default value is `SSL`.

key.serializer

Specifies how to turn the key objects that you provide
with the`ProducerRecord` into bytes.

Valid value: `StringSerializer`.

value.serializer

Specifies how to turn value objects that you provide
with the `ProducerRecord` into bytes.

Valid value: `ByteBufferSerializer`.

ssl.truststore

The truststore file in base64 format or the location
of the truststore file in [AWS Secrets Manager](../../../secretsmanager/latest/userguide.md "../../../secretsmanager/latest/userguide.md"). This value isn't required if
your truststore is trusted by Amazon certificate
authorities (CA).

This field supports substitution templates. If you use
Secrets Manager to store the credentials required to connect
to your Kafka broker, you can use the
`get_secret` SQL function to retrieve the
value for this field. For more information about
substitution templates, see [Substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"). For more
information about the `get_secret` SQL
function, see [get_secret(secretId, secretType, key, roleArn)](iot-sql-functions.md#iot-sql-function-get-secret "iot-sql-functions.md#iot-sql-function-get-secret"). If the
truststore is in the form of a file, use the
`SecretBinary` parameter. If the
truststore is in the form of a string, use the
`SecretString` parameter.

The maximum size of this value is 65 KB.

ssl.truststore.password

The password for the truststore. This value is
required only if you've created a password for the
truststore.

ssl.keystore

The keystore file. This value is required when you
specify `SSL` as the value for
`security.protocol`.

This field supports substitution templates. Use
Secrets Manager to store the credentials required to connect
to your Kafka broker. To retrieve the value for this
field, use the `get_secret` SQL function. For
more information about substitution templates, see [Substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"). For more
information about the `get_secret` SQL
function, see [get_secret(secretId, secretType, key, roleArn)](iot-sql-functions.md#iot-sql-function-get-secret "iot-sql-functions.md#iot-sql-function-get-secret"). Use the
`SecretBinary` parameter.

ssl.keystore.password

The store password for the keystore file. This value
is required if you specify a value for
`ssl.keystore`.

The value of this field can be plaintext . This field
also supports substitution templates. Use Secrets Manager to
store the credentials required to connect to your Kafka
broker. To retrieve the value for this field, use the
`get_secret` SQL function. For more
information about substitution templates, see [Substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"). For more
information about the `get_secret` SQL
function, see [get_secret(secretId, secretType, key, roleArn)](iot-sql-functions.md#iot-sql-function-get-secret "iot-sql-functions.md#iot-sql-function-get-secret"). Use the
`SecretString` parameter.

ssl.key.password

The password of the private key in your keystore
file.

This field supports substitution templates. Use
Secrets Manager to store the credentials required to connect
to your Kafka broker. To retrieve the value for this
field, use the `get_secret` SQL function. For
more information about substitution templates, see [Substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"). For more
information about the `get_secret` SQL
function, see [get_secret(secretId, secretType, key, roleArn)](iot-sql-functions.md#iot-sql-function-get-secret "iot-sql-functions.md#iot-sql-function-get-secret"). Use the
`SecretString` parameter.

sasl.mechanism

The security mechanism used to connect to your Kafka
broker. This value is required when you specify
`SASL_SSL` for
`security.protocol`.

Valid values: `PLAIN`,
`SCRAM-SHA-512`,
`GSSAPI`.

###### Note

`SCRAM-SHA-512` is the only supported
security mechanism in the cn-north-1,
cn-northwest-1, us-gov-east-1, and us-gov-west-1
Regions.

sasl.plain.username

The username used to retrieve the secret string from
Secrets Manager. This value is required when you specify
`SASL_SSL` for
`security.protocol` and
`PLAIN` for
`sasl.mechanism`.

sasl.plain.password

The password used to retrieve the secret string from
Secrets Manager. This value is required when you specify
`SASL_SSL` for
`security.protocol` and
`PLAIN` for
`sasl.mechanism`.

sasl.scram.username

The username used to retrieve the secret string from
Secrets Manager. This value is required when you specify
`SASL_SSL` for
`security.protocol` and
`SCRAM-SHA-512` for
`sasl.mechanism`.

sasl.scram.password

The password used to retrieve the secret string from
Secrets Manager. This value is required when you specify
`SASL_SSL` for
`security.protocol` and
`SCRAM-SHA-512` for
`sasl.mechanism`.

sasl.kerberos.keytab

The keytab file for Kerberos authentication in
Secrets Manager. This value is required when you specify
`SASL_SSL` for
`security.protocol` and
`GSSAPI` for
`sasl.mechanism`.

This field supports substitution templates. Use
Secrets Manager to store the credentials required to connect
to your Kafka broker. To retrieve the value for this
field, use the `get_secret` SQL function. For
more information about substitution templates, see [Substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"). For more
information about the `get_secret` SQL
function, see [get_secret(secretId, secretType, key, roleArn)](iot-sql-functions.md#iot-sql-function-get-secret "iot-sql-functions.md#iot-sql-function-get-secret"). Use the
`SecretBinary` parameter.

sasl.kerberos.service.name

The Kerberos principal name under which Apache Kafka
runs. This value is required when you specify
`SASL_SSL` for
`security.protocol` and
`GSSAPI` for
`sasl.mechanism`.

sasl.kerberos.krb5.kdc

The hostname of the key distribution center (KDC) to
which your Apache Kafka producer client connects. This
value is required when you specify `SASL_SSL`
for `security.protocol` and
`GSSAPI` for
`sasl.mechanism`.

sasl.kerberos.krb5.realm

The realm to which your Apache Kafka producer client
connects. This value is required when you specify
`SASL_SSL` for
`security.protocol` and
`GSSAPI` for
`sasl.mechanism`.

sasl.kerberos.principal

The unique Kerberos identity to which Kerberos can
assign tickets to access Kerberos-aware services. This
value is required when you specify `SASL_SSL`
for `security.protocol` and
`GSSAPI` for
`sasl.mechanism`.

## Examples

The following JSON example defines an Apache Kafka action in an AWS IoT rule.
The following example passes the [sourceIp()](iot-sql-functions.md#iot-function-sourceip "iot-sql-functions.md#iot-function-sourceip") inline function as a [substitution template](iot-substitution-templates.md "iot-substitution-templates.md") in the Kafka Action header.

```
{
	"topicRulePayload": {
		"sql": "SELECT * FROM 'some/topic'",
		"ruleDisabled": false,
		"awsIotSqlVersion": "2016-03-23",
		"actions": [
			{
				"kafka": {
					"destinationArn": "arn:aws:iot:region:123456789012:ruledestination/vpc/VPCDestinationARN",
					"topic": "TopicName",
					"clientProperties": {
						"bootstrap.servers": "kafka.com:9092",
						"security.protocol": "SASL_SSL",
						"ssl.truststore": "${get_secret('kafka_client_truststore', 'SecretBinary','arn:aws:iam::123456789012:role/kafka-get-secret-role-name')}",
						"ssl.truststore.password": "kafka password",
						"sasl.mechanism": "GSSAPI",
						"sasl.kerberos.service.name": "kafka",
						"sasl.kerberos.krb5.kdc": "kerberosdns.com",
						"sasl.kerberos.keytab": "${get_secret('kafka_keytab','SecretBinary', 'arn:aws:iam::123456789012:role/kafka-get-secret-role-name')}",
						"sasl.kerberos.krb5.realm": "KERBEROSREALM",
						"sasl.kerberos.principal": "kafka-keytab/kafka-keytab.com"
					},
					"headers": [
						{
							"key": "static_header_key",
							"value": "static_header_value"
						},
						{
							"key": "substitutable_header_key",
							"value": "${value_from_payload}"
						},
						{
							"key": "source_ip",
							"value": "${sourceIp()}"
						}
					]
				}
			}
		]
	}
}
```

**Important notes about your Kerberos
setup**

- Your key distribution center (KDC) must be resolvable through private
  Domain Name System (DNS) within your target VPC. One possible approach
  is to add the KDC DNS entry to a private hosted zone. For more
  information about this approach, see [Working with private
  hosted zones](../../../Route53/latest/DeveloperGuide/hosted-zones-private.md "../../../Route53/latest/DeveloperGuide/hosted-zones-private.md").
- Each VPC must have DNS resolution enabled. For more information, see
  [Using DNS with your
  VPC](../../../vpc/latest/userguide/vpc-dns.md "../../../vpc/latest/userguide/vpc-dns.md").
- Network interface security groups and instance-level security groups
  in the VPC destination must allow traffic from within your VPC on the
  following ports.
  - TCP traffic on the bootstrap broker listener port (often 9092,
    but must be within the 9000–9100 range)
  - TCP and UDP traffic on port 88 for the KDC

- `SCRAM-SHA-512` is the only supported security mechanism in
  the cn-north-1, cn-northwest-1, us-gov-east-1, and us-gov-west-1
  Regions.
