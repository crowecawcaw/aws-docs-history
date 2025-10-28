This guide provides documentation for Wickr IO Integrations. If you're
using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Host machine and requirements

You should provision a host machine capable of running Docker to deploy the Wickr IO
Docker container. Refer to the [Docker
website](https://docs.docker.com/engine/install/ "https://docs.docker.com/engine/install/") for instructions on how to install Docker on your system. Once the docker is
installed, make sure the docker service is up and running using the `docker info`
command.

While exact requirements may vary based on your deployment scenario, the following
recommendations should be considered as baseline specifications for provisioning the host
system:

## Host OS specifications

The Wickr IO Docker container can be deployed on any Docker capable machine (like Amazon EC2
instances, VMs, etc.). However, since most AWS testing an validation is performed on Ubuntu
20.04 and Amazon Linux, we recommend using either of these operating systems for compatibility and
stability.

The Wickr IO Docker image uses the Ubuntu Linux operating system.

## Host resource specifications

At a minimum the Wickr IO container should have the following resources available when
deploying and running a single bot:

- 4 GB RAM
- 2 CPU
- 8GB+ disk space

###### Note

Increase these resources to ensure availability when running multiple bots or more
intensive local workloads. Make sure to regularly monitor your host's disk space and memory
utilization to avoid disruptions in container performance.

## Networking requirements

Wickr IO bot clients have the same networking requirements as traditional Wickr
clients. The ports and domains needed for basic connectivity are in the AWS Wickr
administration guide. For more information, see [Ports
and domains to allow list](../adminguide/allow-list-ports-domains.md "../adminguide/allow-list-ports-domains.md") for your Wickr network.

Depending on your use case you may have to start the Docker container in a way to allow
access to specific network ports or network proxy settings as well. For example, the Wickr Web
Interface integration requires a TCP port to expose the REST API.

If you plan to use other AWS services with a Wickr bot, you must ensure the host has
the appropriate AWS Identity and Access Management (IAM) role and policy to access them. For more information, see [What is
IAM?](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md").

## Persistent Data

The Wickr IO Docker container will also require access to the host file system in order
to save persistent data. This is necessary to stop or upgrade the image without losing the state
of your Wickr IO clients. You will need to specify this location to the Docker image when you
run it.
