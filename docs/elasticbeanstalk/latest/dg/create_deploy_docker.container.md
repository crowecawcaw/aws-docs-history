# Configuring Elastic Beanstalk Docker environments

This chapter explains additional configuration information for all of the supported Docker platform branches, including the ECS managed Docker platform
branch. Unless a specific platform branch or platform branch component is identified in a section, it applies to all environments that are running supported
Docker and ECS manged Docker platforms.

###### Note

If your Elastic Beanstalk environment uses an Amazon Linux AMI Docker platform version (preceding Amazon Linux 2), be sure to read the additional information in [Docker configuration on Amazon Linux AMI (preceding Amazon Linux 2)](#docker-alami "#docker-alami").

###### Sections

- [Configuring software in Docker environments](#docker-software-config "#docker-software-config")
- [Referencing environment variables in containers](#docker-env-cfg.env-variables "#docker-env-cfg.env-variables")
- [Using interpolate feature for environment variables with Docker Compose](#docker-env-cfg.env-variables-dc-interpolate "#docker-env-cfg.env-variables-dc-interpolate")
- [Generating logs for enhanced health reporting with Docker Compose](#docker-env-cfg.healthd-logging "#docker-env-cfg.healthd-logging")
- [Docker container customized logging with Docker Compose](#docker-env-cfg.dc-customized-logging "#docker-env-cfg.dc-customized-logging")
- [Docker images](#docker-images "#docker-images")
- [Configuring managed updates for Docker environments](#docker-managed-updates "#docker-managed-updates")
- [Docker configuration namespaces](#docker-namespaces "#docker-namespaces")
- [Docker configuration on Amazon Linux AMI (preceding Amazon Linux 2)](#docker-alami "#docker-alami")

## Configuring software in Docker environments

You can use the Elastic Beanstalk console to configure the software running on your environment's instances.

###### To configure your Docker environment in the Elastic Beanstalk console

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk "https://console.aws.amazon.com/elasticbeanstalk"),
   and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.
3. In the navigation pane, choose **Configuration**.
4. In the **Updates, monitoring, and logging** configuration category, choose **Edit**.
5. Make necessary configuration changes.
6. To save the changes choose **Apply** at the bottom of the page.

For information about configuring software settings in any environment, see [Environment variables and other software settings](environments-cfg-softwaresettings.md "environments-cfg-softwaresettings.md"). The following
sections cover Docker specific information.

### Container options

The **Container options** section has platform-specific options. For Docker environments, it lets you choose whether or not your
environment includes the NGINX proxy server.

###### Environments with Docker Compose

If you manage your Docker environment with Docker Compose, Elastic Beanstalk assumes that you run a proxy server as a container. Therefore it defaults to
**None** for the **Proxy server** setting, and Elastic Beanstalk does not provide an NGINX configuration.

###### Note

Even if you select **NGINX** as a proxy server, this setting is ignored in an environment with Docker Compose. The
**Proxy server** setting still defaults to **None**.

Since the NGINX web server proxy is disabled for the Docker on Amazon Linux 2 platform with Docker Compose, you must follow the instructions for generating
logs for enhanced health reporting. For more information, see [Generating logs for enhanced health reporting with Docker Compose](#docker-env-cfg.healthd-logging "#docker-env-cfg.healthd-logging").

### Environment properties (environment variables)

You can use environment properties, (also known as environment variables), to pass values, such endpoints, debug settings, and other information to
your application. The **Environment variables** section of the console lets you specify environment variables on the EC2 instances that
are running your application. Environment variables are passed in as key-value pairs to the application.

Your application code running in a container can refer to an environment variable by name and read its value. The source code that reads these
environment variables will vary by programming language. You can find instructions for reading environment variable values in the programming languages
that Elastic Beanstalk managed platforms support in the respective platform topic. For a list of links to these topics, see [Environment variables and other software settings](environments-cfg-softwaresettings.md "environments-cfg-softwaresettings.md").

###### Secrets and parameters in Elastic Beanstalk environment variables

Elastic Beanstalk offers the ability to reference AWS Secrets Manager and AWS Systems Manager Parameter Store data in environment variables. This is a secure option for your
application to natively access secrets and parameters stored by these services without having to manage API calls to them. Your Elastic Beanstalk Docker and ECS
managed Docker platforms must be a version released on or after [March 26, 2025](../relnotes/release-2025-03-26-windows.md "../relnotes/release-2025-03-26-windows.md") to support this feature. For more information about using
environment variables to reference secrets, see [Fetching secrets and parameters to Elastic Beanstalk environment variables](AWSHowTo.secrets.md "AWSHowTo.secrets.md").

###### Environments with Docker Compose

If you manage your Docker environment with Docker Compose, you must make some additional configuration to retrieve the environment variables in
the containers. In order for the executables running in your container to access these environment variables, you must reference them in the
`docker-compose.yml`. For more information see [Referencing environment variables in containers](#docker-env-cfg.env-variables "#docker-env-cfg.env-variables").

## Referencing environment variables in containers

If you are using the Docker Compose tool on the Amazon Linux 2 Docker platform, Elastic Beanstalk generates a Docker Compose environment file called
`.env` in the root directory of your application project. This file stores the environment variables you configured for Elastic Beanstalk.

###### Note

If you include a `.env` file in your application bundle, Elastic Beanstalk will not generate an `.env` file.

In order for a container to reference the environment variables you define in Elastic Beanstalk, you must follow one or both of these configuration
approaches.

- Add the `.env` file generated by Elastic Beanstalk to the `env_file` configuration option in the `docker-compose.yml`
  file.
- Directly define the environment variables in the `docker-compose.yml` file.

The following files provide an example. The sample `docker-compose.yml` file demonstrates both approaches.

- If you define environment properties `DEBUG_LEVEL=1` and `LOG_LEVEL=error`, Elastic Beanstalk generates the following
  `.env` file for you:

```
DEBUG_LEVEL=1
LOG_LEVEL=error
```

- In this `docker-compose.yml` file, the `env_file` configuration option points to the `.env` file, and it also
  defines the environment variable `DEBUG=1` directly in the `docker-compose.yml` file.

```
services:
  web:
    build: .
    environment:
      - DEBUG=1
    env_file:
      - .env
```

###### Notes

- If you set the same environment variable in both files, the variable defined in the `docker-compose.yml` file has higher precedence than
  the variable defined in the `.env` file.
- Be careful to not leave spaces between the equal sign (=) and the value assigned to your variable in order to prevent spaces from being added to
  the string.

To learn more about environment variables in Docker Compose, see [Environment
variables in Compose](https://docs.docker.com/compose/environment-variables/ "https://docs.docker.com/compose/environment-variables/")

## Using interpolate feature for environment variables with Docker Compose

Starting with the [July 28, 2023](../relnotes/release-2023-07-28-al2.md "../relnotes/release-2023-07-28-al2.md") platform
release, the _Docker Amazon Linux 2_ platform branch offers the Docker Compose _interpolation_ feature. With this
feature, values in a Compose file can be set by variables and interpolated at runtime. For more information about this feature, see [Interpolation](https://docs.docker.com/compose/compose-file/12-interpolation/ "https://docs.docker.com/compose/compose-file/12-interpolation/") on the Docker documentation website.

###### Important

If you'd like to use this feature with your applications, be aware that you'll need to implement an approach that uses platform hooks.

This is necessary due a mitigation that we implemented in the platform engine. This mitigation ensures backward compatibility for customers that
aren't aware of the new interpolation feature and have existing applications that use environment variables with the `$` character. The
updated platform engine escapes the interpolation by default by replacing the `$` character with `$$` characters.

The following is an example of a platform hook script that you can set up to allow use of the interpolation feature.

```
#!/bin/bash

: '
example data format in .env file
key1=value1
key2=value2
'
envfile="/var/app/staging/.env"
tempfile=$(mktemp)

while IFS= read -r line; do
  # split each env var string at '='
  split_str=(${line//=/ })
  if [ ${#split_str[@]} -eq 2 ]; then
    # replace '$$' with '$'
    replaced_str=${split_str[1]//\$\$/\$}
    # update the value of env var using ${replaced_str}
    line="${split_str[0]}=${replaced_str}"
  fi
  # append the updated env var to the tempfile
  echo "${line}" ≫"${tempfile}"
done < "${envfile}"
# replace the original .env file with the tempfile
mv "${tempfile}" "${envfile}"
```

Place the platform hooks under both of these directories:

- `.platform/confighooks/predeploy/`
- `.platform/hooks/predeploy/`

For more information, see [Platform hooks](platforms-linux-extend.md "platforms-linux-extend.md") in the*Extending Linux platforms* topic of this guide.

## Generating logs for enhanced health reporting with Docker Compose

The [Elastic Beanstalk health agent](health-enhanced.md#health-enhanced-agent "health-enhanced.md#health-enhanced-agent") provides operating system and application health metrics for Elastic Beanstalk environments.
It relies on web server log formats that relay information in a specific format.

Elastic Beanstalk assumes that you run a web server proxy as a container. As a result the NGINX web server proxy is disabled for Docker environments running
Docker Compose. You must configure your server to write logs in the location and format that the Elastic Beanstalk health agent uses. Doing so allows you to make full
use of enhanced health reporting, even if the web server proxy is disabled.

For instructions on how to do this, see [Web server log configuration](health-enhanced-serverlogs.md#health-enhanced-serverlogs.configure "health-enhanced-serverlogs.md#health-enhanced-serverlogs.configure")

## Docker container customized logging with Docker Compose

In order to efficiently troubleshoot issues and monitor your containerized services, you can [request instance
logs](using-features.md "using-features.md") from Elastic Beanstalk through the environment management console or the EB CLI. Instance logs are comprised of bundle logs and tail logs, combined and
packaged to allow you to view logs and recent events in an efficient and straightforward manner.

Elastic Beanstalk creates log directories on the container instance, one for each service defined in the `docker-compose.yml` file, at
`/var/log/eb-docker/containers/`<service name>``. If you are using the Docker Compose feature on the Amazon Linux 2
Docker platform, you can mount these directories to the location within the container file structure where logs are written. When you mount log
directories for writing log data, Elastic Beanstalk can gather log data from these directories.

###### To configure your service's logs files to be retrievable tail files and bundle logs

1. Edit the `docker-compose.yml` file.
2. Under the `volumes` key for your service add a bind mount to be the following:

`"${EB_LOG_BASE_DIR}/`<service name>`:`<log directory inside container>``

In the sample `docker-compose.yml` file below:

    * `nginx-proxy` is `<service name>`
    * `/var/log/nginx` is `<log directory inside container>`

```
services:
  nginx-proxy:
    image: "nginx"
    volumes:
      - "${EB_LOG_BASE_DIR}/nginx-proxy:/var/log/nginx"
```

- The `var/log/nginx` directory contains the logs for the _nginx-proxy_ service in the container, and it will be
  mapped to the `/var/log/eb-docker/containers/nginx-proxy` directory on the host.
- All of the logs in this directory are now retrievable as bundle and tail logs through Elastic Beanstalk's [request
  instance logs](using-features.md "using-features.md") functionality.

###### Notes

- _${EB_LOG_BASE_DIR}_ is an environment variable set by Elastic Beanstalk with the value
  `/var/log/eb-docker/containers`.
- Elastic Beanstalk automatically creates the `/var/log/eb-docker/containers/`<service name>``directory for each
service in the`docker-compose.yml`file.

## Docker images

The Docker and ECS managed Docker platform branches for Elastic Beanstalk support the use of Docker images stored in a public or private online image
repository.

Specify images by name in `Dockerrun.aws.json`. Note these conventions:

- Images in official repositories on Docker Hub use a single name (for example, `ubuntu` or `mongo`).
- Images in other repositories on Docker Hub are qualified with an organization name (for example,
  `amazon/amazon-ecs-agent`).
- Images in other online repositories are qualified further by a domain name (for example, `quay.io/assemblyline/ubuntu` or
  ``account-id`.dkr.ecr.us-east-2.amazonaws.com/ubuntu:trusty`).

For environments using the Docker platform only, you can also build your own image during environment creation with a Dockerfile. See [Building custom images with a Dockerfile](single-container-docker-configuration.md#single-container-docker-configuration.dockerfile "single-container-docker-configuration.md#single-container-docker-configuration.dockerfile") for details. The ECS
managed Docker platform doesn't support this functionality.

## Configuring managed updates for Docker environments

With [managed platform updates](environment-platform-update-managed.md "environment-platform-update-managed.md"), you can configure your environment to automatically update
to the latest version of a platform on a schedule.

In the case of Docker environments, you might want to decide if an automatic platform update should happen across Docker versions—when the new
platform version includes a new Docker version. Elastic Beanstalk supports managed platform updates across Docker versions when updating from an environment running a
Docker platform version newer than 2.9.0. When a new platform version includes a new version of Docker, Elastic Beanstalk increments the minor update version number.
Therefore, to allow managed platform updates across Docker versions, enable managed platform updates for both minor and patch version updates. To prevent
managed platform updates across Docker versions, enable managed platform updates to apply patch version updates only.

For example, the following [configuration file](ebextensions.md "ebextensions.md") enables managed platform updates at 9:00 AM UTC each Tuesday for
both minor and patch version updates, thereby allowing for managed updates across Docker versions:

###### Example.ebextensions/managed-platform-update.config

```
option_settings:
  aws:elasticbeanstalk:managedactions:
    ManagedActionsEnabled: true
    PreferredStartTime: "Tue:09:00"
  aws:elasticbeanstalk:managedactions:platformupdate:
    UpdateLevel: `minor`
```

For environments running Docker platform versions 2.9.0 or earlier, Elastic Beanstalk never performs managed platform updates if the new platform version includes
a new Docker version.

## Docker configuration namespaces

You can use a [configuration file](ebextensions.md "ebextensions.md") to set configuration
options and perform other instance configuration tasks during deployments. Configuration options can be [platform specific](command-options-specific.md "command-options-specific.md")
or apply to [all platforms](command-options-general.md "command-options-general.md") in the Elastic Beanstalk service as a whole. Configuration options are organized into
_namespaces_.

###### Note

This information only applies to Docker environment that are not running Docker Compose. This option has a different behavior with Docker
environments that run Docker Compose. For further information on proxy services with Docker Compose see [Container options](#docker-software-config.container "#docker-software-config.container").

The Docker platform supports options in the following namespaces, in addition to the [options supported for all
Elastic Beanstalk environments](command-options-general.md "command-options-general.md"):

- `aws:elasticbeanstalk:environment:proxy` – Choose the proxy server for your environment. Docker supports either running Nginx or
  no proxy server.

The following example configuration file configures a Docker environment to run no proxy server.

###### Example.ebextensions/docker-settings.config

```
option_settings:
  aws:elasticbeanstalk:environment:proxy:
    ProxyServer: none
```

## Docker configuration on Amazon Linux AMI (preceding Amazon Linux 2)

If your Elastic Beanstalk Docker environment uses an Amazon Linux AMI platform version (preceding Amazon Linux 2), read the additional information in this section.

This information is relevant to you if you are [using images from a private repository](docker-configuration.md "docker-configuration.md").
Beginning with Docker version 1.7, the **docker login** command changed the name of the authentication file, and the format of the
file. Amazon Linux AMI Docker platform versions (preceding Amazon Linux 2) require the older `~/.dockercfg` format configuration file.

With Docker version 1.7 and later, the **docker login** command creates the authentication file in
`~/.docker/config.json` in the following format.

```
{
    "auths":{
      "`server`":{
        "auth":"`key`"
      }
    }
  }
```

With Docker version 1.6.2 and earlier, the **docker login** command creates the authentication file in
`~/.dockercfg` in the following format.

```
{
    "`server`" :
    {
      "auth" : "`auth_token`",
      "email" : "`email`"
    }
  }
```

To convert a `config.json` file, remove the outer `auths` key, add an `email` key, and flatten the JSON
document to match the old format.

On Amazon Linux 2 Docker platform versions, Elastic Beanstalk uses the newer authentication file name and format. If you're using an Amazon Linux 2 Docker platform version, you
can use the authentication file that the **docker login** command creates without any conversion.

For improved performance on Amazon Linux AMI, Elastic Beanstalk configures two Amazon EBS storage volumes for your Docker environment's Amazon EC2 instances. In addition to the
root volume provisioned for all Elastic Beanstalk environments, a second 12GB volume named `xvdcz` is provisioned for image storage on Docker
environments.

If you need more storage space or increased IOPS for Docker images, you can customize the image storage volume by using the
`BlockDeviceMapping` configuration option in the [aws:autoscaling:launchconfiguration](command-options-general.md#command-options-general-autoscalinglaunchconfiguration "command-options-general.md#command-options-general-autoscalinglaunchconfiguration") namespace.

For example, the following [configuration file](ebextensions.md "ebextensions.md") increases the storage volume's size to 100 GB with 500
provisioned IOPS:

###### Example.ebextensions/blockdevice-xvdcz.config

```
option_settings:
  aws:autoscaling:launchconfiguration:
    BlockDeviceMappings: /dev/xvdcz=:100::io1:500
```

If you use the `BlockDeviceMappings` option to configure additional volumes for your application, you should include a mapping for
`xvdcz` to ensure that it is created. The following example configures two volumes, the image storage volume `xvdcz` with
default settings and an additional 24 GB application volume named `sdh`:

###### Example.ebextensions/blockdevice-sdh.config

```
option_settings:
  aws:autoscaling:launchconfiguration:
    BlockDeviceMappings: /dev/xvdcz=:12:true:gp2,/dev/sdh=:24
```

###### Note

When you change settings in this namespace, Elastic Beanstalk replaces all instances in your environment with instances running the new configuration. See
[Configuration changes](environments-updating.md "environments-updating.md") for details.
