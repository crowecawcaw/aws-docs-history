

# Building a runtime image from a Lambda base image

The fastest way to build a runtime image is to start from a Lambda base image. Each language base image already has the operating system, the language runtime, and the Lambda runtime interface client (RIC). You add your own components, such as an organization SDK, an extension, or a trusted certificate. Then you push the runtime image to Amazon Elastic Container Registry (Amazon ECR) and publish the image as a runtime version.

This topic shows how to build a runtime image from a Lambda base image. For the principles that apply to every runtime image, such as the file system layout and how Lambda starts the runtime, see [Building runtime images](cmr-building-images.md).

## About Lambda base images
<a name="cmr-base-images-about"></a>

Lambda publishes base images in the [Amazon ECR Public Gallery](https://gallery.ecr.aws/lambda/). Each image URI has the format `public.ecr.aws/lambda/{{runtime}}:{{version}}`. The following table lists examples.


**Examples of Lambda base images**  

| Base image | Contents | 
| --- | --- | 
| public.ecr.aws/lambda/python:3.14 | Amazon Linux 2023, Python 3.14, and the Lambda RIC for Python | 
| public.ecr.aws/lambda/nodejs:24 | Amazon Linux 2023, Node.js 24, and the Lambda RIC for Node.js | 
| public.ecr.aws/lambda/java:21 | Amazon Linux 2023, Java 21, and the Lambda RIC for Java | 
| public.ecr.aws/lambda/dotnet:8 | Amazon Linux 2023, .NET 8, and the Lambda RIC for .NET | 
| public.ecr.aws/lambda/ruby:3.4 | Amazon Linux 2023, Ruby 3.4, and the Lambda RIC for Ruby | 
| public.ecr.aws/lambda/provided:al2023 | Amazon Linux 2023 only, with no language runtime or RIC | 

Each language base image has the same components as the Lambda-managed runtime for that language. For the full list of base images, see [Using an AWS base image for Lambda](images-create.md#runtimes-images-lp). The OS-only base image (`provided:al2023`) contains Amazon Linux 2023 but no language runtime. You can use the OS-only base image as a starting point to add your own language runtime. For more information about the OS-only base image, see [Choosing a base image](cmr-images-from-scratch.md#cmr-images-from-scratch-base-image).

Lambda base images have the following configuration:
+ `ENTRYPOINT` is `["/lambda-entrypoint.sh"]`.
+ `CMD` isn't set.
+ `WORKDIR` is `/var/task`.

Keep the base image's `ENTRYPOINT` unless you have a specific reason to change the `ENTRYPOINT`. Don't set a `CMD`, and don't put a function handler in the runtime image. Lambda passes the handler from the function configuration to `/lambda-entrypoint.sh`. For more information, see [How Lambda base images start the runtime](#cmr-building-images-startup-base-images).

## How Lambda base images start the runtime
<a name="cmr-building-images-startup-base-images"></a>

Every runtime image must follow the startup contract that [How Lambda starts your runtime](cmr-building-images.md#cmr-building-images-startup) describes. Lambda base images implement the startup contract for you.

Lambda base images set `ENTRYPOINT` to `/lambda-entrypoint.sh` and don't set a `CMD`. The working directory in Lambda base images is `/var/task`. A Lambda base image starts the runtime in the following order:

1. Lambda runs `/lambda-entrypoint.sh` with the handler as the only argument. The script exits with an error if the script receives a different number of arguments.

1. The script sets the `_HANDLER` environment variable to the handler, and then runs `/var/runtime/bootstrap`.

1. The bootstrap starts the language runtime, which runs the Lambda RIC.

1. The RIC reads `_HANDLER` to find the function code and the handler function.

For example, a Python function might have the handler `lambda_function.lambda_handler`. Lambda runs a command similar to the following:

```bash
/lambda-entrypoint.sh lambda_function.lambda_handler
```

The script sets `_HANDLER` to `lambda_function.lambda_handler`, and then starts `/var/runtime/bootstrap`. During initialization, the RIC loads the `lambda_function` module, which is the file `lambda_function.py` in `/var/task`. For each invocation, the RIC calls the `lambda_handler` function. For more information about the Python handler format, see [Define Lambda Event Function handler in Python](python-handler.md).

When you run the image outside Lambda, for example on your local machine, the `AWS_LAMBDA_RUNTIME_API` environment variable isn't set. In this case, `/lambda-entrypoint.sh` runs `/var/runtime/bootstrap` under the [runtime interface emulator](https://github.com/aws/aws-lambda-runtime-interface-emulator/) (RIE), `/usr/local/bin/aws-lambda-rie`. You can use the RIE to test your runtime image locally.

Because Lambda base images don't set a `CMD`, a runtime image that you build on a Lambda base image doesn't inherit a handler.

If you replace the `ENTRYPOINT` in a runtime image that you build on a Lambda base image, `/lambda-entrypoint.sh` no longer runs. In this case, Lambda doesn't set the `_HANDLER` environment variable. Your program must read the handler from the arguments that Lambda passes, or set `_HANDLER` itself.

## Adding your components
<a name="cmr-base-images-components"></a>

Add your components on top of the base image in your Dockerfile. Every function that uses the runtime gets these components. The following table shows where to put each kind of component.


**Where to put components in a runtime image**  

| Component | Location | 
| --- | --- | 
| Python libraries | Install with pip install, without the --target option. In Python 3.11 and later base images, pip installs packages in /var/lang/lib/python3.{{x}}/site-packages, with the runtime-included libraries. pip then reports any conflicts with the runtime-included libraries when you build the image. For more information, see [Dependency search path in the base images](python-image.md#python-image-searchpath). | 
| Node.js libraries | Put libraries in /var/runtime/node\_modules. In Lambda base images, /var/runtime/node\_modules is on the NODE\_PATH search path. The Lambda base image build of Node.js searches NODE\_PATH for both CommonJS modules and ES modules (ESM). Standard Node.js searches NODE\_PATH for CommonJS modules only. For more information, see [Dependency search path and runtime-included libraries](nodejs-package.md#nodejs-package-searchpath). | 
| Libraries for other languages | Put libraries in /var/runtime, and make sure that the language runtime's search path includes the library location. For more information, see [Adding code libraries and extensions](cmr-building-images.md#cmr-building-images-libraries). | 
| Extensions | Copy extension executables to /var/runtime-opt/extensions. Lambda starts each file in the directory, so put only extension executables in the directory. For more information, see [Adding code libraries and extensions](cmr-building-images.md#cmr-building-images-libraries). | 
| Certificates | Add certificates to the operating system trust store. On Amazon Linux 2023, copy the certificate to /etc/pki/ca-trust/source/anchors, and then run update-ca-trust. | 
| Configuration files | Put configuration files in any directory except /opt, /var/task, and /tmp. For example, use /etc or /var/runtime. | 

Function code can override the libraries in your runtime. The language runtime searches `/var/task` first, so a library in the function's .zip file archive has precedence over the same library in the runtime image. Function layers can also add or override libraries and extensions.

Some libraries don't use the operating system trust store. For example, the Python `requests` library uses the certificates from the `certifi` package by default, and Node.js uses a certificate store that's built into Node.js. Check how each library in your runtime finds certificates.

When you add components, follow these rules:
+ Don't put anything in `/opt`, `/var/task`, or `/tmp`. Lambda uses these directories for layers, function code, and temporary storage. For more information, see [File system layout](cmr-building-images.md#cmr-building-images-layout).
+ Use absolute paths in `COPY` and `RUN` instructions. The base image sets `WORKDIR` to `/var/task`, so a relative path puts files in `/var/task`.
+ Don't replace the base image's language runtime, RIC, or `/var/runtime/bootstrap`. To change these components, build from scratch instead. For more information, see [Building runtime images from scratch](cmr-images-from-scratch.md).
+ Don't put secrets in the runtime image. Function code can read everything in the runtime image. For more information, see [What goes into a runtime image](cmr-building-images.md#cmr-building-images-components).

### Choosing architectures
<a name="cmr-base-images-architectures"></a>

Lambda base images are available for both the x86\_64 and arm64 architectures. To choose an architecture, use the `--platform` option when you build the image:
+ `--platform linux/amd64` builds an x86\_64 runtime image.
+ `--platform linux/arm64` builds an arm64 runtime image.
+ `--platform linux/amd64,linux/arm64` with **docker buildx** builds a multi-architecture runtime image that supports both architectures.

If you add binary files, such as a native extension, add the correct binary file for each architecture. For more information, see [Architectures](cmr-building-images.md#cmr-building-images-architectures).

### Declaring capabilities
<a name="cmr-base-images-capabilities"></a>

A runtime image that you build from a Lambda base image declares capabilities in the same way as any other runtime image. For example, to let functions on Lambda Managed Instances use your runtime, add the Lambda Managed Instances label to the image. For more information, see [Lambda Managed Instances](cmr-building-images.md#cmr-building-images-managed-instances). Lambda base images set the integration model and Lambda Managed Instances labels, which your image inherits. You can override a label with your own `LABEL` instruction.

## Keeping your runtime patched
<a name="cmr-base-images-patching"></a>

Lambda regularly updates the base images with security patches. However, Lambda doesn't update your runtime image or your runtime versions. To pick up the patches, rebuild your runtime image from the updated base image. Then publish the new runtime image as a new runtime version, and update your runtime aliases. You must also patch the components that you add. For more information, see [Deploying runtime updates](cmr-deploy-updates.md).

The `FROM` instruction can refer to the base image in three ways. You can use a mutable tag, a version-specific tag, or a digest. The following table compares the three options.


**Ways to refer to a base image in the FROM instruction**  

| Option | Example | Trade-offs | 
| --- | --- | --- | 
| Mutable tag | FROM public.ecr.aws/lambda/python:3.14 | Lambda moves the tag to each new patched base image. Every rebuild picks up the latest patches automatically. Builds aren't reproducible, because two builds of the same Dockerfile can produce different runtime images. | 
| Version-specific tag (immutable) | FROM public.ecr.aws/lambda/python:3.14.2026.02.23.16 | Lambda publishes a version-specific tag for each base image release. The tag doesn't change, so builds are reproducible. The tag is also easier to read than a digest. To pick up patches, update the tag to a newer release. | 
| Digest | FROM public.ecr.aws/lambda/python@sha256:{{digest}} | A digest never changes, so builds are reproducible. A digest is harder to read than a tag. To pick up patches, update the digest. | 

Version-specific tags have the format `{{tag}}.{{YYYY}}.{{MM}}.{{DD}}.{{HH}}`, with an optional `-x86_64` or `-arm64` suffix. For example, `public.ecr.aws/lambda/python:3.14.2026.11.13.18`. To find the tags for a base image, see the **Image tags** tab for the image in the Amazon ECR Public Gallery. For example, see the [Python base image](https://gallery.ecr.aws/lambda/python).

If you use a version-specific tag or a digest, automate the updates. For example, a scheduled job or a dependency update tool can check for a new base image release. The job or tool can then open a change request to update the tag or digest in your Dockerfile.

We recommend that you rebuild and publish your runtime in an automated pipeline. A pipeline makes regular patching practical, and the pipeline tests every update in the same way. For more information, see [Building a runtime update pipeline](cmr-deploy-updates.md#cmr-deploy-updates-pipeline).

Lambda stops updating a base image when Lambda deprecates the matching runtime, so the base image no longer gets security patches. You have the following options:
+ Align your [deprecation lifecycle](cmr-lifecycle.md) with the base image that you build on. Set the deprecation date of your runtime, or of your alias, to the deprecation date of the matching Lambda runtime.
+ Move your runtime to a base image for a supported Lambda runtime before the deprecation date.
+ Take over patching the base image yourself.

For more information about the Lambda deprecation policy, see [Runtime deprecation](runtime-support-policy.md).

## Example Dockerfiles
<a name="cmr-base-images-examples"></a>

The following examples show Dockerfiles for runtime images that start from a Lambda base image.

### Python 3.14 with an organization SDK and a certificate
<a name="cmr-base-images-example-python"></a>

The following Dockerfile starts from the Python 3.14 base image. The Dockerfile installs an organization SDK from a wheel file, and adds a private certificate authority (CA) certificate to the trust store. The `--mount` option makes the wheel file available during the build without copying the wheel file into the runtime image.

```dockerfile
FROM public.ecr.aws/lambda/python:3.14

# Install the organization SDK into the runtime's site-packages directory.
RUN --mount=type=bind,source=wheels,target=/wheels \
    pip install --no-cache-dir /wheels/my_org_sdk-2.4.0-py3-none-any.whl

# Add the organization's private CA certificate to the trust store.
COPY certs/my-org-root-ca.pem /etc/pki/ca-trust/source/anchors/my-org-root-ca.pem
RUN update-ca-trust

# Don't set CMD. Lambda passes the handler from the function configuration.
```

The example expects the following files in the build context:
+ `wheels/my_org_sdk-2.4.0-py3-none-any.whl` – The organization SDK
+ `certs/my-org-root-ca.pem` – The CA certificate in PEM format

The `--mount` option requires BuildKit, which is the default builder in current versions of Docker.

### Node.js 24 with an extension
<a name="cmr-base-images-example-nodejs"></a>

The following Dockerfile starts from the Node.js 24 base image and adds a runtime-level extension. The Dockerfile uses the `TARGETARCH` build argument to copy the extension binary file for each architecture. With this approach, you can build a multi-architecture runtime image from one Dockerfile.

```dockerfile
FROM public.ecr.aws/lambda/nodejs:24

# Docker sets TARGETARCH to amd64 or arm64 for each platform in the build.
ARG TARGETARCH

# Add the telemetry extension as a runtime-level extension.
COPY extensions/${TARGETARCH}/my-telemetry-extension /var/runtime-opt/extensions/my-telemetry-extension
RUN chmod 755 /var/runtime-opt/extensions/my-telemetry-extension

# Don't set CMD. Lambda passes the handler from the function configuration.
```

The example expects the extension binary files in `extensions/amd64/my-telemetry-extension` and `extensions/arm64/my-telemetry-extension`. The extension must register with the Lambda Extensions API. For more information, see [Using the Lambda Extensions API to create extensions](runtimes-extensions-api.md).

## Build and push a runtime image
<a name="cmr-base-images-build"></a>

Build the runtime image with Docker, and push the runtime image to Amazon ECR. Then create a runtime version from the runtime image. You build runtime images with Docker tools, so the Lambda console has no steps for this task.

Before you start, make sure that you have the following:
+ Docker with the **buildx** plugin, or a similar tool for building container images.
+ The AWS CLI.
+ A Dockerfile for your runtime image, such as one of the [example Dockerfiles](#cmr-base-images-examples).
+ An Amazon ECR repository in the same AWS Region as your runtime. The repository policy must allow Lambda to read images. For instructions, see [Grant Lambda access to your Amazon ECR repository](cmr-versions.md#cmr-publish-versions-grant-ecr).
+ A runtime. For instructions, see [Creating a runtime](cmr-create.md).

The examples use account `123456789012`, the `us-east-1` Region, and an Amazon ECR repository and runtime named `companypython`. Each build gets a unique, date-based tag, such as `2026-10-08.1`.

**To build and push a runtime image (AWS CLI)**

1. To authenticate Docker to your Amazon ECR registry, run the following command:

   ```bash
   aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com
   ```

1. In the directory that contains your Dockerfile, run the **docker buildx build** command. The `--push` option pushes the runtime image to Amazon ECR after the build.

   To build a single-architecture runtime image, specify one platform:

   ```bash
   docker buildx build \
     --platform linux/arm64 \
     --tag 123456789012.dkr.ecr.us-east-1.amazonaws.com/companypython:2026-10-08.1 \
     --push .
   ```

   To build a multi-architecture runtime image, specify both platforms:

   ```bash
   docker buildx build \
     --platform linux/amd64,linux/arm64 \
     --tag 123456789012.dkr.ecr.us-east-1.amazonaws.com/companypython:2026-10-08.1 \
     --push .
   ```

1. To confirm that Amazon ECR has the runtime image, run the **describe-images** command:

   ```bash
   aws ecr describe-images \
     --repository-name companypython \
     --image-ids imageTag=2026-10-08.1 \
     --region us-east-1
   ```

   The output shows the image digest, tags, and push time.

Your runtime image is now ready. Next, [create a runtime version](cmr-versions.md) from the runtime image. Then roll the new runtime version out to your functions. For more information, see [Deploying runtime updates](cmr-deploy-updates.md).

## (Optional) Test your runtime image locally
<a name="cmr-base-images-test"></a>

Lambda base images include the runtime interface emulator (RIE). When you run the runtime image outside Lambda, `/lambda-entrypoint.sh` starts the runtime under the RIE. You can use the RIE to invoke a sample function with your runtime image before you publish a runtime version. For more information, see [How Lambda base images start the runtime](#cmr-building-images-startup-base-images).

**To test a runtime image locally**

1. In an empty directory, create a file named `lambda_function.py` with sample function code. The following example imports the organization SDK from the Python example Dockerfile:

   ```python
   import my_org_sdk
   
   
   def lambda_handler(event, context):
       return {"sdkVersion": my_org_sdk.__version__}
   ```

1. From the same directory, run the following command. The command mounts the directory as read-only `/var/task`, and passes the handler as the command argument.

   ```bash
   docker run --rm --platform linux/arm64 -p 9000:8080 \
     -v "$PWD":/var/task:ro \
     123456789012.dkr.ecr.us-east-1.amazonaws.com/companypython:2026-10-08.1 \
     lambda_function.lambda_handler
   ```

   The `--platform` value must match an architecture in the runtime image. To run an image for a different architecture than your computer, Docker must support emulation.

1. From a new terminal window, invoke the function with **curl**:

   ```bash
   curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
   ```

   You should see output similar to the following:

   ```json
   {"sdkVersion": "2.4.0"}
   ```

1. To stop the container, press CtrlC in the terminal window where the container runs.

The RIE starts extensions only from `/opt/extensions`. To test a runtime-level extension locally, also copy it to `/opt/extensions` in a test image.

## Next steps
<a name="cmr-base-images-next-steps"></a>

After you push your runtime image, continue with the following topics:
+ To create a runtime, see [Creating a runtime](cmr-create.md).
+ To publish your runtime image as a runtime version, see [Runtime versions](cmr-versions.md).