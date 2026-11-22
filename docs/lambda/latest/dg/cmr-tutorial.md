

# Tutorial: Creating and using a customer-managed runtime

In this tutorial, you use the AWS CLI to create a customer-managed runtime and use the runtime in a Lambda Event Function. You then update the runtime and see the update reach the function without any change to the function code.

You act in both runtime roles. As the *runtime publisher*, you build a runtime image, create a runtime, create a runtime version, and create a runtime alias. As the *runtime consumer*, you create a function that uses the runtime through the alias. For more information about the two roles, see [Runtime publishers and runtime consumers](runtimes-customer-managed.md#runtimes-customer-managed-roles).

The runtime image in this tutorial starts from the Lambda base image for Python 3.14 and adds a small text file, called a *marker file*. The function reads the marker file and returns the file contents. The response shows which runtime version the function used.

In this tutorial, you complete the following tasks:
+ Build a runtime image and push the image to Amazon Elastic Container Registry (Amazon ECR)
+ Create a runtime, a runtime version, and a runtime alias
+ Create and invoke a function that uses the runtime alias
+ Roll out a runtime update by pointing the alias to a new runtime version

**Time to complete** – About 30 minutes.

**Cost to complete** – There's no additional charge for customer-managed runtimes. Standard Lambda charges apply to function invocations, and standard Amazon ECR storage charges apply to the runtime images. The invocations in this tutorial are likely to fall within the AWS Free Tier. To avoid ongoing charges, complete the steps in [Clean up your resources](#cmr-tutorial-cleanup). For more information, see [Pricing](runtimes-customer-managed.md#runtimes-customer-managed-pricing).

## Prerequisites
<a name="cmr-tutorial-prereqs"></a>

Before you start, make sure that you have the following:
+ The AWS CLI version 2.40.3 or later, configured with credentials for your AWS account. To check your version, run `aws --version`. To install or update the AWS CLI, see [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.
+ The [Docker CLI](https://docs.docker.com/get-docker), or a compatible tool such as Podman. The commands in this tutorial use Docker.
+ A Bash shell and the **zip** command. On Windows, you can use Windows Subsystem for Linux (WSL).
+ IAM permissions to create and delete runtimes, runtime versions, and runtime aliases. To create a runtime version, you also need `ecr:BatchGetImage` and `ecr:GetDownloadUrlForLayer` on the Amazon ECR repository that contains the image. For the full list of IAM actions, see [IAM actions](cmr-permissions.md#cmr-permissions-actions).
+ IAM permissions to use the runtime alias in a function, including `lambda:AssociateRuntimeAlias`. For more information, see [Before you begin](cmr-using.md#cmr-using-before).
+ Permissions to create and delete Amazon ECR repositories, IAM roles, and Lambda functions.

In this tutorial, the runtime and the function are in the same account. An identity-based policy is enough to use the runtime. To share a runtime with other accounts, see [Sharing and controlling access to customer-managed runtimes](cmr-permissions.md).

## Set up your shell
<a name="cmr-tutorial-setup"></a>

The commands in this tutorial use shell variables for your account ID, your AWS Region, and your Amazon ECR repository URI. Set the variables before you start, and run every command in the same shell session.

**To set up your shell**

1. Create a working directory for the tutorial files, and change to the directory.

   ```bash
   mkdir cmr-tutorial && cd cmr-tutorial
   ```

1. Set the shell variables. Replace `123456789012` with your account ID, and `us-east-1` with the Region that you want to use.

   ```bash
   export ACCOUNT_ID={{123456789012}}
   export AWS_REGION={{us-east-1}}
   export REPO_URI=${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/my-runtime
   ```

   The AWS CLI sends requests to the Region in the `AWS_REGION` environment variable. The runtime, the Amazon ECR repository, and the function must all be in the same Region.

## Step 1: Create an execution role
<a name="cmr-tutorial-create-role"></a>

Every function needs an execution role that grants the function permission to access AWS resources. The function that you create later in this tutorial uses the role. Create the role first, because a new role can take a few seconds to become available.

The role in this tutorial allows the function to write logs to Amazon CloudWatch Logs. For more information, see [Defining Lambda Event Function permissions with an execution role](lambda-intro-execution-role.md).

**To create an execution role**

1. Create a file named `trust-policy.json` with the following content. The trust policy allows Lambda to assume the role.

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "Service": "lambda.amazonaws.com"
         },
         "Action": "sts:AssumeRole"
       }
     ]
   }
   ```

1. To create a role named `cmr-tutorial-role`, run the `create-role` command.

   ```bash
   aws iam create-role \
     --role-name cmr-tutorial-role \
     --assume-role-policy-document file://trust-policy.json
   ```

1. To allow the function to write logs, attach the `AWSLambdaBasicExecutionRole` managed policy to the role.

   ```bash
   aws iam attach-role-policy \
     --role-name cmr-tutorial-role \
     --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
   ```

## Step 2: Create a runtime
<a name="cmr-tutorial-create-runtime"></a>

A runtime is the top-level resource for a customer-managed runtime. Functions refer to the runtime by its ARN. The runtime is the parent of the runtime versions and runtime aliases that you create later. For more information, see [Creating a runtime](cmr-create.md).

**To create a runtime**

1. To create a runtime named `my-runtime`, run the `create-runtime` command.

   ```bash
   aws lambda-core create-runtime \
     --name my-runtime \
     --description "Tutorial runtime based on the Python 3.14 base image" \
     --license-info "None"
   ```

   Runtime names can contain only lowercase letters, numbers, hyphens, underscores, and periods. You should see output similar to the following:

   ```json
   {
       "Arn": "arn:aws:lambda:us-east-1:123456789012:runtime/my-runtime",
       "Name": "my-runtime",
       "Description": "Tutorial runtime based on the Python 3.14 base image",
       "LicenseInfo": "None",
       "Created": "2026-10-08T09:00:00.000Z",
       "LastModified": "2026-10-08T09:00:00.000Z"
   }
   ```

1. To save the runtime ARN in a shell variable for later steps, run the `get-runtime` command.

   ```bash
   export RUNTIME_ARN=$(aws lambda-core get-runtime \
     --runtime-name my-runtime \
     --query Arn \
     --output text)
   echo ${RUNTIME_ARN}
   ```

   You should see output similar to the following:

   ```bash
   arn:aws:lambda:us-east-1:123456789012:runtime/my-runtime
   ```

Functions can't use the runtime yet. First, the runtime needs a version and an alias.

## Step 3: Build a runtime image
<a name="cmr-tutorial-build-image"></a>

A container image defines the contents of each runtime version. The image contains the operating system and the language runtime. The image also contains the runtime interface client, which runs your function code. In this step, you start from the Lambda base image for Python 3.14 and add the marker file. For more information, see [Building a runtime image from a Lambda base image](cmr-base-images.md) and [Building runtime images](cmr-building-images.md).

**To build a runtime image**

1. Create a file named `Dockerfile` with the following content:

   ```dockerfile
   FROM public.ecr.aws/lambda/python:3.14-x86_64
   RUN echo "Customer-managed runtime - Version 1" > /var/runtime/runtime-info.txt
   ```

   The `FROM` line uses the x86\_64 variant of the base image. The `RUN` line writes the marker file to `/var/runtime`, which holds the runtime code and libraries.

1. To build the image, run the `docker build` command.

   ```bash
   docker build --platform linux/amd64 --tag ${REPO_URI}:v1 .
   ```

   The `--platform linux/amd64` option builds an x86\_64 image on any computer. The tag `v1` identifies the first image. This tutorial uses x86\_64 because the function in this tutorial uses x86\_64, and a runtime version supports only the architectures that its image includes. To build for arm64 instead, use the `python:3.14-arm64` base image and `--platform linux/arm64`, and create the function with `--architectures arm64`. For more information about multi-architecture images, see [Architectures](cmr-building-images.md#cmr-building-images-architectures).

## Step 4: Push the runtime image to Amazon ECR
<a name="cmr-tutorial-push-image"></a>

Lambda reads runtime images from an Amazon ECR repository in the same Region as the runtime. In this step, you create a repository, allow Lambda to read from the repository, and push the image. For more information, see [Amazon ECR requirements](cmr-versions.md#cmr-publish-versions-ecr).

**To push the runtime image to Amazon ECR**

1. To create a repository named `my-runtime`, run the `create-repository` command.

   ```bash
   aws ecr create-repository --repository-name my-runtime
   ```

   The output includes the `repositoryUri`, which matches the value of `REPO_URI`.

1. Create a file named `ecr-policy.json` with the following content. The repository policy allows the Lambda service principal to read images from the repository.

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "LambdaReadAccess",
         "Effect": "Allow",
         "Principal": {
           "Service": "lambda.amazonaws.com"
         },
         "Action": [
           "ecr:BatchGetImage",
           "ecr:DescribeImages",
           "ecr:GetDownloadUrlForLayer"
         ]
       }
     ]
   }
   ```

1. To apply the policy to the repository, run the `set-repository-policy` command.

   ```bash
   aws ecr set-repository-policy \
     --repository-name my-runtime \
     --policy-text file://ecr-policy.json
   ```

1. To authenticate Docker to your Amazon ECR registry, run the following command.

   ```bash
   aws ecr get-login-password | docker login \
     --username AWS \
     --password-stdin ${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com
   ```

   You should see the message `Login Succeeded`.

1. To upload the image, run the `docker push` command.

   ```bash
   docker push ${REPO_URI}:v1
   ```

## Step 5: Create a runtime version
<a name="cmr-tutorial-create-version"></a>

A runtime version points to one container image in Amazon ECR. Runtime versions are immutable. To change the runtime contents later, you create a new runtime version. For more information, see [Runtime versions](cmr-versions.md).

**To create a runtime version**

1. To create a runtime version named `v1` from the image, run the `create-runtime-version` command.

   ```bash
   aws lambda-core create-runtime-version \
     --runtime-name my-runtime \
     --name v1 \
     --image-uri ${REPO_URI}:v1
   ```

   You should see output similar to the following. Lambda resolves the image tag to a digest and reads the architecture from the image.

   ```json
   {
       "Name": "v1",
       "Arn": "arn:aws:lambda:us-east-1:123456789012:runtime/my-runtime/version/v1",
       "ResolvedUri": "123456789012.dkr.ecr.us-east-1.amazonaws.com/my-runtime@sha256:4f6a8c0e2b4d6f8a0c2e4b6d8f0a2c4e6b8d0f2a4c6e8b0d2f4a6c8e0b2d4f6a",
       "State": "CREATING",
       "Platforms": [
           {
               "Architecture": "amd64",
               "Os": "linux",
               "Digest": "sha256:4f6a8c0e2b4d6f8a0c2e4b6d8f0a2c4e6b8d0f2a4c6e8b0d2f4a6c8e0b2d4f6a"
           }
       ],
       "Compatibility": {
           "IntegrationModels": [
               "RuntimeAPI"
           ],
           "Architectures": [
               "x86_64"
           ],
           "ManagedInstances": "NotSupported"
       },
       "Created": "2026-10-08T09:10:00.000Z",
       "LastModified": "2026-10-08T09:10:00.000Z"
   }
   ```

1. The runtime version starts in the `CREATING` state while Lambda processes the image. To wait until the runtime version is ready, run the following command.

   ```bash
   aws lambda-core wait runtime-version-active --runtime-name my-runtime --name v1
   ```

   If the runtime version's state is `FAILED`, the command returns an error. For more information, see [If the version fails](cmr-versions.md#cmr-publish-versions-troubleshoot).

## Step 6: Create a runtime alias
<a name="cmr-tutorial-create-alias"></a>

A runtime alias is a named pointer to one runtime version. Functions use a runtime through an alias. When you point the alias to a new runtime version, functions that use the alias move to the new version without a function update. For more information, see [Runtime aliases](cmr-aliases.md).

**To create a runtime alias**

1. To create an alias named `prod` that points to runtime version `v1`, run the `create-runtime-alias` command.

   ```bash
   aws lambda-core create-runtime-alias \
     --runtime-name my-runtime \
     --name prod \
     --runtime-version v1
   ```

   The alias takes its compatibility from the runtime version that it points to. You can't set compatibility on the alias directly.

   The following example shows an excerpt of the output:

   ```json
   {
       "Name": "prod",
       "Arn": "arn:aws:lambda:us-east-1:123456789012:runtime/my-runtime/alias/prod",
       "RuntimeVersion": "v1",
       "RuntimeVersionArn": "arn:aws:lambda:us-east-1:123456789012:runtime/my-runtime/version/v1",
       "State": "CREATING"
   }
   ```

1. To wait until the alias is ready, run the following command.

   ```bash
   aws lambda-core wait runtime-alias-active --runtime-name my-runtime --name prod
   ```

## Step 7: Create a function that uses the runtime
<a name="cmr-tutorial-create-function"></a>

Now you switch to the runtime consumer role. To use a customer-managed runtime, set the function runtime to `custom`, and specify the runtime ARN and the alias name. You deploy the function code as a .zip file archive, the same as for a Lambda-managed runtime. For more information, see [Using a customer-managed runtime](cmr-using.md).

**To create a function that uses the runtime**

1. Create a file named `lambda_function.py` with the following content. The handler reads the marker file from the runtime and returns the file contents.

   ```python
   def lambda_handler(event, context):
       with open("/var/runtime/runtime-info.txt") as runtime_info:
           content = runtime_info.read()
       return {"statusCode": 200, "body": content}
   ```

1. To package the function code, create a .zip file archive.

   ```bash
   zip function.zip lambda_function.py
   ```

1. To create the function, run the `create-function` command. For `--role`, use the ARN of the `cmr-tutorial-role` execution role that you created in [Step 1: Create an execution role](#cmr-tutorial-create-role).

   ```bash
   aws lambda create-function \
     --function-name my-cmr-function \
     --runtime custom \
     --runtime-config RuntimeArn=${RUNTIME_ARN},RuntimeAlias=prod \
     --handler lambda_function.lambda_handler \
     --zip-file fileb://function.zip \
     --role arn:aws:iam::${ACCOUNT_ID}:role/cmr-tutorial-role \
     --architectures x86_64
   ```

   The function must use an architecture that the runtime version supports. The runtime image in this tutorial supports x86\_64 only.

   The following example shows an excerpt of the output:

   ```json
   {
       "FunctionName": "my-cmr-function",
       "FunctionArn": "arn:aws:lambda:us-east-1:123456789012:function:my-cmr-function",
       "Runtime": "custom",
       "RuntimeConfig": {
           "RuntimeArn": "arn:aws:lambda:us-east-1:123456789012:runtime/my-runtime",
           "RuntimeAlias": "prod"
       },
       "Handler": "lambda_function.lambda_handler",
       "Architectures": [
           "x86_64"
       ],
       "State": "Pending"
   }
   ```
**Note**  
If you created the role in the last few seconds, the command might fail with the error `The role defined for the function cannot be assumed by Lambda`. Wait about 10 seconds and run the command again.

1. To wait until the function is ready to invoke, run the following command.

   ```bash
   aws lambda wait function-active-v2 --function-name my-cmr-function
   ```

The function uses the **Auto** runtime update mode by default. In **Auto** mode, Lambda resolves the alias to a runtime version each time Lambda creates a new execution environment for the function. For more information, see [Controlling runtime updates](cmr-using.md#cmr-using-controls).

## Step 8: Invoke the function
<a name="cmr-tutorial-invoke"></a>

Invoke the function to confirm that the function runs on your runtime.

**To invoke the function**

1. To invoke the function and save the response to a file, run the `invoke` command.

   ```bash
   aws lambda invoke --function-name my-cmr-function response.json
   ```

   You should see the following output:

   ```json
   {
       "StatusCode": 200,
       "ExecutedVersion": "$LATEST"
   }
   ```

1. To view the function response, display the contents of `response.json`.

   ```bash
   cat response.json
   ```

   You should see the following output:

   ```json
   {"statusCode": 200, "body": "Customer-managed runtime - Version 1\n"}
   ```

   The response contains the marker file from runtime version `v1`. The marker file confirms that the function used your customer-managed runtime.

1. (Optional) To check which runtime version the function uses, run the `get-function-configuration` command.

   ```bash
   aws lambda get-function-configuration \
     --function-name my-cmr-function \
     --query RuntimeVersionConfig
   ```

   You should see output similar to the following:

   ```json
   {
       "RuntimeVersionArn": "arn:aws:lambda:us-east-1:123456789012:runtime/my-runtime/version/v1"
   }
   ```

   For other ways to check the runtime version, see [Check which runtime version your function uses](cmr-using.md#cmr-using-check-version).

## Step 9: Update the runtime image
<a name="cmr-tutorial-update-image"></a>

In steps 9 through 12, you return to the runtime publisher role and publish an update to the runtime. You then roll out the update through the runtime alias. With a customer-managed runtime, you can update the runtime for many functions at once. You don't need to update each function. To roll out an update, you build a new image, create a new runtime version, and point the alias to the new version. In this tutorial, the update changes the marker file. For more information, see [Deploying runtime updates](cmr-deploy-updates.md).

Each runtime update starts with a new container image. Use a new image tag for each build, so that each runtime version refers to a different image.

**To build and push an updated runtime image**

1. Replace the contents of `Dockerfile` with the following content:

   ```dockerfile
   FROM public.ecr.aws/lambda/python:3.14-x86_64
   RUN echo "Customer-managed runtime - Version 2 (updated)" > /var/runtime/runtime-info.txt
   ```

1. To build the updated image with the tag `v2`, run the `docker build` command.

   ```bash
   docker build --platform linux/amd64 --tag ${REPO_URI}:v2 .
   ```

1. To upload the updated image, run the `docker push` command.

   ```bash
   docker push ${REPO_URI}:v2
   ```

   If the push fails with an authentication error, run the `docker login` command from [Step 4: Push the runtime image to Amazon ECR](#cmr-tutorial-push-image) again.

## Step 10: Create a runtime version for the update
<a name="cmr-tutorial-update-version"></a>

Create runtime version `v2` from the updated image. No function uses the new runtime version until you point an alias to the version.

**To create a new runtime version**

1. To create runtime version `v2`, run the `create-runtime-version` command.

   ```bash
   aws lambda-core create-runtime-version \
     --runtime-name my-runtime \
     --name v2 \
     --image-uri ${REPO_URI}:v2
   ```

1. To wait until the new runtime version is ready, run the following command.

   ```bash
   aws lambda-core wait runtime-version-active --runtime-name my-runtime --name v2
   ```

   If the runtime version's state is `FAILED`, the command returns an error. For more information, see [If the version fails](cmr-versions.md#cmr-publish-versions-troubleshoot).

## Step 11: Update the runtime alias to the new version
<a name="cmr-tutorial-update-alias"></a>

Point the `prod` alias to runtime version `v2`. Functions that use the alias in **Auto** mode start to use `v2` at their next cold start. You don't need to update the functions. For more information, see [Update an alias to roll out a runtime update](cmr-aliases.md#cmr-aliases-update).

**To update the runtime alias**

1. To point the alias to runtime version `v2`, run the `update-runtime-alias` command.

   ```bash
   aws lambda-core update-runtime-alias \
     --runtime-name my-runtime \
     --name prod \
     --runtime-version v2
   ```

   The following example shows an excerpt of the output. The alias is in the `UPDATING` state until Lambda finishes the update.

   ```json
   {
       "Name": "prod",
       "Arn": "arn:aws:lambda:us-east-1:123456789012:runtime/my-runtime/alias/prod",
       "RuntimeVersion": "v2",
       "RuntimeVersionArn": "arn:aws:lambda:us-east-1:123456789012:runtime/my-runtime/version/v2",
       "State": "UPDATING"
   }
   ```

1. To wait until the alias update is complete, run the following command.

   ```bash
   aws lambda-core wait runtime-alias-active --runtime-name my-runtime --name prod
   ```

1. To confirm that the alias points to runtime version `v2`, run the `get-runtime-alias` command.

   ```bash
   aws lambda-core get-runtime-alias \
     --runtime-name my-runtime \
     --name prod \
     --query "[State, RuntimeVersion]"
   ```

   The output shows `ACTIVE` and `v2`:

   ```json
   [
       "ACTIVE",
       "v2"
   ]
   ```

## Step 12: Invoke the function with the updated runtime
<a name="cmr-tutorial-update-invoke"></a>

Execution environments that are already running keep the previous runtime version until Lambda replaces them. If you invoke the function right away, the response might still show `Version 1`. New execution environments use runtime version `v2`.

In production, Lambda replaces execution environments over time. The update reaches functions gradually. In this tutorial, you change an environment variable on the function so that Lambda starts new execution environments right away. The change affects only when the update appears. The function picks up `v2` through the alias, not through the function update.

**To invoke the function with the updated runtime**

1. To start new execution environments, add an environment variable to the function.

   ```bash
   aws lambda update-function-configuration \
     --function-name my-cmr-function \
     --environment "Variables={TUTORIAL_STEP=update}"
   ```

1. To wait until the update is complete, run the following command.

   ```bash
   aws lambda wait function-updated-v2 --function-name my-cmr-function
   ```

1. To invoke the function, run the `invoke` command.

   ```bash
   aws lambda invoke --function-name my-cmr-function response.json
   ```

1. To view the function response, display the contents of `response.json`.

   ```bash
   cat response.json
   ```

   You should see the following output:

   ```json
   {"statusCode": 200, "body": "Customer-managed runtime - Version 2 (updated)\n"}
   ```

   The response contains the marker file from runtime version `v2`. You didn't change the function code or the function's runtime configuration.

To roll back a runtime update, point the alias back to the previous runtime version. For more information, see [Roll back a runtime update](cmr-aliases.md#cmr-aliases-rollback).

## Clean up your resources
<a name="cmr-tutorial-cleanup"></a>

To avoid ongoing charges, delete the resources that you created in this tutorial. Delete the runtime resources in order: the alias, then the runtime versions, then the runtime.

Lambda doesn't delete runtime resources immediately. Instead, Lambda schedules each resource for deletion after a waiting period. During the waiting period, you can restore the resource. The following commands use the minimum waiting period of 7 days. For more information, see [Deleting and restoring runtimes](cmr-delete.md).

**To clean up your resources**

1. To delete the function, run the `delete-function` command.

   ```bash
   aws lambda delete-function --function-name my-cmr-function
   ```

1. To delete the runtime alias, run the `delete-runtime-alias` command.

   ```bash
   aws lambda-core delete-runtime-alias \
     --runtime-name my-runtime \
     --name prod \
     --recovery-window-in-days 7
   ```

1. To delete both runtime versions, run the `delete-runtime-version` command for each version.

   ```bash
   aws lambda-core delete-runtime-version \
     --runtime-name my-runtime \
     --name v1 \
     --recovery-window-in-days 7
   aws lambda-core delete-runtime-version \
     --runtime-name my-runtime \
     --name v2 \
     --recovery-window-in-days 7
   ```

1. To delete the runtime, run the `delete-runtime` command.

   ```bash
   aws lambda-core delete-runtime \
     --runtime-name my-runtime \
     --recovery-window-in-days 7
   ```

   You can delete the runtime after the runtime's alias and versions are scheduled for deletion.

1. (Optional) To confirm that the runtime is scheduled for deletion, run the `get-runtime` command.

   ```bash
   aws lambda-core get-runtime --runtime-name my-runtime --query State
   ```

   The output is `"PENDING_DELETION"`.

1. To delete the Amazon ECR repository and both images, run the `delete-repository` command.

   ```bash
   aws ecr delete-repository --repository-name my-runtime --force
   ```

   A restored runtime version needs the original image. If you might restore the runtime versions, keep the repository until Lambda permanently deletes the versions. For more information, see [Container images and charges](cmr-delete.md#cmr-delete-ecr).

1. To detach the managed policy from the execution role, run the `detach-role-policy` command.

   ```bash
   aws iam detach-role-policy \
     --role-name cmr-tutorial-role \
     --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
   ```

1. To delete the execution role, run the `delete-role` command.

   ```bash
   aws iam delete-role --role-name cmr-tutorial-role
   ```

1. Lambda created a log group named `/aws/lambda/my-cmr-function` in Amazon CloudWatch Logs. To delete the log group, run the `delete-log-group` command.

   Before you run the command, wait at least 1 minute after the last invocation so that Lambda finishes sending log events. Otherwise, Lambda might create the log group again.

   ```bash
   aws logs delete-log-group --log-group-name /aws/lambda/my-cmr-function
   ```

1. (Optional) To remove the runtime images from your computer, run the `docker rmi` command. The `docker build` command stored a copy of each image locally, and deleting the Amazon ECR repository doesn't remove them.

   ```bash
   docker rmi ${REPO_URI}:v1 ${REPO_URI}:v2
   ```

**Note**  
Runtimes, runtime versions, and runtime aliases that are scheduled for deletion keep their names and count toward your quotas until Lambda permanently deletes them. To run this tutorial again before then, restore the runtime resources or use different names. For more information, see [Restoring a runtime, runtime version, or runtime alias](cmr-delete.md#cmr-delete-restore) and [Customer-managed runtimes](gettingstarted-limits.md#cmr-quotas) in [Lambda quotas](gettingstarted-limits.md).

## Next steps
<a name="cmr-tutorial-next-steps"></a>

To learn more, see the following topics:
+ To learn what to put in a runtime image, see [Building runtime images](cmr-building-images.md).
+ To write your own runtime interface client, see [Tutorial: Creating a Bash runtime](runtimes-walkthrough.md).
+ To learn how to roll out runtime updates safely, see [Deploying runtime updates](cmr-deploy-updates.md).
+ To learn how runtime consumers set up their functions, see [Using a customer-managed runtime](cmr-using.md).
+ To share a runtime with other accounts, see [Sharing and controlling access to customer-managed runtimes](cmr-permissions.md).