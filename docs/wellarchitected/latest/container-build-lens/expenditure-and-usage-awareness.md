# Expenditure and usage awareness

| CONTAINER_BUILD_COST_02: How do you design your container<br>build process to avoid unnecessary cost? |
| ----------------------------------------------------------------------------------------------------- |
|                                                                                                       |

**Designing efficient
container build process**

Building containers is a process that consumes compute and
storage resources and can lead to unnecessary costs if not
using it properly. The build process consumes resources for
each build, and there are some considerations that have to be
taken for it to be efficient from a cost perspective.

**Application
dependencies**

The container image is usually being built alongside with the application build step. During this build step, all necessary dependencies, libraries, and modules that are being used by the application code are downloaded to the container image.
Using unnecessary dependencies will make the build time longer, and will result in wasting compute resources of the build system.

**Common container image
dependencies**

Some operating system packages are needed for multiple applications in the
organization for a specific runtime (for example, Python and Java). Building a parent
container image that preinstalls all common operating system packages and dependencies for
the specific runtime will result in a more efficient build process. Without this common
image, each individual container image would be installing the same packages, thus wasting
compute and network resources. This practice will also shorten the time for container
images built from a specific runtime, since all of its common operating system packages
and dependencies are already included in the parent container image. As a result, this
will reduce costs for building all other container images that use this parent image.
