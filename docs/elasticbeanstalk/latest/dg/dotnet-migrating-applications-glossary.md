# Migration glossary

This glossary provides definitions for key terms and concepts related to IIS, Elastic Beanstalk, and the
migration of IIS applications to Elastic Beanstalk.

## Windows, IIS, and .NET

terms

\***\*IIS\*\***

Internet Information Services, a web server software developed by Microsoft for use
with Windows Server. IIS hosts websites, web applications, and web services, providing a
platform for running ASP.NET and other web technologies. During migration to Elastic Beanstalk, IIS
sites and their configurations are packaged and deployed to Windows Server instances in
the AWS Cloud.

IIS versions 7.0 and later are supported for migration, with IIS 10.0 on Windows
Server 2016 or later providing the most compatible environment.

\***\*.NET Framework\*\***

A software development platform developed by Microsoft for building and running
Windows applications. It provides a large class library called Framework Class Library
(FCL) and supports language interoperability across several programming
languages.

When migrating to Elastic Beanstalk, applications built on the .NET Framework continue to run on
the same version of the framework in the cloud environment. Elastic Beanstalk supports multiple .NET
Framework versions (4.x) on its Windows Server platforms.

\***\*.NET Core\*\***

A cross-platform, open-source successor to the .NET Framework, designed to be more
modular and lightweight. .NET Core (now simply called .NET 5 and later) enables
developers to build applications that run on Windows, Linux, and macOS.

When migrating applications built on .NET Core to Elastic Beanstalk, you can choose between
Windows Server platforms or Linux-based platforms, depending on your application's
requirements and dependencies.

\***\*Common Language Runtime (CLR)\*\***

The virtual machine component of the .NET Framework that manages the execution of
.NET programs. The CLR provides services such as memory management, type safety,
exception handling, garbage collection, and thread management.

When migrating to Elastic Beanstalk, the appropriate CLR version is automatically available on
the Windows Server platform you select, ensuring compatibility with your application's
requirements.

\***\*Site\*\***

A logical container in IIS that represents a web application or service, identified
by a unique binding of IP address, port, and host header. Each IIS site has its own
application pool, bindings, and configuration settings, and can contain one or more
applications.

\***\*Application\*\***

A grouping of content and code files within an IIS site that handles requests for a
specific URL space. Applications in IIS can have their own configuration settings, which
are typically stored in `web.config` files.

When migrating to Elastic Beanstalk, applications are preserved with their path structure and
configuration settings. The migration process ensures that nested applications maintain
their hierarchy and URL paths in the cloud environment.

\***\*ApplicationPool\*\***

An IIS feature that isolates web applications for better security, reliability, and
performance management. Application pools define the runtime environment for
applications, including the .NET Framework version, pipeline mode, and identity
settings.

\***\*VirtualDirectory\*\***

A directory mapping in IIS that allows content to be served from a location outside
the site's root directory. Virtual directories enable you to organize content across
different physical locations while presenting a unified URL structure to users.

When migrating to Elastic Beanstalk, virtual directories are preserved with their path mappings.
The **eb migrate** command creates the necessary directory structure and
configurations in the cloud environment to maintain the same URL paths.

\***\*ARR\*\***

Application Request Routing, an IIS extension that provides load balancing and
proxying capabilities for web servers. ARR enables URL-based routing, HTTP request
forwarding, and load distribution across multiple servers.

During migration to Elastic Beanstalk, ARR configurations are preserved through the installation
of ARR features on EC2 instances and the configuration of appropriate routing rules. For
complex routing scenarios, the migration process may also leverage Application Load
Balancer rules to implement similar functionality.

\***\*URL Rewrite\*\***

An IIS module that modifies requested URLs based on defined rules before they reach
the web application. URL Rewrite enables URL manipulation, redirection, and content
delivery based on patterns and conditions.

When migrating to Elastic Beanstalk, URL rewrite rules from your `web.config`
files are translated into ALB routing rules where possible, or preserved in the IIS
configuration on the EC2 instances. This ensures that URL patterns and redirects
continue to function as expected in the cloud environment.

\***\*msdeploy.exe\*\***

A command-line tool used for deploying web applications and websites to IIS servers.
Also known as Web Deploy, it provides a way to package, synchronize, and deploy web
applications, websites, and server configurations.

The **eb migrate** command uses Web Deploy (version 3.6 or later) to
package your applications during migration to Elastic Beanstalk. This tool must be installed on your
source server for the migration process to work correctly.

\***\*Physical Path\*\***

The actual file system location where an IIS site or application's content files are
stored. Physical paths can point to local directories, network shares, or other storage
locations accessible to the IIS server.

During migration to Elastic Beanstalk, physical paths are mapped to appropriate locations on the
EC2 instances in your environment. The migration process preserves the content structure
while ensuring that all files are properly deployed to the cloud environment.

\***\*applicationHost.config\*\***

The root configuration file for IIS that defines server-wide settings and contains
configuration for all sites, applications, and virtual directories. This file is located
in the `%windir%\System32\inetsrv\config` directory and controls the overall
behavior of the IIS server.

When migrating to Elastic Beanstalk, relevant settings from
`applicationHost.config` are extracted and applied to the IIS
configuration on the EC2 instances in your environment. This ensures that server-wide
settings are preserved during migration.

\***\*web.config\*\***

An XML-based configuration file used in ASP.NET applications to control application
settings, security, and behavior at the application or directory level.
`web.config` files can contain settings for authentication,
authorization, session state, compilation, and custom application parameters.

During migration to Elastic Beanstalk, `web.config` files are preserved and
deployed with your application. The migration process ensures that application-specific
configurations continue to function as expected in the cloud environment.

\***\*DefaultDocument\*\***

An IIS feature that specifies the default file to serve when a user requests a
directory without specifying a file name. Default documents are enabled by default, and
IIS 7 defines the following default document files in the
`applicationHost.config` file as server-wide defaults: Default.htm,
Default.asp, Index.htm, Index.html, Iisstart.htm.

When migrating to Elastic Beanstalk, default document settings are preserved in the IIS
configuration on the EC2 instances, ensuring that directory requests are handled
consistently in the cloud environment.

\***\*system.webServer\*\***

A configuration section in `web.config` or
`applicationHost.config` that contains IIS-specific settings for
modules, handlers, and other server behaviors. This section controls how IIS processes
requests, manages modules, and configures server features.

During migration to Elastic Beanstalk, system.webServer configurations are preserved in your
application's `web.config` files and applied to the IIS installation
on the EC2 instances in your environment. This ensures that IIS-specific behaviors are
maintained in the cloud environment.

## Elastic Beanstalk terms

\***\*Platform\*\***

A combination of operating system, programming language runtime, web server,
application server, and Elastic Beanstalk components that define the software stack for running
applications.

For Windows migrations, Elastic Beanstalk provides platforms based on Windows Server 2016, 2019,
and 2022 with IIS and various .NET Framework versions to ensure compatibility with your
source environment.

\***\*SolutionStack\*\***

A predefined platform configuration in Elastic Beanstalk that specifies the operating system,
runtime, and other components needed to run an application. Conceptually identical to a
platform and used interchangeably to operate environments.

During migration, the **eb migrate** command selects an appropriate
solution stack based on your source environment's configuration, ensuring compatibility
with your IIS applications.

\***\*CreateEnvironment\*\***

An Elastic Beanstalk API action that creates a new environment to host an application version.
This API is used by the **eb migrate** command to provision the necessary
AWS resources for your migrated application.

The migration process configures appropriate environment parameters based on your
source IIS environment, including instance type, environment variables, and option
settings.

\***\*CreateApplicationVersion\*\***

An Elastic Beanstalk API action that creates a new application version from a source bundle
stored in Amazon S3. The **eb migrate** command uses this API to register your
packaged IIS application as a version in Elastic Beanstalk.

During migration, your application files and configuration are packaged, uploaded to
Amazon S3, and registered as an application version before deployment.

\***\*DescribeEvents\*\***

An Elastic Beanstalk API action that retrieves a list of events for an environment, including
deployments, configuration changes, and operational issues. The **eb
migrate** command uses this API to monitor the progress of your
migration.

You can also use the **eb events** command after migration to view
the history of events for your environment.

\***\*DescribeEnvironmentHealth\*\***

An Elastic Beanstalk API action that provides detailed health information about the instances
and other components of an environment. This API is used to verify the health of your
migrated application after deployment.

After migration, you can use the **eb health** command to check the
status of your environment and identify any issues that need attention.

\***\*HealthD\*\***

A monitoring agent in Elastic Beanstalk that collects metrics, monitors logs, and reports health
status for EC2 instances in an environment. HealthD provides enhanced health reporting
for your migrated applications.

After migration, HealthD monitors your application's performance, resource
utilization, and request success rates, providing a comprehensive view of your
environment's health.

\***\*Bundle Logs\*\***

A feature in Elastic Beanstalk that compresses and uploads logs from EC2 instances to Amazon S3 for
centralized storage and analysis. This feature helps you troubleshoot issues with your
migrated applications.

After migration, you can use the **eb logs** command to retrieve and
view logs from your environment.

\***\*aws-windows-deployment-manifest.json\*\***

A file that describes the contents, dependencies, and configuration of a software
package or application. This manifest is generated during the migration process to
define how your IIS applications should be deployed on Elastic Beanstalk.

\***\*custom manifest section\*\***

A section within `aws-windows-deployment-manifest.json` that
provides custom control over application deployment. This section contains PowerShell
scripts and commands that are executed during the deployment process.

During migration, custom manifest sections are generated to handle specific aspects
of your IIS configuration, such as virtual directory setup, permission management, and
application pool configuration.

\***\*EB CLI\*\***

A command-line tool that provides commands for creating, configuring, and managing
Elastic Beanstalk applications and environments. The EB CLI includes the **eb
migrate** command specifically for migrating IIS applications to Elastic Beanstalk.

After migration, you can continue to use the EB CLI to manage your environment,
deploy updates, monitor health, and perform other administrative tasks.

\***\*Option settings\*\***

Configuration values that define how Elastic Beanstalk provisions and configures AWS resources
in your environment. Option settings are organized into namespaces that represent
different components of your environment, such as load balancers, instances, and
environment processes.

During migration, the **eb migrate** command generates appropriate
option settings based on your IIS configuration to ensure that your cloud environment
matches your source environment's capabilities. For more information, see [Configuration options](command-options-general.md "command-options-general.md") in the Elastic Beanstalk Developer Guide.

\***\*aws:elbv2:listener:default\*\***

An Elastic Beanstalk configuration namespace for the default listener on an Application Load
Balancer. During migration, this namespace is configured based on your IIS site bindings
to ensure proper traffic routing.

The default listener typically handles HTTP traffic on port 80, which is then
forwarded to your application instances according to the routing rules.

\***\*aws:elbv2:listener:listener_port\*\***

An Elastic Beanstalk configuration namespace for a specific listener port on an Application Load
Balancer. This namespace is used to configure additional listeners for your migrated
applications, such as HTTPS on port 443.

During migration, listeners are created based on the port bindings of your IIS
sites, ensuring that your applications remain accessible on the same ports as in your
source environment.

\***\*aws:elbv2:listenerrule:rule_name\*\***

An Elastic Beanstalk configuration namespace for defining routing rules for an Application Load
Balancer listener. These rules determine how incoming requests are routed to different
target groups based on path patterns or host headers.

During migration, listener rules are created to match the URL structure of your IIS
applications, ensuring that requests are routed to the correct application paths.

\***\*aws:elasticbeanstalk:environment:process:default\*\***

An Elastic Beanstalk configuration namespace for the default process in an environment. This
namespace defines how the default web application process is configured, including
health check settings, port mappings, and proxy settings.

During migration, the default process is configured based on your primary IIS site's
settings, ensuring proper health monitoring and request handling.

\***\*aws:elasticbeanstalk:environment:process:process_name\*\***

An Elastic Beanstalk configuration namespace for a specific named process in an environment.
This namespace allows you to define multiple processes with different configurations,
similar to having multiple application pools in IIS.

During migration, additional processes may be created to represent different site
bindings from your source environment.

###### Note

For more information about some of the terms described in this topic see the following
resources:

- Elastic Beanstalk API actions - [AWS Elastic Beanstalk API Reference](../api.md "../api.md")
- Elastic Beanstalk platforms, including supported platform versions -
  [Supported
  Platforms](../platforms/platforms-supported.md "../platforms/platforms-supported.md") in the _AWS Elastic Beanstalk Platforms guide_
- Elastic Beanstalk configuration namespaces - [General options for all environments](command-options-general.md "command-options-general.md") in this
  guide
- The EB CLI or specific EB CLI commands - [Setting up the EB command line interface (EB CLI) to manage Elastic Beanstalk](eb-cli3.md "eb-cli3.md") in this guide

## Python terms

\***\*pip\*\***

The package installer for Python, used to install and manage software packages
written in Python. The EB CLI is installed and updated using pip.

During the migration process, pip is used to install the EB CLI package and its
dependencies on your source server, providing the tools needed for migration.

\***\*PyPI\*\***

Python Package Index, the official repository for third-party Python software
packages, from which pip retrieves and installs packages. The EB CLI and its
dependencies are hosted on PyPI.

When installing the EB CLI for migration, pip connects to PyPI to download and
install the necessary packages.

\***\*virtualenv\*\***

A tool to create isolated Python environments, allowing different projects to have
their own dependencies and packages without conflicts. Using virtualenv is recommended
when installing the EB CLI to avoid conflicts with other Python applications.

Creating a virtual environment before installing the EB CLI ensures that the
migration tools have a clean, isolated environment with the correct dependencies.

\***\*pywin32\*\***

A set of Python extensions that provide access to many of the Windows APIs, enabling
interaction with the Windows operating system and its components. The EB CLI uses
pywin32 to interact with Windows-specific features during migration.

During the migration process, pywin32 is used to access IIS configuration, Windows
registry settings, and other system information needed to properly package and migrate
your applications.

\***\*pythonnet\*\***

A package that enables Python code to interact with .NET Framework and .NET Core
applications. This integration allows the EB CLI to work with .NET components during the
migration process.

The migration process may use pythonnet to interact with .NET assemblies and
components when analyzing and packaging your applications for deployment to
Elastic Beanstalk.
