# Preparing your Docker image for deployment to Elastic Beanstalk

This section describes how to prepare your Docker image for deployment to Elastic Beanstalk with either of the _Docker running
AL2 or AL2023_ platform branches. The configuration files that you'll require depend on whether your images are local, remote, and if
you're using Docker Compose.

###### Note

For an example of a procedure that launches a Docker environment see the [QuickStart for Docker](docker-quickstart.md "docker-quickstart.md")
topic.

###### Topics

- [Managing your images with Docker Compose in Elastic Beanstalk](#single-container-docker-configuration-dc "#single-container-docker-configuration-dc")
- [Managing images without Docker Compose in Elastic Beanstalk](#single-container-docker-configuration.no-compose "#single-container-docker-configuration.no-compose")
- [Building custom images with a Dockerfile](#single-container-docker-configuration.dockerfile "#single-container-docker-configuration.dockerfile")

## Managing your images with Docker Compose in Elastic Beanstalk

You may choose to use Docker Compose to manage various services in one YAML file. To learn more about Docker Compose see [Why use Compose?](https://docs.docker.com/compose/intro/features-uses/ "https://docs.docker.com/compose/intro/features-uses/") on the Docker website.

- Create a `docker-compose.yml`. This file is required if you're using Docker Compose to manage your application with Elastic Beanstalk.
  If all your deployments are sourced from images in public repositories, then no other configuration files are required.
  If your deployment's source images are in a private repository, you'll need to do some additional configuration. For more information, see [Using images from a private repository](docker-configuration.md "docker-configuration.md"). For more information about the `docker-compose.yml` file, see [Compose file reference](https://docs.docker.com/compose/compose-file/ "https://docs.docker.com/compose/compose-file/") on the Docker website.
- The `Dockerfile` is optional. Create one if you need Elastic Beanstalk to build and run a local custom image. For more information about the `Dockerfile` see [Dockerfile
  reference](https://docs.docker.com/engine/reference/builder/ "https://docs.docker.com/engine/reference/builder/") on the Docker website.
- You may need to create a `.zip` file. If you use only a `Dockerfile` file to deploy your application, you don't need to create one. If you use additional configuration files the .zip file must include the `Dockerfile`, the `docker-compose.yml` file, your application files, and any application file dependencies.
  The `Dockerfile` and the `docker-compose.yml` must be at the root, or top level, of the .zip archive.
  If you use the EB CLI to deploy your application, it creates a .zip file for you.

To learn more about Docker Compose and how to install it, see the Docker sites [Overview of Docker
Compose](https://docs.docker.com/compose/ "https://docs.docker.com/compose/") and [Install Docker Compose](https://docs.docker.com/compose/install/ "https://docs.docker.com/compose/install/").

## Managing images without Docker Compose in Elastic Beanstalk

If you're not using Docker Compose to manage your Docker images, you'll need to configure a `Dockerfile`, a `Dockerrun.aws.json`
file, or both.

- Create a `Dockerfile` to have Elastic Beanstalk build and run a custom image locally.
- Create a `Dockerrun.aws.json v1` file to deploy a Docker image from a hosted repository to Elastic Beanstalk.
- You may need to create a `.zip` file. If you use _only one_ of either file, the `Dockerfile` or the
  `Dockerrun.aws.json`, then you don't need to create a .zip file. If you use both files, then you do need a .zip file. The .zip file
  must include both the `Dockerfile` and the `Dockerrun.aws.json`, along with the file containing your application files
  plus any application file dependencies. If you use the EB CLI to deploy your application, it creates a `.zip` file for you.

### `Dockerrun.aws.json` v1 configuration file

A `Dockerrun.aws.json` file describes how to deploy a remote Docker image as an Elastic Beanstalk application. This JSON file is specific to Elastic Beanstalk. If
your application runs on an image that is available in a hosted repository, you can specify the image in a `Dockerrun.aws.json v1` file
and omit the `Dockerfile`.

###### Dockerrun.aws.json versions

The `AWSEBDockerrunVersion` parameter indicates the version of the `Dockerrun.aws.json` file.

- The Docker AL2 and AL2023 platforms use the following versions of the file.
  - `Dockerrun.aws.json v3` — environments that use Docker Compose.

  - `Dockerrun.aws.json v1` — environments that do not use Docker Compose.

- _ECS running on Amazon Linux 2_ and _ECS running on AL2023_ uses the
  `Dockerrun.aws.json v2` file. The retired platform _ECS-The Multicontainer Docker Amazon Linux AMI (AL1)_ also used this
  same version.

Valid keys and values for the `Dockerrun.aws.json v1` file include the following operations:

**AWSEBDockerrunVersion**

(Required) Specify the version number `1` if you're not using Docker Compose to manage your image.

**Authentication**

(Required only for private repositories) Specifies the Amazon S3 object storing the `.dockercfg` file.

See [Authenticating with image repositories](docker-configuration.md#docker-configuration.remote-repo.dockerrun-aws "docker-configuration.md#docker-configuration.remote-repo.dockerrun-aws")
in _Using images from a private repository_ later in this chapter.

**Image**

Specifies the Docker base image on an existing Docker repository from which you're building a Docker container. Specify the value of the
**Name** key in the format `<organization>/<image name>` for images on
Docker Hub, or `<site>/<organization name>/<image name>` for other sites.

When you specify an image in the `Dockerrun.aws.json` file, each instance in your Elastic Beanstalk environment runs `docker pull`
to run the image. Optionally, include the **Update** key. The default value is `true` and instructs
Elastic Beanstalk to check the repository, pull any updates to the image, and overwrite any cached images.

When using a `Dockerfile`, do not specify the **Image** key in the `Dockerrun.aws.json`
file. Elastic Beanstalk always builds and uses the image described in the `Dockerfile` when one is present.

**Ports**

(Required when you specify the **Image** key) Lists the ports to expose on the Docker container. Elastic Beanstalk uses the
**ContainerPort** value to connect the Docker container to the reverse proxy running on the host.

You can specify multiple container ports, but Elastic Beanstalk uses only the first port. It uses this port to connect your container to the host's
reverse proxy and route requests from the public internet. If you're using a `Dockerfile`, the first **ContainerPort** value should match the first entry in the `Dockerfile`'s **EXPOSE** list.

Optionally, you can specify a list of ports in **HostPort**. **HostPort** entries
specify the host ports that **ContainerPort** values are mapped to. If you don't specify a **HostPort** value, it defaults to the **ContainerPort** value.

```
{
  "Image": {
    "Name": "`image-name`"
  },
  "Ports": [
    {
      "ContainerPort": `8080`,
      "HostPort": `8000`
    }
  ]
}

```

\***\*Volumes\*\***

Map volumes from an EC2 instance to your Docker container. Specify one or more arrays of volumes to map.

```
{
  "Volumes": [
    {
      "HostDirectory": "`/path/inside/host`",
      "ContainerDirectory": "`/path/inside/container`"
    }
  ]
...
```

\***\*Logging\*\***

Specify the directory inside the container to which your application writes logs. Elastic Beanstalk uploads any logs in this directory to Amazon S3 when you
request tail or bundle logs. If you rotate logs to a folder named `rotated` within this directory, you can also configure
Elastic Beanstalk to upload rotated logs to Amazon S3 for permanent storage. For more information, see [Viewing logs from Amazon EC2 instances in your Elastic Beanstalk environment](using-features.md "using-features.md").

**Command**

Specify a command to run in the container. If you specify an **Entrypoint**, then **Command** is added as an argument to **Entrypoint**. For more information, see [CMD](https://docs.docker.com/engine/reference/run/#cmd-default-command-or-options "https://docs.docker.com/engine/reference/run/#cmd-default-command-or-options") in the Docker documentation.

**Entrypoint**

Specify a default command to run when the container starts. For more information, see [ENTRYPOINT](https://docs.docker.com/engine/reference/run/#cmd-default-command-or-options "https://docs.docker.com/engine/reference/run/#cmd-default-command-or-options") in the Docker documentation.

The following snippet is an example that illustrates the syntax of the `Dockerrun.aws.json` file for a single container.

```
{
  "AWSEBDockerrunVersion": "1",
  "Image": {
    "Name": "janedoe/image",
    "Update": "true"
  },
  "Ports": [
    {
      "ContainerPort": "1234"
    }
  ],
  "Volumes": [
    {
      "HostDirectory": "/var/app/mydb",
      "ContainerDirectory": "/etc/mysql"
    }
  ],
  "Logging": "/var/log/nginx",
  "Entrypoint": "/app/bin/myapp",
  "Command": "--argument"
}>
```

You can provide Elastic Beanstalk with only the `Dockerrun.aws.json` file, or with a `.zip` archive containing both the
`Dockerrun.aws.json` and `Dockerfile` files. When you provide both files, the `Dockerfile` describes the Docker
image and the `Dockerrun.aws.json` file provides additional information for deployment, as described later in this section.

###### Note

The two files must be at the root, or top level, of the `.zip` archive. Don't build the archive from a directory containing the
files. Instead, navigate into that directory and build the archive there.

When you provide both files, don't specify an image in the `Dockerrun.aws.json` file. Elastic Beanstalk builds and uses the image described in the
`Dockerfile` and ignores the image specified in the `Dockerrun.aws.json` file.

## Building custom images with a Dockerfile

You need to create a `Dockerfile` if you don't already have an existing image hosted in a repository.

The following snippet is an example of the `Dockerfile`. If you follow the instructions in [QuickStart for Docker](docker-quickstart.md "docker-quickstart.md"), you can upload this `Dockerfile` as written. Elastic Beanstalk runs the game
2048 when you use this `Dockerfile`.

For more information about instructions you can include in the `Dockerfile`, see [Dockerfile reference](https://docs.docker.com/engine/reference/builder "https://docs.docker.com/engine/reference/builder") on the Docker website.

```
FROM ubuntu:12.04

RUN apt-get update
RUN apt-get install -y nginx zip curl

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN curl -o /usr/share/nginx/www/master.zip -L https://codeload.github.com/gabrielecirulli/2048/zip/master
RUN cd /usr/share/nginx/www/ && unzip master.zip && mv 2048-master/* . && rm -rf 2048-master master.zip

EXPOSE 80

CMD ["/usr/sbin/nginx", "-c", "/etc/nginx/nginx.conf"]
```

###### Note

You can run multi-stage builds from a single Dockerfile to produce smaller-sized images with a significant reduction in complexity. For more
information, see [Use multi-stage builds](https://docs.docker.com/develop/develop-images/multistage-build/ "https://docs.docker.com/develop/develop-images/multistage-build/") on the Docker documentation
website.
