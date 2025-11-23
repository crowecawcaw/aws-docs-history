# Tutorial: Configure a CodeBuild-hosted GitLab

runner

This tutorial shows you how to configure your CodeBuild projects to run GitLab CI/CD pipeline jobs.
For more information about using GitLab or GitLab Self Managed with CodeBuild, see [Self-managed GitLab runners in AWS CodeBuild](gitlab-runner.md "gitlab-runner.md").

To complete this tutorial, you must first:

- Connect with a OAuth app by using CodeConnections. Note that when connecting with an OAuth app, you must
  use the CodeBuild console to do so. For more instructions, see
  [GitLab access in CodeBuild](access-tokens-gitlab-overview.md "access-tokens-gitlab-overview.md").
- Connect CodeBuild to your GitLab account. To do so, you can add GitLab as a source provider
  in the console. For instructions, see [GitLab access in CodeBuild](access-tokens-gitlab-overview.md "access-tokens-gitlab-overview.md").

###### Note

This only needs to be done if you haven't connected to GitLab for your
account.

With this feature, CodeBuild needs additional permissions. such as `create_runner`
and `manage_runner` from the GitLab OAuth app. If there are existing CodeConnections for
a particular GitLab account, then it doesn't automatically request for permission updates.
To do so, you can go to the CodeConnections console and create a dummy connection to the same GitLab account
to trigger the reauthorization to get the additional prmissions. With this, all the existing
connections can use the runner feature. Once complete, you can delete the dummy connection.

## Step 1: Create a CodeBuild

project with a webhook

In this step, you will create a CodeBuild project with a webhook and review it in the
GitLab console.

###### To create a CodeBuild project with a webhook

1. Open the AWS CodeBuild console at [https://console.aws.amazon.com/codesuite/codebuild/home](https://console.aws.amazon.com/codesuite/codebuild/home "https://console.aws.amazon.com/codesuite/codebuild/home").
2. Create a build project. For information, see [Create a build project (console)](create-project.md#create-project-console "create-project.md#create-project-console")
   and [Run a build (console)](run-build-console.md "run-build-console.md").

In **Project type**, choose **Runner
project**.

    * In **Runner**:




    	+ For **Runner provider**, choose
    	 **GitLab**.
    	+ For **Credential**, choose one of the
    	 following:




    		- Choose  **Default source
    		 credential**. Default connection applies a
    		 default GitLab connection across all projects.
    		- Choose  **Custom source credential**.
    		 Custom connection applies a custom GitLab connection
    		 that overrides your account's default settings.
    	###### Note

    	If you have not already created a connection to your
    	 provider, you'll have to create a new GitLab connection. For
    	 instructions, see [Connect CodeBuild to GitLab](access-tokens-gitlab-overview.md#connections-gitlab "access-tokens-gitlab-overview.md#connections-gitlab").
    	+ For **Runner location**, choose
    	 **Repository**.
    	+ For **Repository**, choose the name of your
    	 project in GitLab by specifying the project path with the
    	 namespace.
    * In **Environment**:




    	+ Choose a supported **Environment image** and
    	 **Compute**. Note that you have the option
    	 to override the image and instance settings by using a label in
    	 your GitLab CI/CD pipeline YAML. For more information, see [Step 2: Create a .gitlab-ci.yml file in your repository](#sample-gitlab-runners-gitlab-ci "#sample-gitlab-runners-gitlab-ci").
    * In **Buildspec**:




    	+ Note that your buildspec will be ignored unless
    	 `buildspec-override:true` is added as a label.
    	 Instead, CodeBuild will override it to use commands that will setup
    	 the self-managed runner.


    *

3. Continue with the default values and then choose **Create build
   project**.
4. Open the GitLab console at
   `https://gitlab.com/`user-name`/`repository-name`/-/hooks`
   to verify that a webhook has been created and is enabled to deliver
   **Workflow jobs** events.

## Step 2: Create a .gitlab-ci.yml file in your repository

In this step, you will create a `.gitlab-ci.yml` file in [`GitLab`](https://gitlab.com/ "https://gitlab.com/") to configure your build
environment and use GitLab self-managed runners in CodeBuild. For more information,
see [Use self-managed runners](https://docs.gitlab.com/runner/#use-self-managed-runners "https://docs.gitlab.com/runner/#use-self-managed-runners").

### Update your GitLab CI/CD pipeline YAML

Navigate to `https://gitlab.com/`user-name`/`project-name`/-/tree/`branch-name``
 and create a`.gitlab-ci.yml` file in your repository. You can configure your build environment by doing one of the
following:

- You can specify the CodeBuild project name, in which case the build will
  use your existing project configuration for the compute, image, image
  version, and instance size. The project name is needed to link the
  AWS-related settings of your GitLab job to a specific CodeBuild
  project. By including the project name in the YAML, CodeBuild is allowed to
  invoke jobs with the correct project settings.

```
tags:
    - codebuild-`<codebuild-project-name>`-$CI_PROJECT_ID-$CI_PIPELINE_IID-$CI_JOB_NAME
```

`$CI_PROJECT_ID-$CI_PIPELINE_IID-$CI_JOB_NAME` is required to map the
build to specific pipeline job runs and stop the build when the pipeline run is cancelled.

###### Note

Make sure that your `<project-name>`
matches the name of the project that you created in CodeBuild.
If it doesn't match, CodeBuild will not process the webhook and the GitLab CI/CD pipeline might hang.

The following is an example of a GitLab CI/CD pipeline YAML:

```
workflow:
  name: HelloWorld
stages:          # List of stages for jobs, and their order of execution
  - build

build-job:       # This job runs in the build stage, which runs first.
  stage: build
  script:
    - echo "Hello World!"
  tags:
    - codebuild-myProject-$CI_PROJECT_ID-$CI_PIPELINE_IID-$CI_JOB_NAME
```

- You can also override your image and compute type in the tag. See [Compute images
  supported with the CodeBuild-hosted GitLab runner](sample-gitlab-runners-gitlab-ci.md "sample-gitlab-runners-gitlab-ci.md")
  for a list of curated images. For using custom images, see [Label overrides
  supported with the CodeBuild-hosted GitLab runner](gitlab-runners-update-labels.md "gitlab-runners-update-labels.md").
  The compute type and image in the tag will override
  the environment settings on your project. To override your
  environment settings for an Amazon EC2 compute build, use the following
  syntax:

```
tags:
    - codebuild-`<codebuild-project-name>`-$CI_PROJECT_ID-$CI_PIPELINE_IID-$CI_JOB_NAME
    - image:`<environment-type>`-`<image-identifier>`
    - instance-size:`<instance-size>`
```

The following is an example of a GitLab CI/CD pipeline YAML:

```
stages:
  - build

build-job:
  stage: build
  script:
    - echo "Hello World!"
  tags:
    - codebuild-myProject-$CI_PROJECT_ID-$CI_PIPELINE_IID-$CI_JOB_NAME
    - image:arm-3.0
    - instance-size:small
```

- You can override the fleet used for your build in the tag. This will
  override the fleet settings configured on your project to use the specified
  fleet. For more information, see [Run builds on reserved capacity fleets](fleets.md "fleets.md"). To override your fleet settings for an Amazon EC2
  compute build, use the following syntax:

```
tags:
    - codebuild-`<codebuild-project-name>`-$CI_PROJECT_ID-$CI_PIPELINE_IID-$CI_JOB_NAME
    - fleet:`<fleet-name>`
```

To override both the fleet and the image used for the build, use the
following syntax:

```
tags:
    - codebuild-`<codebuild-project-name>`-$CI_PROJECT_ID-$CI_PIPELINE_IID-$CI_JOB_NAME
    - fleet:`<fleet-name>`
    - image:`<environment-type>`-`<image-identifier>`
```

The following is an example of a GitLab CI/CD pipeline YAML:

```
stages:
  - build

build-job:
  stage: build
  script:
    - echo "Hello World!"
  tags:
    - codebuild-myProject-$CI_PROJECT_ID-$CI_PIPELINE_IID-$CI_JOB_NAME
    - fleet:myFleet
    - image:arm-3.0
```

- In order to run your GitLab CI/CD pipeline jobs on a custom image, you can configure a
  custom image in your CodeBuild project and avoid providing an image override label. CodeBuild
  will use the image configured in the project if no image override label is provided.

After you commit your changes to `.gitlab-ci.yml`, a GitLab
pipeline will be triggered and the `build-job` will send a webhook
notification that will start your build in CodeBuild.

### Run buildspec commands the INSTALL, PRE_BUILD, and POST_BUILD phases

By default, CodeBuild ignores any buildspec commands when running a self-managed GitLab build. To run buildspec
commands during the build, `buildspec-override:true` can be added as a suffix to `tags`:

```
tags:
    - codebuild-`<codebuild-project-name>`-$CI_PROJECT_ID-$CI_PIPELINE_IID-$CI_JOB_NAME
    - buildspec-override:true
```

By using this command, CodeBuild will create a folder called `gitlab-runner` in the container's primary source folder. When
the GitLab runner starts during the `BUILD` phase, the runner will run in the `gitlab-runner` directory.

There are several limitations when using a buildspec override in a self-managed GitLab build:

- CodeBuild will not run buildspec commands during the `BUILD` phase, as the self-managed runner runs in the `BUILD` phase.
- CodeBuild will not download any primary or secondary sources during the `DOWNLOAD_SOURCE` phase. If you have a buildspec file configured,
  only that file will be downloaded from the project's primary source.
- If a build command fails in the `PRE_BUILD` or `INSTALL` phase, CodeBuild will not start the
  self-managed runner and the GitLab CI/CD pipeline job will need to be cancelled manually.
- CodeBuild fetches the runner token during the `DOWNLOAD_SOURCE` phase, which has an expiration time of one hour.
  If your `PRE_BUILD` or `INSTALL` phases exceed an hour, the runner token may expire before the GitLab self-managed runner starts.

## Step 3: Review your

results

Whenever a GitLab CI/CD pipeline run occurs, CodeBuild would receive the CI/CD pipeline job
events through the webhook. For each job in the CI/CD pipeline, CodeBuild starts a build to run an
ephemeral GitLab runner. The runner is responsible for executing a single
CI/CD pipeline job. Once the job is completed, the runner and the associated build process
will be immediately terminated.

To view your CI/CD pipeline job logs, navigate to your repository in GitLab, choose
**Build**, **Jobs**, and then choose the
specific **Job** that you'd like to review the logs for.

You can review the requested labels in the log while the job is waiting to be picked
up by a self-managed runner in CodeBuild.

## Filter GitLab webhook events (CloudFormation)

The following YAML-formatted portion of an CloudFormation
template creates a filter group that triggers a build when it evaluates to true.
The following filter group specifies a GitLab CI/CD pipeline job request with a
CI/CD pipeline name matching the regular expression `\[CI-CodeBuild\]`.

```
CodeBuildProject:
  Type: AWS::CodeBuild::Project
  Properties:
    Name: MyProject
    ServiceRole: service-role
    Artifacts:
      Type: NO_ARTIFACTS
    Environment:
      Type: LINUX_CONTAINER
      ComputeType: BUILD_GENERAL1_SMALL
      Image: aws/codebuild/standard:5.0
    Source:
      Type: GITLAB
      Location: CODEBUILD_DEFAULT_WEBHOOK_SOURCE_LOCATION
    Triggers:
      Webhook: true
      ScopeConfiguration:
        Name: group-name
        Scope: GITLAB_GROUP
      FilterGroups:
        - - Type: EVENT
            Pattern: WORKFLOW_JOB_QUEUED
          - Type: WORKFLOW_NAME
            Pattern: \[CI-CodeBuild\]
```
