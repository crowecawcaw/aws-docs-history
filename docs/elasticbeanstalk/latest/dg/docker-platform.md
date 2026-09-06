

# Elastic Beanstalk Docker platform branches
<a name="docker-platform"></a>

The Elastic Beanstalk Docker platform supports the following platform branches:

***Docker running Amazon Linux 2*and *Docker running AL2023***  
Elastic Beanstalk deploys Docker container(s) and source code to EC2 instances and manages them. These platform branches offer multi-container support. You can use the Docker Compose tool to simplify your application configuration, testing, and deployment. For more information about this platform branch, see [Using the Elastic Beanstalk Docker platform branch](docker.md).

***ECS running on Amazon Linux 2* and *ECS running on AL2023***  
We provide this branch for customers who need a migration path to AL2023/AL2 from the retired platform branch *Multi-container Docker running on (Amazon Linux AMI)*. The latest platform branches support all of the features from the retired platform branch. No changes to the source code are required. For more information, see [Migrating your Elastic Beanstalk application from ECS managed Multi-container Docker on AL1 to ECS on Amazon Linux 2023](migrate-to-ec2-AL2-platform.md). If you don't have an Elastic Beanstalk environment running on an ECS based platform branch, we recommend you use the platform branch, *Docker Running on 64bit AL2023*. This offers a simpler approach and requires less resources.

For a list of the software component versions associated with each of these platform branches, see [Docker](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html#platforms-supported.docker) in the *AWS Elastic Beanstalk Platforms* document.

## Retired platform branches running on Amazon Linux AMI (AL1)
<a name="al1-platforms"></a>

 On [July 18, 2022](https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2022-07-18-linux-al1-retire.html), Elastic Beanstalk set the status of all platform branches based on Amazon Linux AMI (AL1) to **retired**. Expand each section that follows to read more about each retired platform branch and its migration path to the latest platform branch running on Amazon Linux 2 or Amazon Linux 2023 (recommended).

### Docker (Amazon Linux AMI)
<a name="docker-platform-single"></a>

This platform branch can deploy a Docker image, described in a Dockerfile or a `Dockerrun.aws.json` v1 definition. This platform branch runs *only one* container for each instance. Its succeeding platform branches,*Docker running on 64bit AL2023* and *Docker running on 64bit Amazon Linux 2* support multiple Docker containers per instance.

We recommend that you create your environments with the newer and supported platform branch *Docker running on 64bit AL2023*. You can then migrate your application to the newly created environment. For more information about creating these environments, see [Using the Elastic Beanstalk Docker platform branch](docker.md). For more information about migration, see [Migrating your Elastic Beanstalk Linux application to Amazon Linux 2023 or Amazon Linux 2](using-features.migration-al.md).

### Multi-container Docker (Amazon Linux AMI)
<a name="docker-platform-multi"></a>

This platform branch uses Amazon ECS to coordinate a deployment of multiple Docker containers to an Amazon ECS cluster in an Elastic Beanstalk environment. If you're currently using this retired platform branch, we recommend that you migrate to the latest *ECS Running on Amazon Linux 2023* platform branch. The latest platform branch supports all of the features from this discontinued platform branch. No changes to the source code are required. For more information, see [Migrating your Elastic Beanstalk application from ECS managed Multi-container Docker on AL1 to ECS on Amazon Linux 2023](migrate-to-ec2-AL2-platform.md).

### Preconfigured Docker containers
<a name="docker-platform-preconfigured"></a>

In addition to the prior mentioned Docker platforms, there is also the *Preconfigured Docker GlassFish* platform branch that runs on the Amazon Linux AMI operating system (AL1).

This platform branch has been superseded by the platform branches *Docker running on 64bit AL2023* and *Docker running on 64bit Amazon Linux 2*. For more information, see [Deploying a GlassFish application to the Docker platform](create_deploy_dockerpreconfig.md#docker-glassfish-tutorial).