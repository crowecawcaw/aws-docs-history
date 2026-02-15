# Using the Elastic Beanstalk Tomcat platform

This topic describes how to configure, build, and run your Java applications that run on the Elastic Beanstalk Tomcat platform.

The AWS Elastic Beanstalk Tomcat platform is a set of [platform
versions](../platforms/platforms-supported.md#platforms-supported.java "../platforms/platforms-supported.md#platforms-supported.java") for Java web applications that can run in a Tomcat web container. Tomcat runs
behind an nginx proxy server. Each platform branch corresponds to a major version of Tomcat.

Configuration options are available in the Elastic Beanstalk console for
[modifying the configuration of a running
environment](environment-configuration-methods-after.md "environment-configuration-methods-after.md"). To avoid losing your environment's configuration when you terminate it, you can
use [saved configurations](environment-configuration-savedconfig.md "environment-configuration-savedconfig.md") to save
your settings and later apply them to another environment.

To save settings in your source code, you can include
[configuration files](ebextensions.md "ebextensions.md"). Settings in configuration files are
applied every time you create an environment or deploy your application. You
can also use configuration files to install packages, run scripts, and perform other instance
customization operations during deployments.

The Elastic Beanstalk Tomcat platform includes a reverse proxy that forwards requests to your
application. You can use [configuration options](#java-tomcat-namespaces "#java-tomcat-namespaces") to
configure the proxy server to serve static assets from a folder in your source code to reduce
the load on your application. For advanced scenarios, you can [include your own .conf files](java-tomcat-proxy.md "java-tomcat-proxy.md") in your source bundle to extend the
Elastic Beanstalk proxy configuration or overwrite it completely.

###### Note

Elastic Beanstalk supports [nginx](https://www.nginx.com/ "https://www.nginx.com/") (the default) and [Apache HTTP Server](https://httpd.apache.org/ "https://httpd.apache.org/") as the proxy servers on the
Tomcat platform. If your Elastic Beanstalk Tomcat environment uses an Amazon Linux AMI platform branch (preceding
Amazon Linux 2), you also have the option of using [Apache HTTP Server Version 2.2](https://httpd.apache.org/docs/2.2/ "https://httpd.apache.org/docs/2.2/"). Apache (latest) is the default on these older
platform branches.

On [July 18, 2022](../relnotes/release-2022-07-18-linux-al1-retire.md "../relnotes/release-2022-07-18-linux-al1-retire.md"),
Elastic Beanstalk set the status of all platform branches based on Amazon Linux AMI (AL1) to **retired**.
For more information about migrating to a current and fully supported Amazon Linux 2023 platform branch, see [Migrating your Elastic Beanstalk Linux application to Amazon Linux 2023 or Amazon Linux 2](using-features.md "using-features.md").

You must package Java applications in a web application archive (WAR) file with a specific
structure. For information on the required structure and how it relates to the structure of your
project directory, see [Structuring your project folder](java-tomcat-platform-directorystructure.md "java-tomcat-platform-directorystructure.md").

To run multiple applications on the same web server, you can [bundle multiple WAR files](java-tomcat-multiple-war-files.md "java-tomcat-multiple-war-files.md") into a single source
bundle. Each application in a multiple WAR source bundle runs at the root path
(`ROOT.war` runs at
``myapp`.elasticbeanstalk.com/`) or at a path directly
 beneath it (`app2.war` runs at
 ``myapp`.elasticbeanstalk.com/`app2`/`),
as determined by the name of the WAR. In a single WAR source bundle, the application always runs
at the root path.

Settings applied in the Elastic Beanstalk console override the same
settings in configuration files, if they exist. This lets you have default settings in configuration
files, and override them with environment-specific settings in the console. For more information
about precedence, and other methods of changing settings, see [Configuration options](command-options.md "command-options.md").

For details about the various ways you can extend an Elastic Beanstalk Linux-based platform, see [Extending Elastic Beanstalk Linux platforms](platforms-linux-extend.md "platforms-linux-extend.md").

###### Topics

- [Configuring your Tomcat environment](#java-tomcat-options "#java-tomcat-options")
- [Tomcat configuration namespaces](#java-tomcat-namespaces "#java-tomcat-namespaces")
- [Bundling multiple WAR files for Tomcat
  environments](java-tomcat-multiple-war-files.md "java-tomcat-multiple-war-files.md")
- [Structuring your project folder](java-tomcat-platform-directorystructure.md "java-tomcat-platform-directorystructure.md")
- [Configuring the proxy server](java-tomcat-proxy.md "java-tomcat-proxy.md")

## Configuring your Tomcat environment

The Elastic Beanstalk Tomcat platform provides a few platform-specific options in addition to the
standard options that all platforms have. These options enable you to configure the Java
virtual machine (JVM) that runs on your environment's web servers, and define system
properties that provide information configuration strings to your application.

You can use the Elastic Beanstalk console to enable log rotation to Amazon S3 and configure variables that
your application can read from the environment.

###### To configure your Tomcat environment in the Elastic Beanstalk console

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk "https://console.aws.amazon.com/elasticbeanstalk"),
   and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.
3. In the navigation pane, choose **Configuration**.
4. In the **Updates, monitoring, and logging** configuration category, choose **Edit**.

### Container options

You can specify these platform-specific options:

- **Proxy server** – The proxy server to use on your
  environment instances. By default, nginx is used.

### JVM container options

The heap size in the Java virtual machine (JVM) determines how many objects your
application can create in memory before _[garbage collection](https://docs.oracle.com/javase/8/docs/technotes/guides/vm/gctuning/introduction.html "https://docs.oracle.com/javase/8/docs/technotes/guides/vm/gctuning/introduction.html")_ occurs. You can modify the**Initial JVM Heap Size** (`-Xms option`) and a **Maximum JVM Heap Size** (`-Xmx` option). A larger initial heap size
allows more objects to be created before garbage collection occurs, but it also means that
the garbage collector will take longer to compact the heap. The maximum heap size specifies
the maximum amount of memory the JVM can allocate when expanding the heap during heavy
activity.

###### Note

The available memory depends on the Amazon EC2 instance type. For more information about
the EC2 instance types available for your Elastic Beanstalk environment, see [Instance Types](../../../AWSEC2/latest/UserGuide/instance-types.md "../../../AWSEC2/latest/UserGuide/instance-types.md")
in the _Amazon Elastic Compute Cloud User Guide for Linux Instances_.

The _permanent generation_ is a section of the JVM heap that stores
class definitions and associated metadata. To modify the size of the permanent generation,
type the new size in the **Maximum JVM PermGen Size**
(`-XX:MaxPermSize`) option. This setting applies only to Java 7 and earlier.
This option was deprecated in JDK 8 and superseded by the **MaxMetaspace
Size** (`-XX:MaxMetaspaceSize`) option.

###### Important

JDK 17 removed support of the Java `-XX:MaxPermSize` option. Usage of this
option with an environment running on an Elastic Beanstalk platform branch with Corretto 17 will
result in an error. Elastic Beanstalk released its first platform branch running Tomcat with
Corretto 17 on [July 13,
2023](../relnotes/release-2023-07-13-al2023.md "../relnotes/release-2023-07-13-al2023.md").

For more information see the following resources.

- Oracle Java documentation website: [Removed Java Options](https://docs.oracle.com/en/java/javase/17/docs/specs/man/java.html#removed-java-options "https://docs.oracle.com/en/java/javase/17/docs/specs/man/java.html#removed-java-options")
- Oracle Java documentation website: _Class
  Metadata_ section in [Other Considerations](https://docs.oracle.com/javase/8/docs/technotes/guides/vm/gctuning/considerations.html "https://docs.oracle.com/javase/8/docs/technotes/guides/vm/gctuning/considerations.html")

For more information about Elastic Beanstalk platforms and their components, see [Supported Platforms](../platforms/platforms-supported.md "../platforms/platforms-supported.md") in the _AWS Elastic Beanstalk Platforms_
guide.

### Log options

The **Log Options** section has two settings:

- **Instance profile** – Specifies the instance profile that
  has permission to access the Amazon S3 bucket associated with your application.
- **Enable log file rotation to Amazon S3** – Specifies whether log files
  for your application's Amazon EC2 instances are copied to the Amazon S3
  bucket associated with your application.

### Static files

To improve performance, you can use the **Static files** section to configure the proxy server to serve
static files (for example, HTML or images) from a set of directories inside your web application.
For each directory, you set the virtual path to directory mapping. When the proxy server receives a request for a file under the specified path,
it serves the file directly instead of routing the request to your application.

For details about configuring static files using configuration files or the Elastic Beanstalk console, see [Serving static files](environment-cfg-staticfiles.md "environment-cfg-staticfiles.md").

### Environment properties

In the **Environment Properties** section, you can specify environment
configuration settings on the Amazon EC2 instances that are running your application. Environment
properties are passed in as key-value pairs to the application.

The Tomcat platform defines a placeholder property named
`JDBC_CONNECTION_STRING` for Tomcat environments for passing a connection
string to an external database.

###### Note

If you attach an RDS DB instance to your environment, construct the JDBC connection
string dynamically from the Amazon Relational Database Service (Amazon RDS) environment properties provided by Elastic Beanstalk.
Use JDBC_CONNECTION_STRING only for database instances that are not provisioned using
Elastic Beanstalk.

For more information about using Amazon RDS with your Java application, see [Adding an Amazon RDS DB instance to your Java Elastic Beanstalk environment](java-rds.md "java-rds.md").

For Tomcat platform versions released prior to [March 26, 2025](../relnotes/release-2025-03-26-windows.md "../relnotes/release-2025-03-26-windows.md"), environment variables are accessible using
`System.getProperty()`. For example, you could read a property named `API_ENDPOINT` from a variable with the following
code.

```
String endpoint = System.getProperty("API_ENDPOINT");
```

Tomcat platform versions released on or after [March 26, 2025](../relnotes/release-2025-03-26-windows.md "../relnotes/release-2025-03-26-windows.md"), can also use `System.getenv`
to access plaintext environment variables. You can continue to use `System.getProperty` to access plaintext environment variables.
However, [environment variables stored as secrets](AWSHowTo.secrets.md "AWSHowTo.secrets.md") are only available using `System.getenv`. For example, you could read an environment variable named `API_KEY` with the following code.

```
String apiKey = System.getenv("API_KEY");
```

###### Important

The addition of `System.getenv()` access for environment variables in Tomcat platform versions released on or after
[March 26, 2025](../relnotes/release-2025-03-26-windows.md "../relnotes/release-2025-03-26-windows.md") may cause unexpected behavior in applications that give environment variables precedence over Java
system properties or when explicitly switching from `System.getProperty()` to `System.getenv()`.

Since system properties (passed via command line) require shell escaping for special characters while environment variables do not,
values may be resolved differently when using environment variables instead of Java system properties.

If your application is affected, consider:

- Removing escape characters from your environment property values when using `System.getenv()`
- Configuring your application to explicitly use `System.getProperty()`
- Testing your application thoroughly when upgrading to ensure consistent behavior

See [Environment variables and other software settings](environments-cfg-softwaresettings.md "environments-cfg-softwaresettings.md")
for more information.

## Tomcat configuration namespaces

You can use a [configuration file](ebextensions.md "ebextensions.md") to set configuration
options and perform other instance configuration tasks during deployments. Configuration options can be [platform specific](command-options-specific.md "command-options-specific.md")
or apply to [all platforms](command-options-general.md "command-options-general.md") in the Elastic Beanstalk service as a whole. Configuration options are organized into
_namespaces_.

The Tomcat platform supports options in the following namespaces, in addition to the [options supported for all Elastic Beanstalk
environments](command-options-general.md "command-options-general.md"):

- `aws:elasticbeanstalk:container:tomcat:jvmoptions` – Modify JVM
  settings. Options in this namespace correspond to options in the management console, as
  follows:
  - `Xms` – **JVM command line options**
  - `JVM Options` – **JVM command line
    options**

- `aws:elasticbeanstalk:environment:proxy` – Choose the environment's
  proxy server.

The following example configuration file shows the use of the Tomcat-specific
configuration options.

###### Example.ebextensions/tomcat-settings.config

```
option_settings:
  aws:elasticbeanstalk:container:tomcat:jvmoptions:
    Xms: 512m
    JVM Options: '-Xmn128m'
  aws:elasticbeanstalk:application:environment:
    API_ENDPOINT: mywebapi.zkpexsjtmd.us-west-2.elasticbeanstalk.com
  aws:elasticbeanstalk:environment:proxy:
    ProxyServer: apache
```

Elastic Beanstalk provides many configuration options for customizing your environment. In
addition to configuration files, you can also set configuration options using the console, saved configurations, the EB CLI, or the AWS CLI.
See [Configuration options](command-options.md "command-options.md") for more information.

If your Elastic Beanstalk Tomcat environment uses an Amazon Linux AMI platform version (preceding Amazon Linux 2),
read the additional information in this section.

###### Notes

- The information in this topic only applies to platform branches based on Amazon Linux AMI (AL1). AL2023/AL2 platform branches are incompatible with previous Amazon Linux AMI
  (AL1) platform versions and _require different configuration settings_.
- On [July 18, 2022](../relnotes/release-2022-07-18-linux-al1-retire.md "../relnotes/release-2022-07-18-linux-al1-retire.md"),
  Elastic Beanstalk set the status of all platform branches based on Amazon Linux AMI (AL1) to **retired**.
  For more information about migrating to a current and fully supported Amazon Linux 2023 platform branch, see [Migrating your Elastic Beanstalk Linux application to Amazon Linux 2023 or Amazon Linux 2](using-features.md "using-features.md").
  The Tomcat Amazon Linux AMI platform supports additional options in the following
  namespaces:

- `aws:elasticbeanstalk:container:tomcat:jvmoptions` – In
  addition to the options mentioned earlier on this page for this namespace, older
  Amazon Linux AMI platform versions also support:
  - `XX:MaxPermSize` – **Maximum JVM permanent
    generation size**

- `aws:elasticbeanstalk:environment:proxy` – In addition to
  choosing the proxy server, also configure response compression.
  The following example configuration file shows the use of the proxy namespace
  configuration options.

###### Example.ebextensions/tomcat-settings.config

```
option_settings:
  aws:elasticbeanstalk:environment:proxy:
    GzipCompression: 'true'
    ProxyServer: nginx
```

To deploy `.ebextensions` configuration files, include them in
your application source. For a single application, add your
`.ebextensions` to a compressed WAR file by running the following
command:

###### Example

```
zip -ur `your_application.war` .ebextensions
```

For an application requiring multiple WAR files, see [Bundling multiple WAR files for Tomcat
environments](java-tomcat-multiple-war-files.md "java-tomcat-multiple-war-files.md") for further instructions.
