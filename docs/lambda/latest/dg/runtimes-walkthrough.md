

# Tutorial: Creating a Bash runtime

In this tutorial, you write a minimal runtime interface client (RIC) in Bash. You build the RIC into a runtime image, and create a customer-managed runtime from the image. Then you create and invoke a Lambda Event Function that uses the runtime.

The tutorial shows how a runtime uses the Lambda runtime API. Use the same approach to add support for a new language. For the requirements that every runtime must meet, see [Supporting a new programming language for AWS Lambda Event Functions](runtimes-custom.md). For the API that the runtime calls, see [Using the Lambda runtime API](runtimes-api.md). For what goes into a runtime image, see [Building runtime images](cmr-building-images.md).

Some steps are the same as in the main customer-managed runtime tutorial. For the basic steps on a Lambda base image, including how to update a runtime, see [Tutorial: Creating and using a customer-managed runtime](cmr-tutorial.md).

**Cost to complete** – There's no additional charge for customer-managed runtimes. Standard Lambda charges apply to function invocations, and standard Amazon ECR storage charges apply to the runtime image. To avoid ongoing charges, complete the steps in [Clean up](#runtimes-walkthrough-cleanup).

## Prerequisites
<a name="runtimes-walkthrough-prereqs"></a>

This tutorial assumes that you have some knowledge of basic Lambda operations and the Lambda console. If you haven't already, follow the instructions in [Create a Lambda function with the console](getting-started.md#getting-started-create-function) to create your first Lambda function.

To complete the following steps, you need the [AWS CLI version 2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html). Commands and the expected output are listed in separate blocks:

```
aws --version
```

You should see the following output:

```
aws-cli/2.13.27 Python/3.11.6 Linux/4.14.328-248.540.amzn2.x86_64 exe/x86_64.amzn.2
```

For long commands, an escape character (`\`) is used to split a command over multiple lines.

On Linux and macOS, use your preferred shell and package manager.

**Note**  
In Windows, some Bash CLI commands that you commonly use with Lambda (such as `zip`) are not supported by the operating system's built-in terminals. To get a Windows-integrated version of Ubuntu and Bash, [install the Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10). Example CLI commands in this guide use Linux formatting. Commands which include inline JSON documents must be reformatted if you are using the Windows CLI. 

You also need the following:
+ The AWS CLI version 2.40.3 or later. To check your version, run `aws --version`. To install or update the AWS CLI, see [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.
+ The [Docker CLI](https://docs.docker.com/get-docker), or a compatible tool such as Podman. The commands in this tutorial use Docker.
+ IAM permissions to create and delete runtimes, runtime versions, and runtime aliases. To create a runtime version, you also need `ecr:BatchGetImage` and `ecr:GetDownloadUrlForLayer` on the Amazon ECR repository that contains the image. For the full list of IAM actions, see [IAM actions](cmr-permissions.md#cmr-permissions-actions).
+ IAM permissions to use the runtime alias in a function, including `lambda:AssociateRuntimeAlias`. For more information, see [Before you begin](cmr-using.md#cmr-using-before).
+ Permissions to create and delete Amazon ECR repositories and Lambda functions.
+ IAM permissions to create and delete the function's execution role, and to pass the role to Lambda: `iam:CreateRole`, `iam:AttachRolePolicy`, `iam:PassRole`, `iam:DetachRolePolicy`, and `iam:DeleteRole`.

## How the Bash runtime works
<a name="runtimes-walkthrough-how"></a>

The runtime in this tutorial has one part: a Bash script named `bootstrap`. The `bootstrap` script is the RIC. The script links the function code to Lambda through the runtime API.

The runtime image starts from the Lambda OS-only base image, `provided:al2023`. The base image's `ENTRYPOINT` is `/lambda-entrypoint.sh`. When Lambda starts an execution environment, `/lambda-entrypoint.sh` sets the `_HANDLER` environment variable to the function's handler. Then `/lambda-entrypoint.sh` runs `/var/runtime/bootstrap`. For more information, see [Choosing an entrypoint](cmr-images-from-scratch.md#cmr-images-from-scratch-entrypoint).

The runtime defines the handler format. The Bash runtime uses the format `{{file}}.{{function}}`. For example, the handler `function.handler` refers to the `handler` function in the `function.sh` file.

The `bootstrap` script does the following:

1. Reads the file name from `_HANDLER`, and loads `$LAMBDA_TASK_ROOT/{{file}}.sh`. Lambda extracts the function code to the directory in `LAMBDA_TASK_ROOT`.

1. Sends a `GET` request to the `/runtime/invocation/next` path to get the next invocation event. The request waits until an event is available. For more information, see [Next invocation](runtimes-api.md#runtimes-api-next).

1. Reads the `Lambda-Runtime-Aws-Request-Id` header and the `Lambda-Runtime-Invocation-Id` header from the response.

1. Calls the handler function with the event data.

1. Sends the handler output in a `POST` request to the `/runtime/invocation/{{AwsRequestId}}/response` path. The request includes the `Lambda-Runtime-Invocation-Id` header with the value from step 3. For more information, see [Invocation response](runtimes-api.md#runtimes-api-response).

1. Returns to step 2 for the next event.

**Note**  
The Bash runtime is a minimal example. The `bootstrap` script doesn't report errors to Lambda, and doesn't provide context information to the handler. A production runtime reports errors with the [Initialization error](runtimes-api.md#runtimes-api-initerror) and [Invocation error](runtimes-api.md#runtimes-api-invokeerror) methods. For all runtime responsibilities, see [Requirements](runtimes-custom.md#runtimes-custom-build).

## Step 1: Create an execution role
<a name="runtimes-walkthrough-role"></a>

The function that you create later in this tutorial needs an execution role. Create the role first, because a new role can take a few seconds to become available.

In this tutorial, you create a role that grants only basic permissions: the `AWSLambdaBasicExecutionRole` managed policy lets the function write logs to Amazon CloudWatch Logs. If your function needs to call other AWS services, add the permissions that it needs to the role, or use a different execution role. For more information, see [Defining Lambda Event Function permissions with an execution role](lambda-intro-execution-role.md).

**To create an execution role**

1. To create a role named `bash-tutorial-role` that Lambda can assume, run the `create-role` command.

   ```bash
   aws iam create-role \
     --role-name bash-tutorial-role \
     --assume-role-policy-document '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Service":"lambda.amazonaws.com"},"Action":"sts:AssumeRole"}]}'
   ```

1. To allow the function to write logs, attach the `AWSLambdaBasicExecutionRole` managed policy to the role.

   ```bash
   aws iam attach-role-policy \
     --role-name bash-tutorial-role \
     --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
   ```

## Step 2: Write the runtime interface client
<a name="runtimes-walkthrough-ric"></a>

Create the `bootstrap` script. In the next step, you install the script at `/var/runtime/bootstrap` in the runtime image.

**To write the runtime interface client**

1. Create a directory for the project, and change to the directory.

   ```bash
   mkdir bash-runtime-tutorial && cd bash-runtime-tutorial
   ```

1. Create a file named `bootstrap` with the following content:

   ```bash
   #!/bin/bash
   
   set -euo pipefail
   
   # Initialization - load function handler
   source $LAMBDA_TASK_ROOT/"$(echo $_HANDLER | cut -d. -f1).sh"
   
   # Processing
   while true
   do
     HEADERS="$(mktemp)"
     # Get an event. The HTTP request will block until one is received
     EVENT_DATA=$(curl -sS -LD "$HEADERS" "http://${AWS_LAMBDA_RUNTIME_API}/2018-06-01/runtime/invocation/next")
   
     # Extract request ID by scraping response headers received above
     REQUEST_ID=$(grep -Fi Lambda-Runtime-Aws-Request-Id "$HEADERS" | tr -d '[:space:]' | cut -d: -f2)
   
     # Extract invocation ID for cross-wiring protection, if present
     INVOCATION_ID=$(grep -Fi Lambda-Runtime-Invocation-Id "$HEADERS" | tr -d '[:space:]' | cut -d: -f2 || true)
   
     # Run the handler function from the script
     RESPONSE=$($(echo "$_HANDLER" | cut -d. -f2) "$EVENT_DATA")
   
     # Send the response, echoing the invocation ID
     curl -sS "http://${AWS_LAMBDA_RUNTIME_API}/2018-06-01/runtime/invocation/$REQUEST_ID/response"  -d "$RESPONSE" \
       ${INVOCATION_ID:+--header "Lambda-Runtime-Invocation-Id: $INVOCATION_ID"}
   
     # Remove the temporary headers file
     rm -f "$HEADERS"
   done
   ```

   The script gets the endpoint of the runtime API from the `AWS_LAMBDA_RUNTIME_API` environment variable. To get the request ID, the script saves the response headers to a temporary file, and then reads the `Lambda-Runtime-Aws-Request-Id` header from the file. After it sends the response, the script deletes the file. The `Lambda-Runtime-Invocation-Id` header might not be present, for example when you test the runtime locally with the runtime interface emulator. In that case, the script continues without it.

## Step 3: Build and push the runtime image
<a name="runtimes-walkthrough-image"></a>

Each runtime version gets its contents from a container image in Amazon Elastic Container Registry (Amazon ECR). The runtime image in this tutorial adds the `bootstrap` script to the OS-only base image. For more information about building runtime images without a Lambda language base image, see [Building runtime images from scratch](cmr-images-from-scratch.md).

**To build the runtime image**

1. Create a file named `Dockerfile` with the following content:

   ```dockerfile
   FROM public.ecr.aws/lambda/provided:al2023
   
   # Install the runtime interface client.
   COPY bootstrap /var/runtime/bootstrap
   RUN chmod 755 /var/runtime/bootstrap
   
   # Keep the inherited ENTRYPOINT, /lambda-entrypoint.sh. Don't set CMD.
   ```

   The runtime image inherits the base image's `ENTRYPOINT`, which runs `/var/runtime/bootstrap`.

1. Set shell variables for your account ID, your AWS Region, and your Amazon ECR repository URI. Replace `123456789012` with your account ID, and `us-east-1` with the Region that you want to use.

   ```bash
   export ACCOUNT_ID={{123456789012}}
   export AWS_REGION={{us-east-1}}
   export REPO_URI=${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/bash-runtime
   ```

   The AWS CLI sends requests to the Region in the `AWS_REGION` environment variable. The runtime, the Amazon ECR repository, and the function must all be in the same Region. Run the remaining commands in the same shell session.

1. To build the runtime image, run the `docker build` command.

   ```bash
   docker build --platform linux/amd64 --tag ${REPO_URI}:v1 .
   ```

   The `--platform linux/amd64` option builds an x86\_64 image on any computer.

Next, create an Amazon ECR repository, allow Lambda to read from the repository, and push the runtime image. For more information, see [Amazon ECR requirements](cmr-versions.md#cmr-publish-versions-ecr).

**To push the runtime image to Amazon ECR**

1. To create a repository named `bash-runtime`, run the `create-repository` command.

   ```bash
   aws ecr create-repository --repository-name bash-runtime
   ```

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
     --repository-name bash-runtime \
     --policy-text file://ecr-policy.json
   ```

1. To authenticate Docker to your Amazon ECR registry, run the following command.

   ```bash
   aws ecr get-login-password | docker login \
     --username AWS \
     --password-stdin ${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com
   ```

   You should see the message `Login Succeeded`.

1. To upload the runtime image, run the `docker push` command.

   ```bash
   docker push ${REPO_URI}:v1
   ```

## Step 4: Create the runtime, runtime version, and alias
<a name="runtimes-walkthrough-cmr"></a>

Functions use a customer-managed runtime through three resources. The runtime is the parent resource. A runtime version points to one runtime image. A runtime alias points to one runtime version. For more information, see [Creating a runtime](cmr-create.md), [Runtime versions](cmr-versions.md), and [Runtime aliases](cmr-aliases.md).

**To create the runtime**

1. To create a runtime named `bash-runtime`, run the `create-runtime` command.

   ```bash
   aws lambda-core create-runtime \
     --name bash-runtime \
     --description "Minimal Bash runtime"
   ```

   You should see output similar to the following:

   ```json
   {
       "Arn": "arn:aws:lambda:us-east-1:123456789012:runtime/bash-runtime",
       "Name": "bash-runtime",
       "Description": "Minimal Bash runtime",
       "LicenseInfo": "",
       "Created": "2026-10-08T09:00:00.000Z",
       "LastModified": "2026-10-08T09:00:00.000Z"
   }
   ```

1. To save the runtime ARN in a shell variable for later steps, run the `get-runtime` command.

   ```bash
   export RUNTIME_ARN=$(aws lambda-core get-runtime \
     --runtime-name bash-runtime \
     --query Arn \
     --output text)
   echo ${RUNTIME_ARN}
   ```

**To create a runtime version**

1. To create a runtime version named `v1` from the runtime image, run the `create-runtime-version` command.

   ```bash
   aws lambda-core create-runtime-version \
     --runtime-name bash-runtime \
     --name v1 \
     --image-uri ${REPO_URI}:v1
   ```

   The following example shows an excerpt of the output. Lambda resolves the image tag to a digest and reads the platform (architecture and OS) from the runtime image.

   ```json
   {
       "Name": "v1",
       "Arn": "arn:aws:lambda:us-east-1:123456789012:runtime/bash-runtime/version/v1",
       "ResolvedUri": "123456789012.dkr.ecr.us-east-1.amazonaws.com/bash-runtime@sha256:0a1afafd0777718289b2301be0926e267ef17bd9440521e141d51364e7a5fbb5",
       "State": "CREATING",
       "Platforms": [
           {
               "Architecture": "amd64",
               "Os": "linux",
               "Digest": "sha256:0a1afafd0777718289b2301be0926e267ef17bd9440521e141d51364e7a5fbb5"
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
       }
   }
   ```

1. To wait until the runtime version is ready, run the following command.

   ```bash
   aws lambda-core wait runtime-version-active --runtime-name bash-runtime --name v1
   ```

   If the runtime version's state is `FAILED`, the command returns an error. For more information, see [If the version fails](cmr-versions.md#cmr-publish-versions-troubleshoot).

**To create a runtime alias**

1. To create an alias named `prod` that points to runtime version `v1`, run the `create-runtime-alias` command.

   ```bash
   aws lambda-core create-runtime-alias \
     --runtime-name bash-runtime \
     --name prod \
     --runtime-version v1
   ```

   The following example shows an excerpt of the output.

   ```json
   {
       "Name": "prod",
       "Arn": "arn:aws:lambda:us-east-1:123456789012:runtime/bash-runtime/alias/prod",
       "RuntimeVersion": "v1",
       "RuntimeVersionArn": "arn:aws:lambda:us-east-1:123456789012:runtime/bash-runtime/version/v1",
       "State": "CREATING"
   }
   ```

1. To wait until the alias is ready, run the following command.

   ```bash
   aws lambda-core wait runtime-alias-active --runtime-name bash-runtime --name prod
   ```

## Step 5: Create and invoke a function
<a name="runtimes-walkthrough-function"></a>

Create a function that uses the Bash runtime. The function's .zip file archive holds only the handler script. The runtime image provides the `bootstrap` script. For more information, see [Using a customer-managed runtime](cmr-using.md).

**To create and invoke a function**

1. Create a file named `function.sh` with the following content. The `handler` function takes the event data, logs the event data to `stderr`, and returns a response.

   ```bash
   function handler () {
     EVENT_DATA=$1
     echo "$EVENT_DATA" 1>&2;
     RESPONSE="Echoing request: '$EVENT_DATA'"
   
     echo $RESPONSE
   }
   ```

1. To make the handler script executable and add the script to a .zip file archive, run the following commands.

   ```bash
   chmod 755 function.sh
   zip function.zip function.sh
   ```

1. To create the function, run the `create-function` command. For `--role`, use the ARN of the `bash-tutorial-role` execution role that you created in [Step 1: Create an execution role](#runtimes-walkthrough-role).

   ```bash
   aws lambda create-function \
     --function-name bash-function \
     --runtime custom \
     --runtime-config RuntimeArn=${RUNTIME_ARN},RuntimeAlias=prod \
     --handler function.handler \
     --zip-file fileb://function.zip \
     --role arn:aws:iam::${ACCOUNT_ID}:role/bash-tutorial-role \
     --architectures x86_64
   ```

   The handler `function.handler` tells the Bash runtime to load `function.sh` and call the `handler` function. The function must use an architecture that the runtime version supports. The runtime image in this tutorial supports x86\_64 only.
**Note**  
If you created the role in the last few seconds, the command might fail with the error `The role defined for the function cannot be assumed by Lambda`. Wait about 10 seconds and run the command again.

1. To wait until the function is ready to invoke, run the following command.

   ```bash
   aws lambda wait function-active-v2 --function-name bash-function
   ```

1. To invoke the function, run the `invoke` command.

   ```bash
   aws lambda invoke \
     --function-name bash-function \
     --payload '{"text":"Hello"}' \
     --cli-binary-format raw-in-base64-out \
     response.txt
   ```

   The **cli-binary-format** option is required if you're using AWS CLI version 2. To make this the default setting, run `aws configure set cli-binary-format raw-in-base64-out`. For more information, see [AWS CLI supported global command line options](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-options.html#cli-configure-options-list) in the *AWS Command Line Interface User Guide for Version 2*.

   You should see the following output:

   ```json
   {
       "StatusCode": 200,
       "ExecutedVersion": "$LATEST"
   }
   ```

1. To view the function response, display the contents of `response.txt`.

   ```bash
   cat response.txt
   ```

   You should see the following output:

   ```text
   Echoing request: '{"text":"Hello"}'
   ```

   The response comes from the `handler` function, through the `bootstrap` script in your customer-managed runtime.

## Clean up
<a name="runtimes-walkthrough-cleanup"></a>

Lambda doesn't charge for storing the runtime, its runtime version and alias, or the function. However, Amazon ECR charges for storing the runtime image. When you finish this tutorial, delete the resources that you created. Delete the runtime resources in order: the alias, then the runtime version, then the runtime.

Lambda doesn't delete runtime resources right away. First, Lambda schedules each resource for deletion. You can restore the resource during the waiting period. The following commands use the minimum waiting period of 7 days. For more information, see [Deleting and restoring runtimes](cmr-delete.md).

**To clean up your resources**

1. To delete the function, run the `delete-function` command.

   ```bash
   aws lambda delete-function --function-name bash-function
   ```

1. To delete the runtime alias, run the `delete-runtime-alias` command.

   ```bash
   aws lambda-core delete-runtime-alias \
     --runtime-name bash-runtime \
     --name prod \
     --recovery-window-in-days 7
   ```

1. To delete the runtime version, run the `delete-runtime-version` command.

   ```bash
   aws lambda-core delete-runtime-version \
     --runtime-name bash-runtime \
     --name v1 \
     --recovery-window-in-days 7
   ```

1. To delete the runtime, run the `delete-runtime` command.

   ```bash
   aws lambda-core delete-runtime \
     --runtime-name bash-runtime \
     --recovery-window-in-days 7
   ```

   You can delete the runtime after the runtime's alias and version are scheduled for deletion.

1. (Optional) To confirm that the runtime is scheduled for deletion, run the `get-runtime` command.

   ```bash
   aws lambda-core get-runtime --runtime-name bash-runtime --query State
   ```

   The output is `"PENDING_DELETION"`.

1. To delete the Amazon ECR repository and the runtime image, run the `delete-repository` command.

   ```bash
   aws ecr delete-repository --repository-name bash-runtime --force
   ```

   A restored runtime version needs the original image. If you might restore the runtime version, keep the repository until Lambda permanently deletes the version. For more information, see [Container images and charges](cmr-delete.md#cmr-delete-ecr).

1. To detach the managed policy from the execution role, run the `detach-role-policy` command.

   ```bash
   aws iam detach-role-policy \
     --role-name bash-tutorial-role \
     --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
   ```

1. To delete the execution role, run the `delete-role` command.

   ```bash
   aws iam delete-role --role-name bash-tutorial-role
   ```

1. Lambda created a log group named `/aws/lambda/bash-function` in Amazon CloudWatch Logs. To delete the log group, run the `delete-log-group` command.

   Before you run the command, wait at least 1 minute after the last invocation so that Lambda finishes sending log events. Otherwise, Lambda might create the log group again.

   ```bash
   aws logs delete-log-group --log-group-name /aws/lambda/bash-function
   ```

1. (Optional) To remove the runtime image from your computer, run the `docker rmi` command. The `docker build` command stored a copy of the image locally, and deleting the Amazon ECR repository doesn't remove it.

   ```bash
   docker rmi ${REPO_URI}:v1
   ```

**Note**  
Runtimes, runtime versions, and runtime aliases that are scheduled for deletion keep their names and count toward your quotas until Lambda permanently deletes them. To run this tutorial again before then, restore the runtime resources or use different names. For more information, see [Restoring a runtime, runtime version, or runtime alias](cmr-delete.md#cmr-delete-restore) and [Customer-managed runtimes](gettingstarted-limits.md#cmr-quotas) in [Lambda quotas](gettingstarted-limits.md).

## Next steps
<a name="runtimes-walkthrough-next-steps"></a>

To learn more, see the following topics:
+ To roll out a runtime update by pointing an alias to a new runtime version, see [Tutorial: Creating and using a customer-managed runtime](cmr-tutorial.md).
+ To learn what to put in a runtime image, see [Building runtime images](cmr-building-images.md).
+ To learn about every method that a runtime can call, see [Using the Lambda runtime API](runtimes-api.md).