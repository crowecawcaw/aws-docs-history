# Using the Elastic Beanstalk Python platform

This topic describes how to configure, build, and run your Python applications on Elastic Beanstalk.

AWS Elastic Beanstalk supports a number of platform branches for different versions of the Python programming language. See [Python](../platforms/platforms-supported.md#platforms-supported.python "../platforms/platforms-supported.md#platforms-supported.python") in the _AWS Elastic Beanstalk Platforms_
document for a full list.

The Python web applications can run behind a proxy server with WSGI. Elastic Beanstalk provides [Gunicorn](https://gunicorn.org/ "https://gunicorn.org/") as the default
WSGI server.

You can add a `Procfile` to your source bundle to specify and configure the WSGI server for your application. For details, see [Configuring the WSGI server with a Procfile on Elastic Beanstalk](python-configuration-procfile.md "python-configuration-procfile.md").

You can use the `Pipfile` and `Pipfile.lock` files created by Pipenv to specify Python package dependencies and
other requirements. For details about specifying dependencies, see [Specifying dependencies using a requirements file on Elastic Beanstalk](python-configuration-requirements.md "python-configuration-requirements.md").

Elastic Beanstalk provides [configuration options](command-options.md "command-options.md") that you can use to customize the software that runs on the EC2 instances in
your Elastic Beanstalk environment. You can configure environment variables needed by your application, enable log rotation to Amazon S3, and map folders in your application
source that contain static files to paths served by the proxy server.

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

For Python packages available from `pip`, you can include a requirements file in the root of your application source code. Elastic Beanstalk installs any
dependency packages specified in a requirements file during deployment. For details, see [Specifying dependencies using a requirements file on Elastic Beanstalk](python-configuration-requirements.md "python-configuration-requirements.md").

For details about the various ways you can extend an Elastic Beanstalk Linux-based platform, see [Extending Elastic Beanstalk Linux platforms](platforms-linux-extend.md "platforms-linux-extend.md").

## Configuring your Python environment

The Python platform settings let you fine-tune the behavior of your Amazon EC2 instances. You can edit the Elastic Beanstalk environment's Amazon EC2 instance configuration
using the Elastic Beanstalk console.

Use the Elastic Beanstalk console to configure Python process settings, enable AWS X-Ray, enable log rotation to Amazon S3, and configure variables that your
application can read from the environment.

###### To configure your Python environment in the Elastic Beanstalk console

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk "https://console.aws.amazon.com/elasticbeanstalk"),
   and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.
3. In the navigation pane, choose **Configuration**.
4. In the **Updates, monitoring, and logging** configuration category, choose **Edit**.

### Python settings

- **Proxy server** – The proxy server to use on your environment instances. By default, nginx is used.
- **WSGI Path** – The name of or path to your main application file. For example, `application.py`, or
  `django/wsgi.py`.
- **NumProcesses** – The number of processes to run on each application instance.
- **NumThreads** – The number of threads to run in each process.

### AWS X-Ray settings

- **X-Ray daemon** – Run the AWS X-Ray daemon to process trace data from the [AWS X-Ray SDK for Python](../../../xray/latest/devguide/xray-sdk-python.md "../../../xray/latest/devguide/xray-sdk-python.md").

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

By default, the proxy server in a Python environment serves any files in a folder named `static` at the
`/static` path. For example, if your application source contains a file named `logo.png` in a folder named
`static`, the proxy server serves it to users at
``subdomain`.elasticbeanstalk.com/static/logo.png`. You can configure additional mappings as explained in
this section.

### Environment properties

You can use environment properties to provide information to your application and configure environment variables. For example, you can create an
environment property named `CONNECTION_STRING` that specifies a connection string that your application can use to connect to a
database.

Inside the Python environment running in Elastic Beanstalk, these values are accessible using Python's `os.environ` dictionary. For more information,
see [http://docs.python.org/library/os.html](http://docs.python.org/library/os.html "http://docs.python.org/library/os.html").

You can use code that looks similar to the following to access the keys and parameters:

```
import os
endpoint = os.environ['`API_ENDPOINT`']
```

Environment properties can also provide information to a framework. For example, you can create a property named
`DJANGO_SETTINGS_MODULE` to configure Django to use a specific settings module. Depending on the environment, the value could be
`development.settings`, `production.settings`, etc.

See [Environment variables and other software settings](environments-cfg-softwaresettings.md "environments-cfg-softwaresettings.md")
for more information.

## Python configuration namespaces

You can use a [configuration file](ebextensions.md "ebextensions.md") to set configuration
options and perform other instance configuration tasks during deployments. Configuration options can be [platform specific](command-options-specific.md "command-options-specific.md")
or apply to [all platforms](command-options-general.md "command-options-general.md") in the Elastic Beanstalk service as a whole. Configuration options are organized into
_namespaces_.

The Python platform defines options in the `aws:elasticbeanstalk:environment:proxy`,
`aws:elasticbeanstalk:environment:proxy:staticfiles`, and `aws:elasticbeanstalk:container:python` namespaces.

The following example configuration file specifies configuration option settings to create an environment property named
`DJANGO_SETTINGS_MODULE`, choose the Apache proxy server, specify two static files options that map a directory named
`statichtml` to the path `/html` and a directory named `staticimages` to the path
`/images`, and specify additional settings in the `aws:elasticbeanstalk:container:python` namespace. This namespace contains options that let you specify the location of the WSGI
script in your source code, and the number of threads and processes to run in WSGI.

```
option_settings:
  aws:elasticbeanstalk:application:environment:
    DJANGO_SETTINGS_MODULE: production.settings
  aws:elasticbeanstalk:environment:proxy:
    ProxyServer: apache
  aws:elasticbeanstalk:environment:proxy:staticfiles:
    /html: statichtml
    /images: staticimages
  aws:elasticbeanstalk:container:python:
    WSGIPath: ebdjango.wsgi:application
    NumProcesses: 3
    NumThreads: 20
```

###### Notes

- If you're using an Amazon Linux AMI Python platform version (preceding Amazon Linux 2), replace the value for `WSGIPath` with
  `ebdjango/wsgi.py`. The value in the example works with the Gunicorn WSGI server, which isn't supported on Amazon Linux AMI platform
  versions.
- In addition, these older platform versions use a different namespace for configuring static
  files—`aws:elasticbeanstalk:container:python:staticfiles`. It has the same option names and semantics as the standard static file
  namespace.

Configuration files also support several keys to further [modify the software on your environment's
instances](customize-containers-ec2.md "customize-containers-ec2.md"). This example uses the [packages](customize-containers-ec2.md#linux-packages "customize-containers-ec2.md#linux-packages") key to install Memcached with `yum` and [container commands](customize-containers-ec2.md#linux-container-commands "customize-containers-ec2.md#linux-container-commands") to run commands that configure the server during deployment:

```
packages:
  yum:
    libmemcached-devel: '0.31'

container_commands:
  collectstatic:
    command: "django-admin.py collectstatic --noinput"
  01syncdb:
    command: "django-admin.py syncdb --noinput"
    leader_only: true
  02migrate:
    command: "django-admin.py migrate"
    leader_only: true
  03wsgipass:
    command: 'echo "WSGIPassAuthorization On" >> ../wsgi.conf'
  99customize:
    command: "scripts/customize.sh"
```

Elastic Beanstalk provides many configuration options for customizing your environment. In
addition to configuration files, you can also set configuration options using the console, saved configurations, the EB CLI, or the AWS CLI.
See [Configuration options](command-options.md "command-options.md") for more information.

## The `python3` executable

The version of the `python3` executable available on EC2 instances in Elastic Beanstalk Python environments will not always correspond
to the same Python version used by the platform. For example, on the Python 3.12 AL2023 platform, `/usr/bin/python3` points to Python 3.9.
This is because Python 3.9 is the _system Python_ on AL2023. For more information, see [Python in AL2023](../../../linux/al2023/ug/python.md "../../../linux/al2023/ug/python.md") in the _Amazon Linux 2023 User Guide_. You can access an executable corresponding
to the Python version used by the platform at a versioned location (e.g. `/usr/bin/python3.12`) or in the application virtual environment
`bin` directory (e.g. `/var/app/venv/staging-LQM1lest/bin/python3`). The platform uses the correct Python
executable that corresponds to the platform branch.
