# Using the ElastiCache Cluster Client for Java

The program below demonstrates how to use the ElastiCache Cluster Client to connect to a cluster
configuration endpoint and add a data item to the cache. Using Auto Discovery, the
program connects to all of the nodes in the cluster without any further
intervention.

```
package com.amazon.elasticache;

import java.io.IOException;
import java.net.InetSocketAddress;

// Import the &AWS;-provided library with Auto Discovery support
import net.spy.memcached.MemcachedClient;

public class AutoDiscoveryDemo {

    public static void main(String[] args) throws IOException {

        String configEndpoint = "mycluster.fnjyzo.cfg.use1.cache.amazonaws.com";
        Integer clusterPort = 11211;

        MemcachedClient client = new MemcachedClient(
                                 new InetSocketAddress(configEndpoint,
                                                       clusterPort));
        // The client will connect to the other cache nodes automatically.

        // Store a data item for an hour.
        // The client will decide which cache host will store this item.
        client.set("theKey", 3600, "This is the data value");
    }
}
```

ElastiCache Serverless caches always have in-transit encryption (TLS) enabled.
You can also enable TLS on node-based clusters. To connect to a TLS-enabled
cache, configure the client with an SSLContext as shown in the
following example.

###### Note

The `setSSLContext` method is only available in the AWS fork of the spymemcached client. For the source, see [aws-elasticache-cluster-client-memcached-for-java](https://github.com/awslabs/aws-elasticache-cluster-client-memcached-for-java "https://github.com/awslabs/aws-elasticache-cluster-client-memcached-for-java") on the GitHub website. This method is not part of the standard open-source spymemcached library.

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

For more information about connecting with TLS, see
[Creating a TLS Memcached client using Java](in-transit-encryption.md#in-transit-encryption-connect-java "in-transit-encryption.md#in-transit-encryption-connect-java").
For a Serverless cache, use the cache's Serverless endpoint on port 11211.
The Serverless endpoint does not contain ".cfg" in the address. For a
node-based cluster with TLS enabled, use the configuration endpoint that
contains ".cfg".
