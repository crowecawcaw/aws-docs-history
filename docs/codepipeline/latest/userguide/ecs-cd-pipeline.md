# Tutorial: Amazon ECS Standard Deployment with CodePipeline

This tutorial helps you to create a complete, end-to-end continuous deployment (CD)
pipeline with Amazon ECS with CodePipeline.

###### Important

As part of creating a pipeline in the console, an S3 artifact bucket will be used by CodePipeline
for artifacts. (This is different from the bucket used for an S3 source action.) If the S3
artifact bucket is in a different account from the account for your pipeline, make sure that
the S3 artifact bucket is owned by AWS accounts that are safe and will be dependable.

###### Note

This tutorial is for the Amazon ECS standard deployment action for CodePipeline. For a tutorial
that uses the Amazon ECS to CodeDeploy blue/green deployment action in CodePipeline, see [Tutorial: Create a pipeline with an Amazon ECR
source and ECS-to-CodeDeploy deployment](tutorials-ecs-ecr-codedeploy.md "tutorials-ecs-ecr-codedeploy.md").

###### Note

This tutorial is for the Amazon ECS standard deployment action for CodePipeline with a source
action. For a tutorial that uses the Amazon ECSstandard deployment action along with the
ECRBuildAndPublish build action in CodePipeline to push your image, see [Tutorial: Build and push a Docker image to
Amazon ECR with CodePipeline (V2 type)](tutorials-ecr-build-publish.md "tutorials-ecr-build-publish.md").

## Prerequisites

There are a few resources that you must have in place before you can use this tutorial
to create your CD pipeline. Here are the things you need to get started:

###### Note

All of these resources should be created within the same AWS Region.

- A source control repository (this tutorial uses CodeCommit) with your Dockerfile
  and application source. For more information, see [Create a CodeCommit
  Repository](../../../codecommit/latest/userguide/how-to-create-repository.md "../../../codecommit/latest/userguide/how-to-create-repository.md") in the _AWS CodeCommit User Guide_.
- A Docker image repository (this tutorial uses Amazon ECR) that contains an image
  you have built from your Dockerfile and application source. For more
  information, see [Creating a
  Repository](../../../AmazonECR/latest/userguide/repository-create.md "../../../AmazonECR/latest/userguide/repository-create.md") and [Pushing an Image](../../../AmazonECR/latest/userguide/docker-push-ecr-image.md "../../../AmazonECR/latest/userguide/docker-push-ecr-image.md") in the
  _Amazon Elastic Container Registry User Guide_.
- An Amazon ECS task definition that references the Docker image hosted in your image
  repository. For more information, see [Creating a Task
  Definition](../../../AmazonECS/latest/developerguide/create-task-definition.md "../../../AmazonECS/latest/developerguide/create-task-definition.md") in the _Amazon Elastic Container Service Developer Guide_.

###### Important

The Amazon ECS standard deployment action for CodePipeline creates its own revision of
the task definition based on the the revision used by the Amazon ECS service. If
you create new revisions for the task definition without updating the Amazon ECS
service, the deployment action will ignore those revisions.

Below is a sample task definition used for this tutorial. The value you use
for `name` and `family` will be used in the next step for
your build specification file.

```
{
  "ipcMode": null,
  "executionRoleArn": "`role_ARN`",
  "containerDefinitions": [
    {
      "dnsSearchDomains": null,
      "environmentFiles": null,
      "logConfiguration": {
        "logDriver": "awslogs",
        "secretOptions": null,
        "options": {
          "awslogs-group": "/ecs/`hello-world`",
          "awslogs-region": "us-west-2",
          "awslogs-stream-prefix": "ecs"
        }
      },
      "entryPoint": null,
      "portMappings": [
        {
          "hostPort": 80,
          "protocol": "tcp",
          "containerPort": 80
        }
      ],
      "command": null,
      "linuxParameters": null,
      "cpu": 0,
      "environment": [],
      "resourceRequirements": null,
      "ulimits": null,
      "dnsServers": null,
      "mountPoints": [],
      "workingDirectory": null,
      "secrets": null,
      "dockerSecurityOptions": null,
      "memory": null,
      "memoryReservation": 128,
      "volumesFrom": [],
      "stopTimeout": null,
      "image": "`image_name`",
      "startTimeout": null,
      "firelensConfiguration": null,
      "dependsOn": null,
      "disableNetworking": null,
      "interactive": null,
      "healthCheck": null,
      "essential": true,
      "links": null,
      "hostname": null,
      "extraHosts": null,
      "pseudoTerminal": null,
      "user": null,
      "readonlyRootFilesystem": null,
      "dockerLabels": null,
      "systemControls": null,
      "privileged": null,
      "name": "`hello-world`"
    }
  ],
  "placementConstraints": [],
  "memory": "2048",
  "taskRoleArn": null,
  "compatibilities": [
    "EC2",
    "FARGATE"
  ],
  "taskDefinitionArn": "`ARN`",
  "family": "`hello-world`",
  "requiresAttributes": [],
  "pidMode": null,
  "requiresCompatibilities": [
    "FARGATE"
  ],
  "networkMode": "awsvpc",
  "cpu": "1024",
  "revision": 1,
  "status": "ACTIVE",
  "inferenceAccelerators": null,
  "proxyConfiguration": null,
  "volumes": []
}
```

- An Amazon ECS cluster that is running a service that uses your previously mentioned
  task definition. For more information, see [Creating a Cluster](../../../AmazonECS/latest/developerguide/clusters.md "../../../AmazonECS/latest/developerguide/clusters.md") and [Creating a Service](../../../AmazonECS/latest/developerguide/create-service-console-v2.md "../../../AmazonECS/latest/developerguide/create-service-console-v2.md") in the
  _Amazon Elastic Container Service Developer Guide_.

After you have satisfied these prerequisites, you can proceed with the tutorial and
create your CD pipeline.

## Step 1: Add a Build Specification File to Your Source

Repository

This tutorial uses CodeBuild to build your Docker image and push the image to Amazon ECR. Add a
`buildspec.yml` file to your source code repository to tell CodeBuild
how to do that. The example build specification below does the following:

- Pre-build stage:
  - Log in to Amazon ECR.
  - Set the repository URI to your ECR image and add an image tag with the
    first seven characters of the Git commit ID of the source.

- Build stage:
  - Build the Docker image and tag the image both as `latest`
    and with the Git commit ID.

- Post-build stage:
  - Push the image to your ECR repository with both tags.
  - Write a file called `imagedefinitions.json` in the
    build root that has your Amazon ECS service's container name and the image
    and tag. The deployment stage of your CD pipeline uses this information
    to create a new revision of your service's task definition, and then it
    updates the service to use the new task definition. The
    `imagedefinitions.json` file is required for the
    ECS job worker.

Paste this sample text to create your `buildspec.yml` file, and
replace the values for your image and task definition. This text uses the example
account ID 111122223333.

```
version: 0.2

phases:
  pre_build:
    commands:
      - echo Logging in to Amazon ECR...
      - aws --version
      - aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin 111122223333.dkr.ecr.us-west-2.amazonaws.com
      - REPOSITORY_URI=012345678910.dkr.ecr.us-west-2.amazonaws.com/hello-world
      - COMMIT_HASH=$(echo $CODEBUILD_RESOLVED_SOURCE_VERSION | cut -c 1-7)
      - IMAGE_TAG=${COMMIT_HASH:=latest}
  build:
    commands:
      - echo Build started on `date`
      - echo Building the Docker image...
      - docker build -t $REPOSITORY_URI:latest .
      - docker tag $REPOSITORY_URI:latest $REPOSITORY_URI:$IMAGE_TAG
  post_build:
    commands:
      - echo Build completed on `date`
      - echo Pushing the Docker images...
      - docker push $REPOSITORY_URI:latest
      - docker push $REPOSITORY_URI:$IMAGE_TAG
      - echo Writing image definitions file...
      - printf '[{"name":"hello-world","imageUri":"%s"}]' $REPOSITORY_URI:$IMAGE_TAG > imagedefinitions.json
artifacts:
    files: imagedefinitions.json
```

The build specification was written for the sample task definition that was provided
in [Prerequisites](#ecs-cd-prereqs "#ecs-cd-prereqs"), used by the Amazon ECS
service for this tutorial. The `REPOSITORY_URI` value corresponds to the
`image` repository (without any image tag), and the
`hello-world` value near the end of the
file corresponds to the container name in the service's task definition.

###### To add a `buildspec.yml` file to your source

repository

1. Open a text editor and then copy and paste the build specification above into
   a new file.
2. Replace the `REPOSITORY_URI` value
   (`012345678910.dkr.ecr.us-west-2.amazonaws.com/hello-world`)
   with your Amazon ECR repository URI (without any image tag) for your Docker image.
   Replace `hello-world` with the container
   name in your service's task definition that references your Docker image.
3. Commit and push your `buildspec.yml` file to your source
   repository.
   1. Add the file.

   ```
   `git add .`
   ```

   2. Commit the change.

   ```
   `git commit -m "Adding build specification."`
   ```

   3. Push the commit.

   ```
   `git push`
   ```

## Step 2: Creating Your Continuous Deployment

Pipeline

Use the CodePipeline wizard to create your pipeline stages and connect your source repository
to your ECS service.

###### To create your pipeline

1. Open the CodePipeline console at
   [https://console.aws.amazon.com/codepipeline/](https://console.aws.amazon.com/codepipeline/ "https://console.aws.amazon.com/codepipeline/").
2. On the **Welcome** page, choose **Create
   pipeline**.

If this is your first time using CodePipeline, an introductory page appears instead
of **Welcome**. Choose **Get Started
Now**. 3. On the **Step 1: Choose creation option** page, under
**Creation options**, choose the **Build custom
pipeline** option. Choose **Next**. 4. In **Step 2: Choose pipeline settings**, in
**Pipeline name**, type the name for your pipeline. For
this tutorial, the pipeline name is **hello-world**. 5. In **Pipeline type**, keep the default selection at
**V2**. Pipeline types differ in characteristics and price.
For more information, see [Pipeline types](pipeline-types.md "pipeline-types.md"). Choose **Next**. 6. On the **Step 3: Add source stage** page, for
**Source provider**, choose **AWS CodeCommit**.

    1. For **Repository name**, choose the name of the CodeCommit
     repository to use as the source location for your pipeline.
    2. For **Branch name**, choose the branch to use and
     choose **Next**.

7. On the **Step 4: Add build stage** page, for **Build
   provider** choose **AWS CodeBuild**, and then choose
   **Create project**.
   1. For **Project name**, choose a unique name for your
      build project. For this tutorial, the project name is
      **hello-world**.
   2. For **Environment image**, choose **Managed
      image**.
   3. For **Operating system**, choose **Amazon
      Linux 2**.
   4. For **Runtime(s)**, choose
      **Standard**.
   5. For **Image**, choose
      **`aws/codebuild/amazonlinux2-x86_64-standard:3.0`**.
   6. For **Image version** and **Environment
      type**, use the default values.
   7. Select **Enable this flag if you want to build Docker images
      or want your builds to get elevated privileges**.
   8. Deselect **CloudWatch logs**. You might need to
      expand **Advanced**.
   9. Choose **Continue to CodePipeline**.
   10. Choose **Next**.

   ###### Note

   The wizard creates a CodeBuild service role for your build project,
   called
   **codebuild-`build-project-name`-service-role**.
   Note this role name, as you add Amazon ECR permissions to it
   later.

8. On the **Step 5: Add deploy stage** page, for
   **Deployment provider**, choose
   **Amazon ECS**.
   1. For **Cluster name**, choose the Amazon ECS cluster in
      which your service is running. For this tutorial, the cluster is
      **default**.
   2. For **Service name**, choose the service to update
      and choose **Next**. For this tutorial, the service
      name is **hello-world**.

9. On the **Step 6: Review** page, review your pipeline
   configuration and choose **Create pipeline** to create the
   pipeline.

###### Note

Now that the pipeline has been created, it attempts to run through the
different pipeline stages. However, the default CodeBuild role created by the
wizard does not have permissions to execute all of the commands contained in
the `buildspec.yml` file, so the build stage fails. The
next section adds the permissions for the build stage.

## Step 3: Add Amazon ECR Permissions to the CodeBuild

Role

The CodePipeline wizard created an IAM role for the CodeBuild build project, called
**codebuild-`build-project-name`-service-role**.
For this tutorial, the name is **codebuild-hello-world-service-role**.
Because the `buildspec.yml` file makes calls to Amazon ECR API operations,
the role must have a policy that allows permissions to make these Amazon ECR calls. The
following procedure helps you attach the proper permissions to the role.

###### To add Amazon ECR permissions to the CodeBuild role

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left navigation pane, choose **Roles**.
3. In the search box, type **codebuild-** and choose the role
   that was created by the CodePipeline wizard. For this tutorial, the role name is
   **codebuild-hello-world-service-role**.
4. On the **Summary** page, choose **Attach
   policies**.
5. Select the box to the left of the
   **AmazonEC2ContainerRegistryPowerUser** policy, and choose
   **Attach policy**.

## Step 4: Test Your Pipeline

Your pipeline should have everything for running an end-to-end native AWS continuous
deployment. Now, test its functionality by pushing a code change to your source
repository.

###### To test your pipeline

1. Make a code change to your configured source repository, commit, and push the
   change.
2. Open the CodePipeline console at
   [https://console.aws.amazon.com/codepipeline/](https://console.aws.amazon.com/codepipeline/ "https://console.aws.amazon.com/codepipeline/").
3. Choose your pipeline from the list.
4. Watch the pipeline progress through its stages. Your pipeline should complete
   and your Amazon ECS service runs the Docker image that was created from your code
   change.
