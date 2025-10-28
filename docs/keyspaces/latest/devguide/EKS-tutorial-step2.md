# Step 2: Configure the application

In this step you build your application that connects to Amazon Keyspaces using the SigV4 plugin.
You can view and download the example Java application from the Amazon Keyspaces example code repo
on [Github](https://github.com/aws-samples/amazon-keyspaces-examples/tree/main/java/datastax-v4/eks "https://github.com/aws-samples/amazon-keyspaces-examples/tree/main/java/datastax-v4/eks"). Or you can follow along using your own application, making sure to complete all configuration steps.

###### Configure your application and add the required dependencies.

1. You can download the example Java application by cloning the Github repository using the following command.

```
git clone https://github.com/aws-samples/amazon-keyspaces-examples.git
```

2. After downloading the Github repo, unzip the downloaded file and navigate to the
   `resources` directory to the
   `application.conf` file.
   1. **Application configuration**

   In this step you configure the SigV4 authentication plugin. You can use the
   following example in your application. If you
   haven't already done so, you need to generate your IAM access keys (an access key
   ID and a secret access key) and save them in your AWS config file or as
   environment variables. For detailed instructions, see [Credentials required by the AWS CLI, the AWS SDK, or the Amazon Keyspaces SigV4 plugin for Cassandra client drivers](SigV4_credentials.md "SigV4_credentials.md"). Update the AWS Region and
   the service endpoint for Amazon Keyspaces as needed. For more service endpoints, see [Service endpoints for Amazon Keyspaces](programmatic.md "programmatic.md"). Replace the truststore location, truststore name, and the truststore password with your own.

   ```
   datastax-java-driver {
     basic.contact-points = ["cassandra.`us-east-1`.amazonaws.com:9142"]
     basic.load-balancing-policy.local-datacenter = "`us-east-1`"
     advanced.auth-provider {
       class = software.aws.mcs.auth.SigV4AuthProvider
       aws-region = "`us-east-1`"
     }
     advanced.ssl-engine-factory {
       class = DefaultSslEngineFactory
       truststore-path = "`truststore_location``truststore_name`.jks"
       truststore-password = "`truststore_password`;"
     }
   }
   ```

   2. **Add the STS module dependency.**

   This adds the ability to use a `WebIdentityTokenCredentialsProvider` that
   returns the AWS credentials that the application needs to provide so that the service account can assume the IAM role. You can do this
   based on the following example.

   ```
           <dependency>
               <groupId>com.amazonaws</groupId>
               <artifactId>aws-java-sdk-sts</artifactId>
               <version>1.11.717</version>
           </dependency>
   ```

   3. **Add the SigV4 dependency.**

   This package implements the SigV4 authentication plugin that is needed to authenticate to Amazon Keyspaces

   ```
           <dependency>
               <groupId>software.aws.mcs</groupId>
               <artifactId>aws-sigv4-auth-cassandra-java-driver-plugin</artifactId>
               <version>4.0.3</version>
           </dependency>
   ```

3. **Add a logging dependency.**

Without logs, troubleshooting connection issues is impossible. In
this tutorial, we use `slf4j` as the logging framework, and use
`logback.xml` to store the log output. We set the logging
level to `debug` to establish the connection. You can use the
following example to add the dependency.

```
        <dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-api</artifactId>
            <version>2.0.5</version>
        </dependency>
```

You can use the following code snippet to configure the logging.

```
<configuration>
    <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">

        <encoder>
            <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>

    <root level="debug">
        <appender-ref ref="STDOUT" />
    </rootv
</configuration>
```

###### Note

The `debug` level is needed to investigate connection failures.
After you have successfully connected to Amazon Keyspaces from your application, you can
change the logging level to `info` or
`warning` as needed.
