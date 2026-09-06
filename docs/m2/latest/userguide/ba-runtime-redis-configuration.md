

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# Available Redis cache properties in AWS Transform for mainframe Runtime
<a name="ba-runtime-redis-configuration"></a>

You can use this document to learn about the Redis caches in AWS Transform for mainframe Runtime, along with Gapwalk configuration, supported Redis properties and how `application-main.yml` file can reference secret ARN for Redis caches.

## Redis caches in AWS Transform for mainframe Runtime
<a name="ba-redis-caches-in-runtime"></a>

Redis servers can be used as caches for various features in the AWS Transform for mainframe Gapwalk application, such as:



| AWS Transform for mainframe Runtime features that use Redis caching | Description | 
| --- | --- | 
| Blusam cache | A Redis Blusam cache for reading records efficiently, using a write-behind strategy, to optimize write-intensive workloads encountered on batch payloads.  | 
| Blusam locks | A cache for distributed locks for datasets and records. | 
| Dataset catalog | The catalog dataset cache. | 
| Session cache | A Redis cache for HttpSession. The cache stores the username, the state of the dialogue with the Angular frontend, and specific 'dialect' (BMS, MFS, AS400) information. | 
| Session tracker | A cache of active sessions with associated username and session-creation-time information. | 
| JICS cache | A cache for JICS resource definitions. | 
| TS queues | Storage for TS queues. | 
| JCL checkpoint |  JCL checkpoint cache. | 
| Gapwalk file locks | A cache for distributed file locks by job. | 
| Blu4iv locks | Storage for Blu4iv record locks. | 

## Redis Gapwalk configuration
<a name="ba-runtime-redis-gapwalk-configuration"></a>

The global Redis configuration is used if `redis` is specified as the caching mechanism and no Redis configuration is provided for the specific feature. This configuration makes it possible for you to use the same configuration for multiple Redis caches simultaneously.

In the following example the Blusam datasets cache and JICS cache use the `gapwalk.redis` (`redis.server1`) configuration because their cache type is set to `redis`, and no implicit Redis properties are specified under [JICS resource definitions](#ba-runtime-redis-jics-cache) and [JICS resource definitions](#ba-runtime-redis-jics-cache). However, the Blusam locks cache will use a different Redis configuration (`redis.server2`) because its Redis properties are explicitly defined.

```
...
 
 gapwalk:
   redis:
     hostName: redis.server1
 	port: 6379
 ...
 
 bluesam:
   # Redis bluesam cache
   cache: redis
   # Redis locks cache
   locks:
     cache: redis
 	hostName: redis.server2
 	port: 6379
 ...
 # Redis jics cache
 jics:
   resource-definitions:
     store-type: redis
 ...
```

 To enable the global Redis configuration, add the following configuration in `main-application.yml`. 

```
 gapwalk:
   redis:
     hostName: localhost
     port: 6379
     mode: standalone                        # Optional
     username:                               # Optional
     password: ""                            # Optional
     useSsl: false                           # Optional
     database: 0                             # Optional
     maxTotal: 128                           # Optional
     maxIdle: 128                            # Optional
     minIdle: 16                             # Optional
     testOnBorrow: true                      # Optional
     testOnReturn: true                      # Optional
     testWhileIdle: true                     # Optional
     testOnCreate: true                      # Optional
     minEvictableIdleTimeMillis: 60000       # Optional
     timeBetweenEvictionRunsMillis: 30000    # Optional
     numTestsPerEvictionRun: -1              # Optional
     blockWhenExhausted: true                # Optional
     nettyThreads: 32                        # Optional
     subscriptionsPerConnection: 10          # Optional
     subscriptionConnectionPoolSize: 100     # Optional
     pageSizeInBytes: 8192                   # Optional
     readTimeout: 2000                       # Optional
```

## Supported Redis properties
<a name="ba-runtime-redis-supported-properties"></a>

The following table shows the Redis properties that are supported for global and specific Redis caches on AWS Transform for mainframe Runtime.



| Property name | Required? | Description | Values | Default | 
| --- | --- | --- | --- | --- | 
| mode | No | The Redis running mode. | standalone \| cluster | standalone | 
| hostname | Yes | The hostname or IP address of the Redis server. | string | null | 
| port | Yes | The port number on which the Redis server is listening for connections. | int | null | 
| username | No | The username for authentication. | string | null | 
| password | No | The password for authentication. | string | empty string | 
| useSsl  | No | Specifies whether to enable SSL/TLS encryption for the Redis connection. | boolean | false | 
| database | No | The Redis database number to use. Redis supports multiple logical databases, and this property specifies which one to use. | int | 0 | 
| maxTotal | No | The maximum number of connections allowed in the Redis connection pool. | int  | 128 | 
| maxIdle | No | The maximum number of idle connections allowed in the Redis connection pool. | int | 128 | 
| minIdle | No | The minimum number of idle connections to maintain in the Redis connection pool. | int | 16 | 
| testOnBorrow  | No | A boolean value indicating whether to validate connections before borrowing them from the pool. | boolean | true | 
| testOnReturn  | No | A boolean value indicating whether to validate connections before returning them to the pool.  | boolean | true | 
| testWhileIdle  | No | A boolean value indicating whether to validate idle connections in the pool periodically. | boolean | true | 
| testOnCreate  | No | A boolean value indicating whether to validate connections when they are created. | boolean | true | 
| minEvictableIdleTimeMillis  | No | The minimum amount of time (in milliseconds) that an idle connection must remain in the pool before it can be evicted. | long | 60000L  | 
| timeBetweenEvictionRunsMillis  | No | The time (in milliseconds) between successive runs of the idle connection evictor thread. | long | 30000L | 
| numTestsPerEvictionRun  | No | The maximum number of connections to test during each run of the idle connection evictor thread. | int | -1 | 
| blockWhenExhausted  | No | A boolean value indicating whether to block and wait for a connection to become available when the pool is exhausted. | boolean | true | 
| nettyThreads  | No | The number of Netty threads to use for handling Redis connections. | int | 32 | 
| subscriptionsPerConnection  | No | The maximum number of subscriptions allowed per Redis connection. | int | 10 | 
| subscriptionConnectionPoolSize  | No | The maximum number of connections allowed in the Redis subscription connection pool.  | int | 100 | 
| pageSizeInBytes  | No | The default page size in bytes for Redis operations. | long | 262144000  | 
| readTimeout | No | The read timeout in milliseconds for Redis operations. | long | 2000 | 
| timeToLiveMillis | No | The duration (in Milliseconds) for which a cache entry remains in the cache before being considered expired and removed. If this property is not specified, cache entries will not automatically expire by default. | long | -1 | 
| useAsyncBatch | No | Enables asynchronous execution for Redis bulk write operations to improve performance. When set to false, falls back to synchronous execution mode. | boolean | true | 
| useBatchInMemoryAtomic | No | Enables In-memory-atomic mode for Redis batch read operations. When set to false, falls back to default In-memory batch mode. | boolean | false | 
| connectionPoolSize | No | The size of the connection pool used for Redisson client connections to Redis server. | int | 64 | 
| connectionMinimumIdleSize | No | The minimum number of idle connections that Redisson will maintain in its connection pool. | int | 24 | 
| idleConnectionTimeout | No | The timeout in milliseconds after which an idle connection in the pool will be closed. | int | 10000 | 
| connectTimeout | No | The timeout in milliseconds for establishing a connection to Redis server. | int | 10000 | 

## Redis cache properties
<a name="ba-runtime-redis-caches-properties"></a>

### Redis Blusam cache
<a name="ba-runtime-redis-blusam-cache"></a>

```
bluesam:
   cache: redis
 # If the following redis properties are not specified gapwalk.redis configuration will be used for this cache 
   redis:
     hostName: localhost
     port: 6379
     mode: standalone                        # Optional
     username:                               # Optional
     password: ""                            # Optional
     useSsl: false                           # Optional
     database: 0                             # Optional
     maxTotal: 128                           # Optional
     maxIdle: 128                            # Optional
     minIdle: 16                             # Optional
     testOnBorrow: true                      # Optional
     testOnReturn: true                      # Optional
     testWhileIdle: true                     # Optional
     testOnCreate: true                      # Optional
     minEvictableIdleTimeMillis: 60000       # Optional
     timeBetweenEvictionRunsMillis: 30000    # Optional
     numTestsPerEvictionRun: -1              # Optional
     blockWhenExhausted: true                # Optional
     nettyThreads: 32                        # Optional
     subscriptionsPerConnection: 10          # Optional
     subscriptionConnectionPoolSize: 100     # Optional
     pageSizeInBytes: 8192                   # Optional
     readTimeout: 2000                       # Optional
     timeToLiveMillis: 60000                 # Optional
     connectionPoolSize: 64                  # Optional
     connectionMinimumIdleSize: 24           # Optional
     idleConnectionTimeout: 10000            # Optional
     connectTimeout: 10000                   # Optional
```

### Redis Blusam cache
<a name="ba-runtime-redis-blusame-locks"></a>

```
bluesam:
   locks:
     cache: redis
 # If the following redis properties are not specified gapwalk.redis configuration will be used for this cache 
       hostName: localhost
       port: 6379
       mode: standalone                        # Optional
       username:                               # Optional
       password: ""                            # Optional
       useSsl: false                           # Optional
       database: 0                             # Optional
       maxTotal: 128                           # Optional
       maxIdle: 128                            # Optional
       minIdle: 16                             # Optional
       testOnBorrow: true                      # Optional
       testOnReturn: true                      # Optional
       testWhileIdle: true                     # Optional
       testOnCreate: true                      # Optional
       minEvictableIdleTimeMillis: 60000       # Optional
       timeBetweenEvictionRunsMillis: 30000    # Optional
       numTestsPerEvictionRun: -1              # Optional
       blockWhenExhausted: true                # Optional
       nettyThreads: 32                        # Optional
       subscriptionsPerConnection: 10          # Optional
       subscriptionConnectionPoolSize: 100     # Optional
       pageSizeInBytes: 8192                   # Optional
       readTimeout: 2000                       # Optional
```

### Session cache
<a name="ba-runtime-redis-session-cache"></a>

```
 spring:
   session:
     store-type: redis
 # If the following redis properties are not specified gapwalk.redis configuration will be used for this cache 
 jics:
   redis:
     hostName: localhost
     port: 6379
     mode: standalone                        # Optional
     username:                               # Optional
     password: ""                            # Optional
     useSsl: false                           # Optional
     database: 0                             # Optional
     maxTotal: 128                           # Optional
     maxIdle: 128                            # Optional
     minIdle: 16                             # Optional
     testOnBorrow: true                      # Optional
     testOnReturn: true                      # Optional
     testWhileIdle: true                     # Optional
     testOnCreate: true                      # Optional
     minEvictableIdleTimeMillis: 60000       # Optional
     timeBetweenEvictionRunsMillis: 30000    # Optional
     numTestsPerEvictionRun: -1              # Optional
     blockWhenExhausted: true                # Optional
     nettyThreads: 32                        # Optional
     subscriptionsPerConnection: 10          # Optional
     subscriptionConnectionPoolSize: 100     # Optional
     pageSizeInBytes: 8192                   # Optional
     readTimeout: 2000                       # Optional
```

### JICS resource definitions
<a name="ba-runtime-redis-jics-cache"></a>

```
jics:
   resource-definitions:
     store-type: redis
 # If the following redis properties are not specified gapwalk.redis configuration will be used for this cache 
   redis:
     hostName: localhost
     port: 6379
     mode: standalone                        # Optional
     username:                               # Optional
     password: ""                            # Optional
     useSsl: false                           # Optional
     database: 0                             # Optional
     maxTotal: 128                           # Optional
     maxIdle: 128                            # Optional
     minIdle: 16                             # Optional
     testOnBorrow: true                      # Optional
     testOnReturn: true                      # Optional
     testWhileIdle: true                     # Optional
     testOnCreate: true                      # Optional
     minEvictableIdleTimeMillis: 60000       # Optional
     timeBetweenEvictionRunsMillis: 30000    # Optional
     numTestsPerEvictionRun: -1              # Optional
     blockWhenExhausted: true                # Optional
     nettyThreads: 32                        # Optional
     subscriptionsPerConnection: 10          # Optional
     subscriptionConnectionPoolSize: 100     # Optional
     pageSizeInBytes: 8192                   # Optional
     readTimeout: 2000                       # Optional
```

### JICS TS queues
<a name="ba-runtime-jics-ts-queues"></a>

```
jics:
   parameters:
     tsqimpl: redis
 # If the following redis properties are not specified gapwalk.redis configuration will be used for this cache 
   queues:
     ts:
       redis:
         hostName: localhost
         port: 6379
         mode: standalone                        # Optional
         username:                               # Optional
         password: ""                            # Optional
         useSsl: false                           # Optional
         database: 0                             # Optional
         maxTotal: 128                           # Optional
         maxIdle: 128                            # Optional
         minIdle: 16                             # Optional
         testOnBorrow: true                      # Optional
         testOnReturn: true                      # Optional
         testWhileIdle: true                     # Optional
         testOnCreate: true                      # Optional
         minEvictableIdleTimeMillis: 60000       # Optional
         timeBetweenEvictionRunsMillis: 30000    # Optional
         numTestsPerEvictionRun: -1              # Optional
         blockWhenExhausted: true                # Optional
         nettyThreads: 32                        # Optional
         subscriptionsPerConnection: 10          # Optional
         subscriptionConnectionPoolSize: 100     # Optional
         pageSizeInBytes: 8192                   # Optional
         readTimeout: 2000                       # Optional
```

### Session tracker
<a name="ba-runtime-session-tracker"></a>

```
session-tracker:
   store-type: redis
 # If the following redis properties are not specified gapwalk.redis configuration will be used for this cache 
   redis:
     hostName: localhost
     port: 6379
     mode: standalone                        # Optional
     username:                               # Optional
     password: ""                            # Optional
     useSsl: false                           # Optional
     database: 0                             # Optional
     maxTotal: 128                           # Optional
     maxIdle: 128                            # Optional
     minIdle: 16                             # Optional
     testOnBorrow: true                      # Optional
     testOnReturn: true                      # Optional
     testWhileIdle: true                     # Optional
     testOnCreate: true                      # Optional
     minEvictableIdleTimeMillis: 60000       # Optional
     timeBetweenEvictionRunsMillis: 30000    # Optional
     numTestsPerEvictionRun: -1              # Optional
     blockWhenExhausted: true                # Optional
     nettyThreads: 32                        # Optional
     subscriptionsPerConnection: 10          # Optional
     subscriptionConnectionPoolSize: 100     # Optional
     pageSizeInBytes: 8192                   # Optional
     readTimeout: 2000                       # Optional
```

### JCL checkpoint
<a name="ba-runtime-jcl-checkpoint"></a>

```
jcl:
   checkpoint:
     provider: redis
 # If the following redis properties are not specified gapwalk.redis configuration will be used for this cache 
   redis:
     hostname: localhost
     port: 6379
     mode: standalone                        # Optional
     username:                               # Optional
     password: ""                            # Optional
     useSsl: false                           # Optional
     database: 0                             # Optional
     maxTotal: 128                           # Optional
     maxIdle: 128                            # Optional
     minIdle: 16                             # Optional
     testOnBorrow: true                      # Optional
     testOnReturn: true                      # Optional
     testWhileIdle: true                     # Optional
     testOnCreate: true                      # Optional
     minEvictableIdleTimeMillis: 60000       # Optional
     timeBetweenEvictionRunsMillis: 30000    # Optional
   	 numTestsPerEvictionRun: -1              # Optional
     blockWhenExhausted: true                # Optional
     nettyThreads: 32                        # Optional
     subscriptionsPerConnection: 10          # Optional
     subscriptionConnectionPoolSize: 100     # Optional
     pageSizeInBytes: 8192                   # Optional
     readTimeout: 2000                       # Optional
```

### Gapwalk file locks
<a name="ba-runtime-gapwalk-file-locks"></a>

```
filesLocks:
   enabled: true
   retryTime: 1000
   MaxRetry: 5
   provider: redis
 # If the following redis properties are not specified gapwalk.redis configuration will be used for this cache 
   redis:
     hostName: localhost
     port: 6379
     mode: standalone                          # Optional
     username:                                 # Optional
     password: ""                              # Optional
     useSsl: false                             # Optional
     database: 0                               # Optional
     pool:
       maxTotal: 128                           # Optional
       maxIdle: 128                            # Optional
       minIdle: 16                             # Optional
       testOnBorrow: true                      # Optional
       testOnReturn: true                      # Optional
       testWhileIdle: true                     # Optional
       testOnCreate: true                      # Optional
       minEvictableIdleTimeMillis: 60000       # Optional
       timeBetweenEvictionRunsMillis: 30000    # Optional
       numTestsPerEvictionRun: -1              # Optional
       blockWhenExhausted: true                # Optional
       nettyThreads: 32                        # Optional
       subscriptionsPerConnection: 10          # Optional
       subscriptionConnectionPoolSize: 100     # Optional
       pageSizeInBytes: 8192                   # Optional
       readTimeout: 2000                       # Optional
```

### Blu4iv locks
<a name="ba-runtime-blu4iv-locks"></a>

```
 blu4iv.lock: redis
 blu4iv.lock.timeout: 10 #(in millisecondes)
 	# If the following redis properties are not specified gapwalk.redis configuration will be used for this cache 
 blu4iv.lock.redis:
       hostName: localhost
       port: 6379
       mode: standalone                        # Optional
       username:                               # Optional
       password: ""                            # Optional
       useSsl: false                           # Optional
       database: 0                             # Optional
       maxTotal: 128                           # Optional
       maxIdle: 128                            # Optional
       minIdle: 16                             # Optional
       testOnBorrow: true                      # Optional
       testOnReturn: true                      # Optional
       testWhileIdle: true                     # Optional
       testOnCreate: true                      # Optional
       minEvictableIdleTimeMillis: 60000       # Optional
       timeBetweenEvictionRunsMillis: 30000    # Optional
       numTestsPerEvictionRun: -1              # Optional
       blockWhenExhausted: true                # Optional
       nettyThreads: 32                        # Optional
       subscriptionsPerConnection: 10          # Optional
       subscriptionConnectionPoolSize: 100     # Optional
       pageSizeInBytes: 8192                   # Optional
       readTimeout: 2000                       # Optional
```

### Dataset catalog
<a name="ba-runtime-dataset-catalog"></a>

```
datasimplifier:   
   catalogImplementation: redis
   # If the following redis properties are not specified gapwalk.redis configuration will be used for this cache    
   redis:
     hostName: localhost
     port: 6379
     mode: standalone                        # Optional
     username:                               # Optional
     password: ""                            # Optional
     useSsl: false                           # Optional
     database: 0                             # Optional
     maxTotal: 128                           # Optional
     maxIdle: 128                            # Optional
     minIdle: 16                             # Optional
     testOnBorrow: true                      # Optional
     testOnReturn: true                      # Optional
     testWhileIdle: true                     # Optional
     testOnCreate: true                      # Optional
     minEvictableIdleTimeMillis: 60000       # Optional
     timeBetweenEvictionRunsMillis: 30000    # Optional
     numTestsPerEvictionRun: -1              # Optional
     blockWhenExhausted: true                # Optional
     nettyThreads: 32                        # Optional
     subscriptionsPerConnection: 10          # Optional
     subscriptionConnectionPoolSize: 100     # Optional
     pageSizeInBytes: 8192                   # Optional
     readTimeout: 2000                       # Optional
```

## Secret manager for Redis caches
<a name="ba-runtime-redis-secrets-properties"></a>

The `application-main.yaml` file can reference the secret ARN for Redis caches. For information about how to integrate AWS Secrets Manager to securely retrieve Redis connection details at runtime, see [AWS Transform for mainframe Runtime secrets](ba-runtime-config-app-secrets.md).