# Apache Kafka streams as a source in EventBridge Pipes

Apache Kafka is an open-source event streaming platform that supports workloads such as data
pipelines and streaming analytics. You can use [Amazon Managed Streaming for Apache Kafka](eb-pipes-msk.md "eb-pipes-msk.md") (Amazon MSK), or a self managed Apache Kafka cluster. In AWS terminology, a
_self managed_ cluster refers to any Apache Kafka cluster not hosted by AWS.
This includes both clusters you manage yourself, as well as those hosted by a third-party
provider, such as [Confluent
Cloud](https://www.confluent.io/ "https://www.confluent.io/"), [CloudKarafka](https://www.cloudkarafka.com/ "https://www.cloudkarafka.com/"), or [Redpanda](https://redpanda.com/ "https://redpanda.com/").

For more information on other AWS hosting options for your cluster, see
[Best
Practices for Running Apache Kafka on AWS](https://aws.amazon.com/blogs/big-data/best-practices-for-running-apache-kafka-on-aws/ "https://aws.amazon.com/blogs/big-data/best-practices-for-running-apache-kafka-on-aws/") on the _AWS Big Data
Blog_.

Apache Kafka as a source operates similarly to using Amazon Simple Queue Service (Amazon SQS) or Amazon Kinesis. EventBridge
internally polls for new messages from the source and then synchronously invokes the target.
EventBridge reads the messages in batches and provides these to your function as an event payload.
The maximum batch size is configurable. (The default is 100 messages.)

For Apache Kafka-based sources, EventBridge supports processing control parameters, such as batching
windows and batch size.

EventBridge sends the batch of messages in the event parameter when it invokes your pipe. The event
payload contains an array of messages. Each array item contains details of the Apache Kafka topic and
Apache Kafka partition identifier, together with a timestamp and a base64-encoded message.

**Example events**

The following sample event shows the information that is received by the pipe. You can use
this event to create and filter your event patterns, or to define input transformation. Not all
of the fields can be filtered. For more information about which fields you can filter, see [Event filtering in Amazon EventBridge Pipes](eb-pipes-event-filtering.md "eb-pipes-event-filtering.md").

```
[
  {
    "eventSource": "SelfManagedKafka",
    "bootstrapServers": "b-2.demo-cluster-1.a1bcde.c1.kafka.us-east-1.amazonaws.com:9092,b-1.demo-cluster-1.a1bcde.c1.kafka.us-east-1.amazonaws.com:9092",
    "eventSourceKey": "mytopic-0",
    "topic": "mytopic",
    "partition": 0,
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

## Apache Kafka cluster authentication

EventBridge Pipes supports several methods to authenticate with your self managed Apache Kafka cluster. Make sure that
you configure the Apache Kafka cluster to use one of these supported authentication methods. For more
information about Apache Kafka security, see the [Security](http://kafka.apache.org/documentation.html#security "http://kafka.apache.org/documentation.html#security") section of the
Apache Kafka documentation.

### VPC access

If you are using a self managed Apache Kafka environment where only Apache Kafka users
within your VPC have access to your Apache Kafka brokers, you must configure the Amazon Virtual Private Cloud (Amazon VPC) in the Apache Kafka source.

### SASL/SCRAM authentication

EventBridge Pipes supports Simple Authentication and Security Layer/Salted Challenge Response Authentication Mechanism
(SASL/SCRAM) authentication with Transport Layer Security (TLS) encryption. EventBridge Pipes sends the encrypted credentials to authenticate with
the cluster. For more information about SASL/SCRAM authentication, see [RFC 5802](https://tools.ietf.org/html/rfc5802 "https://tools.ietf.org/html/rfc5802").

EventBridge Pipes supports SASL/PLAIN authentication with TLS encryption. With SASL/PLAIN authentication, EventBridge Pipes sends
credentials as clear text (unencrypted) to the server.

For SASL authentication, you store the sign-in credentials as a secret in AWS Secrets Manager.

### Mutual TLS authentication

Mutual TLS (mTLS) provides two-way authentication between the client and server. The client sends a
certificate to the server for the server to verify the client, and the server sends a certificate to the client
for the client to verify the server.

In self managed Apache Kafka, EventBridge Pipes acts as the client. You configure a client certificate (as a secret in
Secrets Manager) to authenticate EventBridge Pipes with your Apache Kafka brokers. The client certificate must be
signed by a certificate authority (CA) in the server's trust store.

The Apache Kafka cluster sends a server certificate to EventBridge Pipes to authenticate the Apache Kafka
brokers with EventBridge Pipes. The server certificate can be a public CA certificate or a private
CA/self-signed certificate. The public CA certificate must be signed by a CA that's in the
EventBridge Pipes trust store. For a private CA/self-signed certificate, you configure the server root
CA certificate (as a secret in Secrets Manager). EventBridge Pipes uses the root certificate to verify the
Apache Kafka brokers.

For more information about mTLS, see [Introducing mutual TLS authentication for Amazon MSK as an source](https://aws.amazon.com/blogs/compute/introducing-mutual-tls-authentication-for-amazon-msk-as-an-event-source "https://aws.amazon.com/blogs/compute/introducing-mutual-tls-authentication-for-amazon-msk-as-an-event-source").

### Configuring the client certificate secret

The CLIENT_CERTIFICATE_TLS_AUTH secret requires a certificate field and a private key field. For an
encrypted private key, the secret requires a private key password. Both the certificate and private key must be
in PEM format.

###### Note

EventBridge Pipes supports the [PBES1](https://datatracker.ietf.org/doc/html/rfc2898/#section-6.1 "https://datatracker.ietf.org/doc/html/rfc2898/#section-6.1") (but not
PBES2) private key encryption algorithms.

The certificate field must contain a list of certificates, beginning with the client certificate, followed
by any intermediate certificates, and ending with the root certificate. Each certificate must start on a new
line with the following structure:

```
-----BEGIN CERTIFICATE-----
        <certificate contents>
-----END CERTIFICATE-----
```

Secrets Manager supports secrets up to 65,536 bytes, which is enough space for long certificate chains.

The private key must be in [PKCS #8](https://datatracker.ietf.org/doc/html/rfc5208 "https://datatracker.ietf.org/doc/html/rfc5208")
format, with the following structure:

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

The following example shows the contents of a secret for mTLS authentication using an encrypted private key.
For an encrypted private key, include the private key password in the secret.

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

### Configuring the server root CA certificate secret

You create this secret if your Apache Kafka brokers use TLS encryption with certificates signed
by a private CA. You can use TLS encryption for VPC, SASL/SCRAM, SASL/PLAIN, or mTLS
authentication.

The server root CA certificate secret requires a field that contains the Apache Kafka broker's
root CA certificate in PEM format. The following example shows the structure of the
secret.

```
{
     "certificate": "-----BEGIN CERTIFICATE-----
  MIID7zCCAtegAwIBAgIBADANBgkqhkiG9w0BAQsFADCBmDELMAkGA1UEBhMCVVMx
  EDAOBgNVBAgTB0FyaXpvbmExEzARBgNVBAcTClNjb3R0c2RhbGUxJTAjBgNVBAoT
  HFN0YXJmaWVsZCBUZWNobm9sb2dpZXMsIEluYy4xOzA5BgNVBAMTMlN0YXJmaWVs
  ZCBTZXJ2aWNlcyBSb290IENlcnRpZmljYXRlIEF1dG...
  -----END CERTIFICATE-----"
```

## Network configuration

If you are using a self managed Apache Kafka environment that uses private VPC connectivity, EventBridge must have
access to the Amazon Virtual Private Cloud (Amazon VPC) resources associated with your Apache Kafka brokers.

- To access the VPC of your Apache Kafka cluster, EventBridge can use outbound internet access for
  the subnets of your source. For private subnets it can be a NAT gateway, or your own NAT. Ensure that
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

- Inbound rules – Allow all traffic on the Apache Kafka broker port for the security
  groups specified for your source.
- Outbound rules – Allow all traffic on port 443 for all destinations. Allow all
  traffic on the Apache Kafka broker port for the security groups specified for your
  source.

Broker ports include:

    + 9092 for plaintext
    + 9094 for TLS
    + 9096
     for SASL
    + 9098 for IAM

## Consumer auto scaling with Apache Kafka sources

When you initially create an Apache Kafka source, EventBridge allocates one consumer to process
all partitions in the Kafka topic. Each consumer has multiple processors running in parallel
to handle increased workloads. Additionally, EventBridge automatically scales up or down the number
of consumers, based on workload. To preserve message ordering in each partition, the maximum
number of consumers is one consumer per partition in the topic.

In one-minute intervals, EventBridge evaluates the consumer offset lag of all the partitions in the topic. If the lag is
too high, the partition is receiving messages faster than EventBridge can process them. If necessary, EventBridge adds or
removes consumers from the topic. The scaling process of adding or removing consumers occurs within three minutes of evaluation.

If your target is overloaded, EventBridge reduces the number of consumers. This action reduces the
workload on the function by reducing the number of messages that consumers can retrieve and send to the
function.
