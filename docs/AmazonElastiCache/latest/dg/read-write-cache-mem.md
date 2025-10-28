# Read and write data to the cache

This section assumes that you've created an Amazon EC2 instance and can connect to it. For instructions on how to do this, see the [Amazon EC2 Getting Started Guide](https://aws.amazon.com/ec2/getting-started/ "https://aws.amazon.com/ec2/getting-started/").

By default, ElastiCache creates a cache in your default VPC. Make sure that your EC2 instance is also created in the default VPC, so that it is able to connect to the cache.

**Find your cache endpoint**

**AWS Management Console**

To find your cache’s endpoint using the ElastiCache console:

1. Sign in to the AWS Management Console and open the Amazon ElastiCache console at [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. In the navigation pane on the left side of the console, choose **Memcached Caches**.
3. On the right side of the console, click on the name of the cache that you just created.
4. In the **Cache details**, locate and copy the cache endpoint.
   **AWS CLI**

The following AWS CLI example shows to find the endpoint for your new cache using the describe-serverless-caches command.
Once you have run the command, look for the "Endpoint" field.

**Linux**

```
aws elasticache describe-serverless-caches \
		--serverless-cache-name CacheName
```

**Windows**

```
aws elasticache describe-serverless-caches ^
		--serverless-cache-name CacheName
```

For information on how to connect using OpenSSL, see [ElastiCache in-transit encryption (TLS)](in-transit-encryption.md "in-transit-encryption.md")

```
import java.security.KeyStore;
import javax.net.ssl.SSLContext;
import javax.net.ssl.TrustManagerFactory;
import net.spy.memcached.AddrUtil;
import net.spy.memcached.ConnectionFactoryBuilder;
import net.spy.memcached.FailureMode;
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
        // Set Failure Mode to Retry
        connectionFactoryBuilder.setFailureMode(FailureMode.Retry);
        MemcachedClient client = new MemcachedClient(connectionFactoryBuilder.build(), AddrUtil.getAddresses("mycluster-fnjyzo.serverless.use1.cache.amazonaws.com:11211"));

        // Store a data item for an hour.
        client.set("theKey", 3600, "This is the data value");
    }
}
```

```
<?php
$cluster_endpoint = "mycluster.serverless.use1.cache.amazonaws.com";
$server_port = 11211;

/* Initialize a persistent Memcached client in TLS mode */
$tls_client = new Memcached('persistent-id');
$tls_client->addServer($cluster_endpoint, $server_port);
if(!$tls_client->setOption(Memcached::OPT_USE_TLS, 1)) {
    echo $tls_client->getLastErrorMessage(), "\n";
    exit(1);
}
$tls_config = new MemcachedTLSContextConfig();
$tls_config->hostname = '*.serverless.use1.cache.amazonaws.com';
$tls_config->skip_cert_verify = false;
$tls_config->skip_hostname_verify = false;
$tls_client->createAndSetTLSContext((array)$tls_config);

 /* store the data for 60 seconds in the cluster */
$tls_client->set('key', 'value', 60);
?>
```

See [https://pymemcache.readthedocs.io/en/latest/getting_started.html](https://pymemcache.readthedocs.io/en/latest/getting_started.html "https://pymemcache.readthedocs.io/en/latest/getting_started.html")

```
import ssl
from pymemcache.client.base import Client

context = ssl.create_default_context()
cluster_endpoint = <To be taken from the AWS CLI / console>
target_port = 11211
memcached_client = Client(("{cluster_endpoint}", target_port), tls_context=context)
memcached_client.set("key", "value", expire=500, noreply=False)
assert self.memcached_client.get("key").decode() == "value"

```

See [https://github.com/electrode-io/memcache](https://github.com/electrode-io/memcache "https://github.com/electrode-io/memcache")
and [https://www.npmjs.com/package/memcache-client](https://www.npmjs.com/package/memcache-client "https://www.npmjs.com/package/memcache-client")

Install via `npm i memcache-client`

In the application, create a memcached TLS client as follows:

```
var memcache = require("memcache-client");
const client = new memcache.MemcacheClient({server: "{cluster_endpoint}:11211", tls: {}});
client.set("key", "value");
```

See [https://crates.io/crates/memcache](https://crates.io/crates/memcache "https://crates.io/crates/memcache")
and [https://github.com/aisk/rust-memcache](https://github.com/aisk/rust-memcache "https://github.com/aisk/rust-memcache").

```
// create connection with to memcached server node:
let client = memcache::connect("memcache+tls://<cluster_endpoint>:11211?verify_mode=none").unwrap();

// set a string value
client.set("foo", "bar", 0).unwrap();
```

See [https://github.com/bradfitz/gomemcache](https://github.com/bradfitz/gomemcache "https://github.com/bradfitz/gomemcache")

```

c := New(net.JoinHostPort("{cluster_endpoint}", strconv.Itoa(port)))
c.DialContext = func(ctx context.Context, network, addr string) (net.Conn, error) {
var td tls.Dialer
td.Config = &tls.Config{}
return td.DialContext(ctx, network, addr)
}
foo := &Item{Key: "foo", Value: []byte("fooval"), Flags: 123}
err := c.Set(foo)
```

See [https://github.com/petergoldstein/dalli](https://github.com/petergoldstein/dalli "https://github.com/petergoldstein/dalli")

```
require 'dalli'
ssl_context = OpenSSL::SSL::SSLContext.new
ssl_context.ssl_version = :SSLv23
ssl_context.verify_hostname = true
ssl_context.verify_mode = OpenSSL::SSL::VERIFY_PEER
client = Dalli::Client.new("<cluster_endpoint>:11211", :ssl_context => ssl_context);
client.get("abc")
```

See [https://github.com/cnblogs/EnyimMemcachedCore](https://github.com/cnblogs/EnyimMemcachedCore "https://github.com/cnblogs/EnyimMemcachedCore")

```

"MemcachedClient": {
"Servers": [
{
"Address": "{cluster_endpoint}",
"Port": 11211
}
],
"UseSslStream":  true
}
```

You may now proceed to [(Optional) Clean up](read-write-cleanup-mem.md "read-write-cleanup-mem.md").
