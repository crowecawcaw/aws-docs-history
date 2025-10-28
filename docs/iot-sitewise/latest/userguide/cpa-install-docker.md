# Set up Docker on your

SiteWise Edge gateway

AWS IoT SiteWise provides a Docker image that allows you to run the
SiteWise Edge application on various platforms and environments. This
Docker image encapsulates all the necessary components and
dependencies required to collect, process, and send data from your industrial
equipment to the AWS Cloud. By using the Docker image, you can deploy and run
the SiteWise Edge application on Docker-compatible hosts, such as servers, edge
devices, or cloud-based container services.

To add a partner data source, [Docker Engine](https://docs.docker.com/engine/ "https://docs.docker.com/engine/") 1.9.1 or later must be installed on your local
device.

###### Note

Version 20.10 is the latest version that is verified to work with the
SiteWise Edge gateway software.

## Verify Docker is

installed

To verify Docker is installed, run the following command
from a terminal connected to your SiteWise Edge gateway:

```
docker info
```

If the command returns a `docker is not recognized` result, or
an older version of Docker is installed, [Install Docker
Engine](https://docs.docker.com/engine/install/ "https://docs.docker.com/engine/install/") before continuing.

## Set up Docker

The system user that runs a Docker container component must
have root or administrator permissions, or you must configure
Docker to run it as a non-root or non-admistrator
user.

On Linux devices, you must add a `ggc_user` user to the
`docker` group to call Docker commands without
`sudo`.

To add `ggc_user`, or the non-root user that you use to run
Docker container components, to the `docker`
group, run the following command:

```
sudo usermod -aG docker ggc_user
```

For more information, see [Linux
post-installation steps for DockerEngine](https://docs.docker.com/engine/install/linux-postinstall/ "https://docs.docker.com/engine/install/linux-postinstall/").
