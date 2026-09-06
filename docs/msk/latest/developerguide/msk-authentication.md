

# Mutual TLS client authentication for Amazon MSK
<a name="msk-authentication"></a>

You can enable client authentication with TLS for connections from your applications to your Amazon MSK brokers. To use client authentication, you need an AWS Private CA. The AWS Private CA can be either in the same AWS account as your cluster, or in a different account. For information about AWS Private CAs, see [Creating and Managing a AWS Private CA](https://docs.aws.amazon.com/acm-pca/latest/userguide/create-CA.html).

Amazon MSK doesn't support certificate revocation lists (CRLs). To control access to your cluster topics or block compromised certificates, use Apache Kafka ACLs and AWS security groups. For information about using Apache Kafka ACLs, see [Apache Kafka ACLs](msk-acls.md).

**Topics**
+ [Create a Amazon MSK cluster that supports client authentication](msk-authentication-cluster.md)
+ [Set up a client to use authentication](msk-authentication-client.md)
+ [Produce and consume messages using authentication](msk-authentication-messages.md)