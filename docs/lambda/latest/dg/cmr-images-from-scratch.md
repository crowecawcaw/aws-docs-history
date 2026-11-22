

# Building runtime images from scratch

To build a runtime image from scratch, you start from a base image that has no language runtime. Then you add a language runtime, one of the open-source Lambda runtime interface clients (RICs), and a bootstrap that starts the runtime. You push the runtime image to Amazon Elastic Container Registry (Amazon ECR), and then publish the runtime image as a runtime version.

Build a runtime image from scratch in the following cases:
+ You need a language version or distribution that no Lambda base image offers. For example, you might need a different minor version, or a build with different compile options.
+ You need an operating system (OS) other than Amazon Linux 2023.
+ You need strict control over every component in the runtime image, for example to meet security or compliance rules.

When you build from scratch, you own more of the runtime image than when you start from a Lambda base image. You choose, install, and patch the language runtime and the RIC. If you use your own base image, you also own and patch the OS libraries. If you only need to add libraries, extensions, or certificates to a language that Lambda supports, start from a Lambda base image instead. For more information, see [Building a runtime image from a Lambda base image](cmr-base-images.md).

To support a language that has no Lambda RIC, you write your own RIC. For more information, see [Supporting a new programming language for AWS Lambda Event Functions](runtimes-custom.md).

This topic covers the implementation steps. For the principles that apply to every runtime image, such as the file system layout and image best practices, see [Building runtime images](cmr-building-images.md).

**Note**  
If you already build container image functions, the Dockerfile for a runtime image looks familiar. However, a runtime image doesn't contain function code or a `CMD`. Functions that use your runtime are .zip file archive functions. For more information about container image functions, see [Create a Lambda Event Function using a container image](images-create.md).

## Choosing a base image
<a name="cmr-images-from-scratch-base-image"></a>

A runtime image that you build from scratch starts from one of the following kinds of base image:
+ **A Lambda OS-only base image** – The [OS-only base image](https://gallery.ecr.aws/lambda/provided), `public.ecr.aws/lambda/provided:al2023`, has no language runtime or RIC. The OS-only base image contains the following:
  + Amazon Linux 2023
  + `/lambda-entrypoint.sh`, which is the image's `ENTRYPOINT`
  + The runtime interface emulator (RIE), for local testing
  + The [environment variables](#cmr-building-images-envvars) that Lambda runtimes need
  + `/var/task` as the working directory

  Lambda patches the OS in the OS-only base image. To get the OS patches, rebuild your runtime image. For more information, see [OS-only runtimes](lambda-runtimes.md#runtimes-provided).
+ **Your own base image** – A base image of your choice, such as an image with a different Linux distribution. You provide every component, including the startup files and environment variables that the OS-only base image provides. You also patch every component. For the environment variables to set, and the variables that Lambda sets for you, see [Setting environment variables in the runtime image](#cmr-building-images-envvars).

We recommend that you start from the Lambda OS-only base image. The OS-only base image already works with the way that Lambda starts the runtime, and Lambda keeps the OS patched.

## The runtime startup contract
<a name="cmr-images-from-scratch-startup"></a>

A runtime image that you build from scratch must start the runtime in the way that Lambda expects. When Lambda sets up an execution environment for a function, Lambda runs the executable that the image's `ENTRYPOINT` specifies. Lambda passes the function's handler to the executable as the last argument. The handler is the `Handler` property in the function configuration. If the `ENTRYPOINT` includes its own arguments, Lambda appends the handler after them. For example, with `ENTRYPOINT ["/var/runtime/bootstrap", "--flag"]`, the bootstrap receives `--flag` and then the handler.

If the image doesn't set an `ENTRYPOINT`, Lambda runs `/var/runtime/bootstrap` with the handler as the argument. If the image sets no `ENTRYPOINT` and includes no `/var/runtime/bootstrap`, invocations fail with the error type `Runtime.InvalidEntrypoint`. Lambda doesn't use the image's `CMD`, so don't put the handler in `ENTRYPOINT` or `CMD`. Lambda places the function code in `/var/task`. For a summary that applies to every runtime image, see [How Lambda starts your runtime](cmr-building-images.md#cmr-building-images-startup).

Lambda doesn't set the `_HANDLER` environment variable for a runtime that you build from scratch. Your runtime must read the handler from the arguments, or set `_HANDLER` itself. The Lambda base images set `_HANDLER` for you because the `/lambda-entrypoint.sh` script copies the handler into the variable.

Your runtime is responsible for the following tasks:
+ During initialization, use the handler to find and load the function code from `/var/task`.
+ For each invocation, call the handler.
+ Use the Lambda runtime API to get events and to send responses and errors. For more information, see [Using the Lambda runtime API](runtimes-api.md).

When you use a Lambda RIC, the RIC does these tasks for you. Your runtime defines the handler format. The handler format typically follows the conventions of the runtime's programming language. For compiled languages, the executable that `ENTRYPOINT` specifies can contain the RIC itself.

### Choosing an entrypoint
<a name="cmr-images-from-scratch-entrypoint"></a>

You can start your runtime in one of the following ways:
+ **Reuse `/lambda-entrypoint.sh`** – If you start from the OS-only base image, keep the inherited `ENTRYPOINT`. The `/lambda-entrypoint.sh` script sets the `_HANDLER` environment variable to the handler, and then runs `/var/runtime/bootstrap`. You provide the bootstrap. Outside Lambda, the script runs the bootstrap under the RIE, so you can test the runtime image locally. For more information, see [How Lambda base images start the runtime](cmr-base-images.md#cmr-building-images-startup-base-images).
+ **Write your own entrypoint** – Set `ENTRYPOINT` to your own executable. The executable receives the handler as the last argument. If neither your base image nor your Dockerfile sets an `ENTRYPOINT`, Lambda runs `/var/runtime/bootstrap`. To test locally, run your entrypoint under the RIE. For more information, see [(Optional) Test your runtime image locally](#cmr-images-from-scratch-test).

We recommend that you reuse `/lambda-entrypoint.sh` when you start from the OS-only base image.

Use the exec form of `ENTRYPOINT`, which is a JSON array, so that Lambda can pass the handler to your runtime. With the shell form, Docker stores the entrypoint as `/bin/sh -c`, and your runtime never receives the handler. The following example shows both forms:

```dockerfile
# Correct: exec form. Lambda passes the handler to the entrypoint.
ENTRYPOINT ["/var/runtime/bootstrap"]

# Wrong: shell form. The runtime never receives the handler.
# ENTRYPOINT /var/runtime/bootstrap
```

### Writing the bootstrap
<a name="cmr-images-from-scratch-bootstrap"></a>

The bootstrap starts the language runtime, and the language runtime runs the RIC. The bootstrap passes the handler to the RIC. A bootstrap is typically a short shell script. When you write the bootstrap, follow these guidelines:
+ Make the bootstrap executable, for example with **chmod 755**.
+ Set the language search paths before the bootstrap starts the language runtime. For more information, see [Adding a language runtime](#cmr-images-from-scratch-language-runtime).
+ Start the language runtime with **exec**. The language runtime process then replaces the shell process.
+ Optionally, support wrapper scripts. If the function sets the `AWS_LAMBDA_EXEC_WRAPPER` environment variable, run the wrapper script, passing the language runtime command and its arguments. For more information, see [Wrapper scripts](runtimes-modify.md#runtime-wrapper).

For an example bootstrap, see [Example: Python runtime from the OS-only base image](#cmr-images-from-scratch-example).

## Adding a language runtime
<a name="cmr-images-from-scratch-language-runtime"></a>

Add the interpreter or virtual machine for your language to the runtime image. Consider the following when you add a language runtime:
+ **Where to install the language runtime** – Lambda base images install the language runtime in `/var/lang`. The default `PATH` and `LD_LIBRARY_PATH` values include `/var/lang/bin` and `/var/lang/lib`. If you install the language runtime from the OS package manager, the package manager chooses the location, such as `/usr/bin`. Don't install the language runtime in `/opt`, `/var/task`, or `/tmp`. For more information, see [File system layout](cmr-building-images.md#cmr-building-images-layout).
+ **Which version to install** – Choose a version that gets security updates for as long as you plan to support the runtime. The end of support for the language version can determine when you deprecate the runtime. For more information, see [Runtime lifecycle](cmr-lifecycle.md).
+ **Language search paths** – Configure the language runtime to find function code in `/var/task`, libraries from layers in `/opt`, and your libraries in `/var/runtime`. For example, set `PYTHONPATH` for Python or `NODE_PATH` for Node.js. Set the search paths in the bootstrap or with the Dockerfile `ENV` instruction.

To match the behavior of Lambda-managed runtimes, use the same search path order. For example, see [Dependency search path and runtime-included libraries](python-package.md#python-package-searchpath) and [Dependency search path and runtime-included libraries](nodejs-package.md#nodejs-package-searchpath).

Lambda base images search function code (`/var/task`) first, then layer paths, and then the runtime's own libraries. For Python, the layer paths are `/opt/python/lib/python{{X.Y}}/site-packages` and `/opt/python`. For Node.js, they're `/opt/nodejs/node{{NN}}/node_modules` and `/opt/nodejs/node_modules`.

## Adding a Lambda runtime interface client
<a name="cmr-images-from-scratch-ric"></a>

The RIC loads the function handler, gets events from Lambda, and sends back responses. Lambda publishes RICs for several languages as open source. For the list of RICs, their packages, and their source code repositories, see [Open-source repositories](runtimes-open-source.md).

Install the RIC in `/var/runtime`, or in another location that the language search path includes. Keep the RIC up to date. New RIC releases can include fixes and support for new Lambda features.

In your bootstrap, pass the handler to the RIC. With `/lambda-entrypoint.sh`, the handler is in the `_HANDLER` environment variable. If you write your own entrypoint, read the handler from the arguments that Lambda passes. For the handler format for each language, see [Programming languages](lambda-programming-languages.md).

## Setting environment variables in the runtime image
<a name="cmr-building-images-envvars"></a>

Your runtime, function code, and layers need environment variables, such as `PATH` and `LAMBDA_TASK_ROOT`, to work as expected. Some variables come from the runtime image, and Lambda sets others when it starts the runtime. You set environment variables in the runtime image with the Dockerfile `ENV` instruction. Your runtime and the function code can read these variables at run time.

**Note**  
If you build from a Lambda base image, including the OS-only base image, the runtime image inherits the environment variables in the following table. You don't need to set them.

If you use your own base image, set the following environment variables:
+ **`PATH`** – Include the directories for your language runtime and tools. Your runtime uses the `PATH` value from the image.
+ **Language-specific variables** – Set any variables that your language runtime needs, such as `PYTHONPATH` for Python or `NODE_PATH` for Node.js. Set them in your bootstrap or with `ENV`. Lambda base images set language-specific search paths in the bootstrap, not with `ENV`. For more information, see [Adding a language runtime](#cmr-images-from-scratch-language-runtime).

When Lambda starts the runtime, it always sets `LAMBDA_TASK_ROOT` and `LAMBDA_RUNTIME_DIR`. It sets `LANG`, `TZ`, and `LD_LIBRARY_PATH` only if the image doesn't set them. For example, if the image doesn't set `TZ`, Lambda sets it to `:UTC`. You don't need to set these variables in the image. The RIE doesn't set these variables. To test the runtime image locally, pass them when you run the container. For more information, see [(Optional) Test your runtime image locally](#cmr-images-from-scratch-test).

Lambda doesn't set `_HANDLER` for a runtime that you build from scratch. Unless your entrypoint sets `_HANDLER`, your bootstrap must read the handler from its arguments. For more information, see [The runtime startup contract](#cmr-images-from-scratch-startup).

The following table lists the environment variables that Lambda base images set. For `LAMBDA_TASK_ROOT` and `LAMBDA_RUNTIME_DIR`, the table also shows the values that Lambda uses when it starts the runtime.


**Environment variables in Lambda base images**  

| Variable | Purpose | Value in Lambda base images | 
| --- | --- | --- | 
| LANG | Sets the locale, including the default character encoding. | en\_US.UTF-8 | 
| TZ | Sets the time zone from the system time zone file, /etc/localtime. | :/etc/localtime (UTC) | 
| PATH | Lists the directories to search for executables. The list includes the language runtime (/var/lang/bin) and executables from layers (/opt/bin). | /var/lang/bin:/usr/local/bin:/usr/bin/:/bin:/opt/bin | 
| LD\_LIBRARY\_PATH | Lists the directories that the dynamic linker searches for shared libraries (.so files) before the system defaults. The list includes libraries for the language runtime (/var/lang/lib) and for the runtime (/var/runtime). The list also includes native libraries in the function code (/var/task/lib) and in layers (/opt/lib). | /var/lang/lib:/lib64:/usr/lib64:/var/runtime:/var/runtime/lib:/var/task:/var/task/lib:/opt/lib | 
| LAMBDA\_TASK\_ROOT | Sets the path to the function code. Lambda runtimes use the value to find and load the function code. For example, the Python runtime adds the value to the module search path. | /var/task | 
| LAMBDA\_RUNTIME\_DIR | Sets the path to the runtime files. | /var/runtime | 

Lambda also sets reserved environment variables at run time, such as `AWS_REGION`, `AWS_LAMBDA_FUNCTION_NAME`, and `AWS_LAMBDA_RUNTIME_API`. Don't set reserved environment variables in the runtime image. For a list of reserved environment variables, see [Defined runtime environment variables](configuration-envvars.md#configuration-envvars-runtime).

Your runtime can also read the environment variables in the function configuration. For more information, see [Working with Lambda environment variables](configuration-envvars.md).

Function environment variables override variables with the same name in the runtime image.

Don't put secrets in environment variables in the runtime image. Function code can read every environment variable that the image sets. For more information, see [What goes into a runtime image](cmr-building-images.md#cmr-building-images-components).

## Declaring capabilities
<a name="cmr-images-from-scratch-capabilities"></a>

A runtime image that you build from scratch declares capabilities in the same way as any other runtime image. For example, to let functions on Lambda Managed Instances use your runtime, add the Lambda Managed Instances label to the image. Your runtime must also handle multiple invocations at the same time in one execution environment. For more information, see [Lambda Managed Instances](cmr-building-images.md#cmr-building-images-managed-instances).

## Example: Python runtime from the OS-only base image
<a name="cmr-images-from-scratch-example"></a>

The following example builds a Python runtime image from the OS-only base image. The Dockerfile installs Python 3.14, the latest Python version in the Amazon Linux 2023 package repositories. Then the Dockerfile installs the Python RIC in `/var/runtime`, and adds a bootstrap. For the Python RIC package, see [Open-source repositories](runtimes-open-source.md). The runtime image keeps the inherited `ENTRYPOINT`, `/lambda-entrypoint.sh`.

The example expects the following files in the build context:
+ `Dockerfile` – The instructions to build the runtime image
+ `bootstrap` – The script that starts the Python RIC

The following example shows the `Dockerfile`:

```dockerfile
FROM public.ecr.aws/lambda/provided:al2023

# Install the Python interpreter and pip from the Amazon Linux 2023 repositories.
RUN dnf install -y python3.14 python3.14-pip && dnf clean all

# Install the Lambda runtime interface client for Python in /var/runtime.
RUN python3.14 -m pip install --no-cache-dir --target /var/runtime awslambdaric

# Add the bootstrap. /lambda-entrypoint.sh runs /var/runtime/bootstrap.
COPY bootstrap /var/runtime/bootstrap
RUN chmod 755 /var/runtime/bootstrap

# Keep the inherited ENTRYPOINT. Don't set CMD.
# Lambda passes the handler from the function configuration.
```

The following example shows the `bootstrap` script. `/lambda-entrypoint.sh` sets `_HANDLER` before the script runs. The script sets the Python search path, and then starts the Python RIC with the handler. If the function sets `AWS_LAMBDA_EXEC_WRAPPER`, the script runs the Python RIC through the wrapper script.

```bash
#!/bin/sh
# Function code first, then layers, then the runtime's own libraries.
export PYTHONPATH="/var/task:/opt/python/lib/python3.14/site-packages:/opt/python:/var/runtime"

if [ -n "$AWS_LAMBDA_EXEC_WRAPPER" ]; then
  exec "$AWS_LAMBDA_EXEC_WRAPPER" /usr/bin/python3.14 -m awslambdaric "$_HANDLER"
fi

exec /usr/bin/python3.14 -m awslambdaric "$_HANDLER"
```

Save the `bootstrap` file with Unix line endings (LF). A script with Windows line endings (CRLF) fails to run.

Functions that use this runtime set the handler in the Python format, for example `lambda_function.lambda_handler`. For more information, see [Define Lambda Event Function handler in Python](python-handler.md).

## Build and push the runtime image
<a name="cmr-images-from-scratch-build"></a>

You build and push a runtime image from scratch in the same way as a runtime image from a Lambda base image. For the procedure, see [Build and push a runtime image](cmr-base-images.md#cmr-base-images-build). Use your own Amazon ECR repository name and image tag in the commands.

If you build a multi-architecture runtime image, make sure that every component works on both architectures. Most OS packages and RIC packages are available for both architectures. Any binary file that you copy into the image must match each architecture. For more information, see [Architectures](cmr-building-images.md#cmr-building-images-architectures).

After you push the runtime image, [create a runtime version](cmr-versions.md) from the runtime image. Then roll the new runtime version out to your functions. For more information, see [Deploying runtime updates](cmr-deploy-updates.md).

## (Optional) Test your runtime image locally
<a name="cmr-images-from-scratch-test"></a>

The OS-only base image includes the [runtime interface emulator](https://github.com/aws/aws-lambda-runtime-interface-emulator/) (RIE). If your runtime image keeps `/lambda-entrypoint.sh` as the `ENTRYPOINT`, the script starts the runtime under the RIE when you run the runtime image outside Lambda.

**To test a runtime image from the OS-only base image locally**

1. In an empty directory, create a file named `lambda_function.py` with sample function code. The following example returns the Python version of the runtime:

   ```python
   import platform
   
   
   def lambda_handler(event, context):
       return {"pythonVersion": platform.python_version()}
   ```

1. From the same directory, run the following command. The command uses the example image URI from [Build and push a runtime image](cmr-base-images.md#cmr-base-images-build). The command mounts the directory as read-only `/var/task`, and passes the handler as the command argument.

   ```bash
   docker run --rm --platform linux/arm64 -p 9000:8080 \
     -v "$PWD":/var/task:ro \
     123456789012.dkr.ecr.us-east-1.amazonaws.com/companypython:2026-10-08.1 \
     lambda_function.lambda_handler
   ```

   The `--platform` value must match an architecture in the runtime image.

1. From a new terminal window, invoke the function with **curl**:

   ```bash
   curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
   ```

   You should see output similar to the following:

   ```json
   {"pythonVersion": "3.14.8"}
   ```

1. To stop the container, press CtrlC in the terminal window where the container runs.

If you use your own entrypoint, the RIE doesn't start automatically. To test locally, download the RIE and run your entrypoint under it. You can [build the emulator into your image](https://github.com/aws/aws-lambda-runtime-interface-emulator/?tab=readme-ov-file#build-rie-into-your-base-image) or [install the emulator on your local machine](https://github.com/aws/aws-lambda-runtime-interface-emulator/?tab=readme-ov-file#test-an-image-without-adding-rie-to-the-image).

If your own base image copies `/lambda-entrypoint.sh` from a Lambda base image, the script starts the RIE when you run the image outside Lambda. The script runs the RIE from `/usr/local/bin/aws-lambda-rie`, and your image doesn't include the RIE unless you add it. To test locally, add the RIE to the image at that path. Or mount it when you run the container, for example with `-v ./aws-lambda-rie:/usr/local/bin/aws-lambda-rie`. Lambda doesn't need the RIE in the runtime image.

The RIE doesn't set Lambda environment variables such as `LAMBDA_TASK_ROOT`. In Lambda, the service sets them, and Lambda base images also set them with `ENV`. To test a runtime image from your own base image locally, pass the variables when you run the container. For example, pass `-e LAMBDA_TASK_ROOT=/var/task` to **docker run**. If your bootstrap uses `LAMBDA_RUNTIME_DIR`, also pass `-e LAMBDA_RUNTIME_DIR=/var/runtime`.

## Keeping your runtime patched
<a name="cmr-images-from-scratch-patching"></a>

Lambda doesn't update your runtime image or your runtime versions. You're responsible for patching every component in the runtime image. What you patch depends on your base image:
+ **Lambda OS-only base image** – Lambda patches the OS. To get the OS patches, rebuild your runtime image from the updated OS-only base image. You patch the language runtime, the RIC, and everything else that you add.
+ **Your own base image** – You patch every component, including the OS libraries.

After each rebuild, publish the new runtime image as a new runtime version, and update your runtime aliases. We recommend that you rebuild, test, and publish your runtime in an automated pipeline. For more information, see [Building a runtime update pipeline](cmr-deploy-updates.md#cmr-deploy-updates-pipeline).

To make builds reproducible, refer to the base image with a version-specific tag or a digest, and pin the versions of the language runtime and the RIC. Then update the pinned versions to pick up patches. For more information about the trade-offs, see [Keeping your runtime patched](cmr-base-images.md#cmr-base-images-patching).

## Next steps
<a name="cmr-images-from-scratch-next-steps"></a>

After you push your runtime image, continue with the following topics:
+ To create a runtime, see [Creating a runtime](cmr-create.md).
+ To publish your runtime image as a runtime version, see [Runtime versions](cmr-versions.md).
+ To roll out the runtime version to functions, see [Deploying runtime updates](cmr-deploy-updates.md).