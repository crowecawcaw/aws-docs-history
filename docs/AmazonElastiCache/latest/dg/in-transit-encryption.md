# ElastiCache in-transit encryption (TLS)

To help keep your data secure, Amazon ElastiCache and Amazon EC2 provide mechanisms to guard against
unauthorized access of your data on the server. By providing in-transit encryption
capability, ElastiCache gives you a tool you can use to help protect your data when it is moving
from one location to another.

All Valkey or Redis OSS serverless caches have in-transit encryption enabled. For node-based clusters, you can enable in-transit encryption on a replication group by setting the
parameter `TransitEncryptionEnabled` to `true`
(CLI: `--transit-encryption-enabled`) when you create the replication
group. You can do this whether you are creating the replication group using the AWS Management Console,
the AWS CLI, or the ElastiCache API.

All serverless caches have in-transit encryption enabled. For node-based clusters, you can enable in-transit encryption on a cluster by setting the parameter
`TransitEncryptionEnabled` to `true` (CLI:
`--transit-encryption-enabled`) when you create the cluster using the
`CreateCacheCluster` (CLI: `create-cache-cluster`)
operation.

###### Topics

- [In-transit encryption overview](#in-transit-encryption-overview "#in-transit-encryption-overview")
- [In-transit encryption conditions (Valkey and Redis OSS)](#in-transit-encryption-constraints "#in-transit-encryption-constraints")
- [In-transit encryption conditions (Memcached)](#in-transit-encryption-constraints "#in-transit-encryption-constraints")
- [In-transit encryption best practices](#in-transit-encryption-best-practices "#in-transit-encryption-best-practices")
- [Further Valkey and Redis OSS options](#in-transit-encryption-see-also "#in-transit-encryption-see-also")
- [Enabling in-transit encryption for Memcached](#in-transit-encryption-enable-existing-mc "#in-transit-encryption-enable-existing-mc")
- [Enabling in-transit encryption](in-transit-encryption-enable.md "in-transit-encryption-enable.md")
- [Connecting to ElastiCache (Valkey) or Amazon ElastiCache for Redis OSS with in-transit encryption using valkey-cli](connect-tls.md "connect-tls.md")
- [Enabling in-transit encryption on a node-based Redis OSS cluster using Python](in-transit-encryption-enable-python.md "in-transit-encryption-enable-python.md")
- [Best practices when enabling in-transit encryption](enable-python-best-practices.md "enable-python-best-practices.md")
- [Connecting to nodes enabled with in-transit encryption using Openssl (Memcached)](#in-transit-encryption-connect-mc "#in-transit-encryption-connect-mc")
- [Creating a TLS Memcached client using Java](#in-transit-encryption-connect-java "#in-transit-encryption-connect-java")
- [Creating a TLS Memcached client using PHP](#in-transit-encryption-connect-php-mc "#in-transit-encryption-connect-php-mc")

## In-transit encryption overview

Amazon ElastiCache in-transit encryption is a feature that allows you to increase the
security of your data at its most vulnerable points—when it is in transit from
one location to another. Because there is some processing needed to encrypt and decrypt
the data at the endpoints, enabling in-transit encryption can have some performance
impact. You should benchmark your data with and without in-transit encryption to
determine the performance impact for your use cases.

ElastiCache in-transit encryption implements the following features:

- Encrypted client connections—client connections to
  cache nodes are TLS encrypted.
- Encrypted server connections—data moving
  between nodes in a cluster is encrypted.
- Server authentication—clients can
  authenticate that they are connecting to the right server.
- Client authentication—using the Valkey and Redis OSS AUTH feature, the server can authenticate the clients.

###### Note

ElastiCache does not support mTLS (mutual TLS).

## In-transit encryption conditions (Valkey and Redis OSS)

The following constraints on Amazon ElastiCache in-transit encryption should be kept in mind
when you plan your node-based cluster implementation:

- In-transit encryption is supported on replication groups running Valkey 7.2 and later, and Redis OSS versions 3.2.6, 4.0.10 and later.
- Modifying the in-transit encryption setting, for an existing cluster, is
  supported on replication groups running Valkey 7.2 and later, and Redis OSS version 7 and later.
- In-transit encryption is supported only for replication groups running in an Amazon VPC.
- In-transit encryption is not supported for replication groups running the following node types: M1, M2.

For more information, see [Supported node types](CacheNodes.md "CacheNodes.md").

- In-transit encryption is enabled by explicitly setting the parameter
  `TransitEncryptionEnabled` to `true`.
- Ensure that your caching client supports TLS connectivity and that you have
  enabled it in client configuration.
- Starting January 26, 2026, AWS will update the minimum supported TLS version to 1.2 on ElastiCache for Valkey version 7.2 and above, and ElastiCache for Redis OSS version 6 and above. Customers must update their client software before that date. This update helps you meet security, compliance, and regulatory needs.

## In-transit encryption conditions (Memcached)

The following constraints on Amazon ElastiCache in-transit encryption should be kept in mind
when you plan your node-based cluster implementation:

- In-transit encryption is supported on clusters running Memcached versions
  1.6.12 and later.
- In-transit encryption supports Transport Layer Security (TLS) versions 1.2 and
  1.3.
- In-transit encryption is supported only for clusters running in an
  Amazon VPC.
- In-transit encryption is not supported for replication groups running the following node types: M1, M2, M3, R3, T2.

For more information, see [Supported node types](CacheNodes.md "CacheNodes.md").

- In-transit encryption is enabled by explicitly setting the parameter
  `TransitEncryptionEnabled` to `true`.
- You can enable in-transit encryption on a cluster only when creating the
  cluster. You cannot toggle in-transit encryption on and off by modifying a
  cluster.
- Ensure that your caching client supports TLS connectivity and that you have
  enabled it in client configuration.

## In-transit encryption best practices

- Because of the processing required to encrypt and decrypt the data at the
  endpoints, implementing in-transit encryption can reduce performance. Benchmark
  in-transit encryption compared to no encryption on your own data to determine
  its impact on performance for your implementation.
- Because creating new connections can be expensive, you can reduce the
  performance impact of in-transit encryption by persisting your TLS
  connections.

## Further Valkey and Redis OSS options

For further information on options available for Valkey and Redis OSS, see the followling links.

- [At-Rest Encryption in ElastiCache](at-rest-encryption.md "at-rest-encryption.md")
- [Authenticating with the Valkey and Redis OSS AUTH command](auth.md "auth.md")
- [Role-Based Access Control (RBAC)](Clusters.md "Clusters.md")
- [Amazon VPCs and ElastiCache security](VPCs.md "VPCs.md")
- [Identity and Access Management for Amazon ElastiCache](IAM.md "IAM.md")

## Enabling in-transit encryption for Memcached

To enable in-transit encryption when creating a Memcached cluster using the AWS
Management Console, make the following selections:

- Choose Memcached as your engine.
- Choose engine version 1.6.12 or later.
- Under **Encryption in transit**, choose
  **Enable**.

For the step-by-step process, see [Creating a cluster for Valkey or Redis OSS](Clusters.md "Clusters.md").

## Connecting to nodes enabled with in-transit encryption using Openssl (Memcached)

To access data from ElastiCache for Memcached nodes enabled with in-transit encryption, you need to use
clients that work with Secure Socket Layer (SSL). You can also use Openssl s_client on
Amazon Linux and Amazon Linux 2.

To use Openssl s_client to connect to a Memcached cluster enabled with in-transit
encryption on Amazon Linux 2 or Amazon Linux:

```
/usr/bin/openssl s_client -connect `memcached-node-endpoint`:`memcached-port`
```

## Creating a TLS Memcached client using Java

To create a client in TLS mode, do the following to initialize the client with the
appropriate SSLContext:

```
import java.security.KeyStore;
import javax.net.ssl.SSLContext;
import javax.net.ssl.TrustManagerFactory;
import net.spy.memcached.AddrUtil;
import net.spy.memcached.ConnectionFactoryBuilder;
import net.spy.memcached.MemcachedClient;
public class TLSDemo {
    public static void main(String[] args) throws Exception {
        ConnectionFactoryBuilder connectionFactoryBuilder = new ConnectionFactoryBuilder();
        // Build SSLContext
        TrustManagerFactory tmf = TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm());
        tmf.init((KeyStore) null);
        SSLContext sslContext = SSLContext.getInstance("TLS");
        sslContext.init(null, tmf.getTrustManagers(), null);
        // Create the client in TLS mode
        connectionFactoryBuilder.setSSLContext(sslContext);
        MemcachedClient client = new MemcachedClient(connectionFactoryBuilder.build(), AddrUtil.getAddresses("mycluster.fnjyzo.cfg.use1.cache.amazonaws.com:11211"));

        // Store a data item for an hour.
        client.set("theKey", 3600, "This is the data value");
    }
}
```

## Creating a TLS Memcached client using PHP

To create a client in TLS mode, do the following to initialize the client with the
appropriate SSLContext:

```
<?php

/**
 * Sample PHP code to show how to create a TLS Memcached client. In this example we
 * will use the Amazon ElastiCache Auto Descovery feature, but TLS can also be
 * used with a Static mode client.
 * See Using the ElastiCache Cluster Client for PHP (https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoDiscovery.Using.ModifyApp.PHP.html) for more information
 * about Auto Discovery and persistent-id.
 */

/* Configuration endpoint to use to initialize memcached client.
 * this is only an example */
$server_endpoint = "mycluster.fnjyzo.cfg.use1.cache.amazonaws.com";

/* Port for connecting to the cluster.
 * This is only an example     */
$server_port = 11211;

/* Initialize a persistent Memcached client and configure it with the Dynamic client mode  */
$tls_client =  new Memcached('persistent-id');
$tls_client->setOption(Memcached::OPT_CLIENT_MODE, Memcached::DYNAMIC_CLIENT_MODE);

/* Add the memcached's cluster server/s */
$tls_client->addServer($server_endpoint, $server_port);

/* Configure the client to use TLS */
if(!$tls_client->setOption(Memcached::OPT_USE_TLS, 1)) {
    echo $tls_client->getLastErrorMessage(), "\n";
    exit(1);
}

/* Set your TLS context configurations values.
 * See MemcachedTLSContextConfig in memcached-api.php for all configurations */
$tls_config = new MemcachedTLSContextConfig();
$tls_config->hostname = '*.mycluster.fnjyzo.use1.cache.amazonaws.com';
$tls_config->skip_cert_verify = false;
$tls_config->skip_hostname_verify = false;

/* Use the created TLS context configuration object to create OpenSSL's SSL_CTX and set it to your client.
 * Note:  These TLS context configurations will be applied to all the servers connected to this client. */
$tls_client->createAndSetTLSContext((array)$tls_config);

/* test the TLS connection with set-get scenario: */

 /* store the data for 60 seconds in the cluster.
 * The client will decide which cache host will store this item.
 */
if($tls_client->set('key', 'value', 60)) {
    print "Successfully stored key\n";
} else {
    echo "Failed to set key: ", $tls_client->getLastErrorMessage(), "\n";
    exit(1);
}

/* retrieve the key */
if ($tls_client->get('key') === 'value') {
    print "Successfully retrieved key\n";
} else {
    echo "Failed to get key: ", $tls_client->getLastErrorMessage(), "\n";
    exit(1);
}
```

For more information on using the PHP client, see [Installing the ElastiCache cluster client for PHP](Appendix.md "Appendix.md").
