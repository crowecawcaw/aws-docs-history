# Connecting to Amazon DocumentDB with a MongoDB Java driver

This section provides a step-by-step guide for connecting to Amazon DocumentDB using Java drivers.
This will get you started with integrating DocumentDB into your Java applications.

###### Topics

- [Step 1: Set up your project](#step1-set-up "#step1-set-up")
- [Step 2: Create the connection string](#step2-create-connection-string "#step2-create-connection-string")
- [Step 3: Write the connection code](#step3-write-connect-code "#step3-write-connect-code")
- [Step 4: Handle connection exceptions](#step4-handle-connect-exceptions "#step4-handle-connect-exceptions")
- [Step 5: Running the code](#step5-running-code "#step5-running-code")
- [Connection best practices](#java-connect-best-practices "#java-connect-best-practices")

## Step 1: Set up your project

1. Using Maven, create java project:

```
mvn archetype:generate -DgroupId=com.docdb.guide -DartifactId=my-docdb-project -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
```

2. Add the MongoDB Java driver as a dependency for the project in your ‘pom.xml’ file:

```
<dependency>
    <groupId>org.mongodb</groupId>
    <artifactId>mongodb-driver-sync</artifactId>
    <version>5.3.0</version>
</dependency>
```

## Step 2: Create the connection string

Amazon DocumentDB connection string is essential for establishing a connection between your application and your DocumentDB cluster.
This string encapsulates crucial information such as the cluster endpoint, port, authentication details, and various connection options.
To build a DocumentDB connection string, you typically start with the basic format:

```
"mongodb://`username`:`password`@cluster-endpoint:port/?[connection options]"
```

You'll need to replace "username" and "password" with your actual credentials.
You can find your cluster's endpoint and port number in the AWS Management Console as well as through the AWS CLI.
See [Finding a cluster's endpoints](db-cluster-endpoints-find.md "db-cluster-endpoints-find.md") to find the cluster endpoint for your cluster.
The default port for DocumentDB is 27017.

**Connection string examples**

- Making a connection to DocumentDB using encryption in transit and making sure read requests go to read replicas and write to primary:

```
"mongodb://username:password@cluster-endpoint:27017/?tls=true&
   tlsCAFile=global-bundle.pem&
   readPreference=secondaryPreferred&
   retryWrites=false"
```

- Making a connection to DocumentDB using IAM authentication:

```
"mongodb://cluster-endpoint:27017/?tls=true&
   tlsCAFile=global-bundle.pem&
   readPreference=secondaryPreferred&
   retryWrites=false&
   authSource=%24external&
   authMechanism=MONGODB-AWS"
```

The different options available for the connection string are as follows:

- [TLS certificate](#connection-string-tls "#connection-string-tls")
- [Reading from read replicas](#connection-string-read-rep "#connection-string-read-rep")
- [Write concern and journaling](#connection-string-write-journal "#connection-string-write-journal")
- [RetryWrites](#connection-string-retry-writes "#connection-string-retry-writes")
- [IAM authentication](#connection-string-iam-auth "#connection-string-iam-auth")
- [Connection pool](#connection-string-pool "#connection-string-pool")
- [Connection timeout parameters](#connection-string-timeout "#connection-string-timeout")

### TLS certificate

**`tls=true|false`** — This option enables or disables Transport Layer Security (TLS).
By default, encryption in transit is enabled on Amazon DocumentDB cluster and therefore, unless TLS is disabled at the cluster level, the value for this option should be `true`.

When using TLS, the code needs to provide an SSL certificate when creating connection to a DocumentDB cluster.
Download the certificate that is required to make the secure connection to the cluster: [`global-bundle.pem`](https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem "https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem").
There are two ways to use the `global-bundle.pem` file.

- **Option 1** — Extract all the certificates from the `global-bundle.pem` file and use Java’s keytool to store them in a `.jks` file that can be later used in the code.
  Refer to the Java tab in [Connecting with TLS enabled](connect_programmatically.md#connect_programmatically-tls_enabled "connect_programmatically.md#connect_programmatically-tls_enabled") for the script that shows how to do this.
- **Option 2** — Dynamically add the `global-bundle.pem` file in the code, build an in-memory keystore and use `SSLContext` to provide the certificate as part of making the connection.

### Reading from read replicas

**`replicaSet=rs0&readPreference=secondaryPreferred`** — Specifying these two options routes all the read requests to the read replicas, and write requests to the primary instance.
Using `replicaSet=rs0` in the connection string enables the MongoDB driver to maintain an automatically updated view of the cluster topology, allowing applications to maintain visibility of current node configurations as instances are added or removed.
Not providing these options or specifying `readPreference=primary` sends all the reads and writes to primary instance.
For more options for `readPreference`, see [Read preference options](how-it-works.md#durability-consistency-isolation "how-it-works.md#durability-consistency-isolation").

### Write concern and journaling

Write concern determines the level of acknowledgment requested from the database for write operations.
MongoDB drivers provide an option to tune write concern and journal files.
Amazon DocumentDB doesn’t expect you to set write concern and journal, and ignores the values sent for `w` and `j` (`writeConcern` and `journal`).
DocumentDB always writes data with `writeConcern`: `majority` and `journal`: `true` so the writes are durably recorded on a majority of nodes before sending an acknowledgement to the client.

### RetryWrites

**`retryWrites=false`** — DocumentDB does not support retryable writes and therefore this attribute should always be set to `false`.

### IAM authentication

**`authSource=%24external` and `authMechanism=MONGODB-AWS`** — These two parameters are used to authenticate using AWS Identity and Access Management.
IAM authentication is currently only available in instance-based cluster version 5.0.
For more information, see [Authentication using IAM identity](iam-identity-auth.md "iam-identity-auth.md").

### Connection pool

These options are available for connection pooling:

- **`maxPoolSize`** — Sets the maximum number of connections that can be created in the pool.
  When all connections are in use and a new request comes in, it waits for a connection to become available.
  The default for MongoDB Java drivers is 100.
- **`minPoolSize`** — Indicates the minimum number of connections that should be maintained in the pool at all times.
  The default for MongoDB Java drivers is 0.
- **`maxIdleTimeMS`** — Determines how long a connection can remain idle in the pool before being closed and removed.
  The default for MongoDB Java drivers is 100 milliseconds.
- **`waitQueueTimeoutMS`** — Configures how long a thread should wait for a connection to become available when the pool is at its maximum size.
  If a connection doesn't become available within this time, an exception is thrown.
  The default value for MongoDB Java drivers is 120,000 milliseconds (2 minutes).

### Connection timeout parameters

Timeout is a mechanism to limit the amount of time an operation or connection attempt can take before it is considered failed.
The following timeout parameters are available for preventing indefinite waits and managing resource allocation:

- **`connectTimeoutMS`** — Configures how long the driver will wait to establish a connection to the cluster.
  The default is 10,000 milliseconds (10 seconds).
- **`socketTimeoutMS`** — Specifies how long the driver will wait for a response from the server for a non-write operation.
  The default is 0, (no timeout or infinite).
- **`serverSelectionTimeoutMS`** — Species how long the driver will wait to find an available server in the cluster.
  The default value for this setting is 30 seconds and is sufficient for a new primary instance to be elected during failover.

## Step 3: Write the connection code

The following code example shows how to make a TLS connection to Amazon DocumentDB:

- It creates Java’s [`KeyStore`](https://docs.oracle.com/javase/8/docs/api/java/security/KeyStore.html "https://docs.oracle.com/javase/8/docs/api/java/security/KeyStore.html") and [`SSLContext`>](https://docs.oracle.com/javase/8/docs/api/javax/net/ssl/SSLContext.html "https://docs.oracle.com/javase/8/docs/api/javax/net/ssl/SSLContext.html") objects.
- It also creates the [`MongoClientSettings`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/MongoClientSettings.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/MongoClientSettings.html") object by passing it to the [`ConnectionString`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/ConnectionString.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-core/com/mongodb/ConnectionString.html") object.
  To make TLS connection, you must use the `MongoClientSettings` object to bind the `connectionstring` and `sslcontext`.
- Using [`MongoClients`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/MongoClients.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/MongoClients.html") gets a [`MongoClient`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/MongoClient.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/MongoClient.html") object.

```
public static MongoClient makeDbConnection(String dbName, String DbUserName, String DbPassword,
    String DbClusterEndPoint, String keyStorePass) throws Exception {
    MongoClient connectedClient;
    String connectionOptions = "?replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false";
    String connectionUrl = "mongodb://" + DbUserName + ":" + DbPassword + "@" + DbClusterEndPoint + ":27017/" +
        dbName + connectionOptions;

    try {
        KeyStore trustStore = KeyStore.getInstance(KeyStore.getDefaultType());
        try (FileInputStream fis = new FileInputStream("src/main/resources/certs/truststore.jks")) {
            trustStore.load(fis, keyStorePass.toCharArray());
            TrustManagerFactory tmf = TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm());
            tmf.init(trustStore);

            SSLContext sslContext = SSLContext.getInstance("TLSv1.2");
            sslContext.init(null, tmf.getTrustManagers(), new SecureRandom());
            ConnectionString connectionString = new ConnectionString(connectionUrl);
            MongoClientSettings settings = MongoClientSettings.builder()
                .applyConnectionString(connectionString)
                .applyToSslSettings(builder - > {
                    builder.enabled(true);
                    builder.context(sslContext);
                })
                .build();
            connectedClient = MongoClients.create(settings);
        }
        return connectedClient;
    } catch (MongoException e5) {
        throw new RuntimeException(e5);
    } catch (Exception e) {
        throw new RuntimeException(e);
    }
}
```

## Step 4: Handle connection exceptions

When working with DocumentDB in Java applications, handling connection exceptions is crucial for maintaining robust and reliable database operations.
Properly managing, these exceptions not only help in diagnosing issues quickly, but also ensure that your application can gracefully handle temporary network disruptions or server unavailability, leading to improved stability and user experience.
Some of the critical exceptions related to establishing connection include:

- **`MongoException`** — A general exception and could be issued in various scenarios not covered by more specific exceptions.
  Make sure this exception is handled after all the other specific exceptions as this is a general catch all MongoDB exception.
- **`MongoTimeoutException`** — Issued when an operation times out.
  For example, querying a nonexistent cluster endpoint.
- **`MongoSocketException`** — Issued for network-related issues.
  For example, sudden network disconnection during an operation.
- **`MongoSecurityException`** — Issued when authentication fails.
  For example, connecting with incorrect credentials.
- **`MongoConfigurationException`** — Issued when there is an error in the client configuration.
  For example, using an invalid connection string.

## Step 5: Running the code

The following code sample creates an Amazon DocumentDB connection and prints all the databases:

```
public static void TestConnection() {
    try (MongoClient mongoClient = makeDbConnection(DATABASE_NAME, DB_USER_NAME, DB_PASSWORD, DB_CLUSTER_ENDPOINT, KEYSTORE_PASSWORD)) {
        List < String > databases = mongoClient.listDatabaseNames().into(new ArrayList < > ());
        System.out.println("Databases: " + databases);
    } catch (MongoException e) {
        System.err.println("MongoDB error: " + e.getMessage());
        throw new RuntimeException(e);
    }
}
```

## Connection best practices

The following are best practices to consider when connecting to Amazon DocumentDB with a MongoDB Java driver:

- Always close your [`MongoClient`](https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/MongoClient.html "https://mongodb.github.io/mongo-java-driver/5.3/apidocs/mongodb-driver-sync/com/mongodb/client/MongoClient.html") when you no longer need the client to release resources.
- Handle exceptions appropriately and implement proper error logging.
- Use environment variables or AWS Secrets Manager to store sensitive information like usernames and passwords.
