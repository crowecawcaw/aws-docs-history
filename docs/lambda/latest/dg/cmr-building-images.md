

# Building runtime images

Each version of a customer-managed runtime references a container image in Amazon Elastic Container Registry (Amazon ECR) to define the runtime file system contents. The image has everything that Lambda needs to run function code in your language. This topic explains what goes into an image, how Lambda uses it, and how to structure it.

## Ways to build a runtime image
<a name="cmr-building-images-approaches"></a>

You can build a runtime image in one of the following ways:
+ **Start from a Lambda base image** – Add your components on top of an image that already has the operating system (OS), language runtime, and runtime interface client (RIC). Each language base image has the same components as the Lambda-managed runtime for that language. For more information, see [Building a runtime image from a Lambda base image](cmr-base-images.md).
+ **Build from scratch with a Lambda runtime interface client** – Start from a base image without a language runtime. Then add a language runtime and one of the open-source RICs from Lambda. For a list of these RICs, see [Open-source repositories](runtimes-open-source.md). For more information, see [Building runtime images from scratch](cmr-images-from-scratch.md).
+ **Support a new language with your own RIC** – Start from a base image without a language runtime, and write your own RIC for a language that Lambda doesn't support. Your RIC uses the Lambda runtime API to get events and send responses. For more information, see [Supporting a new programming language for AWS Lambda Event Functions](runtimes-custom.md) and [Using the Lambda runtime API](runtimes-api.md).

For the second and third options, you can start from either a Lambda [OS-only base image](https://gallery.ecr.aws/lambda/provided) such as `public.ecr.aws/lambda/provided:al2023` or a base image of your choice. The Lambda OS-only base images are updated regularly with the latest security patches. For more information, see [OS-only runtimes](lambda-runtimes.md#runtimes-provided).

The following table compares the three approaches.


**Comparison of approaches to building a runtime image**  

| Approach | Effort | Control | Patching | Typical use | 
| --- | --- | --- | --- | --- | 
| Start from a Lambda base image | Low. Lambda provides the OS, language runtime, and RIC. | You control what you add. Lambda controls the base. | Lambda patches the base image. You rebuild to get the patches, and you patch what you add. | Add your own libraries, certificates, or extensions to a language that Lambda supports. | 
| Build from scratch with a Lambda RIC | Medium. You assemble the runtime from the base image, adding the language runtime and one of the Lambda open-source RICs. | You control the language runtime and choice of RIC. The base image (Lambda or other) controls the OS libraries. | You patch the language runtime and OS libraries, and keep the RIC up to date. If you use a Lambda OS-only base image, rebuild to get OS patches. | Use a different OS or language version, or meet strict security rules. | 
| Support a new language with your own RIC | High. You assemble the runtime from the base image, adding the language runtime and your own RIC, which you write and maintain. | You control the language runtime, your RIC, and how the runtime communicates with Lambda. The base image (Lambda or other) controls the OS libraries. | You patch the language runtime, your RIC, and OS libraries. If you use a Lambda OS-only base image, rebuild to get OS patches. | Run a language or framework that Lambda doesn't support. | 

## What goes into a runtime image
<a name="cmr-building-images-components"></a>

A runtime image holds everything that functions need to run, except function code and layers. It typically includes the following:
+ **OS libraries** – The system libraries and packages that the language runtime and function code need.
+ **Language runtime** – The interpreter or virtual machine for your language, if it needs one. For example, Node.js, Python, or Java.
+ **Runtime interface client** – The code that loads the function handler. It gets events from Lambda and sends back responses.
+ **Bootstrap** – The file that Lambda runs to start the runtime. This is the entrypoint of the container image.
+ **Packages and certificates** – Extra packages, and the trusted certificates that code uses for secure connections.
+ **Shared components** – Items that you want every function to have, such as your own SDKs, security tools, and extensions.

A runtime image also needs environment variables, such as `PATH`. Lambda base images, including the OS-only base image, already set them. Lambda sets variables such as `LAMBDA_TASK_ROOT` when it starts the runtime. If you use your own base image, see [Setting environment variables in the runtime image](cmr-images-from-scratch.md#cmr-building-images-envvars).

**Important**  
Don't put secrets in a runtime image. Function code can read everything in the image. Anyone who can deploy or invoke a function that uses the runtime can read the entire runtime contents. Don't include passwords, keys, tokens, or sensitive settings.

**Important**  
Choose the packages that you include in a runtime image carefully. For each package, check the following:  
**Backward compatibility policy** – Functions that use the runtime pick up [runtime updates](cmr-deploy-updates.md) automatically. Future updates to each package must stay backward compatible with existing function code. Consider both API compatibility and ABI compatibility. API compatibility covers the source-level interfaces that function code calls. ABI compatibility covers binary interfaces, for example for native extensions or compiled dependencies.
**Support period** – Check how long each package is supported, or the package's end-of-life policy. A package's end of support can determine when you need to [deprecate the runtime](cmr-lifecycle.md).

## File system layout
<a name="cmr-building-images-layout"></a>

Lambda uses some directories for function code, layers, and temporary storage. Put your runtime files only in the runtime directories. The following table describes each directory.


**Directories in a runtime image**  

| Directory | Purpose | Guidance for runtime images | 
| --- | --- | --- | 
| /var/runtime | The runtime code and libraries. In Lambda base images, this directory includes the bootstrap. | We recommend that you put the bootstrap here. If you put the bootstrap somewhere else, point the image's ENTRYPOINT to it. We also recommend that you put the code libraries that you add here. In a runtime image that you build from a Lambda base image, use the language runtime's default library location instead. For more information, see [Adding your components](cmr-base-images.md#cmr-base-images-components). | 
| /var/runtime-opt/extensions | Runtime-level extensions that you manage as the runtime publisher. | Put extensions that every function needs here. For more information, see [Adding code libraries and extensions](#cmr-building-images-libraries). | 
| /opt | Reserved for function layers. | Don't put anything in /opt. | 
| /var/task | Reserved for function code from the .zip file archive. | Required. Create /var/task, but leave it empty. Lambda mounts the function code there. For more information, see [Required paths](#cmr-building-images-required-paths). | 
| /tmp | Writable temporary storage for the function. | Don't put anything in /tmp. | 

At run time, the file system is read-only, except for `/tmp`. This behavior is the same as for other Lambda Event Functions. Make sure that your runtime doesn't write to other directories.

### Required paths
<a name="cmr-building-images-required-paths"></a>

Every runtime image must contain the following paths. Lambda mounts over these paths when it creates the execution environment.
+ `/etc/hosts` – A file. The file can be empty. Lambda adds its own entries. If the file is empty, the execution environment has no entry for `localhost`. We recommend that you keep the default `/etc/hosts` file from your base distribution.
+ `/etc/resolv.conf` – A file. The file can be empty. Lambda provides the DNS configuration.
+ `/var/task` – A directory. Leave the directory empty. Lambda mounts the function code there.

Lambda base images include all three paths. If you build from another base image, such as Alpine Linux, make sure that the image contains them.

Some base images don't include `/etc/hosts` or `/etc/resolv.conf` in the image itself. Docker adds these files only when a container runs. As a result, a file that you create with a `RUN` instruction doesn't persist in the image. Instead, use a `COPY` instruction to add each file to the image. The following Dockerfile instructions add the required paths. In this example, `hosts` and `resolv.conf` are files in the build context.

```dockerfile
COPY hosts /etc/hosts
COPY resolv.conf /etc/resolv.conf
RUN mkdir -p /var/task
```

## How Lambda starts your runtime
<a name="cmr-building-images-startup"></a>

Every runtime image must work with the way that Lambda starts the runtime. When Lambda sets up an execution environment for a function, Lambda runs the executable that the image's `ENTRYPOINT` specifies. Lambda passes the function's handler to the executable as the last argument. The handler is the `Handler` property in the function configuration. If the image doesn't set an `ENTRYPOINT`, Lambda runs `/var/runtime/bootstrap`. Lambda places the function code in `/var/task`. Use the exec form of `ENTRYPOINT`, which is a JSON array, so that Lambda can pass the handler to your runtime.

**Important**  
Customer-managed runtimes don't use the image's `CMD`. This behavior is different from container image functions. When you package a function as a container image, you set the handler in the image. In a Lambda base image, you set the handler with `CMD`, and Docker passes the `CMD` value to the `ENTRYPOINT`. For more information, see [Create a Lambda Event Function using a container image](images-create.md).  
When you build a runtime image, don't include the handler in `ENTRYPOINT` or `CMD`. Functions that use your runtime are .zip file archive functions. Lambda supplies the handler from the function configuration as the last argument passed to the `ENTRYPOINT`.

Lambda base images set up the runtime startup for you. For more information, see [How Lambda base images start the runtime](cmr-base-images.md#cmr-building-images-startup-base-images). If you build a runtime image from scratch, see [The runtime startup contract](cmr-images-from-scratch.md#cmr-images-from-scratch-startup).

Lambda base images also set the environment variables that Lambda runtimes need. If you build a runtime image from scratch, see [Setting environment variables in the runtime image](cmr-images-from-scratch.md#cmr-building-images-envvars).

## Adding code libraries and extensions
<a name="cmr-building-images-libraries"></a>

You can add libraries and extensions to your runtime. Every function that uses the runtime then gets them. For example, you can add your own SDK or a monitoring agent.
+ **Code libraries** – We recommend that you put code libraries in `/var/runtime`. In a runtime image that you build from a Lambda base image, put them in the language runtime's default library location instead, such as `site-packages` for Python. For more information, see [Adding your components](cmr-base-images.md#cmr-base-images-components). Resolve conflicts with the runtime's own libraries when you build the image.
+ **Extensions** – Put runtime-level extensions in `/var/runtime-opt/extensions`. Lambda starts each file in this directory, just as it does for `/opt/extensions`. Each extension must register with the Lambda Extensions API. For more information, see [Using the Lambda Extensions API to create extensions](runtimes-extensions-api.md).

Extensions in `/opt/extensions` run alongside your runtime's extensions. Functions and layers can override the extensions in your runtime. If `/opt/extensions` and `/var/runtime-opt/extensions` both have a file with the same name, only the file in `/opt/extensions` runs, and Lambda logs a warning. Because a function can replace a runtime extension in this way, don't rely on a runtime extension to enforce a control that functions must not bypass.

You can't attach Lambda layers to a runtime. Add everything that the runtime needs to the image when you build it. Function developers can still add layers to their functions. For more information about layers, see [Managing Lambda Event Function dependencies with layers](chapter-layers.md).

## Architectures and feature compatibility
<a name="cmr-building-images-capabilities"></a>

Some runtime features, such as support for the `x86_64` and `arm64` architectures and Lambda Managed Instances, require support in the runtime. Lambda blocks functions from using features that their runtime doesn't support.

Lambda reads the supported architectures and features of a runtime version from its container image. You can't set them when you create a runtime version.

The architectures and features are mirrored from the runtime version to any runtime alias that references the version. To prevent regressions for existing functions, you can't update an alias to reference a runtime version that removes an architecture or feature. For more information, see [Runtime version compatibility](cmr-versions.md#cmr-publish-versions-compatibility) and [Alias compatibility](cmr-aliases.md#cmr-aliases-compatibility).

Lambda tracks some features as capabilities on each runtime version and alias, and checks them when a consumer creates or updates a function. Lambda handles other features at a different time, or not at all. The following table summarizes how Lambda handles each feature.


**Runtime features and how Lambda handles them**  

| Feature | Tracked as a capability? | How you set it | Notes | 
| --- | --- | --- | --- | 
| Integration model | Yes | Add a label to the image. | Optional. Declares how the runtime connects to Lambda. If the image doesn't set the label, Lambda uses RuntimeAPI. For more information, see [Feature compatibility labels](#cmr-building-images-capability-annotations). | 
| Architectures | Yes | Determined by the image platforms. | A function can use the runtime only if the runtime supports the function's architecture. For more information, see [Architectures](#cmr-building-images-architectures). | 
| Lambda Managed Instances | Yes | Add a label to the image. | Declares whether functions on Lambda Managed Instances can use the runtime. If the image doesn't set the label to Supported, functions on Lambda Managed Instances can't use the runtime. For more information, see [Lambda Managed Instances](#cmr-building-images-managed-instances). | 
| Response streaming | No | Implement it in the runtime. | Lambda doesn't track or enforce response streaming. A runtime that supports it must implement the streaming response mode of the Lambda runtime API. For more information, see [Implementing response streaming in your runtime](runtimes-custom.md#runtimes-custom-response-streaming) and [Response streaming for Lambda Event Functions](configuration-response-streaming.md). | 
| Durable functions | No | No runtime changes needed. | The function needs the appropriate SDK and configuration. | 
| Bundled SDKs | No | No runtime changes needed. | A runtime can package an SDK. Describe the SDK in the runtime or alias description. | 

Lambda checks architecture and Lambda Managed Instances compatibility when a consumer creates or updates a function, or pins it to a runtime version in **Manual** mode.

Lambda also checks that a runtime version supports at least the capabilities of any alias that points to the version. For more information, see [How Lambda checks alias compatibility](cmr-aliases.md#cmr-aliases-compatibility-rules).

### Architectures
<a name="cmr-building-images-architectures"></a>

Lambda determines the architectures that a runtime supports from the platforms in the container image. There's no label for architectures. You can build a runtime image for one architecture, or for both:
+ **Single-architecture image** – An image for either `x86_64` or `arm64`. The runtime version supports only that architecture.
+ **Multi-architecture image** – An image index (manifest list) with an image for each architecture. The runtime version supports both architectures.

A function can use a runtime only if the runtime supports the function's architecture. When a function uses a multi-architecture runtime version, Lambda selects the image that matches the function's architecture. For more information about how Lambda reads architectures from an image, see [Supported architectures](cmr-versions.md#cmr-publish-versions-architectures). For more information about function architectures, see [Selecting and configuring an instruction set architecture for your Lambda function](foundation-arch.md).

To build a multi-architecture image, use the **docker buildx build** command and specify both platforms:

```bash
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  --tag 123456789012.dkr.ecr.us-east-1.amazonaws.com/companyphp8:v8.3.1 \
  --push .
```

A multi-architecture runtime version must support the same features for both architectures. To offer different features for each architecture, publish single-architecture versions and point a separate alias to each one, or create separate runtimes.

### Feature compatibility labels
<a name="cmr-building-images-capability-annotations"></a>

To declare which features your runtime supports, add Docker `LABEL` instructions to the image's Dockerfile. Lambda reads the labels when you publish a runtime version, and sets the version's capabilities from them. An alias reflects the capabilities of the version that the alias points to. For more information, see [Runtime version compatibility](cmr-versions.md#cmr-publish-versions-compatibility) and [Alias compatibility](cmr-aliases.md#cmr-aliases-compatibility).

Keep the following in mind when you set labels:
+ Labels are inherited from base images. Lambda base images set the integration model and Lambda Managed Instances labels, so an image that you build from a Lambda base image inherits them. You can override an inherited label with your own `LABEL` instruction.
+ Label values aren't case-sensitive.
+ In a multi-architecture image, labels are stored in each architecture's image, not in the image index (manifest list). The images for both `x86_64` and `arm64` must therefore have the same labels. When you build both platforms with one **docker buildx build** command, as shown in [Architectures](#cmr-building-images-architectures), both images get the same labels from the same Dockerfile. If you build the images separately and combine them into an image index, for example with **docker buildx imagetools create**, make sure that each image has the same labels.

**Integration model**

The integration model declares how the runtime connects to Lambda. The only supported value is `RuntimeAPI`, which means that the runtime uses the Lambda runtime API and can be used with Lambda Event Functions. For more information, see [Using the Lambda runtime API](runtimes-api.md).

If the image doesn't set this label, Lambda uses `RuntimeAPI`. For runtimes that Lambda Event Functions use, you don't need to set the label. To set it explicitly, add the following `LABEL` instruction:

```dockerfile
LABEL com.amazonaws.lambda.feature.integrationmodel="RuntimeAPI"
```

#### Lambda Managed Instances
<a name="cmr-building-images-managed-instances"></a>

This label declares whether functions on [Lambda Managed Instances](lambda-managed-instances.md) can use the runtime. To support Lambda Managed Instances, your runtime must also handle multiple invocations at the same time in one execution environment. For more information, see [Supporting a new programming language for AWS Lambda Event Functions](runtimes-custom.md).

Before you set this label, make sure that your runtime meets the requirements in [Supporting Lambda Managed Instances in your runtime](runtimes-custom.md#runtimes-custom-managed-instances). Functions on Lambda Managed Instances also need the Lambda service principal to have the `ecr:DescribeImages` permission on your repository. For more information, see [Grant Lambda access to your Amazon ECR repository](cmr-versions.md#cmr-publish-versions-grant-ecr).

Set the label to one of the following values:
+ `Supported` – Functions on Lambda Managed Instances can use the runtime.
+ `NotSupported` – Functions on Lambda Managed Instances can't use the runtime.

```dockerfile
LABEL com.amazonaws.lambda.feature.managedinstances="Supported"
```

To support Lambda Managed Instances, set the label to `Supported`. The value isn't case-sensitive, so `supported` also works. Lambda treats any other value as `NotSupported`. If the image doesn't set this label, the runtime version doesn't support Lambda Managed Instances. Functions on Lambda Managed Instances can't use the runtime version.

#### Combined example
<a name="cmr-building-images-capability-example"></a>

The following Dockerfile sets the Lambda Managed Instances label on a runtime image that builds from a Lambda base image. The image doesn't set the integration model label, so Lambda uses `RuntimeAPI`.

```dockerfile
FROM public.ecr.aws/lambda/python:3.14

LABEL com.amazonaws.lambda.feature.managedinstances="Supported"
```

You can also set several labels in a single `LABEL` instruction. The following example also sets the integration model explicitly:

```dockerfile
LABEL com.amazonaws.lambda.feature.integrationmodel="RuntimeAPI" \
      com.amazonaws.lambda.feature.managedinstances="Supported"
```

## Image requirements and best practices
<a name="cmr-building-images-best-practices"></a>

Follow these requirements and best practices when you build and store runtime images.

Do the following:
+ **Include the required paths** – Make sure that the image contains the `/etc/hosts` and `/etc/resolv.conf` files and the `/var/task` directory. Lambda base images include them. For more information, see [Required paths](#cmr-building-images-required-paths).
+ **Stay within the size limit** – For the maximum size of a runtime image, see [Customer-managed runtimes](gettingstarted-limits.md#cmr-quotas) in [Lambda quotas](gettingstarted-limits.md).
+ **Keep images small** – Include only what functions need. Smaller images help reduce cold start times. Lambda caches runtime images that many functions share, so speed improves with use.
+ **Store images in the same AWS Region** – Push the image to an Amazon ECR repository in the same Region as the runtime. The repository can be in a different AWS account. To use the runtime in other Regions, replicate the image to each Region. For more information, see [Deploying runtimes in multiple Regions](cmr-multi-region.md).
+ **Keep images while runtime versions exist** – You must keep the image in Amazon ECR for as long as any runtime version uses the image. If you delete the image, functions that use a runtime version based on the image become `Inactive`. This change can take up to 24 hours. Existing execution environments continue to handle invocations, but invocations that require a cold start fail. Deleting the repository or removing Lambda's access to the image has the same effect. The functions recover automatically after you restore the image. A runtime version refers to the image by digest (`ResolvedUri`), so the restored image must have an identical digest. Standard Amazon ECR storage rates apply. For more information, see [Runtime versions](cmr-versions.md).
+ **Use unique tags or digests** – Give each build a unique tag, or refer to images by digest. When you create a runtime version, Lambda resolves the tag to a digest. Retagging an image later doesn't change the runtime version.
+ **Patch regularly** – You're responsible for patching every part of the image. Rebuild it often to include security fixes, and publish a new runtime version. If you use a Lambda base image, rebuild to get its updates. For more information, see [Deploying runtime updates](cmr-deploy-updates.md).
+ **Test images locally** – Test your runtime with sample functions before you publish a runtime version.
+ **Document your runtime** – Tell your runtime consumers the handler format, what the runtime includes, what it supports, and which runtime aliases they can use.

Don't do the following:
+ **Don't include secrets** – Don't put passwords, keys, tokens, or other sensitive settings in a runtime image, including in environment variables. For more information, see [What goes into a runtime image](#cmr-building-images-components).
+ **Don't use reserved directories** – Don't put anything in `/opt` or `/var/task`. Lambda uses these directories for layers and function code. The image must still contain the `/var/task` directory, so create it, but leave it empty.
+ **Don't rely on retagging** – Moving a tag to a new image doesn't change a runtime version. To update a runtime, publish a new runtime version and update your runtime aliases.
+ **Don't delete images that runtime versions use** – Delete an image only after Lambda permanently deletes every runtime version that uses the image. A runtime version that is scheduled for deletion still needs the image, so that you can restore the version. For more information, see [Container images and charges](cmr-delete.md#cmr-delete-ecr).

## Next steps
<a name="cmr-building-images-next-steps"></a>

To build your runtime image, see the following topics:
+ To start from a Lambda base image, see [Building a runtime image from a Lambda base image](cmr-base-images.md).
+ To build from scratch with a Lambda runtime interface client, see [Building runtime images from scratch](cmr-images-from-scratch.md).
+ To support a new language with your own runtime interface client, see [Supporting a new programming language for AWS Lambda Event Functions](runtimes-custom.md).

After you build and push your image, continue with the following topics:
+ To create a runtime, see [Creating a runtime](cmr-create.md).
+ To publish your image as a runtime version, see [Runtime versions](cmr-versions.md).
+ For an overview of customer-managed runtimes, see [Customer-managed runtimes](runtimes-customer-managed.md).