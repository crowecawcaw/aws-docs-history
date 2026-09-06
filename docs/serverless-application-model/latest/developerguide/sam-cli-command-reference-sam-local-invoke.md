

# sam local invoke
<a name="sam-cli-command-reference-sam-local-invoke"></a>

This page provides reference information for the AWS Serverless Application Model Command Line Interface (AWS SAM CLI) `sam local invoke` subcommand.
+ For an introduction to the AWS SAM CLI, see [What is the AWS SAM CLI?](what-is-sam-overview.md#what-is-sam-cli)
+ For documentation on using the AWS SAM CLI `sam local invoke` subcommand, see [Introduction to testing with sam local invoke](using-sam-cli-local-invoke.md).

The `sam local invoke` subcommand initiates a one-time invocation of an AWS Lambda function locally.

**Note**  
It's not recommended to use SAM CLI's local invoke capabilities in untrusted code. To have complete isolation from your local environment, execute the code in the Lambda service directly.

**Note**  
For durable functions, `sam local invoke` supports stateful execution with automatic checkpointing and replay. The container remains running during durable function execution to handle state persistence and resumption.

## Usage
<a name="ref-sam-cli-local-invoke-usage"></a>

```
$ sam local invoke {{<arguments>}} {{<options>}}
```

**Note**  
If you have more than one function defined in your AWS SAM template, provide the function logical ID that you want to invoke.

## Arguments
<a name="ref-sam-cli-local-invoke-args"></a>

**Resource ID**  <a name="ref-sam-cli-local-invoke-args-resource-id"></a>
The ID of the Lambda function to invoke.  
This argument is optional. If your application contains a single Lambda function, the AWS SAM CLI will invoke it. If your application contains multiple functions, provide the ID of the function to invoke.  
*Valid values*: The resource's logical ID or resource ARN.

## Options
<a name="ref-sam-cli-local-invoke-options"></a>

`--add-host {{LIST}}`  <a name="ref-sam-cli-local-invoke-options-add-host"></a>
Passes a hostname to IP address mapping to the Docker container's host file. This parameter can be passed multiple times.  

**Example**  
Example: `--add-host {{example.com:127.0.0.1}}`

`--beta-features | --no-beta-features`  <a name="ref-sam-cli-local-invoke-options-beta-features"></a>
Allow or deny beta features.

`--config-env {{TEXT}}`  <a name="ref-sam-cli-local-invoke-options-config-env"></a>
The environment name specifying the default parameter values in the configuration file to use. The default value is "default". For more information about configuration files, see [AWS SAM CLI configuration file](serverless-sam-cli-config.md).

`--config-file {{PATH}}`  <a name="ref-sam-cli-local-invoke-options-config-file"></a>
The path and file name of the configuration file containing default parameter values to use. The default value is "`samconfig.toml`" in the root of the project directory. For more information about configuration files, see [AWS SAM CLI configuration file](serverless-sam-cli-config.md).

`--container-env-vars`  <a name="ref-sam-cli-local-invoke-options-container-env-vars"></a>
(Optional) Pass environment variables to the Lambda function image container when debugging locally.

`--container-host {{TEXT}}`  <a name="ref-sam-cli-local-invoke-options-container-host"></a>
Host of locally emulated Lambda container. The default value is `localhost`. If you want to run AWS SAM CLI in a Docker container on macOS, you can specify `host.docker.internal`. If you want to run the container on a different host than AWS SAM CLI, you can specify the IP address of the remote host.

`--container-host-interface {{TEXT}}`  <a name="ref-sam-cli-local-invoke-options-container-host-interface"></a>
The IP address of the host network interface that container ports should bind to. The default value is `127.0.0.1`. Use `0.0.0.0` to bind to all interfaces.

`--container-dns {{TEXT}}`  <a name="ref-sam-cli-local-invoke-options-container-dns"></a>
Specifies a custom DNS server for the Docker container. This parameter can be passed multiple times to specify multiple DNS servers.  

**Example**  
Example: `--container-dns {{8.8.8.8}}`

`--debug`  <a name="ref-sam-cli-local-invoke-options-debug"></a>
Turns on debug logging to print debug messages that the AWS SAM CLI generates, and to display timestamps.

`--debug-args {{TEXT}}`  <a name="ref-sam-cli-local-invoke-options-debug-args"></a>
Additional arguments to pass to the debugger.

`--debug-port, -d {{TEXT}}`  <a name="ref-sam-cli-local-invoke-options-debug-port"></a>
When specified, starts the Lambda function container in debug mode and exposes this port on the local host.

`--debugger-path {{TEXT}}`  <a name="ref-sam-cli-local-invoke-options-debugger-path"></a>
The host path to a debugger that's mounted into the Lambda container.

`--docker-network {{TEXT}}`  <a name="ref-sam-cli-local-invoke-options-docker-network"></a>
The name or ID of an existing Docker network that Lambda Docker containers should connect to, along with the default bridge network. If this isn't specified, the Lambda containers connect only to the default bridge Docker network.

`--docker-volume-basedir, -v {{TEXT}}`  <a name="ref-sam-cli-local-invoke-options-docker-volume-basedir"></a>
The location of the base directory where the AWS SAM file exists. If Docker is running on a remote machine, you must mount the path where the AWS SAM file exists on the Docker machine and modify this value to match the remote machine.

`--durable-execution-name {{TEXT}}`  <a name="ref-sam-cli-local-invoke-options-durable-execution-name"></a>
Name for the durable execution (for durable functions only)

`--env-vars, -n {{PATH}}`  <a name="ref-sam-cli-local-invoke-options-env-vars"></a>
The JSON or `.env` file that contains values for the Lambda function's environment variables. The file format is automatically detected. For more information about environment variable files, see [Environment variable file](serverless-sam-cli-using-invoke.md#serverless-sam-cli-using-invoke-environment-file).

`--event, -e {{PATH}}`  <a name="ref-sam-cli-local-invoke-options-event"></a>
The JSON file that contains event data that's passed to the Lambda function when it's invoked. If you don't specify this option, no event is assumed. To input JSON from `stdin`, you must pass in the value '-'. For details about event message formats from different AWS services, see [Working with other services](https://docs.aws.amazon.com/lambda/latest/dg/lambda-services.html) in the *AWS Lambda Developer Guide*.

`--force-image-build`  <a name="ref-sam-cli-local-invoke-options-force-image-build"></a>
Specifies whether the AWS SAM CLI should rebuild the image used for invoking Lambda functions with layers.

`--help`  <a name="ref-sam-cli-local-invoke-options-help"></a>
Shows this message and exits.

`--hook-name TEXT`  <a name="ref-sam-cli-local-invoke-options-hook-name"></a>
The name of the hook that is used to extend AWS SAM CLI functionality.  
Accepted values: `terraform`.

`--invoke-image {{TEXT}}`  <a name="ref-sam-cli-local-invoke-options-invoke-image"></a>
The URI of the container image that you want to use for the local function invocation.  
For Lambda functions with `PackageType: Zip`, this overrides the runtime base image. By default, AWS SAM pulls the container image from Amazon ECR Public (which are listed in [Image repositories for AWS SAM](serverless-image-repositories.md)). Use this option to pull the image from another location.  
For Lambda functions with `PackageType: Image`, this overrides the `ImageUri` from the built template. Use this to invoke a different application image locally without modifying your template.  
You can specify this option multiple times. Each instance of this option can take either a string or a key-value pair. If you specify a string, it is the URI of the container image to use for all functions in your application. For example, `sam local invoke --invoke-image public.ecr.aws/sam/emu-python3.13`. If you specify a key-value pair, the key is the resource name, and the value is the URI of the container image to use for that resource. For example, `sam local invoke --invoke-image public.ecr.aws/sam/emu-python3.13 --invoke-image Function1=amazon/aws-sam-cli-emulation-image-python3.13`. With key-value pairs, you can specify different container images for different resources.

`--layer-cache-basedir {{DIRECTORY}}`  <a name="ref-sam-cli-local-invoke-options-layer-cache-basedir"></a>
Specifies the location of the base directory where the layers that your template uses are downloaded to.

`--log-file, -l {{TEXT}}`  <a name="ref-sam-cli-local-invoke-options-log-file"></a>
The log file to send runtime logs to.

`--mount-symlinks`  <a name="ref-sam-cli-local-invoke-options-mount-symlinks"></a>
Ensures the AWS SAM CLI always mounts symlinks that are present in the files to build or invoke. This applies only to symlinks on the top level directory (that is, symlinks that are directly on the function's root). By default, symlinks are not mounted except for those needed to use `build-in-source` for `node_modules` in NodeJS.

`--no-event`  <a name="ref-sam-cli-local-invoke-options-no-event"></a>
Invokes the function with an empty event.

`--no-memory-limit`  <a name="ref-sam-cli-local-invoke-options-no-memory-limit"></a>
Removes the memory limitation in the container during local invoke, even when memory is configured in the AWS SAM template.

`--parameter-overrides`  <a name="ref-sam-cli-local-invoke-options-parameter-overrides"></a>
A string that contains CloudFormation parameter overrides encoded as key-value pairs. Use the same format as the AWS Command Line Interface (AWS CLI). The AWS SAM CLI format is explicit key and value keywords, each override is separated by a space. Here are two examples:  
+ `--parameter-overrides ParameterKey=hello,ParameterValue=world`
+ `--parameter-overrides ParameterKey=hello,ParameterValue=world ParameterKey=example1,ParameterValue=example2 ParameterKey=apple,ParameterValue=banana`

`--profile {{TEXT}}`  <a name="ref-sam-cli-local-invoke-options-profile"></a>
The specific profile from your credential file that gets AWS credentials.

`--region {{TEXT}}`  <a name="ref-sam-cli-local-invoke-options-region"></a>
The AWS Region to deploy to. For example, us-east-1.

`--runtime {{TEXT}}`  <a name="ref-sam-cli-local-invoke-options-runtime"></a>
Uses the specified runtime to invoke a Lambda function locally. This overrides the runtime defined in the `template.yml` file. This also allows testing Lambda functions with different runtimes without modifying the original function configuration.

`--save-params`  <a name="ref-sam-cli-local-invoke-options-save-params"></a>
Save the parameters that you provide at the command line to the AWS SAM configuration file.

`--shutdown`  <a name="ref-sam-cli-local-invoke-options-shutdown"></a>
Emulates a shutdown event after the invoke completes, in order to test extension handling of shutdown behavior.

`--skip-prepare-infra`  <a name="ref-sam-cli-local-invoke-options-skip-prepare-infra"></a>
Skips the preparation stage if no infrastructure changes have been made. Use with the `--hook-name` option.

`--skip-pull-image`  <a name="ref-sam-cli-local-invoke-options-skip-pull-image"></a>
By default, the AWS SAM CLI checks Lambda's latest remote runtime environment and updates your local image automatically to keep in sync.  
Specify this option to skip pulling down the latest Docker image for your Lambda runtime environment.

`--template, -t {{PATH}}`  <a name="ref-sam-cli-local-invoke-options-template"></a>
The AWS SAM template file.  
This option is not compatible with `--hook-name`.  
If you specify this option, AWS SAM loads only the template and the local resources that it points to.

`--tenant-id {{TEXT}}`  <a name="ref-sam-cli-local-invoke-options-tenancyconfig"></a>
The tenant ID for multi-tenant Lambda functions. Used to ensure compute isolation between different tenants. Required when invoking functions configured with tenant isolation mode.

`--terraform-plan-file`  <a name="ref-sam-cli-local-invoke-options-terraform-plan-file"></a>
The relative or absolute path to your local Terraform plan file when using the AWS SAM CLI with Terraform Cloud. This option requires that `--hook-name` be set to `terraform`.

## Examples
<a name="sam-cli-command-reference-sam-local-invoke-examples"></a>

The following example uses a generated event for local testing by using an `s3.json` event to invoke a Lambda function locally

```
$ sam local invoke --event {{events/s3.json S3JsonLoggerFunction}}
```

The following example tests the function ` HelloWorldFunction` using Python 3.11 runtime

```
$ sam local invoke --runtime {{python3.11 HelloWorldFunction}}
```

The following example tests the function ` HelloWorldFunction` with durable execution name

```
$ sam local invoke {{HelloWorldFunction --durable-execution-name my-execution}}
```