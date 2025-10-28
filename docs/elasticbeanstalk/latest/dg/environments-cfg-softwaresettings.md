# Environment variables and other software settings

The **Configure updates, monitoring, and logging** configuration page lets you configure the software on the Amazon Elastic Compute Cloud (Amazon EC2)
instances that run your application. You can configure environment variables, AWS X-Ray debugging, instance log storing and streaming, and
platform-specific settings.

###### Topics

- [Configure platform-specific settings](#environments-cfg-softwaresettings-specific "#environments-cfg-softwaresettings-specific")
- [Configuring environment properties (environment variables)](#environments-cfg-softwaresettings-console "#environments-cfg-softwaresettings-console")
- [Software setting namespaces](#environments-cfg-softwaresettings-configfiles "#environments-cfg-softwaresettings-configfiles")
- [Accessing environment properties](#environments-cfg-softwaresettings-accessing "#environments-cfg-softwaresettings-accessing")
- [Configuring AWS X-Ray debugging](environment-configuration-debugging.md "environment-configuration-debugging.md")
- [Viewing your Elastic Beanstalk environment logs](environments-cfg-logging.md "environments-cfg-logging.md")

## Configure platform-specific settings

In addition to the standard set of options available for all environments, most Elastic Beanstalk
platforms let you specify language-specific or framework-specific settings. These appear in
the **Platform software** section of the **Configure updates,
monitoring, and logging** page, and can take the following forms.

- **Preset environment properties** – The Ruby platform uses environment properties for framework settings, such
  as `RACK_ENV` and `BUNDLE_WITHOUT`.
- **Placeholder environment properties** – The Tomcat platform defines an environment property named
  `JDBC_CONNECTION_STRING` that is not set to any value. This type of setting was more common on older platform versions.
- **Configuration options** – Most platforms define [configuration options](command-options.md "command-options.md")
  in platform-specific or shared namespaces, such as `aws:elasticbeanstalk:xray` or `aws:elasticbeanstalk:container:python`.

###### To configure platform-specific settings in the Elastic Beanstalk console

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk "https://console.aws.amazon.com/elasticbeanstalk"),
   and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.
3. In the navigation pane, choose **Configuration**.
4. In the **Updates, monitoring, and logging** configuration category, choose **Edit**.
5. Under **Platform software**, make necessary option setting changes.
6. To save the changes choose **Apply** at the bottom of the page.

For information about platform-specific options, and about getting environment property values in your code, see the platform topic for your language or
framework:

- Docker – [Configuring Elastic Beanstalk Docker environments](create_deploy_docker.container.md "create_deploy_docker.container.md")
- Go – [Using the Elastic Beanstalk Go platform](go-environment.md "go-environment.md")
- Java SE – [Using the Elastic Beanstalk Java SE platform](java-se-platform.md "java-se-platform.md")
- Tomcat – [Using the Elastic Beanstalk Tomcat platform](java-tomcat-platform.md "java-tomcat-platform.md")
- .NET Core on Linux – [Using the Elastic Beanstalk .NET core on Linux platform](dotnet-linux-platform.md "dotnet-linux-platform.md")
- .NET – [Using the Elastic Beanstalk .NET Windows platform](create_deploy_NET.container.md "create_deploy_NET.container.md")
- Node.js – [Using the Elastic Beanstalk Node.js platform](create_deploy_nodejs.md "create_deploy_nodejs.md")
- PHP – [Using the Elastic Beanstalk PHP platform](create_deploy_PHP.md "create_deploy_PHP.md")
- Python – [Using the Elastic Beanstalk Python platform](create-deploy-python-container.md "create-deploy-python-container.md")
- Ruby – [Using the Elastic Beanstalk Ruby platform](create_deploy_Ruby.md "create_deploy_Ruby.md")

## Configuring environment properties (environment variables)

You can use **environment properties**, (also known as **environment variables**), to pass endpoints,
debug settings, and other information to your application. Environment variables help you run your application in multiple environments for different
purposes, such as development, testing, staging, and production.

In addition, when you [add a database to your environment](using-features.managing.md "using-features.managing.md"), Elastic Beanstalk sets environment variables, such as
`RDS_HOSTNAME`, that you can read in your application code to construct a connection object or string.

###### To configure environment variables in the Elastic Beanstalk console

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk "https://console.aws.amazon.com/elasticbeanstalk"),
   and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.
3. In the navigation pane, choose **Configuration**.
4. In the **Updates, monitoring, and logging** configuration category, choose **Edit**.
5. Scroll down to **Runtime environment variables**.
6. Select **Add environment variable**.
7. For **Source** select **Plain text**.

###### Note

The **Secrets Manager** and **SSM Parameter Store** values in the drop-down are for configuring environment
variables as secrets to store sensitive data, such as credentials and API keys. For more information, see [Using Elastic Beanstalk with AWS Secrets Manager and AWS Systems Manager Parameter Store](AWSHowTo.md "AWSHowTo.md"). 8. Enter the **Environment variable name** and **Environment variable value** pairs. 9. If you need to add more variables repeat **Step 6** through **Step 8**. 10. To save the changes choose **Apply** at the bottom of the page.

###### Environment property limits

- **Keys** can contain any alphanumeric characters and the following symbols:
  `_ . : / + \ - @`

The symbols listed are valid for environment property keys, but might not be valid for environment variable names on your environment's platform.
For compatibility with all platforms, limit environment properties to the following pattern: `[A-Z_][A-Z0-9_]*`

- **Values** can contain any alphanumeric characters, white space, and the following symbols:
  `_ . : / = + \ - @ ' "`

###### Note

Some characters in environment property values must be escaped. Use the backslash character (`\`) to represent some special
characters and control characters. The following list includes examples for representing some characters that need to be escaped:

    + backslash (`\`) — to represent use `\\`
    + single quote (`'`) — to represent use `\'`
    + double quote (`"`) — to represent use `\"`

- **Keys** and **values** are case sensitive.
- The combined size of all environment properties cannot exceed 4,096 bytes when stored as strings with the format
  `key`=`value`.

## Software setting namespaces

You can use a [configuration file](ebextensions.md "ebextensions.md") to set configuration
options and perform other instance configuration tasks during deployments. Configuration options can be [platform specific](command-options-specific.md "command-options-specific.md")
or apply to [all platforms](command-options-general.md "command-options-general.md") in the Elastic Beanstalk service as a whole. Configuration options are organized into
_namespaces_.

You can use Elastic Beanstalk [configuration files](ebextensions.md "ebextensions.md") to set environment
properties and configuration options in your source code. Use the [aws:elasticbeanstalk:application:environment namespace](command-options-general.md#command-options-general-elasticbeanstalkapplicationenvironment "command-options-general.md#command-options-general-elasticbeanstalkapplicationenvironment") to define environment properties.

###### Example .ebextensions/options.config

```
option_settings:
  aws:elasticbeanstalk:application:environment:
    API_ENDPOINT: www.example.com/api
```

If you use configuration files or AWS CloudFormation templates to create [custom resources](environment-resources.md "environment-resources.md"), you can use an AWS CloudFormation
function to get information about the resource and assign it to an environment property dynamically during deployment. The following example from the
[elastic-beanstalk-samples](https://github.com/awsdocs/elastic-beanstalk-samples/ "https://github.com/awsdocs/elastic-beanstalk-samples/") GitHub repository uses the [Ref function](ebextensions-functions.md "ebextensions-functions.md") to
get the ARN of an Amazon SNS topic that it creates, and assigns it to an environment property named `NOTIFICATION_TOPIC`.

###### Notes

- If you use an AWS CloudFormation function to define an environment property, the Elastic Beanstalk console displays the value of the property before the function is
  evaluated. You can use the [get-config platform script](custom-platforms-scripts.md "custom-platforms-scripts.md") to confirm the values of environment
  properties that are available to your application.
- The [Multicontainer Docker](create_deploy_docker_ecs.md "create_deploy_docker_ecs.md") platform doesn't use AWS CloudFormation to create container resources. As a result, this
  platform doesn't support defining environment properties using AWS CloudFormation functions.

###### Example .Ebextensions/[sns-topic.config](https://github.com/awsdocs/elastic-beanstalk-samples/tree/main/configuration-files/aws-provided/resource-configuration/sns-topic.config "https://github.com/awsdocs/elastic-beanstalk-samples/tree/main/configuration-files/aws-provided/resource-configuration/sns-topic.config")

```
Resources:
  NotificationTopic:
    Type: AWS::SNS::Topic

option_settings:
  aws:elasticbeanstalk:application:environment:
    NOTIFICATION_TOPIC: '`{"Ref" : "NotificationTopic"}`'
```

You can also use this feature to propagate information from [AWS CloudFormation pseudo parameters](../../../AWSCloudFormation/latest/UserGuide/pseudo-parameter-reference.md "../../../AWSCloudFormation/latest/UserGuide/pseudo-parameter-reference.md").
This example gets the current region and assigns it to a property named `AWS_REGION`.

###### Example .Ebextensions/[env-regionname.config](https://github.com/awsdocs/elastic-beanstalk-samples/tree/main/configuration-files/aws-provided/instance-configuration/env-regionname.config "https://github.com/awsdocs/elastic-beanstalk-samples/tree/main/configuration-files/aws-provided/instance-configuration/env-regionname.config")

```
option_settings:
  aws:elasticbeanstalk:application:environment:
    AWS_REGION: '`{"Ref" : "AWS::Region"}`'
```

Most Elastic Beanstalk platforms define additional namespaces with options for configuring software that runs on the instance, such as the reverse proxy that
relays requests to your application. For more information about the namespaces available for your platform, see the following:

- Go – [Go configuration namespace](go-environment.md#go-namespaces "go-environment.md#go-namespaces")
- Java SE – [Java SE configuration namespace](java-se-platform.md#java-se-namespaces "java-se-platform.md#java-se-namespaces")
- Tomcat – [Tomcat configuration namespaces](java-tomcat-platform.md#java-tomcat-namespaces "java-tomcat-platform.md#java-tomcat-namespaces")
- .NET Core on Linux – [.NET Core on Linux configuration namespace](dotnet-linux-platform.md#dotnet-linux-namespace "dotnet-linux-platform.md#dotnet-linux-namespace")
- .NET – [The aws:elasticbeanstalk:container:dotnet:apppool namespace](create_deploy_NET.container.md#dotnet-namespaces "create_deploy_NET.container.md#dotnet-namespaces")
- Node.js – [Node.js configuration namespace](create_deploy_nodejs.md#nodejs-namespaces "create_deploy_nodejs.md#nodejs-namespaces")
- PHP – [Namespaces for configuration](create_deploy_PHP.md#php-namespaces "create_deploy_PHP.md#php-namespaces")
- Python – [Python configuration namespaces](create-deploy-python-container.md#python-namespaces "create-deploy-python-container.md#python-namespaces")
- Ruby – [Ruby configuration namespaces](create_deploy_Ruby.md#ruby-namespaces "create_deploy_Ruby.md#ruby-namespaces")

Elastic Beanstalk provides many configuration options for customizing your environment. In
addition to configuration files, you can also set configuration options using the console, saved configurations, the EB CLI, or the AWS CLI.
See [Configuration options](command-options.md "command-options.md") for more information.

## Accessing environment properties

In most cases, you access environment properties in your application code like an environment variable. In general, however, environment properties
are passed only to the application and can't be viewed by connecting an instance in your environment and running `env`.

- [Go](go-environment.md#go-options-properties "go-environment.md#go-options-properties") – `os.Getenv`

```
endpoint := os.Getenv("API_ENDPOINT")
```

- [Java SE](java-se-platform.md#java-se-options-properties "java-se-platform.md#java-se-options-properties") – `System.getenv`

```
String endpoint = System.getenv("API_ENDPOINT");
```

- [Tomcat](java-tomcat-platform.md#java-tomcat-options-properties "java-tomcat-platform.md#java-tomcat-options-properties") – `System.getProperty` and `System.getenv`

Tomcat platform versions released on or after [March 26, 2025](../relnotes/release-2025-03-26-windows.md "../relnotes/release-2025-03-26-windows.md"), can also use `System.getenv`
to access plaintext environment variables. You can continue to use `System.getProperty` to access plaintext environment variables.
However, [environment variables stored as secrets](AWSHowTo.secrets.md "AWSHowTo.secrets.md") are only available using `System.getenv`.

```
String endpoint = System.getProperty("API_ENDPOINT");
```

```
String endpoint = System.getenv("API_ENDPOINT");
```

###### Important

The addition of `System.getenv` access for environment variables in Tomcat platform versions released on or after [March 26, 2025](../relnotes/release-2025-03-26-windows.md "../relnotes/release-2025-03-26-windows.md")
may cause unexpected behavior in applications that give environment variables precedence over Java system properties or when explicitly switching from
`System.getProperty` to `System.getenv`. For more information and recommended actions,
see [Using the Elastic Beanstalk Tomcat platform](java-tomcat-platform.md "java-tomcat-platform.md").

- [.NET Core on Linux](dotnet-linux-platform.md#dotnet-linux-options-properties "dotnet-linux-platform.md#dotnet-linux-options-properties") – `Environment.GetEnvironmentVariable`

```
string endpoint = Environment.GetEnvironmentVariable("API_ENDPOINT");
```

- [.NET](create_deploy_NET.container.md#dotnet-console-properties "create_deploy_NET.container.md#dotnet-console-properties") – `appConfig`

```
NameValueCollection appConfig = ConfigurationManager.AppSettings;
string endpoint = appConfig["API_ENDPOINT"];
```

- [Node.js](create_deploy_nodejs.md#nodejs-platform-console-envprops "create_deploy_nodejs.md#nodejs-platform-console-envprops") – `process.env`

```
var endpoint = process.env.API_ENDPOINT
```

- [PHP](create_deploy_PHP.md#php-console-properties "create_deploy_PHP.md#php-console-properties") – `$_SERVER`

```
$endpoint = $_SERVER['API_ENDPOINT'];
```

- [Python](create-deploy-python-container.md#create-deploy-python-custom-container-envprop "create-deploy-python-container.md#create-deploy-python-custom-container-envprop") – `os.environ`

```
import os
endpoint = os.environ['API_ENDPOINT']
```

- [Ruby](create_deploy_Ruby.md#create_deploy_Ruby.env.console.ruby.envprops "create_deploy_Ruby.md#create_deploy_Ruby.env.console.ruby.envprops") – `ENV`

```
endpoint = ENV['API_ENDPOINT']
```

Outside of application code, such as in a script that runs during deployment, you can access environment properties with the [get-config platform script](custom-platforms-scripts.md "custom-platforms-scripts.md"). See the [elastic-beanstalk-samples](https://github.com/awsdocs/elastic-beanstalk-samples/search?utf8=%E2%9C%93&q=get-config "https://github.com/awsdocs/elastic-beanstalk-samples/search?utf8=%E2%9C%93&q=get-config") GitHub repository for example configurations that use
`get-config`.
