# Using the PHP platform

###### Important

App Runner will end the support for **PHP 8.1** on December 31, 2025. For recommendations and more information, see [End of support for managed runtime
versions](service-source-code.md#service-source-code.managed-platforms.eos "service-source-code.md#service-source-code.managed-platforms.eos").

The AWS App Runner PHP platform provides managed runtimes. You can use each runtime to build and
run containers with web applications based on a PHP version. When you use a PHP runtime, App Runner
starts with a managed PHP runtime image. This image is based on the [Amazon Linux Docker image](https://hub.docker.com/_/amazonlinux "https://hub.docker.com/_/amazonlinux") and contains the runtime
package for a version of PHP and some tools. App Runner uses this managed runtime image as a base
image, and adds your application code to build a Docker image. It then deploys this image to run
your web service in a container.

You specify a runtime for your App Runner service when you [create a service](manage-create.md "manage-create.md") using the App Runner console or the [CreateService](../api/API_CreateService.md "../api/API_CreateService.md") API operation. You can also specify a runtime as part of your source code. Use the
`runtime` keyword in a [App Runner configuration file](config-file.md "config-file.md") that you include in your code repository.
The naming convention of a managed runtime is `<language-name><major-version>`.

For valid PHP runtime names and versions, see [PHP runtime release information](service-source-code-php-releases.md "service-source-code-php-releases.md").

App Runner updates the runtime for your service to the latest version on every deployment or service update. If your application requires a specific version of
a managed runtime, you can specify it using the `runtime-version` keyword in the [App Runner configuration file](config-file.md "config-file.md"). You
can lock to any level of version, including a major or minor version. App Runner only makes lower-level updates to the runtime of your service.

Version syntax for PHP runtimes:
``major`[.`minor`[.`patch`]]`

For example: `8.1.10`

The following are examples of version locking:

- `8.1` – Lock the major and minor versions. App Runner updates only patch
  versions.
- `8.1.10` – Lock to a specific patch version. App Runner doesn't update your
  runtime version.

###### Important

If you'd like to specify the code repository [source directory](service-source-code.md#service-source-code.source-directory "service-source-code.md#service-source-code.source-directory") for your App Runner service
in a location other than the default repository root directory, your PHP managed runtime version must be PHP `8.1.22` or later. PHP runtime
versions prior to `8.1.22` may only use the default root source directory.

###### Topics

- [PHP runtime configuration](#service-source-code-php.config "#service-source-code-php.config")
- [Compatibility](#service-source-code-php.compatibility "#service-source-code-php.compatibility")
- [PHP runtime examples](#service-source-code-php.examples "#service-source-code-php.examples")
- [PHP runtime release information](service-source-code-php-releases.md "service-source-code-php-releases.md")

## PHP runtime configuration

When you choose a managed runtime, you must also configure, as a minimum, build and run commands. You configure them while [creating](manage-create.md "manage-create.md") or [updating](manage-configure.md "manage-configure.md") your App Runner service. You can do this using one of the following methods:

- Using the App Runner console – Specify the commands in the **Configure build** section of the
  creation process or configuration tab.
- Using the App Runner API – Call the [CreateService](../api/API_CreateService.md "../api/API_CreateService.md") or [UpdateService](../api/API_UpdateService.md "../api/API_UpdateService.md") API operation. Specify the commands using the `BuildCommand` and
  `StartCommand` members of the [CodeConfigurationValues](../api/API_CodeConfigurationValues.md "../api/API_CodeConfigurationValues.md") data type.
- Using a [configuration file](config-file.md "config-file.md") – Specify one or more build commands in up to
  three build phases, and a single run command that serves to start your application. There are additional optional configuration settings.

Providing a configuration file is optional. When you create an App Runner service using the console or the API, you specify if App Runner gets your configuration
settings directly when it's created or from a configuration file.

## Compatibility

You can run your App Runner services on PHP platform using one of the following web servers:

- Apache HTTP Server
- NGINX

Apache HTTP Server and NGINX are compatible with PHP-FPM.
You can start the _Apache HTTP Server_ and
_NGINX_ by using one of the following:

- [Supervisord](http://supervisord.org/introduction.html#supervisor-components/ "http://supervisord.org/introduction.html#supervisor-components/") - For more information about running a
  _supervisord_, see [Running
  supervisord](http://supervisord.org/running.html#running-supervisord "http://supervisord.org/running.html#running-supervisord").
- Startup script

For examples on how to configure your App Runner service with PHP platform using
_Apache HTTP Server_ or _NGINX_, see [Complete PHP application
source](#service-source-code-php.examples.end2end "#service-source-code-php.examples.end2end").

### File

Structure

The `index.php` must be installed in the `public` folder
under the `root` directory of the web server.

###### Note

We recommend that the `startup.sh` or
`supervisord.conf` files be stored in the root directory of the web
server. Make sure that the `start` command points to the location where the
`startup.sh` or `supervisord.conf` files are
stored.

The following is an example of the file structure if you are using
_supervisord_.

```
/
├─ public/
│  ├─ index.php
├─ apprunner.yaml
├─ supervisord.conf
```

The following is an example of the file structure if you are using _startup
script_.

```
/
├─ public/
│  ├─ index.php
├─ apprunner.yaml
├─ startup.sh
```

We recommend that you store these file structures in the code repository [source directory](service-source-code.md#service-source-code.source-directory "service-source-code.md#service-source-code.source-directory") that’s designated
for the App Runner service.

```
/<`sourceDirectory`>/
├─ public/
│  ├─ index.php
├─ apprunner.yaml
├─ startup.sh
```

###### Important

If you'd like to specify the code repository [source directory](service-source-code.md#service-source-code.source-directory "service-source-code.md#service-source-code.source-directory") for your App Runner service
in a location other than the default repository root directory, your PHP managed runtime version must be PHP `8.1.22` or later. PHP runtime
versions prior to `8.1.22` may only use the default root source directory.

App Runner updates the runtime for your service to the latest version on every deployment or
service update. Your service will use the most recent runtimes by default, unless you
specified version locking using the `runtime-version` keyword in the [App Runner configuration file](config-file.md "config-file.md").

## PHP runtime examples

The following are examples of App Runner configuration files that are used for building and
running a PHP service.

The following example is a minimal configuration file that you can use with a PHP
managed runtime. For more information about a minimal configuration file, see [Configuration file
examples](config-file-examples.md#config-file-examples.managed "config-file-examples.md#config-file-examples.managed").

###### Example apprunner.yaml

```
version: 1.0
runtime: php81
build:
  commands:
    build:
      - echo example build command for PHP
run:
  command: ./startup.sh
```

The following example uses all the configuration keys with a PHP managed
runtime.

###### Note

The runtime version that's used in these examples is
`8.1.10`. You can replace it with a version you want to use.
For latest supported PHP runtime version, see [PHP runtime release information](service-source-code-php-releases.md "service-source-code-php-releases.md").

###### Example apprunner.yaml

```
version: 1.0
runtime: php81
build:
  commands:
     pre-build:
      - scripts/prebuild.sh
    build:
      - echo example build command for PHP
    post-build:
      - scripts/postbuild.sh
  env:
    - name: MY_VAR_EXAMPLE
      value: "example"
run:
  runtime-version: `8.1.10`
  command: ./startup.sh
  network:
    port: 5000
    env: APP_PORT
  env:
    - name: MY_VAR_EXAMPLE
      value: "example"
```

The following examples are of PHP application source code that you can use to deploy
to a PHP runtime service using _Apache HTTP Server_ or
_NGINX_. These examples assume that you use the
default file structure.

#### Running

PHP platform with Apache HTTP Server using
supervisord

###### Example File structure

###### Note

- The `supervisord.conf` file can be stored anywhere in the
  repository. Make sure that the `start` command points to where the
  `supervisord.conf` file is stored.
- The `index.php` must be installed in the
  `public` folder under the `root` directory.

```
/
├─ public/
│  ├─ index.php
├─ apprunner.yaml
├─ supervisord.conf
```

###### Example supervisord.conf

```
`[supervisord]
nodaemon=true

[program:httpd]
command=httpd -DFOREGROUND
autostart=`true`
autorestart=`true`
stdout_logfile=/dev/stdout
stdout_logfile_maxbytes=0
stderr_logfile=/dev/stderr
stderr_logfile_maxbytes=0

[program:php-fpm]
command=php-fpm -F
autostart=`true`
autorestart=`true`
stdout_logfile=/dev/stdout
stdout_logfile_maxbytes=0
stderr_logfile=/dev/stderr
stderr_logfile_maxbytes=0`
```

###### Example apprunner.yaml

```
version: 1.0
runtime: php81
build:
  commands:
    build:
      - PYTHON=python2 amazon-linux-extras install epel
      - yum -y install supervisor
run:
  command: supervisord
  network:
    port: 8080
    env: APP_PORT
```

###### Example index.php

```
<html>
<head> <title>First PHP App</title> </head>
<body>
<?php
    print("Hello World!");
    print("<br>");
?>
</body>
</html>
```

#### Running

PHP platform with Apache HTTP Server using startup
script

###### Example File structure

###### Note

- The `startup.sh` file can be stored anywhere in the
  repository. Make sure that the `start` command points to where the
  `startup.sh` file is stored.
- The `index.php` must be installed in the
  `public` folder under the `root` directory.

```
/
├─ public/
│  ├─ index.php
├─ apprunner.yaml
├─ startup.sh
```

###### Example startup.sh

```
#!/bin/bash

set -o monitor

trap exit SIGCHLD

# Start apache
httpd -DFOREGROUND &

# Start php-fpm
php-fpm -F &

wait
```

###### Note

- Make sure to save the `startup.sh` file as an executable
  before you commit it to a Git repository. Use `chmod +x startup.sh` to
  set execute permission on your `startup.sh` file.
- If you don't save the `startup.sh` file as an executable,
  enter `chmod +x startup.sh` as the `build` command in your
  `apprunner.yaml` file.

###### Example apprunner.yaml

```
version: 1.0
runtime: php81
build:
  commands:
    build:
      - echo example build command for PHP
run:
  command: ./startup.sh
  network:
    port: 8080
    env: APP_PORT
```

###### Example index.php

```
<html>
<head> <title>First PHP App</title> </head>
<body>
<?php
    print("Hello World!");
    print("<br>");
?>
</body>
</html>
```

#### Running PHP

platform with NGINX using supervisord

###### Example File structure

###### Note

- The `supervisord.conf` file can be stored anywhere in the
  repository. Make sure that the `start` command points to where the
  `supervisord.conf` file is stored.
- The `index.php` must be installed in the
  `public` folder under the `root` directory.

```
/
├─ public/
│  ├─ index.php
├─ apprunner.yaml
├─ supervisord.conf
```

###### Example supervisord.conf

```
`[supervisord]
nodaemon=true

[program:nginx]
command=nginx -g "daemon off;"
autostart=`true`
autorestart=`true`
stdout_logfile=/dev/stdout
stdout_logfile_maxbytes=0
stderr_logfile=/dev/stderr
stderr_logfile_maxbytes=0

[program:php-fpm]
command=php-fpm -F
autostart=`true`
autorestart=`true`
stdout_logfile=/dev/stdout
stdout_logfile_maxbytes=0
stderr_logfile=/dev/stderr
stderr_logfile_maxbytes=0`
```

###### Example apprunner.yaml

```
version: 1.0
runtime: php81
build:
  commands:
    build:
      - PYTHON=python2 amazon-linux-extras install epel
      - yum -y install supervisor
run:
  command: supervisord
  network:
    port: 8080
    env: APP_PORT
```

###### Example index.php

```
<html>
<head> <title>First PHP App</title> </head>
<body>
<?php
    print("Hello World!");
    print("<br>");
?>
</body>
</html>
```

#### Running

PHP platform with NGINX using startup script

###### Example File structure

###### Note

- The `startup.sh` file can be stored anywhere in the
  repository. Make sure that the `start` command points to where the
  `startup.sh` file is stored.
- The `index.php` must be installed in the
  `public` folder under the `root` directory.

```
/
├─ public/
│  ├─ index.php
├─ apprunner.yaml
├─ startup.sh
```

###### Example startup.sh

```
#!/bin/bash

set -o monitor

trap exit SIGCHLD

# Start nginx
nginx -g 'daemon off;' &

# Start php-fpm
php-fpm -F &

wait
```

###### Note

- Make sure to save the `startup.sh` file as an executable
  before you commit it to a Git repository. Use `chmod +x startup.sh` to
  set execute permission on your `startup.sh` file.
- If you don't save the `startup.sh` file as an executable,
  enter `chmod +x startup.sh` as the `build` command in your
  `apprunner.yaml` file.

###### Example apprunner.yaml

```
version: 1.0
runtime: php81
build:
  commands:
    build:
      - echo example build command for PHP
run:
  command: ./startup.sh
  network:
    port: 8080
    env: APP_PORT
```

###### Example index.php

```
<html>
<head> <title>First PHP App</title> </head>
<body>
<?php
    print("Hello World!");
    print("<br>");
?>
</body>
</html>
```
