# Using the .NET platform

###### Important

App Runner will end the support for **.NET 6** on December 1, 2025.
For recommendations and more information, see [End of support for managed runtime versions](service-source-code.md#service-source-code.managed-platforms.eos "service-source-code.md#service-source-code.managed-platforms.eos").

The AWS App Runner .NET platform provides managed runtimes. Each runtime makes it easy to build
and run containers with web applications based on a .NET version. When you use a .NET runtime,
App Runner starts with a managed .NET runtime image. This image is based on the [Amazon Linux Docker image](https://hub.docker.com/_/amazonlinux "https://hub.docker.com/_/amazonlinux") and contains the runtime
package for a version of .NET and some tools and popular dependency packages. App Runner uses this
managed runtime image as a base image, and adds your application code to build a Docker image.
It then deploys this image to run your web service in a container.

You specify a runtime for your App Runner service when you [create a service](manage-create.md "manage-create.md") using the App Runner console or the [CreateService](../api/API_CreateService.md "../api/API_CreateService.md") API operation. You can also specify a runtime as part of your source code. Use the
`runtime` keyword in a [App Runner configuration file](config-file.md "config-file.md") that you include in your code repository.
The naming convention of a managed runtime is `<language-name><major-version>`.

For valid .NET runtime names and versions, see [.NET runtime release information](service-source-code-dotnet-releases.md "service-source-code-dotnet-releases.md").

App Runner updates the runtime for your service to the latest version on every deployment or service update. If your application requires a specific version of
a managed runtime, you can specify it using the `runtime-version` keyword in the [App Runner configuration file](config-file.md "config-file.md"). You
can lock to any level of version, including a major or minor version. App Runner only makes lower-level updates to the runtime of your service.

Version syntax for .NET runtimes:
``major`[.`minor`[.`patch`]]`

For example: `6.0.9`

The following examples demonstrate version locking:

- `6.0` – Lock the major and minor versions. App Runner updates only patch
  versions.
- `6.0.9` – Lock to a specific patch version. App Runner doesn't update your
  runtime version.

###### Topics

- [.NET runtime configuration](#service-source-code-net6.config "#service-source-code-net6.config")
- [.NET runtime examples](#service-source-code-net6.examples "#service-source-code-net6.examples")
- [.NET runtime release information](service-source-code-dotnet-releases.md "service-source-code-dotnet-releases.md")

## .NET runtime configuration

When you choose a managed runtime, you must also configure, as a minimum, build and run commands. You configure them while [creating](manage-create.md "manage-create.md") or [updating](manage-configure.md "manage-configure.md") your App Runner service. You can do this using one of the following methods:

- Using the App Runner console – Specify the commands in the **Configure build** section of the
  creation process or configuration tab.
- Using the App Runner API – Call the [CreateService](../api/API_CreateService.md "../api/API_CreateService.md") or [UpdateService](../api/API_UpdateService.md "../api/API_UpdateService.md") API operation. Specify the commands using the `BuildCommand` and
  `StartCommand` members of the [CodeConfigurationValues](../api/API_CodeConfigurationValues.md "../api/API_CodeConfigurationValues.md") data type.
- Using a [configuration file](config-file.md "config-file.md") – Specify one or more build commands in up to
  three build phases, and a single run command that serves to start your application. There are additional optional configuration settings.

Providing a configuration file is optional. When you create an App Runner service using the console or the API, you specify if App Runner gets your configuration
settings directly when it's created or from a configuration file.

## .NET runtime examples

The following examples show App Runner configuration files for building and running a .NET
service. The last example is the source code for a complete .NET application that you can
deploy to a .NET runtime service.

###### Note

The runtime version that's used in these examples is `6.0.9`.
You can replace it with a version you want to use. For latest supported .NET runtime
version, see [.NET runtime release information](service-source-code-dotnet-releases.md "service-source-code-dotnet-releases.md").

This example shows a minimal configuration file that you can use with a .NET managed
runtime. For the assumptions that App Runner makes with a minimal configuration file, see [Configuration file examples](config-file-examples.md#config-file-examples.managed "config-file-examples.md#config-file-examples.managed").

###### Example apprunner.yaml

```
version: 1.0
runtime: dotnet6
build:
  commands:
    build:
      - dotnet publish -c Release -o out
run:
  command: dotnet out/HelloWorldDotNetApp.dll
```

This example shows the use of all configuration keys with a .NET managed
runtime.

###### Note

The runtime version that's used in these examples is
`6.0.9`. You can replace it with a version you want to use.
For latest supported .NET runtime version, see [.NET runtime release information](service-source-code-dotnet-releases.md "service-source-code-dotnet-releases.md").

###### Example apprunner.yaml

```
version: 1.0
runtime: dotnet6
build:
  commands:
    pre-build:
      - scripts/prebuild.sh
    build:
      - dotnet publish -c Release -o out
    post-build:
      - scripts/postbuild.sh
  env:
    - name: MY_VAR_EXAMPLE
      value: "example"
run:
  runtime-version: `6.0.9`
  command: dotnet out/HelloWorldDotNetApp.dll
  network:
    port: 5000
    env: APP_PORT
  env:
    - name: ASPNETCORE_URLS
      value: "http://*:5000"
```

This example shows the source code for a complete .NET application that you can deploy
to a .NET runtime service.

###### Note

- Run following command to create a simple .NET 6 web app: `dotnet new web
--name HelloWorldDotNetApp -f net6.0`
- Add the `apprunner.yaml` to the created .NET 6 web app.

###### Example HelloWorldDotNetApp

```
version: 1.0
runtime: dotnet6
build:
  commands:
    build:
      - dotnet publish -c Release -o out
run:
  command: dotnet out/HelloWorldDotNetApp.dll
  network:
    port: 5000
    env: APP_PORT
  env:
    - name: ASPNETCORE_URLS
      value: "http://*:5000"
```
