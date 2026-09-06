

# Migrating your Elastic Beanstalk application from ECS managed Multi-container Docker on AL1 to ECS on Amazon Linux 2023
<a name="migrate-to-ec2-AL2-platform"></a>

**Note**  
On [July 18, 2022](https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2022-07-18-linux-al1-retire.html), Elastic Beanstalk set the status of all platform branches based on Amazon Linux AMI (AL1) to **retired**..

This topic guides you in the migration of your applications from the retired platform branch *Multi-container Docker running on 64bit Amazon Linux* to *ECS Running on 64bit AL2023*. This target platform branch is current and supported. Like the previous *Multi-container Docker AL1* branch, the newer *ECS AL2023* platform branch uses Amazon ECS to coordinate deployment of multiple Docker containers to an Amazon ECS cluster in an Elastic Beanstalk environment. The new *ECS AL2023* platform branch supports all of the features in the previous *Multi-container Docker AL1* platform branch. Also, the same `Dockerrun.aws.json` v2 file is supported.

**Topics**
+ [Migrate with the Elastic Beanstalk console](#migrate-to-ec2-AL2-platform-steps-console)
+ [Migrate with the AWS CLI](#migrate-to-ec2-AL2-platform-steps-cli)

## Migrate with the Elastic Beanstalk console
<a name="migrate-to-ec2-AL2-platform-steps-console"></a>

To migrate using the Elastic Beanstalk console deploy the same source code to a new environment that’s based on the *ECS Running on AL2023* platform branch. No changes to the source code are required. 

**To migrate to the *ECS Running on Amazon Linux 2023* platform branch**

1. Using the application source that's already deployed to the old environment, create an application source bundle. You can use the same application source bundle and the same `Dockerrun.aws.json` v2 file.

1. Create a new environment using the *ECS Running on Amazon Linux 2023* platform branch. Use the source bundle from the prior step for **Application code**. For more detailed steps, see [Deploy to Elastic Beanstalk](create_deploy_docker_ecstutorial.md#create_deploy_docker_ecstutorial_deploy) in the *ECS managed Docker tutorial* earlier in this chapter.

## Migrate with the AWS CLI
<a name="migrate-to-ec2-AL2-platform-steps-cli"></a>

You also have the option to use the AWS Command Line Interface (AWS CLI) to migrate your existing *Multi-container Docker Amazon Linux Docker* environment to the newer *ECS AL2023* platform branch. In this case you don't need to create a new environment or redeploy your source code. You only need to run the AWS CLI [update-environment](https://docs.aws.amazon.com/cli/latest/reference/elasticbeanstalk/update-environment.html) command. It will perform a platform update to migrate your existing environment to the *ECS Amazon Linux 2023* platform branch.

Use the following syntax to migrate your environment to the new platform branch.

```
aws elasticbeanstalk update-environment \
--environment-name {{my-env}} \
--solution-stack-name "64bit Amazon Linux 2023 {{version}} running ECS" \
--region {{my-region}}
```

The following is an example of the command to migrate environment *beta-101* to *version 3.0.0* of the *ECS Amazon Linux 2023* platform branch in the *us-east-1* region. 

```
aws elasticbeanstalk update-environment \
--environment-name beta-101 \
--solution-stack-name "64bit Amazon Linux 2023 v4.0.0 running ECS" \
--region us-east-1
```

The `solution-stack-name` parameter provides the platform branch and its version. Use the most recent platform branch *version* by specifying the proper *solution stack name*. The version of every platform branch is included in the *solution stack name*, as shown in the above example. For a list of the most current solution stacks for the Docker platform, see [Supported platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html#platforms-supported.docker) in the *AWS Elastic Beanstalk Platforms* guide.

**Note**  
 The [list-available-solution-stacks](https://docs.aws.amazon.com/cli/latest/reference/elasticbeanstalk/list-available-solution-stacks.html) command provides a list of the platform versions available for your account in an AWS Region.  

```
aws elasticbeanstalk list-available-solution-stacks --region us-east-1 --query SolutionStacks
```

To learn more about the AWS CLI, see the [*AWS Command Line Interface User Guide*](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html). For more information about AWS CLI commands for Elastic Beanstalk, see the [*AWS CLI Command Reference for Elastic Beanstalk*](https://docs.aws.amazon.com/cli/latest/reference/elasticbeanstalk/index.html).