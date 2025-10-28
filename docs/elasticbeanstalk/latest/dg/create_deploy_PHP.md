# Using the Elastic Beanstalk PHP platform

AWS Elastic Beanstalk provides and supports various **platform branches** for different versions of PHP. The platforms support PHP web applications that run stand-alone or under Composer. See [PHP](../platforms/platforms-supported.md#platforms-supported.PHP "../platforms/platforms-supported.md#platforms-supported.PHP") in the _AWS Elastic Beanstalk Platforms_ document for a full list of supported platform branches.

Elastic Beanstalk provides [configuration options](command-options.md "command-options.md") that you can use to customize the software that runs on the Amazon EC2 instances in
your Elastic Beanstalk environment. You can [configure environment variables](environments-cfg-softwaresettings.md#environments-cfg-softwaresettings-console "environments-cfg-softwaresettings.md#environments-cfg-softwaresettings-console") required by your
application, enable log rotation to Amazon S3, map folders in your application source that contain static files to paths served by the proxy server, and set
common PHP initialization settings.

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

If you use Composer, you can [include a composer.json file](#php-configuration-composer "#php-configuration-composer") in your source bundle
to install packages during deployment.

For advanced PHP configuration and PHP settings that are not provided as configuration options, you can [use
configuration files to provide an INI file](#php-configuration-phpini "#php-configuration-phpini") that can extend and override the default settings applied by Elastic Beanstalk, or install
additional extensions.

Settings applied in the Elastic Beanstalk console override the same
settings in configuration files, if they exist. This lets you have default settings in configuration
files, and override them with environment-specific settings in the console. For more information
about precedence, and other methods of changing settings, see [Configuration options](command-options.md "command-options.md").

For details about the various ways you can extend an Elastic Beanstalk Linux-based platform, see [Extending Elastic Beanstalk Linux platforms](platforms-linux-extend.md "platforms-linux-extend.md").

###### PHP platform topics

- [Installing the AWS SDK for PHP](#php-development-environment-sdk "#php-development-environment-sdk")
- [Considerations for PHP 8.1 on Amazon Linux 2](#php-8-1-considerations "#php-8-1-considerations")
- [Configuring your PHP environment](#php-console "#php-console")
- [Namespaces for configuration](#php-namespaces "#php-namespaces")
- [Installing dependencies](#php-configuration-composer "#php-configuration-composer")
- [Updating Composer](#php-configuration-composerupdate "#php-configuration-composerupdate")
- [Extending php.ini](#php-configuration-phpini "#php-configuration-phpini")

## Installing the AWS SDK for PHP

If you need to manage AWS resources from within your application, install the AWS SDK for PHP. For example, with the SDK for PHP, you can use Amazon DynamoDB (DynamoDB)
to store user and session information without creating a relational database.

To install the SDK for PHP with Composer

```
$ `composer require aws/aws-sdk-php`
```

For more information, see the [AWS SDK for PHP](https://aws.amazon.com/sdk-for-php/ "https://aws.amazon.com/sdk-for-php/") homepage. For instructions, see [Install the AWS SDK for PHP](../../../sdk-for-php/v3/developer-guide/getting-started_installation.md "../../../sdk-for-php/v3/developer-guide/getting-started_installation.md").

## Considerations for PHP 8.1 on Amazon Linux 2

Read this section if you're using the _PHP 8.1 on Amazon Linux 2_ platform branch.

###### Note

The information in this topic only applies to the _PHP 8.1 on
Amazon Linux 2_ platform branch. It does not apply to the PHP platform branches based on
AL2023. It also does not apply to the _PHP 8.0 Amazon Linux 2_
platform branch.

Elastic Beanstalk stores the PHP 8.1 related RPM packages for the _PHP 8.1 on Amazon Linux 2_
platform branch on the EC2 instances in a local directory, instead of the Amazon Linux repository. You
can use **rpm -i** to install packages. Starting with [PHP
8.1 Platform Version 3.5.0](../relnotes/release-2022-10-03-linux.md "../relnotes/release-2022-10-03-linux.md"), Elastic Beanstalk stores the PHP 8.1 related RPM packages in the
following local EC2 directory.

`/opt/elasticbeanstalk/RPMS`

The following example installs the php-debuginfo package.

```
$`rpm -i /opt/elasticbeanstalk/RPMS/php-debuginfo-8.1.8-1.amzn2.x86_64.rpm`
```

The version in the package name will vary according to the actual version that's listed in the EC2 local directory
`/opt/elasticbeanstalk/RPMS`. Use the same syntax to install other PHP 8.1 RPM packages.

Expand the following section to display a list of RPM packages we provide.

The following list provides the RMP packages that the Elastic Beanstalk PHP 8.1 platform provides on Amazon Linux 2. These are located in the local directory
`/opt/elasticbeanstalk/RPMS`.

The version numbers _8.1.8-1_ and _3.7.0-1_ in the listed package names are only an example.

- `php-8.1.8-1.amzn2.x86_64.rpm`
- `php-bcmath-8.1.8-1.amzn2.x86_64.rpm`
- `php-cli-8.1.8-1.amzn2.x86_64.rpm`
- `php-common-8.1.8-1.amzn2.x86_64.rpm`
- `php-dba-8.1.8-1.amzn2.x86_64.rpm`
- `php-dbg-8.1.8-1.amzn2.x86_64.rpm`
- `php-debuginfo-8.1.8-1.amzn2.x86_64.rpm`
- `php-devel-8.1.8-1.amzn2.x86_64.rpm`
- `php-embedded-8.1.8-1.amzn2.x86_64.rpm`
- `php-enchant-8.1.8-1.amzn2.x86_64.rpm`
- `php-fpm-8.1.8-1.amzn2.x86_64.rpm`
- `php-gd-8.1.8-1.amzn2.x86_64.rpm`
- `php-gmp-8.1.8-1.amzn2.x86_64.rpm`
- `php-intl-8.1.8-1.amzn2.x86_64.rpm`
- `php-ldap-8.1.8-1.amzn2.x86_64.rpm`
- `php-mbstring-8.1.8-1.amzn2.x86_64.rpm`
- `php-mysqlnd-8.1.8-1.amzn2.x86_64.rpm`
- `php-odbc-8.1.8-1.amzn2.x86_64.rpm`
- `php-opcache-8.1.8-1.amzn2.x86_64.rpm`
- `php-pdo-8.1.8-1.amzn2.x86_64.rpm`
- `php-pear-1.10.13-1.amzn2.noarch.rpm`
- `php-pgsql-8.1.8-1.amzn2.x86_64.rpm`
- `php-process-8.1.8-1.amzn2.x86_64.rpm`
- `php-pspell-8.1.8-1.amzn2.x86_64.rpm`
- `php-snmp-8.1.8-1.amzn2.x86_64.rpm`
- `php-soap-8.1.8-1.amzn2.x86_64.rpm`
- `php-sodium-8.1.8-1.amzn2.x86_64.rpm`
- `php-xml-8.1.8-1.amzn2.x86_64.rpm`
- `php-pecl-imagick-3.7.0-1.amzn2.x86_64.rpm`
- `php-pecl-imagick-debuginfo-3.7.0-1.amzn2.x86_64.rpm`
- `php-pecl-imagick-devel-3.7.0-1.amzn2.noarch.rpm`
  You can use the PEAR and PECL packages to install common extensions. For more information about PEAR, see the [PEAR PHP
  Extension and Application Repository](https://pear.php.net "https://pear.php.net") website. For more information about PECL, see the [PECL extension](https://pecl.php.net "https://pecl.php.net")
  website.

The following example commands install the Memcached extensions.

```
$`pecl install memcache`
```

Or you could also use the following:

```
$`pear install pecl/memcache`
```

The following example commands install the Redis extensions.

```
$`pecl install redis`
```

Or you could also use the following:

```
$`pear install pecl/redis`
```

## Configuring your PHP environment

You can use the Elastic Beanstalk console to enable log rotation to Amazon S3, configure variables that your application can read from the environment, and change
PHP settings.

###### To configure your PHP environment in the Elastic Beanstalk console

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk "https://console.aws.amazon.com/elasticbeanstalk"),
   and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.
3. In the navigation pane, choose **Configuration**.
4. In the **Updates, monitoring, and logging** configuration category, choose **Edit**.

### PHP settings

- **Proxy server** – The proxy server to use on your environment instances. By default, nginx is used.
- **Document root** – The folder that contains your site's default page. If your welcome page is not at the root of your
  source bundle, specify the folder that contains it relative to the root path. For example, `/public` if the welcome page is in a folder
  named `public`.
- **Memory limit** – The maximum amount of memory that a script is allowed to allocate. For example,
  `512M`.
- **Zlib output compression** – Set to `On` to compress responses.
- **Allow URL fopen** – Set to `Off` to prevent scripts from downloading files from remote locations.
- **Display errors** – Set to `On` to show internal error messages for debugging.
- **Max execution time** – The maximum time in seconds that a script is allowed to run before the environment terminates
  it.

### Log options

The Log Options section has two settings:

- **Instance profile**– Specifies the instance profile that has permission to access the Amazon S3 bucket associated with
  your application.
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

The **Environment Properties** section lets you specify environment configuration settings on the Amazon EC2 instances that are
running your application. These settings are passed in as key-value pairs to the application.

Your application code can access environment properties by using `$_SERVER` or the `get_cfg_var` function.

```
$endpoint = $_SERVER['API_ENDPOINT'];
```

See [Environment variables and other software settings](environments-cfg-softwaresettings.md "environments-cfg-softwaresettings.md")
for more information.

## Namespaces for configuration

You can use a [configuration file](ebextensions.md "ebextensions.md") to set configuration
options and perform other instance configuration tasks during deployments. Configuration options can be [platform specific](command-options-specific.md "command-options-specific.md")
or apply to [all platforms](command-options-general.md "command-options-general.md") in the Elastic Beanstalk service as a whole. Configuration options are organized into
_namespaces_.

The following namespaces configure both your proxy service and PHP specific options:

- [aws:elasticbeanstalk:environment:proxy:staticfiles](command-options-general.md#command-options-general-environmentproxystaticfiles "command-options-general.md#command-options-general-environmentproxystaticfiles")
  – configure the environment proxy to serve static files. You define mappings of virtual paths to application directories.
- [aws:elasticbeanstalk:environment:proxy](command-options-specific.md#command-options-php "command-options-specific.md#command-options-php") – specify the environment's proxy server.
- [aws:elasticbeanstalk:container:php:phpini](command-options-specific.md#command-options-php "command-options-specific.md#command-options-php") – configure PHP specific options. This
  namespace includes `composer_options`, which is not available on the Elastic Beanstalk console. This option sets the custom options to use when
  installing dependencies using Composer through the `composer.phar install` command. For more information about this command,
  including available options, see [install](https://getcomposer.org/doc/03-cli.md#install-i "https://getcomposer.org/doc/03-cli.md#install-i") on the _getcomposer.org_ website.

The following example [configuration file](ebextensions.md "ebextensions.md") specifies a static files option that maps a directory named
`staticimages` to the path `/images`, and shows settings for each of the options available in the
`aws:elasticbeanstalk:container:php:phpini` namespace:

###### Example .ebextensions/php-settings.config

```
option_settings:
  aws:elasticbeanstalk:environment:proxy:
    ProxyServer: apache
  aws:elasticbeanstalk:environment:proxy:staticfiles:
    /images: staticimages
  aws:elasticbeanstalk:container:php:phpini:
    document_root: /public
    memory_limit: 128M
    zlib.output_compression: "Off"
    allow_url_fopen: "On"
    display_errors: "Off"
    max_execution_time: 60
    composer_options: vendor/package
```

###### Note

The `aws:elasticbeanstalk:environment:proxy:staticfiles` namespace isn't defined on Amazon Linux AMI PHP platform branches (preceding
Amazon Linux 2).

Elastic Beanstalk provides many configuration options for customizing your environment. In
addition to configuration files, you can also set configuration options using the console, saved configurations, the EB CLI, or the AWS CLI.
See [Configuration options](command-options.md "command-options.md") for more information.

## Installing your Elastic Beanstalk PHP application's dependencies

This topic describes how to configure you application to install other PHP packages that it requires. Your application might have dependencies on
other PHP packages. You can configure your application to install these dependencies on the environment's Amazon Elastic Compute Cloud (Amazon EC2) instances. Alternatively, you
can include your application's dependencies in the source bundle and deploy them with the application. The following section discuss both of these
ways.

### Use a Composer file to install dependencies on instances

Use a `composer.json` file in the root of your project source to use composer to install packages that your application requires
on your environment's Amazon EC2 instances.

###### Example composer.json

```
{
    "require": {
        "monolog/monolog": "1.0.*"
    }
}
```

When a `composer.json` file is present, Elastic Beanstalk runs `composer.phar install` to install dependencies. You can add
options to append to the command by setting the [composer_options option](#php-namespaces "#php-namespaces") in the
`aws:elasticbeanstalk:container:php:phpini` namespace.

### Include dependencies in source bundle

If your application has a large number of dependencies, installing them might take a long time. This can increase deployment and scaling operations,
because dependencies are installed on every new instance.

To avoid the negative impact on deployment time, use Composer in your development environment to resolve dependencies and install them into the
`vendor` folder.

###### To include dependencies in your application source bundle

1. Run the following command:

```
`%` composer install
```

2. Include the generated `vendor` folder in the root of your application source bundle.

When Elastic Beanstalk finds a `vendor` folder on the instance, it ignores the `composer.json` file (even if it exists).
Your application then uses dependencies from the `vendor` folder.

## Updating Composer on Elastic Beanstalk

This topic describes how to configure Elastic Beanstalk to keep Composer up to date. You may have to update Composer if you see an error when you try to install
packages with a Composer file, or if you're unable to use the latest platform version. Between platform updates, you can update Composer in your
environment instances through the use of configuration files in your [.ebextensions](ebextensions.md "ebextensions.md") folder.

You can self-update Composer with the following configuration.

```
commands:
  01updateComposer:
    command: /usr/bin/composer.phar self-update `2.7.0`
```

The following [option setting](command-options-general.md#command-options-general-elasticbeanstalkapplicationenvironment "command-options-general.md#command-options-general-elasticbeanstalkapplicationenvironment") sets the `COMPOSER_HOME`
environment variable, which configures the location of the Composer cache.

```
option_settings:
  - namespace: aws:elasticbeanstalk:application:environment
    option_name: COMPOSER_HOME
    value: /home/webapp/composer-home
```

You can combine both of these in the same configuration file in your `.ebextensions` folder.

###### Example .ebextensions/composer.config

```
commands:
  01updateComposer:
    command: /usr/bin/composer.phar self-update `2.7.0`

option_settings:
  - namespace: aws:elasticbeanstalk:application:environment
    option_name: COMPOSER_HOME
    value: /home/webapp/composer-home
```

###### Note

Due to updates to the Composer installation in the [February 22, 2024](../relnotes/release-2024-02-22-al2023.md "../relnotes/release-2024-02-22-al2023.md"), AL2023 platform release and the [February 28, 2024](../relnotes/release-2024-02-28-al2.md "../relnotes/release-2024-02-28-al2.md"), AL2 platform release, the Composer self-update may fail
if `COMPOSER_HOME` is set when the self-update executes.

The following combined commands will fail to execute: `export COMPOSER_HOME=/home/webapp/composer-home && /usr/bin/composer.phar
 self-update 2.7.0`

However, the previous example will work. In the previous example, the option setting for `COMPOSER_HOME` will not be passed to the
`01updateComposer` execution, and it will not be set when the self-update command executes.

###### Important

If you omit the version number from the `composer.phar self-update` command, Composer will update to the latest version available every
time you deploy your source code, and when new instances are provisioned by Auto Scaling. This could cause scaling operations and deployments to fail if a
version of Composer is released that is incompatible with your application.

For more information about the Elastic Beanstalk PHP Platforms, including the version of Composer, see [PHP platform versions](../platforms/platforms-supported.md#platforms-supported.PHP "../platforms/platforms-supported.md#platforms-supported.PHP") in the document
_AWS Elastic Beanstalk Platforms_.

## Extending php.ini in your Elastic Beanstalk configuration

Use a configuration file with a `files` block to add a `.ini` file to `/etc/php.d/` on the instances
in your environment. The main configuration file, `php.ini`, pulls in settings from files in this folder in alphabetical order. Many
extensions are enabled by default by files in this folder.

###### Example .ebextensions/mongo.config

```
files:
  "/etc/php.d/99mongo.ini":
    mode: "000755"
    owner: root
    group: root
    content: |
      extension=mongo.so
```
