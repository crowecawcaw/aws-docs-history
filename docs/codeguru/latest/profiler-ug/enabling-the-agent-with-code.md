# Enabling the agent with code

You can enable the Amazon CodeGuru Profiler agent in your application by adding code inside the startup
routine of your application.

In addition to adding code, you also need to add a dependency to the agent library in your
build steps. For this you can use a package manager such as Maven or Gradle.

## Installation

To include the agent in your application, you need to tell your build system how to
access the agent library. You can do this manually by adding a dependency in your Maven or
Gradle configuration files.

### Maven

To add a dependency to the agent, add the following sections to your pom.xml file. if
you already have a `repositories` or `dependencies` element in your
POM, add the individual `repositories` or `dependencies` elements
inside the existing outer elements.

```
<project xmlns="http://maven.apache.org/POM/4.0.0"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
...
    <repositories>
        <repository>
            <id>codeguru-profiler</id>
            <name>codeguru-profiler</name>
            <url>https://d1osg35nybn3tt.cloudfront.net</url>
        </repository>
    </repositories>
    ...
    <dependencies>
        <dependency>
            <groupId>com.amazonaws</groupId>
            <artifactId>codeguru-profiler-java-agent</artifactId>
            <version>1.2.4</version>
        </dependency>
    </dependencies>
...
</project>
```

For more information about configuring repositories in Maven, see [Setting up
Multiple Repositories](https://maven.apache.org/guides/mini/guide-multiple-repositories.html "https://maven.apache.org/guides/mini/guide-multiple-repositories.html") in the Maven documentation.

### Gradle

To add a dependency to the agent, add the following sections to your Gradle file. If
you already have a `repositories` or `dependencies` element in your
Gradle file, add the individual subelements into the existing outer elements.

```
repositories {
    maven {
        url = uri("https://d1osg35nybn3tt.cloudfront.net")
    }
}
dependencies {
    implementation("com.amazonaws:codeguru-profiler-java-agent:1.2.4")
}
```

For more information about creating a custom Gradle repository, see [Declaring a custom repository by URL](https://docs.gradle.org/current/userguide/declaring_repositories.html#sec:declaring_custom_repository "https://docs.gradle.org/current/userguide/declaring_repositories.html#sec:declaring_custom_repository"). For examples, see examples 18 and 19 in
[Supported repository transport protocols](https://docs.gradle.org/current/userguide/declaring_repositories.html#sec:plugin-vs-build-repos "https://docs.gradle.org/current/userguide/declaring_repositories.html#sec:plugin-vs-build-repos").

## Configuration

You can configure the agent by using explicit API calls to the
`Profiler.Builder` class. The following table shows the available
options.

The profiling group name is required to start the CodeGuru Profiler agent. The CodeGuru Profiler heap summary
shows your application's heap usage over time. For more information on the heap summary, see
[Understanding the heap
summary](working-with-visualizations-heap-summary.md "working-with-visualizations-heap-summary.md").

###### Important

It is not recommended to enable heap summary data collection in your production
environments, as it might increase latency in your application.

| Type                                    | API call                                          |
| --------------------------------------- | ------------------------------------------------- |
| Profiling group name (required)         | `.profilingGroupName(String)`                     |
| AWS Credentials Provider                | `.awsCredentialsProvider(AwsCredentialsProvider)` |
| Region                                  | `.awsRegionToReportTo(Region)`                    |
| Heap summary data collection (optional) | `.withHeapSummary(Boolean)`                       |

The following is an example of command line API calls.

```
Profiler.builder()
    .profilingGroupName(“MyProfilingGroup”)
    .withHeapSummary(true) // optional - to start without heap profiling, set to false or remove line 
    .build()
    .start();
```

We recommend that you configure and start the agent inside the startup or
`main` function. The following example shows how to add the configuration to
the `main` function.

```
import software.amazon.codeguruprofilerjavaagent.Profiler;

class MyApplication {
    public static void main(String[] args) {
        Profiler.builder()
            .profilingGroupName("MyProfilingGroup")
            .withHeapSummary(true)
            .build()
            .start();
        ...
    }
}
```

If you don't have access to a startup or `main` function, you can add a
static initializer to your `main` class to configure and start the agent. This
configures and starts the agent during the first time your application class is used inside
the application container, as shown in the following example.

```
import software.amazon.codeguruprofilerjavaagent.Profiler;

class MyClass {

    static {
        Profiler.builder()
            .profilingGroupName("MyProfilingGroup")
            .build()
            .start();
    }
    ...
}
```

When your application is running, data is available in the CodeGuru Profiler console. To view your
profiling data, choose **Profiler** in the navigation pane, choose
**Profiling groups**, and then select your profiling group.

After your application has run for more than 15 minutes, data is available for you to
visualize. For example, you can use an **Overview** visualization to
identify code paths that are executed frequently. For more information about visualizations,
see [Working with visualizations](working-with-visualizations.md "working-with-visualizations.md").

When your application has run for an hour, the first
**Recommendations** report is available. After the first report, new
reports are generated hourly. For more information, see [Working with anomalies and recommendation
reports](working-with-recommendation-reports.md "working-with-recommendation-reports.md").

###### Note

If you don't want to use the default credentials to run the profiler, you can provide
custom credentials by using following code. For more information about custom credentials,
see [Supplying and Retrieving AWS Credentials](../../../sdk-for-java/v2/developer-guide/credentials.md "../../../sdk-for-java/v2/developer-guide/credentials.md").

```
public static void main(String[] args) {
     Profiler.builder()
          .profilingGroupName("MyProfilingGroup")
          .awsCredentialsProvider(myAwsCredentialsProvider).build().start();
 }
```

## Supported languages

The following topics provide code that you can add to your application to enable the
Amazon CodeGuru Profiler agent.

###### Topics

- [Java](java-language-support.md "java-language-support.md")
- [Scala](scala-language-support.md "scala-language-support.md")
- [Kotlin](kotlin-language-support.md "kotlin-language-support.md")
- [Groovy](groovy-language-support.md "groovy-language-support.md")
- [Jython](jython-language-support.md "jython-language-support.md")
- [JRuby](jruby-language-support.md "jruby-language-support.md")
- [Clojure](clojure-language-support.md "clojure-language-support.md")
