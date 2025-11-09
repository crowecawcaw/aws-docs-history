# AWS X-Ray SDK for Java

###### Note

End-of-support notice – On February 25th, 2027, AWS X-Ray will discontinue support for AWS X-Ray SDKs and daemon. After February 25th, 2027, you will no longer receive updates or releases. For more information on the support timeline, see
[X-Ray SDK and daemon end of support timeline](xray-daemon-eos.md "xray-daemon-eos.md"). We recommend to migrate to OpenTelemetry. For more information on migrating to OpenTelemetry, see [Migrating from X-Ray instrumentation to OpenTelemetry instrumentation](xray-sdk-migration.md "xray-sdk-migration.md") .

The X-Ray SDK for Java is a set of libraries for Java web applications that provide classes and methods for
generating and sending trace data to the X-Ray daemon. Trace data includes information about incoming HTTP requests
served by the application, and calls that the application makes to downstream services using the AWS SDK, HTTP
clients, or an SQL database connector. You can also create segments manually and add debug information in
annotations and metadata.

The X-Ray SDK for Java is an open source project. You can follow the project and submit issues and pull requests
on GitHub: [github.com/aws/aws-xray-sdk-java](https://github.com/aws/aws-xray-sdk-java "https://github.com/aws/aws-xray-sdk-java")

Start by [adding AWSXRayServletFilter as a servlet
filter](xray-sdk-java-filters.md "xray-sdk-java-filters.md") to trace incoming requests. A servlet filter creates a [segment](xray-concepts.md#xray-concepts-segments "xray-concepts.md#xray-concepts-segments"). While the segment is open, you can use the SDK client's methods to add information to the segment
and create subsegments to trace downstream calls. The SDK also automatically records exceptions that your
application throws while the segment is open.

Starting in release 1.3, you can instrument your application using [aspect-oriented programming (AOP) in Spring](xray-sdk-java-aop-spring.md "xray-sdk-java-aop-spring.md"). What this means is that you can instrument your application,
while it is running on AWS, without adding any code to your application's runtime.

Next, use the X-Ray SDK for Java to instrument your AWS SDK for Java clients by [including the SDK Instrumentor submodule](#xray-sdk-java-dependencies "#xray-sdk-java-dependencies") in your build configuration. Whenever you make a call to a
downstream AWS service or resource with an instrumented client, the SDK records information about the call in a
subsegment. AWS services and the resources that you access within the services appear as downstream nodes on the
trace map to help you identify errors and throttling issues on individual connections.

If you don't want to instrument all downstream calls to AWS services, you can leave out the Instrumentor
submodule and choose which clients to instrument. Instrument individual clients by [adding a TracingHandler](xray-sdk-java-awssdkclients.md "xray-sdk-java-awssdkclients.md") to an AWS SDK service
client.

Other X-Ray SDK for Java submodules provide instrumentation for downstream calls to HTTP web APIs and SQL databases.
You can [use the X-Ray SDK for Java versions of HTTPClient and
HTTPClientBuilder](xray-sdk-java-httpclients.md "xray-sdk-java-httpclients.md") in the Apache HTTP submodule to instrument Apache HTTP clients. To
instrument SQL queries, [add the SDK's interceptor to your data
source](xray-sdk-java-sqlclients.md "xray-sdk-java-sqlclients.md").

After you start using the SDK, customize its behavior by [configuring
the recorder and servlet filter](xray-sdk-java-configuration.md "xray-sdk-java-configuration.md"). You can add plugins to record data about the compute resources running
your application, customize sampling behavior by defining sampling rules, and set the log level to see more or less
information from the SDK in your application logs.

Record additional information about requests and the work that your application does in [annotations and metadata](xray-sdk-java-segment.md "xray-sdk-java-segment.md"). Annotations are simple key-value pairs that are
indexed for use with [filter expressions](xray-console-filters.md "xray-console-filters.md"), so that you can search for
traces that contain specific data. Metadata entries are less restrictive and can record entire objects and arrays
— anything that can be serialized into JSON.

###### Annotations and Metadata

Annotations and metadata are arbitrary text that you add to segments with the X-Ray SDK.
Annotations are indexed for use with filter expressions. Metadata are not indexed, but can be
viewed in the raw segment with the X-Ray console or API. Anyone that you grant read access to
X-Ray can view this data.

When you have a lot of instrumented clients in your code, a single request segment can contain many subsegments,
one for each call made with an instrumented client. You can organize and group subsegments by wrapping client calls
in [custom subsegments](xray-sdk-java-subsegments.md "xray-sdk-java-subsegments.md"). You can create a custom subsegment for an
entire function or any section of code, and record metadata and annotations on the subsegment instead of writing
everything on the parent segment.

## Submodules

You can download the X-Ray SDK for Java from Maven. The X-Ray SDK for Java is split into submodules by use case, with
a bill of materials for version management:

- [`aws-xray-recorder-sdk-core`](https://mvnrepository.com/artifact/com.amazonaws/aws-xray-recorder-sdk-core/ "https://mvnrepository.com/artifact/com.amazonaws/aws-xray-recorder-sdk-core/") (required) – Basic functionality for creating segments
  and transmitting segments. Includes `AWSXRayServletFilter` for instrumenting incoming
  requests.
- [`aws-xray-recorder-sdk-aws-sdk`](https://mvnrepository.com/artifact/com.amazonaws/aws-xray-recorder-sdk-aws-sdk/ "https://mvnrepository.com/artifact/com.amazonaws/aws-xray-recorder-sdk-aws-sdk/") – Instruments calls to AWS services made with
  AWS SDK for Java clients by adding a tracing client as a request handler.
- [`aws-xray-recorder-sdk-aws-sdk-v2`](https://mvnrepository.com/artifact/com.amazonaws/aws-xray-recorder-sdk-aws-sdk-v2/ "https://mvnrepository.com/artifact/com.amazonaws/aws-xray-recorder-sdk-aws-sdk-v2/") – Instruments calls to AWS services made with
  AWS SDK for Java 2.2 and later clients by adding a tracing client as a request intereceptor.
- [`aws-xray-recorder-sdk-aws-sdk-instrumentor`](https://mvnrepository.com/artifact/com.amazonaws/aws-xray-recorder-sdk-aws-sdk-instrumentor/ "https://mvnrepository.com/artifact/com.amazonaws/aws-xray-recorder-sdk-aws-sdk-instrumentor/") – With
  `aws-xray-recorder-sdk-aws-sdk`, instruments all AWS SDK for Java clients automatically.
- [`aws-xray-recorder-sdk-aws-sdk-v2-instrumentor`](https://mvnrepository.com/artifact/com.amazonaws/aws-xray-recorder-sdk-aws-sdk-v2-instrumentor/ "https://mvnrepository.com/artifact/com.amazonaws/aws-xray-recorder-sdk-aws-sdk-v2-instrumentor/") – With
  `aws-xray-recorder-sdk-aws-sdk-v2`, instruments all AWS SDK for Java 2.2 and later clients automatically.
- [`aws-xray-recorder-sdk-apache-http`](https://mvnrepository.com/artifact/com.amazonaws/aws-xray-recorder-sdk-apache-http/ "https://mvnrepository.com/artifact/com.amazonaws/aws-xray-recorder-sdk-apache-http/") – Instruments outbound HTTP calls made with Apache
  HTTP clients.
- [`aws-xray-recorder-sdk-spring`](https://mvnrepository.com/artifact/com.amazonaws/aws-xray-recorder-sdk-spring/ "https://mvnrepository.com/artifact/com.amazonaws/aws-xray-recorder-sdk-spring/") – Provides interceptors for Spring AOP Framework
  applications.
- [`aws-xray-recorder-sdk-sql-postgres`](https://mvnrepository.com/artifact/com.amazonaws/aws-xray-recorder-sdk-sql-postgres/ "https://mvnrepository.com/artifact/com.amazonaws/aws-xray-recorder-sdk-sql-postgres/") – Instruments outbound calls to a PostgreSQL
  database made with JDBC.
- [`aws-xray-recorder-sdk-sql-mysql`](https://mvnrepository.com/artifact/com.amazonaws/aws-xray-recorder-sdk-sql-mysql/ "https://mvnrepository.com/artifact/com.amazonaws/aws-xray-recorder-sdk-sql-mysql/") – Instruments outbound calls to a MySQL database
  made with JDBC.
- [`aws-xray-recorder-sdk-bom`](https://mvnrepository.com/artifact/com.amazonaws/aws-xray-recorder-sdk-bom/ "https://mvnrepository.com/artifact/com.amazonaws/aws-xray-recorder-sdk-bom/") – Provides a bill of materials that you can use to specify
  the version to use for all submodules.
- [`aws-xray-recorder-sdk-metrics`](https://mvnrepository.com/artifact/com.amazonaws/aws-xray-recorder-sdk-metrics/ "https://mvnrepository.com/artifact/com.amazonaws/aws-xray-recorder-sdk-metrics/") – Publish unsampled Amazon CloudWatch metrics from your
  collected X-Ray segments.

If you use Maven or Gradle to build your application, [add the
X-Ray SDK for Java to your build configuration](#xray-sdk-java-dependencies "#xray-sdk-java-dependencies").

For reference documentation of the SDK's classes and methods, see [AWS X-Ray SDK for Java API Reference](../../../xray-sdk-for-java/latest/javadoc.md "../../../xray-sdk-for-java/latest/javadoc.md").

## Requirements

The X-Ray SDK for Java requires Java 8 or later, Servlet API 3, the AWS SDK, and Jackson.

The SDK depends on the following libraries at compile and runtime:

- AWS SDK for Java version 1.11.398 or later
- Servlet API 3.1.0

These dependencies are declared in the SDK's `pom.xml` file and are included automatically
if you build using Maven or Gradle.

If you use a library that is included in the X-Ray SDK for Java, you must use the included version. For example,
if you already depend on Jackson at runtime and include JAR files in your deployment for that dependency, you must
remove those JAR files because the SDK JAR includes its own versions of Jackson libraries.

## Dependency management

The X-Ray SDK for Java is available from Maven:

- **Group** – `com.amazonaws`
- **Artifact** – `aws-xray-recorder-sdk-bom`
- **Version** – `2.11.0`

If you use Maven to build your application, add the SDK as a dependency in your `pom.xml`
file.

###### Example pom.xml - dependencies

```
<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>com.amazonaws</groupId>
      <artifactId>aws-xray-recorder-sdk-bom</artifactId>
      <version>2.11.0</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
  </dependencies>
</dependencyManagement>
<dependencies>
  <dependency>
    <groupId>com.amazonaws</groupId>
    <artifactId>aws-xray-recorder-sdk-core</artifactId>
  </dependency>
  <dependency>
    <groupId>com.amazonaws</groupId>
    <artifactId>aws-xray-recorder-sdk-apache-http</artifactId>
  </dependency>
  <dependency>
    <groupId>com.amazonaws</groupId>
    <artifactId>aws-xray-recorder-sdk-aws-sdk</artifactId>
  </dependency>
  <dependency>
    <groupId>com.amazonaws</groupId>
    <artifactId>aws-xray-recorder-sdk-aws-sdk-instrumentor</artifactId>
  </dependency>
  <dependency>
    <groupId>com.amazonaws</groupId>
    <artifactId>aws-xray-recorder-sdk-sql-postgres</artifactId>
  </dependency>
  <dependency>
    <groupId>com.amazonaws</groupId>
    <artifactId>aws-xray-recorder-sdk-sql-mysql</artifactId>
  </dependency>
</dependencies>
```

For Gradle, add the SDK as a compile-time dependency in your `build.gradle` file.

###### Example build.gradle - dependencies

```
dependencies {
  compile("org.springframework.boot:spring-boot-starter-web")
  testCompile("org.springframework.boot:spring-boot-starter-test")
  compile("com.amazonaws:aws-java-sdk-dynamodb")
  `compile("com.amazonaws:aws-xray-recorder-sdk-core")
 compile("com.amazonaws:aws-xray-recorder-sdk-aws-sdk")
 compile("com.amazonaws:aws-xray-recorder-sdk-aws-sdk-instrumentor")
 compile("com.amazonaws:aws-xray-recorder-sdk-apache-http")
 compile("com.amazonaws:aws-xray-recorder-sdk-sql-postgres")
 compile("com.amazonaws:aws-xray-recorder-sdk-sql-mysql")`
  testCompile("junit:junit:4.11")
}
dependencyManagement {
    imports {
        mavenBom('com.amazonaws:aws-java-sdk-bom:1.11.39')
        `mavenBom('com.amazonaws:aws-xray-recorder-sdk-bom:2.11.0')`
    }
}
```

If you use Elastic Beanstalk to deploy your application, you can use Maven or Gradle to build on-instance each time you
deploy, instead of building and uploading a large archive that includes all of your dependencies. See the [sample application](xray-scorekeep.md "xray-scorekeep.md") for an example that uses Gradle.

## AWS X-Ray metrics for the X-Ray SDK for Java

###### Note

End-of-support notice – On February 25th, 2027, AWS X-Ray will discontinue support for AWS X-Ray SDKs and daemon. After February 25th, 2027, you will no longer receive updates or releases. For more information on the support timeline, see
[X-Ray SDK and daemon end of support timeline](xray-daemon-eos.md "xray-daemon-eos.md"). We recommend to migrate to OpenTelemetry. For more information on migrating to OpenTelemetry, see [Migrating from X-Ray instrumentation to OpenTelemetry instrumentation](xray-sdk-migration.md "xray-sdk-migration.md") .

This topic describes the AWS X-Ray namespace, metrics, and dimensions. You can use the
X-Ray SDK for Java to publish unsampled Amazon CloudWatch metrics from your collected X-Ray segments. These
metrics are derived from the segment’s start and end time, and the error, fault, and throttled
status flags. Use these trace metrics to expose retries and dependency issues within subsegments.

CloudWatch is a metrics repository. A metric is the fundamental concept in CloudWatch and represents a
time-ordered set of data points. You (or AWS services) publish metrics data points into CloudWatch and
you retrieve statistics about those data points as an ordered set of time-series data.

Metrics are uniquely defined by a name, a namespace, and one or more dimensions. Each data
point has a timestamp and, optionally, a unit of measure. When you request statistics, the
returned data stream is identified by namespace, metric name, and dimension.

For more information about CloudWatch, see the [_Amazon CloudWatch User
Guide_](../../../AmazonCloudWatch/latest/DeveloperGuide.md "../../../AmazonCloudWatch/latest/DeveloperGuide.md").

### X-Ray CloudWatch metrics

The `ServiceMetrics/SDK` namespace includes the following metrics.

| Metric         | Statistics available             | Description                                                                                                                                   | Units        |
| -------------- | -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| `Latency`      | Average, Minimum, Maximum, Count | The difference between the start and end time. Average, minimum, and maximum all<br>describe operational latency. Count describes call count. | Milliseconds |
| `ErrorRate`    | Average, Sum                     | The rate of requests that failed with a `4xx Client Error` status code,<br>resulting in an error.                                             | Percent      |
| `FaultRate`    | Average, Sum                     | The rate of traces that failed with a `5xx Server Error` status code,<br>resulting in a fault.                                                | Percent      |
| `ThrottleRate` | Average, Sum                     | The rate of throttled traces that return a `429` status code. This is a<br>subset of the `ErrorRate` metric.                                  | Percent      |
| `OkRate`       | Average, Sum                     | The rate of traced requests resulting in an `OK` status code.                                                                                 | Percent      |

### X-Ray CloudWatch dimensions

Use the dimensions in the following table to refine the metrics returned for your X-Ray
instrumented Java applications.

| Dimension     | Description                                                                            |
| ------------- | -------------------------------------------------------------------------------------- |
| `ServiceType` | The type of the service, for example, `AWS::EC2::Instance` or<br>`NONE`, if not known. |
| `ServiceName` | The canonical name for the service.                                                    |

### Enable X-Ray CloudWatch metrics

Use the following procedure to enable trace metrics in your instrumented Java
application.

###### To configure trace metrics

1. Add the `aws-xray-recorder-sdk-metrics` package as an Apache Maven dependency. For more
   information, see [X-Ray SDK for Java
   Submodules](#xray-sdk-java-submodules "#xray-sdk-java-submodules").
2. Enable a new `MetricsSegmentListener()` as part of the global recorder
   build.

###### Example src/com/myapp/web/Startup.java

```
import com.amazonaws.xray.AWSXRay;
import com.amazonaws.xray.AWSXRayRecorderBuilder;
import com.amazonaws.xray.plugins.EC2Plugin;
import com.amazonaws.xray.plugins.ElasticBeanstalkPlugin;
import com.amazonaws.xray.strategy.sampling.LocalizedSamplingStrategy;

@Configuration
public class WebConfig {
...
  static {
    AWSXRayRecorderBuilder builder = AWSXRayRecorderBuilder
                                        .standard()
                                        .withPlugin(new EC2Plugin())
                                        .withPlugin(new ElasticBeanstalkPlugin())
                                        `.withSegmentListener(new MetricsSegmentListener());`

    URL ruleFile = WebConfig.class.getResource("/sampling-rules.json");
    builder.withSamplingStrategy(new LocalizedSamplingStrategy(ruleFile));

    AWSXRay.setGlobalRecorder(builder.build());
  }
}

```

3. Deploy the CloudWatch agent to collect metrics using Amazon Elastic Compute Cloud (Amazon EC2), Amazon Elastic Container Service (Amazon ECS), or
   Amazon Elastic Kubernetes Service (Amazon EKS):
   - To configure Amazon EC2, see [Installing the CloudWatch agent](../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.md "../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.md").
   - To configure Amazon ECS, see [Monitor Amazon ECS
     containers using Container Insights](../../../AmazonECS/latest/developerguide/cloudwatch-container-insights.md "../../../AmazonECS/latest/developerguide/cloudwatch-container-insights.md").
   - To configure Amazon EKS, see [Install the CloudWatch agent by using the Amazon CloudWatch Observability EKS add-on](../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Observability-EKS-addon.md "../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Observability-EKS-addon.md").

4. Configure the SDK to communicate with the CloudWatch agent. By default, the SDK communicates
   with the CloudWatch agent on the address `127.0.0.1`. You can configure alternate
   addresses by setting the environment variable or Java property to
   `address:port`.

###### Example Environment variable

```
AWS_XRAY_METRICS_DAEMON_ADDRESS=`address:port`
```

###### Example Java property

```
com.amazonaws.xray.metrics.daemonAddress=`address:port`
```

###### To validate configuration

1. Sign in to the AWS Management Console and open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Open the **Metrics** tab to observe the influx of your metrics.
3. (Optional) In the CloudWatch console, on the **Logs** tab, open the
   `ServiceMetricsSDK` log group. Look for a log stream that matches the host metrics,
   and confirm the log messages.
