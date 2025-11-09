# Development and deployment process

Look for opportunities to reduce your sustainability impact by
making changes to your development, test, and deployment
practices. 

| CONTAINER_BUILD_SUSTAINABILITY_03: How do you design<br>your build tooling and services to improve efficiency of the underlying<br>resources? |
| --------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                               |

**Use dynamically created
build servers for building your containerized
workload**

Using dynamically created build servers (such as
[AWS CodeBuild](https://aws.amazon.com/codebuild/ "https://aws.amazon.com/codebuild/")), ensures that while building your
containerized images, the needed infrastructure is being
provisioned when the build process starts, and being
terminated as soon as the build process ends.

**Use pre-defined or built
runtimes to reduce your build time, and reuse needed
dependencies for the build process**

When building different types of containerized applications,
using common and standardized runtimes for the build process
reduces the operational management of creating and maintaining
custom images. Also, by using the specific type of runtime for
your build server, it verifies that no common dependency is
being downloaded and configured as part of the build process.
All relevant dependencies are being incorporated into the
different runtimes of your build servers, and are being used
many times by different build processes for different
applications. An example of
[multiple
build runtimes](../../../codebuild/latest/userguide/runtime-versions.md "../../../codebuild/latest/userguide/runtime-versions.md") can be found in the AWS CodeBuild
documentation.

**Update your parent and base
image regularly**

Update your base and parent images to the latest versions, as
sometimes there is a performance improvement that is
introduced in newer versions. These improvements are
translated into a sustainability improvement as it affects the
resource consumption of the underlying infrastructure, and as
a result improves the overall efficiency.

**Delete unused or obsolete
container images**

As described in the [Cost Optimization Pillar whitepaper](../cost-optimization-pillar/welcome.md "../cost-optimization-pillar/welcome.md"), create mechanisms to verify that unused or
obsolete container images are deleted. This can be achieved, for example, by registry
[lifecycle
policies](../../../AmazonECR/latest/userguide/lifecycle_policy_examples.md "../../../AmazonECR/latest/userguide/lifecycle_policy_examples.md"), as exists in [Amazon ECR.](https://aws.amazon.com/ecr/ "https://aws.amazon.com/ecr/")
