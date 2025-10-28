# Amazon Managed Streaming for Apache Kafka topic as a source in EventBridge Pipes

You can use EventBridge Pipes to receive records from an [Amazon Managed Streaming for Apache Kafka (Amazon MSK)](../../../msk/latest/developerguide/what-is-msk.md "../../../msk/latest/developerguide/what-is-msk.md") topic. You can optionally filter or enhance these records before
sending them to one of the available destinations for processing. There are settings specific to
Amazon MSK that you can choose when setting up a pipe. EventBridge Pipes maintains the order of the records
from the message broker when sending that data to the destination.

Amazon MSK is a fully managed service that you can use to build and run applications that use
Apache Kafka to process streaming data. Amazon MSK simplifies the setup, scaling, and management of
clusters running Apache Kafka. With Amazon MSK, you can configure your application for multiple
Availability Zones and for security with AWS Identity and Access Management (IAM). Amazon MSK supports multiple open-source
versions of Kafka.

Amazon MSK as an source operates similarly to using Amazon Simple Queue Service (Amazon SQS) or Amazon Kinesis. EventBridge
internally polls for new messages from the source and then synchronously invokes the target.
EventBridge reads the messages in batches and provides these to your function as an event payload. The
maximum batch size is configurable. (The default is 100 messages.)

For Apache Kafka-based sources, EventBridge supports processing control parameters, such as batching
windows and batch size.

EventBridge reads the messages sequentially for each partition. After EventBridge processes each batch, it
commits the offsets of the messages in that batch. If the pipe's target returns an error for any
of the messages in a batch, EventBridge retries the entire batch of messages until processing succeeds
or the messages expire.

EventBridge sends the batch of messages in the event when it invokes the target. The event payload
contains an array of messages. Each array item contains details of the Amazon MSK topic and partition
identifier, together with a timestamp and a base64-encoded message.

**Example events**

The following sample event shows the information that is received by the pipe. You can use
this event to create and filter your event patterns, or for to define input transformation. Not
all of the fields can be filtered. For more information about which fields you can filter, see
[Event filtering in Amazon EventBridge Pipes](eb-pipes-event-filtering.md "eb-pipes-event-filtering.md").

```
[
  {
    "eventSource": "aws:kafka",
    "eventSourceArn": "arn:aws:kafka:sa-east-1:123456789012:cluster/vpc-2priv-2pub/751d2973-a626-431c-9d4e-d7975eb44dd7-2",
    "eventSourceKey": "mytopic-0",
    "topic": "mytopic",
    "partition": "0",
    "offset": 15,
    "timestamp": 1545084650987,
    "timestampType": "CREATE_TIME",
    "key":"abcDEFghiJKLmnoPQRstuVWXyz1234==",
    "value":"SGVsbG8sIHRoaXMgaXMgYSB0ZXN0Lg==",
    "headers": [
      {
        "headerKey": [
          104,
          101,
          97,
          100,
          101,
          114,
          86,
          97,
          108,
          117,
          101
        ]
      }
    ]
  }
]
```

## Polling and stream starting position

Be aware that stream source polling during pipe creation and updates is eventually consistent.

- During pipe creation, it may take several minutes to start polling events from the stream.
- During pipe updates to the source polling configuration, it may take
  several minutes to stop and restart polling events from the stream.

This means that if you specify `LATEST` as the starting position for the stream,
the pipe could miss events sent during pipe creation or updates.
To ensure no events are missed, specify the stream starting position as `TRIM_HORIZON`.

## MSK cluster authentication

EventBridge needs permission to access the Amazon MSK cluster, retrieve records, and perform other
tasks. Amazon MSK supports several options for controlling client access to the MSK cluster. For
more information about which authentication method is used when, see [How EventBridge chooses a bootstrap broker](#pipes-msk-bootstrap-brokers "#pipes-msk-bootstrap-brokers").

###### Cluster access options

- [Unauthenticated access](#pipes-msk-permissions-none "#pipes-msk-permissions-none")
- [SASL/SCRAM authentication](#pipes-msk-permissions-add-secret "#pipes-msk-permissions-add-secret")
- [IAM role-based authentication](#pipes-msk-permissions-iam-policy "#pipes-msk-permissions-iam-policy")
- [Mutual TLS authentication](#pipes-msk-permissions-mTLS "#pipes-msk-permissions-mTLS")
- [Configuring the mTLS secret](#smaa-auth-secret "#smaa-auth-secret")
- [How EventBridge chooses a bootstrap broker](#pipes-msk-bootstrap-brokers "#pipes-msk-bootstrap-brokers")

### Unauthenticated access

We recommend only using unauthenticated access for development. Unauthenticated access
will only work if IAM role-based authentication is disabled for the cluster.

### SASL/SCRAM authentication

Amazon MSK supports Simple Authentication and Security Layer/Salted Challenge Response
Authentication Mechanism (SASL/SCRAM) authentication with Transport Layer Security (TLS)
encryption. For EventBridge to connect to the cluster, you store the authentication credentials
(sign-in credentials) in an AWS Secrets Manager secret.

For more information about using Secrets Manager, see [User name and password authentication with AWS Secrets Manager](../../../msk/latest/developerguide/msk-password.md "../../../msk/latest/developerguide/msk-password.md") in the
_Amazon Managed Streaming for Apache Kafka Developer Guide_.

Amazon MSK doesn't support SASL/PLAIN authentication.

### IAM role-based authentication

You can use IAM to authenticate the identity of clients that connect to the MSK
cluster. If IAM authentication is active on your MSK cluster, and you don't provide a
secret for authentication, EventBridge automatically defaults to using IAM authentication. To
create and deploy IAM user or role-based policies, use the IAM console or API. For more
information, see [IAM access
control](../../../msk/latest/developerguide/iam-access-control.md "../../../msk/latest/developerguide/iam-access-control.md") in the _Amazon Managed Streaming for Apache Kafka Developer Guide_.

To allow EventBridge to connect to the MSK cluster, read records, and perform other required
actions, add the following permissions to your pipes's execution role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kafka-cluster:Connect",
 "kafka-cluster:DescribeGroup",
 "kafka-cluster:AlterGroup",
 "kafka-cluster:DescribeTopic",
 "kafka-cluster:ReadData",
 "kafka-cluster:DescribeClusterDynamicConfiguration"
 ],
 "Resource": [
 "arn:aws:kafka:`us-east-1`:`123456789012`:cluster/`cluster-name`/`cluster-uuid`",
 "arn:aws:kafka:`us-east-1`:`123456789012`:topic/`cluster-name`/`cluster-uuid`/`topic-name`",
 "arn:aws:kafka:`us-east-1`:`123456789012`:group/`cluster-name`/`cluster-uuid`/`consumer-group-id`"
 ]
 }
 ]
}`

```

You can scope these permissions to a specific cluster, topic, and group. For more
information, see the [Amazon MSK
Kafka actions](../../../msk/latest/developerguide/iam-access-control.md#kafka-actions "../../../msk/latest/developerguide/iam-access-control.md#kafka-actions") in the _Amazon Managed Streaming for Apache Kafka Developer Guide_.

### Mutual TLS authentication

Mutual TLS (mTLS) provides two-way authentication between the client and server. The
client sends a certificate to the server for the server to verify the client, and the server
sends a certificate to the client for the client to verify the server.

For Amazon MSK, EventBridge acts as the client. You configure a client certificate (as a secret in
Secrets Manager) to authenticate EventBridge with the brokers in your MSK cluster. The client
certificate must be signed by a certificate authority (CA) in the server's trust store. The
MSK cluster sends a server certificate to EventBridge to authenticate the brokers with EventBridge. The
server certificate must be signed by a CA that's in the AWS trust store.

Amazon MSK doesn't support self-signed server certificates, because all brokers in Amazon MSK use
[public certificates](../../../msk/latest/developerguide/msk-encryption.md "../../../msk/latest/developerguide/msk-encryption.md") signed by [Amazon Trust Services CAs](https://www.amazontrust.com/repository/ "https://www.amazontrust.com/repository/"), which
EventBridge trusts by default.

For more information about mTLS for Amazon MSK, see [Mutual TLS Authentication](../../../msk/latest/developerguide/msk-authentication.md "../../../msk/latest/developerguide/msk-authentication.md") in the
_Amazon Managed Streaming for Apache Kafka Developer Guide_.

### Configuring the mTLS secret

The CLIENT_CERTIFICATE_TLS_AUTH secret requires a certificate field and a private key
field. For an encrypted private key, the secret requires a private key password. Both the
certificate and private key must be in PEM format.

###### Note

EventBridge supports the [PBES1](https://datatracker.ietf.org/doc/html/rfc2898/#section-6.1 "https://datatracker.ietf.org/doc/html/rfc2898/#section-6.1") (but not
PBES2) private key encryption algorithms.

The certificate field must contain a list of certificates, beginning with the client
certificate, followed by any intermediate certificates, and ending with the root
certificate. Each certificate must start on a new line with the following structure:

```
-----BEGIN CERTIFICATE-----
        <certificate contents>
-----END CERTIFICATE-----
```

Secrets Manager supports secrets up to 65,536 bytes, which is enough space for long certificate
chains.

The private key must be in [PKCS #8](https://datatracker.ietf.org/doc/html/rfc5208 "https://datatracker.ietf.org/doc/html/rfc5208") format, with the following structure:

```
-----BEGIN PRIVATE KEY-----
         <private key contents>
-----END PRIVATE KEY-----
```

For an encrypted private key, use the following structure:

```
-----BEGIN ENCRYPTED PRIVATE KEY-----
          <private key contents>
-----END ENCRYPTED PRIVATE KEY-----
```

The following example shows the contents of a secret for mTLS authentication using an
encrypted private key. For an encrypted private key, you include the private key password in
the secret.

```
{
 "privateKeyPassword": "testpassword",
 "certificate": "-----BEGIN CERTIFICATE-----
MIIE5DCCAsygAwIBAgIRAPJdwaFaNRrytHBto0j5BA0wDQYJKoZIhvcNAQELBQAw
...
j0Lh4/+1HfgyE2KlmII36dg4IMzNjAFEBZiCRoPimO40s1cRqtFHXoal0QQbIlxk
cmUuiAii9R0=
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
MIIFgjCCA2qgAwIBAgIQdjNZd6uFf9hbNC5RdfmHrzANBgkqhkiG9w0BAQsFADBb
...
rQoiowbbk5wXCheYSANQIfTZ6weQTgiCHCCbuuMKNVS95FkXm0vqVD/YpXKwA/no
c8PH3PSoAaRwMMgOSA2ALJvbRz8mpg==
-----END CERTIFICATE-----",
 "privateKey": "-----BEGIN ENCRYPTED PRIVATE KEY-----
MIIFKzBVBgkqhkiG9w0BBQ0wSDAnBgkqhkiG9w0BBQwwGgQUiAFcK5hT/X7Kjmgp
...
QrSekqF+kWzmB6nAfSzgO9IaoAaytLvNgGTckWeUkWn/V0Ck+LdGUXzAC4RxZnoQ
zp2mwJn2NYB7AZ7+imp0azDZb+8YG2aUCiyqb6PnnA==
-----END ENCRYPTED PRIVATE KEY-----"
}
```

### How EventBridge chooses a bootstrap broker

EventBridge chooses a [bootstrap
broker](../../../msk/latest/developerguide/msk-get-bootstrap-brokers.md "../../../msk/latest/developerguide/msk-get-bootstrap-brokers.md") based on the authentication methods available on your cluster, and whether
you provide a secret for authentication. If you provide a secret for mTLS or SASL/SCRAM,
EventBridge automatically chooses that authentication method. If you don't provide a secret, EventBridge
chooses the strongest authentication method that's active on your cluster. The following is
the order of priority in which EventBridge selects a broker, from strongest to weakest
authentication:

- mTLS (secret provided for mTLS)
- SASL/SCRAM (secret provided for SASL/SCRAM)
- SASL IAM (no secret provided, and IAM authentication is active)
- Unauthenticated TLS (no secret provided, and IAM authentication is not
  active)
- Plaintext (no secret provided, and both IAM authentication and unauthenticated TLS
  are not active)

###### Note

If EventBridge can't connect to the most secure broker type, it doesn't attempt to connect to
a different (weaker) broker type. If you want EventBridge to choose a weaker broker type,
deactivate all stronger authentication methods on your cluster.

## Network configuration

EventBridge must have access to the Amazon Virtual Private Cloud (Amazon VPC) resources associated with your Amazon MSK
cluster.

- To access the VPC of your Amazon MSK cluster, EventBridge can use outbound internet access for the
  subnets of your source. For private subnets it can be a NAT gateway, or your own NAT. Ensure that
  the NAT has a public IP address and can connect to the internet. For public subnets you must use VPC Endpoints (explained below).
- EventBridge Pipes also supports event delivery through [AWS PrivateLink](https://aws.amazon.com/privatelink/ "https://aws.amazon.com/privatelink/"), allowing
  you to send events from an event source located in an Amazon Virtual Private Cloud (Amazon VPC) to a Pipes target without traversing the public internet. You can use Pipes
  to poll from Amazon Managed Streaming for Apache Kafka (Amazon MSK), self-managed Apache Kafka, and
  Amazon MQ sources residing in a private subnet without the need to deploy an
  internet gateway, configure firewall rules, or set up proxy servers.
  You can also use VPC Endpoints to support delivery from Kafka clusters in public subnets.

To set up a VPC endpoint, see [Create a VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws")
in the _AWS PrivateLink User Guide_.
For service name, select `com.amazonaws.`region`.pipes-data`.

Configure your Amazon VPC security groups with the following rules (at minimum):

- Inbound rules – Allow all traffic on the Amazon MSK broker port for the security groups specified for your
  source.
- Outbound rules – Allow all traffic on port 443 for all destinations. Allow all
  traffic on the Amazon MSK broker port for the security groups specified for your source.

Broker ports include:

    + 9092 for plaintext
    + 9094 for TLS
    + 9096
     for SASL
    + 9098 for IAM

###### Note

Your Amazon VPC configuration is discoverable through the [Amazon MSK API](../../../msk/1.0/apireference/resources.md "../../../msk/1.0/apireference/resources.md"). You don't need to configure it during
setup.

## Customizable consumer group ID

When setting up Apache Kafka as an source, you can specify a consumer group ID. This consumer
group ID is an existing identifier for the Apache Kafka consumer group that you want your pipe to
join. You can use this feature to migrate any ongoing Apache Kafka record processing setups from
other consumers to EventBridge.

If you specify a consumer group ID and there are other active pollers within that consumer
group, Apache Kafka distributes messages across all consumers. In other words, EventBridge doesn't receive
all messages for the Apache Kafka topic. If you want EventBridge to handle all messages in the topic, turn
off any other pollers in that consumer group.

Additionally, if you specify a consumer group ID, and Apache Kafka finds a valid existing
consumer group with the same ID, EventBridge ignores the `StartingPosition` parameter for
your pipe. Instead, EventBridge begins processing records according to the committed offset of the
consumer group. If you specify a consumer group ID, and Apache Kafka can't find an existing
consumer group, then EventBridge configures your source with the specified
`StartingPosition`.

The consumer group ID that you specify must be unique among all your Apache Kafka event
sources. After creating a pipe with the consumer group ID specified, you can't update this
value.

## Auto scaling of the Amazon MSK source

When you initially create an Amazon MSK source, EventBridge allocates one consumer to process all
partitions in the Apache Kafka topic. Each consumer has multiple processors running in parallel to
handle increased workloads. Additionally, EventBridge automatically scales up or down the number of
consumers, based on workload. To preserve message ordering in each partition, the maximum
number of consumers is one consumer per partition in the topic.

In one-minute intervals, EventBridge evaluates the consumer offset lag of all the partitions in
the topic. If the lag is too high, the partition is receiving messages faster than EventBridge can
process them. If necessary, EventBridge adds or removes consumers from the topic. The scaling process
of adding or removing consumers occurs within three minutes of evaluation.

If your target is overloaded, EventBridge reduces the number of consumers. This action reduces
the workload on the pipe by reducing the number of messages that consumers can retrieve and
send to the pipe.
