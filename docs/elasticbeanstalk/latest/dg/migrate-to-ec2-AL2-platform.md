# Migrating your Elastic Beanstalk application from ECS managed Multi-container Docker on AL1 to ECS on Amazon Linux 2023

###### Note

On [July 18, 2022](../relnotes/release-2022-07-18-linux-al1-retire.md "../relnotes/release-2022-07-18-linux-al1-retire.md"),
Elastic Beanstalk set the status of all platform branches based on Amazon Linux AMI (AL1) to **retired**..

This topic guides you in the migration of your applications from the retired platform branch _Multi-container Docker running on 64bit
Amazon Linux_ to _ECS Running on 64bit AL2023_. This target platform branch is current and supported. Like the previous
_Multi-container Docker AL1_ branch, the newer _ECS AL2023_ platform branch uses Amazon ECS to coordinate deployment of
multiple Docker containers to an Amazon ECS cluster in an Elastic Beanstalk environment. The new _ECS AL2023_ platform branch supports all of the
features in the previous _Multi-container Docker AL1_ platform branch. Also, the same `Dockerrun.aws.json` v2 file is
supported.

###### Sections

- [Migrate with the Elastic Beanstalk console](#migrate-to-ec2-AL2-platform-steps-console "#migrate-to-ec2-AL2-platform-steps-console")
- [Migrate with the AWS CLI](#migrate-to-ec2-AL2-platform-steps-cli "#migrate-to-ec2-AL2-platform-steps-cli")

## Migrate with the Elastic Beanstalk console

To migrate using the Elastic Beanstalk console deploy the same source code to a new environment that’s based on the _ECS Running on AL2023_
platform branch. No changes to the source code are required.

###### To migrate to the _ECS Running on Amazon Linux 2023_ platform branch

1. Using the application source that's already deployed to the old environment, create an application source bundle. You can use the same application
   source bundle and the same `Dockerrun.aws.json` v2 file.
2. Create a new environment using the _ECS Running on Amazon Linux 2023_ platform branch. Use the source bundle from the prior step for
   **Application code**. For more detailed steps, see [Deploy to Elastic Beanstalk](create_deploy_docker_ecstutorial.md#create_deploy_docker_ecstutorial_deploy "create_deploy_docker_ecstutorial.md#create_deploy_docker_ecstutorial_deploy") in the _ECS managed Docker tutorial_ earlier in this chapter.

## Migrate with the AWS CLI

You also have the option to use the AWS Command Line Interface (AWS CLI) to migrate your existing _Multi-container Docker Amazon Linux Docker_ environment to
the newer _ECS AL2023_ platform branch. In this case you don't need to create a new environment or redeploy your source code. You
only need to run the AWS CLI [update-environment](../../../cli/latest/reference/elasticbeanstalk/update-environment.md "../../../cli/latest/reference/elasticbeanstalk/update-environment.md")
command. It will perform a platform update to migrate your existing environment to the _ECS Amazon Linux 2023_ platform branch.

Use the following syntax to migrate your environment to the new platform branch.

```
aws elasticbeanstalk update-environment \
--environment-name ``my-env`` \
--solution-stack-name `"64bit Amazon Linux 2023 `version` running ECS"` \
--region ``my-region``
```

The following is an example of the command to migrate environment _beta-101_ to _version 3.0.0_ of the
_ECS Amazon Linux 2023_ platform branch in the _us-east-1_ region.

```
aws elasticbeanstalk update-environment \
--environment-name `beta-101` \
--solution-stack-name `"64bit Amazon Linux 2023 v4.0.0 running ECS"` \
--region `us-east-1`
```

The `solution-stack-name` parameter provides the platform branch and its version. Use the most recent platform branch
_version_ by specifying the proper _solution stack name_. The version of every platform branch is included in the
_solution stack name_, as shown in the above example. For a list of the most current solution stacks for the Docker platform, see
[Supported platforms](../platforms/platforms-supported.md#platforms-supported.docker "../platforms/platforms-supported.md#platforms-supported.docker") in
the _AWS Elastic Beanstalk Platforms_ guide.

###### Note

The [list-available-solution-stacks](../../../cli/latest/reference/elasticbeanstalk/list-available-solution-stacks.md "../../../cli/latest/reference/elasticbeanstalk/list-available-solution-stacks.md")
command provides a list of the platform versions available for your account in an AWS Region.

```
aws elasticbeanstalk list-available-solution-stacks --region `us-east-1` --query SolutionStacks
```

To learn more about the AWS CLI, see the [_AWS Command Line Interface User Guide_](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md"). For more information about AWS CLI commands for Elastic Beanstalk, see the [_AWS CLI Command Reference for Elastic Beanstalk_](../../../cli/latest/reference/elasticbeanstalk/index.md "../../../cli/latest/reference/elasticbeanstalk/index.md").
