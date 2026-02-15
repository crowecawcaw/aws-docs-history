#

Using the Elastic Beanstalk Ruby platform

This topic describes how to configure, build, and run your Ruby applications on Elastic Beanstalk.

AWS Elastic Beanstalk supports a number of platform branches for different versions of the Ruby programming language. See [Ruby](../platforms/platforms-supported.md#platforms-supported.ruby "../platforms/platforms-supported.md#platforms-supported.ruby") in the _AWS Elastic Beanstalk Platforms_ document
for a full list.

The Ruby web application can run behind an NGINX proxy server under a Puma application server. If you use RubyGems, you can include a [Gemfile](ruby-platform-gemfile.md "ruby-platform-gemfile.md") in your source bundle to install packages during deployment.

###### Application server configuration

Elastic Beanstalk installs the Puma application server based on the Ruby platform branch that you choose when you create your environment. For more information
about the components provided with the Ruby platform versions, see [Supported Platforms](../platforms/platforms-supported.md#platforms-supported.ruby "../platforms/platforms-supported.md#platforms-supported.ruby") in the
_AWS Elastic Beanstalk Platforms_ guide.

You can configure your application with your own provided Puma server. This provides the option to use a version of Puma other than the one
pre-installed with the Ruby platform branch. You can also configure your application to use a different application server, such as Passenger. To do so, you
must include and customize a `Gemfile` in your deployment. You're also required to configure a `Procfile` to start the
application server. For more information see _[Configuring the application process with a
Procfile](ruby-platform-procfile.md "ruby-platform-procfile.md")\*\*._

###### Other configuration options

Elastic Beanstalk provides [configuration options](command-options.md "command-options.md") that you can use to customize the software that runs on the Amazon Elastic Compute Cloud
(Amazon EC2) instances in your Elastic Beanstalk environment. You can configure environment variables needed by your application, enable log rotation to Amazon S3, and map
folders in your application source that contain static files to paths served by the proxy server. The platform also predefines some common environment
variables related to Rails and Rack for ease of discovery and use.

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

Settings applied in the Elastic Beanstalk console override the same
settings in configuration files, if they exist. This lets you have default settings in configuration
files, and override them with environment-specific settings in the console. For more information
about precedence, and other methods of changing settings, see [Configuration options](command-options.md "command-options.md").

For details about the various ways you can extend an Elastic Beanstalk Linux-based platform, see [Extending Elastic Beanstalk Linux platforms](platforms-linux-extend.md "platforms-linux-extend.md").

## Configuring your Ruby environment

You can use the Elastic Beanstalk console to enable log rotation to Amazon S3 and configure variables that your application can read from the environment.

###### To access the software configuration settings for your environment

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk "https://console.aws.amazon.com/elasticbeanstalk"),
   and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.
3. In the navigation pane, choose **Configuration**.
4. In the **Updates, monitoring, and logging** configuration category, choose **Edit**.

### Log options

The **Log options** section has two settings:

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

By default, the proxy server in a Ruby environment is configured to serve static files as follows:

- Files in the `public` folder are served from the `/public` path and the domain root
  (`/` path).
- Files in the `public/assets` subfolder are served from the `/assets` path.

The following examples illustrate how the default configuration works:

- If your application source contains a file named `logo.png` in a folder named `public`, the proxy server
  serves it to users from ``subdomain`.elasticbeanstalk.com/public/logo.png` and
``subdomain`.elasticbeanstalk.com/logo.png`.
- If your application source contains a file named `logo.png` in a folder named `assets` inside the
  `public` folder, the proxy server serves it from
  ``subdomain`.elasticbeanstalk.com/assets/logo.png`.

You can configure additional mappings for static files. For more information, see [Ruby configuration namespaces](#ruby-namespaces "#ruby-namespaces")
later in this topic.

###### Note

For platform versions prior to _Ruby 2.7 AL2 version 3.3.7_, the default Elastic Beanstalk nginx proxy server configuration doesn't support
serving static files from the domain root (``subdomain`.elasticbeanstalk.com/`). This platform version was
released on October 21, 2021. For more information see [New platform versions - Ruby](../relnotes/release-2021-10-21-linux.md#release-2021-10-21-linux.platforms.ruby "../relnotes/release-2021-10-21-linux.md#release-2021-10-21-linux.platforms.ruby") in
the _AWS Elastic Beanstalk Release Notes_.

### Environment properties

The **Environment Properties** section lets you specify environment configuration settings on the Amazon EC2 instances that are running
your application. Environment properties are passed in as key-value pairs to the application.

The Ruby platform defines the following properties for environment configuration:

- **BUNDLE_WITHOUT** – A colon-separated list of groups to ignore when [installing dependencies](http://bundler.io/bundle_install.html "http://bundler.io/bundle_install.html") from a [Gemfile](http://bundler.io/v1.15/man/gemfile.5.html "http://bundler.io/v1.15/man/gemfile.5.html").
- **BUNDLER_DEPLOYMENT_MODE** – Set to `true` (the default) to install dependencies in [deployment mode](https://bundler.io/man/bundle-install.1.html#DEPLOYMENT-MODE "https://bundler.io/man/bundle-install.1.html#DEPLOYMENT-MODE") using Bundler. Set to `false` to run
  `bundle install` in development mode.

###### Note

This environment property isn't defined on Amazon Linux AMI Ruby platform branches (preceding Amazon Linux 2).

- **RAILS_SKIP_ASSET_COMPILATION** – Set to `true` to skip running [`rake assets:precompile`](http://guides.rubyonrails.org/asset_pipeline.html#precompiling-assets "http://guides.rubyonrails.org/asset_pipeline.html#precompiling-assets") during deployment.
- **RAILS_SKIP_MIGRATIONS** – Set to `true` to skip running [`rake db:migrate`](http://guides.rubyonrails.org/active_record_migrations.html#running-migrations "http://guides.rubyonrails.org/active_record_migrations.html#running-migrations") during
  deployment.
- **RACK_ENV** – Specify the environment stage for Rack. For example, `development`, `production`, or
  `test`.

Inside the Ruby environment running in Elastic Beanstalk, environment variables are accessible using the `ENV` object. For example, you could read a
property named `API_ENDPOINT` to a variable with the following code:

```
endpoint = ENV['API_ENDPOINT']
```

See [Environment variables and other software settings](environments-cfg-softwaresettings.md "environments-cfg-softwaresettings.md")
for more information.

## Ruby configuration namespaces

You can use a [configuration file](ebextensions.md "ebextensions.md") to set configuration
options and perform other instance configuration tasks during deployments. Configuration options can be [platform specific](command-options-specific.md "command-options-specific.md")
or apply to [all platforms](command-options-general.md "command-options-general.md") in the Elastic Beanstalk service as a whole. Configuration options are organized into
_namespaces_.

You can use the `aws:elasticbeanstalk:environment:proxy:staticfiles` namespace to configure the environment proxy to serve static files.
You define mappings of virtual paths to application directories.

The Ruby platform doesn't define any platform-specific namespaces. Instead, it defines environment properties for common Rails and Rack
options.

The following configuration file specifies a static files option that maps a directory named `staticimages` to the path
`/images`, sets each of the platform defined environment properties, and sets an additional environment property named
`LOGGING`.

###### Example.ebextensions/ruby-settings.config

```
option_settings:
  aws:elasticbeanstalk:environment:proxy:staticfiles:
    /images: staticimages
  aws:elasticbeanstalk:application:environment:
    BUNDLE_WITHOUT: test
    BUNDLER_DEPLOYMENT_MODE: true
    RACK_ENV: development
    RAILS_SKIP_ASSET_COMPILATION: true
    RAILS_SKIP_MIGRATIONS: true
    LOGGING: debug
```

###### Note

The `BUNDLER_DEPLOYMENT_MODE` environment property and the `aws:elasticbeanstalk:environment:proxy:staticfiles` namespace
aren't defined on Amazon Linux AMI Ruby platform branches (preceding Amazon Linux 2).

Elastic Beanstalk provides many configuration options for customizing your environment. In
addition to configuration files, you can also set configuration options using the console, saved configurations, the EB CLI, or the AWS CLI.
See [Configuration options](command-options.md "command-options.md") for more information.
