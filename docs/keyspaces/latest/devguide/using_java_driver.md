# Using a Cassandra Java client driver to

access Amazon Keyspaces programmatically

This section shows you how to connect to Amazon Keyspaces by using a Java client driver.

###### Note

Java 17 and the DataStax Java Driver 4.17 are currently only in Beta support. For more information,
see [https://docs.datastax.com/en/developer/java-driver/4.17/upgrade_guide/](https://docs.datastax.com/en/developer/java-driver/4.17/upgrade_guide/ "https://docs.datastax.com/en/developer/java-driver/4.17/upgrade_guide/").

To provide users and applications with credentials for programmatic access to
Amazon Keyspaces resources, you can do either of the following:

- Create service-specific credentials that are associated with a specific
  AWS Identity and Access Management (IAM) user.
- For enhanced security, we recommend to create IAM access keys
  for IAM identities that are used across all AWS services. The Amazon Keyspaces
  SigV4 authentication plugin for Cassandra client drivers enables you to
  authenticate calls to Amazon Keyspaces using IAM access keys instead of user name and
  password. For more information, see [Create and configure AWS credentials for Amazon Keyspaces](access.md "access.md").

###### Note

For an example how to use Amazon Keyspaces with Spring Boot, see [https://github.com/aws-samples/amazon-keyspaces-examples/tree/main/java/datastax-v4/spring](https://github.com/aws-samples/amazon-keyspaces-examples/tree/main/java/datastax-v4/spring "https://github.com/aws-samples/amazon-keyspaces-examples/tree/main/java/datastax-v4/spring").

###### Topics

- [Before you
  begin](#using_java_driver.BeforeYouBegin "#using_java_driver.BeforeYouBegin")
- [Step-by-step tutorial to connect to Amazon Keyspaces using the
  DataStax Java driver for Apache Cassandra using service-specific credentials](#java_tutorial "#java_tutorial")
- [Step-by-step tutorial to connect to Amazon Keyspaces using the 4.x DataStax Java driver for Apache Cassandra
  and the SigV4 authentication plugin](#java_tutorial.SigV4 "#java_tutorial.SigV4")
- [Connect to Amazon Keyspaces using the 3.x DataStax
  Java driver for Apache Cassandra and the SigV4 authentication plugin](#java3x_tutorial.SigV4 "#java3x_tutorial.SigV4")

## Before you

begin

To connect to Amazon Keyspaces, you need to complete the following tasks before you can start.

1.  Amazon Keyspaces requires the use of Transport Layer Security (TLS) to help secure connections with
    clients.
    1.  Download the following digital certificates and save
        the files locally or in your home directory.

            1. AmazonRootCA1
            2. AmazonRootCA2
            3. AmazonRootCA3
            4. AmazonRootCA4
            5. Starfield Class 2 Root (optional – for backward compatibility)

        To download the certificates, you can use the following commands.

    ```
    curl -O https://www.amazontrust.com/repository/AmazonRootCA1.pem
    curl -O https://www.amazontrust.com/repository/AmazonRootCA2.pem
    curl -O https://www.amazontrust.com/repository/AmazonRootCA3.pem
    curl -O https://www.amazontrust.com/repository/AmazonRootCA4.pem
    curl -O https://certs.secureserver.net/repository/sf-class2-root.crt
    ```

    ###### Note

    Amazon Keyspaces previously used TLS certificates anchored to the Starfield Class 2 CA.
    AWS is migrating all AWS Regions to certificates issued under Amazon Trust Services (Amazon Root CAs 1–4).
    During this transition, configure clients to trust both Amazon Root CAs 1–4 and the Starfield root to ensure compatibility across all Regions. 2. Convert the digital certificates into trustStore files and add them to the keystore.

    ```
    openssl x509 -outform der -in AmazonRootCA1.pem -out temp_file.der
    keytool -import -alias amazon-root-ca-1 -keystore cassandra_truststore.jks -file temp_file.der

    openssl x509 -outform der -in AmazonRootCA2.pem -out temp_file.der
    keytool -import -alias amazon-root-ca-2 -keystore cassandra_truststore.jks -file temp_file.der

    openssl x509 -outform der -in AmazonRootCA3.pem -out temp_file.der
    keytool -import -alias amazon-root-ca-3 -keystore cassandra_truststore.jks -file temp_file.der

    openssl x509 -outform der -in AmazonRootCA4.pem -out temp_file.der
    keytool -import -alias amazon-root-ca-4 -keystore cassandra_truststore.jks -file temp_file.der

    openssl x509 -outform der -in sf-class2-root.crt -out temp_file.der
    keytool -import -alias cassandra -keystore cassandra_truststore.jks -file temp_file.der
    ```

    In the last step, you need to create a password for the keystore and trust each
    certificate. The interactive command looks like this.

    ```
    `Enter keystore password:
    Re-enter new password:
    Owner: CN=Amazon Root CA 1, O=Amazon, C=US
    Issuer: CN=Amazon Root CA 1, O=Amazon, C=US
    Serial number: 66c9fcf99bf8c0a39e2f0788a43e696365bca
    Valid from: Tue May 26 00:00:00 UTC 2015 until: Sun Jan 17 00:00:00 UTC 2038
    Certificate fingerprints:
     SHA1: 8D:A7:F9:65:EC:5E:FC:37:91:0F:1C:6E:59:FD:C1:CC:6A:6E:DE:16
     SHA256: 8E:CD:E6:88:4F:3D:87:B1:12:5B:A3:1A:C3:FC:B1:3D:70:16:DE:7F:57:CC:90:4F:E1:CB:97:C6:AE:98:19:6E
    Signature algorithm name: SHA256withRSA
    Subject Public Key Algorithm: 2048-bit RSA key
    Version: 3

    Extensions:

    #1: ObjectId: 2.5.29.19 Criticality=true
    BasicConstraints:[
     CA:true
     PathLen:2147483647
    ]

    #2: ObjectId: 2.5.29.15 Criticality=true
    KeyUsage [
     DigitalSignature
     Key_CertSign
     Crl_Sign
    ]

    #3: ObjectId: 2.5.29.14 Criticality=false
    SubjectKeyIdentifier [
    KeyIdentifier [
    0000: 84 18 CC 85 34 EC BC 0C 94 94 2E 08 59 9C C7 B2 ....4.......Y...
    0010: 10 4E 0A 08 .N..
    ]
    ]

    Trust this certificate? [no]: yes
    Certificate was added to keystore
    Enter keystore password:
    Owner: CN=Amazon Root CA 2, O=Amazon, C=US
    Issuer: CN=Amazon Root CA 2, O=Amazon, C=US
    Serial number: 66c9fd29635869f0a0fe58678f85b26bb8a37
    Valid from: Tue May 26 00:00:00 UTC 2015 until: Sat May 26 00:00:00 UTC 2040
    Certificate fingerprints:
     SHA1: 5A:8C:EF:45:D7:A6:98:59:76:7A:8C:8B:44:96:B5:78:CF:47:4B:1A
     SHA256: 1B:A5:B2:AA:8C:65:40:1A:82:96:01:18:F8:0B:EC:4F:62:30:4D:83:CE:C4:71:3A:19:C3:9C:01:1E:A4:6D:B4
    Signature algorithm name: SHA384withRSA
    Subject Public Key Algorithm: 4096-bit RSA key
    Version: 3

    Extensions:

    #1: ObjectId: 2.5.29.19 Criticality=true
    BasicConstraints:[
     CA:true
     PathLen:2147483647
    ]

    #2: ObjectId: 2.5.29.15 Criticality=true
    KeyUsage [
     DigitalSignature
     Key_CertSign
     Crl_Sign
    ]

    #3: ObjectId: 2.5.29.14 Criticality=false
    SubjectKeyIdentifier [
    KeyIdentifier [
    0000: B0 0C F0 4C 30 F4 05 58 02 48 FD 33 E5 52 AF 4B ...L0..X.H.3.R.K
    0010: 84 E3 66 52 ..fR
    ]
    ]

    Trust this certificate? [no]: yes
    Certificate was added to keystore
    Enter keystore password:
    Owner: CN=Amazon Root CA 3, O=Amazon, C=US
    Issuer: CN=Amazon Root CA 3, O=Amazon, C=US
    Serial number: 66c9fd5749736663f3b0b9ad9e89e7603f24a
    Valid from: Tue May 26 00:00:00 UTC 2015 until: Sat May 26 00:00:00 UTC 2040
    Certificate fingerprints:
     SHA1: 0D:44:DD:8C:3C:8C:1A:1A:58:75:64:81:E9:0F:2E:2A:FF:B3:D2:6E
     SHA256: 18:CE:6C:FE:7B:F1:4E:60:B2:E3:47:B8:DF:E8:68:CB:31:D0:2E:BB:3A:DA:27:15:69:F5:03:43:B4:6D:B3:A4
    Signature algorithm name: SHA256withECDSA
    Subject Public Key Algorithm: 256-bit EC (secp256r1) key
    Version: 3

    Extensions:

    #1: ObjectId: 2.5.29.19 Criticality=true
    BasicConstraints:[
     CA:true
     PathLen:2147483647
    ]

    #2: ObjectId: 2.5.29.15 Criticality=true
    KeyUsage [
     DigitalSignature
     Key_CertSign
     Crl_Sign
    ]

    #3: ObjectId: 2.5.29.14 Criticality=false
    SubjectKeyIdentifier [
    KeyIdentifier [
    0000: AB B6 DB D7 06 9E 37 AC 30 86 07 91 70 C7 9C C4 ......7.0...p...
    0010: 19 B1 78 C0 ..x.
    ]
    ]

    Trust this certificate? [no]: yes
    Certificate was added to keystore
    Enter keystore password:
    Owner: CN=Amazon Root CA 4, O=Amazon, C=US
    Issuer: CN=Amazon Root CA 4, O=Amazon, C=US
    Serial number: 66c9fd7c1bb104c2943e5717b7b2cc81ac10e
    Valid from: Tue May 26 00:00:00 UTC 2015 until: Sat May 26 00:00:00 UTC 2040
    Certificate fingerprints:
     SHA1: F6:10:84:07:D6:F8:BB:67:98:0C:C2:E2:44:C2:EB:AE:1C:EF:63:BE
     SHA256: E3:5D:28:41:9E:D0:20:25:CF:A6:90:38:CD:62:39:62:45:8D:A5:C6:95:FB:DE:A3:C2:2B:0B:FB:25:89:70:92
    Signature algorithm name: SHA384withECDSA
    Subject Public Key Algorithm: 384-bit EC (secp384r1) key
    Version: 3

    Extensions:

    #1: ObjectId: 2.5.29.19 Criticality=true
    BasicConstraints:[
     CA:true
     PathLen:2147483647
    ]

    #2: ObjectId: 2.5.29.15 Criticality=true
    KeyUsage [
     DigitalSignature
     Key_CertSign
     Crl_Sign
    ]

    #3: ObjectId: 2.5.29.14 Criticality=false
    SubjectKeyIdentifier [
    KeyIdentifier [
    0000: D3 EC C7 3A 65 6E CC E1 DA 76 9A 56 FB 9C F3 86 ...:en...v.V....
    0010: 6D 57 E5 81 mW..
    ]
    ]

    Trust this certificate? [no]: yes
    Certificate was added to keystore
    Enter keystore password:
    Owner: OU=Starfield Class 2 Certification Authority, O="Starfield Technologies, Inc.", C=US
    Issuer: OU=Starfield Class 2 Certification Authority, O="Starfield Technologies, Inc.", C=US
    Serial number: 0
    Valid from: Tue Jun 29 17:39:16 UTC 2004 until: Thu Jun 29 17:39:16 UTC 2034
    Certificate fingerprints:
     SHA1: AD:7E:1C:28:B0:64:EF:8F:60:03:40:20:14:C3:D0:E3:37:0E:B5:8A
     SHA256: 14:65:FA:20:53:97:B8:76:FA:A6:F0:A9:95:8E:55:90:E4:0F:CC:7F:AA:4F:B7:C2:C8:67:75:21:FB:5F:B6:58
    Signature algorithm name: SHA1withRSA (weak)
    Subject Public Key Algorithm: 2048-bit RSA key
    Version: 3

    Extensions:

    #1: ObjectId: 2.5.29.35 Criticality=false
    AuthorityKeyIdentifier [
    KeyIdentifier [
    0000: BF 5F B7 D1 CE DD 1F 86 F4 5B 55 AC DC D7 10 C2 ._.......[U.....
    0010: 0E A9 88 E7 ....
    ]
    [OU=Starfield Class 2 Certification Authority, O="Starfield Technologies, Inc.", C=US]
    SerialNumber: [ 00]
    ]

    #2: ObjectId: 2.5.29.19 Criticality=false
    BasicConstraints:[
     CA:true
     PathLen:2147483647
    ]

    #3: ObjectId: 2.5.29.14 Criticality=false
    SubjectKeyIdentifier [
    KeyIdentifier [
    0000: BF 5F B7 D1 CE DD 1F 86 F4 5B 55 AC DC D7 10 C2 ._.......[U.....
    0010: 0E A9 88 E7 ....
    ]
    ]


    Warning:
    The input uses the SHA1withRSA signature algorithm which is considered a security risk. This algorithm will be disabled in a future update.

    Trust this certificate? [no]: yes
    Certificate was added to keystore`
    ```

2.  Attach the trustStore file in the JVM arguments:

```
-Djavax.net.ssl.trustStore=`path_to_file`/cassandra_truststore.jks
-Djavax.net.ssl.trustStorePassword=`my_password`
```

## Step-by-step tutorial to connect to Amazon Keyspaces using the

DataStax Java driver for Apache Cassandra using service-specific credentials

The following step-by-step tutorial walks you through connecting to Amazon Keyspaces using a
Java driver for Cassandra using service-specific credentials. Specifically, you'll
use the 4.0 version of the DataStax Java driver for Apache Cassandra.

###### Topics

- [Step 1: Prerequisites](#java_tutorial.prereq "#java_tutorial.prereq")
- [Step 2: Configure the
  driver](#java_tutorial.driverconfiguration "#java_tutorial.driverconfiguration")
- [Step 3: Run the sample
  application](#java_tutorial.application "#java_tutorial.application")

### Step 1: Prerequisites

To follow this tutorial, you need to generate service-specific
credentials and add the DataStax Java driver for Apache Cassandra to your
Java project.

- Generate service-specific credentials for your Amazon Keyspaces IAM user by completing the steps in
  [Create service-specific
  credentials for programmatic access to Amazon Keyspaces](programmatic.credentials.md "programmatic.credentials.md"). If you prefer to use
  IAM access keys for authentication, see [Step-by-step tutorial to connect to Amazon Keyspaces using the 4.x DataStax Java driver for Apache Cassandra
  and the SigV4 authentication plugin](#java_tutorial.SigV4 "#java_tutorial.SigV4").
- Add the DataStax Java driver for Apache Cassandra to your Java project. Ensure that you're
  using a version of the driver that supports Apache Cassandra
  3.11.2. For more information, see the [DataStax Java driver
  for Apache Cassandra documentation](https://github.com/datastax/java-driver "https://github.com/datastax/java-driver").

### Step 2: Configure the

driver

You can specify settings for the DataStax Java Cassandra
driver by creating a configuration file for your application. This configuration file overrides the default settings and tells the driver
to connect to the Amazon Keyspaces service endpoint using port 9142. For a list of available service endpoints, see [Service endpoints for Amazon Keyspaces](programmatic.md "programmatic.md").

Create a configuration file and save the file in the application's
resources folder—for example,
`src/main/resources/application.conf`. Open
`application.conf` and add the following
configuration settings.

1. Authentication provider – Create the authentication
   provider with the `PlainTextAuthProvider` class.
   `ServiceUserName` and
   `ServicePassword` should match the
   user name and password you obtained when you generated the
   service-specific credentials by following the steps in [Create service-specific
   credentials for programmatic access to Amazon Keyspaces](programmatic.credentials.md "programmatic.credentials.md").

###### Note

You can use short-term credentials by using the authentication plugin for the DataStax Java
driver for Apache Cassandra instead of hardcoding credentials in
your driver configuration file. To learn more, follow the
instructions for the [Step-by-step tutorial to connect to Amazon Keyspaces using the 4.x DataStax Java driver for Apache Cassandra
and the SigV4 authentication plugin](#java_tutorial.SigV4 "#java_tutorial.SigV4"). 2. Local data center – Set the value for
`local-datacenter` to the Region you're
connecting to. For example, if the application is connecting to
`cassandra.us-east-2.amazonaws.com`, then set the
local data center to `us-east-2`. For all available
AWS Regions, see [Service endpoints for Amazon Keyspaces](programmatic.md "programmatic.md"). Set `slow-replica-avoidance = false` to load balance against fewer nodes. 3. SSL/TLS – Initialize the SSLEngineFactory by adding a
section in the configuration file with a single line that specifies the
class with `class = DefaultSslEngineFactory`. Provide the
path to the trustStore file and the password that you created
previously. Amazon Keyspaces doesn't support `hostname-validation` of peers, so set this option to false.

```
datastax-java-driver {

    basic.contact-points = [ "`cassandra.us-east-2.amazonaws.com`:9142"]
    advanced.auth-provider{
        class = PlainTextAuthProvider
        username = `"ServiceUserName"`
        password = `"ServicePassword"`
    }
    basic.load-balancing-policy {
        local-datacenter = `"us-east-2"`
        slow-replica-avoidance = false
    }

    advanced.ssl-engine-factory {
        class = DefaultSslEngineFactory
        truststore-path = `"./src/main/resources/cassandra_truststore.jks"`
        truststore-password = `"my_password"`
        hostname-validation = false
      }
}
```

###### Note

Instead of adding the path to the trustStore in the configuration file, you can also add
the trustStore path directly in the application code or you can add the path
to the trustStore to your JVM arguments.

### Step 3: Run the sample

application

This code example shows a simple command line application that creates a
connection pool to Amazon Keyspaces by using the configuration file we created
earlier. It confirms that the connection is established by running a
simple query.

```
package `<your package>`;
// add the following imports to your project
import com.datastax.oss.driver.api.core.CqlSession;
import com.datastax.oss.driver.api.core.config.DriverConfigLoader;
import com.datastax.oss.driver.api.core.cql.ResultSet;
import com.datastax.oss.driver.api.core.cql.Row;

public class App
{

    public static void main( String[] args )
    {
        //Use DriverConfigLoader to load your configuration file
        DriverConfigLoader loader = DriverConfigLoader.fromClasspath("application.conf");
        try (CqlSession session = CqlSession.builder()
                .withConfigLoader(loader)
                .build()) {

            ResultSet rs = session.execute("select * from system_schema.keyspaces");
            Row row = rs.one();
            System.out.println(row.getString("keyspace_name"));
        }
    }
}
```

###### Note

Use a `try` block to establish the connection to ensure that it's
always closed. If you don't use a `try` block, remember
to close your connection to avoid leaking resources.

## Step-by-step tutorial to connect to Amazon Keyspaces using the 4.x DataStax Java driver for Apache Cassandra

and the SigV4 authentication plugin

The following section describes how to use the SigV4 authentication
plugin for the open-source 4.x DataStax Java driver for Apache Cassandra to access
Amazon Keyspaces (for Apache Cassandra). The plugin is available from the [GitHub
repository](https://github.com/aws/aws-sigv4-auth-cassandra-java-driver-plugin "https://github.com/aws/aws-sigv4-auth-cassandra-java-driver-plugin").

The SigV4 authentication plugin allows you to use IAM credentials for users or
roles when connecting to Amazon Keyspaces. Instead of requiring a user name and password, this
plugin signs API requests using access keys. For more information, see [Create and configure AWS credentials for Amazon Keyspaces](access.md "access.md").

### Step 1: Prerequisites

To follow this tutorial, you need to complete the following tasks.

- If you haven't already done so, create credentials for your IAM user or role following the
  steps at [Create and configure AWS credentials for Amazon Keyspaces](access.md "access.md"). This tutorial assumes
  that the access keys are stored as environment variables. For more information,
  see [Store access keys for programmatic access](aws.credentials.md "aws.credentials.md").
- Add the DataStax Java driver for Apache Cassandra to your Java project. Ensure that you're
  using a version of the driver that supports Apache Cassandra
  3.11.2. For more information, see the [DataStax Java Driver
  for Apache Cassandra documentation](https://github.com/datastax/java-driver "https://github.com/datastax/java-driver").
- Add the authentication plugin to your application. The authentication plugin supports version
  4.x of the DataStax Java driver for Apache Cassandra. If you’re using
  Apache Maven, or a build system that can use Maven dependencies, add the
  following dependencies to your `pom.xml` file.

###### Important

Replace the version of the plugin with the latest version as shown at
[GitHub repository](https://github.com/aws/aws-sigv4-auth-cassandra-java-driver-plugin#add-the-authentication-plugin-to-the-application "https://github.com/aws/aws-sigv4-auth-cassandra-java-driver-plugin#add-the-authentication-plugin-to-the-application").

```
<dependency>
        <groupId>software.aws.mcs</groupId>
        <artifactId>aws-sigv4-auth-cassandra-java-driver-plugin</artifactId>
        <version>`4.0.9`</version>
</dependency>
```

### Step 2: Configure the

driver

You can specify settings for the DataStax Java Cassandra
driver by creating a configuration file for your application. This configuration file overrides the default settings and tells the driver
to connect to the Amazon Keyspaces service endpoint using port 9142. For a list of available service endpoints, see [Service endpoints for Amazon Keyspaces](programmatic.md "programmatic.md").

Create a configuration file and save the file in the application's
resources folder—for example,
`src/main/resources/application.conf`. Open
`application.conf` and add the following
configuration settings.

1. Authentication provider – Set the `advanced.auth-provider.class` to a new instance of
   `software.aws.mcs.auth.SigV4AuthProvider`.
   The SigV4AuthProvider is the authentication handler provided by the plugin for performing SigV4 authentication.
2. Local data center – Set the value for
   `local-datacenter` to the Region you're connecting to.
   For example, if the application is connecting to
   `cassandra.us-east-2.amazonaws.com`, then set the local
   data center to `us-east-2`. For all available AWS Regions,
   see [Service endpoints for Amazon Keyspaces](programmatic.md "programmatic.md"). Set
   `slow-replica-avoidance = false` to load balance against
   all available nodes.
3. Idempotence – Set the default `idempotence`
   for the application to `true` to configure the driver to
   always retry failed read/write/prepare/execute requests. This is a best
   practice for distributed applications that helps to handle transient
   failures by retrying failed requests.
4. SSL/TLS – Initialize the SSLEngineFactory by adding a
   section in the configuration file with a single line that
   specifies the class with `class =
DefaultSslEngineFactory`. Provide the path to the
   trustStore file and the password that you created
   previously. Amazon Keyspaces doesn't support `hostname-validation` of peers, so set this option to false.
5. Connections – Create at least 3 local connections per
   endpoint by setting `local.size = 3`. This is a best practice
   that helps your application to handle overhead and traffic bursts. For
   more information about how to calculate how many local connections per
   endpoint your application needs based on expected traffic patterns, see
   [How to configure connections in Amazon Keyspaces](connections.md#connections.howtoconfigure "connections.md#connections.howtoconfigure").
6. Retry policy – Implement the Amazon Keyspaces retry policy
   `AmazonKeyspacesExponentialRetryPolicy` instead of the
   `DefaultRetryPolicy` that comes with the Cassandra
   driver. This allows you to configure the number of retry attempts for
   the `AmazonKeyspacesExponentialRetryPolicy` that meets your
   needs. By default, the number of retry attempts for the
   `AmazonKeyspacesExponentialRetryPolicy` is set to 3. For
   more information, see [How to configure the retry policy for connections in Amazon Keyspaces](connections.md#connections.retry-policies "connections.md#connections.retry-policies").
7. Prepared statements – Set `prepare-on-all-nodes`
   to false to optimize network usage.

```
datastax-java-driver {
    basic {
        contact-points = [ "`cassandra.us-east-2.amazonaws.com:9142`"]
        request {
            timeout = 2 seconds
            consistency = LOCAL_QUORUM
            page-size = 1024
            default-idempotence = true
        }
        load-balancing-policy {
            local-datacenter = "`us-east-2`"
            class = DefaultLoadBalancingPolicy
            slow-replica-avoidance = false
        }
    }
    advanced {
        auth-provider {
            class = software.aws.mcs.auth.SigV4AuthProvider
            aws-region = `us-east-2`
        }
        ssl-engine-factory {
            class = DefaultSslEngineFactory
            truststore-path = "`./src/main/resources/cassandra_truststore.jks`"
            truststore-password = "`my_password`"
            hostname-validation = false
        }
        connection {
	     connect-timeout = 5 seconds
	     max-requests-per-connection = 512
	     pool {
                local.size = 3
	     }
        }
       retry-policy {
           class =  com.aws.ssa.keyspaces.retry.AmazonKeyspacesExponentialRetryPolicy
	    max-attempts = 3
	    min-wait = 10 mills
	    max-wait = 100 mills
       }
       prepared-statements {
	    prepare-on-all-nodes = false
       }
    }
}
```

###### Note

Instead of adding the path to the trustStore in the configuration file, you can also add
the trustStore path directly in the application code or
you can add the path to the trustStore to your JVM
arguments.

### Step 3: Run the application

This code example shows a simple command line application that creates a
connection pool to Amazon Keyspaces by using the configuration file we created
earlier. It confirms that the connection is established by running a
simple query.

```
package `<your package>`;
// add the following imports to your project
import com.datastax.oss.driver.api.core.CqlSession;
import com.datastax.oss.driver.api.core.config.DriverConfigLoader;
import com.datastax.oss.driver.api.core.cql.ResultSet;
import com.datastax.oss.driver.api.core.cql.Row;

public class App
{

    public static void main( String[] args )
    {
        //Use DriverConfigLoader to load your configuration file
        DriverConfigLoader loader = DriverConfigLoader.fromClasspath("application.conf");
        try (CqlSession session = CqlSession.builder()
                .withConfigLoader(loader)
                .build()) {

            ResultSet rs = session.execute("select * from system_schema.keyspaces");
            Row row = rs.one();
            System.out.println(row.getString("keyspace_name"));
        }
    }
}
```

###### Note

Use a `try` block to establish the connection to ensure that it's
always closed. If you don't use a `try` block, remember
to close your connection to avoid leaking resources.

## Connect to Amazon Keyspaces using the 3.x DataStax

Java driver for Apache Cassandra and the SigV4 authentication plugin

The following section describes how to use the SigV4 authentication plugin for
the 3.x open-source DataStax Java driver for Apache Cassandra to access Amazon Keyspaces. The
plugin is available from the [GitHub repository](https://github.com/aws/aws-sigv4-auth-cassandra-java-driver-plugin/tree/3.x-Driver-Compatible "https://github.com/aws/aws-sigv4-auth-cassandra-java-driver-plugin/tree/3.x-Driver-Compatible").

The SigV4 authentication plugin allows you to use IAM credentials for users
and roles when connecting to Amazon Keyspaces. Instead of requiring a user name and password,
this plugin signs API requests using access keys. For more information,
see [Create and configure AWS credentials for Amazon Keyspaces](access.md "access.md").

### Step 1: Prerequisites

To run this code sample, you first need to complete the following
tasks.

- Create credentials for your IAM user or role following the steps at [Create and configure AWS credentials for Amazon Keyspaces](access.md "access.md"). This tutorial assumes that the
  access keys are stored as environment variables. For more information,
  see [Store access keys for programmatic access](aws.credentials.md "aws.credentials.md").
- Follow the steps at [Before you
  begin](#using_java_driver.BeforeYouBegin "#using_java_driver.BeforeYouBegin") to download the
  digital certificates, convert them to trustStore files, and attach the keystore in the JVM arguments to your application.
- Add the DataStax Java driver for Apache Cassandra to your Java project. Ensure that you're
  using a version of the driver that supports Apache Cassandra
  3.11.2. For more information, see the [DataStax Java Driver
  for Apache Cassandra documentation](https://github.com/datastax/java-driver "https://github.com/datastax/java-driver").
- Add the authentication plugin to your application. The authentication plugin supports version
  3.x of the DataStax Java driver for Apache Cassandra. If you’re using
  Apache Maven, or a build system that can use Maven dependencies, add the
  following dependencies to your `pom.xml` file.
  Replace the version of the plugin with the latest version as shown at
  [GitHub repository](https://github.com/aws/aws-sigv4-auth-cassandra-java-driver-plugin/tree/3.x-Driver-Compatible "https://github.com/aws/aws-sigv4-auth-cassandra-java-driver-plugin/tree/3.x-Driver-Compatible").

```
<dependency>
        <groupId>software.aws.mcs</groupId>
        <artifactId>aws-sigv4-auth-cassandra-java-driver-plugin_3</artifactId>
        <version>`3.0.3`</version>
</dependency>
```

### Step 2: Run the application

This code example shows a simple command line application that creates a
connection pool to Amazon Keyspaces. It confirms that the connection is established by
running a simple query.

```
package `<your package>`;
// add the following imports to your project

import software.aws.mcs.auth.SigV4AuthProvider;
import com.datastax.driver.core.Cluster;
import com.datastax.driver.core.ResultSet;
import com.datastax.driver.core.Row;
import com.datastax.driver.core.Session;

public class App
{

    public static void main( String[] args )
    {
        String endPoint = "`cassandra.us-east-2.amazonaws.com`";
        int portNumber = 9142;
        Session session = Cluster.builder()
	                                 .addContactPoint(endPoint)
	                                 .withPort(portNumber)
	                                 .withAuthProvider(new SigV4AuthProvider("`us-east-2`"))
	                                 .withSSL()
	                                 .build()
	                                 .connect();

        ResultSet rs = session.execute("select * from system_schema.keyspaces");
        Row row = rs.one();
        System.out.println(row.getString("keyspace_name"));
    }
}
```

Usage notes:

For a list of available endpoints, see [Service endpoints for Amazon Keyspaces](programmatic.md "programmatic.md").

See the following repository for helpful Java driver policies, examples, and best practices
when using the Java Driver with Amazon Keyspaces:

[https://github.com/aws-samples/amazon-keyspaces-java-driver-helpers](https://github.com/aws-samples/amazon-keyspaces-java-driver-helpers "https://github.com/aws-samples/amazon-keyspaces-java-driver-helpers").
