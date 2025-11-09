# Identity and access management

| CONTAINER_BUILD_SEC_01: How do you ensure that your container<br>images are using least privilege identity? |
| ----------------------------------------------------------------------------------------------------------- |
|                                                                                                             |

By default, containers provide process isolation. This means that processes running inside of a container are isolated from processes and data
that exist in other containers as well as the container host’s operating system. However, it is important to note that the default behavior is to run
the container using the root user when running a container. When the processes inside the container are running as the root user, not only do they have
full administrative access to containers, they also have the same administrative level access to the container host. Having an application running within
a container through the root user expands the attack surface of the environment. This could provide bad actors with the ability to escalate privilege to
the container host infrastructure if the application is compromised.

There are multiple ways to mitigate this risk. The most straightforward method is to define the `USER` directive in the Dockerfile
used to compile the image:

```
FROM amazonlinux:2
RUN yum update -y && yum install -y python python-pip wget
RUN groupadd -r dev && useradd -r -g dev dev
USER dev
...
```

The Dockerfile referenced previously uses a `RUN` command to add the
`dev` user and group to the image and uses the `USER` directive to
ensure that the `dev` user is used when running commands inside of the
container. Therefore, even if the application hosted in this container is compromised, the
attackers would not be able to use the `dev` user within the container
to access other containers or the container host’s operating system.

| CONTAINER_BUILD_SEC_02: How do you control access to your build<br>infrastructure? |
| ---------------------------------------------------------------------------------- |
|                                                                                    |

**Limit administrator access to build infrastructure (CI pipeline)**

Adding continuous security validation in a build pipeline is a major focus for
organizations moving to a DevSecOps strategy. This helps ensure that security is built
into the application from the beginning of the application’s lifecycle as opposed to
performing security testing only at the end of the development process. However, it is
important to note that securing an organization’s build pipeline should be considered a
high priority as well, as the pipeline typically accesses databases, proprietary code, and
secrets or credentials across dev, test, and prod environments. A compromised build
pipeline could provide a bad actor with access to all of the preceding resources in a
customer environment. As detailed in the security pillar of the AWS Well-Architected
Framework, it is important to follow the best practice of granting the least privileged
access to the container build infrastructure. The least privileged best practice should be
applied to human identities as well as machine identities. An example might be that a
human identity that has access to the container build infrastructure can reach an
application’s source code, secrets, and other sensitive data.
