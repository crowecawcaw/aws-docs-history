# Security Hub controls for Amazon MSK

These AWS Security Hub controls evaluate the Amazon Managed Streaming for Apache Kafka (Amazon MSK) service and resources. The
controls might not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [MSK.1] MSK clusters should be encrypted in transit among broker

nodes

**Related requirements:** NIST.800-53.r5 AC-4,
NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-23, NIST.800-53.r5 SC-23(3), NIST.800-53.r5
SC-7(4), NIST.800-53.r5 SC-8, NIST.800-53.r5 SC-8(1), NIST.800-53.r5 SC-8(2),
PCI DSS v4.0.1/4.2.1

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:**
`AWS::MSK::Cluster`

**AWS Config rule:**
[msk-in-cluster-node-require-tls](../../../config/latest/developerguide/msk-in-cluster-node-require-tls.md "../../../config/latest/developerguide/msk-in-cluster-node-require-tls.md")

**Schedule type:** Change triggered

**Parameters:** None

This controls checks whether an Amazon MSK cluster is encrypted in transit with HTTPS (TLS)
among the broker nodes of the cluster. The control fails if plain text communication is
enabled for a cluster broker node connection.

HTTPS offers an extra layer of security as it uses TLS to move data and can be used to
help prevent potential attackers from using person-in-the-middle or similar attacks to
eavesdrop on or manipulate network traffic. By default, Amazon MSK encrypts data in transit
with TLS. However, you can override this default at the time that you create the
cluster. We recommend using encrypted connections over HTTPS (TLS) for-broker node
connections.

### Remediation

For information about updating the encryption settings for an Amazon MSK cluster, see
[Updating security
settings of a cluster](../../../msk/latest/developerguide/msk-update-security.md "../../../msk/latest/developerguide/msk-update-security.md") in the _Amazon Managed Streaming for Apache Kafka Developer
Guide_.

## [MSK.2] MSK clusters should have enhanced monitoring

configured

**Related requirements:** NIST.800-53.r5 CA-7,
NIST.800-53.r5 SI-2

**Category:** Detect > Detection services

**Severity:** Low

**Resource type:**
`AWS::MSK::Cluster`

**AWS Config rule:**
[msk-enhanced-monitoring-enabled](../../../config/latest/developerguide/msk-enhanced-monitoring-enabled.md "../../../config/latest/developerguide/msk-enhanced-monitoring-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon MSK cluster has enhanced monitoring configured,
specified by a monitoring level of at least `PER_TOPIC_PER_BROKER`. The
control fails if the monitoring level for the cluster is set to `DEFAULT` or
`PER_BROKER`.

The `PER_TOPIC_PER_BROKER` monitoring level provides more granular insights
into the performance of your MSK cluster, and also provides metrics related to resource
utilization, such as CPU and memory usage. This helps you identify performance
bottlenecks and resource utilization patterns for individual topics and brokers. This
visibility, in turn, can optimize the performance of your Kafka brokers.

### Remediation

To configure enhanced monitoring for an MSK cluster, complete the following
steps:

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/ "https://console.aws.amazon.com/msk/home?region=us-east-1#/home/").
2. In the navigation pane, choose **Clusters**. Then, choose
   a cluster.
3. For **Action**, select **Edit
   monitoring**.
4. Select the option for **Enhanced topic-level
   monitoring**.
5. Choose **Save changes**.

For more information about monitoring levels, see [Amazon MSK metrics for
monitoring Standard brokers with CloudWatch](../../../msk/latest/developerguide/metrics-details.md "../../../msk/latest/developerguide/metrics-details.md") in the _Amazon Managed Streaming for Apache Kafka
Developer Guide_.

## [MSK.3] MSK Connect connectors should be encrypted in

transit

**Related requirements:** PCI DSS v4.0.1/4.2.1

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:**
`AWS::KafkaConnect::Connector`

**AWS Config rule:**
`msk-connect-connector-encrypted` (custom Security Hub rule)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon MSK Connect connector is encrypted in transit. This
control fails if the connector isn't encrypted in transit.

Data in transit refers to data that moves from one location to another, such as between nodes in your cluster or between your cluster and your application. Data may move across the internet or within a private network. Encrypting data in transit reduces the risk that an unauthorized user can eavesdrop on network traffic.

### Remediation

You can enable encryption in transit when you create an MSK Connect connector. You
can't change encryption settings after creating a connector. For more information,
see [Create a
connector](../../../msk/latest/developerguide/mkc-create-connector-intro.md "../../../msk/latest/developerguide/mkc-create-connector-intro.md") in the _Amazon Managed Streaming for Apache Kafka Developer Guide_.

## [MSK.4] MSK clusters should have public access disabled

**Category:** Protect > Secure access management > Resource not publicly accessible

**Severity:** Critical

**Resource type:**
`AWS::MSK::Cluster`

**AWS Config rule:**
[msk-cluster-public-access-disabled](../../../config/latest/developerguide/msk-cluster-public-access-disabled.md "../../../config/latest/developerguide/msk-cluster-public-access-disabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether public access is disabled for an Amazon MSK cluster. The
control fails if public access is enabled for the MSK cluster.

By default, clients can access an Amazon MSK cluster only if they're in the same VPC as the
cluster. All communication between Kafka clients and an MSK cluster are private by
default and streaming data doesn't traverse the internet. However, if an MSK cluster is
configured to allow public access, anyone on the internet can establish a connection to
Apache Kafka brokers that are running within the cluster. This can lead to issues such
as unauthorized access, data breaches, or exploitation of vulnerabilities. If you
restrict access to a cluster by requiring authentication and authorization measures, you
can help protect sensitive information and maintain the integrity of your
resources.

### Remediation

For information about managing public access to an Amazon MSK cluster, see [Turn on
public access to an MSK Provisioned cluster](../../../msk/latest/developerguide/public-access.md "../../../msk/latest/developerguide/public-access.md") in the _Amazon Managed Streaming for Apache Kafka
Developer Guide_.

## [MSK.5] MSK connectors should have logging enabled

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::KafkaConnect::Connector`

**AWS Config rule:**
[msk-connect-connector-logging-enabled](../../../config/latest/developerguide/msk-connect-connector-logging-enabled.md "../../../config/latest/developerguide/msk-connect-connector-logging-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether logging is enabled for an Amazon MSK connector. The control
fails if logging is disabled for the MSK connector.

Amazon MSK connectors integrate external systems and Amazon services with Apache Kafka by
continuously copying streaming data from a data source into an Apache Kafka cluster, or
continuously copying data from a cluster into a data sink. MSK Connect can write log
events that can help debug a connector. When you create a connector, you can specify
zero or more of the following log destinations: Amazon CloudWatch Logs, Amazon S3, and Amazon Data Firehose.

###### Note

Sensitive configuration values can appear in connector logs if a plugin does not
define those values as secret. Kafka Connect treats undefined configuration values
the same as any other plaintext value.

### Remediation

To enable logging for an existing Amazon MSK connector, you have to re-create the
connector with the appropriate logging configuration. For information about
configuration options, see [Logging for MSK
Connect](../../../msk/latest/developerguide/msk-connect-logging.md "../../../msk/latest/developerguide/msk-connect-logging.md") in the _Amazon Managed Streaming for Apache Kafka Developer Guide_.

## [MSK.6] MSK clusters should disable unauthenticated

access

**Category:** Protect > Secure access management >
Passwordless authentication

**Severity:** Medium

**Resource type:**
`AWS::MSK::Cluster`

**AWS Config rule:**
[msk-unrestricted-access-check](../../../config/latest/developerguide/msk-unrestricted-access-check.md "../../../config/latest/developerguide/msk-unrestricted-access-check.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether unauthenticated access is enabled for an Amazon MSK cluster.
The control fails if unauthenticated access is enabled for the MSK cluster.

Amazon MSK supports client authentication and authorization mechanisms to control access to
a cluster. These mechanisms verify the identity of clients connecting to the cluster and
determine which actions clients can perform. An MSK cluster can be configured to allow
unauthenticated access, which allows any client with network connectivity to publish and
subscribe to Kafka topics without providing credentials. Running an MSK cluster without
requiring authentication violates the principle of least privilege and can expose the
cluster to unauthorized access. It can allow any client to access, modify, or delete
data in Kafka topics, potentially resulting in data breaches, unauthorized data
modifications, or service disruptions. We recommend enabling authentication mechanisms
such as IAM authentication, SASL/SCRAM, or mutual TLS to ensure proper access control
and maintain security compliance.

### Remediation

For information about changing the authentication settings for an Amazon MSK cluster,
see the following sections of the _Amazon Managed Streaming for Apache Kafka Developer Guide_:
[Update security
settings of an Amazon MSK cluster](../../../msk/latest/developerguide/msk-update-security.md "../../../msk/latest/developerguide/msk-update-security.md") and [Authentication and
authorization for Apache Kafka APIs](../../../msk/latest/developerguide/kafka_apis_iam.md "../../../msk/latest/developerguide/kafka_apis_iam.md").
