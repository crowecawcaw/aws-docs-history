# Using the Ruby platform

###### Important

App Runner will end the support for **Ruby 3.1** on December 1, 2025.
For recommendations and more information, see [End of support for managed runtime versions](service-source-code.md#service-source-code.managed-platforms.eos "service-source-code.md#service-source-code.managed-platforms.eos").

The AWS App Runner Ruby platform provides managed runtimes. Each runtime makes it easy to build and run containers with web applications based on a Ruby
version. When you use a Ruby runtime, App Runner starts with a managed Ruby runtime image. This image is based on the [Amazon Linux Docker image](https://hub.docker.com/_/amazonlinux "https://hub.docker.com/_/amazonlinux") and contains the runtime package for a version of Ruby and some tools. App Runner uses this
managed runtime image as a base image, and adds your application code to build a Docker image. It then deploys this image to run your web service in a
container.

You specify a runtime for your App Runner service when you [create a service](manage-create.md "manage-create.md") using the App Runner console or the [CreateService](../api/API_CreateService.md "../api/API_CreateService.md") API operation. You can also specify a runtime as part of your source code. Use the
`runtime` keyword in a [App Runner configuration file](config-file.md "config-file.md") that you include in your code repository.
The naming convention of a managed runtime is `<language-name><major-version>`.

For valid Ruby runtime names and versions, see [Ruby runtime release information](service-source-code-ruby-releases.md "service-source-code-ruby-releases.md").

App Runner updates the runtime for your service to the latest version on every deployment or service update. If your application requires a specific version of
a managed runtime, you can specify it using the `runtime-version` keyword in the [App Runner configuration file](config-file.md "config-file.md"). You
can lock to any level of version, including a major or minor version. App Runner only makes lower-level updates to the runtime of your service.

Version syntax for Ruby runtimes:
``major`[.`minor`[.`patch`]]`

For example: `3.1.2`

The following examples demonstrate version locking:

- `3.1` – Lock the major and minor versions. App Runner updates only patch versions.
- `3.1.2` – Lock to a specific patch version. App Runner doesn't update your runtime version.

###### Topics

- [Ruby runtime configuration](#service-source-code-ruby.config "#service-source-code-ruby.config")
- [Ruby runtime examples](#service-source-code-ruby.examples "#service-source-code-ruby.examples")
- [Ruby runtime release information](service-source-code-ruby-releases.md "service-source-code-ruby-releases.md")

## Ruby runtime configuration

When you choose a managed runtime, you must also configure, as a minimum, build and run commands. You configure them while [creating](manage-create.md "manage-create.md") or [updating](manage-configure.md "manage-configure.md") your App Runner service. You can do this using one of the following methods:

- Using the App Runner console – Specify the commands in the **Configure build** section of the
  creation process or configuration tab.
- Using the App Runner API – Call the [CreateService](../api/API_CreateService.md "../api/API_CreateService.md") or [UpdateService](../api/API_UpdateService.md "../api/API_UpdateService.md") API operation. Specify the commands using the `BuildCommand` and
  `StartCommand` members of the [CodeConfigurationValues](../api/API_CodeConfigurationValues.md "../api/API_CodeConfigurationValues.md") data type.
- Using a [configuration file](config-file.md "config-file.md") – Specify one or more build commands in up to
  three build phases, and a single run command that serves to start your application. There are additional optional configuration settings.

Providing a configuration file is optional. When you create an App Runner service using the console or the API, you specify if App Runner gets your configuration
settings directly when it's created or from a configuration file.

## Ruby runtime examples

The following examples show App Runner configuration files for building and running a Ruby service.

This example shows a minimal configuration file that you can use with a Ruby managed runtime. For the assumptions that App Runner makes with a minimal
configuration file, see [Configuration file examples](config-file-examples.md#config-file-examples.managed "config-file-examples.md#config-file-examples.managed").

###### Example apprunner.yaml

```
version: 1.0
runtime: ruby31
build:
  commands:
    build:
      - bundle install
run:
  command: bundle exec rackup --host 0.0.0.0 -p 8080
```

This example shows the use of all the configuration keys with a Ruby managed runtime.

###### Note

The runtime version that's used in these examples is `3.1.2`. You can replace it with a version you want to use. For
latest supported Ruby runtime version, see [Ruby runtime release information](service-source-code-ruby-releases.md "service-source-code-ruby-releases.md").

###### Example apprunner.yaml

```
version: 1.0
runtime: ruby31
build:
  commands:
     pre-build:
      - scripts/prebuild.sh
    build:
      - bundle install
    post-build:
      - scripts/postbuild.sh
  env:
    - name: MY_VAR_EXAMPLE
      value: "example"
run:
  runtime-version: `3.1.2`
  command: bundle exec rackup --host 0.0.0.0 -p 4567
  network:
    port: 4567
    env: APP_PORT
  env:
    - name: MY_VAR_EXAMPLE
      value: "example"
```

These examples shows the source code for a complete Ruby application that you can deploy to a Ruby runtime service.

###### Example server.rb

```
# server.rb
require 'sinatra'

get '/' do
  'Hello World!'
end
```

###### Example config.ru

```
# config.ru

require './server'

run Sinatra::Application
```

###### Example Gemfile

```
# Gemfile
source 'https://rubygems.org (https://rubygems.org/)'

gem 'sinatra'
gem 'puma'
```

###### Example apprunner.yaml

```
version: 1.0
runtime: ruby31
build:
  commands:
    build:
      - bundle install
run:
  command: bundle exec rackup --host 0.0.0.0 -p 4567
  network:
    port: 4567
    env: APP_PORT
```
