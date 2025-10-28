# Step 3: Create the application configuration

file

To use the open-source Spark Cassandra Connector with Amazon Keyspaces, you need to provide an
application configuration file that contains the settings required to connect with the
DataStax Java driver. You can use either service-specific credentials or the SigV4
plugin to connect.

If you haven't already done so, you need to convert the digital certificate used to create the TLS connection
into a trustStore file. You can follow the detailed steps at [Before you
begin](using_java_driver.md#using_java_driver.BeforeYouBegin "using_java_driver.md#using_java_driver.BeforeYouBegin") from the Java driver connection
tutorial. Take note of the trustStore file path and password because you need this
information when you create the application config file.

## Connect with SigV4 authentication

This section shows you an example `application.conf` file that
you can use when connecting with AWS credentials and the SigV4 plugin. If you
haven't already done so, you need to generate your IAM access keys (an access key
ID and a secret access key) and save them in your AWS config file or as
environment variables. For detailed instructions, see [Credentials required by the AWS CLI, the AWS SDK, or the Amazon Keyspaces SigV4 plugin for Cassandra client drivers](SigV4_credentials.md "SigV4_credentials.md").

In the following example, replace the file path to your trustStore file, and
replace the password.

```
datastax-java-driver {
        basic.contact-points = ["cassandra.`us-east-1`.amazonaws.com:9142"]
        basic.load-balancing-policy {
            class = DefaultLoadBalancingPolicy
            local-datacenter = `us-east-1`
            slow-replica-avoidance = false
        }
        basic.request {
              consistency = LOCAL_QUORUM
        }
        advanced {
                auth-provider = {
                   class = software.aws.mcs.auth.SigV4AuthProvider
                   aws-region = `us-east-1`
                 }
            ssl-engine-factory {
                class = DefaultSslEngineFactory
                truststore-path = "`path_to_file`/cassandra_truststore.jks"
                truststore-password = "`password`"
        hostname-validation=false
            }
   }
        advanced.connection.pool.local.size = 3
}
```

Update and save this configuration file as
`/home/user1/application.conf`. The following examples use
this path.

## Connect with service-specific credentials

This section shows you an example `application.conf` file that
you can use when connecting with service-specific credentials. If you haven't
already done so, you need to generate service-specific credentials for Amazon Keyspaces. For
detailed instructions, see [Create service-specific
credentials for programmatic access to Amazon Keyspaces](programmatic.credentials.md "programmatic.credentials.md").

In the following example, replace `username` and `password`
with your own credentials. Also, replace the file path to your trustStore file, and
replace the password.

```
datastax-java-driver {
        basic.contact-points = ["cassandra.`us-east-1`.amazonaws.com:9142"]
        basic.load-balancing-policy {
            class = DefaultLoadBalancingPolicy
            local-datacenter = us-east-1
        }
        basic.request {
              consistency = LOCAL_QUORUM
        }
        advanced {
            auth-provider = {
            class = PlainTextAuthProvider
                    username = "`username`"
                    password = "`password`"
                    aws-region = "`us-east-1`"
            }
            ssl-engine-factory {
                class = DefaultSslEngineFactory
                truststore-path = "`path_to_file`/cassandra_truststore.jks"
                truststore-password = "`password`"
                hostname-validation=false
            }
            metadata = {
                schema {
                     token-map.enabled = true
                }
            }
        }
}
```

Update and save this configuration file as
`/home/user1/application.conf` to use with the code
example.

## Connect with a fixed rate

To force a fixed rate per Spark executor, you can define a request throttler. This
request throttler limits the rate of requests per second. The Spark Cassandra
Connector deploys a Cassandra session per executor. Using the following formula can
help you achieve consistent throughput against a table.

```
max-request-per-second * numberOfExecutors = total throughput against a table
```

You can add this example to the application config file that you created
earlier.

```
datastax-java-driver {
  advanced.throttler {
    class = RateLimitingRequestThrottler

    max-requests-per-second = 3000
    max-queue-size = 30000
    drain-interval = 1 millisecond
  }
}
```
