# App Runner service based on source code

You can use AWS App Runner to create and manage services based on two fundamentally different
types of service source: _source code_ and _source image_.
Regardless of the source type, App Runner takes care of starting, running, scaling, and load balancing
your service. You can use the CI/CD capability of App Runner to track changes to your source image or
code. When App Runner discovers a change, it automatically builds (for source code) and deploys the
new version to your App Runner service.

This chapter discusses services based on source code. For information about services based
on a source image, see [App Runner service based on a source image](service-source-image.md "service-source-image.md").

Source code is application code that App Runner builds and deploys for you. You point App Runner to a
[source directory](#service-source-code.source-directory "#service-source-code.source-directory") in a code
repository and choose a suitable _runtime_ that corresponds to a programming
platform version. App Runner builds an image that's based on the base image of the runtime and your
application code. It then starts a service that runs a container based on this image.

App Runner provides convenient platform-specific _managed runtimes_. Each one of
these runtimes builds a container image from your source code, and adds language runtime
dependencies into your image. You don't need to provide container configuration and build
instructions such as a Dockerfile.

Subtopics of this chapter discuss the various platforms that App Runner supports—
_managed platforms_ that provide managed runtimes for different programming
environments and versions.

###### Topics

- [Source code repository providers](#service-source-code.providers "#service-source-code.providers")
- [Source directory](#service-source-code.source-directory "#service-source-code.source-directory")
- [App Runner managed platforms](#service-source-code.managed-platforms "#service-source-code.managed-platforms")
- [End of support for managed runtime versions](#service-source-code.managed-platforms.eos "#service-source-code.managed-platforms.eos")
- [Managed runtime versions and the App Runner build](#service-source-code.build-detail "#service-source-code.build-detail")
- [Using the Python platform](service-source-code-python.md "service-source-code-python.md")
- [Using the Node.js platform](service-source-code-nodejs.md "service-source-code-nodejs.md")
- [Using the Java platform](service-source-code-java.md "service-source-code-java.md")
- [Using the .NET platform](service-source-code-net6.md "service-source-code-net6.md")
- [Using the PHP platform](service-source-code-php.md "service-source-code-php.md")
- [Using the Ruby platform](service-source-code-ruby.md "service-source-code-ruby.md")
- [Using the Go platform](service-source-code-go1.md "service-source-code-go1.md")

## Source code repository providers

App Runner deploys your source code by reading it from a source code repository. App Runner supports
two source code repository providers: [GitHub](https://github.com/ "https://github.com/") and [Bitbucket](https://bitbucket.org/ "https://bitbucket.org/").

### Deploying from your source code repository provider

To deploy your source code to an App Runner service from a source code repository, App Runner
establishes a connection to it. When you use the App Runner console to [create a service](manage-create.md "manage-create.md"), you provide connection details and a
source directory for App Runner to deploy your source code.

###### Connections

You provide connection details as part of the service creation procedure. When you use
the App Runner API or the AWS CLI, a connection is a separate resource. First, you create the
connection using the [CreateConnection](../api/API_CreateConnection.md "../api/API_CreateConnection.md") API action. Then, you provide the connection's ARN during
service creation using the [CreateService](../api/API_CreateService.md "../api/API_CreateService.md") API action.

###### Source directory

When you create a service you also provide a source directory. By default, App Runner uses
the root directory of your repository as the source directory. The source directory is the
location in your source code repository that stores your application’s source code and
configuration files. The build and start commands also execute from the source directory.
When you use the App Runner API or the AWS CLI to create or update a service you provide the
source directory in the [CreateService](../api/API_CreateService.md "../api/API_CreateService.md") and [UpdateService](../api/API_UpdateService.md "../api/API_UpdateService.md") API actions. For more information, see the [Source directory](#service-source-code.source-directory "#service-source-code.source-directory") section that follows.

For more information about App Runner service creation, see [Creating an App Runner service](manage-create.md "manage-create.md").
For more information about App Runner connections, see [Managing App Runner connections](manage-connections.md "manage-connections.md").

## Source directory

When you create an App Runner service you can provide the source directory, along with the
repository and branch. Set the value of the **Source directory** field to the
repository directory path that stores the application’s source code and configuration files.
App Runner executes the build and start commands from the source directory path that you
provide.

Enter the value for source directory path as absolute from the root repository directory.
If you don’t specify a value, it defaults to the repository top-level directory, also known as
the repository root directory.

You also have the option to provide different source directory paths besides the top-level
repository directory. This supports a monorepo repository architecture, which means the source
code for multiple applications is stored in one repository. To create and support multiple
App Runner services from a single monorepo, specify different source directories when you create
each service.

###### Note

If you specify the same source directory for multiple App Runner services, both services will
deploy and operate individually.

If you opt to use an `apprunner.yaml` configuration file to define your
service parameters place it in the source directory folder of the repository.

If the **Deployment trigger** option is set to the **Automatic**, the changes you commit in the source directory will
trigger an automatic deployment. _Only the changes in the source directory_
path will trigger an automatic deployment. It’s important to understand how the location of
the source directory affects the scope of an automatic deployment. For more information, see
_automated deployments_ in [Deployment methods](manage-deploy.md#manage-deploy.methods "manage-deploy.md#manage-deploy.methods").

###### Note

If your App Runner service uses the PHP managed runtimes, and you'd like to designate a source
directory other than the default root repository, it's important to use the correct PHP
runtime version. For more information, see [Using the PHP platform](service-source-code-php.md "service-source-code-php.md").

## App Runner managed platforms

App Runner managed platforms provide managed runtimes for various programming environments. Each
managed runtime makes it easy to build and run containers based on a version of a programming
language or runtime environment. When you use a managed runtime, App Runner starts with a managed
runtime image. This image is based on the [Amazon Linux Docker image](https://hub.docker.com/_/amazonlinux "https://hub.docker.com/_/amazonlinux") and contains a language runtime package as well as some tools and
popular dependency packages. App Runner uses this managed runtime image as a base image, and adds
your application code to build a Docker image. It then deploys this image to run your web
service in a container.

You specify a runtime for your App Runner service when you [create a service](manage-create.md "manage-create.md") using the App Runner console or the [CreateService](../api/API_CreateService.md "../api/API_CreateService.md") API operation. You can also specify a runtime as part of your source code. Use the
`runtime` keyword in a [App Runner configuration file](config-file.md "config-file.md") that you include in your code repository.
The naming convention of a managed runtime is `<language-name><major-version>`.

App Runner updates the runtime for your service to the latest version on every deployment or service update. If your application requires a specific version of
a managed runtime, you can specify it using the `runtime-version` keyword in the [App Runner configuration file](config-file.md "config-file.md"). You
can lock to any level of version, including a major or minor version. App Runner only makes lower-level updates to the runtime of your service.

## End of support for managed runtime versions

When the official provider or community of a managed language runtime officially declares
a version to be End of Life (EOL), App Runner follows by declaring the version status to be
_End of Support_. If your service is running on a managed language
runtime version that has reached End of Support the following policies and recommendations
apply.

**End of Support for a language runtime version:**

- **Existing services** will continue to run and serve
  traffic even if they use a runtime that has reached End of Support. However, they will run
  on unsupported runtimes that no longer receive updates, security patches, or technical
  support.
- **Updates to existing services** that use End of Support
  runtimes are still allowed, but we do not recommend continued use of End of Support
  runtimes for a service.
- **New services** cannot be created using the runtimes
  that have reached the End of Support date.

**Actions Required for language runtime versions with End of Support
status:**

- If your service is **based on a source image**, no
  further action is required on your part for that service.
- If your service is **based on source code**, update your
  service configuration to use a supported runtime version. To do so, select a supported
  runtime version in the [App Runner console](https://console.aws.amazon.com/apprunner "https://console.aws.amazon.com/apprunner"),
  update the `runtime` field in the [apprunner.yaml](config-file.md "config-file.md") configuration file, or use the [CreateService](../api/API_CreateService.md "../api/API_CreateService.md")/[UpdateService](../api/API_UpdateService.md "../api/API_UpdateService.md") API operations or IaC
  tools to set the `runtime` parameter. For a list of supported runtimes, see the
  _Release information_ page for any specific runtime in this
  chapter.
- Alternatively, you can switch to App Runner’s **container image
  source** option. For more details, see [Image-based service](service-source-image.md "service-source-image.md").

###### Note

If you’re moving from Node.js 12, 14, or 16 to **Node.js
22**, or from Python 3.7 or 3.8 to **Python 3.11**,
be aware that Node.js 22 and Python 3.11 use a revised App Runner build process that offers faster
and more efficient builds. To ensure compatibility before upgrading we recommend that you
review the [build process guidance](#service-source-code.build-detail "#service-source-code.build-detail") in
the next section.

The following tables lists the App Runner managed runtime versions that have a designated End of
Support date.

| **Runtime Versions**                                                                                                | **App Runner End of Support date** |
| ------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| Python 3.8 [Supported<br>runtimes](service-source-code-python-releases.md "service-source-code-python-releases.md") | December 1, 2025                   |
| Python 3.7 [Supported<br>runtimes](service-source-code-python-releases.md "service-source-code-python-releases.md") | December 1, 2025                   |
| Node.js 18 [Supported<br>runtimes](service-source-code-nodejs-releases.md "service-source-code-nodejs-releases.md") | December 1, 2025                   |
| Node.js 16 [Supported<br>runtimes](service-source-code-nodejs-releases.md "service-source-code-nodejs-releases.md") | December 1, 2025                   |
| Node.js 14 [Supported<br>runtimes](service-source-code-nodejs-releases.md "service-source-code-nodejs-releases.md") | December 1, 2025                   |
| Node.js 12 [Supported<br>runtimes](service-source-code-nodejs-releases.md "service-source-code-nodejs-releases.md") | December 1, 2025                   |
| .NET 6 \*                                                                                                           | December 1, 2025                   |
| PHP 8.1 \*                                                                                                          | December 31, 2025                  |
| Ruby 3.1 \*                                                                                                         | December 1, 2025                   |
| Go 1 \*                                                                                                             | December 1, 2025                   |

**\*** App Runner will not release any new language versions for the
runtimes marked with an asterisk (\*). These runtimes are the following: .NET, PHP, Ruby, and
Go. If you have a code-based service configured for these runtimes, we recommend one of the
following actions:

- If applicable, switch your service configuration to a different supported managed
  runtime.
- Alternatively, build a custom container image with your preferred runtime version and
  deploy it using App Runner’s [Image-based service](service-source-image.md "service-source-image.md") option. You can host your image in
  Amazon ECR.

## Managed runtime versions and the App Runner build

App Runner offers an updated build process for applications that run on the more recent major
version runtimes. This revised build process is faster and more efficient. It also creates a
final image with a smaller footprint that only contains your source code, build artifacts, and
runtimes needed to run your application.

We refer to the newer build process as the _revised App Runner build_ and to the original build process as the*original App Runner build*. To avoid breaking changes to earlier version of runtime platforms,
App Runner only applies the revised build to specific runtime versions, typically newly
released major releases.

We’ve introduced a new component to the `apprunner.yaml`
configuration file to make the revised build backward compatible for a very specific use
case and to also provide more flexibility to configure the build of your application. This is
the optional [pre-run](config-file-ref.md#config-file-ref.run "config-file-ref.md#config-file-ref.run") parameter. We
explain when to use this parameter along with other useful information about the builds in the
sections that follow.

The following table conveys which version of the App Runner build applies to specific managed
runtime versions. We'll continue to update this document to keep you informed about our
current runtimes.

| **Platform**                                                                                                        | **Runtime Versions** | **Build process** | **App Runner End of Support date** |
| ------------------------------------------------------------------------------------------------------------------- | -------------------- | ----------------- | ---------------------------------- |
| Python – [Release information](service-source-code-python-releases.md "service-source-code-python-releases.md")     | Python 3.11 (!)      | Revised           |                                    |
| Python 3.8                                                                                                          | Original             | December 1, 2025  |
| Python 3.7                                                                                                          | Original             | December 1, 2025  |
| Node.js – [Release<br>information](service-source-code-nodejs-releases.md "service-source-code-nodejs-releases.md") | Node.js 22           | Revised           |                                    |
| Node.js 18                                                                                                          | Revised              | December 1, 2025  |
| Node.js 16                                                                                                          | Original             | December 1, 2025  |
| Node.js 14                                                                                                          | Original             | December 1, 2025  |
| Node.js 12                                                                                                          | Original             | December 1, 2025  |
| Corretto – [Release information](service-source-code-java-releases.md "service-source-code-java-releases.md")       | Corretto 11          | Original          |                                    |
| Corretto 8                                                                                                          | Original             |                   |
| .NET – [Release information](service-source-code-dotnet-releases.md "service-source-code-dotnet-releases.md")       | .NET 6 \*            | Original          | December 1, 2025                   |
| PHP – [Release information](service-source-code-php-releases.md "service-source-code-php-releases.md")              | PHP 8.1 \*           | Original          | December 31, 2025                  |
| Ruby – [Release information](service-source-code-ruby-releases.md "service-source-code-ruby-releases.md")           | Ruby 3.1 \*          | Original          | December 1, 2025                   |
| Go – [Release information](service-source-code-go-releases.md "service-source-code-go-releases.md")                 | Go 1 \*              | Original          | December 1, 2025                   |

###### Note

Some of the listed runtimes include an **End of Support**
date. For more information, see [End of support for managed runtime versions](#service-source-code.managed-platforms.eos "#service-source-code.managed-platforms.eos").

###### Important

**Python 3.11** – We have specific recommendations
for the build configuration of services that use the Python 3.11 managed runtime. For more
information, see [Callouts for specific runtime versions](service-source-code-python.md#service-source-code-python.callouts "service-source-code-python.md#service-source-code-python.callouts") in the _Python
platform_ topic.

### More about the App Runner builds and migration

When you migrate your application to a newer runtime that uses the revised build,
you may need to slightly modify your build configuration.

To provide context for migration considerations, we'll first describe the high level
processes for both the original App Runner build and the revised build. We'll follow with a
section that describes specific attributes about your service that might require some
configuration updates.

#### The original App Runner build

The original App Runner application build process leverages the AWS CodeBuild service. The
initial steps are based on images curated by the CodeBuild service. A Docker build process
follows that uses the applicable App Runner managed runtime image as the base image.

The general steps are the following:

1. Run `pre-build` commands in a CodeBuild-curated image.

The `pre-build` commands are optional. They can only be
specified in the `apprunner.yaml` configuration file. 2. Run the `build` commands using CodeBuild on the same image from the
prior step.

The `build` commands are required. They can be specified in the
App Runner console, the App Runner API, or in the `apprunner.yaml`
configuration file. 3. Run a Docker build to generate an image based on the App Runner managed runtime image
for your specific platform and runtime version. 4. Copy the `/app` directory from the image that we generated in
**Step 2**. The destination is the image based on the
App Runner managed runtime image, that we generated in **Step
3**. 5. Run the `build` commands again on the generated App Runner managed
runtime image. We run the build commands again to generate build artifacts from the
source code in the `/app` directory that we copied to it in
**Step 4**. This image will later be deployed by App
Runner to run your web service in a container.

The `build` commands are required. They can be specified in the
App Runner console, the App Runner API, or in the `apprunner.yaml`
configuration file. 6. Run `post-build` commands in the CodeBuild image from **Step 2**.

The `post-build` commands are optional. They can only be
specified in the `apprunner.yaml` configuration file.

After the build completes, App Runner deploys the generated App Runner managed runtime image from
**Step 5** to run your web service in a container.

#### The revised App Runner build

The revised build process is faster and more efficient than the original build process
described in the prior section. It eliminates the duplication of the build commands that
occurs in the prior version build. It also creates a final image with a smaller footprint
that only contains your source code, build artifacts, and runtimes needed to run your
application.

This build process uses a Docker multi-stage build. The general process steps are the
following:

1.  Build stage — Start a docker build process
    that executes `pre-build` and `build` commands
    on top of the App Runner build images.
    1. Copy the application source code to the `/app`
       directory.

    ###### Note

    This `/app` directory is designated as the working
    directory in every stage of the Docker build. 2. Run `pre-build` commands.

    The`pre-build` commands are optional. They can only be
    specified in the `apprunner.yaml` configuration
    file. 3. Run the `build` commands.

    The `build` commands are required. They can be specified in
    the App Runner console, the App Runner API, or in the
    `apprunner.yaml` configuration file.

2.  Packaging stage — Generates the final
    customer container image, which is also based on the App Runner run image.
    1. Copy the `/app` directory from the prior **Build stage** to the new Run image. This includes your
       application source code and the build artifacts from the prior stage.
    2. Run the `pre-run` commands. If you need to modify the runtime image
       outside of the `/app` directory by using the `build`
       commands, add the same or required commands to this segment of the
       `apprunner.yaml` configuration file.

    This is a new parameter that was introduced to support the
    revised App Runner build.

    The `pre-run` commands are optional. They can only be specified in
    the `apprunner.yaml` configuration file.

    ###### Notes

        * The `pre-run` commands are only supported by the
         revised build. Do not add them to the configuration file if your
         service uses runtime versions that use the original build.
        * If you don't need to modify anything outside of the
         `/app` directory with the `build` commands,
         then you don’t need to specify `pre-run` commands.

3.  Post-build stage — This stage resumes from
    the _Build stage_ and runs `post-build`
    commands.
    1. Run the `post-build` commands inside the
       `/app` directory.

    The `post-build` commands are optional. They can only be
    specified in the `apprunner.yaml` configuration
    file.

After the build completes, App Runner then deploys the Run image to run your web service in
a container.

###### Note

Don’t be misled to the `env` entries in the Run section of the
`apprunner.yaml` when configuring the build process. Even
though the `pre-run` command parameter, referenced in **Step 2(b)**, resides in the Run section, don't use the `env`
parameter in the Run section to configure your build. The `pre-run` commands
only reference the `env` variables defined in the Build section of the
configuration file. For more information, see [Run section](config-file-ref.md#config-file-ref.run "config-file-ref.md#config-file-ref.run") in the _App Runner configuration file
chapter_.

#### Service requirements for migration consideration

If your application environment has either of these two requirements, then you'll need
to revise your build configuration, by adding `pre-run` commands.

- If you need to modify anything outside of the `/app` directory
  with the `build` commands.
- If you need to run the `build` commands twice to create the required
  environment. This is a very unusual requirement. The vast majority of builds will not
  do this.

**Modifications outside the `/app`
directory**

- The [revised App Runner build](#service-source-code.build-detail.v2 "#service-source-code.build-detail.v2")
  assumes that your application does not have dependencies outside the
  `/app` directory.
- The commands that you provide either with the
  `apprunner.yaml` file, the App Runner API, or the App Runner console
  must generate build artifacts in the `/app` directory.
- You can modify the `pre-build`, `build`, and
  `post-build` commands to ensure all the build artifacts are in
  the `/app` directory.
- If your application requires the build to further modify the generated image for
  your service, outside of the `/app` directory, you can use the new
  `pre-run` commands in the
  `apprunner.yaml`. For more information, see [Setting App Runner service options using a configuration file](config-file.md "config-file.md").

**Running the `build` commands
twice**

- The [original App Runner build](#service-source-code.build-detail.v1 "#service-source-code.build-detail.v1") runs
  the `build` commands twice, first in **Step
  2**, then again in **Step 5**. The
  revised App Runner build remedies this redundancy and only runs the `build` commands
  one time. If your application should have an unusual requirement for the
  `build` commands to run twice, the revised App Runner build provides the option to
  specify and execute the same commands again using the `pre-run`
  parameter. Doing so retains the same double build behavior.
