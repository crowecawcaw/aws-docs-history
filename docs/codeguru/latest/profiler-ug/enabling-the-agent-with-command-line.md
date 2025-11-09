# Enabling the agent from the command

line

The command line option for integrating the CodeGuru Profiler agent is the easiest way to start
profiling your application, because it doesn't require recompiling and redeploying your
application. Add the appropriate command line options to your JVM-based runtime environment
and you’re ready to go.

## Installation

Download the [Amazon CodeGuru Profiler agent .jar file](https://d1osg35nybn3tt.cloudfront.net/com/amazonaws/codeguru-profiler-java-agent-standalone/1.2.4/codeguru-profiler-java-agent-standalone-1.2.4.jar "https://d1osg35nybn3tt.cloudfront.net/com/amazonaws/codeguru-profiler-java-agent-standalone/1.2.4/codeguru-profiler-java-agent-standalone-1.2.4.jar").

Save this to a location that is accessible from your JVM-based application.

## Configuration

The only required configuration option to start the CodeGuru Profiler agent is the profiling group
name. You can find this in the **Settings** section of your profiling group
on the CodeGuru Profiler console.

You can use the credential path parameter to have the agent use credentials that are
different from the default credentials. The path must point to a valid AWS credentials
file. For more information about credentials, see [Configuration and credential file settings](../../../cli/latest/userguide/cli-configure-files.md "../../../cli/latest/userguide/cli-configure-files.md").

The CodeGuru Profiler heap summary shows your application's heap usage over time. For more
information on the heap summary, see [Understanding the heap
summary](working-with-visualizations-heap-summary.md "working-with-visualizations-heap-summary.md").

Opt in to heap summary data collection by adding `heapSummaryEnabled:true`.
The following example shows how to enable heap summary collection.

```
-javaagent:/path/to/codeguru-profiler-java-agent-standalone-1.2.4.jar="profilingGroupName:myProfilingGroup,heapSummaryEnabled:true"
```

You can specify these options as an environment variable or as a command line
option.

| Option                          | Environment variable                         | Command line option  |
| ------------------------------- | -------------------------------------------- | -------------------- |
| Profiling group name (required) | `AWS_CODEGURU_PROFILER_GROUP_NAME`           | `profilingGroupName` |
| Credential path                 | `AWS_CODEGURU_PROFILER_CREDENTIAL_PATH`      | `credentialPath`     |
| Region                          | `AWS_CODEGURU_PROFILER_TARGET_REGION`        | `region`             |
| Heap summary data collection    | `AWS_CODEGURU_PROFILER_HEAP_SUMMARY_ENABLED` | `heapSummaryEnabled` |

Your startup script using environment variables might look like the following.

```
#!/bin/bash

export AWS_CODEGURU_PROFILER_GROUP_NAME=MyProfilingGroup
export AWS_CODEGURU_PROFILER_TARGET_REGION=us-west-2

java -javaagent:/path/to/codeguru-profiler-java-agent-standalone-1.2.4.jar -jar MyApplication.jar
```

Alternatively, you can specify the configuration options by using the command line
directly, as follows.

```
java -javaagent:/path/to/codeguru-profiler-java-agent-standalone-1.2.4.jar=profilingGroupName:MyProfilingGroup,region:us-west-2 -jar MyApplication.jar
```

The argument string can contain multiple parameters. Separate parameters with a comma
(`,`). Each parameter is a key-value pair.

###### Note

Your command must either be on one continuous line or a line-continuation option
appropriate for your command shell.

## Supported runtime environments

Most JVM-based application runtime environments support a mechanism to specify and
customize JVM startup parameters to include the CodeGuru Profiler agent in the runtime startup. This
section summarizes some of the popular runtime environments that we have verified to support
this option.

All the examples assume that you have set the profiling group name with an environment
variable: `export AWS_CODEGURU_PROFILER_GROUP_NAME=MyProfilingGroupName`.

###### Topics

- [Java](#javaagent-java "#javaagent-java")
- [Scala](#javaagent-scala "#javaagent-scala")
- [Jython](#javaagent-jython "#javaagent-jython")
- [ColdFusion](#javaagent-coldfusion "#javaagent-coldfusion")
- [Geronimo](#javaagent-geronimo "#javaagent-geronimo")
- [SOLR](#javaagent-solr "#javaagent-solr")
- [Tomcat](#javaagent-tomcat "#javaagent-tomcat")
- [Glassfish](#javaagent-glassfish "#javaagent-glassfish")
- [Grails](#javaagent-grails "#javaagent-grails")
- [Jetty](#javaagent-jetty "#javaagent-jetty")
- [Play](#javaagent-play "#javaagent-play")
- [Resin](#javaagent-resin "#javaagent-resin")
- [Spring Boot](#javaagent-spring-boot "#javaagent-spring-boot")
- [Tanuki Wrapper](#javaagent-tanuki-wrapper "#javaagent-tanuki-wrapper")
- [Websphere Liberty Profile](#javaagent-websphere "#javaagent-websphere")
- [Spark](#javaagent-spark "#javaagent-spark")
- [Other runtime environments](#javaagent-other "#javaagent-other")

### Java

If you start your application using the `java` command, you can enable the
CodeGuru Profiler agent in your application by adding the following `-javaagent` command
line option.

```
java -javaagent:/path/to/codeguru-profiler-java-agent-standalone-1.2.4.jar -jar MyApplication.jar
```

### Scala

If you start your application using the `scala` command, you can enable the
CodeGuru Profiler agent in your application by adding the following `-J-javaagent` command
line option.

```
scala -J-javaagent:/path/to/codeguru-profiler-java-agent-standalone-1.2.4.jar -jar MyScalaApplication.jar
```

### Jython

If you start your application using the `Jython` command, you can enable
the CodeGuru Profiler agent in your application by adding the following `-J-javaagent`
command line option.

```
jython -J-javaagent:/path/to/codeguru-profiler-java-agent-standalone-1.2.4.jar -jar MyJythonApplication.jar
```

### ColdFusion

Enable profiling for ColdFusion applications by adding the `-javaagent`
option to the JVM parameters in the administrator console.

1. Navigate to your ColdFusion administrator console.
2. From the left menu, choose **SERVER SETTINGS**.
3. From the top bar, choose **Java and JVM**.
4. In the **JVM Arguments** field, add the following
   `-javaagent` argument.

```
-javaagent:/path/to/codeguru-profiler-java-agent-standalone-1.2.4.jar
```

5. Choose **Submit changes**, then restart your ColdFusion
   server.

### Geronimo

Add the CodeGuru Profiler agent to the Geronimo startup options by adding the
`-javaagent` command line option to the `JAVA_OPTS` environment
variable before starting your Geronimo instance.

```
export JAVA_OPTS="$JAVA_OPTS -javaagent:/path/to/codeguru-profiler-java-agent-standalone-1.2.4.jar"
geronimo run
```

### SOLR

Add the `-javaagent` command line option to the `SOLR_OPTS`
variable in your SOLR startup configuration script,
`/path/to/solr/bin/solr.in.sh`, by appending the following lines to it and
adjusting them to your environment.

```
SOLR_OPTS="$SOLR_OPTS -javaagent:/path/to/codeguru-profiler-java-agent-standalone-1.2.4.jar"
```

### Tomcat

Add the `-javaagent` command line option to the `JAVA_HOME`
environment variable in Tomcat’s startup script,
`/path/to/tomcat/bin/catalina.sh`.

```
JAVA_OPTS="$JAVA_OPTS -javaagent:/path/to/codeguru-profiler-java-agent-standalone-1.2.4.jar"
```

### Glassfish

1. Add
   `<jvm-options>-javaagent:~/codeguru-profiler-java-agent-standalone-1.2.4.jar</jvm-options>`
   below the `java-config` tag.
2. Start your domain, `./bin/asadmin start-domain domain1`.

If you have JDK version 1.8 or later and are running Glassfish version 5.0 or later,
you receive the following error.

```
java.lang.NoSuchMethodError:
sun.security.ssl.Handshaker.receiveChangeCipherSpec()
```

### Grails

1. Add the following to `/appName/build.groovy`.

```
tasks.withType(JavaExec) { jvmArgs "-javaagent:/path/to/codeguru-profiler-java-agent-standalone-1.2.4.jar" }
```

2. Start the **grails run-app** application.

### Jetty

- Append
  `-javaagent:~/codeguru-profiler-java-agent-standalone-1.2.4.jar`
  to the startup script.

### Play

- Append the following to your startup script, and then run the following.

```
./sbt -J-javaagent:~/codeguru-profiler-java-agent-standalone-1.2.4.jar "run 8080"
```

### Resin

- Add the following to your configuration file.

```
<server-default><jvm-arg>-javaagent:~/codeguru-profiler-java-agent-standalone-1.2.4.jar</jvm-arg>
```

### Spring Boot

- Run the server with the `javaagent`.

```
java -javaagent:~/codeguru-profiler-java-agent-standalone-1.2.4.jar -jar demo-0.0.1-SNAPSHOT.jar
```

### Tanuki Wrapper

- Add the following code to `wrapper.conf`.

```
<NON_DUPLICATE_NUMBER_IN_ADDITIONAL_PARAM_LIST>=-javaagent:~/codeguru-profiler-java-agent-standalone-1.2.4.jar
```

### Websphere Liberty Profile

- Append the following path to `jvm.options`.

```
-javaagent:~/codeguru-profiler-java-agent-standalone-1.2.4.jar
```

### Spark

There is a Spark plugin to profile with CodeGuru Profiler. See [A new Spark plugin for CPU and memory profiling](https://aws.amazon.com/blogs/devops/a-new-spark-plugin-for-cpu-and-memory-profiling/ "https://aws.amazon.com/blogs/devops/a-new-spark-plugin-for-cpu-and-memory-profiling/").

CodeGuru Profiler supports Spark, but does not have `-javaagent` support. The agent is
part of your .jar package ﬁle when you use CodeGuru Profiler in Spark. It doesn't matter if the agent
is the worker or the primary as long as your code takes care of starting and stopping the
agent when a job begins and ends. If a job is shorter than one minute, the agent won't
report recommendations. To provide enough samples per worker, run the agent on
long-running jobs. see [Enabling the agent with code](enabling-the-agent-with-code.md "enabling-the-agent-with-code.md")

### Other runtime environments

You can start any Java-based application by using the `-javaagent` command
line option. If your runtime environment or hosting environment uses Java, consult your
documentation to see how to customize the startup parameters for Java.
