# Workload architecture

| CONTAINER_BUILD_REL_02: How do you handle persistent data in a<br>container application? |
| ---------------------------------------------------------------------------------------- |
|                                                                                          |

**Use volumes to persist
data**

There are times when workloads have to store data across multiple containers. For example, an image-processing application that saves images for processing. Given the ephemeral nature of a container workload, data on the container will be lost once the container is restarted and longer exists.

Use mounted volumes, whether block or network file system (NFS), to persist file data for an application. Mounted volumes allow for file data sharing among multiple running containers. In addition, mounted volumes should be used to persist logs or configuration files.

For persisting data, use external database such as Amazon Relational Database Service (Amazon RDS), Amazon DynamoDB, or Amazon Aurora. Use a database system that provides performance, high-availability, and scalability to your container application when persisting data.

| CONTAINER_BUILD_REL_03: How do you automate building and<br>testing of containers? |
| ---------------------------------------------------------------------------------- |
|                                                                                    |

**Create local testing
processes**

When building a containerized application, you want to be able
to test your application as early as possible. That means that
you have to think about how developers will be able to test
their containerized application locally. First you will have
to decide whether the container build for local testing will
run on the developer’s machine or in a remote machine, because
this will have an impact on the tooling that developers use on
their machines. Second, you will have to provide a local
deployment mechanism. For this, you can use single containers
that run as part of an automation script or deploy the
containers locally using a local version of your target
orchestrator. This can be also part of the testing section of
your local build-script. With this approach, you can deploy
necessary infrastructure components like databases in a
lightweight fashion in order to test your application with the
real infrastructure instead of mocked APIs. One example might
be a Docker Compose manifest to deploy multiple containers in
a single command. For Kubernetes, use minikube to deploy the
containerized application and all of its objects (such as
Deployment, ConfigMaps, and Secrets).

**Design your testing
environments to support your container build
pipeline**

When building a containerized application, it can be easily
deployed throughout multiple environments. In order to
validate that your application is running properly, you will
have to test your containerized applications. With the
container’s ecosystem, you can have multiple manifests for all
of the applications in an environment, and you can easily
provision a ready-to-use environment with all dependent
services already deployed in it. This process of temporary, or
ephemeral testing environments, can be achieved in lower
effort given the ease of reproducing fully configured
environments that are based on containers. Whether you’re
using the GitOps methodology for a Kubernetes based
application, or a centralized deployment configuration, you
should try to create reproducible environments to support
testing of your containerized application.
