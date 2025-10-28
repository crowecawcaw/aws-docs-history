# Elastic Beanstalk Docker platform branches

The Elastic Beanstalk Docker platform supports the following platform branches:

###### _Docker running Amazon Linux 2_ and _Docker running AL2023_

Elastic Beanstalk deploys Docker container(s) and source code to EC2 instances and manages them.
These platform branches offer multi-container support. You can use the Docker Compose tool
to simplify your application configuration, testing, and deployment. For more information
about this platform branch, see [Using the Elastic Beanstalk Docker platform branch](docker.md "docker.md").

###### _ECS running on Amazon Linux 2_ and \*ECS

running on AL2023\*

We provide this branch for customers who need a migration path to
AL2023/AL2 from the retired platform branch _Multi-container Docker
running on (Amazon Linux AMI)_. The latest platform branches support all of the features
from the retired platform branch. No changes to the source code are required. For more
information, see [Migrating your Elastic Beanstalk application from ECS managed Multi-container Docker on AL1 to ECS on Amazon Linux 2023](migrate-to-ec2-AL2-platform.md "migrate-to-ec2-AL2-platform.md"). If you don't have an Elastic Beanstalk environment
running on an ECS based platform branch, we recommend you use the platform branch,
_Docker Running on 64bit AL2023_. This offers a simpler approach and
requires less resources.

For a list of the software component versions associated with each of these platform branches, see
[Docker](../platforms/platforms-supported.md#platforms-supported.docker "../platforms/platforms-supported.md#platforms-supported.docker")
in the _AWS Elastic Beanstalk Platforms_ document.

## Retired platform branches running on Amazon Linux AMI (AL1)

On [July 18, 2022](../relnotes/release-2022-07-18-linux-al1-retire.md "../relnotes/release-2022-07-18-linux-al1-retire.md"),
Elastic Beanstalk set the status of all platform branches based on Amazon Linux AMI (AL1) to **retired**. Expand each section that follows to read
more about each retired platform branch and its migration path to the latest platform branch
running on Amazon Linux 2 or Amazon Linux 2023 (recommended).

This platform branch can deploy a Docker image, described in a Dockerfile or a
`Dockerrun.aws.json` v1 definition. This platform branch runs
_only one_ container for each instance. Its succeeding platform
branches,_Docker running on 64bit AL2023_ and _Docker
running on 64bit Amazon Linux 2_ support multiple Docker containers per
instance.

We recommend that you create your environments with the newer and supported platform
branch _Docker running on 64bit AL2023_. You can then migrate your
application to the newly created environment. For more information about creating these
environments, see [Using the Elastic Beanstalk Docker platform branch](docker.md "docker.md"). For more information about migration, see
[Migrating your Elastic Beanstalk Linux application to Amazon Linux 2023 or Amazon Linux 2](using-features.md "using-features.md").

This platform branch uses Amazon ECS to coordinate a deployment of multiple Docker
containers to an Amazon ECS cluster in an Elastic Beanstalk environment. If you're currently using this
retired platform branch, we recommend that you migrate to the latest _ECS
Running on Amazon Linux 2023_ platform branch. The latest platform branch
supports all of the features from this discontinued platform branch. No changes to the
source code are required. For more information, see [Migrating your Elastic Beanstalk application from ECS managed Multi-container Docker on AL1 to ECS on Amazon Linux 2023](migrate-to-ec2-AL2-platform.md "migrate-to-ec2-AL2-platform.md").

In addition to the prior mentioned Docker platforms, there is also the _Preconfigured Docker GlassFish_ platform branch that runs on
the Amazon Linux AMI operating system (AL1).

This platform branch has been superseded by the platform branches _Docker
running on 64bit AL2023_ and _Docker running on 64bit
Amazon Linux 2_. For more information, see [Deploying a GlassFish application to the Docker platform](create_deploy_dockerpreconfig.md#docker-glassfish-tutorial "create_deploy_dockerpreconfig.md#docker-glassfish-tutorial").
